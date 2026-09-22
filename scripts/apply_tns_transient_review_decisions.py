#!/usr/bin/env python3
"""Apply curated TNS review decisions to the transient runtime source."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REVIEW_DIR = Path("outputs/transients/review")
DEFAULT_DECISIONS_PATH = DEFAULT_REVIEW_DIR / "transient-review-decisions-v1.json"
DEFAULT_DECISIONS_MARKDOWN_PATH = DEFAULT_REVIEW_DIR / "transient-review-decisions-v1.md"
DEFAULT_RUNTIME_PATH = Path("outputs/transients/runtime/transient_opportunities_v1.json")
ALLOWED_STATUSES = {"pending", "approved", "hold", "rejected"}


class DecisionError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Synchronize the TNS decision registry and build the runtime source from "
            "all still-active approved decisions."
        )
    )
    parser.add_argument("--review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS_PATH)
    parser.add_argument(
        "--decisions-markdown",
        type=Path,
        default=DEFAULT_DECISIONS_MARKDOWN_PATH,
    )
    parser.add_argument("--runtime", type=Path, default=DEFAULT_RUNTIME_PATH)
    parser.add_argument("--generated-at", help="UTC ISO-8601 generation time")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when checked-in decisions or runtime output differ from generated output.",
    )
    return parser.parse_args()


def repo_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO_ROOT / path


def read_optional_json(path: Path) -> dict[str, Any] | None:
    absolute = repo_path(path)
    if not absolute.exists():
        return None
    with absolute.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def json_text(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=True) + "\n"


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_datetime(value: Any) -> dt.datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        parsed = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.UTC)
    return parsed.astimezone(dt.UTC)


def candidate_material(candidate: dict[str, Any]) -> dict[str, Any]:
    material = copy.deepcopy(candidate)
    material.pop("reviewDecision", None)
    material.get("provenance", {}).pop("inputRecords", None)
    material.get("enrichment", {}).pop("retrievedAtUTC", None)
    return material


def evidence_hash(candidate: dict[str, Any]) -> str:
    encoded = json.dumps(
        candidate_material(candidate),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def runtime_evidence_hash(opportunity: dict[str, Any]) -> str:
    encoded = json.dumps(
        opportunity,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return f"legacy-runtime-{hashlib.sha256(encoded).hexdigest()[:16]}"


def load_review_queues(review_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    absolute = repo_path(review_dir)
    queues: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(absolute.glob("transient-review-*.json")):
        if path.name == DEFAULT_DECISIONS_PATH.name:
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("reviewOnly") is not True or payload.get("family") != "transientOpportunities":
            raise DecisionError(f"Invalid TNS review queue: {path}")
        queues.append((path, payload))
    if not queues:
        raise DecisionError(f"No TNS review queues found in {absolute}")
    return queues


def latest_candidates(
    queues: list[tuple[Path, dict[str, Any]]],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], str, str]:
    candidates: dict[str, dict[str, Any]] = {}
    provenance: dict[str, dict[str, Any]] = {}
    latest_as_of = ""
    latest_generated_at = ""
    for path, queue in queues:
        as_of = str(queue.get("asOfDate") or "")
        generated_at = str(queue.get("generatedAtUTC") or "")
        latest_as_of = max(latest_as_of, as_of)
        latest_generated_at = max(latest_generated_at, generated_at)
        for candidate in queue.get("opportunities") or []:
            candidate_id = str(candidate.get("id") or "").strip()
            if not candidate_id:
                raise DecisionError(f"Review candidate in {path} is missing id")
            existing = candidates.get(candidate_id)
            existing_modified = str((existing or {}).get("lastModifiedUTC") or "")
            candidate_modified = str(candidate.get("lastModifiedUTC") or "")
            existing_queue_date = str((provenance.get(candidate_id) or {}).get("asOfDate") or "")
            if existing is None or (candidate_modified, as_of) >= (existing_modified, existing_queue_date):
                candidates[candidate_id] = candidate
                provenance[candidate_id] = {
                    "sourceReviewQueue": path.name,
                    "reviewSetID": queue.get("reviewSetID"),
                    "asOfDate": as_of,
                }
    return candidates, provenance, latest_as_of, latest_generated_at


def seed_legacy_decisions(runtime: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    for opportunity in (runtime or {}).get("opportunities") or []:
        candidate_id = str(opportunity.get("id") or "").strip()
        if not candidate_id:
            continue
        review = opportunity.get("review") or {}
        decisions[candidate_id] = {
            "id": candidate_id,
            "status": "approved",
            "evidenceHash": runtime_evidence_hash(opportunity),
            "sourceReviewQueue": review.get("sourceReviewQueue") or "legacy-runtime",
            "reviewSetID": review.get("reviewSetID"),
            "recommendedDecision": "approve",
            "lastSeenAsOfDate": (runtime or {}).get("asOfDate"),
            "decidedBy": review.get("approvedBy") or "project-owner",
            "decidedAtUTC": review.get("approvedAtUTC") or (runtime or {}).get("generatedAtUTC"),
            "note": "Imported from the previously published curator-approved runtime feed.",
        }
    return decisions


def existing_decisions(payload: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if payload is None:
        return {}
    if payload.get("schemaVersion") != 1 or payload.get("family") != "tnsTransientReviewDecisions":
        raise DecisionError("Decision registry must use tnsTransientReviewDecisions schemaVersion 1")
    decisions: dict[str, dict[str, Any]] = {}
    for decision in payload.get("decisions") or []:
        candidate_id = str(decision.get("id") or "").strip()
        if not candidate_id or candidate_id in decisions:
            raise DecisionError("Decision registry contains a missing or duplicate candidate id")
        decisions[candidate_id] = copy.deepcopy(decision)
    return decisions


def sync_decisions(
    registry: dict[str, Any] | None,
    runtime: dict[str, Any] | None,
    candidates: dict[str, dict[str, Any]],
    provenance: dict[str, dict[str, Any]],
    *,
    generated_at: str,
) -> dict[str, Any]:
    decisions = existing_decisions(registry)
    if registry is None:
        decisions.update(seed_legacy_decisions(runtime))

    for candidate_id, candidate in candidates.items():
        current_hash = evidence_hash(candidate)
        source = provenance[candidate_id]
        decision = decisions.get(candidate_id)
        if decision is None:
            decision = {
                "id": candidate_id,
                "status": "pending",
                "decidedBy": None,
                "decidedAtUTC": None,
                "note": None,
            }
            decisions[candidate_id] = decision
        elif decision.get("evidenceHash") != current_hash:
            previous_hash = str(decision.get("evidenceHash") or "")
            previous_status = str(decision.get("status") or "pending")
            if previous_hash.startswith("legacy-runtime-") and previous_status == "approved":
                decision["note"] = (
                    "Migrated from the previously published curator-approved runtime feed "
                    "and rebound to the latest matching review evidence."
                )
            else:
                decision["status"] = "pending"
                decision["decidedBy"] = None
                decision["decidedAtUTC"] = None
                decision["note"] = (
                    f"Evidence changed after the previous {previous_status} decision; review required."
                )
        decision["evidenceHash"] = current_hash
        decision["sourceReviewQueue"] = source["sourceReviewQueue"]
        decision["reviewSetID"] = source["reviewSetID"]
        decision["recommendedDecision"] = candidate.get("recommendedDecision")
        decision["lastSeenAsOfDate"] = source["asOfDate"]

    result = {
        "schemaVersion": 1,
        "family": "tnsTransientReviewDecisions",
        "generatedAtUTC": generated_at,
        "instructions": (
            "Set status to approved, hold, or rejected and record decidedBy/decidedAtUTC. "
            "Approved entries with current evidence are materialized into the runtime feed; "
            "merging the review PR publishes that generated feed through stable metadata."
        ),
        "decisions": sorted(decisions.values(), key=lambda item: str(item.get("id") or "")),
    }
    validate_decisions(result)
    return result


def validate_decisions(registry: dict[str, Any]) -> None:
    if registry.get("schemaVersion") != 1 or registry.get("family") != "tnsTransientReviewDecisions":
        raise DecisionError("Invalid TNS decision registry envelope")
    seen: set[str] = set()
    for decision in registry.get("decisions") or []:
        candidate_id = str(decision.get("id") or "").strip()
        status = str(decision.get("status") or "").strip()
        if not candidate_id or candidate_id in seen:
            raise DecisionError("Decision registry contains a missing or duplicate candidate id")
        seen.add(candidate_id)
        if status not in ALLOWED_STATUSES:
            raise DecisionError(f"Decision {candidate_id} has invalid status {status!r}")
        if not str(decision.get("evidenceHash") or "").strip():
            raise DecisionError(f"Decision {candidate_id} is missing evidenceHash")
        if status != "pending":
            if not str(decision.get("decidedBy") or "").strip():
                raise DecisionError(f"Decision {candidate_id} status {status} requires decidedBy")
            if parse_datetime(decision.get("decidedAtUTC")) is None:
                raise DecisionError(f"Decision {candidate_id} status {status} requires decidedAtUTC")


def is_active(opportunity: dict[str, Any], reference: dt.datetime) -> bool:
    expires = parse_datetime((opportunity.get("activeWindow") or {}).get("expiresAtUTC"))
    return expires is not None and expires > reference


def promote_candidate(candidate: dict[str, Any], decision: dict[str, Any]) -> dict[str, Any]:
    promoted = candidate_material(candidate)
    promoted["reviewOnly"] = False
    promoted["recommendedReviewAction"] = "approved"
    promoted.pop("recommendedDecision", None)
    promoted.pop("decisionReason", None)
    promoted["review"] = {
        "status": "approved",
        "approvedBy": decision.get("decidedBy"),
        "approvedAtUTC": decision.get("decidedAtUTC"),
        "sourceReviewQueue": decision.get("sourceReviewQueue"),
        "reviewSetID": decision.get("reviewSetID"),
        "evidenceHash": decision.get("evidenceHash"),
    }
    return promoted


def build_runtime(
    previous_runtime: dict[str, Any] | None,
    registry: dict[str, Any],
    candidates: dict[str, dict[str, Any]],
    *,
    as_of_date: str,
    generated_at: str,
) -> dict[str, Any]:
    reference = parse_datetime(f"{as_of_date}T23:59:59Z") or parse_datetime(generated_at)
    if reference is None:
        raise DecisionError("Unable to determine runtime reference time")

    previous_by_id = {
        str(item.get("id") or ""): item
        for item in (previous_runtime or {}).get("opportunities") or []
        if item.get("id")
    }
    opportunities: list[dict[str, Any]] = []
    decisions = registry.get("decisions") or []
    for decision in decisions:
        if decision.get("status") != "approved":
            continue
        candidate_id = str(decision.get("id"))
        candidate = candidates.get(candidate_id)
        if candidate is not None and decision.get("evidenceHash") == evidence_hash(candidate):
            opportunity = promote_candidate(candidate, decision)
        else:
            opportunity = copy.deepcopy(previous_by_id.get(candidate_id))
            if opportunity is None:
                continue
        if is_active(opportunity, reference):
            opportunities.append(opportunity)

    opportunities.sort(
        key=lambda item: (
            str((item.get("activeWindow") or {}).get("expiresAtUTC") or ""),
            str(item.get("id") or ""),
        )
    )
    status_counts = {
        status: sum(1 for item in decisions if item.get("status") == status)
        for status in sorted(ALLOWED_STATUSES)
    }
    return {
        "schemaVersion": 1,
        "family": "transientOpportunities",
        "reviewOnly": False,
        "asOfDate": as_of_date,
        "generatedAtUTC": generated_at,
        "approvalPolicy": "tns_transient_review_decisions_v1",
        "counts": {
            "reviewed": sum(status_counts[status] for status in ("approved", "hold", "rejected")),
            "approved": len(opportunities),
            "excluded": status_counts["hold"] + status_counts["rejected"],
            "pending": status_counts["pending"],
            "expiredApproved": status_counts["approved"] - len(opportunities),
        },
        "opportunities": opportunities,
    }


def escape_markdown(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def render_decisions_markdown(
    registry: dict[str, Any],
    candidates: dict[str, dict[str, Any]],
    runtime: dict[str, Any],
) -> str:
    status_counts = {
        status: sum(1 for item in registry.get("decisions") or [] if item.get("status") == status)
        for status in sorted(ALLOWED_STATUSES)
    }
    lines = [
        "## Publication decisions",
        "",
        "> **Merge-to-publish contract:** the generated runtime feed and stable manifest in this PR contain every still-active candidate whose registry status is `approved`. Merging the PR publishes those generated artifacts through the normal dynamic-metadata channel. `pending`, `hold`, and `rejected` entries are not published.",
        "",
        f"- **Approved and active in runtime:** {len(runtime.get('opportunities') or [])}",
        f"- **Pending review:** {status_counts['pending']}",
        f"- **On hold:** {status_counts['hold']}",
        f"- **Rejected:** {status_counts['rejected']}",
        f"- **Approved but expired:** {(runtime.get('counts') or {}).get('expiredApproved', 0)}",
        "",
        "Edit `outputs/transients/review/transient-review-decisions-v1.json`, then rerun this workflow. A non-pending decision requires `decidedBy` and `decidedAtUTC`. Changed evidence automatically resets the candidate to `pending`.",
        "",
        "| Status | Candidate | Recommendation | Discovery mag | Classification | Near-field match | Active through |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for decision in registry.get("decisions") or []:
        candidate = candidates.get(str(decision.get("id") or ""))
        if candidate is None:
            continue
        target = candidate.get("astroGuideObject") or {}
        classification = candidate.get("classification") or {}
        discovery = candidate.get("discovery") or {}
        active_window = candidate.get("activeWindow") or {}
        lines.append(
            "| {status} | [{name}]({url}) | {recommended} | {magnitude} | {classification} | {target} ({separation} deg) | {expires} |".format(
                status=escape_markdown(str(decision.get("status") or "").title()),
                name=escape_markdown(candidate.get("shortTitle") or candidate.get("sourceObjectName") or decision.get("id")),
                url=escape_markdown(candidate.get("sourceURL")),
                recommended=escape_markdown(decision.get("recommendedDecision")),
                magnitude=escape_markdown(discovery.get("magnitude") or "Unavailable"),
                classification=escape_markdown(classification.get("type") or classification.get("kind") or "Unavailable"),
                target=escape_markdown(target.get("displayName") or target.get("id") or "Unavailable"),
                separation=escape_markdown(candidate.get("angularSeparationDegrees") or "Unavailable"),
                expires=escape_markdown(active_window.get("expiresAtUTC") or "Unavailable"),
            )
        )
    lines.append("")
    return "\n".join(lines)


def ensure_equal(path: Path, expected: str) -> None:
    absolute = repo_path(path)
    if not absolute.exists() or absolute.read_text(encoding="utf-8") != expected:
        raise DecisionError(f"Generated TNS artifact is stale: {path}")


def main() -> int:
    args = parse_args()
    queues = load_review_queues(args.review_dir)
    candidates, provenance, latest_as_of, latest_generated_at = latest_candidates(queues)
    previous_runtime = read_optional_json(args.runtime)
    existing_registry = read_optional_json(args.decisions)
    generated_at = args.generated_at or latest_generated_at or utc_now()
    registry = sync_decisions(
        existing_registry,
        previous_runtime,
        candidates,
        provenance,
        generated_at=generated_at,
    )
    runtime = build_runtime(
        previous_runtime,
        registry,
        candidates,
        as_of_date=latest_as_of,
        generated_at=generated_at,
    )
    markdown = render_decisions_markdown(registry, candidates, runtime)

    registry_text = json_text(registry)
    runtime_text = json_text(runtime)
    if args.check:
        ensure_equal(args.decisions, registry_text)
        ensure_equal(args.decisions_markdown, markdown)
        ensure_equal(args.runtime, runtime_text)
        print(
            f"Validated TNS decisions: {len(registry['decisions'])} decisions, "
            f"{len(runtime['opportunities'])} active approved opportunities."
        )
        return 0

    decisions_path = repo_path(args.decisions)
    decisions_path.parent.mkdir(parents=True, exist_ok=True)
    decisions_path.write_text(registry_text, encoding="utf-8")
    markdown_path = repo_path(args.decisions_markdown)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(markdown, encoding="utf-8")
    runtime_path = repo_path(args.runtime)
    runtime_path.parent.mkdir(parents=True, exist_ok=True)
    runtime_path.write_text(runtime_text, encoding="utf-8")
    print(
        f"TNS decisions: {len(registry['decisions'])} decisions -> "
        f"{len(runtime['opportunities'])} active approved opportunities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
