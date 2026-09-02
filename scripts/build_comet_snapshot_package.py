#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "cometSnapshot"
PACKAGE_PATH = Path("v1/packages/comets/comet_snapshot_v1.json")

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the hosted AstroGuide comet snapshot package and refresh the stable manifest."
    )
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument(
        "--source-package",
        type=Path,
        help="Use an already generated cometSnapshot package instead of wrapping app resources.",
    )
    parser.add_argument(
        "--aerith-source",
        type=Path,
        help="Optional normalized Aerith weekly comet source JSON to enrich comet rows.",
    )
    parser.add_argument(
        "--apply-aerith-magnitudes",
        action="store_true",
        help="Patch ephemeris magnitudes between Aerith weekly estimate rows for matched comets.",
    )
    parser.add_argument(
        "--promote-aerith-images",
        action="store_true",
        help=(
            "Deprecated safety guard. Aerith images must be cached through comet detail metadata, not hotlinked."
        ),
    )
    parser.add_argument("--package-version")
    parser.add_argument("--generated-at")
    parser.add_argument("--min-supported-app-version", default="0.1.2")
    parser.add_argument("--min-supported-build", default="1")
    return parser.parse_args()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(generated_at: str) -> str:
    return generated_at.split("T", maxsplit=1)[0]


def build_package(
    app_repo: Path,
    generated_at: str,
    package_version: str | None = None,
) -> dict[str, Any]:
    comet_dir = app_repo / "App/Resources/Comets"
    seeds = read_json(comet_dir / "comet_seeds.json")
    ephemeris = read_json(comet_dir / "comet_ephemeris.json")
    validate_sources(seeds, ephemeris)

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version or f"comet-snapshot-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide bundled comet seed and ephemeris snapshot",
            "generatedBy": "scripts/build_comet_snapshot_package.py",
            "sourceURL": (
                "https://github.com/tophrchris/DSOPlanneriOS/tree/release/1.3.5/"
                "App/Resources/Comets"
            ),
            "notes": (
                "Wraps the bundled comet_seeds.json and comet_ephemeris.json files in the "
                "dynamic metadata package envelope without changing their runtime shape."
            ),
        },
        "seeds": seeds,
        "ephemeris": ephemeris,
    }


def build_package_from_source(
    source_package: Path,
    generated_at: str | None,
    package_version: str | None = None,
) -> dict[str, Any]:
    package = read_json(source_package)
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Source comet package must use schemaVersion 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Source comet package must be a {PACKAGE_FAMILY} package.")
    if generated_at is not None:
        package["generatedAt"] = generated_at
    if not package.get("generatedAt"):
        raise RuntimeError("Source comet package is missing generatedAt.")
    if package_version is not None:
        package["packageVersion"] = package_version
    if not package.get("packageVersion"):
        package["packageVersion"] = f"comet-snapshot-v1-{date_token(package['generatedAt'])}"
    validate_sources(package.get("seeds") or {}, package.get("ephemeris") or {})
    return package


def normalize_comet_key(value: str) -> str:
    text = str(value or "").strip().upper()
    text = re.sub(r"\s+", " ", text)

    numbered = re.match(r"^0*(\d+P)\b", text)
    if numbered:
        return numbered.group(1)

    modern = re.match(r"^([ACPDI]/\d{4})\s+([A-Z]\d+)", text)
    if modern:
        return f"{modern.group(1)}{modern.group(2)}"

    parenthesized = re.match(r"^\((\d+)\)", text)
    if parenthesized:
        return parenthesized.group(1)

    first_token = re.split(r"[\s(]", text, maxsplit=1)[0]
    return re.sub(r"[^A-Z0-9/]", "", first_token)


def seed_match_keys(seed: dict[str, Any]) -> set[str]:
    values: list[str] = [
        str(seed.get("stableID") or "").removeprefix("COMET:").replace("_", "/"),
        str(seed.get("designation") or ""),
        str(seed.get("displayName") or ""),
        str(seed.get("shortName") or ""),
    ]
    aliases = seed.get("aliases") or []
    if isinstance(aliases, list):
        values.extend(str(alias) for alias in aliases)
    return {key for key in (normalize_comet_key(value) for value in values) if key}


def compact_aerith_reference(entry: dict[str, Any]) -> dict[str, Any]:
    image_url = entry.get("thumbnailImageURL")
    reference: dict[str, Any] = {
        "aerithName": entry.get("aerithName"),
        "normalizedDesignation": entry.get("normalizedDesignation"),
        "hemispheres": entry.get("hemispheres") or [],
        "pageRanks": entry.get("pageRanks") or {},
        "sourcePageURLs": entry.get("sourcePageURLs") or {},
        "detailURL": entry.get("detailURL"),
        "currentMagnitude": entry.get("currentMagnitude"),
        "nextWeekMagnitude": entry.get("nextWeekMagnitude"),
        "weeklyRowsByHemisphere": entry.get("weeklyRowsByHemisphere") or {},
    }
    if image_url:
        reference["candidateHeroImageURL"] = image_url
        reference["imagePermissionStatus"] = entry.get("imagePermissionStatus") or "permission-granted"
        reference["imageAttribution"] = entry.get("imageAttribution")
    commentaries = entry.get("sourceCommentaries")
    if commentaries:
        reference["sourceCommentaries"] = commentaries
    reported = entry.get("reportedMagnitudes")
    if reported:
        reference["reportedMagnitudes"] = reported
    return {key: value for key, value in reference.items() if value not in (None, {}, [])}


def aerith_magnitude_rows(entry: dict[str, Any]) -> list[dict[str, Any]]:
    rows_by_hemisphere = entry.get("weeklyRowsByHemisphere") or {}
    for preferred in ("north", "south"):
        rows = rows_by_hemisphere.get(preferred)
        if isinstance(rows, list) and len(rows) >= 2:
            return rows
    for rows in rows_by_hemisphere.values():
        if isinstance(rows, list) and len(rows) >= 2:
            return rows
    return []


def parse_iso_date(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.UTC)


def patch_ephemeris_magnitudes(
    package: dict[str, Any],
    stable_id: str,
    aerith_entry: dict[str, Any],
) -> dict[str, Any] | None:
    rows = sorted(aerith_magnitude_rows(aerith_entry), key=lambda row: str(row.get("date") or ""))
    if len(rows) < 2:
        return None

    start_date = dt.datetime.fromisoformat(rows[0]["date"]).replace(tzinfo=dt.UTC)
    end_date = dt.datetime.fromisoformat(rows[-1]["date"]).replace(tzinfo=dt.UTC)
    start_magnitude = rows[0].get("magnitude")
    end_magnitude = rows[-1].get("magnitude")
    if start_magnitude is None or end_magnitude is None or end_date <= start_date:
        return None

    ephemeris = package["ephemeris"]
    samples = ephemeris["comets"].get(stable_id)
    if not isinstance(samples, list):
        return None

    anchor = parse_iso_date(str(ephemeris["anchorTimestamp"]))
    step_seconds = int(ephemeris["sampleStepHours"]) * 60 * 60
    window_seconds = (end_date - start_date).total_seconds()
    patched = 0
    for index, sample in enumerate(samples):
        if not isinstance(sample, list) or len(sample) < 3:
            continue
        sample_time = anchor + dt.timedelta(seconds=step_seconds * index)
        if sample_time < start_date or sample_time > end_date:
            continue
        fraction = (sample_time - start_date).total_seconds() / window_seconds
        sample[2] = round(float(start_magnitude) + (float(end_magnitude) - float(start_magnitude)) * fraction, 3)
        patched += 1

    if patched == 0:
        return None
    return {
        "stableID": stable_id,
        "aerithName": aerith_entry.get("aerithName"),
        "startDate": rows[0]["date"],
        "endDate": rows[-1]["date"],
        "startMagnitude": start_magnitude,
        "endMagnitude": end_magnitude,
        "sampleCount": patched,
    }


def apply_aerith_source(
    package: dict[str, Any],
    aerith_source: dict[str, Any],
    *,
    apply_magnitudes: bool,
    promote_images: bool,
) -> dict[str, Any]:
    if promote_images:
        raise RuntimeError(
            "Do not promote Aerith image URLs into cometSnapshot heroImageURL values. "
            "Use build_comet_detail_metadata_package.py to publish cached AstroGuide metadata assets."
        )
    if aerith_source.get("schemaVersion") != 1:
        raise RuntimeError("Aerith comet source must use schemaVersion 1.")
    aerith_entries = {
        str(entry.get("normalizedDesignation") or ""): entry
        for entry in aerith_source.get("comets", [])
        if entry.get("normalizedDesignation")
    }
    if not aerith_entries:
        raise RuntimeError("Aerith comet source contains no comet entries.")

    matched_rows: list[dict[str, Any]] = []
    magnitude_patches: list[dict[str, Any]] = []
    for seed in package["seeds"]["comets"]:
        match = next(
            (aerith_entries[key] for key in seed_match_keys(seed) if key in aerith_entries),
            None,
        )
        if match is None:
            continue

        source = seed.get("source")
        if not isinstance(source, dict):
            source = {}
        source["aerithWeekly"] = compact_aerith_reference(match)
        seed["source"] = source
        if promote_images and not seed.get("heroImageURL") and match.get("thumbnailImageURL"):
            seed["heroImageURL"] = match["thumbnailImageURL"]

        if apply_magnitudes:
            patch_summary = patch_ephemeris_magnitudes(package, seed["stableID"], match)
            if patch_summary is not None:
                magnitude_patches.append(patch_summary)

        matched_rows.append(
            {
                "stableID": seed["stableID"],
                "designation": seed.get("designation"),
                "aerithName": match.get("aerithName"),
                "currentMagnitude": match.get("currentMagnitude"),
                "nextWeekMagnitude": match.get("nextWeekMagnitude"),
            }
        )

    source = package.get("source")
    if not isinstance(source, dict):
        source = {"name": "AstroGuide comet snapshot"}
    source["aerithWeeklySource"] = {
        "name": aerith_source.get("source", {}).get("name") or "Aerith Weekly Information about Bright Comets",
        "sourceURL": aerith_source.get("source", {}).get("sourceURL"),
        "generatedAt": aerith_source.get("generatedAt"),
        "permissionStatus": aerith_source.get("source", {}).get("permissionStatus") or "permission-granted",
        "permissionReceived": aerith_source.get("source", {}).get("permissionReceived"),
        "matchedCometCount": len(matched_rows),
        "imageUsage": "reference-only; cached images are published through cometDetailMetadata",
        "magnitudePatchCount": len(magnitude_patches),
    }
    if magnitude_patches:
        source["aerithMagnitudePatches"] = magnitude_patches
    package["source"] = source
    validate_sources(package.get("seeds") or {}, package.get("ephemeris") or {})
    return package


def validate_sources(seeds: dict[str, Any], ephemeris: dict[str, Any]) -> None:
    comet_rows = seeds.get("comets")
    ephemeris_rows = ephemeris.get("comets")
    if not isinstance(comet_rows, list) or not comet_rows:
        raise RuntimeError("Comet seed bundle contains no comets.")
    if not isinstance(ephemeris_rows, dict) or not ephemeris_rows:
        raise RuntimeError("Comet ephemeris bundle contains no comet samples.")
    if int(ephemeris.get("sampleCount") or 0) <= 0:
        raise RuntimeError("Comet ephemeris bundle has an invalid sampleCount.")

    missing_ephemeris: list[str] = []
    for row in comet_rows:
        stable_id = str(row.get("stableID") or "").strip()
        if not stable_id:
            raise RuntimeError("Comet seed row is missing stableID.")
        if stable_id not in ephemeris_rows:
            missing_ephemeris.append(stable_id)
            continue
        samples = ephemeris_rows[stable_id]
        if not isinstance(samples, list) or not samples:
            raise RuntimeError(f"Comet ephemeris for {stable_id} contains no samples.")
    if missing_ephemeris:
        raise RuntimeError(
            "Comet ephemeris bundle is missing samples for: " + ", ".join(missing_ephemeris)
        )


def package_descriptor(
    *,
    package: dict[str, Any],
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict[str, Any]:
    return {
        "family": PACKAGE_FAMILY,
        "packageVersion": package["packageVersion"],
        "payloadSchemaVersion": package["schemaVersion"],
        "packageURL": f"{METADATA_ORIGIN}/{PACKAGE_PATH.as_posix()}",
        "checksum": {
            "algorithm": "sha256",
            "value": hashlib.sha256(data).hexdigest(),
        },
        "byteSize": len(data),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Use the bundled comet seed and ephemeris snapshot if no validated cached package is "
            "available, if the cached package is expired, or if package validation fails."
        ),
    }


def descriptor_key(entry: dict[str, Any]) -> tuple[str, str]:
    family = str(entry.get("family") or "")
    if family == "seasonalRecommendationCandidates":
        return family, str(entry.get("latitudeBand") or "")
    return family, ""


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {band: index for index, band in enumerate(LATITUDE_BAND_ORDER)}

    def key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
        return (
            family_order.get(str(entry.get("family") or ""), len(family_order)),
            band_order.get(str(entry.get("latitudeBand") or ""), 99),
            str(entry.get("family") or ""),
            str(entry.get("packageVersion") or ""),
        )

    return sorted(packages, key=key)


def update_manifest(generated_at: str, descriptor: dict[str, Any]) -> None:
    manifest_path = REPO_ROOT / "v1/channels/stable/manifest.json"
    manifest = read_json(manifest_path)
    descriptors = {
        descriptor_key(entry): entry
        for entry in manifest.get("packages", [])
        if descriptor_key(entry) != descriptor_key(descriptor)
    }
    descriptors[descriptor_key(descriptor)] = descriptor

    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(list(descriptors.values()))
    write_json(manifest_path, manifest)


def main() -> int:
    args = parse_args()
    app_repo = args.app_repo.resolve()
    generated_at = args.generated_at or utc_now()

    package = (
        build_package_from_source(
            args.source_package.resolve(),
            args.generated_at,
            package_version=args.package_version,
        )
        if args.source_package is not None
        else build_package(app_repo, generated_at, package_version=args.package_version)
    )
    if args.aerith_source is not None:
        package = apply_aerith_source(
            package,
            read_json(args.aerith_source.resolve()),
            apply_magnitudes=args.apply_aerith_magnitudes,
            promote_images=args.promote_aerith_images,
        )
    generated_at = package["generatedAt"]
    data = write_json(REPO_ROOT / PACKAGE_PATH, package)
    descriptor = package_descriptor(
        package=package,
        data=data,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
    )
    update_manifest(generated_at, descriptor)

    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
