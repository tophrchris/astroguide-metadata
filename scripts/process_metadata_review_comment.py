#!/usr/bin/env python3
"""Authenticated, evidence-bound PR decisions. Execute only from trusted code.

PR trees supply JSON data, never Python, workflows, shell, or command arguments.
The TNS adapter is deliberately separate from GitHub transport and parsing.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

import apply_tns_transient_review_decisions as decisions
import publish_tns_transient_opportunities as publish

REPO = "tophrchris/astroguide-metadata"
ACTOR = {"login": "tophrchris", "id": 18682191}
BRANCH = "automation/tns-transient-review"
ROOT = Path(__file__).resolve().parents[1]
LEDGER = Path("outputs/transients/decisions/comment-receipts-v1.json")
FILES = [decisions.DEFAULT_DECISIONS_PATH, decisions.DEFAULT_DECISIONS_MARKDOWN_PATH,
         decisions.DEFAULT_RUNTIME_PATH, publish.PACKAGE_PATH, publish.MANIFEST_PATH, LEDGER]
LEGACY_ID = 5970403109
LEGACY_SHA = "4866f46f8a726f55fec17b2af2c09b0a30548abe"
LEGACY_BODY = "I'm ok to APPROVE all 5 items in the review queue, and deploy them as live metadata for app consumption"
STATUSES = {"approve": "approved", "hold": "hold", "reject": "rejected"}


class Refused(RuntimeError):
    """Safe refusal: no decision files or branch refs are changed."""


def run(args, cwd=ROOT):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def git(*args, cwd=ROOT):
    return run(["git", "-c", "core.hooksPath=/dev/null", *map(str, args)], cwd)


def api(path, data=None):
    args = ["gh", "api", path]
    if data is not None:
        args += ["--method", "POST", "--input", "-"]
    result = subprocess.run(args, input=json.dumps(data) if data is not None else None,
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def pages(path):
    result = []
    for page in range(1, 101):
        batch = api(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise Refused("GitHub history exceeds the supported pagination bound.")


def authorize(comment, pr):
    user = comment.get("user", {})
    if any(user.get(k) != v for k, v in ACTOR.items()) or user.get("type") != "User":
        raise Refused("Only verified GitHub user tophrchris (18682191) may decide candidates.")
    if comment.get("issue_url") != f"https://api.github.com/repos/{REPO}/issues/{pr['number']}":
        raise Refused("Comment does not belong to this pull request.")
    if (pr.get("state") != "open" or pr.get("base", {}).get("ref") != "main"
            or pr.get("base", {}).get("repo", {}).get("full_name") != REPO
            or pr.get("head", {}).get("repo", {}).get("full_name") != REPO
            or pr.get("head", {}).get("ref") != BRANCH):
        raise Refused("Expected an open, same-repository TNS review PR targeting main.")
    if comment.get("created_at") != comment.get("updated_at"):
        raise Refused("Edited commands are never applied. Post a new comment with a reviewed revision.")


def parse_command(comment, pr_number):
    body = comment["body"].strip()
    if comment["id"] == LEGACY_ID and pr_number == 80 and body == LEGACY_BODY:
        return "tns", "approved", ["queue"], LEGACY_SHA, 5
    match = re.fullmatch(r"/metadata ([a-z]+) (approve|hold|reject) (.+) at ([0-9a-f]{40})", body)
    if not match:
        raise Refused("Use `/metadata tns approve|hold|reject queue|OBJECT[,OBJECT] at FULL_HEAD_SHA`. "
                      "Ambiguous prose cannot change decisions.")
    family, action, targets, revision = match.groups()
    names = [name.strip() for name in targets.split(",")]
    if not all(re.fullmatch(r"[A-Za-z0-9:]+", name) for name in names):
        raise Refused("Object names must be comma-separated TNS names or candidate IDs.")
    if len(set(name.lower() for name in names)) != len(names) or ("queue" in names and names != ["queue"]):
        raise Refused("Duplicate targets or a mixed queue/object selection is ambiguous.")
    return family, STATUSES[action], names, revision, None


def queue_at(revision):
    paths = git("ls-tree", "-r", "--name-only", revision, "outputs/transients/review").splitlines()
    paths = [p for p in paths if re.fullmatch(r"outputs/transients/review/transient-review-\d{4}-\d{2}-\d{2}\.json", p)]
    if not paths:
        raise Refused("No dated queue exists at the reviewed revision.")
    path = sorted(paths)[-1]
    queue = json.loads(git("show", f"{revision}:{path}"))
    if queue.get("reviewOnly") is not True or queue.get("family") != "transientOpportunities":
        raise Refused("Invalid reviewed queue envelope.")
    return path, queue


def select_candidates(queue, names, expected_count=None):
    items = queue.get("opportunities", [])
    if not items or len({x["id"] for x in items}) != len(items):
        raise Refused("Reviewed queue is empty or contains duplicate IDs.")
    if expected_count is not None and len(items) != expected_count:
        raise Refused(f"The historical approval requires exactly {expected_count} candidates.")
    if names == ["queue"]:
        return items
    selected = []
    for name in names:
        matches = [x for x in items if name.lower() in
                   {str(x.get(k, "")).lower() for k in ("id", "sourceObjectName", "shortTitle")}]
        if len(matches) != 1 or matches[0] in selected:
            raise Refused(f"Target {name!r} is missing, repeated, or ambiguous in the reviewed queue.")
        selected.append(matches[0])
    return selected


def fingerprint(comment):
    return hashlib.sha256(json.dumps({k: comment[k] for k in
        ("id", "body", "created_at", "updated_at")}, sort_keys=True).encode()).hexdigest()


def apply_tns(registry, ledger, comment, revision, queue_path, queue, selected, current, status):
    """Pure transactional adapter: validate all targets before changing any decision."""
    registry, ledger = copy.deepcopy(registry), copy.deepcopy(ledger)
    if ledger.get("schemaVersion") != 1 or not isinstance(ledger.get("receipts"), dict):
        raise Refused("Invalid comment receipt ledger.")
    receipts = ledger["receipts"]
    key = str(comment["id"])
    old = receipts.get(key)
    if old:
        if old["commentFingerprint"] != fingerprint(comment):
            raise Refused("This comment was edited after processing; post a new command.")
        return registry, ledger, old, False
    by_id = decisions.existing_decisions(registry)
    for candidate in selected:
        cid = candidate["id"]
        digest = decisions.evidence_hash(candidate)
        if (cid not in current or decisions.evidence_hash(current[cid]) != digest
                or cid not in by_id or by_id[cid]["evidenceHash"] != digest):
            raise Refused(f"Evidence changed for {candidate['sourceObjectName']}; review the new queue and post a new command.")
        prior_order = (by_id[cid].get("decidedAtUTC") or "",
                       (by_id[cid].get("decisionComment") or {}).get("commentID", 0))
        if prior_order > (comment["created_at"], comment["id"]):
            raise Refused(f"A newer decision already exists for {candidate['sourceObjectName']}.")
    receipt = {
        "commentID": comment["id"], "commentURL": comment["html_url"],
        "commentFingerprint": fingerprint(comment), "actor": ACTOR,
        "createdAtUTC": comment["created_at"], "updatedAtUTC": comment["updated_at"],
        "queueRevision": revision, "sourceReviewQueue": queue_path,
        "reviewSetID": queue.get("reviewSetID"),
        "queueSHA256": hashlib.sha256(json.dumps(queue, sort_keys=True).encode()).hexdigest(),
        "status": status, "candidates": [],
    }
    for candidate in selected:
        entry = by_id[candidate["id"]]
        changed = entry["status"] != status
        receipt["candidates"].append({"id": candidate["id"], "name": candidate["sourceObjectName"],
            "evidenceHash": decisions.evidence_hash(candidate), "previousStatus": entry["status"], "changed": changed})
        entry.update(status=status, decidedBy=ACTOR["login"], decidedAtUTC=comment["created_at"],
                     note=f"Decision from {comment['html_url']}; reviewed revision {revision}.",
                     decisionComment={k: v for k, v in receipt.items() if k != "candidates"})
    registry["decisions"] = sorted(by_id.values(), key=lambda x: x["id"])
    decisions.validate_decisions(registry)
    receipts[key] = receipt
    return registry, ledger, receipt, True


# Future families must provide a data-only evidence validator and materializer,
# and explicitly allow their own branch and output paths; no plugin code from PRs.
ADAPTERS = {"tns": apply_tns}


def safe_paths(root):
    for path in FILES:
        for component in (root / path, *(root / path).parents):
            if component == root.parent:
                break
            if component.is_symlink():
                raise Refused(f"Output path must not be a symlink: {path}")
    for path in (root / decisions.DEFAULT_REVIEW_DIR).glob("*.json"):
        if path.is_symlink():
            raise Refused("Review data must not contain symlinks.")


def materialize(root, registry, ledger, current, as_of, generated, previous):
    decisions.REPO_ROOT = publish.REPO_ROOT = root
    runtime = decisions.build_runtime(previous, registry, current, as_of_date=as_of, generated_at=generated)
    markdown = decisions.render_decisions_markdown(registry, current, runtime)
    package = publish.normalize_package(runtime)
    data = publish.json_bytes(package)
    manifest = publish.read_json(publish.MANIFEST_PATH)
    manifest["packages"] = publish.sort_packages(
        [p for p in manifest["packages"] if p.get("family") != publish.PACKAGE_FAMILY]
        + [publish.descriptor(package, publish.PACKAGE_PATH, data, "1.4.2", "1")])
    manifest["generatedAt"] = manifest["publishedAt"] = decisions.utc_now()
    payloads = {decisions.DEFAULT_DECISIONS_PATH: decisions.json_text(registry),
                decisions.DEFAULT_DECISIONS_MARKDOWN_PATH: markdown,
                decisions.DEFAULT_RUNTIME_PATH: decisions.json_text(runtime),
                publish.PACKAGE_PATH: data.decode(), publish.MANIFEST_PATH: decisions.json_text(manifest),
                LEDGER: decisions.json_text(ledger)}
    for path, text in payloads.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text)
    publish.validate_checked_in_artifacts(publish.MANIFEST_PATH, publish.PACKAGE_PATH)
    if publish.normalize_package(json.loads((root / decisions.DEFAULT_RUNTIME_PATH).read_text())) != package:
        raise Refused("Runtime/package consistency validation failed.")


def acknowledge(pr_number, comment_id, body):
    marker = f"<!-- metadata-decision:{comment_id} -->"
    comments = pages(f"repos/{REPO}/issues/{pr_number}/comments")
    if any(marker in c["body"] and (c["user"].get("id") == ACTOR["id"]
                                   or c["user"].get("login") == "github-actions[bot]" and c["user"].get("id") == 41898282)
           for c in comments):
        return
    api(f"repos/{REPO}/issues/{pr_number}/comments", {"body": marker + "\n" + body})


def receipt_message(receipt):
    lines = [f"Applied **{receipt['status']}** from [this comment]({receipt['commentURL']}) "
             f"to queue revision `{receipt['queueRevision']}` (review set `{receipt['reviewSetID']}`).", ""]
    for item in receipt["candidates"]:
        outcome = f"{item['previousStatus']} → {receipt['status']}" if item["changed"] else f"already {receipt['status']}"
        lines.append(f"- **{item['name']}** (`{item['id']}`): {outcome}; evidence `{item['evidenceHash']}`.")
    lines += ["", "The decision registry, runtime feed, stable package, and manifest were synchronized when this receipt was committed. "
              "A later queue refresh may reset decisions if evidence changes. "
              "Merge remains the publication gate; this action does not merge or notify devices. "
              "Near-field catalog matches remain contextual, not confirmed host associations."]
    return "\n".join(lines)


def process(pr_number, comment_id, write=False):
    pr = api(f"repos/{REPO}/pulls/{pr_number}")
    comment = api(f"repos/{REPO}/issues/comments/{comment_id}")
    authorize(comment, pr)
    family, status, names, revision, count = parse_command(comment, pr_number)
    if family not in ADAPTERS:
        raise Refused("Only the tns metadata family is currently supported.")
    git("fetch", "origin", BRANCH)
    head = git("rev-parse", "FETCH_HEAD")
    if head != pr["head"]["sha"]:
        raise Refused("PR head changed while reading it; retry against fresh state.")
    # Full SHA must be an ancestor of this review PR, never an arbitrary tree.
    try:
        git("merge-base", "--is-ancestor", revision, head)
    except subprocess.CalledProcessError as error:
        raise Refused("Reviewed revision is missing or is not an ancestor of this review PR.") from error
    if decisions.parse_datetime(git("show", "-s", "--format=%cI", revision)) > decisions.parse_datetime(comment["created_at"]):
        raise Refused("The requested revision postdates the command.")
    path, queue = queue_at(revision)
    selected = select_candidates(queue, names, count)
    with tempfile.TemporaryDirectory(prefix="metadata-comment-") as temp:
        root = Path(temp) / "data"
        git("worktree", "add", "--detach", root, head)
        try:
            safe_paths(root)
            decisions.REPO_ROOT = publish.REPO_ROOT = root
            queues = decisions.load_review_queues(decisions.DEFAULT_REVIEW_DIR)
            current, provenance, as_of, generated = decisions.latest_candidates(queues)
            previous = decisions.read_optional_json(decisions.DEFAULT_RUNTIME_PATH)
            registry = decisions.sync_decisions(decisions.read_optional_json(decisions.DEFAULT_DECISIONS_PATH),
                previous, current, provenance, generated_at=generated)
            ledger = decisions.read_optional_json(LEDGER) or {"schemaVersion": 1, "receipts": {}}
            registry, ledger, receipt, fresh = ADAPTERS[family](registry, ledger, comment, revision, path,
                                                               queue, selected, current, status)
            if fresh:
                materialize(root, registry, ledger, current, as_of, generated, previous)
            print(receipt_message(receipt))
            if not write:
                print("DRY RUN: no branch update or acknowledgment posted.")
                return receipt
            # API re-read catches edits/closure; normal fast-forward push is our CAS.
            latest_comment = api(f"repos/{REPO}/issues/comments/{comment_id}")
            latest_pr = api(f"repos/{REPO}/pulls/{pr_number}")
            authorize(latest_comment, latest_pr)
            if fingerprint(latest_comment) != fingerprint(comment) or latest_pr["head"]["sha"] != head:
                raise Refused("Comment or PR changed during validation; retry.")
            if fresh:
                git("add", "--", *FILES, cwd=root)
                git("-c", "user.name=github-actions[bot]", "-c",
                    "user.email=41898282+github-actions[bot]@users.noreply.github.com", "commit", "-m",
                    f"Apply TNS decision comment {comment_id}", cwd=root)
                git("push", "origin", f"HEAD:refs/heads/{BRANCH}", cwd=root)
            acknowledge(pr_number, comment_id, receipt_message(receipt))
            return receipt
        finally:
            git("worktree", "remove", "--force", root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", type=int, required=True)
    parser.add_argument("--comment-id", type=int, required=True)
    parser.add_argument("--write", action="store_true", help="Push scoped artifacts and acknowledge the command")
    args = parser.parse_args()
    try:
        process(args.pr, args.comment_id, args.write)
    except Refused as error:
        print(f"No decisions changed: {error}")
        # Unauthorized users never get a privileged comment response.
        comment = api(f"repos/{REPO}/issues/comments/{args.comment_id}")
        if args.write and all(comment.get("user", {}).get(k) == v for k, v in ACTOR.items()):
            acknowledge(args.pr, f"{args.comment_id}-refused-{fingerprint(comment)[:12]}",
                        f"No decisions changed for comment {args.comment_id}: {error}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
