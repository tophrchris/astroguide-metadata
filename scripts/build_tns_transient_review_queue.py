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
import hashlib
import json
import math
import os
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
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
TNS_OBJECT_API_URL = "https://www.wis-tns.org/api/get/object"
DEFAULT_OUTPUT_DIR = Path("outputs/transients/review")
DEFAULT_TARGET_IMAGE_PACKAGE = Path("v1/packages/target-images/target_image_assets_v1.json")
METADATA_ORIGIN = "https://metadata.astroguide.space"
NEAR_FIELD_WORDING = "near-field match"
RELATIONSHIP_NEAR_FIELD = "near_field"
TargetImageIndex = dict[str, list[tuple[int, dict[str, object]]]]

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
    "redshift": ("redshift", "object_redshift"),
    "reporters": ("reporters", "reporter"),
    "time_received": ("time_received", "timereceived"),
    "creation_date": ("creationdate", "creation_date", "created"),
    "discovery_bibcode": (
        "discovery_ads_bibcode",
        "discoveryadsbibcode",
        "discovery_bibcode",
    ),
    "classification_bibcodes": (
        "class_ads_bibcodes",
        "classadsbibcodes",
        "classification_ads_bibcodes",
        "classification_bibcodes",
    ),
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
            SELECT object_id, primary_name, catalog_name, object_type,
                   constellation, magnitude, angular_size_arcmin,
                   angular_size_maj_arcmin, angular_size_min_arcmin,
                   ra_hours * 15.0 AS ra_deg, dec_degrees, aliases,
                   distance, description
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


def identifier_values(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [item.strip() for item in str(value).split("|") if item.strip()]


def target_identifiers(target: dict[str, object]) -> set[str]:
    values = []
    for key in ("object_id", "primary_name", "catalog_name", "aliases"):
        values.extend(identifier_values(target.get(key)))
    return {normalized_designation(value) for value in values if normalized_designation(value)}


def load_target_image_index(path: Path | None) -> TargetImageIndex:
    """Index provenance-bearing hosted target images by normalized target identifier."""
    if path is None or not path.is_file():
        return {}
    package = json.loads(path.read_text(encoding="utf-8"))
    if (
        package.get("schemaVersion") != 1
        or package.get("packageFamily") != "targetImageAssets"
        or package.get("packageRole") != "index"
        or not str(package.get("packageVersion") or "").strip()
    ):
        raise ValueError("target image package must be targetImageAssets schemaVersion 1")
    index: TargetImageIndex = defaultdict(list)
    for record in package.get("targets", []):
        if not isinstance(record, dict):
            continue
        source = record.get("source") if isinstance(record.get("source"), dict) else {}
        if not source.get("attribution") or not source.get("sourcePackageID"):
            raise ValueError(
                f"target image {record.get('canonicalTargetID')} lacks governed provenance"
            )
        variants = record.get("variants") if isinstance(record.get("variants"), dict) else {}
        for role, variant in variants.items():
            if not isinstance(variant, dict):
                raise ValueError(
                    f"target image {record.get('canonicalTargetID')} has invalid {role} variant"
                )
            variant_path = str(variant.get("path") or "")
            expected_url = f"{METADATA_ORIGIN}/{variant_path}"
            checksum = str(variant.get("sha256") or "")
            if (
                not variant_path.startswith("v1/assets/target-images/")
                or variant.get("url") != expected_url
                or not re.fullmatch(r"[0-9a-f]{64}", checksum)
                or not isinstance(variant.get("byteSize"), int)
                or int(variant["byteSize"]) <= 0
                or not isinstance(variant.get("width"), int)
                or int(variant["width"]) <= 0
                or not isinstance(variant.get("height"), int)
                or int(variant["height"]) <= 0
            ):
                raise ValueError(
                    f"target image {record.get('canonicalTargetID')} has ungoverned {role} variant"
                )
        prioritized_keys = (
            (0, ("canonicalTargetID", "catalogObjectID")),
            (1, ("assetOwnerTargetID", "alternateIDs", "sharedWithTargetIDs")),
            (2, ("aliases",)),
        )
        for priority, keys in prioritized_keys:
            values = []
            for key in keys:
                values.extend(identifier_values(record.get(key)))
            for value in values:
                normalized = normalized_designation(value)
                match = (priority, record)
                if normalized and match not in index[normalized]:
                    index[normalized].append(match)
    return index


def catalog_thumbnail(
    target: dict[str, object],
    target_image_index: TargetImageIndex | None,
) -> dict[str, object]:
    if not target_image_index:
        return {
            "status": "unavailable",
            "reason": "No provenance-safe hosted AstroGuide catalog thumbnail is available.",
        }
    matches: dict[str, tuple[int, dict[str, object]]] = {}
    for identifier in target_identifiers(target):
        for priority, record in target_image_index.get(identifier, []):
            record_id = str(record.get("assetID") or record.get("canonicalTargetID") or "")
            current = matches.get(record_id)
            if current is None or priority < current[0]:
                matches[record_id] = (priority, record)
    if not matches:
        return {
            "status": "unavailable",
            "reason": "No provenance-safe hosted AstroGuide catalog thumbnail is available.",
        }
    _, record = min(
        matches.values(),
        key=lambda match: (
            match[0],
            str(match[1].get("canonicalTargetID") or ""),
            str(match[1].get("assetID") or ""),
        ),
    )
    variants = record.get("variants") if isinstance(record.get("variants"), dict) else {}
    variant = next(
        (
            variants.get(role)
            for role in ("thumbnail160", "thumbnail320", "hero")
            if isinstance(variants.get(role), dict)
        ),
        None,
    )
    if not variant or not variant.get("url"):
        return {
            "status": "unavailable",
            "reason": "The matched AstroGuide image record has no hosted display variant.",
        }
    source = record.get("source") if isinstance(record.get("source"), dict) else {}
    return {
        "status": "available",
        "url": variant.get("url"),
        "path": variant.get("path"),
        "width": variant.get("width"),
        "height": variant.get("height"),
        "sha256": variant.get("sha256"),
        "assetID": record.get("assetID"),
        "ownerTargetID": record.get("assetOwnerTargetID") or record.get("canonicalTargetID"),
        "attribution": source.get("attribution"),
        "sourcePackageID": source.get("sourcePackageID"),
    }


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


def normalized_designations(value: str) -> set[str]:
    parts = [value, *re.split(r"[/;,()]", value)]
    return {normalized_designation(part) for part in parts if normalized_designation(part)}


def host_matches_target(host_name: str, target: dict[str, object]) -> bool:
    hosts = normalized_designations(host_name)
    if not hosts:
        return False
    values = [
        str(target.get("object_id") or ""),
        str(target.get("primary_name") or ""),
        str(target.get("catalog_name") or ""),
        *str(target.get("aliases") or "").split("|"),
    ]
    target_values = {normalized_designation(value) for value in values if value}
    return bool(hosts & target_values)


def split_list(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,;]", value or "") if item.strip()]


def ads_url(bibcode: str) -> str:
    return f"https://ui.adsabs.harvard.edu/abs/{urllib.parse.quote(bibcode, safe='')}/abstract"


def catalog_designation(value: object) -> str | None:
    normalized = re.sub(r"[^A-Z0-9]", "", str(value or "").upper())
    return normalized if re.fullmatch(r"(?:M|NGC|IC|C|LDN)\d+[A-Z]?", normalized) else None


def clean_catalog_distance(value: object) -> str | None:
    text = str(value or "").strip()
    return text if any(character.isdigit() for character in text) else None


def catalog_context(
    target: dict[str, object],
    target_image_index: TargetImageIndex | None,
) -> dict[str, object]:
    aliases = identifier_values(target.get("aliases"))
    object_designation = catalog_designation(target.get("object_id"))
    name_designation = catalog_designation(target.get("primary_name"))
    identity_warning = None
    if object_designation and name_designation and object_designation != name_designation:
        identity_warning = (
            f"Catalog identity conflict: canonical ID {target['object_id']} has the "
            f"different designation {target['primary_name']} as its display name."
        )
    return {
        "id": target["object_id"],
        "displayName": target["primary_name"],
        "catalogName": target["catalog_name"],
        "objectType": target["object_type"],
        "constellation": target.get("constellation"),
        "magnitude": target.get("magnitude"),
        "angularSizeArcmin": target.get("angular_size_arcmin"),
        "angularSizeMajorArcmin": target.get("angular_size_maj_arcmin"),
        "angularSizeMinorArcmin": target.get("angular_size_min_arcmin"),
        "distance": clean_catalog_distance(target.get("distance")),
        "description": target.get("description"),
        "aliases": aliases,
        "identityWarning": identity_warning,
        "coordinates": {
            "raDegrees": round(float(target["ra_deg"]), 7),
            "decDegrees": round(float(target["dec_degrees"]), 7),
        },
        "catalogThumbnail": catalog_thumbnail(target, target_image_index),
    }


def staged_tns_context(row: dict[str, str]) -> dict[str, object]:
    discovery_bibcode = field(row, "discovery_bibcode")
    classification_bibcodes = split_list(field(row, "classification_bibcodes"))
    return {
        "redshift": parse_float(field(row, "redshift")),
        "reporters": field(row, "reporters") or None,
        "receivedAtUTC": isoformat_z(parse_datetime(field(row, "time_received"))),
        "createdAtUTC": isoformat_z(parse_datetime(field(row, "creation_date"))),
        "discoveryReference": (
            {"bibcode": discovery_bibcode, "url": ads_url(discovery_bibcode)}
            if discovery_bibcode
            else None
        ),
        "classificationReferences": [
            {"bibcode": bibcode, "url": ads_url(bibcode)}
            for bibcode in classification_bibcodes
        ],
    }


def recommended_decision(urgency: str) -> str:
    if urgency == "urgent":
        return "approve"
    if urgency == "expired":
        return "reject"
    return "hold"


def review_target_name(target: dict[str, object]) -> str:
    return str(target["id"] if target.get("identityWarning") else target["displayName"])


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
    target_image_index: TargetImageIndex | None = None,
    radius_deg: float = 2.0,
    max_age_days: int = 45,
    watch_magnitude: float = 19.5,
    max_opportunities: int = 0,
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
        elif magnitude is not None and magnitude <= 18.5 and score >= 70:
            urgency = "urgent"
        else:
            urgency = "watch"

        identity = row_identity(record)
        host_name = field(row, "host_name")
        explicit_host_match = host_matches_target(host_name, target)
        relationship_type = "tns_reported_host" if explicit_host_match else RELATIONSHIP_NEAR_FIELD
        relationship_wording = "TNS-reported host match" if explicit_host_match else NEAR_FIELD_WORDING
        expires = discovered + dt.timedelta(days=30) if discovered else None
        source_id = field(row, "objid")
        stable_id = f"tns:{source_id}" if source_id else f"tns:{normalized_designation(name)}"
        target_context = catalog_context(target, target_image_index)
        decision = recommended_decision(urgency)
        decision_reason = None
        if target_context.get("identityWarning"):
            decision = "hold"
            decision_reason = "Hold until the AstroGuide catalog identity conflict is resolved."

        opportunities.append(
            {
                "id": stable_id,
                "source": "TNS",
                "sourceId": source_id or None,
                "sourceObjectName": name,
                "sourceURL": source_url(name),
                "title": event_title(kind, name, review_target_name(target_context)),
                "shortTitle": name,
                "eventType": "novaOpportunity" if kind == "nova" else "transientOpportunity",
                "reviewOnly": True,
                "urgency": urgency,
                "recommendedReviewAction": decision,
                "recommendedDecision": decision,
                "reviewDecision": "pending",
                "decisionReason": decision_reason,
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
                "tnsContext": staged_tns_context(row),
                "enrichment": {
                    "status": "partial",
                    "sources": ["tns_staged_daily_delta", "astroguide_catalog"],
                    "missing": [
                        "tns_reported_host",
                        "latest_public_photometry",
                        "latest_public_spectrum",
                    ],
                },
                "coordinates": {"raDegrees": round(ra, 7), "decDegrees": round(dec, 7)},
                "score": score,
                "reasonTags": reasons,
                "astroGuideObject": target_context,
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
    eligible_opportunities = len(opportunities)
    if max_opportunities > 0:
        opportunities = opportunities[:max_opportunities]
    counts["eligibleReviewOpportunities"] = eligible_opportunities
    counts["reviewOpportunitiesLimit"] = max_opportunities
    counts["reviewOpportunities"] = len(opportunities)
    counts["urgent"] = sum(item["urgency"] == "urgent" for item in opportunities)
    counts["watch"] = sum(item["urgency"] == "watch" for item in opportunities)
    counts["expired"] = sum(item["urgency"] == "expired" for item in opportunities)
    counts["recommendedApprove"] = sum(
        item["recommendedDecision"] == "approve" for item in opportunities
    )
    counts["recommendedHold"] = sum(
        item["recommendedDecision"] == "hold" for item in opportunities
    )
    counts["recommendedReject"] = sum(
        item["recommendedDecision"] == "reject" for item in opportunities
    )

    review_set_id = review_set_identifier(opportunities)

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
        "eligibleReviewOpportunities",
        "reviewOpportunitiesLimit",
        "reviewOpportunities",
        "urgent",
        "watch",
        "expired",
        "recommendedApprove",
        "recommendedHold",
        "recommendedReject",
    )
    return {
        "schemaVersion": 1,
        "family": "transientOpportunities",
        "reviewOnly": True,
        "reviewSetID": review_set_id,
        "asOfDate": as_of.isoformat(),
        "generatedAtUTC": f"{as_of.isoformat()}T00:00:00Z",
        "policy": {
            "nearFieldRadiusDegrees": radius_deg,
            "preferredDiscoveryAgeDays": 30,
            "maximumDiscoveryAgeDays": max_age_days,
            "preferredDiscoveryMagnitude": 18.5,
            "watchDiscoveryMagnitude": watch_magnitude,
            "maxReviewOpportunities": max_opportunities,
            "relationshipDefault": RELATIONSHIP_NEAR_FIELD,
        },
        "counts": {key: counts[key] for key in ordered_count_keys},
        "opportunities": opportunities,
    }


def review_set_identifier(opportunities: Iterable[dict[str, object]]) -> str:
    payload = json.loads(json.dumps(list(opportunities)))
    for item in payload:
        item.pop("reviewDecision", None)
        item.get("provenance", {}).pop("inputRecords", None)
        item.get("enrichment", {}).pop("retrievedAtUTC", None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:16]


def refresh_recommendation_counts(queue: dict[str, object]) -> None:
    opportunities = queue.get("opportunities", [])
    counts = queue.setdefault("counts", {})
    counts["recommendedApprove"] = sum(
        item.get("recommendedDecision") == "approve" for item in opportunities
    )
    counts["recommendedHold"] = sum(
        item.get("recommendedDecision") == "hold" for item in opportunities
    )
    counts["recommendedReject"] = sum(
        item.get("recommendedDecision") == "reject" for item in opportunities
    )


def refresh_existing_queue(
    queue: dict[str, object],
    catalog: list[dict[str, object]],
    target_image_index: TargetImageIndex | None,
) -> None:
    catalog_by_id = {str(target["object_id"]): target for target in catalog}
    for opportunity in queue.get("opportunities", []):
        existing_target = opportunity.get("astroGuideObject") or {}
        target = catalog_by_id.get(str(existing_target.get("id") or ""))
        if target:
            opportunity["astroGuideObject"] = catalog_context(target, target_image_index)
            opportunity["title"] = event_title(
                str(opportunity.get("classification", {}).get("kind") or "transient_candidate"),
                str(opportunity.get("sourceObjectName") or ""),
                review_target_name(opportunity["astroGuideObject"]),
            )
        urgency = str(opportunity.get("urgency") or "watch")
        decision = recommended_decision(urgency)
        if opportunity.get("astroGuideObject", {}).get("identityWarning"):
            decision = "hold"
            opportunity["decisionReason"] = (
                "Hold until the AstroGuide catalog identity conflict is resolved."
            )
        opportunity["recommendedReviewAction"] = decision
        opportunity["recommendedDecision"] = decision
        opportunity.setdefault("reviewDecision", "pending")
        opportunity.setdefault(
            "tnsContext",
            {
                "redshift": None,
                "reporters": None,
                "receivedAtUTC": None,
                "createdAtUTC": None,
                "discoveryReference": None,
                "classificationReferences": [],
            },
        )
        opportunity.setdefault(
            "enrichment",
            {
                "status": "partial",
                "sources": ["tns_staged_daily_delta", "astroguide_catalog"],
                "missing": [
                    "tns_reported_host",
                    "latest_public_photometry",
                    "latest_public_spectrum",
                ],
            },
        )
    refresh_recommendation_counts(queue)
    queue["reviewSetID"] = review_set_identifier(queue.get("opportunities", []))


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def nested_name(value: object) -> str | None:
    if isinstance(value, dict):
        for key in ("name", "value", "label"):
            if value.get(key) not in (None, ""):
                return str(value[key])
        return None
    if value in (None, ""):
        return None
    return str(value)


def detail_entries(value: object) -> list[dict[str, object]]:
    if isinstance(value, dict):
        for key in ("photometry", "spectra", "items", "reply"):
            nested = value.get(key)
            if isinstance(nested, list):
                value = nested
                break
    if not isinstance(value, list):
        return []
    return [entry for entry in value if isinstance(entry, dict)]


def public_detail_entries(value: object) -> list[dict[str, object]]:
    entries = []
    for entry in detail_entries(value):
        visibility = entry.get("public", entry.get("is_public", entry.get("isPublic")))
        if str(visibility).strip().lower() not in {"1", "true", "yes", "y", "public"}:
            continue
        entries.append(entry)
    return entries


def detail_timestamp(entry: dict[str, object]) -> str:
    for key in ("obsdate", "observation_date", "observationDate", "date"):
        value = entry.get(key)
        if value:
            return str(value)
    return ""


def latest_public_photometry(value: object) -> dict[str, object] | None:
    entries = public_detail_entries(value)
    if not entries:
        return None
    entries = [
        entry
        for entry in entries
        if entry.get("flux", entry.get("magnitude", entry.get("mag"))) not in (None, "")
        or entry.get("limflux") not in (None, "")
    ]
    if not entries:
        return None
    entry = max(entries, key=lambda item: detail_timestamp(item))
    flux = entry.get("flux", entry.get("magnitude", entry.get("mag")))
    error = entry.get("fluxerr", entry.get("magnitude_error", entry.get("error")))
    upper_limit = entry.get("upperlimit", entry.get("upper_limit"))
    is_upper_limit = str(upper_limit).strip().lower() in {"1", "true", "yes"} or (
        flux in (None, "") and entry.get("limflux") not in (None, "")
    )
    if is_upper_limit:
        flux = entry.get("limflux")
    return {
        "observationDateUTC": isoformat_z(parse_datetime(detail_timestamp(entry)))
        or detail_timestamp(entry)
        or None,
        "value": parse_float(str(flux)) if flux not in (None, "") else None,
        "error": parse_float(str(error)) if error not in (None, "") else None,
        "units": nested_name(entry.get("flux_unit") or entry.get("units")),
        "band": nested_name(entry.get("filters") or entry.get("filter")),
        "instrument": nested_name(entry.get("instruments") or entry.get("instrument")),
        "telescope": nested_name(entry.get("telescope")),
        "isUpperLimit": is_upper_limit,
    }


def public_spectrum_summary(value: object) -> dict[str, object] | None:
    raw_entries = detail_entries(value)
    entries = public_detail_entries(value)
    if not entries:
        return {"count": 0, "latest": None} if not raw_entries else None
    entry = max(entries, key=lambda item: detail_timestamp(item))
    return {
        "count": len(entries),
        "latest": {
            "observationDateUTC": isoformat_z(parse_datetime(detail_timestamp(entry)))
            or detail_timestamp(entry)
            or None,
            "instrument": nested_name(entry.get("instruments") or entry.get("instrument")),
            "sourceGroup": nested_name(entry.get("source_group") or entry.get("sourceGroup")),
            "remarks": entry.get("remarks") or None,
        },
    }


def normalize_tns_detail(reply: dict[str, object]) -> dict[str, object]:
    classification = nested_name(reply.get("type") or reply.get("object_type"))
    remarks = [
        str(value).strip()
        for value in (
            reply.get("remarks"),
            reply.get("at_rep_remarks"),
            reply.get("classification_remarks"),
        )
        if value and str(value).strip()
    ]
    return {
        "currentType": classification,
        "redshift": (
            parse_float(str(reply.get("redshift")))
            if reply.get("redshift") not in (None, "")
            else None
        ),
        "host": {
            "name": nested_name(reply.get("hostname") or reply.get("host_name")),
            "redshift": (
                parse_float(str(reply.get("host_redshift")))
                if reply.get("host_redshift") not in (None, "")
                else None
            ),
        },
        "latestPhotometry": latest_public_photometry(reply.get("photometry")),
        "spectra": public_spectrum_summary(reply.get("spectra")),
        "remarks": remarks,
    }


def catalog_context_host_match(host_name: str | None, target: dict[str, object]) -> bool:
    hosts = normalized_designations(host_name or "")
    if not hosts:
        return False
    values = [
        target.get("id"),
        target.get("displayName"),
        target.get("catalogName"),
        *(target.get("aliases") or []),
    ]
    target_values = {normalized_designation(str(value)) for value in values if value}
    return bool(hosts & target_values)


def is_magnitude_unit(value: object) -> bool:
    """Return whether a TNS photometry unit can populate reportedMagnitude."""

    return isinstance(value, str) and "mag" in value.casefold()


def merge_tns_detail(
    opportunity: dict[str, object],
    detail: dict[str, object],
    *,
    retrieved_at: str,
    source_kind: str,
) -> None:
    context = opportunity.setdefault("tnsContext", {})
    current_type = detail.get("currentType")
    if current_type:
        classification = opportunity.setdefault("classification", {})
        classification["type"] = current_type
        classification["kind"] = classification_kind(
            str(opportunity.get("sourceObjectName") or ""),
            str(current_type),
            str(classification.get("status") or ""),
        )
        context["currentType"] = current_type
    if detail.get("redshift") is not None:
        context["redshift"] = detail["redshift"]
    host = detail.get("host") if isinstance(detail.get("host"), dict) else {}
    host_name = host.get("name")
    if host_name:
        context["host"] = {
            "name": host_name,
            "redshift": host.get("redshift"),
        }
        relationship = opportunity.setdefault("relationship", {})
        relationship["tnsReportedHost"] = host_name
        if catalog_context_host_match(str(host_name), opportunity["astroGuideObject"]):
            relationship["type"] = "tns_reported_host"
            relationship["wording"] = "TNS-reported host match"
        else:
            relationship["type"] = RELATIONSHIP_NEAR_FIELD
            relationship["wording"] = NEAR_FIELD_WORDING
    if detail.get("latestPhotometry"):
        context["latestPublicPhotometry"] = detail["latestPhotometry"]
        photometry = detail["latestPhotometry"]
        if (
            photometry.get("value") is not None
            and not photometry.get("isUpperLimit")
            and is_magnitude_unit(photometry.get("units"))
        ):
            opportunity["reportedMagnitude"] = {
                "value": photometry.get("value"),
                "band": photometry.get("band"),
                "units": photometry.get("units"),
                "observedAtUTC": photometry.get("observationDateUTC"),
            }
    if detail.get("spectra"):
        context["publicSpectra"] = detail["spectra"]
    discovery_reference = detail.get("discoveryReference")
    if isinstance(discovery_reference, dict) and discovery_reference.get("bibcode"):
        context["discoveryReference"] = discovery_reference
    references = detail.get("classificationReferences")
    if isinstance(references, list) and references:
        existing = {
            str(item.get("bibcode")): item
            for item in context.get("classificationReferences", [])
            if isinstance(item, dict) and item.get("bibcode")
        }
        for reference in references:
            if isinstance(reference, dict) and reference.get("bibcode"):
                existing[str(reference["bibcode"])] = reference
        context["classificationReferences"] = [existing[key] for key in sorted(existing)]
    raw_remarks = detail.get("remarks", [])
    if isinstance(raw_remarks, str):
        raw_remarks = [raw_remarks]
    remarks = [str(value).strip() for value in raw_remarks if str(value).strip()]
    if remarks:
        context["remarks"] = remarks
    requested_decision = detail.get("recommendedDecision")
    decision_reason = detail.get("decisionReason")
    combined_remarks = " ".join(remarks).lower()
    possible_contaminant = any(
        re.search(pattern, combined_remarks) for pattern in CONTAMINANT_PATTERNS
    )
    if requested_decision in {"approve", "hold", "reject"}:
        opportunity["recommendedDecision"] = requested_decision
        opportunity["recommendedReviewAction"] = requested_decision
    enriched_kind = str(opportunity.get("classification", {}).get("kind") or "")
    if enriched_kind == "contaminant":
        opportunity["recommendedDecision"] = "reject"
        opportunity["recommendedReviewAction"] = "reject"
        decision_reason = "Reject because the authoritative classification is a known contaminant class."
    elif enriched_kind in {"transient_candidate", "unsupported"} and opportunity.get(
        "recommendedDecision"
    ) == "approve":
        opportunity["recommendedDecision"] = "hold"
        opportunity["recommendedReviewAction"] = "hold"
        decision_reason = decision_reason or "Hold pending a confirmed high-interest classification."
    if possible_contaminant and opportunity.get("recommendedDecision") != "reject":
        opportunity["recommendedDecision"] = "hold"
        opportunity["recommendedReviewAction"] = "hold"
        decision_reason = decision_reason or "Authoritative remarks flag a possible contaminant."
    if decision_reason:
        opportunity["decisionReason"] = str(decision_reason)
    enrichment = opportunity.setdefault("enrichment", {})
    sources = list(enrichment.get("sources") or [])
    if source_kind not in sources:
        sources.append(source_kind)
    missing = []
    if not context.get("host"):
        missing.append("tns_reported_host")
    if not context.get("latestPublicPhotometry"):
        missing.append("latest_public_photometry")
    if not context.get("publicSpectra"):
        missing.append("latest_public_spectrum")
    enrichment.update(
        {
            "status": "partial" if missing else "complete",
            "sources": sources,
            "retrievedAtUTC": retrieved_at,
            "missing": missing,
        }
    )


def rate_limit_wait_seconds(headers: object) -> int:
    getter = getattr(headers, "get", None)
    if not getter:
        return 5
    retry_after = getter("Retry-After")
    if retry_after:
        try:
            return max(1, int(float(retry_after)))
        except ValueError:
            pass
    reset = getter("x-rate-limit-reset") or getter("X-Rate-Limit-Reset")
    if reset:
        try:
            reset_value = float(reset)
            now = dt.datetime.now(dt.UTC).timestamp()
            return max(1, math.ceil(reset_value - now) + 1) if reset_value > now else max(1, math.ceil(reset_value) + 1)
        except ValueError:
            pass
    return 5


def require_tns_bot_credentials(api_key: str, user_agent: str) -> None:
    if not api_key:
        raise ValueError("TNS API key is required for detailed object enrichment")
    if not user_agent.startswith("tns_marker{"):
        raise ValueError("TNS user agent must use the approved tns_marker{...} format")
    try:
        marker = json.loads(user_agent.removeprefix("tns_marker"))
    except (TypeError, json.JSONDecodeError) as error:
        raise ValueError("TNS user agent contains invalid marker JSON") from error
    if str(marker.get("type") or "").lower() != "bot":
        raise ValueError("TNS Get Object enrichment requires a bot marker")


def fetch_tns_object_detail(
    opportunity: dict[str, object],
    *,
    api_key: str,
    user_agent: str,
) -> tuple[dict[str, object], object]:
    require_tns_bot_credentials(api_key, user_agent)
    object_name = re.sub(
        r"^(?:AT|SN|TDE|SLSN|NOVA)(?=\d{4})",
        "",
        str(opportunity["sourceObjectName"]).replace(" ", ""),
        flags=re.I,
    )
    form = urllib.parse.urlencode(
        {
            "api_key": api_key,
            "data": json.dumps(
                {"objname": object_name, "photometry": "1", "spectra": "1"},
                separators=(",", ":"),
            ),
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        TNS_OBJECT_API_URL,
        data=form,
        headers={
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    payload: dict[str, object] = {}
    headers: object = {}
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read().decode("utf-8"))
                headers = response.headers
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 1:
                raise
            wait_seconds = rate_limit_wait_seconds(error.headers)
            error.close()
            if wait_seconds > 60:
                raise RuntimeError(
                    f"TNS rate limit resets in {wait_seconds}s; refusing an in-process wait over 60s"
                )
            time.sleep(wait_seconds)
            continue
        try:
            id_code = int(payload.get("id_code", 0))
        except (TypeError, ValueError):
            id_code = 0
        if id_code == 429 and attempt == 0:
            wait_seconds = rate_limit_wait_seconds(headers)
            if wait_seconds > 60:
                raise RuntimeError(
                    f"TNS rate limit resets in {wait_seconds}s; refusing an in-process wait over 60s"
                )
            time.sleep(wait_seconds)
            continue
        break
    else:  # pragma: no cover - the loop always returns or raises
        raise RuntimeError("TNS object enrichment failed")
    try:
        id_code = int(payload.get("id_code", 0))
    except (TypeError, ValueError):
        id_code = 0
    if id_code != 200:
        raise RuntimeError(
            f"TNS Get Object failed for {opportunity['sourceObjectName']}: "
            f"{payload.get('id_message') or payload.get('id_code')}"
        )
    reply = payload.get("data", {}).get("reply")
    if not isinstance(reply, dict):
        raise RuntimeError(f"TNS Get Object returned no object for {opportunity['sourceObjectName']}")
    return normalize_tns_detail(reply), headers


def enrich_queue_from_tns_api(
    queue: dict[str, object],
    *,
    api_key: str,
    user_agent: str,
    max_lookups: int = 5,
) -> None:
    require_tns_bot_credentials(api_key, user_agent)
    retrieved_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    opportunities = list(queue.get("opportunities", []))[:max_lookups]
    for index, opportunity in enumerate(opportunities):
        try:
            detail, headers = fetch_tns_object_detail(
                opportunity,
                api_key=api_key,
                user_agent=user_agent,
            )
        except Exception as error:
            if isinstance(error, urllib.error.HTTPError):
                failure = f"tns_http_{error.code}"
                error.close()
            elif "rate limit" in str(error).lower():
                failure = "tns_rate_limited"
            else:
                failure = "tns_detail_lookup_failed"
            enrichment = opportunity.setdefault("enrichment", {})
            sources = list(enrichment.get("sources") or [])
            if "tns_get_object_api" not in sources:
                sources.append("tns_get_object_api")
            enrichment.update(
                {
                    "status": "partial",
                    "sources": sources,
                    "retrievedAtUTC": retrieved_at,
                    "detailLookupError": failure,
                }
            )
            print(
                f"Warning: detailed TNS enrichment failed for "
                f"{opportunity.get('sourceObjectName')}: {failure}.",
                file=sys.stderr,
            )
            if failure == "tns_rate_limited":
                for remaining in opportunities[index + 1 :]:
                    remaining_enrichment = remaining.setdefault("enrichment", {})
                    remaining_sources = list(remaining_enrichment.get("sources") or [])
                    if "tns_get_object_api" not in remaining_sources:
                        remaining_sources.append("tns_get_object_api")
                    remaining_enrichment.update(
                        {
                            "status": "partial",
                            "sources": remaining_sources,
                            "retrievedAtUTC": retrieved_at,
                            "detailLookupError": "tns_rate_limited_before_lookup",
                        }
                    )
                break
            continue
        merge_tns_detail(
            opportunity,
            detail,
            retrieved_at=retrieved_at,
            source_kind="tns_get_object_api",
        )
        remaining = getattr(headers, "get", lambda _key: None)("x-rate-limit-remaining")
        if index + 1 < len(opportunities) and str(remaining) == "0":
            wait_seconds = rate_limit_wait_seconds(headers)
            if wait_seconds > 60:
                for pending in opportunities[index + 1 :]:
                    pending_enrichment = pending.setdefault("enrichment", {})
                    pending_sources = list(pending_enrichment.get("sources") or [])
                    if "tns_get_object_api" not in pending_sources:
                        pending_sources.append("tns_get_object_api")
                    pending_enrichment.update(
                        {
                            "status": "partial",
                            "sources": pending_sources,
                            "retrievedAtUTC": retrieved_at,
                            "detailLookupError": "tns_rate_limited_before_lookup",
                        }
                    )
                print(
                    f"Warning: TNS rate limit resets in {wait_seconds}s; "
                    "leaving remaining candidates partially enriched.",
                    file=sys.stderr,
                )
                break
            time.sleep(wait_seconds)


def apply_tns_details_file(queue: dict[str, object], path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    retrieved_at = str(payload.get("retrievedAtUTC") or "")
    if not retrieved_at:
        raise ValueError("TNS details file requires retrievedAtUTC")
    objects = payload.get("objects")
    if not isinstance(objects, dict):
        raise ValueError("TNS details file requires an objects mapping")
    for opportunity in queue.get("opportunities", []):
        keys = (str(opportunity.get("sourceId") or ""), str(opportunity.get("sourceObjectName") or ""))
        detail = next((objects[key] for key in keys if key in objects), None)
        if not isinstance(detail, dict):
            continue
        merge_tns_detail(
            opportunity,
            detail,
            retrieved_at=retrieved_at,
            source_kind=str(payload.get("sourceKind") or "tns_public_object_page"),
        )


def format_magnitude(value: object) -> str:
    return "—" if value is None else f"{float(value):.2f}".rstrip("0").rstrip(".")


def format_arcminutes(degrees: object) -> str:
    return f"{float(degrees) * 60.0:.2f}′"


def format_photometry(value: object) -> str:
    if not isinstance(value, dict):
        return "Not available in the staged feed"
    measurement = format_magnitude(value.get("value"))
    if value.get("isUpperLimit"):
        measurement = f"limit {measurement}"
    parts = [measurement]
    for key in ("units", "band", "instrument", "telescope"):
        if value.get(key):
            parts.append(str(value[key]))
    if value.get("observationDateUTC"):
        parts.append(str(value["observationDateUTC"]))
    return " · ".join(parts)


def format_spectra(value: object) -> str:
    if not isinstance(value, dict):
        return "Not included in this review snapshot"
    parts = [str(value.get("count", 0))]
    latest = value.get("latest") if isinstance(value.get("latest"), dict) else {}
    if latest:
        for key in ("observationDateUTC", "instrument", "sourceGroup"):
            if latest.get(key):
                parts.append(str(latest[key]))
    return " · ".join(parts)


def format_angular_size(target: dict[str, object]) -> str:
    major = target.get("angularSizeMajorArcmin")
    minor = target.get("angularSizeMinorArcmin")
    if major is not None and minor is not None:
        return f"{format_magnitude(major)}′ × {format_magnitude(minor)}′"
    if target.get("angularSizeArcmin") is not None:
        return f"{format_magnitude(target['angularSizeArcmin'])}′"
    return "—"


def humanize_reason(value: str) -> str:
    labels = {
        "classified_high_interest_transient": "confirmed high-interest transient class",
        "unclassified_transient_candidate": "unclassified transient candidate",
        "discovered_within_7_days": "discovered within 7 days",
        "discovered_within_30_days": "discovered within 30 days",
        "older_than_30_days": "older than 30 days",
        "discovery_magnitude_le_16_5": "discovery magnitude ≤16.5",
        "discovery_magnitude_le_18_5": "discovery magnitude ≤18.5",
        "discovery_magnitude_watch_band": "discovery magnitude in watch band",
        "separation_le_0_25_deg": "separation ≤0.25°",
        "separation_le_1_deg": "separation ≤1°",
        "separation_le_2_deg": "separation ≤2°",
        "nearby_catalog_object_is_galaxy": "nearby catalog subject is a galaxy",
        "recognizable_astroguide_subject": "recognizable AstroGuide subject",
    }
    return labels.get(value, value.replace("_", " "))


def humanize_object_type(value: object) -> str:
    text = str(value or "—")
    return {
        "Open_cluster": "Open cluster",
        "DarkNeb": "Dark nebula",
    }.get(text, text.replace("_", " "))


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
        f"**Review evidence hash:** `{queue.get('reviewSetID', 'legacy')}`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.",
        "",
        "## Summary",
        "",
        f"- {counts['reviewOpportunities']} review opportunities: {counts['urgent']} urgent, {counts['watch']} watch, {counts['expired']} expired",
        f"- Recommendations: {counts.get('recommendedApprove', 0)} approve, {counts.get('recommendedHold', 0)} hold, {counts.get('recommendedReject', 0)} reject",
        f"- {counts['eligibleReviewOpportunities']} eligible opportunities before the top-{counts['reviewOpportunitiesLimit'] or 'all'} review cap",
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
            target_name = review_target_name(target)
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
                        f"{target_name} ({humanize_object_type(target['objectType'])})",
                        f"{item['angularSeparationDegrees']:.5f}°",
                        relationship["wording"],
                        item["score"],
                        item.get("recommendedDecision") or item["recommendedReviewAction"],
                    )
                )
                + " |"
            )
        lines.append("")
        lines.extend(["## Candidate dossiers", ""])
        for index, item in enumerate(opportunities, start=1):
            discovery = item["discovery"]
            classification = item["classification"]
            context = item.get("tnsContext") or {}
            target = item["astroGuideObject"]
            target_name = review_target_name(target)
            thumbnail = target.get("catalogThumbnail") or {}
            relationship = item["relationship"]
            enrichment = item.get("enrichment") or {}
            coordinates = item["coordinates"]
            aladin_target = urllib.parse.quote(
                f"{coordinates['raDegrees']} {coordinates['decDegrees']}",
                safe="",
            )
            lines.extend(
                [
                    f"### {index}. [{item['sourceObjectName']}]({item['sourceURL']}) near {target_name}",
                    "",
                    f"**Recommendation:** `{item.get('recommendedDecision') or item['recommendedReviewAction']}` · **Priority:** `{item['urgency']}` · **Score:** {item['score']}/100",
                    "",
                ]
            )
            if item.get("decisionReason"):
                lines.extend([f"**Decision note:** {item['decisionReason']}", ""])
            if thumbnail.get("status") == "available":
                lines.extend(
                    [
                        f"![AstroGuide catalog thumbnail for {target_name}]({thumbnail['url']})",
                        "",
                        f"Catalog image: {thumbnail.get('attribution') or 'AstroGuide metadata asset'} · [open hosted image]({thumbnail['url']})",
                        "",
                    ]
                )
            else:
                lines.extend(
                    [
                        f"> **Catalog image:** {thumbnail.get('reason') or 'No governed hosted thumbnail is available.'}",
                        "",
                    ]
                )
            if relationship["type"] == RELATIONSHIP_NEAR_FIELD:
                lines.extend(
                    [
                        f"> **Near-field only:** TNS does not identify {target_name} as this object's host. The {item['angularSeparationDegrees']:.5f}° ({format_arcminutes(item['angularSeparationDegrees'])}) match is contextual, not a physical association.",
                        "",
                    ]
                )
            else:
                lines.extend(
                    [
                        f"> **Host evidence:** TNS reports `{relationship.get('tnsReportedHost')}` and it resolves to this AstroGuide subject.",
                        "",
                    ]
                )

            latest_photometry = context.get("latestPublicPhotometry")
            spectra = context.get("publicSpectra") if isinstance(context.get("publicSpectra"), dict) else {}
            host = context.get("host") if isinstance(context.get("host"), dict) else {}
            references = context.get("classificationReferences") or []
            discovery_reference = context.get("discoveryReference") or {}
            discovery_reference_link = (
                f"[{discovery_reference['bibcode']}]({discovery_reference['url']})"
                if discovery_reference.get("bibcode") and discovery_reference.get("url")
                else "—"
            )
            reference_links = ", ".join(
                f"[{reference['bibcode']}]({reference['url']})"
                for reference in references
                if isinstance(reference, dict) and reference.get("bibcode") and reference.get("url")
            ) or "—"
            age = "—" if discovery["ageDays"] is None else f"{discovery['ageDays']} days"
            identity_warning = target.get("identityWarning")
            enrichment_gaps = list(enrichment.get("missing") or [])
            if enrichment.get("detailLookupError"):
                enrichment_gaps.append(str(enrichment["detailLookupError"]))
            lines.extend(
                [
                    "| TNS context | Value |",
                    "|---|---|",
                    f"| Current classification | {markdown_escape(context.get('currentType') or classification.get('type') or classification.get('kind'))} |",
                    f"| Redshift | {markdown_escape(context.get('redshift') if context.get('redshift') is not None else '—')} |",
                    f"| TNS host | {markdown_escape(host.get('name') or relationship.get('tnsReportedHost') or 'Not supplied')} |",
                    f"| Host redshift | {markdown_escape(host.get('redshift') if host.get('redshift') is not None else '—')} |",
                    f"| Discovery | {markdown_escape(discovery.get('dateUTC') or '—')} · {age} · {format_magnitude(discovery.get('magnitude'))} {markdown_escape(discovery.get('band') or '')} |",
                    f"| Latest public photometry | {markdown_escape(format_photometry(latest_photometry))} |",
                    f"| Public spectra | {markdown_escape(format_spectra(spectra))} |",
                    f"| Discovery reference | {discovery_reference_link} |",
                    f"| Classification references | {reference_links} |",
                    f"| TNS remarks | {markdown_escape('; '.join(context.get('remarks') or []) or '—')} |",
                    f"| Enrichment | `{markdown_escape(enrichment.get('status') or 'partial')}` via {markdown_escape(', '.join(enrichment.get('sources') or []))} |",
                    f"| Enrichment retrieved | {markdown_escape(enrichment.get('retrievedAtUTC') or 'Staged record timestamp')} |",
                    f"| Enrichment gaps | {markdown_escape(', '.join(enrichment_gaps) or 'None')} |",
                    "",
                    "| AstroGuide catalog context | Value |",
                    "|---|---|",
                    f"| Subject | **{markdown_escape(target_name)}** · `{markdown_escape(target['id'])}` |",
                    f"| Catalog display name | {markdown_escape(target['displayName'])} |",
                    f"| Type / constellation | {markdown_escape(humanize_object_type(target.get('objectType')))} · {markdown_escape(target.get('constellation') or '—')} |",
                    f"| Catalog magnitude / angular size | {format_magnitude(target.get('magnitude'))} · {format_angular_size(target)} |",
                    f"| Distance | {markdown_escape(target.get('distance') or '—')} |",
                    f"| Separation | {item['angularSeparationDegrees']:.5f}° · {format_arcminutes(item['angularSeparationDegrees'])} |",
                    f"| Catalog description | {markdown_escape(target.get('description') or 'No catalog description available.')} |",
                    "",
                    *(
                        [f"> **Catalog data caution:** {markdown_escape(identity_warning)}", ""]
                        if identity_warning
                        else []
                    ),
                    "**Why it ranked:** " + "; ".join(humanize_reason(reason) for reason in item.get("reasonTags", [])) + ".",
                    "",
                    f"[TNS object]({item['sourceURL']}) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target={aladin_target}&fov=0.5&survey=P%2FDSS2%2Fcolor)",
                    "",
                ]
            )
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
    missing_dates = []
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
                error.close()
                missing_dates.append(date_text)
                print(
                    f"Warning: TNS staged delta is unavailable for {date_text}; "
                    "continuing with the remaining requested dates.",
                    file=sys.stderr,
                )
                continue
            raise
        path.write_bytes(payload)
        if not zipfile.is_zipfile(path):
            raise RuntimeError(f"TNS response is not a ZIP archive: {date_text}")
        paths.append(path)
    if missing_dates:
        print(
            f"Fetched {len(paths)} of {days} requested TNS staged deltas; "
            f"missing: {', '.join(missing_dates)}.",
            file=sys.stderr,
        )
    return paths


def meaningful_opportunities(queue: dict[str, object]) -> list[dict[str, object]]:
    material = json.loads(json.dumps(queue["opportunities"]))
    for item in material:
        item.get("provenance", {}).pop("inputRecords", None)
        item.get("enrichment", {}).pop("retrievedAtUTC", None)
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
    parser.add_argument(
        "--max-opportunities",
        type=int,
        default=0,
        help="Limit output to the top N sorted review opportunities; 0 means unlimited.",
    )
    parser.add_argument("--fetch-days", type=int, default=0)
    parser.add_argument("--staging-dir", type=Path, default=Path("work/tns"))
    parser.add_argument("--tns-user-agent", default=os.environ.get("TNS_USER_AGENT", ""))
    parser.add_argument("--tns-api-key", default=os.environ.get("TNS_API_KEY", ""))
    parser.add_argument(
        "--max-detail-lookups",
        type=int,
        default=5,
        help="Maximum selected candidates to enrich via TNS Get Object; capped at 5.",
    )
    parser.add_argument(
        "--target-image-package",
        type=Path,
        default=DEFAULT_TARGET_IMAGE_PACKAGE,
        help="AstroGuide targetImageAssets package used for governed thumbnails.",
    )
    parser.add_argument(
        "--tns-details-file",
        type=Path,
        help="Optional compact, public TNS detail snapshot to merge after selection.",
    )
    parser.add_argument(
        "--refresh-existing",
        type=Path,
        metavar="QUEUE_JSON",
        help="Refresh catalog context/rendering for an existing review queue without fetching.",
    )
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
            if item.get("recommendedDecision") not in (None, "approve", "hold", "reject"):
                raise RuntimeError("recommendedDecision must be approve, hold, or reject")
            thumbnail = item.get("astroGuideObject", {}).get("catalogThumbnail", {})
            if thumbnail.get("status") == "available" and not str(thumbnail.get("url") or "").startswith(
                "https://metadata.astroguide.space/"
            ):
                raise RuntimeError("catalog thumbnail must use the governed AstroGuide metadata origin")
        expected_review_set_id = review_set_identifier(queue.get("opportunities", []))
        if queue.get("reviewSetID") and queue.get("reviewSetID") != expected_review_set_id:
            raise RuntimeError("reviewSetID does not match the material review evidence")
        print(f"Validated {len(queue.get('opportunities', []))} review opportunities.")
        return 0

    if not args.catalog.is_file():
        parser.error(f"catalog does not exist: {args.catalog}")
    if args.max_detail_lookups < 0 or args.max_detail_lookups > 5:
        parser.error("--max-detail-lookups must be between 0 and 5")
    if args.tns_details_file and not args.tns_details_file.is_file():
        parser.error(f"TNS details file does not exist: {args.tns_details_file}")
    if args.target_image_package and not args.target_image_package.is_file():
        print(
            f"Warning: target image package not found at {args.target_image_package}; "
            "using explicit no-image fallbacks.",
            file=sys.stderr,
        )
    target_image_index = load_target_image_index(args.target_image_package)
    catalog, grid = load_catalog(args.catalog)

    if args.refresh_existing:
        if args.inputs or args.fetch_days:
            parser.error("--refresh-existing cannot be combined with staged inputs or --fetch-days")
        if not args.refresh_existing.is_file():
            parser.error(f"existing queue does not exist: {args.refresh_existing}")
        queue = json.loads(args.refresh_existing.read_text(encoding="utf-8"))
        refresh_existing_queue(queue, catalog, target_image_index)
        if args.tns_details_file:
            apply_tns_details_file(queue, args.tns_details_file)
        if args.tns_api_key and args.max_detail_lookups:
            enrich_queue_from_tns_api(
                queue,
                api_key=args.tns_api_key,
                user_agent=args.tns_user_agent,
                max_lookups=args.max_detail_lookups,
            )
        refresh_recommendation_counts(queue)
        queue["reviewSetID"] = review_set_identifier(queue.get("opportunities", []))
        json_path, markdown_path, _ = write_outputs(
            queue,
            args.refresh_existing.parent,
            skip_unchanged=False,
        )
        print(f"Refreshed {json_path} and {markdown_path}.")
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
        parser.error("no usable staged inputs were provided or fetched")
    missing = [path for path in inputs if not path.is_file()]
    if missing:
        parser.error(f"input does not exist: {missing[0]}")
    if args.max_opportunities < 0:
        parser.error("--max-opportunities must be non-negative")

    queue = build_queue(
        load_source_records(inputs),
        catalog,
        grid,
        as_of=args.as_of,
        target_image_index=target_image_index,
        radius_deg=args.radius_deg,
        max_age_days=args.max_age_days,
        watch_magnitude=args.watch_magnitude,
        max_opportunities=args.max_opportunities,
    )
    if args.tns_details_file:
        apply_tns_details_file(queue, args.tns_details_file)
    if args.tns_api_key and args.max_detail_lookups:
        enrich_queue_from_tns_api(
            queue,
            api_key=args.tns_api_key,
            user_agent=args.tns_user_agent,
            max_lookups=args.max_detail_lookups,
        )
    refresh_recommendation_counts(queue)
    queue["reviewSetID"] = review_set_identifier(queue.get("opportunities", []))
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
