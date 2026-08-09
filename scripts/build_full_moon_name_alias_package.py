#!/usr/bin/env python3
"""Build and validate AstroGuide Full Moon name/alias metadata."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_PATH = Path(
    "sources/full-moon-name-aliases/full_moon_name_aliases_v1.json"
)
DEFAULT_PACKAGE_PATH = Path(
    "v1/packages/full-moon-name-aliases/full_moon_name_alias_metadata_v1.json"
)
DEFAULT_MANIFEST_PATH = Path("v1/channels/stable/manifest.json")
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "fullMoonNameAliases"
PACKAGE_ROLE = "catalog"
RESOLVER_ID = "gregorianMonthOfContainedFullMoon"
PACKAGE_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
CONFIDENCE_VALUES = {"high", "medium", "low", "mixed"}
PROVENANCE_VALUES = {
    "primarySource",
    "authoritativeCompilation",
    "editorialCompilation",
    "institutionalSecondary",
    "unresolvedCompilation",
}
LICENSE_VALUES = {"clear", "attributionRequired", "reviewRequired", "permissionRequired", "unknown"}
USAGE_REVIEW_VALUES = {"ready", "reviewRequired", "permissionRequired", "researchOnly"}
FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "darkSkyPlaces",
    "cometSnapshot",
    "planetCatalog",
    "lunarEvents",
    PACKAGE_FAMILY,
    "planetTargetCloseEncounters",
    "seasonalRecommendationCandidates",
    "transientEventFeed",
]
FORBIDDEN_RECORD_KEYS = {
    "lunationID",
    "lunationId",
    "phaseEventID",
    "phaseEventId",
    "cycleStart",
    "cycleEnd",
    "eventTimeUTC",
    "fullMoonDate",
    "fullMoonInstant",
    "observerLocation",
    "observerSite",
    "timezone",
    "supermoon",
    "micromoon",
    "eclipse",
    "blueMoon",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build the hosted AstroGuide Full Moon name/alias package and refresh "
            "the stable manifest."
        )
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_PACKAGE_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--min-supported-app-version", default="1.4.0")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the existing package and stable-manifest integrity chain.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = repo_path(args.source)
    output_path = repo_path(args.output)
    manifest_path = repo_path(args.manifest)

    if args.validate_only:
        package = read_json(output_path)
        validate_package(package)
        data = output_path.read_bytes()
        if data != json_bytes(package, compact=True):
            raise RuntimeError("Package serialization is not canonical compact JSON.")
        if not args.skip_manifest:
            validate_manifest_descriptor(manifest_path, package, data, output_path)
        print(
            f"Validated {repo_relative(output_path)}: "
            f"{package['counts']['entries']} entries, "
            f"{package['counts']['nameClaims']} name claims."
        )
        return 0

    source = read_json(source_path)
    validate_source(source)
    package = build_package(source)
    validate_package(package)
    data = write_json(output_path, package, compact=True)
    descriptor = descriptor_for_package(package, data, args, output_path)
    if not args.skip_manifest:
        update_manifest(manifest_path, str(package["generatedAt"]), descriptor)
        validate_manifest_descriptor(manifest_path, package, data, output_path)
    print(
        f"{PACKAGE_FAMILY}: {package['packageVersion']} "
        f"{package['counts']['entries']} entries, "
        f"{package['counts']['aliasNames']} alias rows, "
        f"{package['counts']['nameClaims']} name claims, {len(data)} bytes."
    )
    return 0


def build_package(source: dict[str, Any]) -> dict[str, Any]:
    sources = sorted(copy.deepcopy(source["sources"]), key=lambda row: str(row["id"]))
    libraries_with_names = sorted(
        copy.deepcopy(source["libraries"]), key=library_sort_key
    )
    libraries = [
        {key: value for key, value in library.items() if key != "names"}
        for library in libraries_with_names
    ]
    default_library_id = str(source["defaultLibraryID"])
    library_by_id = {str(row["id"]): row for row in libraries_with_names}
    default_library = library_by_id[default_library_id]
    names_by_library = {
        str(library["id"]): {
            int(name["month"]): name for name in library["names"]
        }
        for library in libraries_with_names
    }

    entries: list[dict[str, Any]] = []
    name_claim_count = 0
    alias_name_count = 0
    for month in range(1, 13):
        primary_source_name = names_by_library[default_library_id][month]
        primary_display_name = str(primary_source_name["displayName"])
        primary_key = normalize_display_text(primary_display_name)
        grouped: dict[str, dict[str, Any]] = {}
        for library in libraries_with_names:
            library_id = str(library["id"])
            source_name = names_by_library[library_id][month]
            display_name = str(source_name["displayName"])
            display_key = normalize_display_text(display_name)
            group = grouped.setdefault(
                display_key,
                {
                    "displayName": display_name,
                    "claims": [],
                },
            )
            group["claims"].append(name_claim(library, source_name))
            name_claim_count += 1

        for group in grouped.values():
            group["claims"] = sorted(group["claims"], key=claim_sort_key)
        primary_name = grouped.pop(primary_key)
        aliases = sorted(
            grouped.values(),
            key=lambda row: (
                normalize_display_text(str(row["displayName"])),
                str(row["displayName"]),
            ),
        )
        alias_name_count += len(aliases)
        entry: dict[str, Any] = {
            "id": f"full-moon-gregorian-month-{month:02d}",
            "resolutionKey": {
                "month": month,
                "monthName": month_name(month),
            },
            "primaryName": primary_name,
            "aliases": aliases,
        }
        primary_editorial_notes = primary_source_name.get("editorialNotes")
        if primary_editorial_notes:
            entry["editorialNotes"] = str(primary_editorial_notes)
        entries.append(entry)

    package: dict[str, Any] = {
        "schemaVersion": int(source["schemaVersion"]),
        "packageFamily": str(source["packageFamily"]),
        "packageRole": PACKAGE_ROLE,
        "packageID": str(source["packageID"]),
        "packageVersion": str(source["packageVersion"]),
        "generatedAt": str(source["generatedAt"]),
        "defaultLibraryID": default_library_id,
        "resolver": copy.deepcopy(source["resolver"]),
        "namingConvention": copy.deepcopy(source["namingConvention"]),
        "sources": sources,
        "libraries": libraries,
        "entries": entries,
        "counts": {
            "entries": len(entries),
            "libraries": len(libraries),
            "sources": len(sources),
            "primaryNames": len(entries),
            "aliasNames": alias_name_count,
            "nameClaims": name_claim_count,
            "deduplicatedClaims": name_claim_count - len(entries) - alias_name_count,
        },
        "notes": [
            "This catalog contains name and provenance claims only; it contains no generated lunations, phase events, or concrete cycle dates.",
            "The app calculates the contained Full Moon, lunar-cycle boundaries, phase transitions, distance and apparent size, eclipses, supermoon or micromoon status, Blue Moon and seasonal labels, close encounters, and observer-specific circumstances at runtime.",
            "Alias display text is deduplicated within each entry while every independent library and source claim remains in the claims array.",
            "Libraries and claims are data records so a later package can add, correct, deactivate, or remove a library without changing the app's decoding model.",
        ],
    }
    if str(default_library["role"]) != "primary":
        raise RuntimeError("defaultLibraryID must reference the primary library.")
    return package


def name_claim(library: dict[str, Any], source_name: dict[str, Any]) -> dict[str, Any]:
    claim: dict[str, Any] = {
        "libraryID": str(library["id"]),
        "sourceID": str(source_name["sourceID"]),
        "sourceNameText": str(source_name["sourceNameText"]),
        "confidence": str(source_name.get("confidence") or library["confidence"]),
        "provenanceQuality": str(
            source_name.get("provenanceQuality") or library["provenanceQuality"]
        ),
    }
    if source_name.get("editorialNotes"):
        claim["editorialNotes"] = str(source_name["editorialNotes"])
    return claim


def validate_source(source: dict[str, Any]) -> None:
    require_dict(source, "source document")
    if source.get("schemaVersion") != 1:
        raise RuntimeError("Full Moon source schemaVersion must be 1.")
    if source.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Full Moon source packageFamily must be {PACKAGE_FAMILY}.")
    validate_identifier(source.get("packageID"), "packageID")
    validate_identifier(source.get("defaultLibraryID"), "defaultLibraryID")
    if not str(source.get("packageVersion") or "").strip():
        raise RuntimeError("Full Moon source is missing packageVersion.")
    parse_utc_datetime(source.get("generatedAt"), "generatedAt")
    validate_resolver(source.get("resolver"))
    validate_naming_convention(source.get("namingConvention"))

    sources = require_list(source.get("sources"), "sources")
    if not sources:
        raise RuntimeError("Full Moon source must contain provenance sources.")
    source_ids: set[str] = set()
    for index, source_row in enumerate(sources):
        require_dict(source_row, f"sources[{index}]")
        source_id = validate_identifier(source_row.get("id"), f"sources[{index}].id")
        if source_id in source_ids:
            raise RuntimeError(f"Duplicate source ID {source_id}.")
        source_ids.add(source_id)
        require_text(source_row.get("title"), f"source {source_id} title")
        require_text(source_row.get("publisher"), f"source {source_id} publisher")
        source_url = require_text(source_row.get("url"), f"source {source_id} url")
        if not source_url.startswith(("https://", "http://")):
            raise RuntimeError(f"Source {source_id} URL must be HTTP(S).")
        parse_date(source_row.get("accessedDate"), f"source {source_id} accessedDate")
        require_text(source_row.get("sourceType"), f"source {source_id} sourceType")
        if source_row.get("provenanceQuality") not in PROVENANCE_VALUES:
            raise RuntimeError(f"Source {source_id} has unsupported provenanceQuality.")
        if source_row.get("licenseStatus") not in LICENSE_VALUES:
            raise RuntimeError(f"Source {source_id} has unsupported licenseStatus.")
        require_text(
            source_row.get("usageReviewNotes"),
            f"source {source_id} usageReviewNotes",
        )

    libraries = require_list(source.get("libraries"), "libraries")
    if not libraries:
        raise RuntimeError("Full Moon source must contain libraries.")
    library_ids: set[str] = set()
    display_orders: set[int] = set()
    primary_ids: list[str] = []
    for index, library in enumerate(libraries):
        require_dict(library, f"libraries[{index}]")
        library_id = validate_identifier(library.get("id"), f"libraries[{index}].id")
        if library_id in library_ids:
            raise RuntimeError(f"Duplicate library ID {library_id}.")
        library_ids.add(library_id)
        require_text(library.get("displayName"), f"library {library_id} displayName")
        display_order = library.get("displayOrder")
        if not isinstance(display_order, int) or display_order < 0:
            raise RuntimeError(f"Library {library_id} displayOrder must be non-negative.")
        if display_order in display_orders:
            raise RuntimeError(f"Duplicate library displayOrder {display_order}.")
        display_orders.add(display_order)
        role = library.get("role")
        if role not in {"primary", "alias"}:
            raise RuntimeError(f"Library {library_id} role must be primary or alias.")
        if role == "primary":
            primary_ids.append(library_id)
        if library.get("status") not in {"active", "inactive", "deprecated"}:
            raise RuntimeError(f"Library {library_id} has unsupported status.")
        library_source_ids = require_string_list(
            library.get("sourceIDs"), f"library {library_id} sourceIDs"
        )
        unknown_source_ids = set(library_source_ids) - source_ids
        if unknown_source_ids:
            raise RuntimeError(
                f"Library {library_id} references unknown sources {sorted(unknown_source_ids)}."
            )
        validate_attribution(library.get("attribution"), library_id)
        if library.get("confidence") not in CONFIDENCE_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported confidence.")
        if library.get("provenanceQuality") not in PROVENANCE_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported provenanceQuality.")
        if library.get("usageReviewStatus") not in USAGE_REVIEW_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported usageReviewStatus.")
        require_text(library.get("licensingNotes"), f"library {library_id} licensingNotes")
        names = require_list(library.get("names"), f"library {library_id} names")
        month_set: set[int] = set()
        for name_index, name in enumerate(names):
            require_dict(name, f"library {library_id} names[{name_index}]")
            month = name.get("month")
            if not isinstance(month, int) or not 1 <= month <= 12:
                raise RuntimeError(f"Library {library_id} contains an invalid month.")
            if month in month_set:
                raise RuntimeError(f"Library {library_id} repeats month {month}.")
            month_set.add(month)
            require_text(name.get("displayName"), f"library {library_id} month {month} displayName")
            require_text(
                name.get("sourceNameText"),
                f"library {library_id} month {month} sourceNameText",
            )
            claim_source_id = validate_identifier(
                name.get("sourceID"),
                f"library {library_id} month {month} sourceID",
            )
            if claim_source_id not in library_source_ids:
                raise RuntimeError(
                    f"Library {library_id} month {month} sourceID is not declared by the library."
                )
            if name.get("confidence", library["confidence"]) not in CONFIDENCE_VALUES:
                raise RuntimeError(f"Library {library_id} month {month} has unsupported confidence.")
            if (
                name.get("provenanceQuality", library["provenanceQuality"])
                not in PROVENANCE_VALUES
            ):
                raise RuntimeError(
                    f"Library {library_id} month {month} has unsupported provenanceQuality."
                )
        if month_set != set(range(1, 13)):
            raise RuntimeError(f"Library {library_id} must define months 1 through 12 exactly once.")

    default_library_id = str(source["defaultLibraryID"])
    if primary_ids != [default_library_id]:
        raise RuntimeError("Source must contain exactly one primary library matching defaultLibraryID.")
    reject_forbidden_record_keys(source)


def validate_package(package: dict[str, Any]) -> None:
    require_dict(package, "package")
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Full Moon package schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Full Moon package family must be {PACKAGE_FAMILY}.")
    if package.get("packageRole") != PACKAGE_ROLE:
        raise RuntimeError(f"Full Moon package role must be {PACKAGE_ROLE}.")
    validate_identifier(package.get("packageID"), "packageID")
    require_text(package.get("packageVersion"), "packageVersion")
    parse_utc_datetime(package.get("generatedAt"), "generatedAt")
    default_library_id = validate_identifier(
        package.get("defaultLibraryID"), "defaultLibraryID"
    )
    validate_resolver(package.get("resolver"))
    validate_naming_convention(package.get("namingConvention"))

    sources = require_list(package.get("sources"), "sources")
    source_ids: list[str] = []
    for index, source_row in enumerate(sources):
        require_dict(source_row, f"sources[{index}]")
        source_id = validate_identifier(source_row.get("id"), f"sources[{index}].id")
        source_ids.append(source_id)
        require_text(source_row.get("title"), f"source {source_id} title")
        require_text(source_row.get("publisher"), f"source {source_id} publisher")
        source_url = require_text(source_row.get("url"), f"source {source_id} url")
        if not source_url.startswith(("https://", "http://")):
            raise RuntimeError(f"Source {source_id} URL must be HTTP(S).")
        parse_date(source_row.get("accessedDate"), f"source {source_id} accessedDate")
        require_text(source_row.get("sourceType"), f"source {source_id} sourceType")
        if source_row.get("provenanceQuality") not in PROVENANCE_VALUES:
            raise RuntimeError(f"Source {source_id} has unsupported provenanceQuality.")
        if source_row.get("licenseStatus") not in LICENSE_VALUES:
            raise RuntimeError(f"Source {source_id} has unsupported licenseStatus.")
        require_text(
            source_row.get("usageReviewNotes"),
            f"source {source_id} usageReviewNotes",
        )
    if source_ids != sorted(source_ids) or len(source_ids) != len(set(source_ids)):
        raise RuntimeError("Package sources must be uniquely sorted by ID.")
    libraries = require_list(package.get("libraries"), "libraries")
    if libraries != sorted(libraries, key=library_sort_key):
        raise RuntimeError("Package libraries must use deterministic display order.")
    library_by_id: dict[str, dict[str, Any]] = {}
    display_orders: set[int] = set()
    primary_ids: list[str] = []
    for index, library in enumerate(libraries):
        require_dict(library, f"libraries[{index}]")
        library_id = validate_identifier(library.get("id"), f"libraries[{index}].id")
        if library_id in library_by_id:
            raise RuntimeError(f"Duplicate package library ID {library_id}.")
        library_by_id[library_id] = library
        require_text(library.get("displayName"), f"library {library_id} displayName")
        display_order = library.get("displayOrder")
        if not isinstance(display_order, int) or display_order < 0:
            raise RuntimeError(f"Library {library_id} displayOrder must be non-negative.")
        if display_order in display_orders:
            raise RuntimeError(f"Duplicate library displayOrder {display_order}.")
        display_orders.add(display_order)
        role = library.get("role")
        if role not in {"primary", "alias"}:
            raise RuntimeError(f"Library {library_id} role must be primary or alias.")
        if role == "primary":
            primary_ids.append(library_id)
        if library.get("status") not in {"active", "inactive", "deprecated"}:
            raise RuntimeError(f"Library {library_id} has unsupported status.")
        library_source_ids = require_string_list(
            library.get("sourceIDs"), f"library {library_id} sourceIDs"
        )
        if set(library_source_ids) - set(source_ids):
            raise RuntimeError(f"Library {library_id} references an unknown source.")
        validate_attribution(library.get("attribution"), library_id)
        if library.get("confidence") not in CONFIDENCE_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported confidence.")
        if library.get("provenanceQuality") not in PROVENANCE_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported provenanceQuality.")
        if library.get("usageReviewStatus") not in USAGE_REVIEW_VALUES:
            raise RuntimeError(f"Library {library_id} has unsupported usageReviewStatus.")
        require_text(library.get("licensingNotes"), f"library {library_id} licensingNotes")
        if "names" in library:
            raise RuntimeError("Generated package libraries must not duplicate source name rows.")
    if len(library_by_id) != len(libraries) or default_library_id not in library_by_id:
        raise RuntimeError("Package libraries are missing unique IDs or the default library.")
    if primary_ids != [default_library_id]:
        raise RuntimeError("Package must contain one primary library matching defaultLibraryID.")

    entries = require_list(package.get("entries"), "entries")
    if len(entries) != 12:
        raise RuntimeError("Full Moon package must contain exactly 12 entries.")
    library_claim_months: dict[str, set[int]] = {library_id: set() for library_id in library_by_id}
    calculated_alias_names = 0
    calculated_name_claims = 0
    for expected_month, entry in enumerate(entries, start=1):
        require_dict(entry, f"entry {expected_month}")
        expected_id = f"full-moon-gregorian-month-{expected_month:02d}"
        if entry.get("id") != expected_id:
            raise RuntimeError(f"Entry {expected_month} must use stable ID {expected_id}.")
        resolution_key = require_dict(entry.get("resolutionKey"), f"entry {expected_id} resolutionKey")
        if resolution_key.get("month") != expected_month:
            raise RuntimeError(f"Entry {expected_id} has the wrong resolution month.")
        if resolution_key.get("monthName") != month_name(expected_month):
            raise RuntimeError(f"Entry {expected_id} has the wrong month name.")
        primary_name = validate_display_name_record(
            entry.get("primaryName"),
            f"entry {expected_id} primaryName",
            expected_month,
            library_by_id,
            set(source_ids),
            library_claim_months,
        )
        primary_claims = primary_name["claims"]
        if sum(claim.get("libraryID") == default_library_id for claim in primary_claims) != 1:
            raise RuntimeError(f"Entry {expected_id} must have one default-library primary claim.")
        aliases = require_list(entry.get("aliases"), f"entry {expected_id} aliases")
        alias_keys: set[str] = set()
        previous_alias_key = ""
        for alias_index, alias in enumerate(aliases):
            alias_record = validate_display_name_record(
                alias,
                f"entry {expected_id} aliases[{alias_index}]",
                expected_month,
                library_by_id,
                set(source_ids),
                library_claim_months,
            )
            alias_key = normalize_display_text(str(alias_record["displayName"]))
            if alias_key == normalize_display_text(str(primary_name["displayName"])):
                raise RuntimeError(f"Entry {expected_id} repeats its primary display name as an alias.")
            if alias_key in alias_keys:
                raise RuntimeError(f"Entry {expected_id} contains duplicate alias display text.")
            if alias_key < previous_alias_key:
                raise RuntimeError(f"Entry {expected_id} aliases are not deterministically sorted.")
            previous_alias_key = alias_key
            alias_keys.add(alias_key)
        calculated_alias_names += len(aliases)
        calculated_name_claims += len(primary_claims) + sum(
            len(alias["claims"]) for alias in aliases
        )

    for library_id, claimed_months in library_claim_months.items():
        if claimed_months != set(range(1, 13)):
            raise RuntimeError(
                f"Library {library_id} must contribute one claim for every resolver month."
            )
    calculated_counts = {
        "entries": 12,
        "libraries": len(libraries),
        "sources": len(sources),
        "primaryNames": 12,
        "aliasNames": calculated_alias_names,
        "nameClaims": calculated_name_claims,
        "deduplicatedClaims": calculated_name_claims - 12 - calculated_alias_names,
    }
    if package.get("counts") != calculated_counts:
        raise RuntimeError(
            f"Full Moon package counts do not match content: expected {calculated_counts}."
        )
    reject_forbidden_record_keys(package)


def validate_display_name_record(
    record: Any,
    label: str,
    month: int,
    library_by_id: dict[str, dict[str, Any]],
    source_ids: set[str],
    library_claim_months: dict[str, set[int]],
) -> dict[str, Any]:
    row = require_dict(record, label)
    require_text(row.get("displayName"), f"{label}.displayName")
    claims = require_list(row.get("claims"), f"{label}.claims")
    if not claims:
        raise RuntimeError(f"{label} must retain at least one provenance claim.")
    if claims != sorted(claims, key=claim_sort_key):
        raise RuntimeError(f"{label} claims are not deterministically sorted.")
    seen_libraries: set[str] = set()
    for claim_index, claim in enumerate(claims):
        claim_row = require_dict(claim, f"{label}.claims[{claim_index}]")
        library_id = validate_identifier(
            claim_row.get("libraryID"), f"{label}.claims[{claim_index}].libraryID"
        )
        source_id = validate_identifier(
            claim_row.get("sourceID"), f"{label}.claims[{claim_index}].sourceID"
        )
        if library_id not in library_by_id:
            raise RuntimeError(f"{label} references unknown library {library_id}.")
        if source_id not in source_ids:
            raise RuntimeError(f"{label} references unknown source {source_id}.")
        if source_id not in library_by_id[library_id].get("sourceIDs", []):
            raise RuntimeError(f"{label} source {source_id} is not declared by {library_id}.")
        if library_id in seen_libraries:
            raise RuntimeError(f"{label} contains duplicate claims from {library_id}.")
        seen_libraries.add(library_id)
        if month in library_claim_months[library_id]:
            raise RuntimeError(f"Library {library_id} contributes multiple claims for month {month}.")
        library_claim_months[library_id].add(month)
        require_text(claim_row.get("sourceNameText"), f"{label} sourceNameText")
        if claim_row.get("confidence") not in CONFIDENCE_VALUES:
            raise RuntimeError(f"{label} contains unsupported claim confidence.")
        if claim_row.get("provenanceQuality") not in PROVENANCE_VALUES:
            raise RuntimeError(f"{label} contains unsupported claim provenanceQuality.")
    return row


def validate_resolver(value: Any) -> None:
    resolver = require_dict(value, "resolver")
    if resolver.get("id") != RESOLVER_ID:
        raise RuntimeError(f"Resolver ID must be {RESOLVER_ID}.")
    if resolver.get("version") != 1:
        raise RuntimeError("Resolver version must be 1.")
    if resolver.get("calendar") != "gregorian":
        raise RuntimeError("Resolver calendar must be gregorian.")
    if resolver.get("timeBasis") != "utc":
        raise RuntimeError("Resolver timeBasis must be utc for timezone-stable names.")
    if resolver.get("input") != "containedFullMoonInstantUTC":
        raise RuntimeError("Resolver input must be containedFullMoonInstantUTC.")
    require_text(resolver.get("notes"), "resolver notes")


def validate_naming_convention(value: Any) -> None:
    convention = require_dict(value, "namingConvention")
    if convention.get("id") != "namedAfterContainedFullMoon":
        raise RuntimeError("Unsupported Full Moon naming convention.")
    expected_scope = ["astronomicalFullMoon", "containingNewMoonToNewMoonCycle"]
    if convention.get("displayScope") != expected_scope:
        raise RuntimeError("Naming convention displayScope is incomplete.")
    require_text(convention.get("attribution"), "namingConvention attribution")
    require_text(convention.get("notes"), "namingConvention notes")


def validate_attribution(value: Any, library_id: str) -> None:
    attribution = require_dict(value, f"library {library_id} attribution")
    for key in ("culturalContext", "regions", "hemispheres", "languageTags"):
        require_string_list(attribution.get(key), f"library {library_id} attribution.{key}")
    hemispheres = set(attribution["hemispheres"])
    if not hemispheres or not hemispheres <= {"northern", "southern", "both", "none"}:
        raise RuntimeError(f"Library {library_id} contains invalid hemisphere attribution.")
    if not isinstance(attribution.get("communitySpecific"), bool):
        raise RuntimeError(f"Library {library_id} communitySpecific must be boolean.")
    require_text(attribution.get("notes"), f"library {library_id} attribution.notes")


def descriptor_for_package(
    package: dict[str, Any],
    data: bytes,
    args: argparse.Namespace,
    output_path: Path,
) -> dict[str, Any]:
    package_path = repo_relative_path(output_path)
    return {
        "family": PACKAGE_FAMILY,
        "packageVersion": package["packageVersion"],
        "payloadSchemaVersion": package["schemaVersion"],
        "packageURL": f"{METADATA_ORIGIN}/{package_path.as_posix()}",
        "checksum": {
            "algorithm": "sha256",
            "value": hashlib.sha256(data).hexdigest(),
        },
        "byteSize": len(data),
        "recordCount": int(package["counts"]["entries"]),
        "minSupportedAppVersion": args.min_supported_app_version,
        "minSupportedBuild": args.min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Clients that support this family should retain a bundled or cached validated "
            "snapshot. Resolve by the package-declared contained-Full-Moon UTC month policy; "
            "keep astronomical, seasonal, and observer-specific calculations app-side."
        ),
    }


def update_manifest(
    manifest_path: Path,
    generated_at: str,
    descriptor: dict[str, Any],
) -> None:
    manifest = read_json(manifest_path)
    packages = [
        entry
        for entry in manifest.get("packages", [])
        if descriptor_key(entry) != descriptor_key(descriptor)
    ]
    packages.append(descriptor)
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(packages)
    write_json(manifest_path, manifest)


def validate_manifest_descriptor(
    manifest_path: Path,
    package: dict[str, Any],
    data: bytes,
    output_path: Path,
) -> None:
    manifest = read_json(manifest_path)
    matches = [
        entry
        for entry in manifest.get("packages", [])
        if descriptor_key(entry) == (PACKAGE_FAMILY, "")
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one manifest descriptor for {PACKAGE_FAMILY}, found {len(matches)}."
        )
    entry = matches[0]
    if entry.get("packageVersion") != package.get("packageVersion"):
        raise RuntimeError("Manifest packageVersion does not match Full Moon package.")
    if entry.get("payloadSchemaVersion") != package.get("schemaVersion"):
        raise RuntimeError("Manifest payloadSchemaVersion does not match Full Moon package.")
    expected_url = f"{METADATA_ORIGIN}/{repo_relative_path(output_path).as_posix()}"
    if entry.get("packageURL") != expected_url:
        raise RuntimeError("Manifest packageURL does not reference the Full Moon package.")
    if int(entry.get("byteSize") or 0) != len(data):
        raise RuntimeError("Manifest byteSize does not match Full Moon package.")
    if int(entry.get("recordCount") or 0) != int(package["counts"]["entries"]):
        raise RuntimeError("Manifest recordCount does not match Full Moon package.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != hashlib.sha256(data).hexdigest():
        raise RuntimeError("Manifest checksum does not match Full Moon package.")
    if manifest.get("packages") != sort_packages(manifest.get("packages") or []):
        raise RuntimeError("Stable manifest package ordering is not deterministic.")


def descriptor_key(entry: dict[str, Any]) -> tuple[str, str]:
    family = str(entry.get("family") or "")
    if family == "seasonalRecommendationCandidates":
        return family, str(entry.get("latitudeBand") or "")
    return family, ""


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {
        "north_high_60_90n": 0,
        "north_mid_30_60n": 1,
        "north_low_0_30n": 2,
        "south_low_0_30s": 3,
        "south_mid_30_60s": 4,
        "south_high_60_90s": 5,
    }

    def key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
        family = str(entry.get("family") or "")
        return (
            family_order.get(family, len(family_order)),
            band_order.get(str(entry.get("latitudeBand") or ""), 99),
            family,
            str(entry.get("packageVersion") or ""),
        )

    return sorted(packages, key=key)


def library_sort_key(library: dict[str, Any]) -> tuple[int, str]:
    display_order = library.get("displayOrder")
    return (
        int(display_order) if isinstance(display_order, int) else 9999,
        str(library.get("id") or ""),
    )


def claim_sort_key(claim: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(claim.get("libraryID") or ""),
        str(claim.get("sourceID") or ""),
        str(claim.get("sourceNameText") or "").casefold(),
    )


def normalize_display_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).split()).casefold()


def month_name(month: int) -> str:
    return dt.date(2000, month, 1).strftime("%B")


def parse_utc_datetime(value: Any, label: str) -> dt.datetime:
    text = require_text(value, label)
    if not text.endswith("Z"):
        raise RuntimeError(f"{label} must use a UTC Z timestamp.")
    try:
        parsed = dt.datetime.fromisoformat(text[:-1] + "+00:00")
    except ValueError as exc:
        raise RuntimeError(f"{label} is not a valid timestamp.") from exc
    if parsed.tzinfo != dt.UTC:
        raise RuntimeError(f"{label} must be UTC.")
    return parsed


def parse_date(value: Any, label: str) -> dt.date:
    text = require_text(value, label)
    try:
        return dt.date.fromisoformat(text)
    except ValueError as exc:
        raise RuntimeError(f"{label} is not a valid date.") from exc


def reject_forbidden_record_keys(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_RECORD_KEYS:
                raise RuntimeError(
                    f"Full Moon name metadata must not contain runtime field {path}.{key}."
                )
            reject_forbidden_record_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_forbidden_record_keys(child, f"{path}[{index}]")


def validate_identifier(value: Any, label: str) -> str:
    text = require_text(value, label)
    if not PACKAGE_ID_PATTERN.fullmatch(text):
        raise RuntimeError(f"{label} is not a stable identifier: {text}.")
    return text


def require_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"{label} must be non-empty text.")
    return value


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RuntimeError(f"{label} must be an object.")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise RuntimeError(f"{label} must be an array.")
    return value


def require_string_list(value: Any, label: str) -> list[str]:
    rows = require_list(value, label)
    if not rows or any(not isinstance(row, str) or not row.strip() for row in rows):
        raise RuntimeError(f"{label} must contain non-empty text values.")
    if len(rows) != len(set(rows)):
        raise RuntimeError(f"{label} must not contain duplicates.")
    return rows


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any], *, compact: bool = False) -> bytes:
    data = json_bytes(payload, compact=compact)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def json_bytes(payload: dict[str, Any], *, compact: bool = False) -> bytes:
    if compact:
        serialized = json.dumps(payload, separators=(",", ":"), ensure_ascii=True)
    else:
        serialized = json.dumps(payload, indent=2, ensure_ascii=True)
    return (serialized + "\n").encode("utf-8")


def repo_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO_ROOT / path


def repo_relative_path(path: Path) -> Path:
    try:
        return path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        return path


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


if __name__ == "__main__":
    raise SystemExit(main())
