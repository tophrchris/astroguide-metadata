#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "equipmentCatalog"
PACKAGE_PATH = Path("v1/packages/equipment/equipment_catalog_v1.json")

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "equipmentCatalog",
    "seasonalRecommendationCandidates",
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
        description="Build the hosted AstroGuide equipment catalog package and refresh the stable manifest."
    )
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument("--generated-at")
    parser.add_argument("--min-supported-app-version", default="0.1.2")
    parser.add_argument("--min-supported-build", default="1")
    return parser.parse_args()


def read_json(path: Path):
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


def build_package(app_repo: Path, generated_at: str) -> dict:
    catalog_path = app_repo / "App/Resources/Equipment/equipment_catalog.json"
    catalog = read_json(catalog_path)
    categories = catalog.get("categories") or []
    if not categories:
        raise RuntimeError("Equipment catalog package would be empty.")

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": f"equipment-catalog-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide bundled equipment catalog",
            "generatedBy": "astroguide-metadata equipment package builder",
            "sourceURL": (
                "https://github.com/tophrchris/DSOPlanneriOS/tree/main/"
                "App/Resources/Equipment/equipment_catalog.json"
            ),
            "notes": "Wraps the bundled smart telescope and filter catalog in the dynamic metadata package envelope.",
        },
        "catalog": catalog,
    }


def package_descriptor(
    *,
    package: dict,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict:
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
            "Use the bundled equipment catalog only if no validated cached package is available. "
            "Cache TTL indicates when the app should check for a fresher package; an expired cached "
            "package remains usable until replaced by a validated refresh."
        ),
    }


def sort_packages(packages: list[dict]) -> list[dict]:
    order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {band: index for index, band in enumerate(LATITUDE_BAND_ORDER)}

    def key(entry: dict) -> tuple[int, int, str]:
        return (
            order.get(entry.get("family"), len(order)),
            band_order.get(entry.get("latitudeBand", ""), 99),
            entry.get("packageVersion", ""),
        )

    return sorted(packages, key=key)


def main() -> int:
    args = parse_args()
    app_repo = args.app_repo.resolve()
    generated_at = args.generated_at or utc_now()
    manifest_path = REPO_ROOT / "v1/channels/stable/manifest.json"
    manifest = read_json(manifest_path)

    package = build_package(app_repo, generated_at)
    data = write_json(REPO_ROOT / PACKAGE_PATH, package)
    descriptor = package_descriptor(
        package=package,
        data=data,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
    )

    packages = [
        entry
        for entry in manifest.get("packages", [])
        if entry.get("family") != PACKAGE_FAMILY
    ]
    packages.append(descriptor)

    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(packages)
    write_json(manifest_path, manifest)

    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
