#!/usr/bin/env python3
"""Build AstroGuide hosted lunar event metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import platform
import re
import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_APP_REPO = REPO_ROOT.parent / "DSOPlanneriOS"
DEFAULT_CATALOG_PATH = Path("App/Resources/Catalog/catalog.sqlite")
DEFAULT_PACKAGE_PATH = Path("v1/packages/lunar-events/lunar_event_metadata_v1.json")
DEFAULT_EPHEMERIS_CACHE = Path.home() / "Library/Caches/com.tophrchris.AstroGuide/lunar-events"
DEFAULT_EPHEMERIS = "de421.bsp"
METADATA_ORIGIN = "https://metadata.astroguide.space"
CACHE_TTL_SECONDS = 604800
PACKAGE_FAMILY = "lunarEvents"
PACKAGE_BASENAME = "lunar-events"
MOON_RADIUS_KM = 1737.4
SUPERSEDED_PACKAGE_FAMILIES = {"lunarClosePasses"}

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "darkSkyPlaces",
    "cometSnapshot",
    "planetCatalog",
    "lunarEvents",
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
PHASE_KEYS = {
    "New Moon": "newMoon",
    "First Quarter": "firstQuarter",
    "Full Moon": "fullMoon",
    "Last Quarter": "lastQuarter",
}
PLANET_SUBJECTS = [
    ("mercury", "Mercury", "mercury"),
    ("venus", "Venus", "venus"),
    ("mars", "Mars", "mars"),
    ("jupiter", "Jupiter", "jupiter barycenter"),
    ("saturn", "Saturn", "saturn barycenter"),
    ("uranus", "Uranus", "uranus barycenter"),
    ("neptune", "Neptune", "neptune barycenter"),
]
FORBIDDEN_LUNAR_LABEL_KEYS = {
    "super",
    "micro",
    "supermoon",
    "micromoon",
    "issuper",
    "ismicro",
}


@dataclass(frozen=True)
class TargetRecord:
    object_id: str
    primary_name: str
    catalog_name: str
    object_type: str
    constellation: str | None
    magnitude: float | None
    angular_size_arcmin: float | None
    angular_size_major_arcmin: float | None
    angular_size_minor_arcmin: float | None
    ra_hours: float
    dec_degrees: float
    aliases: tuple[str, ...]

    @property
    def ra_degrees(self) -> float:
        return normalize_degrees(self.ra_hours * 15.0)

    @property
    def display_name(self) -> str:
        return self.primary_name.strip() or self.catalog_name.strip() or self.object_id


@dataclass
class TargetGroup:
    group_id: str
    canonical: TargetRecord
    members: list[TargetRecord]


@dataclass(frozen=True)
class PlanetSubject:
    planet_id: str
    display_name: str
    ephemeris_key: str


@dataclass(frozen=True)
class SkyfieldModules:
    np: Any
    almanac: Any
    eclipselib: Any
    Loader: Any
    planetary_magnitude: Callable[[Any], float]
    versions: dict[str, str]


@dataclass(frozen=True)
class EclipseSegments:
    sun: Any
    earth_barycenter: Any
    earth: Any
    moon: Any


@dataclass(frozen=True)
class EclipseGeometry:
    closest_approach_degrees: float
    moon_radius_degrees: float
    penumbra_radius_degrees: float
    umbra_radius_degrees: float
    umbral_magnitude: float
    penumbral_magnitude: float


class UnionFind:
    def __init__(self, count: int) -> None:
        self.parent = list(range(count))
        self.rank = [0] * count

    def find(self, value: int) -> int:
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, lhs: int, rhs: int) -> None:
        lhs_root = self.find(lhs)
        rhs_root = self.find(rhs)
        if lhs_root == rhs_root:
            return
        if self.rank[lhs_root] < self.rank[rhs_root]:
            lhs_root, rhs_root = rhs_root, lhs_root
        self.parent[rhs_root] = lhs_root
        if self.rank[lhs_root] == self.rank[rhs_root]:
            self.rank[lhs_root] += 1


def parse_args() -> argparse.Namespace:
    today = dt.datetime.now(dt.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    default_end = today + dt.timedelta(days=365 * 2)
    parser = argparse.ArgumentParser(
        description=(
            "Build the hosted AstroGuide lunar event metadata package and refresh "
            "the stable manifest."
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
    parser.add_argument("--start-date", default=isoformat_z(today))
    parser.add_argument("--end-date", default=isoformat_z(default_end))
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--min-supported-app-version", default="1.3.7")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--max-separation-degrees", type=float, default=5.0)
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
        help="Validate an existing lunar event package and its manifest descriptor.",
    )
    args = parser.parse_args()
    if args.max_separation_degrees <= 0:
        raise SystemExit("--max-separation-degrees must be positive")
    if args.sample_step_minutes <= 0:
        raise SystemExit("--sample-step-minutes must be positive")
    if args.refine_step_minutes <= 0:
        raise SystemExit("--refine-step-minutes must be positive")
    if args.scan_padding_hours < 0:
        raise SystemExit("--scan-padding-hours cannot be negative")
    return args


def load_skyfield_modules() -> SkyfieldModules:
    try:
        import numpy as np
        import skyfield
        import jplephem
        from skyfield import almanac, eclipselib
        from skyfield.api import Loader
        from skyfield.magnitudelib import planetary_magnitude
    except ModuleNotFoundError as exc:
        missing = exc.name or "skyfield"
        raise SystemExit(
            f"Missing Python dependency '{missing}'. Install with:\n"
            "  python3 -m venv /tmp/astroguide-lunar-events-venv\n"
            "  /tmp/astroguide-lunar-events-venv/bin/python -m pip install "
            "-r scripts/requirements-lunar-events.txt\n"
            "Then rerun this script with that venv's python."
        ) from exc

    return SkyfieldModules(
        np=np,
        almanac=almanac,
        eclipselib=eclipselib,
        Loader=Loader,
        planetary_magnitude=planetary_magnitude,
        versions={
            "python": platform.python_version(),
            "skyfield": getattr(skyfield, "__version__", "unknown"),
            "numpy": getattr(np, "__version__", "unknown"),
            "jplephem": getattr(jplephem, "__version__", "unknown"),
        },
    )


def main() -> int:
    args = parse_args()
    output_path = repo_path(args.output)
    manifest_path = repo_path(args.manifest)

    if args.validate_only:
        package = read_json(output_path)
        validate_package(package)
        if manifest_path.exists():
            data = output_path.read_bytes()
            descriptor = descriptor_for_package(package, data, args, output_path)
            validate_manifest_descriptor(manifest_path, descriptor, data)
        print(f"Validated {repo_relative(output_path)}")
        return 0

    start = parse_utc_datetime(args.start_date)
    end = parse_utc_datetime(args.end_date)
    if end <= start:
        raise SystemExit("--end-date must be after --start-date")

    app_repo = args.app_repo.resolve()
    catalog_path = (args.catalog.resolve() if args.catalog else app_repo / DEFAULT_CATALOG_PATH).resolve()
    generated_at = args.generated_at or utc_now()
    package_version = args.package_version or f"{PACKAGE_BASENAME}-v1-{date_token(generated_at)}"

    sky = load_skyfield_modules()
    targets = load_targets(catalog_path)
    if not targets:
        raise SystemExit(f"No catalog targets with coordinates found in {catalog_path}")
    target_groups = build_target_groups(targets, args.dedupe_coordinate_arcmin)
    print(
        f"Loaded {len(targets)} coordinate targets, grouped into "
        f"{len(target_groups)} lunar event target groups.",
        flush=True,
    )

    load = sky.Loader(str(args.ephemeris_cache.resolve()))
    eph = load(args.ephemeris)
    ts = load.timescale()
    earth = eph["earth"]
    moon = eph["moon"]
    eclipse_segments = make_eclipse_segments(eph)

    scan_padding = dt.timedelta(hours=args.scan_padding_hours)
    scan_start = start - scan_padding
    scan_end = end + scan_padding
    sample_times = date_grid(scan_start, scan_end, dt.timedelta(minutes=args.sample_step_minutes))
    print(
        f"Scanning {len(sample_times)} coarse lunar samples from "
        f"{isoformat_z(scan_start)} to {isoformat_z(scan_end)}.",
        flush=True,
    )

    close_encounters, event_target_groups = compute_dso_close_encounters(
        sky=sky,
        target_groups=target_groups,
        sample_times=sample_times,
        start=start,
        end=end,
        max_separation_degrees=args.max_separation_degrees,
        coarse_step=dt.timedelta(minutes=args.sample_step_minutes),
        refine_step=dt.timedelta(minutes=args.refine_step_minutes),
        earth=earth,
        moon=moon,
        eph=eph,
        ts=ts,
    )
    planet_subjects = [
        PlanetSubject(planet_id=planet_id, display_name=display_name, ephemeris_key=ephemeris_key)
        for planet_id, display_name, ephemeris_key in PLANET_SUBJECTS
    ]
    planet_encounters = compute_planet_close_encounters(
        sky=sky,
        planet_subjects=planet_subjects,
        sample_times=sample_times,
        start=start,
        end=end,
        max_separation_degrees=args.max_separation_degrees,
        coarse_step=dt.timedelta(minutes=args.sample_step_minutes),
        refine_step=dt.timedelta(minutes=args.refine_step_minutes),
        earth=earth,
        moon=moon,
        eph=eph,
        ts=ts,
    )
    phase_markers = compute_phase_markers(sky, start, end, earth, moon, eph, ts)
    eclipse_events = compute_lunar_eclipses(
        sky=sky,
        start=start,
        end=end,
        earth=earth,
        moon=moon,
        eph=eph,
        ts=ts,
        eclipse_segments=eclipse_segments,
    )

    all_events = sorted(
        [*close_encounters, *planet_encounters, *phase_markers, *eclipse_events],
        key=lambda event: (str(event["eventTimeUTC"]), str(event["id"])),
    )
    metadata = load_catalog_metadata(catalog_path)
    package = build_package(
        package_version=package_version,
        generated_at=generated_at,
        start=start,
        end=end,
        catalog_path=catalog_path,
        app_repo=app_repo,
        catalog_metadata=metadata,
        target_groups=target_groups,
        event_target_groups=event_target_groups,
        planet_subjects=planet_subjects,
        events=all_events,
        args=args,
        sky_versions=sky.versions,
        ephemeris=eph,
    )
    validate_package(package)
    data = write_json(output_path, package, compact=True)
    descriptor = descriptor_for_package(package, data, args, output_path)
    if not args.skip_manifest:
        update_manifest(manifest_path, package["generatedAt"], descriptor)
        validate_manifest_descriptor(manifest_path, descriptor, data)

    counts = package["counts"]
    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}",
        flush=True,
    )
    print(
        "Events: "
        f"{counts['dsoCloseEncounters']} DSO close encounters, "
        f"{counts['planetCloseEncounters']} planet close encounters, "
        f"{counts['lunarEclipses']} lunar eclipses, "
        f"{counts['phaseMarkers']} phase markers.",
        flush=True,
    )
    return 0


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any], *, compact: bool = False) -> bytes:
    if compact:
        serialized = json.dumps(payload, separators=(",", ":"), ensure_ascii=True)
    else:
        serialized = json.dumps(payload, indent=2, ensure_ascii=True)
    data = (serialized + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(timestamp: str) -> str:
    return timestamp.split("T", maxsplit=1)[0].replace("-", "")


def parse_utc_datetime(value: str) -> dt.datetime:
    raw = value.strip()
    if not raw:
        raise SystemExit("Date values cannot be empty")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return dt.datetime.fromisoformat(raw).replace(tzinfo=dt.UTC)
    normalized = raw.replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise SystemExit(f"Invalid date or timestamp: {value}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.UTC)
    return parsed.astimezone(dt.UTC)


def load_targets(catalog_path: Path) -> list[TargetRecord]:
    if not catalog_path.exists():
        raise SystemExit(f"Catalog SQLite not found: {catalog_path}")
    connection = sqlite3.connect(catalog_path)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT object_id, primary_name, catalog_name, object_type, constellation,
                   magnitude, angular_size_arcmin, angular_size_maj_arcmin,
                   angular_size_min_arcmin, ra_hours, dec_degrees, aliases
            FROM deep_sky_objects
            WHERE ra_hours IS NOT NULL
              AND dec_degrees IS NOT NULL
            ORDER BY object_id
            """
        ).fetchall()
    finally:
        connection.close()

    targets: list[TargetRecord] = []
    for row in rows:
        ra_hours = finite_float(row["ra_hours"])
        dec_degrees = finite_float(row["dec_degrees"])
        if ra_hours is None or dec_degrees is None:
            continue
        targets.append(
            TargetRecord(
                object_id=str(row["object_id"] or "").strip(),
                primary_name=str(row["primary_name"] or "").strip(),
                catalog_name=str(row["catalog_name"] or "").strip(),
                object_type=str(row["object_type"] or "").strip(),
                constellation=optional_text(row["constellation"]),
                magnitude=finite_float(row["magnitude"]),
                angular_size_arcmin=finite_float(row["angular_size_arcmin"]),
                angular_size_major_arcmin=finite_float(row["angular_size_maj_arcmin"]),
                angular_size_minor_arcmin=finite_float(row["angular_size_min_arcmin"]),
                ra_hours=ra_hours,
                dec_degrees=dec_degrees,
                aliases=tuple(split_aliases(row["aliases"])),
            )
        )
    return targets


def load_catalog_metadata(catalog_path: Path) -> dict[str, str]:
    connection = sqlite3.connect(catalog_path)
    try:
        rows = connection.execute("SELECT key, value FROM metadata ORDER BY key").fetchall()
    finally:
        connection.close()
    return {str(key): str(value) for key, value in rows}


def build_target_groups(targets: list[TargetRecord], dedupe_coordinate_arcmin: float) -> list[TargetGroup]:
    if dedupe_coordinate_arcmin <= 0:
        return [
            TargetGroup(group_id=target.object_id, canonical=target, members=[target])
            for target in sorted(targets, key=target_sort_key)
        ]

    radius_degrees = dedupe_coordinate_arcmin / 60.0
    grid_size = max(radius_degrees, 0.001)
    ra_cell_count = max(1, math.ceil(360.0 / grid_size))
    grid: dict[tuple[int, int], list[int]] = defaultdict(list)
    union_find = UnionFind(len(targets))
    tokens_by_index = [identity_tokens(target) for target in targets]

    for index, target in enumerate(targets):
        ra_cell = int(math.floor(target.ra_degrees / grid_size)) % ra_cell_count
        dec_cell = int(math.floor((target.dec_degrees + 90.0) / grid_size))
        for ra_offset in (-1, 0, 1):
            for dec_offset in (-1, 0, 1):
                candidates = grid.get(((ra_cell + ra_offset) % ra_cell_count, dec_cell + dec_offset), [])
                for candidate_index in candidates:
                    if tokens_by_index[index].isdisjoint(tokens_by_index[candidate_index]):
                        continue
                    separation = angular_separation_degrees(
                        target.ra_degrees,
                        target.dec_degrees,
                        targets[candidate_index].ra_degrees,
                        targets[candidate_index].dec_degrees,
                    )
                    if separation <= radius_degrees:
                        union_find.union(index, candidate_index)
        grid[(ra_cell, dec_cell)].append(index)

    grouped_indices: dict[int, list[int]] = defaultdict(list)
    for index in range(len(targets)):
        grouped_indices[union_find.find(index)].append(index)

    groups: list[TargetGroup] = []
    used_ids: set[str] = set()
    for indices in grouped_indices.values():
        members = sorted((targets[index] for index in indices), key=target_sort_key)
        canonical = members[0]
        group_id = unique_group_id(canonical.object_id, used_ids)
        groups.append(TargetGroup(group_id=group_id, canonical=canonical, members=members))
    return sorted(groups, key=lambda group: target_sort_key(group.canonical))


def compute_dso_close_encounters(
    *,
    sky: SkyfieldModules,
    target_groups: list[TargetGroup],
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    coarse_step: dt.timedelta,
    refine_step: dt.timedelta,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
) -> tuple[list[dict[str, Any]], list[TargetGroup]]:
    np = sky.np
    target_ra = np.array([math.radians(group.canonical.ra_degrees) for group in target_groups])
    target_dec = np.array([math.radians(group.canonical.dec_degrees) for group in target_groups])
    target_sin_dec = np.sin(target_dec)
    target_cos_dec = np.cos(target_dec)
    min_cosine = math.cos(math.radians(max_separation_degrees))

    moon_ra, moon_dec = moon_radec_arrays(sky, earth, moon, ts, sample_times)
    hits_by_target: dict[int, list[tuple[int, float]]] = defaultdict(list)
    for sample_index, (moon_ra_radians, moon_dec_radians) in enumerate(zip(moon_ra, moon_dec)):
        cosines = (
            target_sin_dec * math.sin(moon_dec_radians)
            + target_cos_dec * math.cos(moon_dec_radians) * np.cos(target_ra - moon_ra_radians)
        )
        hit_indices = np.flatnonzero(cosines >= min_cosine)
        if hit_indices.size == 0:
            continue
        separations = np.degrees(np.arccos(np.clip(cosines[hit_indices], -1.0, 1.0)))
        for target_index, separation in zip(hit_indices.tolist(), separations.tolist()):
            hits_by_target[target_index].append((sample_index, float(separation)))

    print(f"Found coarse DSO hits for {len(hits_by_target)} target groups; refining.", flush=True)
    events: list[dict[str, Any]] = []
    event_target_indices: set[int] = set()
    seen_event_ids: dict[str, int] = defaultdict(int)
    for target_index, hits in sorted(hits_by_target.items()):
        target_group = target_groups[target_index]
        for group_hits in consecutive_hit_groups(hits):
            event = refine_dso_close_encounter(
                sky=sky,
                target_group=target_group,
                group_hits=group_hits,
                sample_times=sample_times,
                start=start,
                end=end,
                max_separation_degrees=max_separation_degrees,
                coarse_step=coarse_step,
                refine_step=refine_step,
                earth=earth,
                moon=moon,
                eph=eph,
                ts=ts,
            )
            if event is None:
                continue
            base_id = str(event["id"])
            seen_event_ids[base_id] += 1
            if seen_event_ids[base_id] > 1:
                event["id"] = f"{base_id}-{seen_event_ids[base_id]}"
            events.append(event)
            event_target_indices.add(target_index)

    event_target_groups = [group for index, group in enumerate(target_groups) if index in event_target_indices]
    return events, event_target_groups


def refine_dso_close_encounter(
    *,
    sky: SkyfieldModules,
    target_group: TargetGroup,
    group_hits: list[tuple[int, float]],
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    coarse_step: dt.timedelta,
    refine_step: dt.timedelta,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
) -> dict[str, Any] | None:
    bracket_start = max(sample_times[0], sample_times[group_hits[0][0]] - coarse_step)
    bracket_end = min(sample_times[-1], sample_times[group_hits[-1][0]] + coarse_step)
    if bracket_end <= bracket_start:
        return None
    fine_times = date_grid(bracket_start, bracket_end, refine_step)
    target = target_group.canonical
    separations, _, _ = target_moon_separations(sky, target, fine_times, earth, moon, ts)
    min_index = int(sky.np.argmin(separations))
    closest_time = refined_minimum_time(fine_times, separations, min_index, refine_step)
    closest_separation, closest_moon_ra, closest_moon_dec = scalar_target_moon_separation(
        sky,
        target,
        closest_time,
        earth,
        moon,
        ts,
    )
    if closest_time < start or closest_time >= end:
        return None
    if closest_separation > max_separation_degrees + 0.000_001:
        return None

    window = threshold_window(fine_times, separations, min_index, max_separation_degrees)
    moon_payload = moon_snapshot(sky, closest_time, earth, moon, eph, ts, closest_moon_ra, closest_moon_dec)
    magnitude_delta = magnitude_delta_vs_moon(target.magnitude, moon_payload.get("approximateVisualMagnitude"))
    subject = {
        "kind": "deepSkyObject",
        "id": target_group.group_id,
        "targetID": target.object_id,
        "magnitudeDeltaVsMoon": magnitude_delta,
    }

    return prune_none(
        {
            "id": event_identifier("lunar-close-encounter", target_group.group_id, closest_time),
            "type": "lunarCloseEncounter",
            "eventTimeUTC": isoformat_z(closest_time),
            "closestApproachUTC": isoformat_z(closest_time),
            "minimumSeparationDegrees": round(closest_separation, 4),
            "windowStartUTC": isoformat_z(window[0]) if window[0] else None,
            "windowEndUTC": isoformat_z(window[1]) if window[1] else None,
            "durationMinutes": duration_minutes(window[0], window[1]),
            "subject": prune_none(subject),
            "moon": close_encounter_moon_payload(moon_payload),
        }
    )


def compute_planet_close_encounters(
    *,
    sky: SkyfieldModules,
    planet_subjects: list[PlanetSubject],
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    coarse_step: dt.timedelta,
    refine_step: dt.timedelta,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for planet in planet_subjects:
        body = eph[planet.ephemeris_key]
        moon_ra, moon_dec = moon_radec_arrays(sky, earth, moon, ts, sample_times)
        planet_ra, planet_dec = apparent_radec_arrays(sky, earth, body, ts, sample_times)
        separations = separation_arrays(sky, moon_ra, moon_dec, planet_ra, planet_dec)
        hit_indices = [index for index, separation in enumerate(separations.tolist()) if separation <= max_separation_degrees]
        if not hit_indices:
            continue
        print(f"Found coarse Moon/{planet.display_name} hits; refining.", flush=True)
        for hit_group in consecutive_index_groups(hit_indices):
            event = refine_planet_close_encounter(
                sky=sky,
                planet=planet,
                body=body,
                hit_indices=hit_group,
                sample_times=sample_times,
                start=start,
                end=end,
                max_separation_degrees=max_separation_degrees,
                coarse_step=coarse_step,
                refine_step=refine_step,
                earth=earth,
                moon=moon,
                eph=eph,
                ts=ts,
            )
            if event is not None:
                events.append(event)
    return events


def refine_planet_close_encounter(
    *,
    sky: SkyfieldModules,
    planet: PlanetSubject,
    body: Any,
    hit_indices: list[int],
    sample_times: list[dt.datetime],
    start: dt.datetime,
    end: dt.datetime,
    max_separation_degrees: float,
    coarse_step: dt.timedelta,
    refine_step: dt.timedelta,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
) -> dict[str, Any] | None:
    bracket_start = max(sample_times[0], sample_times[hit_indices[0]] - coarse_step)
    bracket_end = min(sample_times[-1], sample_times[hit_indices[-1]] + coarse_step)
    fine_times = date_grid(bracket_start, bracket_end, refine_step)
    separations = planet_moon_separations(sky, body, fine_times, earth, moon, ts)
    min_index = int(sky.np.argmin(separations))
    closest_time = refined_minimum_time(fine_times, separations, min_index, refine_step)
    closest_separation = scalar_planet_moon_separation(sky, body, closest_time, earth, moon, ts)
    if closest_time < start or closest_time >= end:
        return None
    if closest_separation > max_separation_degrees + 0.000_001:
        return None

    window = threshold_window(fine_times, separations, min_index, max_separation_degrees)
    moon_payload = moon_snapshot(sky, closest_time, earth, moon, eph, ts)
    planet_payload = planet_snapshot(sky, planet, body, closest_time, earth, ts)
    subject_magnitude = planet_payload.get("visualMagnitude")
    magnitude_delta = magnitude_delta_vs_moon(subject_magnitude, moon_payload.get("approximateVisualMagnitude"))
    subject = {
        "kind": "majorPlanet",
        "id": planet.planet_id,
        "magnitude": subject_magnitude,
        "magnitudeDeltaVsMoon": magnitude_delta,
    }
    return prune_none(
        {
            "id": event_identifier("lunar-close-encounter", planet.planet_id, closest_time),
            "type": "lunarCloseEncounter",
            "eventTimeUTC": isoformat_z(closest_time),
            "closestApproachUTC": isoformat_z(closest_time),
            "minimumSeparationDegrees": round(closest_separation, 4),
            "windowStartUTC": isoformat_z(window[0]) if window[0] else None,
            "windowEndUTC": isoformat_z(window[1]) if window[1] else None,
            "durationMinutes": duration_minutes(window[0], window[1]),
            "subject": prune_none(subject),
            "moon": close_encounter_moon_payload(moon_payload),
        }
    )


def compute_phase_markers(
    sky: SkyfieldModules,
    start: dt.datetime,
    end: dt.datetime,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
) -> list[dict[str, Any]]:
    t0 = ts.from_datetime(start)
    t1 = ts.from_datetime(end)
    times, phase_indices = sky.almanac.find_discrete(t0, t1, sky.almanac.moon_phases(eph))
    events: list[dict[str, Any]] = []
    for sky_time, phase_index in zip(times, phase_indices):
        timestamp = sky_time.utc_datetime().replace(tzinfo=dt.UTC)
        phase_label = str(sky.almanac.MOON_PHASES[int(phase_index)])
        phase_key = PHASE_KEYS[phase_label]
        moon_payload = moon_snapshot(sky, timestamp, earth, moon, eph, ts)
        events.append(
            {
                "id": event_identifier("lunar-phase", phase_key, timestamp),
                "type": "lunarPhaseMarker",
                "eventTimeUTC": isoformat_z(timestamp),
                "phase": phase_key,
                "phaseLabel": phase_label,
                "moon": moon_payload,
            }
        )
    return events


def compute_lunar_eclipses(
    *,
    sky: SkyfieldModules,
    start: dt.datetime,
    end: dt.datetime,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
    eclipse_segments: EclipseSegments,
) -> list[dict[str, Any]]:
    t0 = ts.from_datetime(start)
    t1 = ts.from_datetime(end)
    times, codes, details = sky.eclipselib.lunar_eclipses(t0, t1, eph)
    events: list[dict[str, Any]] = []
    eclipse_names = sky.eclipselib.LUNAR_ECLIPSES
    for index, (sky_time, code) in enumerate(zip(times, codes)):
        maximum = sky_time.utc_datetime().replace(tzinfo=dt.UTC)
        kind = str(eclipse_names[int(code)])
        contacts = lunar_eclipse_contacts(sky, maximum, ts, eclipse_segments)
        geometry = lunar_eclipse_geometry(sky, ts.from_datetime(maximum), eclipse_segments)
        moon_payload = moon_snapshot(sky, maximum, earth, moon, eph, ts)
        contact_payload = {key: isoformat_z(value) for key, value in contacts.items() if value is not None}
        duration_payload = prune_none(
            {
                "penumbralMinutes": duration_minutes(contacts.get("p1"), contacts.get("p4")),
                "partialMinutes": duration_minutes(contacts.get("u1"), contacts.get("u4")),
                "totalMinutes": duration_minutes(contacts.get("u2"), contacts.get("u3")),
            }
        )
        events.append(
            prune_none(
                {
                    "id": event_identifier("lunar-eclipse", kind.lower(), maximum),
                    "type": "lunarEclipse",
                    "eventTimeUTC": isoformat_z(maximum),
                    "maximumEclipseUTC": isoformat_z(maximum),
                    "eclipseKind": kind.lower(),
                    "contactsUTC": contact_payload,
                    "durationMinutes": duration_payload,
                    "eclipseMagnitude": {
                        "umbral": round(float(details["umbral_magnitude"][index]), 4),
                        "penumbral": round(float(details["penumbral_magnitude"][index]), 4),
                    },
                    "geometry": {
                        "closestApproachDegrees": round(geometry.closest_approach_degrees, 6),
                        "moonRadiusDegrees": round(geometry.moon_radius_degrees, 6),
                        "penumbraRadiusDegrees": round(geometry.penumbra_radius_degrees, 6),
                        "umbraRadiusDegrees": round(geometry.umbra_radius_degrees, 6),
                    },
                    "moon": moon_payload,
                }
            )
        )
    return events


def moon_radec_arrays(
    sky: SkyfieldModules,
    earth: Any,
    moon: Any,
    ts: Any,
    times: list[dt.datetime],
) -> tuple[Any, Any]:
    return apparent_radec_arrays(sky, earth, moon, ts, times)


def apparent_radec_arrays(
    sky: SkyfieldModules,
    earth: Any,
    body: Any,
    ts: Any,
    times: list[dt.datetime],
) -> tuple[Any, Any]:
    skyfield_times = ts.from_datetimes(times)
    ra, dec, _ = earth.at(skyfield_times).observe(body).apparent().radec()
    return sky.np.asarray(ra.radians), sky.np.asarray(dec.radians)


def target_moon_separations(
    sky: SkyfieldModules,
    target: TargetRecord,
    times: list[dt.datetime],
    earth: Any,
    moon: Any,
    ts: Any,
) -> tuple[Any, Any, Any]:
    moon_ra, moon_dec = moon_radec_arrays(sky, earth, moon, ts, times)
    target_ra = math.radians(target.ra_degrees)
    target_dec = math.radians(target.dec_degrees)
    cosines = (
        math.sin(target_dec) * sky.np.sin(moon_dec)
        + math.cos(target_dec) * sky.np.cos(moon_dec) * sky.np.cos(target_ra - moon_ra)
    )
    separations = sky.np.degrees(sky.np.arccos(sky.np.clip(cosines, -1.0, 1.0)))
    return separations, sky.np.degrees(moon_ra), sky.np.degrees(moon_dec)


def scalar_target_moon_separation(
    sky: SkyfieldModules,
    target: TargetRecord,
    timestamp: dt.datetime,
    earth: Any,
    moon: Any,
    ts: Any,
) -> tuple[float, float, float]:
    separations, moon_ra_degrees, moon_dec_degrees = target_moon_separations(
        sky,
        target,
        [timestamp],
        earth,
        moon,
        ts,
    )
    return float(separations[0]), float(moon_ra_degrees[0]), float(moon_dec_degrees[0])


def planet_moon_separations(
    sky: SkyfieldModules,
    planet_body: Any,
    times: list[dt.datetime],
    earth: Any,
    moon: Any,
    ts: Any,
) -> Any:
    moon_ra, moon_dec = moon_radec_arrays(sky, earth, moon, ts, times)
    planet_ra, planet_dec = apparent_radec_arrays(sky, earth, planet_body, ts, times)
    return separation_arrays(sky, moon_ra, moon_dec, planet_ra, planet_dec)


def scalar_planet_moon_separation(
    sky: SkyfieldModules,
    planet_body: Any,
    timestamp: dt.datetime,
    earth: Any,
    moon: Any,
    ts: Any,
) -> float:
    return float(planet_moon_separations(sky, planet_body, [timestamp], earth, moon, ts)[0])


def separation_arrays(sky: SkyfieldModules, ra_a: Any, dec_a: Any, ra_b: Any, dec_b: Any) -> Any:
    cosines = sky.np.sin(dec_a) * sky.np.sin(dec_b) + sky.np.cos(dec_a) * sky.np.cos(dec_b) * sky.np.cos(ra_a - ra_b)
    return sky.np.degrees(sky.np.arccos(sky.np.clip(cosines, -1.0, 1.0)))


def moon_snapshot(
    sky: SkyfieldModules,
    timestamp: dt.datetime,
    earth: Any,
    moon: Any,
    eph: Any,
    ts: Any,
    moon_ra_degrees: float | None = None,
    moon_dec_degrees: float | None = None,
) -> dict[str, Any]:
    t = ts.from_datetime(timestamp)
    apparent = earth.at(t).observe(moon).apparent()
    ra, dec, distance = apparent.radec()
    ra_degrees = moon_ra_degrees if moon_ra_degrees is not None else float(ra.degrees)
    dec_degrees = moon_dec_degrees if moon_dec_degrees is not None else float(dec.degrees)
    distance_km = float(distance.km)
    phase_angle = float(sky.almanac.moon_phase(eph, t).degrees)
    illumination = float(sky.almanac.fraction_illuminated(eph, "moon", t))
    apparent_diameter_arcmin = math.degrees(2.0 * math.atan2(MOON_RADIUS_KM, distance_km)) * 60.0
    moon_magnitude = approximate_moon_visual_magnitude(phase_angle)
    return {
        "rightAscensionHours": round(normalize_degrees(ra_degrees) / 15.0, 6),
        "declinationDegrees": round(dec_degrees, 6),
        "distanceKm": round(distance_km),
        "apparentDiameterArcmin": round(apparent_diameter_arcmin, 3),
        "illuminationFraction": round(illumination, 4),
        "phaseAngleDegrees": round(phase_angle, 3),
        "phaseLabel": lunar_phase_label(phase_angle),
        "approximateVisualMagnitude": round(moon_magnitude, 2),
    }


def close_encounter_moon_payload(moon_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "illuminationFraction": moon_payload["illuminationFraction"],
        "phaseAngleDegrees": moon_payload["phaseAngleDegrees"],
    }


def planet_snapshot(
    sky: SkyfieldModules,
    planet: PlanetSubject,
    body: Any,
    timestamp: dt.datetime,
    earth: Any,
    ts: Any,
) -> dict[str, Any]:
    t = ts.from_datetime(timestamp)
    astrometric = earth.at(t).observe(body)
    apparent = astrometric.apparent()
    ra, dec, distance = apparent.radec()
    visual_magnitude = finite_float(sky.planetary_magnitude(astrometric))
    return prune_none(
        {
            "id": planet.planet_id,
            "displayName": planet.display_name,
            "rightAscensionHours": round(float(ra.hours), 6),
            "declinationDegrees": round(float(dec.degrees), 6),
            "distanceAU": round(float(distance.au), 6),
            "visualMagnitude": round_optional(visual_magnitude, 2),
        }
    )


def make_eclipse_segments(eph: Any) -> EclipseSegments:
    segments = {(segment.center, segment.target): segment.spk_segment for segment in eph.segments}
    return EclipseSegments(
        sun=segments[0, 10],
        earth_barycenter=segments[0, 3],
        earth=segments[3, 399],
        moon=segments[3, 301],
    )


def lunar_eclipse_geometry(
    sky: SkyfieldModules,
    time: Any,
    segments: EclipseSegments,
) -> EclipseGeometry:
    jd, fr = time.whole, time.tdb_fraction
    barycenter = segments.earth_barycenter.compute(jd, fr)
    earth = segments.earth.compute(jd, fr)
    moon = segments.moon.compute(jd, fr)
    sun = segments.sun.compute(jd, fr)

    earth_to_sun = sun - barycenter - earth
    moon_to_earth = earth - moon
    solar_radius_km = 696340.0
    moon_radius_km = 1737.1

    pi_m = sky.eclipselib.ERAD / 1e3 / sky.eclipselib.length_of(moon_to_earth)
    pi_s = sky.eclipselib.ERAD / 1e3 / sky.eclipselib.length_of(earth_to_sun)
    s_s = solar_radius_km / sky.eclipselib.length_of(earth_to_sun)
    closest_approach = sky.eclipselib.angle_between(earth_to_sun, moon_to_earth)
    moon_radius = math.asin(moon_radius_km / sky.eclipselib.length_of(moon_to_earth))
    pi_1 = 1.01 * pi_m
    penumbra_radius = pi_1 + pi_s + s_s
    umbra_radius = pi_1 + pi_s - s_s
    twice_radius = 2.0 * moon_radius
    umbral_magnitude = (umbra_radius + moon_radius - closest_approach) / twice_radius
    penumbral_magnitude = (penumbra_radius + moon_radius - closest_approach) / twice_radius
    return EclipseGeometry(
        closest_approach_degrees=math.degrees(float(closest_approach)),
        moon_radius_degrees=math.degrees(float(moon_radius)),
        penumbra_radius_degrees=math.degrees(float(penumbra_radius)),
        umbra_radius_degrees=math.degrees(float(umbra_radius)),
        umbral_magnitude=float(umbral_magnitude),
        penumbral_magnitude=float(penumbral_magnitude),
    )


def lunar_eclipse_contacts(
    sky: SkyfieldModules,
    maximum: dt.datetime,
    ts: Any,
    segments: EclipseSegments,
) -> dict[str, dt.datetime | None]:
    def margin_for(kind: str, timestamp: dt.datetime) -> float:
        geometry = lunar_eclipse_geometry(sky, ts.from_datetime(timestamp), segments)
        if kind == "penumbral":
            return geometry.penumbra_radius_degrees + geometry.moon_radius_degrees - geometry.closest_approach_degrees
        if kind == "umbral":
            return geometry.umbra_radius_degrees + geometry.moon_radius_degrees - geometry.closest_approach_degrees
        if kind == "total":
            return geometry.umbra_radius_degrees - geometry.moon_radius_degrees - geometry.closest_approach_degrees
        raise ValueError(kind)

    contacts: dict[str, dt.datetime | None] = {
        "p1": find_contact(maximum, "penumbral", -1, margin_for),
        "p4": find_contact(maximum, "penumbral", 1, margin_for),
        "u1": find_contact(maximum, "umbral", -1, margin_for),
        "u4": find_contact(maximum, "umbral", 1, margin_for),
        "u2": find_contact(maximum, "total", -1, margin_for),
        "u3": find_contact(maximum, "total", 1, margin_for),
    }
    return contacts


def find_contact(
    maximum: dt.datetime,
    kind: str,
    direction: int,
    margin_for: Callable[[str, dt.datetime], float],
) -> dt.datetime | None:
    if margin_for(kind, maximum) <= 0:
        return None
    step = dt.timedelta(minutes=20)
    cursor = maximum
    for _ in range(48):
        candidate = cursor + (step if direction > 0 else -step)
        if margin_for(kind, candidate) <= 0:
            return bisect_contact(kind, cursor, candidate, margin_for)
        cursor = candidate
    return None


def bisect_contact(
    kind: str,
    inside_time: dt.datetime,
    outside_time: dt.datetime,
    margin_for: Callable[[str, dt.datetime], float],
) -> dt.datetime:
    low = inside_time
    high = outside_time
    for _ in range(34):
        midpoint = low + ((high - low) / 2)
        if margin_for(kind, midpoint) > 0:
            low = midpoint
        else:
            high = midpoint
    return (low + ((high - low) / 2)).replace(microsecond=0)


def build_package(
    *,
    package_version: str,
    generated_at: str,
    start: dt.datetime,
    end: dt.datetime,
    catalog_path: Path,
    app_repo: Path,
    catalog_metadata: dict[str, str],
    target_groups: list[TargetGroup],
    event_target_groups: list[TargetGroup],
    planet_subjects: list[PlanetSubject],
    events: list[dict[str, Any]],
    args: argparse.Namespace,
    sky_versions: dict[str, str],
    ephemeris: Any,
) -> dict[str, Any]:
    counts_by_type = defaultdict(int)
    counts_by_subject_kind = defaultdict(int)
    for event in events:
        counts_by_type[str(event["type"])] += 1
        subject = event.get("subject")
        if isinstance(subject, dict):
            counts_by_subject_kind[str(subject.get("kind") or "unknown")] += 1

    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "generatedAt": generated_at,
        "eventTypes": [
            "lunarCloseEncounter",
            "lunarEclipse",
            "lunarPhaseMarker",
        ],
        "window": {
            "startUTC": isoformat_z(start),
            "endUTC": isoformat_z(end),
            "durationDays": round((end - start).total_seconds() / 86400.0, 3),
        },
        "source": {
            "name": "AstroGuide lunar event metadata pipeline",
            "generatedBy": "scripts/build_lunar_event_package.py",
            "catalogSourceRepo": "tophrchris/DSOPlanneriOS",
            "catalogSourceBranch": "release/1.3.7",
            "catalogPath": source_relative(catalog_path, app_repo),
            "catalogVersion": catalog_metadata.get("catalog_version"),
            "catalogFingerprint": catalog_metadata.get("catalog_fingerprint"),
            "catalogSHA256": sha256_file(catalog_path),
            "ephemeris": args.ephemeris,
            "ephemerisPath": str(getattr(ephemeris, "filename", args.ephemeris)),
            "ephemerisSource": "JPL Development Ephemeris loaded through Skyfield",
            "frame": "Geocentric apparent equatorial RA/Dec from Skyfield earth.at(t).observe(body).apparent().",
            "timescale": "UTC",
            "lunarEclipseModel": "Skyfield eclipselib lunar_eclipses with contact windows refined from the same Earth shadow geometry.",
            "planetMagnitudeModel": "Skyfield magnitudelib planetary_magnitude where finite.",
            "moonMagnitudeModel": "Approximate visual magnitude from lunar phase angle; intended only for relative context.",
            "versions": sky_versions,
        },
        "parameters": {
            "maxSeparationDegrees": args.max_separation_degrees,
            "sampleStepMinutes": args.sample_step_minutes,
            "refineStepMinutes": args.refine_step_minutes,
            "scanPaddingHours": args.scan_padding_hours,
            "dedupeCoordinateArcmin": args.dedupe_coordinate_arcmin,
            "planetSubjects": [planet.planet_id for planet in planet_subjects],
        },
        "counts": {
            "candidateTargetGroups": len(target_groups),
            "eventTargetGroups": len(event_target_groups),
            "dsoCloseEncounters": counts_by_subject_kind["deepSkyObject"],
            "planetCloseEncounters": counts_by_subject_kind["majorPlanet"],
            "lunarEclipses": counts_by_type["lunarEclipse"],
            "phaseMarkers": counts_by_type["lunarPhaseMarker"],
            "events": len(events),
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
            "targetGroups": [target_group_payload(group) for group in event_target_groups],
        },
        "events": events,
        "notes": [
            "Close encounters are global/geocentric baseline events; app-side filtering is responsible for site, selected time period, nighttime, altitude, observability, and equipment field of view.",
            "This package intentionally does not generate or store lunar distance category labels or booleans. App clients can derive display-only distance categories from full-moon distance or apparent diameter for visible rows.",
            "Lunar eclipses only are included; solar eclipses are intentionally out of scope for this package.",
        ],
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
            "Use cached validated lunar event metadata when available. Timeline consumers should "
            "degrade gracefully if no validated cached lunar event package is available."
        ),
    }


def update_manifest(manifest_path: Path, generated_at: str, descriptor: dict[str, Any]) -> None:
    manifest = read_json(manifest_path)
    descriptor_url = descriptor.get("packageURL")
    descriptors = {
        descriptor_key(entry): entry
        for entry in manifest.get("packages", [])
        if descriptor_key(entry) != descriptor_key(descriptor)
        and entry.get("family") not in SUPERSEDED_PACKAGE_FAMILIES
        and entry.get("packageURL") != descriptor_url
    }
    descriptors[descriptor_key(descriptor)] = descriptor
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(list(descriptors.values()))
    write_json(manifest_path, manifest)


def validate_package(package: dict[str, Any]) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Lunar event package schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Lunar event package family must be {PACKAGE_FAMILY}.")
    if not package.get("packageVersion"):
        raise RuntimeError("Lunar event package is missing packageVersion.")
    if not package.get("generatedAt"):
        raise RuntimeError("Lunar event package is missing generatedAt.")
    window = package.get("window") or {}
    parse_utc_datetime(str(window.get("startUTC") or ""))
    parse_utc_datetime(str(window.get("endUTC") or ""))
    events = package.get("events")
    if not isinstance(events, list) or not events:
        raise RuntimeError("Lunar event package contains no events.")

    previous_time = ""
    counts = defaultdict(int)
    for event in events:
        if not isinstance(event, dict):
            raise RuntimeError("Lunar event rows must be objects.")
        event_id = str(event.get("id") or "")
        event_type = str(event.get("type") or "")
        event_time = str(event.get("eventTimeUTC") or "")
        if not event_id:
            raise RuntimeError("Lunar event row is missing id.")
        if event_type not in {"lunarCloseEncounter", "lunarEclipse", "lunarPhaseMarker"}:
            raise RuntimeError(f"Unsupported lunar event type: {event_type}")
        parse_utc_datetime(event_time)
        if event_time < previous_time:
            raise RuntimeError("Lunar events must be sorted by eventTimeUTC.")
        previous_time = event_time
        counts[event_type] += 1
        if event_type == "lunarCloseEncounter":
            subject = event.get("subject") or {}
            if subject.get("kind") not in {"deepSkyObject", "majorPlanet"}:
                raise RuntimeError(f"Close encounter {event_id} has invalid subject kind.")
            if finite_float(event.get("minimumSeparationDegrees")) is None:
                raise RuntimeError(f"Close encounter {event_id} is missing minimum separation.")
        elif event_type == "lunarEclipse":
            if event.get("eclipseKind") not in {"penumbral", "partial", "total"}:
                raise RuntimeError(f"Lunar eclipse {event_id} has invalid kind.")
        elif event_type == "lunarPhaseMarker":
            if event.get("phase") not in {"newMoon", "firstQuarter", "fullMoon", "lastQuarter"}:
                raise RuntimeError(f"Phase marker {event_id} has invalid phase.")

    package_counts = package.get("counts") or {}
    expected_total = int(package_counts.get("events") or 0)
    if expected_total != len(events):
        raise RuntimeError(f"Package counts.events mismatch: expected {expected_total}, got {len(events)}.")
    if int(package_counts.get("lunarEclipses") or 0) != counts["lunarEclipse"]:
        raise RuntimeError("Package lunar eclipse count mismatch.")
    if int(package_counts.get("phaseMarkers") or 0) != counts["lunarPhaseMarker"]:
        raise RuntimeError("Package phase marker count mismatch.")
    assert_no_forbidden_lunar_labels(package)


def validate_manifest_descriptor(manifest_path: Path, descriptor: dict[str, Any], data: bytes) -> None:
    manifest = read_json(manifest_path)
    matches = [entry for entry in manifest.get("packages", []) if descriptor_key(entry) == descriptor_key(descriptor)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one manifest descriptor for {descriptor['family']}, found {len(matches)}.")
    entry = matches[0]
    if entry.get("packageVersion") != descriptor["packageVersion"]:
        raise RuntimeError("Manifest packageVersion does not match package.")
    if entry.get("payloadSchemaVersion") != descriptor["payloadSchemaVersion"]:
        raise RuntimeError("Manifest payloadSchemaVersion does not match package.")
    if int(entry.get("byteSize") or 0) != len(data):
        raise RuntimeError("Manifest byteSize does not match package.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != hashlib.sha256(data).hexdigest():
        raise RuntimeError("Manifest checksum does not match package.")


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


def refined_minimum_time(
    times: list[dt.datetime],
    values: Any,
    min_index: int,
    step: dt.timedelta,
) -> dt.datetime:
    closest_time = times[min_index]
    if 0 < min_index < len(times) - 1:
        offset_fraction = quadratic_minimum_offset(
            float(values[min_index - 1]),
            float(values[min_index]),
            float(values[min_index + 1]),
        )
        if offset_fraction is not None:
            closest_time = closest_time + (step * offset_fraction)
    return closest_time.replace(microsecond=0)


def threshold_window(
    times: list[dt.datetime],
    values: Any,
    min_index: int,
    threshold: float,
) -> tuple[dt.datetime | None, dt.datetime | None]:
    start_time: dt.datetime | None = times[0] if float(values[0]) <= threshold else None
    end_time: dt.datetime | None = times[-1] if float(values[-1]) <= threshold else None

    for index in range(min_index, 0, -1):
        if float(values[index - 1]) > threshold >= float(values[index]):
            start_time = interpolate_threshold_time(
                times[index - 1],
                float(values[index - 1]),
                times[index],
                float(values[index]),
                threshold,
            )
            break
    for index in range(min_index, len(times) - 1):
        if float(values[index]) <= threshold < float(values[index + 1]):
            end_time = interpolate_threshold_time(
                times[index],
                float(values[index]),
                times[index + 1],
                float(values[index + 1]),
                threshold,
            )
            break
    return start_time, end_time


def interpolate_threshold_time(
    time_a: dt.datetime,
    value_a: float,
    time_b: dt.datetime,
    value_b: float,
    threshold: float,
) -> dt.datetime:
    if value_a == value_b:
        return time_a
    fraction = (threshold - value_a) / (value_b - value_a)
    fraction = max(0.0, min(1.0, fraction))
    return (time_a + ((time_b - time_a) * fraction)).replace(microsecond=0)


def quadratic_minimum_offset(previous: float, current: float, next_value: float) -> float | None:
    denominator = previous - (2.0 * current) + next_value
    if abs(denominator) < 1.0e-12:
        return None
    offset = 0.5 * (previous - next_value) / denominator
    return max(-1.0, min(1.0, offset))


def consecutive_hit_groups(hits: list[tuple[int, float]]) -> Iterable[list[tuple[int, float]]]:
    if not hits:
        return
    current: list[tuple[int, float]] = [hits[0]]
    previous_index = hits[0][0]
    for hit in hits[1:]:
        sample_index = hit[0]
        if sample_index == previous_index + 1:
            current.append(hit)
        else:
            yield current
            current = [hit]
        previous_index = sample_index
    yield current


def consecutive_index_groups(indices: list[int]) -> Iterable[list[int]]:
    if not indices:
        return
    current = [indices[0]]
    previous = indices[0]
    for index in indices[1:]:
        if index == previous + 1:
            current.append(index)
        else:
            yield current
            current = [index]
        previous = index
    yield current


def date_grid(start: dt.datetime, end: dt.datetime, step: dt.timedelta) -> list[dt.datetime]:
    values: list[dt.datetime] = []
    cursor = start
    while cursor <= end:
        values.append(cursor)
        cursor += step
    if not values or values[-1] < end:
        values.append(end)
    return values


def target_group_payload(group: TargetGroup) -> dict[str, Any]:
    canonical = group.canonical
    aliases = sorted(
        {
            alias
            for member in group.members
            for alias in (member.object_id, member.primary_name, member.catalog_name, *member.aliases)
            if alias.strip()
        },
        key=lambda value: value.lower(),
    )
    return {
        "id": group.group_id,
        "displayName": canonical.display_name,
        "catalogName": canonical.catalog_name,
        "objectType": canonical.object_type,
        "constellation": canonical.constellation,
        "magnitude": round_optional(canonical.magnitude, 2),
        "angularSizeArcmin": round_optional(canonical.angular_size_arcmin, 3),
        "angularSizeMajorArcmin": round_optional(canonical.angular_size_major_arcmin, 3),
        "angularSizeMinorArcmin": round_optional(canonical.angular_size_minor_arcmin, 3),
        "rightAscensionHours": round(canonical.ra_hours, 8),
        "declinationDegrees": round(canonical.dec_degrees, 8),
        "targetIDs": [member.object_id for member in group.members],
        "aliases": aliases,
    }


def event_identifier(prefix: str, subject_id: str, timestamp: dt.datetime) -> str:
    timestamp_component = timestamp.strftime("%Y%m%dT%H%M%SZ")
    subject_component = re.sub(r"[^A-Za-z0-9_-]+", "-", subject_id).strip("-")
    return f"{prefix}-{timestamp_component}-{subject_component}"


def lunar_phase_label(phase_angle_degrees: float) -> str:
    phase = normalize_degrees(phase_angle_degrees)
    if phase < 22.5 or phase >= 337.5:
        return "New Moon"
    if phase < 67.5:
        return "Waxing Crescent"
    if phase < 112.5:
        return "First Quarter"
    if phase < 157.5:
        return "Waxing Gibbous"
    if phase < 202.5:
        return "Full Moon"
    if phase < 247.5:
        return "Waning Gibbous"
    if phase < 292.5:
        return "Last Quarter"
    return "Waning Crescent"


def approximate_moon_visual_magnitude(phase_angle_degrees: float) -> float:
    full_moon_angle = abs(180.0 - normalize_degrees(phase_angle_degrees))
    return -12.73 + (0.026 * full_moon_angle) + (4.0e-9 * full_moon_angle**4)


def magnitude_delta_vs_moon(subject_magnitude: Any, moon_magnitude: Any) -> float | None:
    subject = finite_float(subject_magnitude)
    moon = finite_float(moon_magnitude)
    if subject is None or moon is None:
        return None
    return round(subject - moon, 2)


def identity_tokens(target: TargetRecord) -> set[str]:
    values = [target.object_id, target.primary_name, target.catalog_name, *target.aliases]
    return {token for value in values for token in normalized_identity_tokens(value)}


def normalized_identity_tokens(value: str | None) -> set[str]:
    if value is None:
        return set()
    normalized = normalize_identity(value)
    tokens = {normalized} if normalized else set()
    for part in re.split(r"[\s,;/|()\\[\\]{}]+", value):
        part_normalized = normalize_identity(part)
        if part_normalized:
            tokens.add(part_normalized)
    return tokens


def normalize_identity(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def target_sort_key(target: TargetRecord) -> tuple[int, float, int, str]:
    object_id = target.object_id.upper()
    if re.fullmatch(r"M\d+[A-Z]?", object_id):
        rank = 0
    elif re.fullmatch(r"NGC\d+[A-Z]?", object_id):
        rank = 1
    elif re.fullmatch(r"IC\d+[A-Z]?", object_id):
        rank = 2
    elif re.fullmatch(r"SH2-\d+[A-Z]?", object_id):
        rank = 3
    else:
        rank = 4
    magnitude = target.magnitude if target.magnitude is not None else 99.0
    return rank, magnitude, len(object_id), object_id


def unique_group_id(candidate: str, used_ids: set[str]) -> str:
    normalized = candidate.strip() or "target"
    if normalized not in used_ids:
        used_ids.add(normalized)
        return normalized
    suffix = 2
    while f"{normalized}-{suffix}" in used_ids:
        suffix += 1
    resolved = f"{normalized}-{suffix}"
    used_ids.add(resolved)
    return resolved


def split_aliases(raw_aliases: str | None) -> list[str]:
    if not raw_aliases:
        return []
    return [alias.strip() for alias in str(raw_aliases).split("|") if alias.strip()]


def optional_text(value: object) -> str | None:
    text = str(value or "").strip()
    return text or None


def finite_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def round_optional(value: float | None, digits: int) -> float | None:
    return round(value, digits) if value is not None else None


def angular_separation_degrees(
    ra_degrees_a: float,
    dec_degrees_a: float,
    ra_degrees_b: float,
    dec_degrees_b: float,
) -> float:
    ra_a = math.radians(ra_degrees_a)
    dec_a = math.radians(dec_degrees_a)
    ra_b = math.radians(ra_degrees_b)
    dec_b = math.radians(dec_degrees_b)
    cosine = (
        math.sin(dec_a) * math.sin(dec_b)
        + math.cos(dec_a) * math.cos(dec_b) * math.cos(ra_a - ra_b)
    )
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def normalize_degrees(value: float) -> float:
    remainder = value % 360.0
    return remainder if remainder >= 0 else remainder + 360.0


def duration_minutes(start: dt.datetime | None, end: dt.datetime | None) -> int | None:
    if start is None or end is None or end < start:
        return None
    return int(round((end - start).total_seconds() / 60.0))


def isoformat_z(value: dt.datetime) -> str:
    return value.astimezone(dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


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


def source_relative(path: Path, source_root: Path) -> str:
    try:
        return str(path.resolve().relative_to(source_root.resolve()))
    except ValueError:
        return repo_relative(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prune_none(value: dict[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if item is not None}


def assert_no_forbidden_lunar_labels(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            normalized_key = re.sub(r"[^a-z0-9]+", "", str(key).lower())
            if normalized_key in FORBIDDEN_LUNAR_LABEL_KEYS:
                raise RuntimeError(f"Forbidden lunar distance label key at {path}.{key}")
            assert_no_forbidden_lunar_labels(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            assert_no_forbidden_lunar_labels(item, f"{path}[{index}]")
    elif isinstance(value, str):
        normalized_value = re.sub(r"[^a-z0-9]+", "", value.lower())
        if "supermoon" in normalized_value or "micromoon" in normalized_value:
            raise RuntimeError(f"Forbidden lunar distance label value at {path}")


if __name__ == "__main__":
    raise SystemExit(main())
