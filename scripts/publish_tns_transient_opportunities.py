#!/usr/bin/env python3
"""Promote an approved TNS transient review output to a runtime package."""

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_PATH = Path("outputs/transients/runtime/transient_opportunities_v1.json")
PACKAGE_PATH = Path("v1/packages/transients/transient_opportunities_v1.json")
MANIFEST_PATH = Path("v1/channels/stable/manifest.json")
METADATA_ORIGIN = "https://metadata.astroguide.space"
PACKAGE_FAMILY = "transientEventFeed"
CONTENT_FAMILY = "transientOpportunities"
CACHE_TTL_SECONDS = 6 * 60 * 60
ALLOWED_EVENT_TYPES = {"transientOpportunity", "novaOpportunity", "supernovaOpportunity"}

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "targetImageAssets",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "astrophotographyEquipmentSanitizedCatalog",
    "telescopeReferencePrices",
    "telescopeOfficialProductLinks",
    "darkSkyPlaces",
    "starPartyAstroSites",
    "cometSnapshot",
    "cometOrbitGeometry",
    "cometDetailMetadata",
    "planetCatalog",
    "lunarEvents",
    "fullMoonNameAliases",
    "planetTargetCloseEncounters",
    "cometCloseEncounters",
    "seasonalRecommendationCandidates",
    "transientEventFeed",
]
LATITUDE_BAND_ORDER = [
    "north_high_60_90n",
    "north_mid_30_60n",
    "north_low_0_30n",
    "south_low_0_30s",
    "south_mid_30_60s",
    "south_high_60_90s",
]


class ValidationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Promote a curator-approved TNS transient opportunity JSON file into "
            "the hosted runtime package and refresh the stable manifest."
        )
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_PATH)
    parser.add_argument("--manifest", type=Path, default=MANIFEST_PATH)
    parser.add_argument("--package-path", type=Path, default=PACKAGE_PATH)
    parser.add_argument("--min-supported-app-version", default="1.4.2")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--generated-at", help="UTC ISO-8601 manifest timestamp")
    parser.add_argument("--validate-only", action="store_true")
    return parser.parse_args()


def repo_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO_ROOT / path


def read_json(path: Path) -> Any:
    with repo_path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = json_bytes(payload)
    absolute = repo_path(path)
    absolute.parent.mkdir(parents=True, exist_ok=True)
    absolute.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(value: str | None) -> str:
    if value:
        match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", value)
        if match:
            return "".join(match.groups())
    return dt.datetime.now(dt.UTC).strftime("%Y%m%d")


def package_version(package: dict[str, Any]) -> str:
    existing = str(package.get("packageVersion") or "").strip()
    if existing:
        return existing
    return f"transient-event-feed-v1-{date_token(package.get('asOfDate'))}-approved"


def normalize_package(source: dict[str, Any]) -> dict[str, Any]:
    if source.get("schemaVersion") != 1:
        raise ValidationError("Transient opportunity package schemaVersion must be 1.")
    if source.get("family") not in (CONTENT_FAMILY, None):
        raise ValidationError(f"Transient opportunity package family must be {CONTENT_FAMILY}.")
    if source.get("reviewOnly") is not False:
        raise ValidationError("Runtime transient opportunity package must set reviewOnly=false.")
    opportunities = source.get("opportunities")
    if not isinstance(opportunities, list) or not opportunities:
        raise ValidationError("Runtime transient opportunity package must contain opportunities.")

    promoted: dict[str, Any] = {
        "schemaVersion": source["schemaVersion"],
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version(source),
        "family": CONTENT_FAMILY,
    }
    for key, value in source.items():
        if key in {"schemaVersion", "packageFamily", "packageVersion", "family"}:
            continue
        promoted[key] = copy.deepcopy(value)
    validate_package(promoted)
    return promoted


def validate_package(package: dict[str, Any]) -> None:
    if package.get("schemaVersion") != 1:
        raise ValidationError("Package schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise ValidationError(f"Package packageFamily must be {PACKAGE_FAMILY}.")
    if package.get("family") != CONTENT_FAMILY:
        raise ValidationError(f"Package family must be {CONTENT_FAMILY}.")
    if not str(package.get("packageVersion") or "").strip():
        raise ValidationError("Package packageVersion is required.")
    if package.get("reviewOnly") is not False:
        raise ValidationError("Package reviewOnly must be false.")
    opportunities = package.get("opportunities")
    if not isinstance(opportunities, list) or not opportunities:
        raise ValidationError("Package opportunities must be a non-empty list.")
    for index, opportunity in enumerate(opportunities):
        if opportunity.get("reviewOnly") is not False:
            raise ValidationError(f"Opportunity {index} must set reviewOnly=false.")
        if opportunity.get("eventType") not in ALLOWED_EVENT_TYPES:
            raise ValidationError(
                f"Opportunity {index} eventType must be one of {sorted(ALLOWED_EVENT_TYPES)}."
            )
        active_window = opportunity.get("activeWindow") or {}
        if not active_window.get("startsAtUTC") or not active_window.get("expiresAtUTC"):
            raise ValidationError(f"Opportunity {index} must include activeWindow starts/expires.")


def descriptor(
    package: dict[str, Any],
    package_path: Path,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict[str, Any]:
    opportunities = package["opportunities"]
    counts = package.get("counts") or {}
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
        "reviewedCount": counts.get("reviewed"),
        "approvedCount": counts.get("approved", len(opportunities)),
        "opportunityCount": len(opportunities),
        "urgentCount": sum(1 for item in opportunities if item.get("urgency") == "urgent"),
        "asOfDate": package.get("asOfDate"),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Curator-approved TNS transient opportunities. Clients should show this "
            "short-lived feed only from a validated cached remote package; expired "
            "cached data remains usable until replaced, but individual events must honor "
            "their activeWindow expiry."
        ),
    }


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {band: index for index, band in enumerate(LATITUDE_BAND_ORDER)}

    def key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
        family = entry.get("family") or entry.get("packageFamily") or ""
        return (
            family_order.get(family, len(family_order)),
            band_order.get(str(entry.get("latitudeBand") or ""), len(band_order)),
            family,
            str(entry.get("packageVersion") or ""),
        )

    return sorted(packages, key=key)


def validate_manifest_descriptor(
    manifest_path: Path,
    package_path: Path,
    package: dict[str, Any],
    data: bytes,
) -> None:
    manifest = read_json(manifest_path)
    matches = [entry for entry in manifest["packages"] if entry.get("family") == PACKAGE_FAMILY]
    if len(matches) != 1:
        raise ValidationError(f"Stable manifest must contain exactly one {PACKAGE_FAMILY} entry.")
    entry = matches[0]
    expected = descriptor(
        package,
        package_path,
        data,
        entry.get("minSupportedAppVersion"),
        entry.get("minSupportedBuild"),
    )
    if entry != expected:
        raise ValidationError("Stable manifest descriptor does not match the transient package.")
    if manifest["packages"] != sort_packages(manifest["packages"]):
        raise ValidationError("Stable manifest packages are not canonically ordered.")


def validate_checked_in_artifacts(manifest_path: Path, package_path: Path) -> None:
    package = read_json(package_path)
    validate_package(package)
    data = repo_path(package_path).read_bytes()
    if data != json_bytes(package):
        raise ValidationError("Checked-in package JSON formatting is not canonical.")
    validate_manifest_descriptor(manifest_path, package_path, package, data)


def main() -> int:
    args = parse_args()
    if args.validate_only:
        validate_checked_in_artifacts(args.manifest, args.package_path)
        package = read_json(args.package_path)
        print(
            f"Validated {PACKAGE_FAMILY}: {len(package['opportunities'])} opportunities, "
            f"{package['packageVersion']}."
        )
        return 0

    package = normalize_package(read_json(args.source))
    data = write_json(args.package_path, package)
    manifest = read_json(args.manifest)
    manifest_descriptor = descriptor(
        package,
        args.package_path,
        data,
        args.min_supported_app_version,
        args.min_supported_build,
    )
    packages = [
        entry for entry in manifest.get("packages", []) if entry.get("family") != PACKAGE_FAMILY
    ]
    packages.append(manifest_descriptor)
    generated_at = args.generated_at or utc_now()
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(packages)
    write_json(args.manifest, manifest)
    validate_checked_in_artifacts(args.manifest, args.package_path)

    print(
        f"{PACKAGE_FAMILY}: {manifest_descriptor['packageVersion']} "
        f"{manifest_descriptor['opportunityCount']} opportunities "
        f"{manifest_descriptor['byteSize']} bytes {manifest_descriptor['checksum']['value']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
