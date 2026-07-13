#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
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
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "darkSkyPlaces",
    "cometSnapshot",
    "seasonalRecommendationCandidates",
    "transientEventFeed",
    "lunarClosePasses",
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


def build_package(app_repo: Path, generated_at: str) -> dict[str, Any]:
    comet_dir = app_repo / "App/Resources/Comets"
    seeds = read_json(comet_dir / "comet_seeds.json")
    ephemeris = read_json(comet_dir / "comet_ephemeris.json")
    validate_sources(seeds, ephemeris)

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": f"comet-snapshot-v1-{date_token(generated_at)}",
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


def build_package_from_source(source_package: Path, generated_at: str | None) -> dict[str, Any]:
    package = read_json(source_package)
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Source comet package must use schemaVersion 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Source comet package must be a {PACKAGE_FAMILY} package.")
    if generated_at is not None:
        package["generatedAt"] = generated_at
    if not package.get("generatedAt"):
        raise RuntimeError("Source comet package is missing generatedAt.")
    if not package.get("packageVersion"):
        package["packageVersion"] = f"comet-snapshot-v1-{date_token(package['generatedAt'])}"
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
        build_package_from_source(args.source_package.resolve(), args.generated_at)
        if args.source_package is not None
        else build_package(app_repo, generated_at)
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
