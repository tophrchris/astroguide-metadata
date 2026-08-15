#!/usr/bin/env python3
"""Build lazy comet detail metadata enriched from Aerith."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
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
CACHE_TTL_SECONDS = 604800
PERMISSION_RECEIVED = "2026-08-15"
USER_AGENT = (
    "AstroGuide metadata comet detail builder/1.0 "
    "(Aerith permission received 2026-08-15; https://astroguide.space)"
)

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
    parser.add_argument("--generated-at")
    parser.add_argument("--package-version")
    parser.add_argument("--manifest", type=Path, default=REPO_ROOT / "v1/channels/stable/manifest.json")
    parser.add_argument("--min-supported-app-version", default="1.4.1")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--image-limit", type=int, default=1)
    parser.add_argument("--max-image-bytes", type=int, default=500_000)
    parser.add_argument("--fetch-delay-seconds", type=float, default=0.5)
    parser.add_argument("--skip-images", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
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
            append_observation(
                {
                    "id": f"{entry['normalizedDesignation']}-{date}-{hemisphere}-weekly-{index}",
                    "date": date,
                    "magnitude": float(magnitude),
                    "qualifier": "weekly-estimate",
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
    return {
        "kind": "thumbnail",
        "url": f"{METADATA_ORIGIN}/{relative_path.as_posix()}",
        "sourceURL": entry.get("detailURL"),
        "attribution": "Image courtesy Aerith / Seiichi Yoshida",
        "byteSize": len(data),
        "checksum": checksum,
    }


def build_records(
    comet_snapshot: dict[str, Any],
    aerith_source: dict[str, Any],
    *,
    generated_at: str,
    cache_images: bool,
    image_limit: int,
    max_image_bytes: int,
    fetch_delay_seconds: float = 0.0,
    fetcher: Callable[[str], bytes] = fetch_url,
) -> list[dict[str, Any]]:
    reference_date = source_page_date(aerith_source)
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
                media = {"thumbnail": asset}
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
                "shardID": shard_id,
                "fileName": shard_path.name,
                "path": relative_shard_path.as_posix(),
                "url": f"{METADATA_ORIGIN}/{relative_shard_path.as_posix()}",
                "checksum": hashlib.sha256(shard_data).hexdigest(),
                "byteSize": len(shard_data),
                "observationCount": len(record.get("brightness") or []),
                "highlightCount": sum(1 for point in record.get("brightness") or [] if point.get("isSignificant")),
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


def main() -> int:
    args = parse_args()
    generated_at = args.generated_at or utc_now()
    package_version = args.package_version or f"comet-detail-metadata-v1-{date_token(generated_at)}-aerith"
    records = build_records(
        read_json(args.source_package.resolve()),
        read_json(args.aerith_source.resolve()),
        generated_at=generated_at,
        cache_images=not args.skip_images,
        image_limit=max(0, args.image_limit),
        max_image_bytes=args.max_image_bytes,
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
        update_manifest_path=None if args.skip_manifest else args.manifest.resolve(),
    )
    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['recordCount']} comets {descriptor['byteSize']} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
