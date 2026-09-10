#!/usr/bin/env python3
"""Build a deterministic, review-only TNS transient opportunity queue.

The builder accepts TNS staged daily CSV or CSV-in-ZIP deltas, collapses
repeated objects to their newest TNS record, and cross-matches plausible
transients against AstroGuide's bundled deep-sky catalog.  Angular proximity
is always described as a near-field match unless the source explicitly names
the same catalog object as its host.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import os
import re
import sqlite3
import sys
import urllib.error
import urllib.request
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import chain
from pathlib import Path
from typing import Iterable, Iterator


TNS_STAGED_URL = (
    "https://www.wis-tns.org/system/files/tns_public_objects/"
    "tns_public_objects_{date}.csv.zip"
)
DEFAULT_OUTPUT_DIR = Path("outputs/transients/review")
NEAR_FIELD_WORDING = "near-field match"
RELATIONSHIP_NEAR_FIELD = "near_field"

FIELD_ALIASES = {
    "objid": ("objid", "object_id", "tns_id"),
    "name": ("name", "objname", "object_name", "tns_name"),
    "prefix": ("prefix", "name_prefix", "object_prefix"),
    "type": ("type", "object_type", "type_name", "classification"),
    "status": ("status", "object_status", "classification_status"),
    "ra": ("ra", "radeg", "ra_deg", "ra_degrees"),
    "dec": ("declination", "dec", "decdeg", "dec_deg", "dec_degrees"),
    "discovery_date": (
        "discoverydate",
        "discovery_date",
        "discovery_datetime",
        "discovery_time",
    ),
    "discovery_mag": (
        "discoverymag",
        "discovery_mag",
        "discovery_magnitude",
        "discoverymag_or_limit",
    ),
    "discovery_band": (
        "filter",
        "discovery_filter",
        "discovery_band",
        "discmagfilter",
    ),
    "reported_mag": (
        "reportedmag",
        "reported_mag",
        "latestmag",
        "latest_mag",
    ),
    "reported_band": ("reportedmagfilter", "reported_band", "latest_filter"),
    "host_name": ("hostname", "host_name", "host"),
    "last_modified": ("lastmodified", "last_modified", "modified"),
    "reporting_group": ("reporting_group", "reportinggroup"),
    "source_group": ("source_group", "sourcegroup"),
    "internal_names": ("internal_names", "internalnames"),
}

CONTAMINANT_PATTERNS = (
    r"\bartifact\b",
    r"\bbogus\b",
    r"\basteroid\b",
    r"\bminor planet\b",
    r"\bvariable star\b",
    r"\bvarstar\b",
    r"\bcataclysmic variable\b",
    r"\bcv\b",
    r"\bagn\b",
    r"\bqso\b",
    r"\bquasar\b",
)

INTERESTING_PATTERNS = (
    r"\bsn(?:\s|$)",
    r"\bsupernova\b",
    r"\bslsn\b",
    r"\bnova\b",
    r"\btde\b",
    r"\btidal disruption\b",
    r"\bluminous red nova\b",
    r"\blrn\b",
    r"\bilrt\b",
    r"\bfast blue optical transient\b",
    r"\bfbot\b",
    r"\btransient\b",
    r"\bcandidate\b",
    r"\bunclassified\b",
    r"\bunknown\b",
)


@dataclass(frozen=True)
class SourceRecord:
    row: dict[str, str]
    input_file: str
    row_number: int


def normalized_key(value: str) -> str:
    return "".join(
        character.lower()
        for character in value.strip().lstrip("\ufeff")
        if character.isalnum() or character == "_"
    )


def normalized_row(row: dict[str, str]) -> dict[str, str]:
    return {
        normalized_key(key): (value or "").strip()
        for key, value in row.items()
        if key is not None
    }


def field(row: dict[str, str], logical_name: str) -> str:
    for alias in FIELD_ALIASES[logical_name]:
        value = row.get(normalized_key(alias), "")
        if value:
            return value
    return ""


def parse_datetime(value: str) -> dt.datetime | None:
    text = (value or "").strip().replace("Z", "+00:00")
    if not text:
        return None
    for candidate in (text, text.replace(" ", "T", 1)):
        try:
            parsed = dt.datetime.fromisoformat(candidate)
            return parsed.astimezone(dt.UTC) if parsed.tzinfo else parsed.replace(tzinfo=dt.UTC)
        except ValueError:
            continue
    return None


def isoformat_z(value: dt.datetime | None) -> str | None:
    if value is None:
        return None
    return value.astimezone(dt.UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_float(value: str) -> float | None:
    try:
        parsed = float((value or "").strip())
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def parse_angle(value: str, *, is_ra: bool) -> float:
    text = value.strip().replace("−", "-")
    if not text:
        raise ValueError("missing angle")
    if ":" not in text and " " not in text:
        result = float(text)
    else:
        parts = text.replace(":", " ").split()
        if len(parts) != 3:
            raise ValueError(f"unsupported sexagesimal angle: {text}")
        sign = -1.0 if parts[0].startswith("-") else 1.0
        major = abs(float(parts[0]))
        result = sign * (major + float(parts[1]) / 60.0 + float(parts[2]) / 3600.0)
        if is_ra:
            result *= 15.0
    if is_ra and not 0.0 <= result <= 360.0:
        raise ValueError(f"RA outside 0..360 degrees: {text}")
    if not is_ra and not -90.0 <= result <= 90.0:
        raise ValueError(f"declination outside -90..90 degrees: {text}")
    return result


def rows_from_lines(lines: Iterable[str]) -> Iterator[dict[str, str]]:
    iterator = iter(lines)
    try:
        first_line = next(iterator)
    except StopIteration:
        return
    if len(next(csv.reader([first_line]))) == 1:
        try:
            first_line = next(iterator)
        except StopIteration:
            return
    yield from csv.DictReader(chain((first_line,), iterator))


def iter_csv_rows(path: Path) -> Iterator[tuple[int, dict[str, str]]]:
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            members = sorted(name for name in archive.namelist() if name.lower().endswith(".csv"))
            if not members:
                raise ValueError(f"ZIP has no CSV member: {path}")
            row_number = 0
            for member in members:
                with archive.open(member) as raw:
                    lines = (line.decode("utf-8-sig", errors="replace") for line in raw)
                    for row in rows_from_lines(lines):
                        row_number += 1
                        yield row_number, row
    else:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row_number, row in enumerate(rows_from_lines(handle), start=1):
                yield row_number, row


def display_name(row: dict[str, str]) -> str:
    name = field(row, "name")
    prefix = field(row, "prefix")
    return f"{prefix}{name}" if prefix and not name.upper().startswith(prefix.upper()) else name


def source_url(name: str) -> str:
    compact = name.replace(" ", "")
    compact = re.sub(r"^(?:AT|SN|TDE|SLSN|NOVA)(?=\d{4})", "", compact, flags=re.I)
    return f"https://www.wis-tns.org/object/{compact}"


def classification_kind(name: str, object_type: str, status: str) -> str:
    combined = " ".join(part for part in (object_type, status) if part).lower()
    if any(re.search(pattern, combined) for pattern in CONTAMINANT_PATTERNS):
        return "contaminant"
    if re.search(r"\bslsn\b", combined):
        return "superluminous_supernova"
    if re.search(r"\b(?:sn|supernova)(?:\s|$)", combined) or name.upper().startswith("SN"):
        return "supernova"
    if re.search(r"\bnova\b|\blrn\b|\bluminous red nova\b", combined):
        return "nova"
    if re.search(r"\btde\b|\btidal disruption\b", combined):
        return "tidal_disruption_event"
    if not combined or any(re.search(pattern, combined) for pattern in INTERESTING_PATTERNS):
        return "transient_candidate"
    return "unsupported"


def row_identity(record: SourceRecord) -> str:
    return field(record.row, "objid") or source_url(display_name(record.row))


def canonical_row_text(row: dict[str, str]) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def deduplicate_records(
    records: Iterable[SourceRecord],
) -> tuple[list[SourceRecord], dict[str, list[dict[str, object]]], int]:
    grouped: dict[str, list[SourceRecord]] = defaultdict(list)
    for record in records:
        grouped[row_identity(record)].append(record)

    selected: list[SourceRecord] = []
    provenance: dict[str, list[dict[str, object]]] = {}
    for identity in sorted(grouped):
        candidates = grouped[identity]
        selected.append(
            max(
                candidates,
                key=lambda item: (
                    parse_datetime(field(item.row, "last_modified")) or dt.datetime.min.replace(tzinfo=dt.UTC),
                    canonical_row_text(item.row),
                ),
            )
        )
        provenance[identity] = sorted(
            (
                {
                    "inputFile": item.input_file,
                    "rowNumber": item.row_number,
                    "lastModifiedUTC": isoformat_z(parse_datetime(field(item.row, "last_modified"))),
                }
                for item in candidates
            ),
            key=lambda item: (
                str(item["inputFile"]),
                int(item["rowNumber"]),
                str(item["lastModifiedUTC"] or ""),
            ),
        )
    return selected, provenance, sum(len(group) - 1 for group in grouped.values())


def load_source_records(paths: Iterable[Path]) -> list[SourceRecord]:
    records = []
    for path in sorted(paths, key=lambda item: item.name):
        for row_number, raw_row in iter_csv_rows(path):
            records.append(SourceRecord(normalized_row(raw_row), path.name, row_number))
    return records


def load_catalog(path: Path) -> tuple[list[dict[str, object]], dict[tuple[int, int], list[int]]]:
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT object_id, primary_name, catalog_name, object_type, magnitude,
                   ra_hours * 15.0 AS ra_deg, dec_degrees, aliases
            FROM deep_sky_objects
            WHERE ra_hours IS NOT NULL AND dec_degrees IS NOT NULL
            """
        ).fetchall()
    finally:
        connection.close()
    catalog = [dict(row) for row in rows]
    grid: dict[tuple[int, int], list[int]] = defaultdict(list)
    for index, row in enumerate(catalog):
        grid[(math.floor(float(row["dec_degrees"])), math.floor(float(row["ra_deg"])) % 360)].append(index)
    return catalog, grid


def nearby_catalog_indices(
    ra: float,
    dec: float,
    grid: dict[tuple[int, int], list[int]],
    radius: float,
) -> set[int]:
    dec_min = max(-90, math.floor(dec - radius))
    dec_max = min(89, math.floor(dec + radius))
    cos_dec = abs(math.cos(math.radians(dec)))
    ra_radius = 180.0 if cos_dec < 0.02 else min(180.0, radius / cos_dec + 0.2)
    ra_bins: Iterable[int]
    if ra_radius >= 180.0:
        ra_bins = range(360)
    else:
        ra_bins = [value % 360 for value in range(math.floor(ra - ra_radius), math.floor(ra + ra_radius) + 1)]
    result: set[int] = set()
    for dec_bin in range(dec_min, dec_max + 1):
        for ra_bin in ra_bins:
            result.update(grid.get((dec_bin, ra_bin), ()))
    return result


def angular_separation_deg(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    ra1r, dec1r, ra2r, dec2r = map(math.radians, (ra1, dec1, ra2, dec2))
    cosine = (
        math.sin(dec1r) * math.sin(dec2r)
        + math.cos(dec1r) * math.cos(dec2r) * math.cos(ra1r - ra2r)
    )
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def nearest_catalog_object(
    ra: float,
    dec: float,
    catalog: list[dict[str, object]],
    grid: dict[tuple[int, int], list[int]],
    radius: float,
) -> tuple[float, dict[str, object]] | None:
    nearest = None
    for index in nearby_catalog_indices(ra, dec, grid, radius):
        target = catalog[index]
        separation = angular_separation_deg(
            ra,
            dec,
            float(target["ra_deg"]),
            float(target["dec_degrees"]),
        )
        target_key = (str(target["object_id"]), str(target["primary_name"]))
        if separation <= radius and (
            nearest is None or (separation, target_key) < (nearest[0], nearest[1])
        ):
            nearest = (separation, target_key, target)
    return (nearest[0], nearest[2]) if nearest else None


def is_recognizable(target: dict[str, object]) -> bool:
    identifiers = " ".join(
        str(target.get(key) or "") for key in ("object_id", "catalog_name", "aliases")
    )
    return bool(re.search(r"(?:^|[|\s])(?:M\s?\d+|NGC\s?\d+|IC\s?\d+)(?:$|[|\s])", identifiers, re.I))


def normalized_designation(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def host_matches_target(host_name: str, target: dict[str, object]) -> bool:
    host = normalized_designation(host_name)
    if not host:
        return False
    values = [
        str(target.get("object_id") or ""),
        str(target.get("primary_name") or ""),
        str(target.get("catalog_name") or ""),
        *str(target.get("aliases") or "").split("|"),
    ]
    return host in {normalized_designation(value) for value in values if value}


def score_candidate(
    *,
    kind: str,
    age_days: int | None,
    magnitude: float | None,
    separation: float,
    target: dict[str, object],
) -> tuple[int, list[str]]:
    score = 20
    reasons = []
    if kind in {"supernova", "superluminous_supernova", "nova", "tidal_disruption_event"}:
        score += 20
        reasons.append("classified_high_interest_transient")
    else:
        score += 5
        reasons.append("unclassified_transient_candidate")

    if age_days is None:
        score -= 10
        reasons.append("discovery_date_missing")
    elif age_days <= 7:
        score += 20
        reasons.append("discovered_within_7_days")
    elif age_days <= 30:
        score += 12
        reasons.append("discovered_within_30_days")
    else:
        score -= 25
        reasons.append("older_than_30_days")

    if magnitude is None:
        score -= 5
        reasons.append("discovery_magnitude_missing")
    elif magnitude <= 16.5:
        score += 25
        reasons.append("discovery_magnitude_le_16_5")
    elif magnitude <= 18.5:
        score += 15
        reasons.append("discovery_magnitude_le_18_5")
    elif magnitude <= 19.5:
        score += 5
        reasons.append("discovery_magnitude_watch_band")
    else:
        score -= 15
        reasons.append("fainter_than_watch_band")

    if separation <= 0.25:
        score += 25
        reasons.append("separation_le_0_25_deg")
    elif separation <= 1.0:
        score += 12
        reasons.append("separation_le_1_deg")
    else:
        score += 5
        reasons.append("separation_le_2_deg")

    if "galaxy" in str(target.get("object_type") or "").lower():
        score += 10
        reasons.append("nearby_catalog_object_is_galaxy")
    if is_recognizable(target):
        score += 8
        reasons.append("recognizable_astroguide_subject")
    return max(0, min(score, 100)), reasons


def is_review_eligible(
    *,
    kind: str,
    magnitude: float | None,
    separation: float,
    target: dict[str, object],
    watch_magnitude: float,
) -> bool:
    """Apply the conservative gate after broad classification and geometry filters."""
    confirmed = {
        "supernova",
        "superluminous_supernova",
        "nova",
        "tidal_disruption_event",
    }
    if magnitude is None:
        return kind in confirmed and separation <= 0.25
    if magnitude > watch_magnitude:
        return False
    if kind in confirmed or separation <= 0.25:
        return True
    return magnitude <= 18.5 and "galaxy" in str(target.get("object_type") or "").lower()


def event_title(kind: str, name: str, target_name: str) -> str:
    noun = {
        "supernova": "Supernova",
        "superluminous_supernova": "Superluminous supernova",
        "nova": "Nova",
        "tidal_disruption_event": "Tidal disruption event",
    }.get(kind, "Transient candidate")
    return f"{noun} {name} near {target_name}"


def build_queue(
    records: Iterable[SourceRecord],
    catalog: list[dict[str, object]],
    grid: dict[tuple[int, int], list[int]],
    *,
    as_of: dt.date,
    radius_deg: float = 2.0,
    max_age_days: int = 45,
    watch_magnitude: float = 19.5,
) -> dict[str, object]:
    selected, provenance, duplicate_count = deduplicate_records(records)
    counts = Counter(
        rawRows=sum(len(items) for items in provenance.values()),
        duplicateRowsCollapsed=duplicate_count,
        uniqueObjects=len(selected),
    )
    opportunities = []
    as_of_datetime = dt.datetime.combine(as_of, dt.time.min, tzinfo=dt.UTC)

    for record in selected:
        row = record.row
        name = display_name(row)
        kind = classification_kind(name, field(row, "type"), field(row, "status"))
        if kind == "contaminant":
            counts["contaminantsRejected"] += 1
            continue
        if kind == "unsupported":
            counts["unsupportedClassificationsRejected"] += 1
            continue
        counts["plausibleCandidates"] += 1

        discovered = parse_datetime(field(row, "discovery_date"))
        age_days = (as_of_datetime.date() - discovered.date()).days if discovered else None
        if age_days is not None and (age_days < 0 or age_days > max_age_days):
            counts["outsideDiscoveryWindow"] += 1
            continue
        magnitude = parse_float(field(row, "discovery_mag"))
        if magnitude is not None and magnitude > watch_magnitude:
            counts["fainterThanWatchBand"] += 1
            continue

        try:
            ra = parse_angle(field(row, "ra"), is_ra=True)
            dec = parse_angle(field(row, "dec"), is_ra=False)
        except ValueError:
            counts["invalidCoordinates"] += 1
            continue
        nearest = nearest_catalog_object(ra, dec, catalog, grid, radius_deg)
        if nearest is None:
            counts["outsideNearFieldRadius"] += 1
            continue
        separation, target = nearest
        counts["nearFieldMatches"] += 1

        if not is_review_eligible(
            kind=kind,
            magnitude=magnitude,
            separation=separation,
            target=target,
            watch_magnitude=watch_magnitude,
        ):
            counts["outsideReviewGate"] += 1
            continue

        score, reasons = score_candidate(
            kind=kind,
            age_days=age_days,
            magnitude=magnitude,
            separation=separation,
            target=target,
        )
        if age_days is not None and age_days > 30:
            urgency = "expired"
            action = "reject"
        elif magnitude is not None and magnitude <= 18.5 and score >= 70:
            urgency = "urgent"
            action = "approve_or_enrich"
        else:
            urgency = "watch"
            action = "watch" if discovered and magnitude is not None else "needs_enrichment"

        identity = row_identity(record)
        host_name = field(row, "host_name")
        explicit_host_match = host_matches_target(host_name, target)
        relationship_type = "tns_reported_host" if explicit_host_match else RELATIONSHIP_NEAR_FIELD
        relationship_wording = "TNS-reported host match" if explicit_host_match else NEAR_FIELD_WORDING
        expires = discovered + dt.timedelta(days=30) if discovered else None
        source_id = field(row, "objid")
        stable_id = f"tns:{source_id}" if source_id else f"tns:{normalized_designation(name)}"

        opportunities.append(
            {
                "id": stable_id,
                "source": "TNS",
                "sourceId": source_id or None,
                "sourceObjectName": name,
                "sourceURL": source_url(name),
                "title": event_title(kind, name, str(target["primary_name"])),
                "shortTitle": name,
                "eventType": "novaOpportunity" if kind == "nova" else "transientOpportunity",
                "reviewOnly": True,
                "urgency": urgency,
                "recommendedReviewAction": action,
                "activeWindow": {
                    "startsAtUTC": isoformat_z(discovered),
                    "expiresAtUTC": isoformat_z(expires),
                },
                "discovery": {
                    "dateUTC": isoformat_z(discovered),
                    "ageDays": age_days,
                    "magnitude": magnitude,
                    "band": field(row, "discovery_band") or None,
                },
                "reportedMagnitude": {
                    "value": parse_float(field(row, "reported_mag")),
                    "band": field(row, "reported_band") or None,
                },
                "classification": {
                    "kind": kind,
                    "type": field(row, "type") or None,
                    "status": field(row, "status") or None,
                },
                "coordinates": {"raDegrees": round(ra, 7), "decDegrees": round(dec, 7)},
                "score": score,
                "reasonTags": reasons,
                "astroGuideObject": {
                    "id": target["object_id"],
                    "displayName": target["primary_name"],
                    "catalogName": target["catalog_name"],
                    "objectType": target["object_type"],
                    "magnitude": target["magnitude"],
                },
                "angularSeparationDegrees": round(separation, 5),
                "relationship": {
                    "type": relationship_type,
                    "wording": relationship_wording,
                    "tnsReportedHost": host_name or None,
                },
                "lastModifiedUTC": isoformat_z(parse_datetime(field(row, "last_modified"))),
                "provenance": {
                    "inputRecords": provenance[identity],
                    "reportingGroup": field(row, "reporting_group") or None,
                    "sourceGroup": field(row, "source_group") or None,
                    "internalNames": [
                        item.strip()
                        for item in field(row, "internal_names").split(",")
                        if item.strip()
                    ],
                },
            }
        )

    opportunities.sort(
        key=lambda item: (
            {"urgent": 0, "watch": 1, "expired": 2}[str(item["urgency"])],
            -int(item["score"]),
            str(item["id"]),
        )
    )
    counts["reviewOpportunities"] = len(opportunities)
    counts["urgent"] = sum(item["urgency"] == "urgent" for item in opportunities)
    counts["watch"] = sum(item["urgency"] == "watch" for item in opportunities)
    counts["expired"] = sum(item["urgency"] == "expired" for item in opportunities)

    ordered_count_keys = (
        "rawRows",
        "duplicateRowsCollapsed",
        "uniqueObjects",
        "contaminantsRejected",
        "unsupportedClassificationsRejected",
        "plausibleCandidates",
        "outsideDiscoveryWindow",
        "fainterThanWatchBand",
        "invalidCoordinates",
        "outsideNearFieldRadius",
        "nearFieldMatches",
        "outsideReviewGate",
        "reviewOpportunities",
        "urgent",
        "watch",
        "expired",
    )
    return {
        "schemaVersion": 1,
        "family": "transientOpportunities",
        "reviewOnly": True,
        "asOfDate": as_of.isoformat(),
        "generatedAtUTC": f"{as_of.isoformat()}T00:00:00Z",
        "policy": {
            "nearFieldRadiusDegrees": radius_deg,
            "preferredDiscoveryAgeDays": 30,
            "maximumDiscoveryAgeDays": max_age_days,
            "preferredDiscoveryMagnitude": 18.5,
            "watchDiscoveryMagnitude": watch_magnitude,
            "relationshipDefault": RELATIONSHIP_NEAR_FIELD,
        },
        "counts": {key: counts[key] for key in ordered_count_keys},
        "opportunities": opportunities,
    }


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def format_magnitude(value: object) -> str:
    return "—" if value is None else f"{float(value):.2f}".rstrip("0").rstrip(".")


def render_markdown(queue: dict[str, object]) -> str:
    counts = queue["counts"]
    opportunities = queue["opportunities"]
    lines = [
        f"# TNS transient opportunity review — {queue['asOfDate']}",
        "",
        "> Review queue only. Nothing in this report is published as app-facing metadata or a notification.",
        "",
        "AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.",
        "",
        "## Summary",
        "",
        f"- {counts['reviewOpportunities']} review opportunities: {counts['urgent']} urgent, {counts['watch']} watch, {counts['expired']} expired",
        f"- {counts['rawRows']} staged rows collapsed to {counts['uniqueObjects']} unique TNS objects ({counts['duplicateRowsCollapsed']} duplicate/change rows)",
        f"- {counts['contaminantsRejected']} known contaminants rejected before cross-match",
        "",
        "## Review queue",
        "",
    ]
    if not opportunities:
        lines.append("No candidates met the current review policy.")
        lines.append("")
    else:
        lines.extend(
            [
                "| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |",
                "|---|---|---|---:|---:|---|---:|---|---:|---|",
            ]
        )
        for item in opportunities:
            discovery = item["discovery"]
            classification = item["classification"]
            target = item["astroGuideObject"]
            relationship = item["relationship"]
            age = "—" if discovery["ageDays"] is None else str(discovery["ageDays"])
            lines.append(
                "| "
                + " | ".join(
                    markdown_escape(value)
                    for value in (
                        item["urgency"],
                        f"[{item['sourceObjectName']}]({item['sourceURL']})",
                        classification["type"] or classification["kind"],
                        age,
                        format_magnitude(discovery["magnitude"]),
                        f"{target['displayName']} ({target['objectType']})",
                        f"{item['angularSeparationDegrees']:.5f}°",
                        relationship["wording"],
                        item["score"],
                        item["recommendedReviewAction"],
                    )
                )
                + " |"
            )
        lines.append("")
    lines.extend(
        [
            "## Policy notes",
            "",
            "- Discovery magnitude is not a current magnitude; candidates may have faded.",
            "- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.",
            "- The 18.5–19.5 magnitude band remains lower-priority watch material.",
            "- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.",
            "- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.",
            "",
        ]
    )
    return "\n".join(lines)


def fetch_staged_deltas(
    *,
    as_of: dt.date,
    days: int,
    destination: Path,
    user_agent: str,
) -> list[Path]:
    if not user_agent.startswith("tns_marker{"):
        raise ValueError("TNS user agent must use the approved tns_marker{...} format")
    destination.mkdir(parents=True, exist_ok=True)
    paths = []
    for offset in reversed(range(days)):
        date = as_of - dt.timedelta(days=offset)
        date_text = date.strftime("%Y%m%d")
        path = destination / f"tns_public_objects_{date_text}.csv.zip"
        request = urllib.request.Request(
            TNS_STAGED_URL.format(date=date_text),
            headers={"User-Agent": user_agent},
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = response.read()
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise RuntimeError(
                    f"TNS staged delta is not available yet for {date_text}; "
                    "rerun with an earlier --as-of date or wait for TNS to publish it."
                ) from error
            raise
        path.write_bytes(payload)
        if not zipfile.is_zipfile(path):
            raise RuntimeError(f"TNS response is not a ZIP archive: {date_text}")
        paths.append(path)
    return paths


def meaningful_opportunities(queue: dict[str, object]) -> list[dict[str, object]]:
    material = json.loads(json.dumps(queue["opportunities"]))
    for item in material:
        item.get("provenance", {}).pop("inputRecords", None)
    return material


def latest_previous_queue(output_dir: Path, current_path: Path) -> Path | None:
    paths = [path for path in output_dir.glob("transient-review-*.json") if path != current_path]
    return max(paths, default=None, key=lambda path: path.name)


def write_outputs(
    queue: dict[str, object],
    output_dir: Path,
    *,
    skip_unchanged: bool,
) -> tuple[Path, Path, bool]:
    output_dir.mkdir(parents=True, exist_ok=True)
    date = str(queue["asOfDate"])
    json_path = output_dir / f"transient-review-{date}.json"
    markdown_path = output_dir / f"transient-review-{date}.md"
    previous = latest_previous_queue(output_dir, json_path)
    if skip_unchanged and previous:
        previous_queue = json.loads(previous.read_text(encoding="utf-8"))
        if meaningful_opportunities(previous_queue) == meaningful_opportunities(queue):
            print(f"No material opportunity changes since {previous.name}; outputs unchanged.")
            return json_path, markdown_path, False
    json_path.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(queue), encoding="utf-8")
    return json_path, markdown_path, True


def parse_as_of(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("expected YYYY-MM-DD") from error


def default_fetch_as_of(today: dt.date | None = None) -> dt.date:
    """Use yesterday by default because same-day TNS staged deltas can lag."""
    current_day = today or dt.datetime.now(dt.UTC).date()
    return current_day - dt.timedelta(days=1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="*", type=Path, help="TNS staged .csv or .csv.zip deltas")
    parser.add_argument("--catalog", type=Path, required=True, help="AstroGuide catalog.sqlite")
    parser.add_argument("--as-of", type=parse_as_of, default=default_fetch_as_of())
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--radius-deg", type=float, default=2.0)
    parser.add_argument("--max-age-days", type=int, default=45)
    parser.add_argument("--watch-magnitude", type=float, default=19.5)
    parser.add_argument("--fetch-days", type=int, default=0)
    parser.add_argument("--staging-dir", type=Path, default=Path("work/tns"))
    parser.add_argument("--tns-user-agent", default=os.environ.get("TNS_USER_AGENT", ""))
    parser.add_argument("--skip-unchanged", action="store_true")
    parser.add_argument("--validate-only", type=Path, metavar="QUEUE_JSON")
    args = parser.parse_args()

    if args.validate_only:
        queue = json.loads(args.validate_only.read_text(encoding="utf-8"))
        if queue.get("reviewOnly") is not True or queue.get("family") != "transientOpportunities":
            raise RuntimeError("not a review-only transientOpportunities queue")
        rendered = json.dumps(queue, ensure_ascii=False)
        if "host/association" in rendered.lower():
            raise RuntimeError("queue uses prohibited inferred host/association wording")
        for item in queue.get("opportunities", []):
            relationship = item.get("relationship", {})
            if relationship.get("type") == RELATIONSHIP_NEAR_FIELD and relationship.get("wording") != NEAR_FIELD_WORDING:
                raise RuntimeError("near_field relationship does not use near-field match wording")
        print(f"Validated {len(queue.get('opportunities', []))} review opportunities.")
        return 0

    inputs = list(args.inputs)
    if args.fetch_days:
        if args.fetch_days < 1 or args.fetch_days > 14:
            parser.error("--fetch-days must be between 1 and 14")
        if not args.tns_user_agent:
            parser.error("--fetch-days requires --tns-user-agent or TNS_USER_AGENT")
        inputs.extend(
            fetch_staged_deltas(
                as_of=args.as_of,
                days=args.fetch_days,
                destination=args.staging_dir,
                user_agent=args.tns_user_agent,
            )
        )
    if not inputs:
        parser.error("provide staged inputs or --fetch-days")
    missing = [path for path in inputs if not path.is_file()]
    if missing:
        parser.error(f"input does not exist: {missing[0]}")
    if not args.catalog.is_file():
        parser.error(f"catalog does not exist: {args.catalog}")

    catalog, grid = load_catalog(args.catalog)
    queue = build_queue(
        load_source_records(inputs),
        catalog,
        grid,
        as_of=args.as_of,
        radius_deg=args.radius_deg,
        max_age_days=args.max_age_days,
        watch_magnitude=args.watch_magnitude,
    )
    json_path, markdown_path, wrote = write_outputs(
        queue,
        args.output_dir,
        skip_unchanged=args.skip_unchanged,
    )
    if wrote:
        print(f"Wrote {json_path} and {markdown_path}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
