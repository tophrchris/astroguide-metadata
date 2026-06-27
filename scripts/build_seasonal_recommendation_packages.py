#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import re
import sqlite3
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = Path("/Users/chollander/.codex/worktrees/dsoplannerios-dynamic-metadata-foundation")
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
MIN_MAX_ALT_DEGREES = 20.0

PACKAGE_FAMILY = "seasonalRecommendationCandidates"
TARGET_PACKAGE_PATHS = {
    "targetMetadataOverlay": Path("v1/packages/target-metadata/target_metadata_overlay_v1.json"),
    "targetNeighborhoodDefinitions": Path(
        "v1/packages/target-neighborhoods/target_neighborhood_definitions_v1.json"
    ),
    "equipmentCatalog": Path("v1/packages/equipment/equipment_catalog_v1.json"),
}
SEASONAL_PACKAGE_DIR = Path("v1/packages/seasonal-recommendations")

BANDS = {
    "north_high_60_90n": 75.0,
    "north_mid_30_60n": 45.0,
    "north_low_0_30n": 15.0,
    "south_low_0_30s": -15.0,
    "south_mid_30_60s": -45.0,
    "south_high_60_90s": -75.0,
}

MONTHS = [
    ("January", 5.78),
    ("February", 7.9),
    ("March", 9.66),
    ("April", 11.55),
    ("May", 13.46),
    ("June", 15.56),
    ("July", 17.62),
    ("August", 19.64),
    ("September", 21.52),
    ("October", 23.33),
    ("November", 1.35),
    ("December", 3.49),
]
MONTH_NAMES = [month for month, _ in MONTHS]

SPECTRUM_CAPS = {
    "broadband": 30,
    "narrowband": 30,
    "mixed": 15,
}

CATALOG_PREFERENCE = [
    ("Messier", re.compile(r"^M\d+[A-Z]?$")),
    ("NGC", re.compile(r"^NGC\d+[A-Z]?$")),
    ("IC", re.compile(r"^IC\d+[A-Z]?$")),
    ("Sharpless", re.compile(r"^(SH2|SH)\d+[A-Z]?$")),
    ("Caldwell", re.compile(r"^C\d+[A-Z]?$")),
    ("Lynds", re.compile(r"^(LBN|LDN)\d+[A-Z]?$")),
    ("VDB", re.compile(r"^VDB\d+[A-Z]?$")),
    ("Barnard", re.compile(r"^B\d+[A-Z]?$")),
    ("Collinder", re.compile(r"^(CR|COLLINDER)\d+[A-Z]?$")),
    ("Melotte", re.compile(r"^(MEL|MELOTTE)\d+[A-Z]?$")),
]
CATALOG_RANK = {name: index for index, (name, _) in enumerate(CATALOG_PREFERENCE)}
GENERIC_IDENTIFIERS = {
    "",
    "M",
    "NGC",
    "IC",
    "SH",
    "SH2",
    "C",
    "LBN",
    "LDN",
    "VDB",
    "B",
    "CR",
    "MEL",
    "ABL",
}


@dataclass(frozen=True)
class CatalogRow:
    object_id: str
    primary_name: str
    catalog_name: str
    object_type: str
    constellation: str
    magnitude: float | None
    size: float | None
    size_major: float | None
    size_minor: float | None
    ra_hours: float | None
    dec_degrees: float | None
    aliases: list[str]
    description: str
    image_url: str
    image_urls: str
    tokens: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class MetadataEntry:
    source: str
    canonical_id: str
    preferred_name: str
    aliases: list[str]
    catalog_object_id: str
    object_type: str
    visual_family: str
    signals: dict[str, Any]
    constellation: str
    ra_hours: float | None
    dec_degrees: float | None
    description: str = ""
    image_url: str = ""

    @property
    def is_target_metadata(self) -> bool:
        return self.source == "targetMetadataOverlay"

    @property
    def is_media(self) -> bool:
        return self.source == "targetMediaOverride"

    @property
    def tokens(self) -> set[str]:
        values = [
            self.canonical_id,
            self.catalog_object_id,
            self.preferred_name,
            *self.aliases,
        ]
        tokens: set[str] = set()
        for value in values:
            tokens.update(identifier_variants(value))
        return tokens


@dataclass
class Subject:
    subject_key: str
    display_name: str
    canonical_id: str
    object_type: str
    visual_family: str
    constellation: str
    ra_hours: float
    dec_degrees: float
    magnitude: float | None
    angular_size_arcmin: float | None
    aliases: list[str]
    catalog_ids: list[str]
    metadata_entries: list[MetadataEntry]
    description: str
    image_url: str
    catalog_preference: str
    catalog_rank: int
    recognition_rank: int

    @property
    def metadata_priority(self) -> bool:
        return any(entry.is_target_metadata for entry in self.metadata_entries)

    @property
    def has_media(self) -> bool:
        return bool(self.description or self.image_url or any(entry.is_media for entry in self.metadata_entries))


@dataclass(frozen=True)
class CandidateEntry:
    subject: Subject
    month: str
    spectrum: str
    ra_offset_hours: float
    center_fit: float
    max_altitude_degrees: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build banded AstroGuide seasonal recommendation dynamic metadata packages "
            "from the app catalog and target metadata overlay."
        )
    )
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument("--generated-at")
    parser.add_argument("--min-supported-app-version", default="0.1.2")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--skip-manifest", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(generated_at: str) -> str:
    return generated_at.split("T", maxsplit=1)[0]


def normalize_identifier(value: Any) -> str:
    text = str(value or "").strip().upper()
    text = text.replace("SH 2", "SH2").replace("SH-2", "SH2")
    text = text.replace("COLLINDER", "CR").replace("MELOTTE", "MEL")
    return re.sub(r"[^A-Z0-9]", "", text)


def split_aliases(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        parts = value
    else:
        parts = re.split(r"[|;]", str(value))
    return [str(part).strip() for part in parts if str(part).strip()]


def meaningful_identifier(value: Any) -> bool:
    token = normalize_identifier(value)
    if token in GENERIC_IDENTIFIERS or len(token) < 2:
        return False
    if token.isdigit():
        return False
    return bool(re.search(r"\d", token)) or len(token) >= 5


def identifier_variants(value: Any) -> set[str]:
    variants: set[str] = set()
    if value is None:
        return variants
    candidates = [str(value)]
    candidates.extend(split_aliases(value))
    for item in candidates:
        token = normalize_identifier(item)
        if meaningful_identifier(token):
            variants.add(token)
        compact_match = re.search(
            r"\b(M|NGC|IC|SH2|C|LBN|LDN|VDB|B|CR|MEL)\s*[- ]?\s*(\d+[A-Z]?)\b",
            item,
            flags=re.IGNORECASE,
        )
        if compact_match:
            variants.add(normalize_identifier(compact_match.group(1) + compact_match.group(2)))
    return {token for token in variants if meaningful_identifier(token)}


def clean_float(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def parse_ra(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value or "").strip()
    if not text:
        return None
    number = clean_float(text)
    if number is not None and ":" not in text:
        return number
    parts = [
        clean_float(part)
        for part in text.replace("h", ":").replace("m", ":").replace("s", "").split(":")
    ]
    if not parts or parts[0] is None:
        return None
    hours = parts[0]
    minutes = parts[1] if len(parts) > 1 and parts[1] is not None else 0.0
    seconds = parts[2] if len(parts) > 2 and parts[2] is not None else 0.0
    return (hours + minutes / 60.0 + seconds / 3600.0) % 24.0


def parse_dec(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value or "").strip().replace("−", "-")
    if not text:
        return None
    number = clean_float(text)
    if number is not None and ":" not in text:
        return number
    sign = -1.0 if text.startswith("-") else 1.0
    parts = [
        clean_float(part)
        for part in text.lstrip("+-").replace("d", ":").replace("m", ":").replace("s", "").split(":")
    ]
    if not parts or parts[0] is None:
        return None
    degrees = abs(parts[0])
    minutes = parts[1] if len(parts) > 1 and parts[1] is not None else 0.0
    seconds = parts[2] if len(parts) > 2 and parts[2] is not None else 0.0
    return sign * (degrees + minutes / 60.0 + seconds / 3600.0)


def catalog_preference(tokens: set[str]) -> tuple[str, int]:
    best_name = "Other"
    best_rank = len(CATALOG_PREFERENCE)
    for token in tokens:
        for name, pattern in CATALOG_PREFERENCE:
            if pattern.match(token) and CATALOG_RANK[name] < best_rank:
                best_name = name
                best_rank = CATALOG_RANK[name]
    return best_name, best_rank


def catalog_id_sort_key(value: str) -> tuple[int, int, str]:
    token = normalize_identifier(value)
    _, rank = catalog_preference({token})
    match = re.search(r"(\d+)", token)
    number = int(match.group(1)) if match else 999999
    return rank, number, token


def common_name(name: str, object_id: str) -> bool:
    normalized_name = normalize_identifier(name)
    if not normalized_name or normalized_name == normalize_identifier(object_id):
        return False
    return not any(pattern.match(normalized_name) for _, pattern in CATALOG_PREFERENCE)


def infer_visual_family(object_type: str) -> str:
    text = normalize_identifier(object_type).lower()
    if "galaxy" in text:
        return "galaxy"
    if "globular" in text or "cluster" in text or "asterism" in text:
        return "cluster"
    if "planetary" in text:
        return "planetaryNebula"
    if "supernova" in text or text == "snr":
        return "supernovaRemnant"
    if "dark" in text:
        return "darkNebula"
    if "reflection" in text:
        return "reflectionNebula"
    if "emission" in text or "hii" in text or "nebula" in text:
        return "emissionNebula"
    if "star" in text:
        return "star"
    return "other"


def signal_strength(signals: dict[str, Any], key: str) -> str:
    value = signals.get(key)
    if isinstance(value, dict):
        value = value.get("strength")
    return str(value or "").strip().lower()


def strongest_signal(entries: list[MetadataEntry], key: str) -> str:
    ranks = {
        "none": 0,
        "unknown": 1,
        "weak": 2,
        "moderate": 3,
        "strong": 4,
    }
    best = ""
    best_rank = -1
    for entry in entries:
        strength = signal_strength(entry.signals, key)
        rank = ranks.get(strength, -1)
        if rank > best_rank:
            best = strength
            best_rank = rank
    return best


def infer_spectrum(subject: Subject) -> str:
    object_text = f"{subject.object_type} {subject.visual_family}".lower()
    ha = strongest_signal(subject.metadata_entries, "hAlpha")
    oiii = strongest_signal(subject.metadata_entries, "oxygenIII")
    sii = strongest_signal(subject.metadata_entries, "sulfurII")
    continuum = strongest_signal(subject.metadata_entries, "continuum")
    reflection = strongest_signal(subject.metadata_entries, "reflection")
    dust = strongest_signal(subject.metadata_entries, "dust")
    has_emission = any(value == "strong" for value in [ha, oiii, sii])
    has_continuum = any(value == "strong" for value in [continuum, reflection, dust])

    if has_emission and has_continuum:
        return "mixed"
    if "galaxy" in object_text and has_emission and continuum in {"moderate", "strong"}:
        return "mixed"
    if has_emission:
        return "narrowband"
    if any(token in object_text for token in ["planetary", "supernova", "emission", "hii"]):
        return "narrowband"
    return "broadband"


def max_altitude(latitude_degrees: float, dec_degrees: float) -> float:
    return max(-90.0, min(90.0, 90.0 - abs(latitude_degrees - dec_degrees)))


def signed_ra_offset(ra_hours: float, center_hours: float) -> float:
    return ((ra_hours - center_hours + 12.0) % 24.0) - 12.0


def center_fit_score(offset_hours: float) -> float:
    return max(0.0, 1.0 - abs(offset_hours) / 2.5)


def challenge_rating(subject: Subject) -> str:
    magnitude = subject.magnitude
    size = subject.angular_size_arcmin
    if magnitude is None and size is None:
        return "unresolved"
    if magnitude is not None and magnitude <= 7.5:
        return "easy"
    if size is not None and size >= 45 and (magnitude is None or magnitude <= 10.5):
        return "easy"
    if magnitude is not None and magnitude <= 10.5:
        return "moderate"
    if size is not None and size >= 20:
        return "moderate"
    if magnitude is not None and magnitude <= 13.5:
        return "challenging"
    return "demanding"


def size_facet(size: float | None) -> str:
    if size is None:
        return "unresolved"
    if size < 20:
        return "small"
    if size < 60:
        return "medium"
    return "large"


def read_catalog(app_repo: Path) -> list[CatalogRow]:
    catalog_db = app_repo / "App/Resources/Catalog/catalog.sqlite"
    if not catalog_db.exists():
        raise RuntimeError(f"Catalog database not found: {catalog_db}")
    query = """
        select object_id, primary_name, catalog_name, object_type, constellation,
               magnitude, angular_size_arcmin, angular_size_maj_arcmin,
               angular_size_min_arcmin, ra_hours, dec_degrees, aliases,
               description, image_url, image_urls
          from deep_sky_objects
    """
    rows: list[CatalogRow] = []
    with sqlite3.connect(catalog_db) as db:
        db.row_factory = sqlite3.Row
        for row in db.execute(query):
            aliases = split_aliases(row["aliases"])
            values = [
                row["object_id"],
                row["primary_name"],
                row["catalog_name"],
                *aliases,
            ]
            tokens: set[str] = set()
            for value in values:
                tokens.update(identifier_variants(value))
            rows.append(
                CatalogRow(
                    object_id=row["object_id"] or "",
                    primary_name=row["primary_name"] or "",
                    catalog_name=row["catalog_name"] or "",
                    object_type=row["object_type"] or "",
                    constellation=row["constellation"] or "",
                    magnitude=row["magnitude"],
                    size=row["angular_size_arcmin"],
                    size_major=row["angular_size_maj_arcmin"],
                    size_minor=row["angular_size_min_arcmin"],
                    ra_hours=row["ra_hours"],
                    dec_degrees=row["dec_degrees"],
                    aliases=aliases,
                    description=row["description"] or "",
                    image_url=row["image_url"] or "",
                    image_urls=row["image_urls"] or "",
                    tokens=tokens,
                )
            )
    return rows


def load_metadata_entries(app_repo: Path) -> list[MetadataEntry]:
    dynamic_dir = app_repo / "App/Resources/DynamicMetadata/TargetMetadata"
    overlay = read_json(dynamic_dir / "target_metadata_overlay_v1.json")
    neighborhoods = read_json(dynamic_dir / "target_neighborhood_definitions_v1.json")
    entries: list[MetadataEntry] = []

    for item in overlay.get("targets") or []:
        resolution = item.get("resolution") or {}
        entries.append(
            MetadataEntry(
                source="targetMetadataOverlay",
                canonical_id=item.get("canonicalID", ""),
                preferred_name=item.get("preferredName", ""),
                aliases=split_aliases(item.get("aliases")),
                catalog_object_id=resolution.get("catalogObjectID", ""),
                object_type=item.get("curatedObjectTypeDisplayName", "")
                or item.get("curatedObjectTypeRaw", ""),
                visual_family=item.get("curatedVisualFamily", ""),
                signals=item.get("signals") or {},
                constellation=item.get("constellation", ""),
                ra_hours=parse_ra(item.get("rightAscensionJ2000")),
                dec_degrees=parse_dec(item.get("declinationJ2000")),
            )
        )

    for item in overlay.get("mediaOverrides") or []:
        entries.append(
            MetadataEntry(
                source="targetMediaOverride",
                canonical_id=item.get("canonicalID", ""),
                preferred_name="",
                aliases=[],
                catalog_object_id=item.get("canonicalID", ""),
                object_type="",
                visual_family="",
                signals={},
                constellation="",
                ra_hours=None,
                dec_degrees=None,
                description=item.get("description", ""),
                image_url=item.get("imageURL", ""),
            )
        )

    for neighborhood in neighborhoods.get("neighborhoods") or []:
        name = neighborhood.get("name", "")
        for catalog_id in neighborhood.get("catalogIDs") or []:
            entries.append(
                MetadataEntry(
                    source="targetNeighborhoodDefinitions",
                    canonical_id=catalog_id,
                    preferred_name=name,
                    aliases=[catalog_id],
                    catalog_object_id=catalog_id,
                    object_type="",
                    visual_family="",
                    signals={},
                    constellation="",
                    ra_hours=None,
                    dec_degrees=None,
                )
            )
    return entries


def metadata_index(entries: list[MetadataEntry]) -> dict[str, list[MetadataEntry]]:
    index: dict[str, list[MetadataEntry]] = defaultdict(list)
    for entry in entries:
        for token in entry.tokens:
            index[token].append(entry)
    return index


def build_subjects(catalog_rows: list[CatalogRow], metadata_entries: list[MetadataEntry]) -> list[Subject]:
    meta_by_token = metadata_index(metadata_entries)
    matched_entries: set[int] = set()
    subjects: list[Subject] = []
    for row in catalog_rows:
        if row.ra_hours is None or row.dec_degrees is None:
            continue
        row_entries: list[MetadataEntry] = []
        seen_keys: set[tuple[str, str, str]] = set()
        for token in row.tokens:
            for entry in meta_by_token.get(token, []):
                key = (entry.source, entry.canonical_id, entry.catalog_object_id)
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                row_entries.append(entry)
                matched_entries.add(id(entry))
        subject = subject_from_catalog_row(row, row_entries)
        if subject:
            subjects.append(subject)

    for entry in metadata_entries:
        if id(entry) in matched_entries or not entry.is_target_metadata:
            continue
        if entry.ra_hours is None or entry.dec_degrees is None:
            continue
        subject = subject_from_metadata_entry(entry)
        if subject:
            subjects.append(subject)

    deduped: dict[str, Subject] = {}
    for subject in subjects:
        key = normalize_identifier(subject.subject_key or subject.canonical_id or subject.display_name)
        existing = deduped.get(key)
        if existing is None or subject_sort_strength(subject) < subject_sort_strength(existing):
            deduped[key] = subject
    return sorted(deduped.values(), key=lambda subject: normalize_identifier(subject.subject_key))


def subject_sort_strength(subject: Subject) -> tuple[Any, ...]:
    return (
        0 if subject.metadata_priority else 1,
        subject.recognition_rank,
        subject.catalog_rank,
        0 if subject.has_media else 1,
        0 if subject.magnitude is not None and subject.angular_size_arcmin is not None else 1,
        normalize_identifier(subject.display_name),
    )


def subject_from_catalog_row(row: CatalogRow, entries: list[MetadataEntry]) -> Subject | None:
    entries = sorted(entries, key=lambda entry: (0 if entry.is_target_metadata else 1, entry.preferred_name))
    target_entries = [entry for entry in entries if entry.is_target_metadata]
    primary = target_entries[0] if target_entries else entries[0] if entries else None
    canonical_id = (
        primary.catalog_object_id
        if primary and primary.catalog_object_id
        else row.object_id
    )
    subject_key = canonical_id or row.object_id
    display_name = (
        primary.preferred_name
        if primary and primary.preferred_name
        else row.primary_name
        if common_name(row.primary_name, row.object_id)
        else canonical_id
    )
    object_type = (
        primary.object_type
        if primary and primary.object_type
        else row.object_type
    )
    visual_family = (
        primary.visual_family
        if primary and primary.visual_family
        else infer_visual_family(object_type)
    )
    size = row.size if row.size is not None else row.size_major if row.size_major is not None else row.size_minor
    aliases: set[str] = set(row.aliases)
    if row.catalog_name:
        aliases.add(row.catalog_name)
    for entry in entries:
        aliases.update(entry.aliases)
        if entry.preferred_name:
            aliases.add(entry.preferred_name)
    tokens = set(row.tokens)
    for entry in entries:
        tokens.update(entry.tokens)
    pref_name, pref_rank = catalog_preference(tokens)
    recognition_rank = 0 if target_entries else 1 if common_name(display_name, subject_key) or row.description or row.image_url else 2
    description = first_text([entry.description for entry in entries] + [row.description])
    image_url = first_text([entry.image_url for entry in entries] + [row.image_url, row.image_urls])

    return Subject(
        subject_key=subject_key,
        display_name=display_name or subject_key,
        canonical_id=canonical_id,
        object_type=object_type,
        visual_family=valid_visual_family(visual_family),
        constellation=primary.constellation if primary and primary.constellation else row.constellation,
        ra_hours=float(row.ra_hours),
        dec_degrees=float(row.dec_degrees),
        magnitude=row.magnitude,
        angular_size_arcmin=size,
        aliases=clean_aliases(aliases, subject_key),
        catalog_ids=[row.object_id],
        metadata_entries=entries,
        description=description,
        image_url=image_url,
        catalog_preference=pref_name,
        catalog_rank=pref_rank,
        recognition_rank=recognition_rank,
    )


def subject_from_metadata_entry(entry: MetadataEntry) -> Subject | None:
    if entry.ra_hours is None or entry.dec_degrees is None:
        return None
    tokens = entry.tokens
    pref_name, pref_rank = catalog_preference(tokens)
    canonical_id = entry.catalog_object_id or entry.canonical_id
    display_name = entry.preferred_name or canonical_id
    return Subject(
        subject_key=canonical_id,
        display_name=display_name,
        canonical_id=canonical_id,
        object_type=entry.object_type,
        visual_family=valid_visual_family(entry.visual_family or infer_visual_family(entry.object_type)),
        constellation=entry.constellation,
        ra_hours=entry.ra_hours,
        dec_degrees=entry.dec_degrees,
        magnitude=None,
        angular_size_arcmin=None,
        aliases=clean_aliases(set(entry.aliases), canonical_id),
        catalog_ids=[],
        metadata_entries=[entry],
        description=entry.description,
        image_url=entry.image_url,
        catalog_preference=pref_name,
        catalog_rank=pref_rank,
        recognition_rank=0,
    )


def valid_visual_family(value: str) -> str:
    valid = {
        "comet",
        "galaxy",
        "emissionNebula",
        "reflectionNebula",
        "planetaryNebula",
        "supernovaRemnant",
        "brightNebula",
        "darkNebula",
        "cluster",
        "star",
        "other",
    }
    if value in valid:
        return value
    return infer_visual_family(value)


def first_text(values: list[str]) -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return ""


def clean_aliases(values: set[str], subject_key: str) -> list[str]:
    subject_norm = normalize_identifier(subject_key)
    result = []
    seen = set()
    for value in sorted(values):
        text = str(value or "").strip()
        if not text:
            continue
        norm = normalize_identifier(text)
        if not norm or norm == subject_norm or norm in seen:
            continue
        seen.add(norm)
        result.append(text)
    return result[:18]


def build_candidates(subjects: list[Subject], latitude_degrees: float) -> dict[tuple[str, str], list[CandidateEntry]]:
    by_bucket: dict[tuple[str, str], list[CandidateEntry]] = defaultdict(list)
    for subject in subjects:
        altitude = max_altitude(latitude_degrees, subject.dec_degrees)
        if altitude < MIN_MAX_ALT_DEGREES:
            continue
        spectrum = infer_spectrum(subject)
        for month, center in MONTHS:
            offset = signed_ra_offset(subject.ra_hours, center)
            if abs(offset) > 2.5:
                continue
            by_bucket[(month, spectrum)].append(
                CandidateEntry(
                    subject=subject,
                    month=month,
                    spectrum=spectrum,
                    ra_offset_hours=offset,
                    center_fit=center_fit_score(offset),
                    max_altitude_degrees=altitude,
                )
            )
    return by_bucket


def entry_score(entry: CandidateEntry, used_counts: Counter[str], month_subjects: set[str]) -> float:
    subject = entry.subject
    subject_id = normalize_identifier(subject.subject_key)
    score = 0.0
    if subject.metadata_priority:
        score += 1000
    score += max(0, 100 - subject.catalog_rank * 8)
    score += max(0, 80 - subject.recognition_rank * 20)
    if subject.has_media:
        score += 18
    if subject.magnitude is not None:
        score += max(0.0, 15.0 - min(15.0, subject.magnitude))
    if subject.angular_size_arcmin is not None:
        score += 8
    score += max(0.0, min(20.0, (entry.max_altitude_degrees - MIN_MAX_ALT_DEGREES) / 3.5))
    score += entry.center_fit * 25.0
    score -= used_counts[subject_id] * 80
    if subject_id in month_subjects:
        score -= 300
    return round(score, 4)


def pass_allows(entry: CandidateEntry, used_counts: Counter[str], pass_name: str) -> bool:
    used_before = used_counts[normalize_identifier(entry.subject.subject_key)] > 0
    metadata = entry.subject.metadata_priority
    if pass_name == "unique-metadata":
        return metadata and not used_before
    if pass_name == "repeat-metadata":
        return metadata and used_before
    if pass_name == "unique-quality":
        return not metadata and not used_before
    if pass_name == "repeat-quality":
        return not metadata and used_before
    return False


def sort_candidates(
    entries: list[CandidateEntry],
    used_counts: Counter[str],
    month_subjects: set[str],
    pass_name: str,
) -> list[CandidateEntry]:
    def key(entry: CandidateEntry) -> tuple[Any, ...]:
        subject = entry.subject
        prior_uses = used_counts[normalize_identifier(subject.subject_key)]
        return (
            0 if subject.metadata_priority else 1,
            subject.recognition_rank,
            subject.catalog_rank,
            prior_uses,
            -entry_score(entry, used_counts, month_subjects),
            -entry.center_fit,
            -entry.max_altitude_degrees,
            normalize_identifier(subject.display_name),
        )

    return sorted(
        (entry for entry in entries if pass_allows(entry, used_counts, pass_name)),
        key=key,
    )


def selected_rows_for_band(subjects: list[Subject], band: str, latitude_degrees: float) -> list[dict[str, Any]]:
    candidates = build_candidates(subjects, latitude_degrees)
    used_counts: Counter[str] = Counter()
    selected: list[dict[str, Any]] = []
    priority_rank = 0

    for month, _ in MONTHS:
        for spectrum in ["broadband", "narrowband", "mixed"]:
            bucket = candidates.get((month, spectrum), [])
            cap = SPECTRUM_CAPS[spectrum]
            chosen: list[tuple[CandidateEntry, str]] = []
            month_subjects = {
                normalize_identifier(row["subjectKey"])
                for row in selected
                if row["month"] == month
            }
            for pass_name in ["unique-metadata", "repeat-metadata", "unique-quality", "repeat-quality"]:
                if len(chosen) >= cap:
                    break
                for entry in sort_candidates(bucket, used_counts, month_subjects, pass_name):
                    subject_id = normalize_identifier(entry.subject.subject_key)
                    if subject_id in month_subjects:
                        continue
                    chosen.append((entry, pass_name))
                    month_subjects.add(subject_id)
                    if len(chosen) >= cap:
                        break

            for bucket_rank, (entry, pass_name) in enumerate(chosen, start=1):
                subject = entry.subject
                subject_id = normalize_identifier(subject.subject_key)
                priority_rank += 1
                flags = []
                if not subject.metadata_priority:
                    flags.append("notInTargetMetadata")
                if not subject.description:
                    flags.append("missingDescription")
                if not subject.image_url:
                    flags.append("missingImage")
                if subject.magnitude is None:
                    flags.append("missingMagnitude")
                if subject.angular_size_arcmin is None:
                    flags.append("missingSize")

                priority_tier = (
                    "1 TargetMetadata"
                    if subject.metadata_priority
                    else "2 Recognizable catalog target"
                    if subject.recognition_rank <= 1
                    else "3 Complete catalog target"
                )
                notes = [
                    priority_tier,
                    f"catalog={subject.catalog_preference}",
                    f"selection={pass_name}",
                    f"centerFit={entry.center_fit:.2f}",
                    (
                        "maxAltitudeAt45North contains representative-band max altitude "
                        f"for {band} compatibility."
                    ),
                ]
                selected.append(
                    {
                        "month": month,
                        "subjectKey": subject.subject_key,
                        "canonicalID": subject.canonical_id,
                        "displayName": subject.display_name,
                        "aliases": subject.aliases,
                        "spectrum": spectrum,
                        "seasonStatus": "peak",
                        "challengeRating": challenge_rating(subject),
                        "sizeFacet": size_facet(subject.angular_size_arcmin),
                        "magnitude": rounded(subject.magnitude, 3),
                        "angularSizeArcmin": rounded(subject.angular_size_arcmin, 3),
                        "maxAltitudeAt45North": rounded(entry.max_altitude_degrees, 1),
                        "maxAltitudeAtRepresentativeLatitude": rounded(entry.max_altitude_degrees, 1),
                        "objectType": subject.object_type,
                        "visualFamily": subject.visual_family,
                        "constellation": subject.constellation,
                        "rightAscensionHours": rounded(subject.ra_hours, 4),
                        "declinationDegrees": rounded(subject.dec_degrees, 4),
                        "priorityTier": priority_tier,
                        "dataFlags": flags,
                        "notes": " | ".join(notes),
                        "_bucketRank": bucket_rank,
                        "_priorityRank": priority_rank,
                    }
                )
                used_counts[subject_id] += 1

    derive_season_status(selected)
    for row in selected:
        row.pop("_bucketRank", None)
        row.pop("_priorityRank", None)
        compact_optional_fields(row)
    return selected


def rounded(value: float | None, digits: int) -> float | None:
    if value is None:
        return None
    return round(float(value), digits)


def compact_optional_fields(row: dict[str, Any]) -> None:
    for key in [
        "magnitude",
        "angularSizeArcmin",
        "maxAltitudeAt45North",
        "maxAltitudeAtRepresentativeLatitude",
        "objectType",
        "visualFamily",
        "constellation",
        "rightAscensionHours",
        "declinationDegrees",
        "priorityTier",
        "notes",
    ]:
        if row.get(key) in {None, ""}:
            row.pop(key, None)
    if not row.get("aliases"):
        row["aliases"] = []
    if not row.get("dataFlags"):
        row["dataFlags"] = []


def derive_season_status(rows: list[dict[str, Any]]) -> None:
    present_by_month: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        present_by_month[row["month"]].add(normalize_identifier(f"{row['subjectKey']}:{row['spectrum']}"))

    month_index = {month: index for index, month in enumerate(MONTH_NAMES)}
    for row in rows:
        subject_key = normalize_identifier(f"{row['subjectKey']}:{row['spectrum']}")
        index = month_index[row["month"]]
        previous_month = MONTH_NAMES[(index - 1) % len(MONTH_NAMES)]
        next_month = MONTH_NAMES[(index + 1) % len(MONTH_NAMES)]
        present_previous = subject_key in present_by_month[previous_month]
        present_next = subject_key in present_by_month[next_month]
        if not present_previous and present_next:
            row["seasonStatus"] = "rising"
        elif present_previous and not present_next:
            row["seasonStatus"] = "leaving"
        else:
            row["seasonStatus"] = "peak"


def build_package(
    *,
    band: str,
    latitude_degrees: float,
    rows: list[dict[str, Any]],
    generated_at: str,
) -> dict[str, Any]:
    if not rows:
        raise RuntimeError(f"No legitimate seasonal recommendation rows generated for {band}.")
    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": f"{band}-catalog-targetmetadata-seasonal-v1-{date_token(generated_at)}",
        "latitudeBand": band,
        "representativeLatitudeDegrees": latitude_degrees,
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide catalog and target metadata seasonal recommendations",
            "generatedBy": "scripts/build_seasonal_recommendation_packages.py",
            "sourceURL": "https://github.com/tophrchris/DSOPlanneriOS/tree/main/App/Resources",
            "notes": (
                "Derived from the app catalog.sqlite plus dynamic target metadata overlay and "
                "target neighborhood packages. Uses the prime-time monthly RA centers from the "
                "north-mid review pipeline, applies a band-specific representative-latitude "
                "max-altitude filter, and does not add placeholder rows."
            ),
        },
        "rows": rows,
    }


def package_descriptor(
    *,
    family: str,
    package: dict[str, Any],
    package_path: Path,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict[str, Any]:
    descriptor: dict[str, Any] = {
        "family": family,
        "packageVersion": package["packageVersion"],
        "payloadSchemaVersion": package["schemaVersion"],
        "packageURL": f"{METADATA_ORIGIN}/{package_path.as_posix()}",
        "checksum": {
            "algorithm": "sha256",
            "value": hashlib.sha256(data).hexdigest(),
        },
        "byteSize": len(data),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": fallback_notes(family),
    }
    if family == PACKAGE_FAMILY:
        descriptor["latitudeBand"] = package["latitudeBand"]
    return descriptor


def fallback_notes(family: str) -> str:
    if family == PACKAGE_FAMILY:
        return (
            "Use the bundled seasonal recommendation snapshot for this latitude band only if no "
            "validated cached package is available. Cache TTL indicates when the app should check "
            "for a fresher package; an expired cached package remains usable until replaced by a "
            "validated refresh."
        )
    if family == "equipmentCatalog":
        return (
            "Use the bundled equipment catalog only if no validated cached package is available. "
            "Cache TTL indicates when the app should check for a fresher package; an expired cached "
            "package remains usable until replaced by a validated refresh."
        )
    return (
        "Use the bundled target metadata snapshot only if no validated cached package is available. "
        "Cache TTL indicates when the app should check for a fresher package; an expired cached "
        "package remains usable until replaced by a validated refresh."
    )


def update_manifest(
    generated_at: str,
    descriptors: list[dict[str, Any]],
) -> None:
    manifest_path = REPO_ROOT / "v1/channels/stable/manifest.json"
    manifest = read_json(manifest_path)
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(descriptors)
    write_json(manifest_path, manifest)


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {
        "targetMetadataOverlay": 0,
        "targetNeighborhoodDefinitions": 1,
        "equipmentCatalog": 2,
        PACKAGE_FAMILY: 3,
    }
    band_order = {band: index for index, band in enumerate(BANDS)}

    def key(entry: dict[str, Any]) -> tuple[int, int, str]:
        family = entry.get("family", "")
        return (
            family_order.get(family, 99),
            band_order.get(entry.get("latitudeBand", ""), 99),
            entry.get("packageVersion", ""),
        )

    return sorted(packages, key=key)


def descriptors_for_existing_target_packages(
    min_supported_app_version: str,
    min_supported_build: str,
) -> list[dict[str, Any]]:
    descriptors = []
    for family, relative_path in TARGET_PACKAGE_PATHS.items():
        package_path = REPO_ROOT / relative_path
        package = read_json(package_path)
        data = package_path.read_bytes()
        descriptors.append(
            package_descriptor(
                family=family,
                package=package,
                package_path=relative_path,
                data=data,
                min_supported_app_version=min_supported_app_version,
                min_supported_build=min_supported_build,
            )
        )
    return descriptors


def main() -> int:
    args = parse_args()
    app_repo = args.app_repo.resolve()
    generated_at = args.generated_at or utc_now()
    catalog_rows = read_catalog(app_repo)
    metadata_entries = load_metadata_entries(app_repo)
    subjects = build_subjects(catalog_rows, metadata_entries)
    if not subjects:
        raise RuntimeError("No subjects could be built from catalog and target metadata sources.")

    descriptors = descriptors_for_existing_target_packages(
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
    )
    for band, latitude_degrees in BANDS.items():
        rows = selected_rows_for_band(subjects, band, latitude_degrees)
        package = build_package(
            band=band,
            latitude_degrees=latitude_degrees,
            rows=rows,
            generated_at=generated_at,
        )
        relative_path = SEASONAL_PACKAGE_DIR / f"seasonal_recommendation_candidates_{band}_v1.json"
        data = write_json(REPO_ROOT / relative_path, package)
        descriptors.append(
            package_descriptor(
                family=PACKAGE_FAMILY,
                package=package,
                package_path=relative_path,
                data=data,
                min_supported_app_version=args.min_supported_app_version,
                min_supported_build=args.min_supported_build,
            )
        )
        print(f"{band}: {len(rows)} rows {len(data)} bytes {hashlib.sha256(data).hexdigest()}")

    if not args.skip_manifest:
        update_manifest(generated_at, descriptors)
        print("Updated v1/channels/stable/manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
