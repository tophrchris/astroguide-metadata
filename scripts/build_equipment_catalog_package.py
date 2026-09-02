#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
EQUIPMENT_PACKAGE_FAMILY = "equipmentCatalog"
EQUIPMENT_PACKAGE_PATH = Path("v1/packages/equipment/equipment_catalog_v1.json")
ASTROPHOTOGRAPHY_PACKAGE_FAMILY = "astrophotographyEquipmentCatalog"
ASTROPHOTOGRAPHY_PACKAGE_PATH = Path("v1/packages/equipment/astrophotography_equipment_catalog_v1.json")
SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_FAMILY = "astrophotographyEquipmentSanitizedCatalog"
SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_PATH = Path(
    "v1/packages/equipment/astrophotography_equipment_sanitized_catalog_v1.json"
)

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
        description="Build hosted AstroGuide equipment catalog packages and refresh the stable manifest."
    )
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument("--generated-at")
    parser.add_argument("--min-supported-app-version", default="0.1.2")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument(
        "--package",
        choices=["equipment", "astrophotography", "astrophotography-sanitized", "all"],
        default="equipment",
        help=(
            "Package family to rebuild. Defaults to the legacy smart-scope equipment package; "
            "use 'astrophotography' for Telescope Workshop optics/cameras, "
            "'astrophotography-sanitized' for the app-rendered Telescope Workshop projection, "
            "or 'all' for every equipment package."
        ),
    )
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


def build_equipment_package(app_repo: Path, generated_at: str) -> dict:
    catalog_path = app_repo / "App/Resources/Equipment/equipment_catalog.json"
    catalog = read_json(catalog_path)
    categories = catalog.get("categories") or []
    if not categories:
        raise RuntimeError("Equipment catalog package would be empty.")

    return {
        "schemaVersion": 1,
        "packageFamily": EQUIPMENT_PACKAGE_FAMILY,
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


def build_astrophotography_package(app_repo: Path, generated_at: str) -> dict:
    catalog_path = app_repo / "App/Resources/Equipment/astrophotography_equipment.json"
    curation_path = app_repo / "App/Resources/Equipment/astrophotography_equipment_curation.json"
    catalog = read_json(catalog_path)
    curation = read_json(curation_path) if curation_path.exists() else None
    optical_components = catalog.get("opticalComponents") or []
    camera_components = catalog.get("cameraComponents") or []
    if not optical_components and not camera_components:
        raise RuntimeError("Astrophotography equipment catalog package would be empty.")

    return {
        "schemaVersion": 1,
        "packageFamily": ASTROPHOTOGRAPHY_PACKAGE_FAMILY,
        "packageVersion": f"astrophotography-equipment-catalog-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide bundled astrophotography equipment catalog",
            "generatedBy": "astroguide-metadata equipment package builder",
            "sourceURL": (
                "https://github.com/tophrchris/DSOPlanneriOS/tree/main/"
                "App/Resources/Equipment/astrophotography_equipment.json"
            ),
            "notes": "Wraps the bundled Telescope Workshop optics and imaging component catalog in the dynamic metadata package envelope.",
        },
        "catalog": catalog,
        "curation": curation,
    }


def normalized_key(value: str | None) -> str:
    if value is None:
        return ""
    return "".join(character for character in value.lower() if character.isalnum())


def catalog_include_flag(value) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"", "1", "true", "yes", "y", "include", "included"}:
            return True
        if normalized in {"0", "false", "no", "n", "exclude", "excluded"}:
            return False
    return True


def finite_positive_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def positive_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def optical_kind(component: dict) -> str:
    component_type = str(component.get("component_type") or "").strip().lower()
    if component_type in {"lens", "lens_candidate"}:
        return "lens"
    return "optical_tube"


def optical_type_label(component: dict) -> str:
    return "Lens" if optical_kind(component) == "lens" else "Tube"


def display_name(component: dict) -> str:
    return f"{component.get('manufacturer', '')} {component.get('model', '')}".strip()


def tokenized(value: str) -> list[str]:
    return [token for token in re.split(r"[^A-Za-z0-9]+", value) if token]


def model_matches_product_line(model: str, product_line: str) -> bool:
    line = product_line.strip()
    if not line:
        return False

    lowercased_model = model.lower()
    lowercased_line = line.lower()
    if len(lowercased_line) <= 2:
        tokens = tokenized(lowercased_model)
        return lowercased_line in tokens or (tokens[0].startswith(lowercased_line) if tokens else False)
    return lowercased_line in lowercased_model


def product_lines_for_manufacturer(curation: dict | None, manufacturer: str) -> list[str]:
    if not curation:
        return []
    manufacturer_key = normalized_key(manufacturer)
    return [
        entry.get("productLine", "")
        for entry in curation.get("opticalProductLines", [])
        if normalized_key(entry.get("manufacturer")) == manufacturer_key
    ]


def optical_product_line(component: dict, curation: dict | None) -> str | None:
    lines = sorted(
        product_lines_for_manufacturer(curation, str(component.get("manufacturer") or "")),
        key=lambda value: (-len(value), natural_sort_key(value)),
    )
    model = str(component.get("model") or "")
    for product_line in lines:
        if model_matches_product_line(model, product_line):
            return product_line
    return None


def contains_excluded_term(value: str, curation: dict | None) -> bool:
    if not curation:
        return False
    lowercased = value.lower()
    terms = curation.get("excludedModelPhrases", []) + curation.get("excludedSmartTelescopeTerms", [])
    return any(term.strip().lower() and term.strip().lower() in lowercased for term in terms)


def allows_optical_component(component: dict, curation: dict | None) -> bool:
    if not curation:
        return True
    allowed = {normalized_key(value) for value in curation.get("opticalBrandAllowlist", [])}
    return (
        normalized_key(component.get("manufacturer")) in allowed
        and not contains_excluded_term(str(component.get("model") or ""), curation)
    )


def camera_pixel_size_microns(component: dict) -> float | None:
    width = component.get("pixel_size_width_um")
    height = component.get("pixel_size_height_um")
    if finite_positive_number(width) and finite_positive_number(height):
        if abs(float(width) - float(height)) <= 0.001:
            return (float(width) + float(height)) / 2.0
        return None
    if finite_positive_number(width):
        return float(width)
    if finite_positive_number(height):
        return float(height)
    return None


def camera_has_usable_sensor_geometry(component: dict) -> bool:
    sensor_width = component.get("sensor_width_mm")
    sensor_height = component.get("sensor_height_mm")
    if finite_positive_number(sensor_width) and finite_positive_number(sensor_height):
        return True
    return (
        camera_pixel_size_microns(component) is not None
        and positive_int(component.get("horizontal_resolution_px"))
        and positive_int(component.get("vertical_resolution_px"))
    )


def allows_camera_component(component: dict, curation: dict | None) -> bool:
    if not curation:
        return True
    allowed = {normalized_key(value) for value in curation.get("cameraBrandAllowlist", [])}
    exclusion_value = f"{component.get('manufacturer', '')} {component.get('model', '')}"
    return (
        normalized_key(component.get("manufacturer")) in allowed
        and not contains_excluded_term(exclusion_value, curation)
    )


def is_selectable_optical_component(component: dict, curation: dict | None) -> bool:
    return (
        catalog_include_flag(component.get("include_in_app"))
        and bool(str(component.get("component_id") or "").strip())
        and bool(str(component.get("manufacturer") or "").strip())
        and bool(str(component.get("model") or "").strip())
        and finite_positive_number(component.get("aperture_mm"))
        and finite_positive_number(component.get("native_focal_length_mm"))
        and allows_optical_component(component, curation)
    )


def is_selectable_camera_component(component: dict, curation: dict | None) -> bool:
    return (
        catalog_include_flag(component.get("include_in_app"))
        and bool(str(component.get("component_id") or "").strip())
        and bool(str(component.get("manufacturer") or "").strip())
        and bool(str(component.get("model") or "").strip())
        and camera_has_usable_sensor_geometry(component)
        and allows_camera_component(component, curation)
    )


def natural_sort_key(value: str | None) -> list:
    parts = re.split(r"(\d+)", str(value or "").casefold())
    return [int(part) if part.isdigit() else part for part in parts]


def sanitize_optional(component: dict, key: str):
    value = component.get(key)
    if value in ("", [], {}):
        return None
    return value


def sanitized_optical_component(component: dict, curation: dict | None) -> dict:
    product_line = optical_product_line(component, curation)
    sanitized = {
        "component_id": component["component_id"],
        "component_type": optical_kind(component),
        "type_label": optical_type_label(component),
        "manufacturer": component["manufacturer"],
        "product_line": product_line,
        "model": component["model"],
        "display_name": display_name(component),
        "aperture_mm": component["aperture_mm"],
        "native_focal_length_mm": component["native_focal_length_mm"],
    }
    for source_key in (
        "native_focal_ratio",
        "optical_design",
        "source_id",
        "source_label",
        "source_url",
        "source_attribution",
        "source_confidence",
    ):
        value = sanitize_optional(component, source_key)
        if value is not None:
            sanitized[source_key] = value
    return sanitized


def sanitized_camera_component(component: dict) -> dict:
    sanitized = {
        "component_id": component["component_id"],
        "component_type": "camera",
        "manufacturer": component["manufacturer"],
        "model": component["model"],
        "display_name": display_name(component),
    }
    for source_key in (
        "sensor_model",
        "pixel_size_width_um",
        "pixel_size_height_um",
        "horizontal_resolution_px",
        "vertical_resolution_px",
        "sensor_width_mm",
        "sensor_height_mm",
        "sensor_diagonal_mm",
        "max_supported_magnitude",
        "supported_sub_lengths_seconds",
        "source_id",
        "source_label",
        "source_url",
        "source_attribution",
        "source_confidence",
    ):
        value = sanitize_optional(component, source_key)
        if value is not None:
            sanitized[source_key] = value
    pixel_size = camera_pixel_size_microns(component)
    if pixel_size is not None:
        sanitized["pixel_size_um"] = round(pixel_size, 6)
    return sanitized


def sorted_unique(values: list[str]) -> list[str]:
    return sorted(
        {value.strip() for value in values if value and value.strip()},
        key=natural_sort_key,
    )


def build_sanitized_astrophotography_package(app_repo: Path, generated_at: str) -> dict:
    catalog_path = app_repo / "App/Resources/Equipment/astrophotography_equipment.json"
    curation_path = app_repo / "App/Resources/Equipment/astrophotography_equipment_curation.json"
    catalog = read_json(catalog_path)
    curation = read_json(curation_path) if curation_path.exists() else None

    selectable_optics = [
        component
        for component in catalog.get("opticalComponents", [])
        if is_selectable_optical_component(component, curation)
    ]
    selectable_optics.sort(
        key=lambda component: (
            natural_sort_key(component.get("manufacturer")),
            optical_kind(component),
            natural_sort_key(component.get("model")),
        )
    )

    selectable_cameras = [
        component
        for component in catalog.get("cameraComponents", [])
        if is_selectable_camera_component(component, curation)
    ]
    selectable_cameras.sort(
        key=lambda component: (
            natural_sort_key(component.get("manufacturer")),
            natural_sort_key(component.get("model")),
        )
    )

    if not selectable_optics and not selectable_cameras:
        raise RuntimeError("Sanitized astrophotography equipment package would be empty.")

    sanitized_optics = [
        sanitized_optical_component(component, curation)
        for component in selectable_optics
    ]
    sanitized_cameras = [
        sanitized_camera_component(component)
        for component in selectable_cameras
    ]

    optical_product_lines = []
    for manufacturer in sorted_unique([component["manufacturer"] for component in sanitized_optics]):
        manufacturer_components = [
            component
            for component in sanitized_optics
            if component["manufacturer"] == manufacturer
        ]
        matched_lines = [
            line
            for line in product_lines_for_manufacturer(curation, manufacturer)
            if any(component.get("product_line") == line for component in manufacturer_components)
        ]
        if any(component.get("product_line") is None for component in manufacturer_components):
            matched_lines.append("Other")
        for line in matched_lines:
            optical_product_lines.append({"manufacturer": manufacturer, "productLine": line})

    return {
        "schemaVersion": 1,
        "packageFamily": SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_FAMILY,
        "packageVersion": f"astrophotography-equipment-sanitized-catalog-v1-{date_token(generated_at)}",
        "generatedAt": generated_at,
        "source": {
            "name": "AstroGuide rendered Telescope Workshop equipment catalog",
            "generatedBy": "astroguide-metadata equipment package builder",
            "sourceURL": (
                "https://github.com/tophrchris/DSOPlanneriOS/tree/main/"
                "App/Resources/Equipment/astrophotography_equipment.json"
            ),
            "curationSourceURL": (
                "https://github.com/tophrchris/DSOPlanneriOS/tree/main/"
                "App/Resources/Equipment/astrophotography_equipment_curation.json"
            ),
            "notes": (
                "Selectable Telescope Workshop projection after applying AstroGuide "
                "curation, runtime validity, and product-line display rules."
            ),
        },
        "sanitization": {
            "mirrorsAppProjection": True,
            "curationStatusGate": False,
            "rules": [
                "include_in_app defaults to included and explicitly false/0 values are excluded",
                "optics require component id, manufacturer, model, positive aperture, and positive native focal length",
                "cameras require component id, manufacturer, model, and usable sensor geometry",
                "manufacturer allowlists and excluded model phrases from astrophotography_equipment_curation.json are applied",
                "raw source values, curator notes, manufacturer_raw, curation_status, and include_in_app are omitted",
            ],
        },
        "catalog": {
            "schemaVersion": catalog.get("schemaVersion", 1),
            "generatedAt": catalog.get("generatedAt"),
            "counts": {
                "opticalComponents": len(sanitized_optics),
                "cameraComponents": len(sanitized_cameras),
                "totalComponents": len(sanitized_optics) + len(sanitized_cameras),
            },
            "opticalManufacturers": sorted_unique([component["manufacturer"] for component in sanitized_optics]),
            "cameraManufacturers": sorted_unique([component["manufacturer"] for component in sanitized_cameras]),
            "opticalProductLines": optical_product_lines,
            "opticalComponents": sanitized_optics,
            "cameraComponents": sanitized_cameras,
        },
    }


def package_descriptor(
    *,
    family: str,
    package_path: Path,
    package: dict,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict:
    if family == ASTROPHOTOGRAPHY_PACKAGE_FAMILY:
        fallback_notes = (
            "Use the bundled Telescope Workshop equipment catalog only if no validated cached package is available. "
            "Cache TTL indicates when the app should check for a fresher package; an expired cached package "
            "remains usable until replaced by a validated refresh."
        )
    elif family == SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_FAMILY:
        fallback_notes = (
            "Use the bundled Telescope Workshop projection if no validated cached sanitized package is available. "
            "This package mirrors the app-rendered selectable optics and imaging rows for review, web, and "
            "metadata consumers; an expired cached package remains usable until replaced by a validated refresh."
        )
    else:
        fallback_notes = (
            "Use the bundled equipment catalog only if no validated cached package is available. "
            "Cache TTL indicates when the app should check for a fresher package; an expired cached "
            "package remains usable until replaced by a validated refresh."
        )

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
        "fallbackNotes": fallback_notes,
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

    package_specs = []
    if args.package in {"equipment", "all"}:
        package_specs.append(
            (
                EQUIPMENT_PACKAGE_FAMILY,
                EQUIPMENT_PACKAGE_PATH,
                build_equipment_package(app_repo, generated_at),
            )
        )
    if args.package in {"astrophotography", "all"}:
        package_specs.append(
            (
                ASTROPHOTOGRAPHY_PACKAGE_FAMILY,
                ASTROPHOTOGRAPHY_PACKAGE_PATH,
                build_astrophotography_package(app_repo, generated_at),
            )
        )
    if args.package in {"astrophotography-sanitized", "all"}:
        package_specs.append(
            (
                SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_FAMILY,
                SANITIZED_ASTROPHOTOGRAPHY_PACKAGE_PATH,
                build_sanitized_astrophotography_package(app_repo, generated_at),
            )
        )
    descriptors = []
    for family, package_path, package in package_specs:
        data = write_json(REPO_ROOT / package_path, package)
        descriptors.append(
            package_descriptor(
                family=family,
                package_path=package_path,
                package=package,
                data=data,
                min_supported_app_version=args.min_supported_app_version,
                min_supported_build=args.min_supported_build,
            )
        )

    packages = [
        entry
        for entry in manifest.get("packages", [])
        if entry.get("family") not in {descriptor["family"] for descriptor in descriptors}
    ]
    packages.extend(descriptors)

    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(packages)
    write_json(manifest_path, manifest)

    for descriptor in descriptors:
        print(
            f"{descriptor['family']}: {descriptor['packageVersion']} "
            f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
