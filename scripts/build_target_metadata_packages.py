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

PACKAGE_PATHS = {
    "targetMetadataOverlay": Path("v1/packages/target-metadata/target_metadata_overlay_v1.json"),
    "targetNeighborhoodDefinitions": Path(
        "v1/packages/target-neighborhoods/target_neighborhood_definitions_v1.json"
    ),
}

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "seasonalRecommendationCandidates",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build hosted AstroGuide target metadata packages and refresh the stable manifest."
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


def source_block(name: str, generated_by: str, notes: str) -> dict:
    return {
        "name": name,
        "generatedBy": generated_by,
        "sourceURL": "https://github.com/tophrchris/DSOPlanneriOS/tree/main/App/Resources/TargetMetadata",
        "notes": notes,
    }


def build_overlay_package(app_repo: Path, generated_at: str) -> dict:
    target_metadata = app_repo / "App/Resources/TargetMetadata"
    nebula = read_json(target_metadata / "curated_nebula_targets.json")
    galaxy = read_json(target_metadata / "curated_galaxy_targets.json")
    media = read_json(target_metadata / "curated_target_media_overrides.json")

    targets = list(nebula.get("targets") or []) + list(galaxy.get("targets") or [])
    media_overrides = list(media.get("media") or [])
    if not targets and not media_overrides:
        raise RuntimeError("Target metadata overlay package would be empty.")

    return {
        "schemaVersion": 1,
        "packageFamily": "targetMetadataOverlay",
        "packageVersion": f"target-metadata-overlay-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": source_block(
            "AstroGuide bundled target metadata overlay",
            "astroguide-metadata target package builder",
            "Combines curated nebula target metadata, curated galaxy target metadata, and curated media overrides into the dynamic metadata overlay package.",
        ),
        "targets": targets,
        "mediaOverrides": media_overrides,
    }


def build_neighborhood_package(app_repo: Path, generated_at: str) -> dict:
    target_metadata = app_repo / "App/Resources/TargetMetadata"
    neighborhoods = read_json(target_metadata / "curated_target_neighborhoods.json")
    if not neighborhoods:
        raise RuntimeError("Target neighborhood definitions package would be empty.")

    return {
        "schemaVersion": 1,
        "packageFamily": "targetNeighborhoodDefinitions",
        "packageVersion": f"target-neighborhood-definitions-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": source_block(
            "AstroGuide curated target neighborhoods",
            "astroguide-metadata target package builder",
            "Wraps the curated target neighborhood definitions in the dynamic metadata package envelope.",
        ),
        "neighborhoods": neighborhoods,
    }


def package_descriptor(
    *,
    family: str,
    package: dict,
    package_path: Path,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict:
    return {
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
        "fallbackNotes": (
            "Use the bundled target metadata snapshot only if no validated cached package is available. "
            "Cache TTL indicates when the app should check for a fresher package; an expired cached package "
            "remains usable until replaced by a validated refresh."
        ),
    }


def sort_packages(packages: list[dict]) -> list[dict]:
    order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    return sorted(packages, key=lambda entry: order.get(entry.get("family"), len(order)))


def main() -> int:
    args = parse_args()
    app_repo = args.app_repo.resolve()
    generated_at = args.generated_at or utc_now()

    manifest_path = REPO_ROOT / "v1/channels/stable/manifest.json"
    manifest = read_json(manifest_path)

    packages = {
        "targetMetadataOverlay": build_overlay_package(app_repo, generated_at),
        "targetNeighborhoodDefinitions": build_neighborhood_package(app_repo, generated_at),
    }

    generated_descriptors: dict[str, dict] = {}
    for family, package in packages.items():
        relative_path = PACKAGE_PATHS[family]
        data = write_json(REPO_ROOT / relative_path, package)
        generated_descriptors[family] = package_descriptor(
            family=family,
            package=package,
            package_path=relative_path,
            data=data,
            min_supported_app_version=args.min_supported_app_version,
            min_supported_build=args.min_supported_build,
        )

    existing_descriptors = {
        entry["family"]: entry
        for entry in manifest.get("packages", [])
        if entry.get("family") not in generated_descriptors
    }
    existing_descriptors.update(generated_descriptors)

    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(list(existing_descriptors.values()))
    write_json(manifest_path, manifest)

    for family in packages:
        descriptor = generated_descriptors[family]
        print(
            f"{family}: {descriptor['packageVersion']} "
            f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
