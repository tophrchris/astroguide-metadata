#!/usr/bin/env python3
"""Build lazy comet detail metadata enriched from Aerith."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import math
import re
import time
import urllib.request
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
METADATA_ORIGIN = "https://metadata.astroguide.space"
PACKAGE_FAMILY = "cometDetailMetadata"
PACKAGE_PATH = Path("v1/packages/comet-details/comet_detail_metadata_v1.json")
SHARD_DIR = Path("v1/packages/comet-details/shards")
ASSET_DIR = Path("v1/assets/comets/aerith")
DEFAULT_COMET_SNAPSHOT = REPO_ROOT / "v1/packages/comets/comet_snapshot_v1.json"
DEFAULT_AERITH_SOURCE = REPO_ROOT / "sources/comets/aerith_current_comets_v1.json"
DEFAULT_ORBIT_GEOMETRY = REPO_ROOT / "v1/packages/comet-orbit-geometry/comet_orbit_geometry_v1.json"
CACHE_TTL_SECONDS = 604800
PERMISSION_RECEIVED = "2026-08-15"
USER_AGENT = (
    "AstroGuide metadata comet detail builder/1.0 "
    "(Aerith permission received 2026-08-15; https://astroguide.space)"
)
DEFAULT_BRIGHTNESS_LOOKBACK_DAYS = 90
DEFAULT_USEFUL_MAGNITUDE_LIMIT = 16.0
AERITH_USEFUL_ALTITUDE_DEGREES = 10.0
AERITH_USEFUL_ELONGATION_DEGREES = 30.0
TREND_STABLE_DELTA_MAGNITUDE = 0.2
TREND_NOTABLE_DELTA_MAGNITUDE = 1.0
ORBITAL_FAMILIES = {
    "jupiter_family",
    "halley_type",
    "long_period",
    "oort_cloud",
    "main_belt",
    "interstellar",
    "unknown",
}
INCLINATION_CLASSES = {
    "low_inclination",
    "moderate_inclination",
    "high_inclination",
    "retrograde",
    "unknown",
}
RETURN_STATUSES = {
    "returning",
    "first_observed_return",
    "dynamically_new",
    "non_periodic_or_uncertain",
    "unknown",
}
VISIBILITY_STATES = {
    "current",
    "comingSoon",
    "futureVisible",
    "notCurrentlyUseful",
    "unknown",
}
TREND_DIRECTIONS = {"brightening", "fading", "stable", "uncertain"}

FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
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
MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build lazy Aerith-backed comet detail metadata shards."
    )
    parser.add_argument("--source-package", type=Path, default=DEFAULT_COMET_SNAPSHOT)
    parser.add_argument("--aerith-source", type=Path, default=DEFAULT_AERITH_SOURCE)
    parser.add_argument("--orbit-geometry", type=Path, default=DEFAULT_ORBIT_GEOMETRY)
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--manifest", type=Path, default=REPO_ROOT / "v1/channels/stable/manifest.json")
    parser.add_argument("--min-supported-app-version", default="1.4.1")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--brightness-lookback-days", type=int, default=DEFAULT_BRIGHTNESS_LOOKBACK_DAYS)
    parser.add_argument("--useful-magnitude-limit", type=float, default=DEFAULT_USEFUL_MAGNITUDE_LIMIT)
    parser.add_argument("--image-limit", type=int, default=1)
    parser.add_argument("--max-image-bytes", type=int, default=500_000)
    parser.add_argument("--fetch-delay-seconds", type=float, default=0.5)
    parser.add_argument("--skip-images", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the checked-in comet detail index, shards, manifest descriptor, and cached-image invariants.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def date_token(generated_at: str) -> str:
    return generated_at.split("T", maxsplit=1)[0].replace("-", "")


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def normalize_comet_key(value: str) -> str:
    text = html.unescape(str(value or "")).strip().upper()
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
    stable_without_prefix = str(seed.get("stableID") or "").removeprefix("COMET:").replace("_", "/")
    values = [
        stable_without_prefix,
        str(seed.get("designation") or ""),
        str(seed.get("displayName") or ""),
        str(seed.get("shortName") or ""),
    ]
    aliases = seed.get("aliases") or []
    if isinstance(aliases, list):
        values.extend(str(alias) for alias in aliases)
    return {key for key in (normalize_comet_key(value) for value in values) if key}


def safe_identifier(stable_id: str) -> str:
    value = stable_id.replace(":", "_").replace("/", "_").replace(" ", "_")
    return re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_") or "COMET"


def source_page_date(aerith_source: dict[str, Any]) -> dt.date:
    dates: list[dt.date] = []
    for page in aerith_source.get("pages") or []:
        try:
            dates.append(dt.date.fromisoformat(str(page.get("pageDate"))))
        except ValueError:
            continue
    return max(dates) if dates else dt.date.today()


def parse_date(value: Any) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


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


def finite_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def date_from_report_text(value: str, reference_date: dt.date) -> str | None:
    match = re.search(r"\b([A-Za-z]{3,9})\.?\s+(\d{1,2})\b", value or "")
    if not match:
        return None
    month = MONTHS.get(match.group(1).lower().rstrip("."))
    if month is None:
        return None
    year = reference_date.year
    if month - reference_date.month < -6:
        year += 1
    elif month - reference_date.month > 6:
        year -= 1
    try:
        return dt.date(year, month, int(match.group(2))).isoformat()
    except ValueError:
        return None


def build_observations(entry: dict[str, Any], reference_date: dt.date) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    seen: set[tuple[str, float, str]] = set()
    commentaries = [
        str(value).strip()
        for value in entry.get("sourceCommentaries") or []
        if str(value).strip()
    ]
    source_url = entry.get("detailURL")

    def append_observation(row: dict[str, Any]) -> None:
        key = (str(row.get("date") or ""), float(row.get("magnitude")), str(row.get("qualifier") or ""))
        if key in seen:
            return
        seen.add(key)
        observations.append(row)

    for index, report in enumerate(entry.get("reportedMagnitudes") or [], start=1):
        date = date_from_report_text(str(report.get("reportedDateText") or ""), reference_date)
        magnitude = report.get("magnitude")
        if date is None or magnitude is None:
            continue
        row: dict[str, Any] = {
            "id": f"{entry['normalizedDesignation']}-{date}-report-{index}",
            "date": date,
            "magnitude": float(magnitude),
            "qualifier": "reported",
            "estimateKind": "reported",
            "isProjection": False,
            "sourceLabel": "Aerith reported magnitude",
            "sourceURL": source_url,
        }
        commentary = commentary_for_report(report, commentaries)
        if commentary:
            row["commentary"] = commentary
        append_observation(row)

    rows_by_hemisphere = entry.get("weeklyRowsByHemisphere") or {}
    for hemisphere in sorted(rows_by_hemisphere):
        page_url = (entry.get("sourcePageURLs") or {}).get(hemisphere) or source_url
        for index, weekly in enumerate(rows_by_hemisphere.get(hemisphere) or [], start=1):
            date = weekly.get("date")
            magnitude = weekly.get("magnitude")
            if not date or magnitude is None:
                continue
            parsed_date = parse_date(date)
            append_observation(
                {
                    "id": f"{entry['normalizedDesignation']}-{date}-{hemisphere}-weekly-{index}",
                    "date": date,
                    "magnitude": float(magnitude),
                    "qualifier": "weekly-estimate",
                    "estimateKind": "projection" if parsed_date and parsed_date > reference_date else "current",
                    "isProjection": bool(parsed_date and parsed_date > reference_date),
                    "sourceLabel": f"Aerith weekly bright-comet table ({hemisphere})",
                    "sourceURL": page_url,
                }
            )

    observations.sort(key=lambda row: (row["date"], row["id"]))
    annotate_deltas(observations)
    return observations


def commentary_for_report(
    report: dict[str, Any],
    commentaries: list[str],
) -> str | None:
    if not commentaries:
        return None
    reported_date = str(report.get("reportedDateText") or "").lower().replace(".", "")
    for commentary in commentaries:
        normalized = commentary.lower().replace(".", "")
        if reported_date and reported_date in normalized:
            return commentary
    return commentaries[0]


def annotate_deltas(observations: list[dict[str, Any]]) -> None:
    previous: dict[str, Any] | None = None
    for row in observations:
        magnitude = row.get("magnitude")
        if magnitude is None:
            continue
        if previous is not None and previous.get("magnitude") is not None:
            delta = round(float(magnitude) - float(previous["magnitude"]), 2)
            row["magnitudeDelta"] = delta
            if abs(delta) >= 1.0:
                row["isSignificant"] = True
                if delta < 0:
                    row["significanceKind"] = "outburst"
                    row.setdefault(
                        "interpretation",
                        f"Brightened {abs(delta):.1f} mag between Aerith magnitude reports or estimates.",
                    )
                else:
                    row["significanceKind"] = "fade"
                    row.setdefault(
                        "interpretation",
                        f"Faded {abs(delta):.1f} mag between Aerith magnitude reports or estimates.",
                    )
        commentary = str(row.get("commentary") or row.get("interpretation") or "").lower()
        if "outburst" in commentary or "brighten" in commentary:
            row["isSignificant"] = True
            row.setdefault("significanceKind", "outburst")
        previous = row


def chart_points(
    observations: list[dict[str, Any]],
    *,
    lookback_days: int,
) -> list[dict[str, Any]]:
    dated = [
        (parse_date(row.get("date")), row)
        for row in observations
        if parse_date(row.get("date")) is not None
    ]
    if not dated:
        return []
    latest = max(date for date, _ in dated if date is not None)
    cutoff = latest - dt.timedelta(days=max(0, lookback_days))
    window = [row for date, row in dated if date is not None and date >= cutoff]
    return [dict(row) for row in window]


def build_brightness_chart(
    observations: list[dict[str, Any]],
    *,
    lookback_days: int,
) -> dict[str, Any]:
    points = chart_points(observations, lookback_days=lookback_days)
    dates = [parse_date(point.get("date")) for point in points]
    resolved_dates = [date for date in dates if date is not None]
    start = min(resolved_dates) if resolved_dates else None
    end = max(resolved_dates) if resolved_dates else None
    return {
        "lookbackDays": max(0, lookback_days),
        "availableStartDate": start.isoformat() if start else None,
        "availableEndDate": end.isoformat() if end else None,
        "actualDaySpan": (end - start).days if start and end else 0,
        "pointCount": len(points),
        "containsProjection": any(bool(point.get("isProjection")) for point in points),
        "containsReportedObservation": any(point.get("qualifier") == "reported" for point in points),
        "points": points,
    }


def build_brightness_trend(observations: list[dict[str, Any]]) -> dict[str, Any]:
    dated = [
        (parse_date(row.get("date")), row)
        for row in observations
        if parse_date(row.get("date")) is not None and row.get("magnitude") is not None
    ]
    dated.sort(key=lambda item: (item[0] or dt.date.min, str(item[1].get("id") or "")))
    notable_ids = [
        str(row.get("id"))
        for _, row in dated
        if row.get("isSignificant") and row.get("id")
    ]
    if not dated:
        return {
            "currentMagnitude": None,
            "currentDate": None,
            "comparisonMagnitude": None,
            "comparisonDate": None,
            "comparisonWindowDays": None,
            "deltaMagnitude": None,
            "direction": "uncertain",
            "isNotable": False,
            "notableChangeThresholdMagnitude": TREND_NOTABLE_DELTA_MAGNITUDE,
            "notableObservationIDs": notable_ids,
        }

    current_date, current = dated[-1]
    comparison_date: dt.date | None = None
    comparison: dict[str, Any] | None = None
    for candidate_date, candidate in reversed(dated[:-1]):
        if candidate.get("magnitude") is not None:
            comparison_date = candidate_date
            comparison = candidate
            break

    current_magnitude = finite_float(current.get("magnitude"))
    comparison_magnitude = finite_float(comparison.get("magnitude")) if comparison else None
    delta: float | None = None
    direction = "uncertain"
    is_notable = False
    window_days: int | None = None
    if current_magnitude is not None and comparison_magnitude is not None:
        delta = round(current_magnitude - comparison_magnitude, 2)
        if current_date and comparison_date:
            window_days = (current_date - comparison_date).days
        if abs(delta) <= TREND_STABLE_DELTA_MAGNITUDE:
            direction = "stable"
        elif delta < 0:
            direction = "brightening"
        else:
            direction = "fading"
        is_notable = abs(delta) >= TREND_NOTABLE_DELTA_MAGNITUDE

    return {
        "currentMagnitude": current_magnitude,
        "currentDate": current_date.isoformat() if current_date else None,
        "currentPointID": current.get("id"),
        "comparisonMagnitude": comparison_magnitude,
        "comparisonDate": comparison_date.isoformat() if comparison_date else None,
        "comparisonPointID": comparison.get("id") if comparison else None,
        "comparisonWindowDays": window_days,
        "deltaMagnitude": delta,
        "direction": direction,
        "isNotable": is_notable,
        "notableChangeThresholdMagnitude": TREND_NOTABLE_DELTA_MAGNITUDE,
        "notableObservationIDs": notable_ids,
    }


def orbit_records_by_id(orbit_geometry: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not isinstance(orbit_geometry, dict):
        return {}
    return {
        str(record.get("stableID")): record
        for record in orbit_geometry.get("records") or []
        if isinstance(record, dict) and record.get("stableID")
    }


def orbital_family(seed: dict[str, Any], orbit: dict[str, Any] | None) -> str:
    designation = str(seed.get("designation") or "").strip().upper()
    code = str((orbit or {}).get("jplOrbitClassCode") or "").strip().upper()
    orbit_class = str(seed.get("orbitClass") or (orbit or {}).get("orbitClass") or "").lower()
    if designation.startswith("I/") or code in {"INT", "IEO"}:
        return "interstellar"
    if code == "MBC":
        return "main_belt"
    if code == "HTC":
        return "halley_type"
    if code == "JFC":
        return "jupiter_family"
    if "long-period" in orbit_class or designation.startswith("C/"):
        return "long_period"
    return "unknown"


def inclination_class(orbit: dict[str, Any] | None) -> str:
    inclination = finite_float((orbit or {}).get("inclinationDegrees"))
    if inclination is None:
        return "unknown"
    if inclination >= 90.0:
        return "retrograde"
    if inclination < 20.0:
        return "low_inclination"
    if inclination < 60.0:
        return "moderate_inclination"
    return "high_inclination"


def return_status(seed: dict[str, Any], orbit: dict[str, Any] | None) -> str:
    designation = str(seed.get("designation") or "").strip().upper()
    orbit_class = str(seed.get("orbitClass") or (orbit or {}).get("orbitClass") or "").lower()
    eccentricity = finite_float((orbit or {}).get("eccentricity"))
    period_days = finite_float((orbit or {}).get("orbitalPeriodDays"))
    if re.match(r"^\d+P\b", designation):
        return "returning"
    if designation.startswith("P/") and period_days is not None and (eccentricity is None or eccentricity < 1.0):
        return "first_observed_return"
    if designation.startswith("C/") or "non-periodic" in orbit_class or eccentricity is not None and eccentricity >= 1.0:
        return "non_periodic_or_uncertain"
    return "unknown"


def build_classification(seed: dict[str, Any], orbit: dict[str, Any] | None) -> dict[str, Any]:
    return {
        "orbitalFamily": orbital_family(seed, orbit),
        "inclinationClass": inclination_class(orbit),
        "returnStatus": return_status(seed, orbit),
        "source": {
            "orbitClass": seed.get("orbitClass") or (orbit or {}).get("orbitClass"),
            "jplOrbitClassCode": (orbit or {}).get("jplOrbitClassCode"),
        },
    }


def sample_records_for_comet(
    comet_snapshot: dict[str, Any],
    stable_id: str,
) -> list[dict[str, Any]]:
    ephemeris = comet_snapshot.get("ephemeris") or {}
    samples = (ephemeris.get("comets") or {}).get(stable_id)
    anchor = parse_timestamp(ephemeris.get("anchorTimestamp"))
    step_hours = finite_float(ephemeris.get("sampleStepHours"))
    if not isinstance(samples, list) or anchor is None or step_hours is None:
        return []
    records: list[dict[str, Any]] = []
    for index, sample in enumerate(samples):
        if not isinstance(sample, list) or len(sample) < 3:
            continue
        magnitude = finite_float(sample[2])
        ra_hours = finite_float(sample[0])
        dec_degrees = finite_float(sample[1])
        sample_time = anchor + dt.timedelta(hours=step_hours * index)
        records.append(
            {
                "timestamp": sample_time,
                "date": sample_time.date(),
                "rightAscensionHours": ra_hours,
                "declinationDegrees": dec_degrees,
                "magnitude": magnitude,
            }
        )
    return records


def nearest_sample(
    samples: list[dict[str, Any]],
    reference_date: dt.date,
) -> dict[str, Any] | None:
    if not samples:
        return None
    reference_dt = dt.datetime.combine(reference_date, dt.time.min, tzinfo=dt.UTC)
    return min(samples, key=lambda sample: abs((sample["timestamp"] - reference_dt).total_seconds()))


def build_ephemeris_summary(
    comet_snapshot: dict[str, Any],
    seed: dict[str, Any],
    *,
    reference_date: dt.date,
    useful_magnitude_limit: float,
) -> dict[str, Any]:
    stable_id = str(seed.get("stableID") or "")
    ephemeris = comet_snapshot.get("ephemeris") or {}
    samples = sample_records_for_comet(comet_snapshot, stable_id)
    current = nearest_sample(samples, reference_date)
    magnitude_samples = [sample for sample in samples if sample.get("magnitude") is not None]
    future_samples = [sample for sample in magnitude_samples if sample["date"] >= reference_date]
    useful_samples = [
        sample
        for sample in future_samples
        if finite_float(sample.get("magnitude")) is not None
        and float(sample["magnitude"]) <= useful_magnitude_limit
    ]
    brightest = min(magnitude_samples, key=lambda sample: float(sample["magnitude"])) if magnitude_samples else None
    faintest = max(magnitude_samples, key=lambda sample: float(sample["magnitude"])) if magnitude_samples else None

    useful_start = useful_samples[0]["date"] if useful_samples else None
    useful_end = useful_samples[-1]["date"] if useful_samples else None
    current_magnitude = finite_float((current or {}).get("magnitude"))
    current_is_useful = current_magnitude is not None and current_magnitude <= useful_magnitude_limit
    return {
        "validStart": seed.get("ephemerisValidStart") or ephemeris.get("anchorTimestamp"),
        "validEnd": seed.get("ephemerisValidEnd"),
        "sourcePackageVersion": comet_snapshot.get("packageVersion"),
        "sourceGeneratedAt": ephemeris.get("generatedAt") or comet_snapshot.get("generatedAt"),
        "sampleStepHours": ephemeris.get("sampleStepHours"),
        "sampleCount": ephemeris.get("sampleCount"),
        "referenceDate": reference_date.isoformat(),
        "usefulMagnitudeLimit": useful_magnitude_limit,
        "currentMagnitudeEstimate": current_magnitude,
        "currentSampleDate": current["date"].isoformat() if current else None,
        "currentSampleStatus": "useful" if current_is_useful else "tooFaint" if current_magnitude is not None else "unknown",
        "firstFutureUsefulDate": useful_start.isoformat() if useful_start else None,
        "lastFutureUsefulDate": useful_end.isoformat() if useful_end else None,
        "daysUntilUsefulStart": (useful_start - reference_date).days if useful_start else None,
        "daysUntilUsefulEnd": (useful_end - reference_date).days if useful_end else None,
        "brightestMagnitude": finite_float((brightest or {}).get("magnitude")),
        "brightestDate": brightest["date"].isoformat() if brightest else None,
        "faintestMagnitude": finite_float((faintest or {}).get("magnitude")),
        "faintestDate": faintest["date"].isoformat() if faintest else None,
    }


def weekly_visibility_points(entry: dict[str, Any]) -> list[dict[str, Any]]:
    points: list[dict[str, Any]] = []
    for hemisphere, rows in sorted((entry.get("weeklyRowsByHemisphere") or {}).items()):
        for row in rows or []:
            parsed_date = parse_date(row.get("date"))
            if parsed_date is None:
                continue
            points.append(
                {
                    "hemisphere": hemisphere,
                    "date": parsed_date,
                    "magnitude": finite_float(row.get("magnitude")),
                    "bestAltitudeDegrees": finite_float(row.get("bestAltitudeDegrees")),
                    "elongationDegrees": finite_float(row.get("elongationDegrees")),
                    "rightAscensionHours": finite_float(row.get("rightAscensionHours")),
                    "declinationDegrees": finite_float(row.get("declinationDegrees")),
                }
            )
    points.sort(key=lambda point: (point["date"], str(point["hemisphere"])))
    return points


def aerith_point_is_useful(point: dict[str, Any], useful_magnitude_limit: float) -> bool:
    magnitude = finite_float(point.get("magnitude"))
    altitude = finite_float(point.get("bestAltitudeDegrees"))
    elongation = finite_float(point.get("elongationDegrees"))
    return (
        magnitude is not None
        and magnitude <= useful_magnitude_limit
        and altitude is not None
        and altitude >= AERITH_USEFUL_ALTITUDE_DEGREES
        and elongation is not None
        and elongation >= AERITH_USEFUL_ELONGATION_DEGREES
    )


def by_hemisphere(points: list[dict[str, Any]], key: str) -> dict[str, float]:
    result: dict[str, float] = {}
    for point in points:
        value = finite_float(point.get(key))
        if value is not None:
            result[str(point["hemisphere"])] = value
    return result


def build_visibility_summary(
    entry: dict[str, Any],
    ephemeris_summary: dict[str, Any],
    *,
    reference_date: dt.date,
    useful_magnitude_limit: float,
) -> dict[str, Any]:
    points = weekly_visibility_points(entry)
    current_points = [point for point in points if point["date"] <= reference_date]
    latest_current_date = max((point["date"] for point in current_points), default=None)
    latest_current = [point for point in current_points if point["date"] == latest_current_date]
    future_points = [point for point in points if point["date"] > reference_date]
    useful_current = [point for point in latest_current if aerith_point_is_useful(point, useful_magnitude_limit)]
    useful_future = [point for point in future_points if aerith_point_is_useful(point, useful_magnitude_limit)]
    first_future_useful = min((point["date"] for point in useful_future), default=None)

    if useful_current:
        state = "current"
    elif first_future_useful is not None:
        state = "comingSoon"
    elif ephemeris_summary.get("firstFutureUsefulDate"):
        state = "futureVisible"
    elif points:
        state = "notCurrentlyUseful"
    else:
        state = "unknown"

    future_useful_start = ephemeris_summary.get("firstFutureUsefulDate")
    future_useful_end = ephemeris_summary.get("lastFutureUsefulDate")
    return {
        "state": state,
        "referenceDate": reference_date.isoformat(),
        "basis": "Aerith weekly bright-comet rows plus AstroGuide cometSnapshot magnitude window",
        "usefulMagnitudeLimit": useful_magnitude_limit,
        "aerithCurrentDate": latest_current_date.isoformat() if latest_current_date else None,
        "aerithNextUsefulDate": first_future_useful.isoformat() if first_future_useful else None,
        "aerithCurrentMagnitude": min(
            (float(point["magnitude"]) for point in latest_current if point.get("magnitude") is not None),
            default=None,
        ),
        "aerithNextMagnitude": min(
            (float(point["magnitude"]) for point in future_points if point.get("magnitude") is not None),
            default=None,
        ),
        "currentBestAltitudeDegreesByHemisphere": by_hemisphere(latest_current, "bestAltitudeDegrees"),
        "nextBestAltitudeDegreesByHemisphere": by_hemisphere(
            [point for point in future_points if point["date"] == min((item["date"] for item in future_points), default=None)],
            "bestAltitudeDegrees",
        ),
        "futureUsefulStartDate": future_useful_start,
        "futureUsefulEndDate": future_useful_end,
        "daysUntilFutureUsefulStart": ephemeris_summary.get("daysUntilUsefulStart"),
        "daysUntilFutureUsefulEnd": ephemeris_summary.get("daysUntilUsefulEnd"),
    }


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def cache_image_asset(
    *,
    entry: dict[str, Any],
    stable_id: str,
    max_image_bytes: int,
    fetcher: Callable[[str], bytes] = fetch_url,
) -> dict[str, Any] | None:
    source_image_url = entry.get("thumbnailImageURL")
    if not source_image_url:
        return None
    data = fetcher(str(source_image_url))
    if len(data) > max_image_bytes:
        raise RuntimeError(
            f"Skipping oversized Aerith image for {stable_id}: {len(data)} bytes exceeds {max_image_bytes}."
        )
    checksum = hashlib.sha256(data).hexdigest()
    suffix = Path(urlparse(str(source_image_url)).path).suffix.lower()
    if suffix not in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        suffix = ".jpg"
    file_name = f"{safe_identifier(stable_id).lower()}_{checksum[:12]}{suffix}"
    asset_path = REPO_ROOT / ASSET_DIR / file_name
    asset_path.parent.mkdir(parents=True, exist_ok=True)
    asset_path.write_bytes(data)
    relative_path = ASSET_DIR / file_name
    cached_url = f"{METADATA_ORIGIN}/{relative_path.as_posix()}"
    return {
        "kind": "thumbnail",
        "url": cached_url,
        "cachedURL": cached_url,
        "cachedPath": relative_path.as_posix(),
        "originalURL": source_image_url,
        "sourceURL": entry.get("detailURL"),
        "aerithDetailURL": entry.get("detailURL"),
        "attribution": "Image courtesy Aerith / Seiichi Yoshida",
        "byteSize": len(data),
        "checksum": checksum,
    }


def build_records(
    comet_snapshot: dict[str, Any],
    aerith_source: dict[str, Any],
    *,
    orbit_geometry: dict[str, Any] | None = None,
    generated_at: str,
    cache_images: bool,
    image_limit: int,
    max_image_bytes: int,
    brightness_lookback_days: int = DEFAULT_BRIGHTNESS_LOOKBACK_DAYS,
    useful_magnitude_limit: float = DEFAULT_USEFUL_MAGNITUDE_LIMIT,
    fetch_delay_seconds: float = 0.0,
    fetcher: Callable[[str], bytes] = fetch_url,
) -> list[dict[str, Any]]:
    reference_date = source_page_date(aerith_source)
    orbit_by_id = orbit_records_by_id(orbit_geometry)
    aerith_entries = {
        str(entry.get("normalizedDesignation") or ""): entry
        for entry in aerith_source.get("comets") or []
        if entry.get("normalizedDesignation")
    }
    records: list[dict[str, Any]] = []
    images_cached = 0

    for seed in comet_snapshot.get("seeds", {}).get("comets", []):
        match = next(
            (aerith_entries[key] for key in seed_match_keys(seed) if key in aerith_entries),
            None,
        )
        if match is None:
            continue

        observations = build_observations(match, reference_date)
        if not observations:
            continue
        brightness_chart = build_brightness_chart(
            observations,
            lookback_days=max(0, brightness_lookback_days),
        )
        brightness_trend = build_brightness_trend(brightness_chart["points"])
        classification = build_classification(seed, orbit_by_id.get(seed["stableID"]))
        ephemeris_summary = build_ephemeris_summary(
            comet_snapshot,
            seed,
            reference_date=reference_date,
            useful_magnitude_limit=useful_magnitude_limit,
        )
        visibility_summary = build_visibility_summary(
            match,
            ephemeris_summary,
            reference_date=reference_date,
            useful_magnitude_limit=useful_magnitude_limit,
        )

        media: dict[str, Any] | None = None
        if cache_images and images_cached < image_limit:
            try:
                asset = cache_image_asset(
                    entry=match,
                    stable_id=seed["stableID"],
                    max_image_bytes=max_image_bytes,
                    fetcher=fetcher,
                )
            except Exception as error:  # noqa: BLE001 - source image fetch is optional
                print(f"Warning: {error}", flush=True)
                asset = None
            if asset is not None:
                hero_asset = dict(asset)
                hero_asset["kind"] = "hero"
                media = {"thumbnail": asset, "hero": hero_asset}
                images_cached += 1
                if fetch_delay_seconds > 0:
                    time.sleep(fetch_delay_seconds)

        records.append(
            {
                "stableID": seed["stableID"],
                "designation": seed.get("designation"),
                "displayName": seed.get("displayName") or match.get("aerithName") or seed["stableID"],
                "aerithName": match.get("aerithName"),
                "detailURL": match.get("detailURL"),
                "generatedAt": generated_at,
                "visibilitySummary": visibility_summary,
                "ephemerisSummary": ephemeris_summary,
                "classification": classification,
                "source": {
                    "name": "Aerith / Seiichi Yoshida",
                    "sourceURL": aerith_source.get("source", {}).get("sourceURL"),
                    "detailURL": match.get("detailURL"),
                    "attribution": "Source: Aerith / Seiichi Yoshida",
                    "generatedAt": aerith_source.get("generatedAt"),
                    "permissionReceived": aerith_source.get("source", {}).get("permissionReceived")
                    or PERMISSION_RECEIVED,
                },
                "media": media,
                "brightness": observations,
                "brightnessChart": brightness_chart,
                "brightnessTrend": brightness_trend,
            }
        )

    return records


def write_detail_package(
    records: list[dict[str, Any]],
    *,
    package_version: str,
    generated_at: str,
    min_supported_app_version: str,
    min_supported_build: str,
    update_manifest_path: Path | None,
) -> dict[str, Any]:
    descriptors: list[dict[str, Any]] = []
    for record in records:
        shard_id = safe_identifier(record["stableID"])
        shard = {
            "schemaVersion": 1,
            "packageFamily": PACKAGE_FAMILY,
            "packageVersion": package_version,
            "packageRole": "comet",
            "shardID": shard_id,
            "record": record,
        }
        shard_path = REPO_ROOT / SHARD_DIR / f"{shard_id}_v1.json"
        shard_data = write_json(shard_path, shard)
        relative_shard_path = shard_path.relative_to(REPO_ROOT)
        descriptors.append(
            {
                "stableID": record["stableID"],
                "designation": record.get("designation"),
                "displayName": record["displayName"],
                "aerithName": record.get("aerithName"),
                "aliases": [],
                "aerithDetailURL": record.get("detailURL"),
                "visibilityState": (record.get("visibilitySummary") or {}).get("state"),
                "visibilitySummary": record.get("visibilitySummary"),
                "ephemerisSummary": record.get("ephemerisSummary"),
                "classification": record.get("classification"),
                "brightnessTrend": record.get("brightnessTrend"),
                "brightnessRange": {
                    "lookbackDays": (record.get("brightnessChart") or {}).get("lookbackDays"),
                    "availableStartDate": (record.get("brightnessChart") or {}).get("availableStartDate"),
                    "availableEndDate": (record.get("brightnessChart") or {}).get("availableEndDate"),
                    "actualDaySpan": (record.get("brightnessChart") or {}).get("actualDaySpan"),
                    "pointCount": (record.get("brightnessChart") or {}).get("pointCount"),
                    "containsProjection": (record.get("brightnessChart") or {}).get("containsProjection"),
                    "containsReportedObservation": (record.get("brightnessChart") or {}).get(
                        "containsReportedObservation"
                    ),
                },
                "shardID": shard_id,
                "fileName": shard_path.name,
                "path": relative_shard_path.as_posix(),
                "url": f"{METADATA_ORIGIN}/{relative_shard_path.as_posix()}",
                "checksum": hashlib.sha256(shard_data).hexdigest(),
                "byteSize": len(shard_data),
                "observationCount": len(record.get("brightness") or []),
                "highlightCount": sum(1 for point in record.get("brightness") or [] if point.get("isSignificant")),
                "cachedImageCount": sum(1 for asset in (record.get("media") or {}).values() if asset),
            }
        )

    package = {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": package_version,
        "packageRole": "index",
        "generatedAt": generated_at,
        "source": {
            "name": "Aerith / Seiichi Yoshida",
            "sourceURL": "https://www.aerith.net/",
            "attribution": "Source: Aerith / Seiichi Yoshida",
            "permissionReceived": PERMISSION_RECEIVED,
        },
        "comets": descriptors,
    }
    data = write_json(REPO_ROOT / PACKAGE_PATH, package)
    descriptor = package_descriptor(
        package=package,
        data=data,
        min_supported_app_version=min_supported_app_version,
        min_supported_build=min_supported_build,
    )
    if update_manifest_path is not None:
        update_manifest(update_manifest_path, generated_at, descriptor)
    return descriptor


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
        "recordCount": len(package.get("comets") or []),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Clients that support this family should lazy-load a comet shard only for the opened "
            "detail target and hide Aerith brightness/media affordances when no compatible package exists."
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


def repo_relative_path(path: Path) -> Path:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve())
    except ValueError:
        return path


def validate_package(package: dict[str, Any], index_path: Path) -> None:
    if package.get("schemaVersion") != 1:
        raise RuntimeError("Comet detail metadata schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Comet detail metadata packageFamily must be {PACKAGE_FAMILY}.")
    if package.get("packageRole") != "index":
        raise RuntimeError("Comet detail metadata index packageRole must be index.")
    if not str(package.get("packageVersion") or "").strip():
        raise RuntimeError("Comet detail metadata packageVersion is required.")
    if parse_timestamp(package.get("generatedAt")) is None:
        raise RuntimeError("Comet detail metadata generatedAt must be an ISO-8601 timestamp.")
    source = package.get("source") or {}
    if "Aerith" not in str(source.get("attribution") or ""):
        raise RuntimeError("Comet detail metadata source attribution must credit Aerith.")
    if source.get("permissionReceived") != PERMISSION_RECEIVED:
        raise RuntimeError("Comet detail metadata source must preserve the Aerith permission date.")
    descriptors = package.get("comets")
    if not isinstance(descriptors, list) or not descriptors:
        raise RuntimeError("Comet detail metadata index contains no comet descriptors.")

    seen: set[str] = set()
    for descriptor in descriptors:
        stable_id = str(descriptor.get("stableID") or "")
        if not stable_id:
            raise RuntimeError("Comet detail descriptor is missing stableID.")
        if stable_id in seen:
            raise RuntimeError(f"Duplicate comet detail descriptor stableID: {stable_id}.")
        seen.add(stable_id)
        validate_summary_fields(stable_id, descriptor)
        shard_path = REPO_ROOT / str(descriptor.get("path") or "")
        if not shard_path.exists():
            raise RuntimeError(f"Missing comet detail shard for {stable_id}: {descriptor.get('path')}.")
        shard_data = shard_path.read_bytes()
        if len(shard_data) != int(descriptor.get("byteSize") or 0):
            raise RuntimeError(f"Shard byteSize mismatch for {stable_id}.")
        if hashlib.sha256(shard_data).hexdigest() != descriptor.get("checksum"):
            raise RuntimeError(f"Shard checksum mismatch for {stable_id}.")
        expected_url = f"{METADATA_ORIGIN}/{repo_relative_path(shard_path).as_posix()}"
        if descriptor.get("url") != expected_url:
            raise RuntimeError(f"Shard URL mismatch for {stable_id}.")
        shard = read_json(shard_path)
        validate_shard(stable_id, shard, package.get("packageVersion"))
    if not index_path.exists():
        raise RuntimeError("Comet detail metadata index path does not exist.")


def validate_summary_fields(stable_id: str, payload: dict[str, Any]) -> None:
    visibility = payload.get("visibilitySummary") or {}
    state = payload.get("visibilityState") or visibility.get("state")
    if state not in VISIBILITY_STATES:
        raise RuntimeError(f"Unsupported visibilityState for {stable_id}: {state}.")
    classification = payload.get("classification") or {}
    if classification.get("orbitalFamily") not in ORBITAL_FAMILIES:
        raise RuntimeError(f"Unsupported orbitalFamily for {stable_id}.")
    if classification.get("inclinationClass") not in INCLINATION_CLASSES:
        raise RuntimeError(f"Unsupported inclinationClass for {stable_id}.")
    if classification.get("returnStatus") not in RETURN_STATUSES:
        raise RuntimeError(f"Unsupported returnStatus for {stable_id}.")
    trend = payload.get("brightnessTrend") or {}
    if trend.get("direction") not in TREND_DIRECTIONS:
        raise RuntimeError(f"Unsupported brightness trend direction for {stable_id}.")
    brightness_range = payload.get("brightnessRange")
    if brightness_range is not None and int(brightness_range.get("pointCount") or 0) < 0:
        raise RuntimeError(f"Invalid brightnessRange pointCount for {stable_id}.")


def validate_shard(stable_id: str, shard: dict[str, Any], package_version: Any) -> None:
    if shard.get("schemaVersion") != 1:
        raise RuntimeError(f"Comet detail shard {stable_id} schemaVersion must be 1.")
    if shard.get("packageFamily") != PACKAGE_FAMILY:
        raise RuntimeError(f"Comet detail shard {stable_id} packageFamily mismatch.")
    if shard.get("packageVersion") != package_version:
        raise RuntimeError(f"Comet detail shard {stable_id} packageVersion mismatch.")
    record = shard.get("record") or {}
    if record.get("stableID") != stable_id:
        raise RuntimeError(f"Comet detail shard {stable_id} record stableID mismatch.")
    validate_summary_fields(stable_id, record)
    detail_url = record.get("detailURL")
    source = record.get("source") or {}
    if source.get("detailURL") != detail_url:
        raise RuntimeError(f"Comet detail shard {stable_id} source detailURL mismatch.")
    if "Aerith" not in str(source.get("attribution") or ""):
        raise RuntimeError(f"Comet detail shard {stable_id} source attribution must credit Aerith.")
    brightness = record.get("brightness")
    if not isinstance(brightness, list) or not brightness:
        raise RuntimeError(f"Comet detail shard {stable_id} has no brightness observations.")
    chart = record.get("brightnessChart") or {}
    points = chart.get("points")
    if not isinstance(points, list) or int(chart.get("pointCount") or -1) != len(points):
        raise RuntimeError(f"Comet detail shard {stable_id} brightnessChart pointCount mismatch.")
    for point in points:
        if point.get("estimateKind") not in {"reported", "current", "projection"}:
            raise RuntimeError(f"Comet detail shard {stable_id} has unsupported estimateKind.")
    validate_media(record)


def validate_media(record: dict[str, Any]) -> None:
    media = record.get("media") or {}
    detail_url = record.get("detailURL")
    for role, asset in media.items():
        if not asset:
            continue
        url = str(asset.get("url") or "")
        cached_path = str(asset.get("cachedPath") or "")
        if not url.startswith(f"{METADATA_ORIGIN}/v1/assets/comets/aerith/"):
            raise RuntimeError(f"{record.get('stableID')} {role} image is not served from AstroGuide metadata.")
        if "aerith.net/pictures" in url:
            raise RuntimeError(f"{record.get('stableID')} {role} image hotlinks an Aerith picture URL.")
        if not cached_path.startswith("v1/assets/comets/aerith/"):
            raise RuntimeError(f"{record.get('stableID')} {role} image cachedPath is invalid.")
        asset_path = REPO_ROOT / cached_path
        if not asset_path.exists():
            raise RuntimeError(f"{record.get('stableID')} {role} cached image is missing: {cached_path}.")
        if asset.get("byteSize") != asset_path.stat().st_size:
            raise RuntimeError(f"{record.get('stableID')} {role} cached image byteSize mismatch.")
        if hashlib.sha256(asset_path.read_bytes()).hexdigest() != asset.get("checksum"):
            raise RuntimeError(f"{record.get('stableID')} {role} cached image checksum mismatch.")
        if asset.get("sourceURL") != detail_url or asset.get("aerithDetailURL") != detail_url:
            raise RuntimeError(f"{record.get('stableID')} {role} image must link back to the Aerith detail page.")
        if "Aerith" not in str(asset.get("attribution") or ""):
            raise RuntimeError(f"{record.get('stableID')} {role} image attribution must credit Aerith.")


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
        raise RuntimeError("Manifest packageVersion does not match comet detail metadata index.")
    if entry.get("payloadSchemaVersion") != package.get("schemaVersion"):
        raise RuntimeError("Manifest payloadSchemaVersion does not match comet detail metadata index.")
    expected_url = f"{METADATA_ORIGIN}/{repo_relative_path(output_path).as_posix()}"
    if entry.get("packageURL") != expected_url:
        raise RuntimeError("Manifest packageURL does not reference comet detail metadata index.")
    if int(entry.get("byteSize") or 0) != len(data):
        raise RuntimeError("Manifest byteSize does not match comet detail metadata index.")
    checksum = entry.get("checksum") or {}
    if checksum.get("algorithm") != "sha256":
        raise RuntimeError("Manifest checksum algorithm must be sha256.")
    if checksum.get("value") != hashlib.sha256(data).hexdigest():
        raise RuntimeError("Manifest checksum does not match comet detail metadata index.")
    if int(entry.get("recordCount") or 0) != len(package.get("comets") or []):
        raise RuntimeError("Manifest recordCount does not match comet detail metadata index.")


def main() -> int:
    args = parse_args()
    index_path = REPO_ROOT / PACKAGE_PATH
    manifest_path = args.manifest.resolve()
    if args.validate_only:
        package = read_json(index_path)
        data = index_path.read_bytes()
        validate_package(package, index_path)
        if not args.skip_manifest:
            validate_manifest_descriptor(manifest_path, package, data, index_path)
        print(f"Validated {repo_relative_path(index_path).as_posix()}")
        return 0

    generated_at = args.generated_at or utc_now()
    package_version = args.package_version or f"comet-detail-metadata-v1-{date_token(generated_at)}-aerith"
    records = build_records(
        read_json(args.source_package.resolve()),
        read_json(args.aerith_source.resolve()),
        orbit_geometry=read_json(args.orbit_geometry.resolve()) if args.orbit_geometry.exists() else None,
        generated_at=generated_at,
        cache_images=not args.skip_images,
        image_limit=max(0, args.image_limit),
        max_image_bytes=args.max_image_bytes,
        brightness_lookback_days=args.brightness_lookback_days,
        useful_magnitude_limit=args.useful_magnitude_limit,
        fetch_delay_seconds=max(0, args.fetch_delay_seconds),
    )
    if not records:
        raise RuntimeError("No comet detail records were generated.")

    descriptor = write_detail_package(
        records,
        package_version=package_version,
        generated_at=generated_at,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
        update_manifest_path=None if args.skip_manifest else manifest_path,
    )
    package = read_json(index_path)
    validate_package(package, index_path)
    if not args.skip_manifest:
        validate_manifest_descriptor(manifest_path, package, index_path.read_bytes(), index_path)
    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['recordCount']} comets {descriptor['byteSize']} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
