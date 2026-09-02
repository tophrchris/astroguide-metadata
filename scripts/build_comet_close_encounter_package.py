#!/usr/bin/env python3
"""Build AstroGuide hosted comet/catalog-target close encounters."""

from __future__ import annotations

import argparse
import bisect
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
DEFAULT_COMET_SNAPSHOT = Path("v1/packages/comets/comet_snapshot_v1.json")
DEFAULT_PACKAGE_PATH = Path(
    "v1/packages/comet-close-encounters/comet_close_encounter_metadata_v1.json"
)
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "cometCloseEncounters"
PACKAGE_BASENAME = "comet-close-encounters"
EVENT_FAMILY = "closeEncounter"
COMET_TARGET_EVENT_TYPE = "cometTargetCloseEncounter"
COMET_DYNAMIC_EVENT_TYPE = "cometDynamicCloseEncounter"
EVENT_TYPES = [COMET_TARGET_EVENT_TYPE, COMET_DYNAMIC_EVENT_TYPE]
EVENT_TYPE = COMET_TARGET_EVENT_TYPE
ALGORITHM_VERSION = "comet-close-encounters-v1"
DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT = lunar.DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT
DEFAULT_EPHEMERIS_CACHE = Path.home() / "Library/Caches/com.tophrchris.AstroGuide/lunar-events"
DEFAULT_EPHEMERIS = "de421.bsp"
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


@dataclass(frozen=True)
class CometSample:
    timestamp: dt.datetime
    right_ascension_hours: float
    declination_degrees: float
    magnitude: float | None


@dataclass(frozen=True)
class CometStream:
    stable_id: str
    designation: str
    display_name: str
    orbit_class: str | None
    samples: list[CometSample]

    @property
    def start(self) -> dt.datetime:
        return self.samples[0].timestamp

    @property
    def end(self) -> dt.datetime:
        return self.samples[-1].timestamp

    @property
    def minimum_magnitude(self) -> float | None:
        values = [sample.magnitude for sample in self.samples if sample.magnitude is not None]
        return min(values) if values else None

    @property
    def maximum_magnitude(self) -> float | None:
        values = [sample.magnitude for sample in self.samples if sample.magnitude is not None]
        return max(values) if values else None


@dataclass(frozen=True)
class InterpolatedCometState:
    timestamp: dt.datetime
    right_ascension_hours: float
    declination_degrees: float
    magnitude: float | None


@dataclass(frozen=True)
class DynamicBodySubject:
    kind: str
    body_id: str
    display_name: str
    ephemeris_key: str


@dataclass(frozen=True)
class ShardBuild:
    path: Path
    payload: dict[str, Any]
    data: bytes
    descriptor: dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-repo", type=Path, default=DEFAULT_APP_REPO)
    parser.add_argument(
        "--catalog",
        type=Path,
        help=(
            "Catalog SQLite path. Defaults to App/Resources/Catalog/catalog.sqlite "
            "inside --app-repo."
        ),
    )
    parser.add_argument("--comet-snapshot", type=Path, default=DEFAULT_COMET_SNAPSHOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_PACKAGE_PATH)
    parser.add_argument("--manifest", type=Path, default=Path("v1/channels/stable/manifest.json"))
    parser.add_argument(
        "--seasonal-recommendation-dir",
        type=Path,
        default=lunar.DEFAULT_SEASONAL_RECOMMENDATION_DIR,
    )
    parser.add_argument("--target-metadata", type=Path, default=lunar.DEFAULT_TARGET_METADATA_PATH)
    parser.add_argument(
        "--target-neighborhoods",
        type=Path,
        default=lunar.DEFAULT_TARGET_NEIGHBORHOOD_PATH,
    )
    parser.add_argument("--start-date")
    parser.add_argument("--end-date")
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--min-supported-app-version", default="1.4.0")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--max-separation-degrees", type=float, default=5.0)
    parser.add_argument(
        "--dynamic-dynamic-max-separation-degrees",
        type=float,
        help="Maximum separation for comet-to-Moon/planet events. Defaults to --max-separation-degrees.",
    )
    parser.add_argument("--max-comet-magnitude", type=float)
    parser.add_argument("--max-target-magnitude", type=float)
    parser.add_argument(
        "--bright-ngc-ic-mag-limit",
        type=float,
        default=DEFAULT_BRIGHT_NGC_IC_MAG_LIMIT,
    )
    parser.add_argument("--refine-step-minutes", type=int, default=60)
    parser.add_argument("--dynamic-sample-step-minutes", type=int, default=180)
    parser.add_argument("--ephemeris-cache", type=Path, default=DEFAULT_EPHEMERIS_CACHE)
    parser.add_argument("--ephemeris", default=DEFAULT_EPHEMERIS)
    parser.add_argument("--dedupe-coordinate-arcmin", type=float, default=6.0)
    parser.add_argument(
        "--max-events-per-comet",
        type=int,
        default=0,
        help="Optional ranking cap per comet after event generation. 0 means unlimited.",
    )
    parser.add_argument(
        "--skip-dynamic-dynamic",
        action="store_true",
        help="Generate only Comet-to-DSO dynamic-static events.",
    )
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate an existing package, monthly shards, and manifest descriptor.",
    )
    args = parser.parse_args()
    if args.max_separation_degrees <= 0:
        raise SystemExit("--max-separation-degrees must be positive")
    if (
        args.dynamic_dynamic_max_separation_degrees is not None
        and args.dynamic_dynamic_max_separation_degrees <= 0
    ):
        raise SystemExit("--dynamic-dynamic-max-separation-degrees must be positive")
    if args.bright_ngc_ic_mag_limit <= 0:
        raise SystemExit("--bright-ngc-ic-mag-limit must be positive")
    if args.refine_step_minutes <= 0:
        raise SystemExit("--refine-step-minutes must be positive")
    if args.dynamic_sample_step_minutes <= 0:
        raise SystemExit("--dynamic-sample-step-minutes must be positive")
    if args.refine_step_minutes > args.dynamic_sample_step_minutes:
        raise SystemExit("--refine-step-minutes cannot exceed --dynamic-sample-step-minutes")
    if args.dedupe_coordinate_arcmin < 0:
        raise SystemExit("--dedupe-coordinate-arcmin cannot be negative")
    if args.max_events_per_comet < 0:
        raise SystemExit("--max-events-per-comet cannot be negative")
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

    app_repo = args.app_repo.resolve()
    catalog_path = (args.catalog.resolve() if args.catalog else app_repo / DEFAULT_CATALOG_PATH).resolve()
    comet_snapshot_path = repo_path(args.comet_snapshot)
    comet_snapshot = read_json(comet_snapshot_path)
    streams = load_comet_streams(comet_snapshot)
    if not streams:
        raise SystemExit("No comet streams found in comet snapshot package.")

    source_start = max(stream.start for stream in streams)
    source_end = min(stream.end for stream in streams)
    start = lunar.parse_utc_datetime(args.start_date) if args.start_date else source_start
    end = lunar.parse_utc_datetime(args.end_date) if args.end_date else source_end
    if start < source_start or end > source_end:
        raise SystemExit(
            "Requested window must stay inside the comet snapshot ephemeris window "
            f"({lunar.isoformat_z(source_start)} to {lunar.isoformat_z(source_end)})."
        )
    if end <= start:
        raise SystemExit("--end-date must be after --start-date")

    generated_at = args.generated_at or lunar.utc_now()
    lunar.parse_utc_datetime(generated_at)
    package_version = args.package_version or f"{PACKAGE_BASENAME}-v1-{lunar.date_token(generated_at)}"

    targets = lunar.load_targets(catalog_path)
    if not targets:
        raise SystemExit(f"No catalog targets with coordinates found in {catalog_path}")
    all_target_groups = lunar.build_target_groups(targets, args.dedupe_coordinate_arcmin)
    identity_context = lunar.build_target_identity_context(
        all_target_groups,
        args.dedupe_coordinate_arcmin,
    )
    curated_references = [
        *lunar.load_curated_recommendation_references(repo_path(args.seasonal_recommendation_dir)),
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
    target_groups = apply_target_magnitude_limit(target_groups, args.max_target_magnitude)
    comet_streams = apply_comet_magnitude_limit(streams, args.max_comet_magnitude)
    if not comet_streams:
        raise SystemExit("No comet streams remain after magnitude filtering.")

    print(
        f"Loaded {len(targets)} coordinate targets, grouped into "
        f"{len(all_target_groups)} canonical target groups.",
        flush=True,
    )
    print(
        f"Selected {len(target_groups)} DSO target groups "
        f"({lunar.selection_reason_summary(selection_reasons)}).",
        flush=True,
    )
    print(f"Selected {len(comet_streams)} comet ephemeris streams.", flush=True)

    np = load_numpy()
    target_events, event_target_group_ids = compute_close_encounters(
        np=np,
        comet_streams=comet_streams,
        target_groups=target_groups,
        identity_context=identity_context,
        start=start,
        end=end,
        max_separation_degrees=args.max_separation_degrees,
        refine_step=dt.timedelta(minutes=args.refine_step_minutes),
        package_version=package_version,
    )
    dynamic_body_subjects = supported_dynamic_body_subjects()
    event_dynamic_body_ids: set[str] = set()
    dynamic_events: list[dict[str, Any]] = []
    sky_versions: dict[str, str] = {}
    eph: Any = None
    if not args.skip_dynamic_dynamic:
        sky = lunar.load_skyfield_modules()
        sky_versions = sky.versions
        load = sky.Loader(str(args.ephemeris_cache.resolve()))
        eph = load(args.ephemeris)
        ts = load.timescale()
        earth = eph["earth"]
        dynamic_threshold = (
            args.dynamic_dynamic_max_separation_degrees
            if args.dynamic_dynamic_max_separation_degrees is not None
            else args.max_separation_degrees
        )
        dynamic_sample_times = lunar.date_grid(
            start,
            end,
            dt.timedelta(minutes=args.dynamic_sample_step_minutes),
        )
        print(
            f"Scanning {len(dynamic_sample_times)} dynamic samples for comet-to-Moon/planet "
            f"close encounters.",
            flush=True,
        )
        dynamic_events, event_dynamic_body_ids = compute_dynamic_close_encounters(
            sky=sky,
            comet_streams=comet_streams,
            dynamic_body_subjects=dynamic_body_subjects,
            sample_times=dynamic_sample_times,
            start=start,
            end=end,
            max_separation_degrees=dynamic_threshold,
            refine_step=dt.timedelta(minutes=args.refine_step_minutes),
            package_version=package_version,
            earth=earth,
            eph=eph,
            ts=ts,
        )
    events = [*target_events, *dynamic_events]
    events = apply_event_limit(events, args.max_events_per_comet)
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
        comet_snapshot_path=comet_snapshot_path,
        comet_snapshot=comet_snapshot,
        source_target_group_count=len(all_target_groups),
        candidate_target_groups=target_groups,
        event_target_groups=event_target_groups,
        identity_context=identity_context,
        selection_reasons=selection_reasons,
        source_comet_streams=streams,
        comet_streams=comet_streams,
        dynamic_body_subjects=dynamic_body_subjects,
        event_dynamic_body_ids=event_dynamic_body_ids,
        events=events,
        shard_descriptors=[shard.descriptor for shard in shard_builds],
        shard_event_rows=sum(int(shard.descriptor["eventCount"]) for shard in shard_builds),
        args=args,
        sky_versions=sky_versions,
        skyfield_ephemeris=eph,
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
    print(f"Events by type: {counts['eventsByType']}", flush=True)
    print(f"Events by comet: {counts['eventsByComet']}", flush=True)
    return 0


def load_numpy() -> Any:
    try:
        import numpy as np  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment diagnostic
        raise SystemExit(
            "numpy is required. Install scripts/requirements-lunar-events.txt in the active venv."
        ) from exc
    return np


def load_comet_streams(package: dict[str, Any]) -> list[CometStream]:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Comet snapshot schemaVersion must be 1.")
    if package.get("packageFamily") != "cometSnapshot":
        raise RuntimeError("Comet close-encounter generation requires a cometSnapshot package.")
    seeds = package.get("seeds") or {}
    ephemeris = package.get("ephemeris") or {}
    seed_rows = seeds.get("comets")
    ephemeris_rows = ephemeris.get("comets")
    if not isinstance(seed_rows, list) or not seed_rows:
        raise RuntimeError("Comet snapshot package contains no seed rows.")
    if not isinstance(ephemeris_rows, dict) or not ephemeris_rows:
        raise RuntimeError("Comet snapshot package contains no ephemeris rows.")

    anchor = lunar.parse_utc_datetime(str(ephemeris.get("anchorTimestamp") or ""))
    sample_step_hours = int(ephemeris.get("sampleStepHours") or 0)
    sample_count = int(ephemeris.get("sampleCount") or 0)
    if sample_step_hours <= 0 or sample_count <= 0:
        raise RuntimeError("Comet snapshot ephemeris sample cadence is invalid.")

    streams: list[CometStream] = []
    for seed in seed_rows:
        stable_id = str(seed.get("stableID") or "").strip()
        rows = ephemeris_rows.get(stable_id)
        if not stable_id or not isinstance(rows, list) or not rows:
            raise RuntimeError(f"Comet snapshot ephemeris is missing rows for {stable_id}.")
        samples: list[CometSample] = []
        for index, row in enumerate(rows):
            if not isinstance(row, list) or len(row) < 2:
                raise RuntimeError(f"Comet ephemeris row {index} for {stable_id} is invalid.")
            ra_hours = lunar.finite_float(row[0])
            dec_degrees = lunar.finite_float(row[1])
            magnitude = lunar.finite_float(row[2]) if len(row) > 2 else None
            if ra_hours is None or dec_degrees is None:
                raise RuntimeError(f"Comet ephemeris row {index} for {stable_id} is non-finite.")
            samples.append(
                CometSample(
                    timestamp=anchor + dt.timedelta(hours=sample_step_hours * index),
                    right_ascension_hours=ra_hours % 24.0,
                    declination_degrees=dec_degrees,
                    magnitude=magnitude,
                )
            )
        if len(samples) != sample_count:
            raise RuntimeError(f"Comet ephemeris row count mismatch for {stable_id}.")
        streams.append(
            CometStream(
                stable_id=stable_id,
                designation=str(seed.get("designation") or stable_id),
                display_name=str(seed.get("displayName") or seed.get("designation") or stable_id),
                orbit_class=optional_text(seed.get("orbitClass")),
                samples=samples,
            )
        )
    return streams


def apply_comet_magnitude_limit(
    streams: list[CometStream],
    max_magnitude: float | None,
) -> list[CometStream]:
    if max_magnitude is None:
        return streams
    return [
        stream
        for stream in streams
        if stream.minimum_magnitude is not None and stream.minimum_magnitude <= max_magnitude
    ]


def apply_target_magnitude_limit(
    target_groups: list[lunar.TargetGroup],
    max_magnitude: float | None,
) -> list[lunar.TargetGroup]:
    if max_magnitude is None:
        return target_groups
    return [
        group
        for group in target_groups
        if group.canonical.magnitude is not None and group.canonical.magnitude <= max_magnitude
    ]


def compute_close_encounters(
    *,
    np: Any,
    comet_streams: list[CometStream],
    target_groups: list[lunar.TargetGroup],
    identity_context: lunar.TargetIdentityContext,
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    package_version: str,
) -> tuple[list[dict[str, Any]], set[str]]:
    events_by_id: dict[str, dict[str, Any]] = {}
    event_target_group_ids: set[str] = set()

    for stream in comet_streams:
        sample_times, comet_ra, comet_dec = comet_arrays(np, stream)
        candidate_count = 0
        for target_group in target_groups:
            separations = separation_from_fixed_target(
                np,
                target_group.canonical,
                comet_ra,
                comet_dec,
            )
            for minimum_index in local_minimum_indices(np, separations, max_separation_degrees):
                if minimum_index <= 0 or minimum_index >= len(sample_times) - 1:
                    continue
                event = refine_close_encounter(
                    np=np,
                    stream=stream,
                    target_group=target_group,
                    identity_context=identity_context,
                    minimum_index=minimum_index,
                    sample_times=sample_times,
                    start=start,
                    end=end,
                    max_separation_degrees=max_separation_degrees,
                    refine_step=refine_step,
                    package_version=package_version,
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
        print(f"{stream.display_name}: refined {candidate_count} close encounters.", flush=True)

    return list(events_by_id.values()), event_target_group_ids


def comet_arrays(
    np: Any,
    stream: CometStream,
) -> tuple[list[dt.datetime], Any, Any]:
    sample_times = [sample.timestamp for sample in stream.samples]
    ra = np.radians([sample.right_ascension_hours * 15.0 for sample in stream.samples])
    dec = np.radians([sample.declination_degrees for sample in stream.samples])
    return sample_times, ra, dec


def separation_from_fixed_target(
    np: Any,
    target: lunar.TargetRecord,
    body_ra: Any,
    body_dec: Any,
) -> Any:
    target_ra = math.radians(target.ra_degrees)
    target_dec = math.radians(target.dec_degrees)
    cosines = (
        math.sin(target_dec) * np.sin(body_dec)
        + math.cos(target_dec)
        * np.cos(body_dec)
        * np.cos(target_ra - body_ra)
    )
    return np.degrees(np.arccos(np.clip(cosines, -1.0, 1.0)))


def local_minimum_indices(np: Any, values: Any, threshold: float) -> list[int]:
    if len(values) < 3:
        return []
    middle = values[1:-1]
    mask = (middle <= threshold) & (middle <= values[:-2]) & (middle < values[2:])
    return (np.flatnonzero(mask) + 1).tolist()


def refine_close_encounter(
    *,
    np: Any,
    stream: CometStream,
    target_group: lunar.TargetGroup,
    identity_context: lunar.TargetIdentityContext,
    minimum_index: int,
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    package_version: str,
) -> dict[str, Any] | None:
    bracket_start = sample_times[minimum_index - 1]
    bracket_end = sample_times[minimum_index + 1]
    fine_times = lunar.date_grid(bracket_start, bracket_end, refine_step)
    fine_states = [interpolate_comet_state(stream, timestamp) for timestamp in fine_times]
    separations = np.asarray(
        [
            scalar_separation_degrees(
                state.right_ascension_hours * 15.0,
                state.declination_degrees,
                target_group.canonical.ra_degrees,
                target_group.canonical.dec_degrees,
            )
            for state in fine_states
        ]
    )
    fine_minimum_index = int(np.argmin(separations))
    closest_time = lunar.refined_minimum_time(
        fine_times,
        separations,
        fine_minimum_index,
        refine_step,
    )
    closest_state = interpolate_comet_state(stream, closest_time)
    closest_separation = scalar_separation_degrees(
        closest_state.right_ascension_hours * 15.0,
        closest_state.declination_degrees,
        target_group.canonical.ra_degrees,
        target_group.canonical.dec_degrees,
    )
    if closest_time < start or closest_time >= end:
        return None
    if closest_separation > max_separation_degrees + 0.000_001:
        return None

    participants = [
        comet_participant(stream, closest_state),
        target_participant(target_group, identity_context),
    ]
    event_id = event_identifier(stream.stable_id, target_group.group_id, closest_time)
    return {
        "id": event_id,
        "eventFamily": EVENT_FAMILY,
        "type": EVENT_TYPE,
        "eventTimeUTC": lunar.isoformat_z(closest_time),
        "closestApproachUTC": lunar.isoformat_z(closest_time),
        "minimumSeparationDegrees": round(closest_separation, 4),
        "participants": participants,
        "source": {
            "packageFamily": PACKAGE_FAMILY,
            "packageVersion": package_version,
            "recordID": event_id,
            "sourceDescription": "Generated from cometSnapshot ephemeris and AstroGuide catalog metadata.",
        },
    }


def supported_dynamic_body_subjects() -> list[DynamicBodySubject]:
    return [
        DynamicBodySubject(
            kind="moon",
            body_id="moon",
            display_name="Moon",
            ephemeris_key="moon",
        ),
        *[
            DynamicBodySubject(
                kind="majorPlanet",
                body_id=planet_id,
                display_name=display_name,
                ephemeris_key=ephemeris_key,
            )
            for planet_id, display_name, ephemeris_key in lunar.PLANET_SUBJECTS
        ],
    ]


def compute_dynamic_close_encounters(
    *,
    sky: lunar.SkyfieldModules,
    comet_streams: list[CometStream],
    dynamic_body_subjects: list[DynamicBodySubject],
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    package_version: str,
    earth: Any,
    eph: Any,
    ts: Any,
) -> tuple[list[dict[str, Any]], set[str]]:
    events_by_id: dict[str, dict[str, Any]] = {}
    event_dynamic_body_ids: set[str] = set()
    comet_arrays_by_id = {
        stream.stable_id: comet_state_arrays(sky.np, stream, sample_times)
        for stream in comet_streams
    }

    for body_subject in dynamic_body_subjects:
        body = eph[body_subject.ephemeris_key]
        body_ra, body_dec = lunar.apparent_radec_arrays(sky, earth, body, ts, sample_times)
        body_candidate_count = 0
        for stream in comet_streams:
            comet_ra, comet_dec = comet_arrays_by_id[stream.stable_id]
            separations = lunar.separation_arrays(
                sky,
                comet_ra,
                comet_dec,
                body_ra,
                body_dec,
            )
            for minimum_index in local_minimum_indices(
                sky.np,
                separations,
                max_separation_degrees,
            ):
                if minimum_index <= 0 or minimum_index >= len(sample_times) - 1:
                    continue
                event = refine_dynamic_close_encounter(
                    sky=sky,
                    stream=stream,
                    body_subject=body_subject,
                    body=body,
                    minimum_index=minimum_index,
                    sample_times=sample_times,
                    start=start,
                    end=end,
                    max_separation_degrees=max_separation_degrees,
                    refine_step=refine_step,
                    package_version=package_version,
                    earth=earth,
                    eph=eph,
                    ts=ts,
                )
                if event is None:
                    continue
                body_candidate_count += 1
                event_id = str(event["id"])
                previous = events_by_id.get(event_id)
                if previous is None or float(event["minimumSeparationDegrees"]) < float(
                    previous["minimumSeparationDegrees"]
                ):
                    events_by_id[event_id] = event
                event_dynamic_body_ids.add(body_subject.body_id)
        print(
            f"{body_subject.display_name}: refined {body_candidate_count} comet dynamic close encounters.",
            flush=True,
        )

    return list(events_by_id.values()), event_dynamic_body_ids


def refine_dynamic_close_encounter(
    *,
    sky: lunar.SkyfieldModules,
    stream: CometStream,
    body_subject: DynamicBodySubject,
    body: Any,
    minimum_index: int,
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    refine_step: dt.timedelta,
    package_version: str,
    earth: Any,
    eph: Any,
    ts: Any,
) -> dict[str, Any] | None:
    bracket_start = sample_times[minimum_index - 1]
    bracket_end = sample_times[minimum_index + 1]
    fine_times = lunar.date_grid(bracket_start, bracket_end, refine_step)
    comet_ra, comet_dec = comet_state_arrays(sky.np, stream, fine_times)
    body_ra, body_dec = lunar.apparent_radec_arrays(sky, earth, body, ts, fine_times)
    separations = lunar.separation_arrays(sky, comet_ra, comet_dec, body_ra, body_dec)
    fine_minimum_index = int(sky.np.argmin(separations))
    closest_time = lunar.refined_minimum_time(
        fine_times,
        separations,
        fine_minimum_index,
        refine_step,
    )
    closest_state = interpolate_comet_state(stream, closest_time)
    companion = dynamic_body_participant(
        sky=sky,
        body_subject=body_subject,
        body=body,
        timestamp=closest_time,
        earth=earth,
        eph=eph,
        ts=ts,
    )
    companion_coordinate = companion["coordinate"]
    closest_separation = scalar_separation_degrees(
        closest_state.right_ascension_hours * 15.0,
        closest_state.declination_degrees,
        float(companion_coordinate["rightAscensionHours"]) * 15.0,
        float(companion_coordinate["declinationDegrees"]),
    )
    if closest_time < start or closest_time >= end:
        return None
    if closest_separation > max_separation_degrees + 0.000_001:
        return None

    participants = [
        comet_participant(stream, closest_state),
        companion,
    ]
    event_id = event_identifier(
        stream.stable_id,
        body_subject.body_id,
        closest_time,
        event_type=COMET_DYNAMIC_EVENT_TYPE,
    )
    return {
        "id": event_id,
        "eventFamily": EVENT_FAMILY,
        "type": COMET_DYNAMIC_EVENT_TYPE,
        "eventTimeUTC": lunar.isoformat_z(closest_time),
        "closestApproachUTC": lunar.isoformat_z(closest_time),
        "minimumSeparationDegrees": round(closest_separation, 4),
        "participants": participants,
        "source": {
            "packageFamily": PACKAGE_FAMILY,
            "packageVersion": package_version,
            "recordID": event_id,
            "sourceDescription": "Generated from cometSnapshot ephemeris and Skyfield/JPL Moon/planet ephemerides.",
        },
    }


def comet_state_arrays(
    np: Any,
    stream: CometStream,
    sample_times: list[dt.datetime],
) -> tuple[Any, Any]:
    states = [interpolate_comet_state(stream, timestamp) for timestamp in sample_times]
    return (
        np.radians([state.right_ascension_hours * 15.0 for state in states]),
        np.radians([state.declination_degrees for state in states]),
    )


def interpolate_comet_state(
    stream: CometStream,
    timestamp: dt.datetime,
) -> InterpolatedCometState:
    samples = stream.samples
    if timestamp <= samples[0].timestamp:
        sample = samples[0]
        return InterpolatedCometState(
            timestamp=timestamp,
            right_ascension_hours=sample.right_ascension_hours,
            declination_degrees=sample.declination_degrees,
            magnitude=sample.magnitude,
        )
    if timestamp >= samples[-1].timestamp:
        sample = samples[-1]
        return InterpolatedCometState(
            timestamp=timestamp,
            right_ascension_hours=sample.right_ascension_hours,
            declination_degrees=sample.declination_degrees,
            magnitude=sample.magnitude,
        )

    timestamps = [sample.timestamp for sample in samples]
    index = bisect.bisect_right(timestamps, timestamp)
    previous = samples[index - 1]
    current = samples[index]
    duration = max((current.timestamp - previous.timestamp).total_seconds(), 1.0e-9)
    fraction = min(
        max((timestamp - previous.timestamp).total_seconds() / duration, 0.0),
        1.0,
    )
    previous_ra = previous.right_ascension_hours * 15.0
    current_ra = current.right_ascension_hours * 15.0
    delta_ra = ((current_ra - previous_ra + 180.0) % 360.0) - 180.0
    ra_degrees = normalize_degrees(previous_ra + (delta_ra * fraction))
    dec_degrees = interpolate(previous.declination_degrees, current.declination_degrees, fraction)
    magnitude = interpolate_optional(previous.magnitude, current.magnitude, fraction)
    return InterpolatedCometState(
        timestamp=timestamp,
        right_ascension_hours=ra_degrees / 15.0,
        declination_degrees=dec_degrees,
        magnitude=magnitude,
    )


def comet_participant(
    stream: CometStream,
    state: InterpolatedCometState,
) -> dict[str, Any]:
    return lunar.prune_none(
        {
            "kind": "comet",
            "id": stream.stable_id,
            "designation": stream.designation,
            "displayName": stream.display_name,
            "orbitClass": stream.orbit_class,
            "magnitude": lunar.round_optional(state.magnitude, 2),
            "coordinate": coordinate_payload(
                state.right_ascension_hours,
                state.declination_degrees,
            ),
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
            "coordinate": coordinate_payload(canonical.ra_hours, canonical.dec_degrees),
        }
    )


def dynamic_body_participant(
    *,
    sky: lunar.SkyfieldModules,
    body_subject: DynamicBodySubject,
    body: Any,
    timestamp: dt.datetime,
    earth: Any,
    eph: Any,
    ts: Any,
) -> dict[str, Any]:
    if body_subject.kind == "moon":
        moon_payload = lunar.moon_snapshot(sky, timestamp, earth, body, eph, ts)
        return lunar.prune_none(
            {
                "kind": "moon",
                "id": body_subject.body_id,
                "displayName": body_subject.display_name,
                "magnitude": moon_payload.get("approximateVisualMagnitude"),
                "coordinate": coordinate_payload(
                    float(moon_payload["rightAscensionHours"]),
                    float(moon_payload["declinationDegrees"]),
                ),
                "distanceKm": moon_payload.get("distanceKm"),
                "apparentDiameterArcmin": moon_payload.get("apparentDiameterArcmin"),
                "illuminationFraction": moon_payload.get("illuminationFraction"),
                "phaseAngleDegrees": moon_payload.get("phaseAngleDegrees"),
                "phaseLabel": moon_payload.get("phaseLabel"),
            }
        )

    planet = lunar.PlanetSubject(
        planet_id=body_subject.body_id,
        display_name=body_subject.display_name,
        ephemeris_key=body_subject.ephemeris_key,
    )
    planet_payload = lunar.planet_snapshot(sky, planet, body, timestamp, earth, ts)
    return lunar.prune_none(
        {
            "kind": "majorPlanet",
            "id": planet_payload.get("id") or body_subject.body_id,
            "displayName": planet_payload.get("displayName") or body_subject.display_name,
            "magnitude": planet_payload.get("visualMagnitude"),
            "coordinate": coordinate_payload(
                float(planet_payload["rightAscensionHours"]),
                float(planet_payload["declinationDegrees"]),
            ),
            "distanceAU": planet_payload.get("distanceAU"),
        }
    )


def coordinate_payload(ra_hours: float, dec_degrees: float) -> dict[str, float]:
    return {
        "rightAscensionHours": round(ra_hours % 24.0, 6),
        "declinationDegrees": round(dec_degrees, 6),
    }


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
            if shard_start <= lunar.parse_utc_datetime(str(event["eventTimeUTC"])) < shard_end
        ]
        if not shard_events:
            continue
        shard_id = shard_start.strftime("%Y-%m")
        shard_path = (
            index_path.parent
            / "shards"
            / f"comet_close_encounters_{shard_start:%Y_%m}_v1.json"
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
            "counts": event_counts(payload["events"]),
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
    comet_snapshot_path: Path,
    comet_snapshot: dict[str, Any],
    source_target_group_count: int,
    candidate_target_groups: list[lunar.TargetGroup],
    event_target_groups: list[lunar.TargetGroup],
    identity_context: lunar.TargetIdentityContext,
    selection_reasons: dict[str, list[str]],
    source_comet_streams: list[CometStream],
    comet_streams: list[CometStream],
    dynamic_body_subjects: list[DynamicBodySubject],
    event_dynamic_body_ids: set[str],
    events: list[dict[str, Any]],
    shard_descriptors: list[dict[str, Any]],
    shard_event_rows: int,
    args: argparse.Namespace,
    sky_versions: dict[str, str],
    skyfield_ephemeris: Any,
) -> dict[str, Any]:
    counts = event_counts(events)
    selection_counts: dict[str, int] = defaultdict(int)
    for reasons in selection_reasons.values():
        for reason in reasons:
            selection_counts[reason] += 1

    comet_ephemeris = comet_snapshot.get("ephemeris") or {}
    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "packageRole": "index",
        "generatedAt": generated_at,
        "eventFamilies": [EVENT_FAMILY],
        "eventTypes": EVENT_TYPES,
        "window": {
            "startUTC": lunar.isoformat_z(start),
            "endUTC": lunar.isoformat_z(end),
            "durationDays": round((end - start).total_seconds() / 86400.0, 3),
        },
        "source": {
            "name": "AstroGuide comet close-encounter pipeline",
            "generatedBy": "scripts/build_comet_close_encounter_package.py",
            "algorithmVersion": ALGORITHM_VERSION,
            "catalogSourceRepo": "tophrchris/DSOPlanneriOS",
            "catalogPath": lunar.source_relative(catalog_path, app_repo),
            "catalogVersion": catalog_metadata.get("catalog_version"),
            "catalogFingerprint": catalog_metadata.get("catalog_fingerprint"),
            "catalogSHA256": lunar.sha256_file(catalog_path),
            "targetMetadataPath": repo_relative(repo_path(args.target_metadata)),
            "targetNeighborhoodPath": repo_relative(repo_path(args.target_neighborhoods)),
            "seasonalRecommendationDirectory": repo_relative(repo_path(args.seasonal_recommendation_dir)),
            "cometSnapshotPath": repo_relative(comet_snapshot_path),
            "cometSnapshotPackageVersion": comet_snapshot.get("packageVersion"),
            "cometSnapshotSHA256": lunar.sha256_file(comet_snapshot_path),
            "cometEphemerisGeneratedAt": comet_ephemeris.get("generatedAt"),
            "cometFrame": (
                "Geocentric apparent equatorial RA/Dec samples from the cometSnapshot "
                "ephemeris, linearly interpolated between source sample timestamps."
            ),
            "targetFrame": "Catalog J2000 equatorial RA/Dec held fixed during the scan.",
            "coordinateFrame": {
                "comet": "geocentric-apparent-equatorial-of-date",
                "target": "catalog-j2000-equatorial",
                "dynamicBody": "geocentric-apparent-equatorial-of-date",
                "units": {
                    "rightAscension": "hours",
                    "declination": "degrees",
                },
            },
            "timescale": "UTC",
            "closestApproachAlgorithm": (
                "Detect local angular-separation minima on the cometSnapshot sample grid "
                "for static targets and on the dynamic Moon/planet sample grid for dynamic "
                "targets, refine each bracket on a finer grid, then apply quadratic time "
                "interpolation."
            ),
            "eventIDAlgorithm": (
                "Stable comet ID plus companion ID plus UTC closest-approach date."
            ),
            "cometMagnitudeModel": (
                "Interpolated apparent magnitude from the cometSnapshot sample row when finite."
            ),
            "ephemeris": None if args.skip_dynamic_dynamic else args.ephemeris,
            "ephemerisPath": None
            if args.skip_dynamic_dynamic
            else str(getattr(skyfield_ephemeris, "filename", args.ephemeris)),
            "ephemerisSource": (
                None
                if args.skip_dynamic_dynamic
                else "JPL Development Ephemeris loaded through Skyfield"
            ),
            "dynamicBodyFrame": (
                None
                if args.skip_dynamic_dynamic
                else (
                    "Geocentric apparent equatorial RA/Dec for Moon and planets from "
                    "Skyfield earth.at(t).observe(body).apparent()."
                )
            ),
            "planetMagnitudeModel": (
                None
                if args.skip_dynamic_dynamic
                else "Skyfield magnitudelib planetary_magnitude where finite."
            ),
            "moonMagnitudeModel": (
                None
                if args.skip_dynamic_dynamic
                else "Approximate visual magnitude from lunar phase angle; intended for context."
            ),
            "versions": sky_versions or None,
        },
        "generationModel": {
            "dynamicStatic": {
                "status": "generated",
                "dynamicParticipantKind": "comet",
                "staticParticipantKind": "deepSkyObject",
                "eventType": COMET_TARGET_EVENT_TYPE,
            },
            "dynamicDynamic": lunar.prune_none(
                {
                    "status": "skipped" if args.skip_dynamic_dynamic else "generated",
                    "participantKinds": ["comet", "moon", "majorPlanet"],
                    "eventType": COMET_DYNAMIC_EVENT_TYPE,
                    "reason": None
                    if not args.skip_dynamic_dynamic
                    else "Dynamic-dynamic generation was explicitly skipped for this build.",
                }
            ),
            "excluded": ["deepSkyObject-deepSkyObject"],
        },
        "parameters": {
            "maxSeparationDegrees": args.max_separation_degrees,
            "dynamicDynamicMaxSeparationDegrees": (
                args.dynamic_dynamic_max_separation_degrees
                if args.dynamic_dynamic_max_separation_degrees is not None
                else args.max_separation_degrees
            ),
            "cometCandidateFilter": {
                "sourceCometCount": len(source_comet_streams),
                "maxCometMagnitude": args.max_comet_magnitude,
                "includedComets": len(comet_streams),
                "magnitudePolicy": (
                    "When maxCometMagnitude is unset, all cometSnapshot streams are eligible, "
                    "including faint curated comets."
                ),
            },
            "dsoCandidateFilter": {
                "curatedRecommendationUnion": (
                    "seasonal recommendation priorityTier=1 plus target metadata overlay"
                ),
                "includeMessier": True,
                "brightNGCICMagnitudeLimit": args.bright_ngc_ic_mag_limit,
                "maxTargetMagnitude": args.max_target_magnitude,
                "includeNamedShowcaseTargets": "target neighborhood catalog IDs",
                "excludeUnknownMagnitudeBackCatalogTargets": True,
            },
            "sourceSampleStepHours": comet_ephemeris.get("sampleStepHours"),
            "refineStepMinutes": args.refine_step_minutes,
            "dynamicSampleStepMinutes": args.dynamic_sample_step_minutes,
            "dedupeCoordinateArcmin": args.dedupe_coordinate_arcmin,
            "ranking": {
                "maxEventsPerComet": args.max_events_per_comet,
                "limitStrategy": (
                    "Unlimited by default; when capped, keep smallest separations per comet "
                    "with UTC time and ID as deterministic tie-breakers."
                ),
            },
            "siteObservabilityFilters": {
                "minimumAltitudeDegrees": None,
                "nighttimeFilter": "app-side",
                "horizonObstructionFilter": "app-side",
            },
            "shardStrategy": "monthly UTC by true closestApproachUTC",
            "dynamicSubjects": {
                "includeMoon": any(subject.kind == "moon" for subject in dynamic_body_subjects),
                "majorPlanets": [
                    subject.body_id
                    for subject in dynamic_body_subjects
                    if subject.kind == "majorPlanet"
                ],
            },
            "identityResolution": {
                "coordinateToleranceArcmin": identity_context.coordinate_tolerance_arcmin,
                "catalogPreferenceOrder": ["Messier", "NGC", "IC", "Caldwell", "supportedCatalogs"],
                "quarantinedCommonNameTokens": len(identity_context.ambiguous_common_tokens),
                "quarantinedAliasTokens": len(identity_context.ambiguous_exact_tokens),
            },
        },
        "counts": {
            "sourceTargetGroups": source_target_group_count,
            "candidateTargetGroups": len(candidate_target_groups),
            "eventTargetGroups": len(event_target_groups),
            "sourceComets": len(source_comet_streams),
            "candidateComets": len(comet_streams),
            "candidateSelectionReasons": dict(sorted(selection_counts.items())),
            "events": counts["events"],
            "eventsByType": counts["eventsByType"],
            "eventsByComet": counts["eventsByComet"],
            "eventsByTarget": counts["eventsByTarget"],
            "eventsBySolarSystemBody": counts["eventsBySolarSystemBody"],
            "shardEventRows": shard_event_rows,
            "shards": len(shard_descriptors),
        },
        "subjects": {
            "comets": [comet_subject_payload(stream) for stream in comet_streams],
            "dynamicBodies": [
                dynamic_body_subject_payload(subject, subject.body_id in event_dynamic_body_ids)
                for subject in dynamic_body_subjects
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
                "Ordered generic participants: comet first, then deep-sky target, Moon, "
                "or major planet."
            ),
        },
        "shards": shard_descriptors,
        "notes": [
            (
                "Events preserve true UTC closest-approach instants. App clients should group "
                "by local night and apply site observability filters at display time."
            ),
            (
                "Comet positions are interpolated from the deterministic cometSnapshot "
                "ephemeris cadence; this is a planning metadata proof point, not a replacement "
                "for precision Horizons queries."
            ),
            (
                "DSO-to-DSO events are intentionally not generated because static catalog "
                "targets do not move relative to each other."
            ),
        ],
    }


def comet_subject_payload(stream: CometStream) -> dict[str, Any]:
    return lunar.prune_none(
        {
            "id": stream.stable_id,
            "displayName": stream.display_name,
            "designation": stream.designation,
            "orbitClass": stream.orbit_class,
            "sampleCount": len(stream.samples),
            "startUTC": lunar.isoformat_z(stream.start),
            "endUTC": lunar.isoformat_z(stream.end),
            "minimumMagnitude": lunar.round_optional(stream.minimum_magnitude, 2),
            "maximumMagnitude": lunar.round_optional(stream.maximum_magnitude, 2),
        }
    )


def dynamic_body_subject_payload(subject: DynamicBodySubject, has_events: bool) -> dict[str, Any]:
    return {
        "kind": subject.kind,
        "id": subject.body_id,
        "displayName": subject.display_name,
        "ephemerisKey": subject.ephemeris_key,
        "hasEvents": has_events,
    }


def event_counts(events: list[dict[str, Any]]) -> dict[str, Any]:
    by_type: dict[str, int] = defaultdict(int)
    by_comet: dict[str, int] = defaultdict(int)
    by_target: dict[str, int] = defaultdict(int)
    by_solar_system_body: dict[str, int] = defaultdict(int)
    for event in events:
        by_type[str(event.get("type") or "unknown")] += 1
        comet, companion = event_participants(event)
        if comet:
            by_comet[str(comet.get("id") or "unknown")] += 1
        if companion:
            companion_id = str(companion.get("id") or "unknown")
            if companion.get("kind") == "deepSkyObject":
                by_target[companion_id] += 1
            elif companion.get("kind") in {"moon", "majorPlanet"}:
                by_solar_system_body[companion_id] += 1
    return {
        "events": len(events),
        "eventsByType": dict(sorted(by_type.items())),
        "eventsByComet": dict(sorted(by_comet.items())),
        "eventsByTarget": dict(sorted(by_target.items())),
        "eventsBySolarSystemBody": dict(sorted(by_solar_system_body.items())),
    }


def apply_event_limit(events: list[dict[str, Any]], max_events_per_comet: int) -> list[dict[str, Any]]:
    if max_events_per_comet <= 0:
        return events
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        comet, _ = event_participants(event)
        comet_id = str((comet or {}).get("id") or "unknown")
        grouped[comet_id].append(event)
    kept: list[dict[str, Any]] = []
    for rows in grouped.values():
        kept.extend(
            sorted(
                rows,
                key=lambda event: (
                    float(event["minimumSeparationDegrees"]),
                    str(event["eventTimeUTC"]),
                    str(event["id"]),
                ),
            )[:max_events_per_comet]
        )
    return kept


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
            "Clients that support this family should retain bundled or cached validated "
            "close-encounter shards and degrade gracefully when no compatible package exists."
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
    band_order = {band: index for index, band in enumerate(lunar.LATITUDE_BAND_ORDER)}

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
        raise RuntimeError("Comet close-encounter index schemaVersion must be 1.")
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
    model = package.get("generationModel") or {}
    if (model.get("dynamicStatic") or {}).get("status") != "generated":
        raise RuntimeError("Package must describe generated dynamic-static output.")
    if (model.get("dynamicDynamic") or {}).get("status") not in {"generated", "skipped"}:
        raise RuntimeError("Package must describe the dynamic-dynamic generation status.")

    window = package.get("window") or {}
    package_start = lunar.parse_utc_datetime(str(window.get("startUTC") or ""))
    package_end = lunar.parse_utc_datetime(str(window.get("endUTC") or ""))
    if package_end <= package_start:
        raise RuntimeError("Package window must be non-empty.")
    parameters = package.get("parameters") or {}
    threshold = lunar.finite_float(parameters.get("maxSeparationDegrees"))
    dynamic_threshold = lunar.finite_float(parameters.get("dynamicDynamicMaxSeparationDegrees"))
    if threshold is None or threshold <= 0:
        raise RuntimeError("Package maxSeparationDegrees must be positive.")
    if dynamic_threshold is None:
        dynamic_threshold = threshold
    if dynamic_threshold <= 0:
        raise RuntimeError("Package dynamicDynamicMaxSeparationDegrees must be positive.")

    subjects = package.get("subjects") or {}
    comet_ids = {
        str(row.get("id") or "")
        for row in subjects.get("comets") or []
        if isinstance(row, dict)
    }
    target_groups = {
        str(row.get("id") or ""): row
        for row in subjects.get("targetGroups") or []
        if isinstance(row, dict)
    }
    dynamic_body_ids = {
        str(row.get("id") or "")
        for row in subjects.get("dynamicBodies") or []
        if isinstance(row, dict)
    }
    if not comet_ids:
        raise RuntimeError("Index must contain comet subjects.")
    if not dynamic_body_ids:
        raise RuntimeError("Index must contain dynamic body subjects.")

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
            dynamic_threshold=dynamic_threshold,
            package_start=package_start,
            package_end=package_end,
            comet_ids=comet_ids,
            target_groups=target_groups,
            dynamic_body_ids=dynamic_body_ids,
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
    if counts["eventsByComet"] != package_counts.get("eventsByComet"):
        raise RuntimeError("Index eventsByComet does not match shards.")
    if counts["eventsByTarget"] != package_counts.get("eventsByTarget"):
        raise RuntimeError("Index eventsByTarget does not match shards.")
    if counts["eventsBySolarSystemBody"] != package_counts.get("eventsBySolarSystemBody"):
        raise RuntimeError("Index eventsBySolarSystemBody does not match shards.")
    if counts["eventsByType"] != package_counts.get("eventsByType"):
        raise RuntimeError("Index eventsByType does not match shards.")
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
    dynamic_threshold: float,
    package_start: dt.datetime,
    package_end: dt.datetime,
    comet_ids: set[str],
    target_groups: dict[str, dict[str, Any]],
    dynamic_body_ids: set[str],
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
        dynamic_threshold=dynamic_threshold,
        package_start=package_start,
        package_end=package_end,
        shard_start=shard_start,
        shard_end=shard_end,
        comet_ids=comet_ids,
        target_groups=target_groups,
        dynamic_body_ids=dynamic_body_ids,
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
    dynamic_threshold: float | None = None,
    package_start: dt.datetime,
    package_end: dt.datetime,
    shard_start: dt.datetime,
    shard_end: dt.datetime,
    comet_ids: set[str],
    target_groups: dict[str, dict[str, Any]],
    dynamic_body_ids: set[str],
) -> dict[str, Any]:
    previous_key = ("", "")
    seen_ids: set[str] = set()
    for event in events:
        if not isinstance(event, dict):
            raise RuntimeError("Comet close-encounter event rows must be objects.")
        event_id = str(event.get("id") or "")
        event_time_text = str(event.get("eventTimeUTC") or "")
        closest_text = str(event.get("closestApproachUTC") or "")
        if not event_id:
            raise RuntimeError("Comet close-encounter event is missing id.")
        if event_id in seen_ids:
            raise RuntimeError(f"Duplicate event ID within shard: {event_id}.")
        seen_ids.add(event_id)
        event_type = str(event.get("type") or "")
        if event.get("eventFamily") != EVENT_FAMILY or event_type not in EVENT_TYPES:
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
            raise RuntimeError("Comet close-encounter events must be sorted by time and ID.")
        previous_key = key

        event_threshold = (
            dynamic_threshold
            if event_type == COMET_DYNAMIC_EVENT_TYPE and dynamic_threshold is not None
            else threshold
        )
        separation = lunar.finite_float(event.get("minimumSeparationDegrees"))
        if separation is None or separation < 0 or separation > event_threshold + 0.000_001:
            raise RuntimeError(f"Event {event_id} separation is outside the package threshold.")
        comet, companion = event_participants(event)
        if comet is None or companion is None:
            raise RuntimeError(
                f"Event {event_id} must contain one comet and one companion participant."
            )
        comet_id = str(comet.get("id") or "")
        companion_id = str(companion.get("id") or "")
        if comet_id not in comet_ids:
            raise RuntimeError(f"Event {event_id} references unknown comet {comet_id}.")
        for participant in (comet, companion):
            validate_participant_coordinate(participant, event_id)
            magnitude = participant.get("magnitude")
            if magnitude is not None and lunar.finite_float(magnitude) is None:
                raise RuntimeError(f"Event {event_id} contains a non-finite magnitude.")
        if event_type == COMET_TARGET_EVENT_TYPE:
            if companion.get("kind") != "deepSkyObject":
                raise RuntimeError(f"Event {event_id} must contain a DSO companion.")
            target_group = target_groups.get(companion_id)
            if target_group is None:
                raise RuntimeError(f"Event {event_id} references unknown target group {companion_id}.")
            for key_name in ("catalogID", "displayName", "objectType"):
                if not str(companion.get(key_name) or "").strip():
                    raise RuntimeError(f"Event {event_id} target is missing {key_name}.")
            target_ids = target_group.get("targetIDs") or []
            if companion.get("catalogID") not in target_ids:
                raise RuntimeError(
                    f"Event {event_id} target catalogID is not canonical for {companion_id}."
                )
            if companion.get("displayName") != target_group.get("displayName"):
                raise RuntimeError(f"Event {event_id} target displayName disagrees with index.")
            if companion.get("objectType") != (target_group.get("objectType") or "Unknown"):
                raise RuntimeError(f"Event {event_id} target objectType disagrees with index.")
        else:
            if companion.get("kind") not in {"moon", "majorPlanet"}:
                raise RuntimeError(f"Event {event_id} must contain a Moon or major planet companion.")
            if companion_id not in dynamic_body_ids:
                raise RuntimeError(
                    f"Event {event_id} references unknown dynamic body {companion_id}."
                )
            if not str(companion.get("displayName") or "").strip():
                raise RuntimeError(f"Event {event_id} dynamic body is missing displayName.")
        expected_id = event_identifier(
            comet_id,
            companion_id,
            closest_time,
            event_type=event_type,
        )
        if event_id != expected_id:
            raise RuntimeError(
                f"Event {event_id} does not match stable ID convention {expected_id}."
            )
        source = event.get("source") or {}
        if source.get("packageFamily") != PACKAGE_FAMILY or source.get("recordID") != event_id:
            raise RuntimeError(f"Event {event_id} source metadata is incomplete.")
    return event_counts(events)


def event_participants(
    event: dict[str, Any],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    participants = event.get("participants")
    if not isinstance(participants, list) or len(participants) != 2:
        return None, None
    comets = [
        row for row in participants if isinstance(row, dict) and row.get("kind") == "comet"
    ]
    companions = [
        row
        for row in participants
        if isinstance(row, dict) and row.get("kind") in {"deepSkyObject", "moon", "majorPlanet"}
    ]
    if len(comets) != 1 or len(companions) != 1:
        return None, None
    return comets[0], companions[0]


def validate_participant_coordinate(participant: dict[str, Any], event_id: str) -> None:
    coordinate = participant.get("coordinate")
    if not isinstance(coordinate, dict):
        raise RuntimeError(f"Event {event_id} participant is missing coordinates.")
    ra = lunar.finite_float(coordinate.get("rightAscensionHours"))
    dec = lunar.finite_float(coordinate.get("declinationDegrees"))
    if ra is None or dec is None or not 0.0 <= ra < 24.0 or not -90.0 <= dec <= 90.0:
        raise RuntimeError(f"Event {event_id} participant coordinates are invalid.")


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


def event_identifier(
    comet_id: str,
    companion_id: str,
    timestamp: dt.datetime,
    *,
    event_type: str = COMET_TARGET_EVENT_TYPE,
) -> str:
    comet_component = identifier_component(comet_id)
    companion_component = identifier_component(companion_id)
    prefix = (
        "comet-dynamic-close-encounter"
        if event_type == COMET_DYNAMIC_EVENT_TYPE
        else "comet-target-close-encounter"
    )
    return (
        f"{prefix}-{comet_component}-{companion_component}-"
        f"{timestamp:%Y%m%d}"
    )


def identifier_component(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-") or "unknown"


def scalar_separation_degrees(
    ra_degrees_a: float,
    dec_degrees_a: float,
    ra_degrees_b: float,
    dec_degrees_b: float,
) -> float:
    return lunar.angular_separation_degrees(
        normalize_degrees(ra_degrees_a),
        dec_degrees_a,
        normalize_degrees(ra_degrees_b),
        dec_degrees_b,
    )


def interpolate(lhs: float, rhs: float, fraction: float) -> float:
    return lhs + ((rhs - lhs) * fraction)


def interpolate_optional(lhs: float | None, rhs: float | None, fraction: float) -> float | None:
    if lhs is None or rhs is None:
        return lhs if fraction < 0.5 else rhs
    return interpolate(lhs, rhs, fraction)


def normalize_degrees(value: float) -> float:
    return value % 360.0


def optional_text(value: object) -> str | None:
    text = str(value or "").strip()
    return text or None


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
    for path in shard_dir.glob("comet_close_encounters_*_v1.json"):
        path.unlink()


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
