#!/usr/bin/env python3
"""Build hosted target image asset metadata from an approved Capture Harvest package."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
METADATA_ORIGIN = "https://metadata.astroguide.space"
PACKAGE_FAMILY = "targetImageAssets"
PACKAGE_PATH = Path("v1/packages/target-images/target_image_assets_v1.json")
ASSET_DIR = Path("v1/assets/target-images")
TARGET_METADATA_OVERLAY_PATH = Path("v1/packages/target-metadata/target_metadata_overlay_v1.json")
CACHE_TTL_SECONDS = 604800

REQUIRED_SOURCE_FILES = [
    "README.md",
    "contact-sheet.html",
    "manifest.json",
    "catalog-update.json",
    "catalog-size-updates.json",
    "catalog-size-updates.csv",
    "source-selection.json",
    "validation.json",
]

VARIANTS = [
    {
        "key": "hero",
        "sourceKey": "hero",
        "fileName": "hero.jpg",
        "role": "hero",
    },
    {
        "key": "thumbnail320",
        "sourceKey": "thumbnail",
        "fileName": "thumbnail-320.jpg",
        "role": "thumbnail320",
    },
    {
        "key": "thumbnail160",
        "sourceKey": "compactThumbnail",
        "fileName": "thumbnail-160.jpg",
        "role": "thumbnail160",
    },
]

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "targetImageAssets",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "astrophotographyEquipmentSanitizedCatalog",
    "darkSkyPlaces",
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
        description="Build hosted AstroGuide target image asset metadata."
    )
    parser.add_argument(
        "--source-package",
        type=Path,
        help="Approved Capture Harvest package directory.",
    )
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "v1/channels/stable/manifest.json",
    )
    parser.add_argument("--min-supported-app-version", default="1.4.1")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the checked-in target image package, assets, and manifest descriptor.",
    )
    return parser.parse_args()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_descriptor(path: Path, relative_to: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(relative_to).as_posix(),
        "byteSize": len(data),
        "sha256": sha256_bytes(data),
    }


def parse_timestamp(value: Any) -> dt.datetime | None:
    if not value:
        return None
    raw = str(value).replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.UTC)
    return parsed.astimezone(dt.UTC)


def normalized_timestamp(value: Any) -> str:
    parsed = parse_timestamp(value)
    if parsed is None:
        raise RuntimeError(f"Invalid timestamp: {value}")
    return parsed.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(generated_at: str) -> str:
    return generated_at.split("T", maxsplit=1)[0]


def path_safe(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_-]+", value))


def normalized_identifier(value: Any) -> str:
    return "".join(character for character in str(value or "").upper() if character.isalnum())


def ordered_unique(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def required_int(payload: dict[str, Any], key: str) -> int:
    if key not in payload:
        raise RuntimeError(f"Missing required integer field: {key}")
    value = payload.get(key)
    if isinstance(value, bool):
        raise RuntimeError(f"Field {key} must be an integer, not a boolean.")
    try:
        return int(value)
    except (TypeError, ValueError) as error:
        raise RuntimeError(f"Field {key} must be an integer.") from error


def validate_source_package(source_root: Path) -> dict[str, Any]:
    source_root = source_root.resolve()
    if not source_root.is_dir():
        raise RuntimeError(f"Source package directory does not exist: {source_root}")

    missing = [name for name in REQUIRED_SOURCE_FILES if not (source_root / name).exists()]
    if missing:
        raise RuntimeError(f"Source package is missing required files: {', '.join(missing)}")

    manifest = read_json(source_root / "manifest.json")
    selection = read_json(source_root / "source-selection.json")
    validation = read_json(source_root / "validation.json")
    size_updates = read_json(source_root / "catalog-size-updates.json")

    if manifest.get("schema") != "astroguide-capture-package/v1":
        raise RuntimeError("Source manifest schema must be astroguide-capture-package/v1.")
    if validation.get("passed") is not True:
        raise RuntimeError("Source validation.json did not pass.")

    subjects = manifest.get("subjects")
    if not isinstance(subjects, list) or not subjects:
        raise RuntimeError("Source manifest contains no subjects.")
    object_ids = [str(subject.get("objectId") or "") for subject in subjects]
    if any(not object_id for object_id in object_ids):
        raise RuntimeError("Every source subject must include objectId.")
    if len(object_ids) != len(set(object_ids)):
        raise RuntimeError("Source manifest objectIds must be unique.")
    if required_int(manifest, "selectionCount") != len(subjects):
        raise RuntimeError("Source manifest selectionCount does not match subjects.")
    if required_int(selection, "selectionCount") != len(selection.get("selections") or []):
        raise RuntimeError("Source selectionCount does not match source-selection selections.")
    if required_int(selection, "selectionCount") != len(subjects):
        raise RuntimeError("source-selection.json selectionCount does not match manifest subjects.")

    asset_ids = [str(subject.get("assetId") or "") for subject in subjects]
    if any(not asset_id for asset_id in asset_ids):
        raise RuntimeError("Every source subject must include assetId.")
    if any(not path_safe(asset_id) for asset_id in asset_ids):
        raise RuntimeError("Source assetId values must be path-safe.")
    if any(not path_safe(object_id) for object_id in object_ids):
        raise RuntimeError("Source objectId values must be path-safe.")

    asset_counts = Counter(asset_ids)
    shared_assets = {asset_id: count for asset_id, count in asset_counts.items() if count > 1}
    if required_int(manifest, "assetCount") != len(asset_counts):
        raise RuntimeError("Source manifest assetCount does not match unique assets.")
    if required_int(manifest, "sharedAssetCount") != len(shared_assets):
        raise RuntimeError("Source manifest sharedAssetCount does not match shared assets.")

    expanded_count = sum(
        1
        for subject in subjects
        if (subject.get("cropFraming") or {}).get("mode") != "exact"
    )
    if required_int(manifest, "expandedCropCount") != expanded_count:
        raise RuntimeError("Source manifest expandedCropCount does not match subjects.")

    manual_warning_count = sum(
        1
        for subject in subjects
        if subject.get("humanSelected") and not subject.get("qualityReady")
    )
    if required_int(manifest, "manualSelectionCount") != manual_warning_count:
        raise RuntimeError("Source manifest manualSelectionCount does not match subjects.")
    if required_int(validation, "manualSelectionWarnings") != manual_warning_count:
        raise RuntimeError("validation.json manualSelectionWarnings does not match subjects.")

    size_proposals = size_updates.get("updates") or []
    if required_int(manifest, "sizeProposalCount") != len(size_proposals):
        raise RuntimeError("Source manifest sizeProposalCount does not match catalog-size-updates.json.")

    path_to_descriptor: dict[str, dict[str, Any]] = {}
    asset_media_descriptors: dict[str, dict[str, Any]] = {}
    for subject in subjects:
        media = subject.get("media") or {}
        asset_id = str(subject["assetId"])
        asset_media = {
            variant["sourceKey"]: media.get(variant["sourceKey"])
            for variant in VARIANTS
        }
        prior_asset_media = asset_media_descriptors.get(asset_id)
        if prior_asset_media is not None and prior_asset_media != asset_media:
            raise RuntimeError(f"Shared asset has inconsistent media descriptors: {asset_id}")
        asset_media_descriptors[asset_id] = asset_media
        for variant in VARIANTS:
            item = media.get(variant["sourceKey"])
            if not isinstance(item, dict):
                raise RuntimeError(f"{subject.get('objectId')} is missing {variant['sourceKey']} media.")
            relative_path = str(item.get("path") or "")
            if not relative_path:
                raise RuntimeError(f"{subject.get('objectId')} {variant['sourceKey']} path is empty.")
            path = source_root / relative_path
            if not path.exists():
                raise RuntimeError(f"Missing source image: {relative_path}")
            data = path.read_bytes()
            if int(item.get("bytes") or -1) != len(data):
                raise RuntimeError(f"Source byte mismatch: {relative_path}")
            if str(item.get("sha256") or "") != sha256_bytes(data):
                raise RuntimeError(f"Source SHA-256 mismatch: {relative_path}")
            prior = path_to_descriptor.get(relative_path)
            if prior is not None and prior != item:
                raise RuntimeError(f"Shared source path has inconsistent metadata: {relative_path}")
            path_to_descriptor[relative_path] = item

    if required_int(validation, "selectionCount") != len(subjects):
        raise RuntimeError("validation.json selectionCount does not match subjects.")
    if required_int(validation, "assetCount") != len(asset_counts):
        raise RuntimeError("validation.json assetCount does not match unique assets.")
    if required_int(validation, "checkedImageFiles") != len(path_to_descriptor):
        raise RuntimeError("validation.json checkedImageFiles does not match distinct images.")

    return {
        "sourceRoot": source_root,
        "manifest": manifest,
        "selection": selection,
        "validation": validation,
        "sizeUpdates": size_updates,
        "sourceFiles": [file_descriptor(source_root / name, source_root) for name in REQUIRED_SOURCE_FILES],
        "distinctImageFileCount": len(path_to_descriptor),
        "variantReferenceCount": len(subjects) * len(VARIANTS),
        "sharedAssets": shared_assets,
    }


def target_metadata_aliases() -> dict[str, dict[str, Any]]:
    path = REPO_ROOT / TARGET_METADATA_OVERLAY_PATH
    if not path.exists():
        return {}
    package = read_json(path)
    aliases_by_key: dict[str, dict[str, Any]] = {}
    for target in package.get("targets") or []:
        resolution = target.get("resolution") or {}
        candidate_values = [
            target.get("canonicalID"),
            target.get("preferredName"),
            resolution.get("catalogObjectID"),
            *(target.get("aliases") or []),
        ]
        alias_payload = {
            "preferredName": target.get("preferredName"),
            "aliases": target.get("aliases") or [],
            "targetMetadataCanonicalID": target.get("canonicalID"),
            "targetMetadataCatalogObjectID": resolution.get("catalogObjectID"),
        }
        for value in candidate_values:
            key = normalized_identifier(value)
            if key:
                aliases_by_key.setdefault(key, alias_payload)
    return aliases_by_key


def source_selection_by_object_id(selection: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("objectId")): row
        for row in selection.get("selections") or []
        if row.get("objectId")
    }


def asset_owner_by_asset_id(subjects: list[dict[str, Any]]) -> dict[str, str]:
    owners: dict[str, str] = {}
    for subject in subjects:
        owners.setdefault(str(subject["assetId"]), str(subject["objectId"]))
    return owners


def shared_target_ids_by_asset_id(subjects: list[dict[str, Any]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for subject in subjects:
        grouped[str(subject["assetId"])].append(str(subject["objectId"]))
    return {asset_id: sorted(target_ids) for asset_id, target_ids in grouped.items() if len(target_ids) > 1}


def build_aliases(
    subject: dict[str, Any],
    overlay_aliases: dict[str, dict[str, Any]],
) -> tuple[list[str], list[str], dict[str, Any] | None]:
    object_id = str(subject.get("objectId") or "")
    overlay = overlay_aliases.get(normalized_identifier(object_id))
    alias_values: list[Any] = []
    alternate_ids: list[Any] = []

    if subject.get("commonName"):
        alias_values.append(subject.get("commonName"))
    if overlay:
        alias_values.append(overlay.get("preferredName"))
        alias_values.extend(overlay.get("aliases") or [])
        alternate_ids.append(overlay.get("targetMetadataCanonicalID"))
        alternate_ids.append(overlay.get("targetMetadataCatalogObjectID"))

    alternate_ids.extend(subject.get("associatedSubjects") or [])
    aliases = [
        value
        for value in ordered_unique(alias_values)
        if normalized_identifier(value) != normalized_identifier(object_id)
    ]
    alternate_ids = [
        value
        for value in ordered_unique(alternate_ids)
        if normalized_identifier(value) != normalized_identifier(object_id)
    ]
    return aliases, alternate_ids, overlay


def copy_asset_files(
    *,
    source_root: Path,
    subjects: list[dict[str, Any]],
    owners: dict[str, str],
) -> None:
    destination_root = REPO_ROOT / ASSET_DIR
    if destination_root.exists():
        shutil.rmtree(destination_root)

    copied: set[str] = set()
    subjects_by_asset: dict[str, dict[str, Any]] = {}
    for subject in subjects:
        subjects_by_asset.setdefault(str(subject["assetId"]), subject)
    for asset_id in sorted(subjects_by_asset):
        source_subject = subjects_by_asset[asset_id]
        owner_id = owners[asset_id]
        destination_dir = destination_root / owner_id / asset_id
        destination_dir.mkdir(parents=True, exist_ok=True)
        for variant in VARIANTS:
            item = source_subject["media"][variant["sourceKey"]]
            source_path = source_root / item["path"]
            destination_path = destination_dir / variant["fileName"]
            shutil.copyfile(source_path, destination_path)
            data = destination_path.read_bytes()
            if sha256_bytes(data) != item["sha256"]:
                raise RuntimeError(f"Copied asset hash mismatch for {destination_path}")
            copied.add(destination_path.relative_to(REPO_ROOT).as_posix())

    if len(copied) != len(subjects_by_asset) * len(VARIANTS):
        raise RuntimeError("Copied target image file count does not match distinct assets.")


def build_variant(
    *,
    subject: dict[str, Any],
    owner_id: str,
    variant: dict[str, str],
) -> dict[str, Any]:
    source_item = subject["media"][variant["sourceKey"]]
    relative_path = ASSET_DIR / owner_id / str(subject["assetId"]) / variant["fileName"]
    return {
        "role": variant["role"],
        "path": relative_path.as_posix(),
        "url": f"{METADATA_ORIGIN}/{relative_path.as_posix()}",
        "width": source_item["width"],
        "height": source_item["height"],
        "byteSize": source_item["bytes"],
        "sha256": source_item["sha256"],
        "sourcePath": source_item["path"],
    }


def record_geometry(
    subject: dict[str, Any],
    selection: dict[str, Any] | None,
) -> dict[str, Any]:
    geometry: dict[str, Any] = {
        "orientationStandard": "north-up-east-left",
        "framing": subject.get("framing"),
        "cropFraming": subject.get("cropFraming"),
        "naturalSourceOutputSize": (subject.get("media") or {}).get("naturalSourceOutputSize"),
        "heroCapped": bool((subject.get("media") or {}).get("heroCapped")),
    }
    if selection:
        for key in (
            "nativeSize",
            "productionNativeSize",
            "sourceCrop",
            "displayCrop",
            "exactTreatmentCrop",
            "productionCrop",
            "originalImageDimensions",
            "orientation",
            "frameMarginFraction",
        ):
            if key in selection:
                geometry[key] = selection[key]
    return {key: value for key, value in geometry.items() if value is not None}


def build_records(
    *,
    manifest: dict[str, Any],
    selection: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    subjects = manifest.get("subjects") or []
    owners = asset_owner_by_asset_id(subjects)
    shared_targets = shared_target_ids_by_asset_id(subjects)
    selections = source_selection_by_object_id(selection)
    overlay_aliases = target_metadata_aliases()

    records: list[dict[str, Any]] = []
    shared_asset_records: list[dict[str, Any]] = []
    for asset_id, target_ids in sorted(shared_targets.items()):
        shared_asset_records.append(
            {
                "assetID": asset_id,
                "assetOwnerTargetID": owners[asset_id],
                "targetIDs": target_ids,
            }
        )

    for subject in subjects:
        object_id = str(subject["objectId"])
        asset_id = str(subject["assetId"])
        owner_id = owners[asset_id]
        aliases, alternate_ids, overlay = build_aliases(subject, overlay_aliases)
        display_name = subject.get("commonName") or (overlay or {}).get("preferredName") or object_id
        selection_record = selections.get(object_id)
        variants = {
            variant["key"]: build_variant(subject=subject, owner_id=owner_id, variant=variant)
            for variant in VARIANTS
        }
        shared_target_ids = shared_targets.get(asset_id, [])

        records.append(
            {
                "canonicalTargetID": object_id,
                "catalogObjectID": object_id,
                "catalog": subject.get("catalog"),
                "displayName": display_name,
                "commonName": subject.get("commonName"),
                "objectType": subject.get("objectType"),
                "constellation": subject.get("constellation"),
                "aliases": aliases,
                "alternateIDs": alternate_ids,
                "assetID": asset_id,
                "sourceAssetID": asset_id,
                "assetOwnerTargetID": owner_id,
                "isSharedAsset": bool(shared_target_ids),
                "sharedWithTargetIDs": shared_target_ids,
                "variants": variants,
                "geometry": record_geometry(subject, selection_record),
                "quality": {
                    "automaticQualityReady": bool(subject.get("qualityReady")),
                    "humanSelected": bool(subject.get("humanSelected")),
                    "manualSelectionWarning": bool(subject.get("humanSelected") and not subject.get("qualityReady")),
                    "wcsMethod": subject.get("wcsMethod"),
                    "preferredResult": bool(subject.get("preferredResult")),
                },
                "source": {
                    "sourcePackageID": manifest.get("packageId"),
                    "sourcePackageGeneratedAt": manifest.get("generatedAt"),
                    "selectionExport": manifest.get("selectionExport"),
                    "result": subject.get("result"),
                    "captureResultID": (subject.get("result") or {}).get("resultId"),
                    "captureDate": (subject.get("result") or {}).get("captureDate"),
                    "attribution": "AstroGuide Capture Harvest approved target image asset",
                    "notes": (
                        "Image bytes are cached under AstroGuide metadata paths. "
                        "Source result-gallery paths are retained only as provenance."
                    ),
                },
            }
        )

    records.sort(key=lambda row: row["canonicalTargetID"])
    return records, shared_asset_records


def build_package(
    *,
    source_validation: dict[str, Any],
    generated_at: str,
    package_version: str,
) -> dict[str, Any]:
    manifest = source_validation["manifest"]
    validation = source_validation["validation"]
    records, shared_assets = build_records(
        manifest=manifest,
        selection=source_validation["selection"],
    )

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "packageRole": "index",
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide Capture Harvest approved target image assets",
            "generatedBy": "astroguide-metadata target image package builder",
            "sourcePackageID": manifest.get("packageId"),
            "sourcePackageGeneratedAt": manifest.get("generatedAt"),
            "selectionExport": manifest.get("selectionExport"),
            "reportGeneratedAt": (manifest.get("source") or {}).get("reportGeneratedAt"),
            "galleryGeneratedAt": (manifest.get("source") or {}).get("galleryGeneratedAt"),
            "astroGuideCatalogVersion": (manifest.get("source") or {}).get("astroGuideCatalogVersion"),
            "sirilTag": (manifest.get("source") or {}).get("sirilTag"),
            "orientationStandard": manifest.get("orientationStandard"),
            "sourceFiles": source_validation["sourceFiles"],
            "attribution": "AstroGuide Capture Harvest approved selections",
            "notes": (
                "Publishes cached 160 px, 320 px, and hero image variants for target detail/list consumers. "
                "The core app catalog remains URL-free; clients resolve these relative paths through the "
                "dynamic metadata package."
            ),
        },
        "compatibility": {
            "relativeAssetBase": ASSET_DIR.as_posix(),
            "metadataOrigin": METADATA_ORIGIN,
            "clientsShouldNotHotlinkSourceGallery": True,
            "sharedAssetsAreDeduplicated": True,
        },
        "counts": {
            "targetRecords": len(records),
            "uniqueCatalogObjectIDs": len({record["catalogObjectID"] for record in records}),
            "distinctAssets": int(manifest.get("assetCount") or 0),
            "sharedAssets": int(manifest.get("sharedAssetCount") or 0),
            "variantReferences": source_validation["variantReferenceCount"],
            "imageFiles": source_validation["distinctImageFileCount"],
            "expandedContextCrops": int(manifest.get("expandedCropCount") or 0),
            "humanApprovedAutomaticQualityWarnings": int(validation.get("manualSelectionWarnings") or 0),
            "sirilBackedSizeProposals": int(manifest.get("sizeProposalCount") or 0),
        },
        "sharedAssets": shared_assets,
        "targets": records,
    }


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
            "value": sha256_bytes(data),
        },
        "byteSize": len(data),
        "recordCount": int((package.get("counts") or {}).get("targetRecords") or 0),
        "assetCount": int((package.get("counts") or {}).get("distinctAssets") or 0),
        "imageFileCount": int((package.get("counts") or {}).get("imageFiles") or 0),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Clients that support this family should use bundled target thumbnails when available, "
            "then load these hosted target-image assets lazily and degrade gracefully if the package "
            "is absent, expired, or invalid."
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


def update_manifest(manifest_path: Path, generated_at: str, descriptor: dict[str, Any]) -> None:
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


def validate_variant(record: dict[str, Any], variant_key: str, variant: dict[str, Any]) -> str:
    target_id = str(record.get("canonicalTargetID") or "")
    path_value = str(variant.get("path") or "")
    if not path_value.startswith(f"{ASSET_DIR.as_posix()}/"):
        raise RuntimeError(f"{target_id} {variant_key} path is outside target image assets.")
    if path_value.startswith("http://") or path_value.startswith("https://"):
        raise RuntimeError(f"{target_id} {variant_key} path must be relative.")
    expected_url = f"{METADATA_ORIGIN}/{path_value}"
    if variant.get("url") != expected_url:
        raise RuntimeError(f"{target_id} {variant_key} url does not match metadata origin.")
    path = REPO_ROOT / path_value
    if not path.exists():
        raise RuntimeError(f"Missing target image asset: {path_value}")
    data = path.read_bytes()
    if int(variant.get("byteSize") or -1) != len(data):
        raise RuntimeError(f"{target_id} {variant_key} byteSize mismatch.")
    if str(variant.get("sha256") or "") != sha256_bytes(data):
        raise RuntimeError(f"{target_id} {variant_key} SHA-256 mismatch.")
    if int(variant.get("width") or 0) <= 0 or int(variant.get("height") or 0) <= 0:
        raise RuntimeError(f"{target_id} {variant_key} dimensions must be positive.")
    return path_value


def validate_package(package: dict[str, Any], package_path: Path) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Target image package schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Target image packageFamily must be {PACKAGE_FAMILY}.")
    if package.get("packageRole") != "index":
        raise RuntimeError("Target image packageRole must be index.")
    if parse_timestamp(package.get("generatedAt")) is None:
        raise RuntimeError("Target image package generatedAt must be an ISO-8601 timestamp.")

    records = package.get("targets")
    if not isinstance(records, list) or not records:
        raise RuntimeError("Target image package contains no records.")
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    asset_counter: Counter[str] = Counter()
    for record in records:
        target_id = str(record.get("canonicalTargetID") or "")
        if not target_id:
            raise RuntimeError("Target image record is missing canonicalTargetID.")
        if target_id in seen_ids:
            raise RuntimeError(f"Duplicate target image canonicalTargetID: {target_id}")
        if not path_safe(target_id):
            raise RuntimeError(f"Target image canonicalTargetID is not path-safe: {target_id}")
        seen_ids.add(target_id)

        asset_id = str(record.get("assetID") or "")
        if not asset_id:
            raise RuntimeError(f"{target_id} is missing assetID.")
        asset_counter[asset_id] += 1
        variants = record.get("variants")
        if not isinstance(variants, dict):
            raise RuntimeError(f"{target_id} variants must be an object.")
        for variant in VARIANTS:
            value = variants.get(variant["key"])
            if not isinstance(value, dict):
                raise RuntimeError(f"{target_id} is missing {variant['key']}.")
            seen_paths.add(validate_variant(record, variant["key"], value))

        quality = record.get("quality") or {}
        if quality.get("manualSelectionWarning") and quality.get("automaticQualityReady"):
            raise RuntimeError(f"{target_id} manualSelectionWarning conflicts with qualityReady.")
        source = record.get("source") or {}
        result = source.get("result") or {}
        for value in (result.get("persistedImagePath"), result.get("originalPngSource")):
            if str(value or "").startswith(("http://", "https://")):
                raise RuntimeError(f"{target_id} source gallery provenance must not be a hotlink.")

    counts = package.get("counts") or {}
    shared_assets = {asset_id: count for asset_id, count in asset_counter.items() if count > 1}
    if required_int(counts, "targetRecords") != len(records):
        raise RuntimeError("Target image count targetRecords mismatch.")
    if required_int(counts, "uniqueCatalogObjectIDs") != len(seen_ids):
        raise RuntimeError("Target image count uniqueCatalogObjectIDs mismatch.")
    if required_int(counts, "distinctAssets") != len(asset_counter):
        raise RuntimeError("Target image count distinctAssets mismatch.")
    if required_int(counts, "sharedAssets") != len(shared_assets):
        raise RuntimeError("Target image count sharedAssets mismatch.")
    if required_int(counts, "variantReferences") != len(records) * len(VARIANTS):
        raise RuntimeError("Target image count variantReferences mismatch.")
    if required_int(counts, "imageFiles") != len(seen_paths):
        raise RuntimeError("Target image count imageFiles mismatch.")

    expected_shared = [
        {
            "assetID": asset_id,
            "assetOwnerTargetID": next(
                str(record.get("assetOwnerTargetID") or "")
                for record in records
                if record.get("assetID") == asset_id
            ),
            "targetIDs": [
                str(record.get("canonicalTargetID") or "")
                for record in records
                if record.get("assetID") == asset_id
            ],
        }
        for asset_id in sorted(shared_assets)
    ]
    if package.get("sharedAssets") != expected_shared:
        raise RuntimeError("Target image sharedAssets list does not match records.")
    if not package_path.exists():
        raise RuntimeError("Target image package path does not exist.")


def validate_manifest_descriptor(manifest_path: Path, package: dict[str, Any], package_data: bytes) -> None:
    manifest = read_json(manifest_path)
    matching = [entry for entry in manifest.get("packages") or [] if entry.get("family") == PACKAGE_FAMILY]
    if len(matching) != 1:
        raise RuntimeError("Stable manifest must contain exactly one targetImageAssets descriptor.")
    entry = matching[0]
    if entry.get("packageVersion") != package.get("packageVersion"):
        raise RuntimeError("Manifest packageVersion does not match target image package.")
    if entry.get("packageURL") != f"{METADATA_ORIGIN}/{PACKAGE_PATH.as_posix()}":
        raise RuntimeError("Manifest packageURL does not reference target image package.")
    if int(entry.get("byteSize") or 0) != len(package_data):
        raise RuntimeError("Manifest byteSize does not match target image package.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != sha256_bytes(package_data):
        raise RuntimeError("Manifest checksum does not match target image package.")
    counts = package.get("counts") or {}
    if required_int(entry, "recordCount") != required_int(counts, "targetRecords"):
        raise RuntimeError("Manifest recordCount does not match target image package.")
    if required_int(entry, "assetCount") != required_int(counts, "distinctAssets"):
        raise RuntimeError("Manifest assetCount does not match target image package.")
    if required_int(entry, "imageFileCount") != required_int(counts, "imageFiles"):
        raise RuntimeError("Manifest imageFileCount does not match target image package.")
    if manifest.get("packages") != sort_packages(manifest.get("packages") or []):
        raise RuntimeError("Stable manifest package descriptors are not deterministically sorted.")


def write_target_image_package(
    *,
    source_root: Path,
    generated_at: str,
    package_version: str,
    min_supported_app_version: str,
    min_supported_build: str,
    update_manifest_path: Path | None,
) -> dict[str, Any]:
    source_validation = validate_source_package(source_root)
    subjects = source_validation["manifest"].get("subjects") or []
    owners = asset_owner_by_asset_id(subjects)
    copy_asset_files(
        source_root=source_validation["sourceRoot"],
        subjects=subjects,
        owners=owners,
    )

    package = build_package(
        source_validation=source_validation,
        generated_at=generated_at,
        package_version=package_version,
    )
    data = write_json(REPO_ROOT / PACKAGE_PATH, package)
    descriptor = package_descriptor(
        package=package,
        data=data,
        min_supported_app_version=min_supported_app_version,
        min_supported_build=min_supported_build,
    )
    if update_manifest_path is not None:
        update_manifest(update_manifest_path, generated_at, descriptor)
    validate_package(package, REPO_ROOT / PACKAGE_PATH)
    if update_manifest_path is not None:
        validate_manifest_descriptor(update_manifest_path, package, data)
    return descriptor


def main() -> None:
    args = parse_args()
    if args.validate_only:
        package_path = REPO_ROOT / PACKAGE_PATH
        package_data = package_path.read_bytes()
        package = read_json(package_path)
        validate_package(package, package_path)
        if not args.skip_manifest:
            validate_manifest_descriptor(args.manifest, package, package_data)
        print(
            "Validated target image package: "
            f"{(package.get('counts') or {}).get('targetRecords')} targets, "
            f"{(package.get('counts') or {}).get('distinctAssets')} assets, "
            f"{(package.get('counts') or {}).get('imageFiles')} image files"
        )
        return

    if args.source_package is None:
        raise RuntimeError("--source-package is required unless --validate-only is used.")

    source_validation = validate_source_package(args.source_package)
    source_generated_at = (source_validation["manifest"] or {}).get("generatedAt")
    generated_at = normalized_timestamp(args.generated_at or source_generated_at)
    package_version = args.package_version or f"target-image-assets-v1-{date_token(generated_at)}-capture-harvest-75"
    descriptor = write_target_image_package(
        source_root=args.source_package,
        generated_at=generated_at,
        package_version=package_version,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
        update_manifest_path=None if args.skip_manifest else args.manifest,
    )
    print(
        "Wrote target image package: "
        f"{descriptor['recordCount']} targets, "
        f"{descriptor['assetCount']} assets, "
        f"{descriptor['imageFileCount']} image files, "
        f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
    )


if __name__ == "__main__":
    main()
