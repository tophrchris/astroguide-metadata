#!/usr/bin/env python3
"""Build AstroGuide hosted major-planet/catalog-target close encounters."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_lunar_event_package as lunar  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
DEFAULT_CATALOG_PATH = Path("App/Resources/Catalog/catalog.sqlite")
DEFAULT_PACKAGE_PATH = Path(
    "v1/packages/planet-target-close-encounters/"
    "planet_target_close_encounter_metadata_v1.json"
)
DEFAULT_EPHEMERIS_CACHE = Path.home() / "Library/Caches/com.tophrchris.AstroGuide/lunar-events"
DEFAULT_EPHEMERIS = "de421.bsp"
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "planetTargetCloseEncounters"
PACKAGE_BASENAME = "planet-target-close-encounters"
EVENT_FAMILY = "closeEncounter"
EVENT_TYPE = "planetTargetCloseEncounter"
ALGORITHM_VERSION = "planet-target-close-encounters-v1"
DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT = lunar.DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT
FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "darkSkyPlaces",
    "cometSnapshot",
    "planetCatalog",
    "lunarEvents",
    "fullMoonNameAliases",
    PACKAGE_FAMILY,
    "seasonalRecommendationCandidates",
    "transientEventFeed",
]


@dataclass(frozen=True)
class ShardBuild:
    path: Path
    payload: dict[str, Any]
    data: bytes
    descriptor: dict[str, Any]


def parse_args() -> argparse.Namespace:
    today = dt.datetime.now(dt.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    default_end = add_years(today, 2)
    parser = argparse.ArgumentParser(
        description=(
            "Build the hosted AstroGuide major-planet/catalog-target close-encounter "
            "package and refresh the stable manifest."
        )
    )
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument(
        "--catalog",
        type=Path,
        help=(
            "Catalog SQLite path. Defaults to App/Resources/Catalog/catalog.sqlite "
            "inside --app-repo."
        ),
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_PACKAGE_PATH)
    parser.add_argument("--manifest", type=Path, default=Path("v1/channels/stable/manifest.json"))
    parser.add_argument(
        "--seasonal-recommendation-dir",
        type=Path,
        default=lunar.DEFAULT_SEASONAL_RECOMMENDATION_DIR,
    )
    parser.add_argument(
        "--target-metadata",
        type=Path,
        default=lunar.DEFAULT_TARGET_METADATA_PATH,
    )
    parser.add_argument(
        "--target-neighborhoods",
        type=Path,
        default=lunar.DEFAULT_TARGET_NEIGHBORHOOD_PATH,
    )
    parser.add_argument("--start-date", default=lunar.isoformat_z(today))
    parser.add_argument("--end-date", default=lunar.isoformat_z(default_end))
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--min-supported-app-version", default="1.4.0")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--max-separation-degrees", type=float, default=5.0)
    parser.add_argument(
        "--bright-ngc-ic-mag-limit",
        type=float,
        default=DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT,
    )
    parser.add_argument("--sample-step-minutes", type=int, default=60)
    parser.add_argument("--refine-step-minutes", type=int, default=5)
    parser.add_argument("--scan-padding-hours", type=int, default=72)
    parser.add_argument("--dedupe-coordinate-arcmin", type=float, default=6.0)
    parser.add_argument("--ephemeris-cache", type=Path, default=DEFAULT_EPHEMERIS_CACHE)
    parser.add_argument("--ephemeris", default=DEFAULT_EPHEMERIS)
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate an existing package, its monthly shards, and manifest chain.",
    )
    args = parser.parse_args()
    if args.max_separation_degrees <= 0:
        raise SystemExit("--max-separation-degrees must be positive")
    if args.bright_ngc_ic_mag_limit <= 0:
        raise SystemExit("--bright-ngc-ic-mag-limit must be positive")
    if args.sample_step_minutes <= 0:
        raise SystemExit("--sample-step-minutes must be positive")
    if args.refine_step_minutes <= 0:
        raise SystemExit("--refine-step-minutes must be positive")
    if args.refine_step_minutes > args.sample_step_minutes:
        raise SystemExit("--refine-step-minutes cannot exceed --sample-step-minutes")
    if args.scan_padding_hours < 0:
        raise SystemExit("--scan-padding-hours cannot be negative")
    if args.dedupe_coordinate_arcmin < 0:
        raise SystemExit("--dedupe-coordinate-arcmin cannot be negative")
    return args


def main() -> int:
    args = parse_args()
    output_path = repo_path(args.output)
    manifest_path = repo_path(args.manifest)

    if args.validate_only:
        package = read_json(output_path)
        validate_package(package, output_path)
        if not args.skip_manifest:
            validate_manifest_descriptor(manifest_path, package, output_path.read_bytes(), output_path)
        print(f"Validated {repo_relative(output_path)}")
        return 0

    start = lunar.parse_utc_datetime(args.start_date)
    end = lunar.parse_utc_datetime(args.end_date)
    if end <= start:
        raise SystemExit("--end-date must be after --start-date")

    app_repo = args.app_repo.resolve()
    catalog_path = (args.catalog.resolve() if args.catalog else app_repo / DEFAULT_CATALOG_PATH).resolve()
    generated_at = args.generated_at or lunar.utc_now()
    lunar.parse_utc_datetime(generated_at)
    package_version = args.package_version or f"{PACKAGE_BASENAME}-v1-{lunar.date_token(generated_at)}"

    sky = lunar.load_skyfield_modules()
    targets = lunar.load_targets(catalog_path)
    if not targets:
        raise SystemExit(f"No catalog targets with coordinates found in {catalog_path}")
    all_target_groups = lunar.build_target_groups(targets, args.dedupe_coordinate_arcmin)
    identity_context = lunar.build_target_identity_context(
        all_target_groups,
        args.dedupe_coordinate_arcmin,
    )
    curated_references = [
        *lunar.load_curated_recommendation_references(
            repo_path(args.seasonal_recommendation_dir)
        ),
        *lunar.load_target_metadata_references(repo_path(args.target_metadata)),
    ]
    named_showcase_references = lunar.load_target_neighborhood_references(
        repo_path(args.target_neighborhoods)
    )
    lunar.populate_common_name_owners(identity_context, curated_references)
    target_groups, selection_reasons = lunar.select_dso_target_groups(
        all_target_groups,
        identity_context=identity_context,
        curated_references=curated_references,
        named_showcase_references=named_showcase_references,
        bright_ngc_ic_mag_limit=args.bright_ngc_ic_mag_limit,
    )
    print(
        f"Loaded {len(targets)} coordinate targets, grouped into "
        f"{len(all_target_groups)} canonical target groups.",
        flush=True,
    )
    print(
        f"Selected {len(target_groups)} presentation DSO target groups "
        f"({lunar.selection_reason_summary(selection_reasons)}).",
        flush=True,
    )

    planet_subjects = [
        lunar.PlanetSubject(
            planet_id=planet_id,
            display_name=display_name,
            ephemeris_key=ephemeris_key,
        )
        for planet_id, display_name, ephemeris_key in lunar.PLANET_SUBJECTS
    ]
    load = sky.Loader(str(args.ephemeris_cache.resolve()))
    eph = load(args.ephemeris)
    ts = load.timescale()
    earth = eph["earth"]

    scan_padding = dt.timedelta(hours=args.scan_padding_hours)
    scan_start = start - scan_padding
    scan_end = end + scan_padding
    sample_times = lunar.date_grid(
        scan_start,
        scan_end,
        dt.timedelta(minutes=args.sample_step_minutes),
    )
    print(
        f"Scanning {len(sample_times)} coarse geocentric samples from "
        f"{lunar.isoformat_z(scan_start)} to {lunar.isoformat_z(scan_end)}.",
        flush=True,
    )

    events, event_target_group_ids = compute_close_encounters(
        sky=sky,
        planet_subjects=planet_subjects,
        target_groups=target_groups,
        identity_context=identity_context,
        sample_times=sample_times,
        start=start,
        end=end,
        max_separation_degrees=args.max_separation_degrees,
        refine_step=dt.timedelta(minutes=args.refine_step_minutes),
        earth=earth,
        eph=eph,
        ts=ts,
    )
    events = sorted(events, key=lambda event: (str(event["eventTimeUTC"]), str(event["id"])))
    event_target_groups = [
        group for group in target_groups if group.group_id in event_target_group_ids
    ]
    catalog_metadata = lunar.load_catalog_metadata(catalog_path)
    clean_shard_directory(output_path)
    shard_builds = build_shards(
        events=events,
        package_version=package_version,
        generated_at=generated_at,
        package_start=start,
        package_end=end,
        index_path=output_path,
    )
    package = build_package(
        package_version=package_version,
        generated_at=generated_at,
        start=start,
        end=end,
        catalog_path=catalog_path,
        app_repo=app_repo,
        catalog_metadata=catalog_metadata,
        source_target_group_count=len(all_target_groups),
        candidate_target_groups=target_groups,
        event_target_groups=event_target_groups,
        identity_context=identity_context,
        selection_reasons=selection_reasons,
        planet_subjects=planet_subjects,
        events=events,
        shard_descriptors=[shard.descriptor for shard in shard_builds],
        shard_event_rows=sum(int(shard.descriptor["eventCount"]) for shard in shard_builds),
        args=args,
        sky_versions=sky.versions,
        ephemeris=eph,
    )
    for shard in shard_builds:
        shard.path.parent.mkdir(parents=True, exist_ok=True)
        shard.path.write_bytes(shard.data)
    data = write_json(output_path, package, compact=True)
    validate_package(package, output_path)
    descriptor = descriptor_for_package(package, data, args, output_path)
    if not args.skip_manifest:
        update_manifest(manifest_path, package["generatedAt"], descriptor)
        validate_manifest_descriptor(manifest_path, package, data, output_path)

    counts = package["counts"]
    total_bytes = len(data) + sum(len(shard.data) for shard in shard_builds)
    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{counts['events']} events across {counts['shards']} shards, "
        f"{total_bytes} total bytes.",
        flush=True,
    )
    print(f"Events by planet: {counts['eventsByPlanet']}", flush=True)
    return 0


def compute_close_encounters(
    *,
    sky: lunar.SkyfieldModules,
    planet_subjects: list[lunar.PlanetSubject],
    target_groups: list[lunar.TargetGroup],
    identity_context: lunar.TargetIdentityContext,
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    earth: Any,
    eph: Any,
    ts: Any,
) -> tuple[list[dict[str, Any]], set[str]]:
    events_by_id: dict[str, dict[str, Any]] = {}
    event_target_group_ids: set[str] = set()

    for planet in planet_subjects:
        body = eph[planet.ephemeris_key]
        planet_ra, planet_dec = lunar.apparent_radec_arrays(
            sky,
            earth,
            body,
            ts,
            sample_times,
        )
        candidate_count = 0
        for target_group in target_groups:
            target = target_group.canonical
            separations = separation_from_fixed_target(
                sky,
                target,
                planet_ra,
                planet_dec,
            )
            for minimum_index in local_minimum_indices(
                sky,
                separations,
                max_separation_degrees,
            ):
                event = refine_close_encounter(
                    sky=sky,
                    planet=planet,
                    planet_body=body,
                    target_group=target_group,
                    identity_context=identity_context,
                    minimum_index=minimum_index,
                    sample_times=sample_times,
                    start=start,
                    end=end,
                    max_separation_degrees=max_separation_degrees,
                    refine_step=refine_step,
                    earth=earth,
                    ts=ts,
                )
                if event is None:
                    continue
                candidate_count += 1
                event_id = str(event["id"])
                previous = events_by_id.get(event_id)
                if previous is None or float(event["minimumSeparationDegrees"]) < float(
                    previous["minimumSeparationDegrees"]
                ):
                    events_by_id[event_id] = event
                event_target_group_ids.add(target_group.group_id)
        print(
            f"{planet.display_name}: refined {candidate_count} close encounters.",
            flush=True,
        )

    return list(events_by_id.values()), event_target_group_ids


def separation_from_fixed_target(
    sky: lunar.SkyfieldModules,
    target: lunar.TargetRecord,
    body_ra: Any,
    body_dec: Any,
) -> Any:
    target_ra = math.radians(target.ra_degrees)
    target_dec = math.radians(target.dec_degrees)
    cosines = (
        math.sin(target_dec) * sky.np.sin(body_dec)
        + math.cos(target_dec)
        * sky.np.cos(body_dec)
        * sky.np.cos(target_ra - body_ra)
    )
    return sky.np.degrees(sky.np.arccos(sky.np.clip(cosines, -1.0, 1.0)))


def local_minimum_indices(
    sky: lunar.SkyfieldModules,
    values: Any,
    threshold: float,
) -> list[int]:
    if len(values) < 3:
        return []
    middle = values[1:-1]
    mask = (
        (middle <= threshold)
        & (middle <= values[:-2])
        & (middle < values[2:])
    )
    return (sky.np.flatnonzero(mask) + 1).tolist()


def refine_close_encounter(
    *,
    sky: lunar.SkyfieldModules,
    planet: lunar.PlanetSubject,
    planet_body: Any,
    target_group: lunar.TargetGroup,
    identity_context: lunar.TargetIdentityContext,
    minimum_index: int,
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    earth: Any,
    ts: Any,
) -> dict[str, Any] | None:
    bracket_start = sample_times[minimum_index - 1]
    bracket_end = sample_times[minimum_index + 1]
    fine_times = lunar.date_grid(bracket_start, bracket_end, refine_step)
    body_ra, body_dec = lunar.apparent_radec_arrays(
        sky,
        earth,
        planet_body,
        ts,
        fine_times,
    )
    separations = separation_from_fixed_target(
        sky,
        target_group.canonical,
        body_ra,
        body_dec,
    )
    fine_minimum_index = int(sky.np.argmin(separations))
    closest_time = lunar.refined_minimum_time(
        fine_times,
        separations,
        fine_minimum_index,
        refine_step,
    )
    closest_separation = scalar_target_planet_separation(
        sky,
        target_group.canonical,
        planet_body,
        closest_time,
        earth,
        ts,
    )
    if closest_time < start or closest_time >= end:
        return None
    if closest_separation > max_separation_degrees + 0.000_001:
        return None

    planet_snapshot = lunar.planet_snapshot(
        sky,
        planet,
        planet_body,
        closest_time,
        earth,
        ts,
    )
    participants = [
        planet_participant(planet_snapshot),
        target_participant(target_group, identity_context),
    ]
    return {
        "id": event_identifier(planet.planet_id, target_group.group_id, closest_time),
        "eventFamily": EVENT_FAMILY,
        "type": EVENT_TYPE,
        "eventTimeUTC": lunar.isoformat_z(closest_time),
        "closestApproachUTC": lunar.isoformat_z(closest_time),
        "minimumSeparationDegrees": round(closest_separation, 4),
        "participants": participants,
    }


def scalar_target_planet_separation(
    sky: lunar.SkyfieldModules,
    target: lunar.TargetRecord,
    planet_body: Any,
    timestamp: dt.datetime,
    earth: Any,
    ts: Any,
) -> float:
    body_ra, body_dec = lunar.apparent_radec_arrays(
        sky,
        earth,
        planet_body,
        ts,
        [timestamp],
    )
    return float(separation_from_fixed_target(sky, target, body_ra, body_dec)[0])


def planet_participant(snapshot: dict[str, Any]) -> dict[str, Any]:
    return lunar.prune_none(
        {
            "kind": "majorPlanet",
            "id": snapshot.get("id"),
            "displayName": snapshot.get("displayName"),
            "magnitude": snapshot.get("visualMagnitude"),
            "distanceAU": snapshot.get("distanceAU"),
        }
    )


def target_participant(
    group: lunar.TargetGroup,
    identity_context: lunar.TargetIdentityContext,
) -> dict[str, Any]:
    canonical = group.canonical
    return lunar.prune_none(
        {
            "kind": "deepSkyObject",
            "id": group.group_id,
            "catalogID": canonical.object_id,
            "displayName": lunar.target_group_display_name(group, identity_context),
            "catalogName": canonical.catalog_name,
            "objectType": canonical.object_type or "Unknown",
            "magnitude": lunar.round_optional(canonical.magnitude, 2),
        }
    )


def event_identifier(planet_id: str, target_id: str, timestamp: dt.datetime) -> str:
    planet_component = identifier_component(planet_id)
    target_component = identifier_component(target_id)
    return (
        f"planet-target-close-encounter-{planet_component}-{target_component}-"
        f"{timestamp:%Y%m%d}"
    )


def identifier_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-") or "unknown"


def build_shards(
    *,
    events: list[dict[str, Any]],
    package_version: str,
    generated_at: str,
    package_start: dt.datetime,
    package_end: dt.datetime,
    index_path: Path,
) -> list[ShardBuild]:
    shards: list[ShardBuild] = []
    for shard_start, shard_end in lunar.month_windows(package_start, package_end):
        shard_events = [
            event
            for event in events
            if shard_start
            <= lunar.parse_utc_datetime(str(event["eventTimeUTC"]))
            < shard_end
        ]
        if not shard_events:
            continue
        shard_id = shard_start.strftime("%Y-%m")
        shard_path = (
            index_path.parent
            / "shards"
            / f"planet_target_close_encounters_{shard_start:%Y_%m}_v1.json"
        )
        payload = build_shard_payload(
            shard_id=shard_id,
            package_version=package_version,
            generated_at=generated_at,
            shard_start=shard_start,
            shard_end=shard_end,
            events=sorted(
                shard_events,
                key=lambda event: (str(event["eventTimeUTC"]), str(event["id"])),
            ),
        )
        data = json_bytes(payload, compact=True)
        counts = event_counts(payload["events"])
        descriptor = {
            "id": shard_id,
            "kind": "month",
            "startUTC": lunar.isoformat_z(shard_start),
            "endUTC": lunar.isoformat_z(shard_end),
            "url": f"{METADATA_ORIGIN}/{repo_relative_path(shard_path).as_posix()}",
            "path": repo_relative(shard_path),
            "checksum": {
                "algorithm": "sha256",
                "value": hashlib.sha256(data).hexdigest(),
            },
            "byteSize": len(data),
            "eventCount": len(payload["events"]),
            "uniqueEventCount": len({str(event["id"]) for event in payload["events"]}),
            "counts": counts,
        }
        shards.append(
            ShardBuild(
                path=shard_path,
                payload=payload,
                data=data,
                descriptor=descriptor,
            )
        )
    return shards


def build_shard_payload(
    *,
    shard_id: str,
    package_version: str,
    generated_at: str,
    shard_start: dt.datetime,
    shard_end: dt.datetime,
    events: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "packageRole": "shard",
        "shardID": shard_id,
        "shardKind": "month",
        "generatedAt": generated_at,
        "window": {
            "startUTC": lunar.isoformat_z(shard_start),
            "endUTC": lunar.isoformat_z(shard_end),
        },
        "counts": event_counts(events),
        "events": events,
    }


def build_package(
    *,
    package_version: str,
    generated_at: str,
    start: dt.datetime,
    end: dt.datetime,
    catalog_path: Path,
    app_repo: Path,
    catalog_metadata: dict[str, str],
    source_target_group_count: int,
    candidate_target_groups: list[lunar.TargetGroup],
    event_target_groups: list[lunar.TargetGroup],
    identity_context: lunar.TargetIdentityContext,
    selection_reasons: dict[str, list[str]],
    planet_subjects: list[lunar.PlanetSubject],
    events: list[dict[str, Any]],
    shard_descriptors: list[dict[str, Any]],
    shard_event_rows: int,
    args: argparse.Namespace,
    sky_versions: dict[str, str],
    ephemeris: Any,
) -> dict[str, Any]:
    counts = event_counts(events)
    selection_counts: dict[str, int] = defaultdict(int)
    for reasons in selection_reasons.values():
        for reason in reasons:
            selection_counts[reason] += 1

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "packageRole": "index",
        "generatedAt": generated_at,
        "eventFamilies": [EVENT_FAMILY],
        "eventTypes": [EVENT_TYPE],
        "window": {
            "startUTC": lunar.isoformat_z(start),
            "endUTC": lunar.isoformat_z(end),
            "durationDays": round((end - start).total_seconds() / 86400.0, 3),
        },
        "source": {
            "name": "AstroGuide planet/catalog-target close-encounter pipeline",
            "generatedBy": "scripts/build_planet_target_close_encounter_package.py",
            "algorithmVersion": ALGORITHM_VERSION,
            "catalogSourceRepo": "tophrchris/DSOPlanneriOS",
            "catalogPath": lunar.source_relative(catalog_path, app_repo),
            "catalogVersion": catalog_metadata.get("catalog_version"),
            "catalogFingerprint": catalog_metadata.get("catalog_fingerprint"),
            "catalogSHA256": lunar.sha256_file(catalog_path),
            "targetMetadataPath": repo_relative(repo_path(args.target_metadata)),
            "targetNeighborhoodPath": repo_relative(repo_path(args.target_neighborhoods)),
            "seasonalRecommendationDirectory": repo_relative(
                repo_path(args.seasonal_recommendation_dir)
            ),
            "ephemeris": args.ephemeris,
            "ephemerisPath": str(getattr(ephemeris, "filename", args.ephemeris)),
            "ephemerisSource": "JPL Development Ephemeris loaded through Skyfield",
            "planetFrame": (
                "Geocentric apparent equatorial RA/Dec from "
                "Skyfield earth.at(t).observe(body).apparent()."
            ),
            "targetFrame": "Catalog J2000 equatorial RA/Dec held fixed during the scan.",
            "timescale": "UTC",
            "closestApproachAlgorithm": (
                "Detect local angular-separation minima on the coarse time grid, "
                "refine each bracket on the fine grid, then apply quadratic time interpolation."
            ),
            "eventIDAlgorithm": (
                "Stable planet ID plus canonical target-group ID plus UTC closest-approach date."
            ),
            "planetMagnitudeModel": "Skyfield magnitudelib planetary_magnitude where finite.",
            "versions": sky_versions,
        },
        "parameters": {
            "maxSeparationDegrees": args.max_separation_degrees,
            "dsoCandidateFilter": {
                "curatedRecommendationUnion": (
                    "seasonal recommendation priorityTier=1 plus target metadata overlay"
                ),
                "includeMessier": True,
                "brightNGCICMagnitudeLimit": args.bright_ngc_ic_mag_limit,
                "includeNamedShowcaseTargets": "target neighborhood catalog IDs",
                "excludeUnknownMagnitudeBackCatalogTargets": True,
            },
            "sampleStepMinutes": args.sample_step_minutes,
            "refineStepMinutes": args.refine_step_minutes,
            "scanPaddingHours": args.scan_padding_hours,
            "dedupeCoordinateArcmin": args.dedupe_coordinate_arcmin,
            "identityResolution": {
                "coordinateToleranceArcmin": identity_context.coordinate_tolerance_arcmin,
                "catalogPreferenceOrder": [
                    "Messier",
                    "NGC",
                    "IC",
                    "Caldwell",
                    "supportedCatalogs",
                ],
                "quarantinedCommonNameTokens": len(
                    identity_context.ambiguous_common_tokens
                ),
                "quarantinedAliasTokens": len(identity_context.ambiguous_exact_tokens),
            },
            "planetSubjects": [planet.planet_id for planet in planet_subjects],
        },
        "counts": {
            "sourceTargetGroups": source_target_group_count,
            "candidateTargetGroups": len(candidate_target_groups),
            "eventTargetGroups": len(event_target_groups),
            "candidateSelectionReasons": dict(sorted(selection_counts.items())),
            "events": counts["events"],
            "eventsByPlanet": counts["eventsByPlanet"],
            "shardEventRows": shard_event_rows,
            "shards": len(shard_descriptors),
        },
        "subjects": {
            "majorPlanets": [
                {
                    "id": planet.planet_id,
                    "displayName": planet.display_name,
                    "ephemerisKey": planet.ephemeris_key,
                }
                for planet in planet_subjects
            ],
            "targetGroups": [
                lunar.target_group_payload(
                    group,
                    identity_context,
                    sorted(selection_reasons.get(group.group_id, [])),
                )
                for group in event_target_groups
            ],
        },
        "payloadFormat": {
            "index": "compact-json",
            "shards": "compact-json",
            "shardStrategy": "monthly",
            "participantModel": (
                "Ordered generic participants: major planet first, deep-sky target second."
            ),
        },
        "shards": shard_descriptors,
        "notes": [
            (
                "Events are global/geocentric baselines. App-side filtering is responsible "
                "for active site, nighttime, altitude, horizon/obstructions, and observability."
            ),
            (
                "The presentation-focused DSO candidate filter matches the lunar-events "
                "pipeline to keep package size and low-value back-catalog matches under control."
            ),
            (
                "Window and duration fields are intentionally omitted in v1 because slow outer "
                "planets can remain within five degrees through multiple local minima; the "
                "closest-approach instant is deterministic and unambiguous."
            ),
            "Comets and meteor showers are intentionally out of scope for this package family.",
            (
                "The stable manifest points at this index; the index references checksummed "
                "monthly shards."
            ),
        ],
    }


def event_counts(events: list[dict[str, Any]]) -> dict[str, Any]:
    by_planet: dict[str, int] = defaultdict(int)
    for event in events:
        planet, _ = event_participants(event)
        if planet:
            by_planet[str(planet.get("id") or "unknown")] += 1
    return {
        "events": len(events),
        "eventsByPlanet": dict(sorted(by_planet.items())),
    }


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
            "Clients that support this family should retain a bundled or cached validated "
            "snapshot and degrade gracefully when no compatible package is available."
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


def descriptor_key(entry: dict[str, Any]) -> tuple[str, str]:
    family = str(entry.get("family") or "")
    if family == "seasonalRecommendationCandidates":
        return family, str(entry.get("latitudeBand") or "")
    return family, ""


def sort_packages(packages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {
        band: index for index, band in enumerate(lunar.LATITUDE_BAND_ORDER)
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


def validate_package(package: dict[str, Any], index_path: Path) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Planet/target close-encounter index schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Package family must be {PACKAGE_FAMILY}.")
    if not package.get("packageVersion"):
        raise RuntimeError("Package is missing packageVersion.")
    if package.get("packageRole") != "index":
        raise RuntimeError("Package must have the index role.")
    lunar.parse_utc_datetime(str(package.get("generatedAt") or ""))
    source = package.get("source") or {}
    if source.get("algorithmVersion") != ALGORITHM_VERSION:
        raise RuntimeError("Package algorithmVersion is missing or unsupported.")

    window = package.get("window") or {}
    package_start = lunar.parse_utc_datetime(str(window.get("startUTC") or ""))
    package_end = lunar.parse_utc_datetime(str(window.get("endUTC") or ""))
    if package_end <= package_start:
        raise RuntimeError("Package window must be non-empty.")
    threshold = lunar.finite_float(
        (package.get("parameters") or {}).get("maxSeparationDegrees")
    )
    if threshold is None or threshold <= 0:
        raise RuntimeError("Package maxSeparationDegrees must be positive.")

    subjects = package.get("subjects") or {}
    planet_ids = {
        str(row.get("id") or "")
        for row in subjects.get("majorPlanets") or []
        if isinstance(row, dict)
    }
    target_groups = {
        str(row.get("id") or ""): row
        for row in subjects.get("targetGroups") or []
        if isinstance(row, dict)
    }
    if planet_ids != {planet_id for planet_id, _, _ in lunar.PLANET_SUBJECTS}:
        raise RuntimeError("Index majorPlanets does not match the supported seven planets.")

    shards = package.get("shards")
    if not isinstance(shards, list) or not shards:
        raise RuntimeError("Package index contains no monthly shards.")
    descriptor_ids: set[str] = set()
    unique_events: dict[str, dict[str, Any]] = {}
    shard_event_rows = 0
    for descriptor in shards:
        validate_shard_descriptor(descriptor)
        descriptor_id = str(descriptor["id"])
        if descriptor_id in descriptor_ids:
            raise RuntimeError(f"Duplicate shard descriptor: {descriptor_id}.")
        descriptor_ids.add(descriptor_id)
        shard_path = shard_path_from_descriptor(descriptor)
        data = shard_path.read_bytes()
        if len(data) != int(descriptor["byteSize"]):
            raise RuntimeError(f"Shard byteSize mismatch for {descriptor_id}.")
        checksum = descriptor.get("checksum") or {}
        if checksum.get("algorithm") != "sha256":
            raise RuntimeError(f"Shard checksum algorithm must be sha256 for {descriptor_id}.")
        if hashlib.sha256(data).hexdigest() != checksum.get("value"):
            raise RuntimeError(f"Shard checksum mismatch for {descriptor_id}.")
        payload = json.loads(data)
        counts = validate_shard_payload(
            payload,
            descriptor,
            package,
            threshold=threshold,
            package_start=package_start,
            package_end=package_end,
            planet_ids=planet_ids,
            target_groups=target_groups,
        )
        shard_event_rows += counts["events"]
        for event in payload["events"]:
            event_id = str(event["id"])
            if event_id in unique_events:
                raise RuntimeError(f"Event ID appears in multiple shards: {event_id}.")
            unique_events[event_id] = event

    counts = event_counts(list(unique_events.values()))
    package_counts = package.get("counts") or {}
    if counts["events"] != int(package_counts.get("events") or 0):
        raise RuntimeError("Index event count does not match shards.")
    if counts["eventsByPlanet"] != package_counts.get("eventsByPlanet"):
        raise RuntimeError("Index eventsByPlanet does not match shards.")
    if shard_event_rows != int(package_counts.get("shardEventRows") or 0):
        raise RuntimeError("Index shardEventRows does not match shards.")
    if len(shards) != int(package_counts.get("shards") or 0):
        raise RuntimeError("Index shard count does not match descriptors.")


def validate_shard_descriptor(descriptor: dict[str, Any]) -> None:
    required = {
        "id",
        "kind",
        "startUTC",
        "endUTC",
        "url",
        "path",
        "checksum",
        "byteSize",
        "eventCount",
        "uniqueEventCount",
        "counts",
    }
    missing = sorted(required.difference(descriptor))
    if missing:
        raise RuntimeError(f"Shard descriptor is missing {', '.join(missing)}.")
    if descriptor.get("kind") != "month":
        raise RuntimeError(f"Shard {descriptor.get('id')} must use monthly sharding.")
    start = lunar.parse_utc_datetime(str(descriptor["startUTC"]))
    end = lunar.parse_utc_datetime(str(descriptor["endUTC"]))
    if end <= start:
        raise RuntimeError(f"Shard {descriptor.get('id')} has an invalid window.")
    if int(descriptor["eventCount"]) != int(descriptor["uniqueEventCount"]):
        raise RuntimeError(f"Shard {descriptor.get('id')} event IDs are not unique.")


def validate_shard_payload(
    payload: dict[str, Any],
    descriptor: dict[str, Any],
    index_package: dict[str, Any],
    *,
    threshold: float,
    package_start: dt.datetime,
    package_end: dt.datetime,
    planet_ids: set[str],
    target_groups: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    shard_id = str(descriptor["id"])
    if payload.get("schemaVersion") != 1:
        raise RuntimeError(f"Shard {shard_id} schemaVersion must be 1.")
    if payload.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Shard {shard_id} family mismatch.")
    if payload.get("packageVersion") != index_package.get("packageVersion"):
        raise RuntimeError(f"Shard {shard_id} packageVersion mismatch.")
    if payload.get("packageRole") != "shard":
        raise RuntimeError(f"Shard {shard_id} packageRole must be shard.")
    if payload.get("shardID") != shard_id:
        raise RuntimeError(f"Shard {shard_id} shardID mismatch.")
    window = payload.get("window") or {}
    shard_start = lunar.parse_utc_datetime(str(window.get("startUTC") or ""))
    shard_end = lunar.parse_utc_datetime(str(window.get("endUTC") or ""))
    if lunar.isoformat_z(shard_start) != descriptor["startUTC"]:
        raise RuntimeError(f"Shard {shard_id} startUTC mismatch.")
    if lunar.isoformat_z(shard_end) != descriptor["endUTC"]:
        raise RuntimeError(f"Shard {shard_id} endUTC mismatch.")
    events = payload.get("events")
    if not isinstance(events, list) or not events:
        raise RuntimeError(f"Shard {shard_id} contains no events.")
    counts = validate_events(
        events,
        threshold=threshold,
        package_start=package_start,
        package_end=package_end,
        shard_start=shard_start,
        shard_end=shard_end,
        planet_ids=planet_ids,
        target_groups=target_groups,
    )
    if counts["events"] != int(descriptor["eventCount"]):
        raise RuntimeError(f"Shard {shard_id} eventCount mismatch.")
    if counts != descriptor.get("counts") or counts != payload.get("counts"):
        raise RuntimeError(f"Shard {shard_id} counts mismatch.")
    return counts


def validate_events(
    events: list[dict[str, Any]],
    *,
    threshold: float,
    package_start: dt.datetime,
    package_end: dt.datetime,
    shard_start: dt.datetime,
    shard_end: dt.datetime,
    planet_ids: set[str],
    target_groups: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    previous_key = ("", "")
    seen_ids: set[str] = set()
    for event in events:
        if not isinstance(event, dict):
            raise RuntimeError("Close-encounter event rows must be objects.")
        event_id = str(event.get("id") or "")
        event_time_text = str(event.get("eventTimeUTC") or "")
        closest_text = str(event.get("closestApproachUTC") or "")
        if not event_id:
            raise RuntimeError("Close-encounter event is missing id.")
        if event_id in seen_ids:
            raise RuntimeError(f"Duplicate event ID within shard: {event_id}.")
        seen_ids.add(event_id)
        if event.get("eventFamily") != EVENT_FAMILY or event.get("type") != EVENT_TYPE:
            raise RuntimeError(f"Event {event_id} has unsupported family or type.")
        event_time = lunar.parse_utc_datetime(event_time_text)
        closest_time = lunar.parse_utc_datetime(closest_text)
        if event_time != closest_time:
            raise RuntimeError(f"Event {event_id} eventTimeUTC must equal closestApproachUTC.")
        if not package_start <= event_time < package_end:
            raise RuntimeError(f"Event {event_id} is outside the package window.")
        if not shard_start <= event_time < shard_end:
            raise RuntimeError(f"Event {event_id} is outside its shard window.")
        key = (event_time_text, event_id)
        if key < previous_key:
            raise RuntimeError("Close-encounter events must be sorted by time and ID.")
        previous_key = key

        separation = lunar.finite_float(event.get("minimumSeparationDegrees"))
        if separation is None or separation < 0 or separation > threshold + 0.000_001:
            raise RuntimeError(f"Event {event_id} separation is outside the package threshold.")
        planet, target = event_participants(event)
        if planet is None or target is None:
            raise RuntimeError(f"Event {event_id} must contain one planet and one DSO participant.")
        planet_id = str(planet.get("id") or "")
        target_id = str(target.get("id") or "")
        if planet_id not in planet_ids:
            raise RuntimeError(f"Event {event_id} references unknown planet {planet_id}.")
        target_group = target_groups.get(target_id)
        if target_group is None:
            raise RuntimeError(f"Event {event_id} references unknown target group {target_id}.")
        for key_name in ("catalogID", "displayName", "objectType"):
            if not str(target.get(key_name) or "").strip():
                raise RuntimeError(f"Event {event_id} target is missing {key_name}.")
        target_ids = target_group.get("targetIDs") or []
        if target.get("catalogID") not in target_ids:
            raise RuntimeError(f"Event {event_id} target catalogID is not canonical for {target_id}.")
        if target.get("displayName") != target_group.get("displayName"):
            raise RuntimeError(f"Event {event_id} target displayName disagrees with index.")
        if target.get("objectType") != (target_group.get("objectType") or "Unknown"):
            raise RuntimeError(f"Event {event_id} target objectType disagrees with index.")
        for participant in (planet, target):
            magnitude = participant.get("magnitude")
            if magnitude is not None and lunar.finite_float(magnitude) is None:
                raise RuntimeError(f"Event {event_id} contains a non-finite magnitude.")
        expected_id = event_identifier(planet_id, target_id, closest_time)
        if event_id != expected_id:
            raise RuntimeError(
                f"Event {event_id} does not match stable ID convention {expected_id}."
            )
    return event_counts(events)


def event_participants(
    event: dict[str, Any],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    participants = event.get("participants")
    if not isinstance(participants, list) or len(participants) != 2:
        return None, None
    planets = [
        row for row in participants if isinstance(row, dict) and row.get("kind") == "majorPlanet"
    ]
    targets = [
        row for row in participants if isinstance(row, dict) and row.get("kind") == "deepSkyObject"
    ]
    if len(planets) != 1 or len(targets) != 1:
        return None, None
    return planets[0], targets[0]


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
        raise RuntimeError("Manifest packageVersion does not match index.")
    if entry.get("payloadSchemaVersion") != package.get("schemaVersion"):
        raise RuntimeError("Manifest payloadSchemaVersion does not match index.")
    expected_url = f"{METADATA_ORIGIN}/{repo_relative_path(output_path).as_posix()}"
    if entry.get("packageURL") != expected_url:
        raise RuntimeError("Manifest packageURL does not reference the generated index.")
    if int(entry.get("byteSize") or 0) != len(data):
        raise RuntimeError("Manifest byteSize does not match index.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != hashlib.sha256(data).hexdigest():
        raise RuntimeError("Manifest checksum does not match index.")


def shard_path_from_descriptor(descriptor: dict[str, Any]) -> Path:
    raw_path = str(descriptor.get("path") or "").strip()
    if not raw_path:
        raise RuntimeError(f"Shard {descriptor.get('id')} is missing a repository path.")
    path = Path(raw_path)
    return path if path.is_absolute() else REPO_ROOT / path


def clean_shard_directory(index_path: Path) -> None:
    shard_dir = index_path.parent / "shards"
    if not shard_dir.exists():
        return
    for path in shard_dir.glob("planet_target_close_encounters_*_v1.json"):
        path.unlink()


def add_years(value: dt.datetime, years: int) -> dt.datetime:
    try:
        return value.replace(year=value.year + years)
    except ValueError:
        return value.replace(year=value.year + years, month=2, day=28)


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
