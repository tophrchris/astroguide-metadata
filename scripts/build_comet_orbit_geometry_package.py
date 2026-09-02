#!/usr/bin/env python3
"""Build hosted AstroGuide comet orbit/trajectory geometry metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
DEFAULT_SOURCE_PACKAGE = Path("App/Resources/Comets/comet_orbits.json")
DEFAULT_SEEDS = Path("App/Resources/Comets/comet_seeds.json")
DEFAULT_OUTPUT = Path("v1/packages/comet-orbit-geometry/comet_orbit_geometry_v1.json")
DEFAULT_MANIFEST = Path("v1/channels/stable/manifest.json")
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "cometOrbitGeometry"
PACKAGE_BASENAME = "comet-orbit-geometry"
ALGORITHM_VERSION = "comet-orbit-geometry-v1"

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
RENDERING_KINDS = {"closedOrbit", "trajectoryArc"}
FRAME_ALIASES = {
    "heliocentric-ecliptic-j2000-au",
    "heliocentricEclipticJ2000AU",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument(
        "--source-package",
        type=Path,
        help=(
            "Comet orbit JSON to wrap. Defaults to App/Resources/Comets/"
            "comet_orbits.json inside --app-repo."
        ),
    )
    parser.add_argument(
        "--seeds",
        type=Path,
        help=(
            "Optional comet seed bundle used to verify stable-ID coverage. Defaults to "
            "App/Resources/Comets/comet_seeds.json inside --app-repo when present."
        ),
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--min-supported-app-version", default="1.4.0")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the generated comet orbit geometry package and manifest descriptor.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = repo_path(args.output)
    manifest_path = repo_path(args.manifest)

    if args.validate_only:
        package = read_json(output_path)
        validate_package(package)
        data = output_path.read_bytes()
        if not args.skip_manifest:
            validate_manifest_descriptor(manifest_path, package, data, output_path)
        print(f"Validated {repo_relative(output_path)}")
        return 0

    app_repo = args.app_repo.resolve()
    source_package_path = (
        args.source_package.resolve()
        if args.source_package is not None
        else app_repo / DEFAULT_SOURCE_PACKAGE
    )
    seeds_path = args.seeds.resolve() if args.seeds is not None else app_repo / DEFAULT_SEEDS
    seed_bundle = read_json(seeds_path) if seeds_path.exists() else None
    source_package = read_json(source_package_path)

    generated_at = args.generated_at or utc_now()
    parse_utc_datetime(generated_at)
    package_version = args.package_version or f"{PACKAGE_BASENAME}-v1-{date_token(generated_at)}"

    package = build_package(
        source_package=source_package,
        source_package_path=source_package_path,
        seed_bundle=seed_bundle,
        seeds_path=seeds_path if seeds_path.exists() else None,
        app_repo=app_repo,
        generated_at=generated_at,
        package_version=package_version,
    )
    data = write_json(output_path, package, compact=True)
    validate_package(package)
    descriptor = descriptor_for_package(package, data, args, output_path)
    if not args.skip_manifest:
        update_manifest(manifest_path, package["generatedAt"], descriptor)
        validate_manifest_descriptor(manifest_path, package, data, output_path)

    counts = package["counts"]
    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{counts['records']} records, {descriptor['byteSize']} bytes, "
        f"{descriptor['checksum']['value']}",
        flush=True,
    )
    return 0


def build_package(
    *,
    source_package: dict[str, Any],
    source_package_path: Path,
    seed_bundle: dict[str, Any] | None,
    seeds_path: Path | None,
    app_repo: Path,
    generated_at: str,
    package_version: str,
) -> dict[str, Any]:
    validate_source_package(source_package)
    source_records = source_package.get("records") or []
    seed_records = seed_bundle.get("comets") if isinstance(seed_bundle, dict) else None
    seed_ids = stable_ids_from_seeds(seed_records)
    ordered_records = order_records(source_records, seed_ids)
    counts = validate_records(ordered_records, seed_ids=seed_ids)
    source = build_source_metadata(
        source_package,
        source_package_path=source_package_path,
        seeds_path=seeds_path,
        app_repo=app_repo,
    )

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "generatedAt": generated_at,
        "source": source,
        "coordinateFrames": {
            "heliocentric-ecliptic-j2000-au": {
                "origin": "Sun",
                "plane": "ecliptic",
                "equinox": "J2000",
                "units": "astronomicalUnits",
                "axes": ["xAU", "yAU", "zAU"],
                "notes": (
                    "Vectors are sampled from osculating SBDB elements and are intended "
                    "for planning-scale rendering, not precision navigation."
                ),
            }
        },
        "sampleSchemas": {
            "pathSamples": ["xAU", "yAU", "zAU"],
            "datedSamples": ["julianDate", "xAU", "yAU", "zAU"],
        },
        "renderingKinds": [
            {
                "id": "closedOrbit",
                "description": (
                    "Periodic, reasonably closed short-period comet orbit sampled around "
                    "one full revolution."
                ),
            },
            {
                "id": "trajectoryArc",
                "description": (
                    "Long-period, non-periodic, hyperbolic, parabolic, or otherwise poorly "
                    "closed trajectory rendered as an honest perihelion-centered arc."
                ),
            },
        ],
        "tailModel": {
            "direction": "antiSolar",
            "extent": "estimatedPlanningEnvelope",
            "notes": (
                "The package supplies a planning envelope. The app computes actual "
                "anti-solar sky orientation at display time."
            ),
        },
        "counts": counts,
        "recordCount": len(ordered_records),
        "records": ordered_records,
        "notes": [
            "This package is separate from cometSnapshot and shares the same comet stable IDs.",
            (
                "Non-periodic, long-period, hyperbolic, parabolic, and poorly closed objects "
                "must remain trajectoryArc records; clients should not render them as fake loops."
            ),
            (
                "The package is deterministic when generated from a reviewed source orbit "
                "bundle; live SBDB refreshes should be reviewed as source-data changes."
            ),
        ],
    }


def build_source_metadata(
    source_package: dict[str, Any],
    *,
    source_package_path: Path,
    seeds_path: Path | None,
    app_repo: Path,
) -> dict[str, Any]:
    source = source_package.get("source") or {}
    source_notes = [str(note) for note in source.get("notes") or [] if str(note).strip()]
    notes = [
        *source_notes,
        "Hosted package envelope generated by scripts/build_comet_orbit_geometry_package.py.",
        (
            "Orbit records were migrated from the DSOPlanneriOS bundled comet orbit geometry "
            "contract and validated against comet seed stable IDs when available."
        ),
    ]
    result = {
        "name": "NASA/JPL Small-Body Database comet orbit geometry snapshot",
        "url": source.get("url") or "https://ssd-api.jpl.nasa.gov/sbdb.api",
        "seedPath": source.get("seedPath"),
        "algorithmVersion": ALGORITHM_VERSION,
        "generatedBy": "scripts/build_comet_orbit_geometry_package.py",
        "sourceAlgorithmVersion": source.get("algorithmVersion"),
        "sourceGeneratedAt": source_package.get("generatedAt"),
        "sourcePackagePath": source_relative(source_package_path, app_repo),
        "sourcePackageSHA256": sha256_file(source_package_path),
        "notes": notes,
    }
    if seeds_path is not None:
        result["seedPath"] = source_relative(seeds_path, app_repo)
        result["seedSHA256"] = sha256_file(seeds_path)
    return prune_none(result)


def validate_source_package(package: dict[str, Any]) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Source comet orbit package schemaVersion must be 1.")
    generated_at = str(package.get("generatedAt") or "")
    parse_utc_datetime(generated_at)
    records = package.get("records")
    if not isinstance(records, list) or not records:
        raise RuntimeError("Source comet orbit package contains no records.")
    if int(package.get("recordCount") or 0) != len(records):
        raise RuntimeError("Source comet orbit package recordCount does not match records.")


def validate_package(package: dict[str, Any]) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Comet orbit geometry schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Comet orbit geometry packageFamily must be {PACKAGE_FAMILY}.")
    if not str(package.get("packageVersion") or "").strip():
        raise RuntimeError("Comet orbit geometry packageVersion is required.")
    parse_utc_datetime(str(package.get("generatedAt") or ""))
    source = package.get("source") or {}
    if source.get("algorithmVersion") != ALGORITHM_VERSION:
        raise RuntimeError("Comet orbit geometry algorithmVersion is missing or unsupported.")
    records = package.get("records")
    if not isinstance(records, list) or not records:
        raise RuntimeError("Comet orbit geometry package contains no records.")
    if int(package.get("recordCount") or 0) != len(records):
        raise RuntimeError("Comet orbit geometry recordCount does not match records.")
    counts = validate_records(records, seed_ids=None)
    if package.get("counts") != counts:
        raise RuntimeError("Comet orbit geometry counts do not match records.")
    if "coordinateFrames" not in package or "sampleSchemas" not in package:
        raise RuntimeError("Comet orbit geometry package is missing frame/sample metadata.")


def validate_records(
    records: list[dict[str, Any]],
    *,
    seed_ids: list[str] | None,
) -> dict[str, Any]:
    seen: set[str] = set()
    counts_by_kind: dict[str, int] = defaultdict(int)
    total_path_samples = 0
    total_dated_samples = 0
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise RuntimeError(f"Comet orbit record {index} must be an object.")
        stable_id = str(record.get("stableID") or "").strip()
        if not stable_id:
            raise RuntimeError(f"Comet orbit record {index} is missing stableID.")
        if stable_id in seen:
            raise RuntimeError(f"Duplicate comet orbit record stableID: {stable_id}.")
        seen.add(stable_id)
        for key in ("designation", "displayName"):
            if not str(record.get(key) or "").strip():
                raise RuntimeError(f"Comet orbit record {stable_id} is missing {key}.")
        kind = str(record.get("renderingKind") or "")
        if kind not in RENDERING_KINDS:
            raise RuntimeError(f"Comet orbit record {stable_id} has unsupported renderingKind.")
        counts_by_kind[kind] += 1
        path_frame = str(record.get("pathSampleFrame") or "")
        dated_frame = str(record.get("datedSampleFrame") or "")
        if path_frame not in FRAME_ALIASES or dated_frame not in FRAME_ALIASES:
            raise RuntimeError(f"Comet orbit record {stable_id} has unsupported sample frame.")
        path_samples = validate_vector_samples(record.get("pathSamples"), stable_id=stable_id)
        dated_samples = validate_dated_samples(record.get("datedSamples"), stable_id=stable_id)
        total_path_samples += len(path_samples)
        total_dated_samples += len(dated_samples)
        if kind == "closedOrbit" and not path_is_closed(path_samples):
            raise RuntimeError(f"Closed comet orbit record {stable_id} does not close.")
        tail_model = record.get("tailModel") or {}
        if tail_model.get("direction") != "antiSolar":
            raise RuntimeError(f"Comet orbit record {stable_id} tailModel must be antiSolar.")
    if seed_ids is not None and set(seed_ids) != seen:
        missing = sorted(set(seed_ids).difference(seen))
        extra = sorted(seen.difference(seed_ids))
        detail = []
        if missing:
            detail.append("missing " + ", ".join(missing))
        if extra:
            detail.append("extra " + ", ".join(extra))
        raise RuntimeError("Comet orbit records do not match seed stable IDs: " + "; ".join(detail))
    return {
        "records": len(records),
        "renderingKinds": dict(sorted(counts_by_kind.items())),
        "pathSamples": total_path_samples,
        "datedSamples": total_dated_samples,
    }


def validate_vector_samples(value: Any, *, stable_id: str) -> list[list[float]]:
    if not isinstance(value, list) or len(value) < 2:
        raise RuntimeError(f"Comet orbit record {stable_id} has too few pathSamples.")
    samples: list[list[float]] = []
    for sample in value:
        if not isinstance(sample, list) or len(sample) != 3:
            raise RuntimeError(f"Comet orbit record {stable_id} has invalid path sample shape.")
        parsed = [finite_float(component) for component in sample]
        if any(component is None for component in parsed):
            raise RuntimeError(f"Comet orbit record {stable_id} has non-finite path sample.")
        samples.append([float(component) for component in parsed if component is not None])
    return samples


def validate_dated_samples(value: Any, *, stable_id: str) -> list[list[float]]:
    if not isinstance(value, list) or len(value) < 2:
        raise RuntimeError(f"Comet orbit record {stable_id} has too few datedSamples.")
    samples: list[list[float]] = []
    previous_jd = -math.inf
    for sample in value:
        if not isinstance(sample, list) or len(sample) != 4:
            raise RuntimeError(f"Comet orbit record {stable_id} has invalid dated sample shape.")
        parsed = [finite_float(component) for component in sample]
        if any(component is None for component in parsed):
            raise RuntimeError(f"Comet orbit record {stable_id} has non-finite dated sample.")
        resolved = [float(component) for component in parsed if component is not None]
        if resolved[0] <= previous_jd:
            raise RuntimeError(f"Comet orbit record {stable_id} datedSamples are not sorted.")
        previous_jd = resolved[0]
        samples.append(resolved)
    return samples


def path_is_closed(samples: list[list[float]]) -> bool:
    first = samples[0]
    last = samples[-1]
    return all(abs(first[index] - last[index]) <= 0.0002 for index in range(3))


def stable_ids_from_seeds(seed_records: Any) -> list[str] | None:
    if not isinstance(seed_records, list) or not seed_records:
        return None
    stable_ids: list[str] = []
    for seed in seed_records:
        if not isinstance(seed, dict):
            continue
        stable_id = str(seed.get("stableID") or "").strip()
        if stable_id:
            stable_ids.append(stable_id)
    return stable_ids or None


def order_records(
    records: list[dict[str, Any]],
    seed_ids: list[str] | None,
) -> list[dict[str, Any]]:
    by_id = {str(record.get("stableID") or ""): record for record in records if isinstance(record, dict)}
    if seed_ids:
        return [by_id[stable_id] for stable_id in seed_ids if stable_id in by_id]
    return sorted(records, key=lambda record: str(record.get("stableID") or ""))


def rendering_kind(seed: dict[str, Any], elements: dict[str, float]) -> str:
    eccentricity = elements.get("e")
    period_days = elements.get("per")
    orbit_class = str(seed.get("orbitClass") or "").lower()
    if (
        eccentricity is not None
        and eccentricity < 0.98
        and period_days is not None
        and period_days < 200.0 * 365.25
        and "periodic" in orbit_class
        and "non-periodic" not in orbit_class
    ):
        return "closedOrbit"
    return "trajectoryArc"


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
        "minSupportedAppVersion": args.min_supported_app_version,
        "minSupportedBuild": args.min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Clients that support this family should retain bundled comet orbit geometry "
            "or hide orbit-rendering affordances when no compatible package is available."
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
        raise RuntimeError(f"Expected one manifest descriptor for {PACKAGE_FAMILY}.")
    entry = matches[0]
    if entry.get("packageVersion") != package.get("packageVersion"):
        raise RuntimeError("Manifest packageVersion does not match comet orbit geometry package.")
    if entry.get("payloadSchemaVersion") != package.get("schemaVersion"):
        raise RuntimeError("Manifest payloadSchemaVersion does not match comet orbit geometry package.")
    expected_url = f"{METADATA_ORIGIN}/{repo_relative_path(output_path).as_posix()}"
    if entry.get("packageURL") != expected_url:
        raise RuntimeError("Manifest packageURL does not reference comet orbit geometry package.")
    if int(entry.get("byteSize") or 0) != len(data):
        raise RuntimeError("Manifest byteSize does not match comet orbit geometry package.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != hashlib.sha256(data).hexdigest():
        raise RuntimeError("Manifest checksum does not match comet orbit geometry package.")


def descriptor_key(entry: dict[str, Any]) -> tuple[str, str]:
    family = str(entry.get("family") or "")
    if family == "seasonalRecommendationCandidates":
        return family, str(entry.get("latitudeBand") or "")
    return family, ""


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {band: index for index, band in enumerate(LATITUDE_BAND_ORDER)}

    def key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
        family = str(entry.get("family") or "")
        return (
            family_order.get(family, len(family_order)),
            band_order.get(str(entry.get("latitudeBand") or ""), 99),
            family,
            str(entry.get("packageVersion") or ""),
        )

    return sorted(packages, key=key)


def parse_utc_datetime(value: str) -> dt.datetime:
    raw = value.strip()
    if not raw:
        raise RuntimeError("Date values cannot be empty.")
    normalized = raw.replace("Z", "+00:00")
    parsed = dt.datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.UTC)
    return parsed.astimezone(dt.UTC)


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(timestamp: str) -> str:
    return timestamp.split("T", maxsplit=1)[0].replace("-", "")


def finite_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def prune_none(value: dict[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if item is not None}


def source_relative(path: Path, app_repo: Path) -> str:
    try:
        return str(path.resolve().relative_to(app_repo.resolve()))
    except ValueError:
        return repo_relative(path)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def identifier_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-") or "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
