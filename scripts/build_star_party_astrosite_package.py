#!/usr/bin/env python3
"""Build and validate the curated Star Party AstroSites metadata package."""

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import uuid
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "sources/star-party-astrosites/records"
PACKAGE_PATH = Path(
    "v1/packages/star-party-astrosites/star_party_astrosites_v1.json"
)
MANIFEST_PATH = REPO_ROOT / "v1/channels/stable/manifest.json"
METADATA_ORIGIN = "https://metadata.astroguide.space"
PACKAGE_FAMILY = "starPartyAstroSites"
CACHE_TTL_SECONDS = 604800
SOURCE_SITE_ID_ROOT = f"{METADATA_ORIGIN}/star-party-astrosites/"

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

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
COUNTRY_CODE_PATTERN = re.compile(r"^[A-Z]{2}$")
EVENT_STATUSES = {"scheduled", "completed", "cancelled"}
SOURCE_KEYS = {"title", "url", "verifiedAt"}
RECORD_REQUIRED_KEYS = {
    "schemaVersion",
    "recordKind",
    "id",
    "displayName",
    "description",
    "descriptionSources",
    "astroSite",
    "location",
    "officialURLs",
    "events",
}
RECORD_OPTIONAL_KEYS = {"media"}


class ValidationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build the curated Star Party AstroSites package and refresh the stable "
            "manifest, or validate the checked-in artifacts without writing."
        )
    )
    parser.add_argument("--generated-at", help="UTC ISO-8601 package timestamp")
    parser.add_argument("--min-supported-app-version", default="1.4.1")
    parser.add_argument("--min-supported-build", default="1")
    parser.add_argument("--validate-only", action="store_true")
    return parser.parse_args()


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def json_bytes(payload: dict) -> bytes:
    return (json.dumps(payload, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def write_json(path: Path, payload: dict) -> bytes:
    data = json_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_utc_timestamp(value: str, label: str) -> dt.datetime:
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError) as error:
        raise ValidationError(f"{label} must be an ISO-8601 timestamp: {value!r}") from error
    if parsed.tzinfo is None or parsed.utcoffset() != dt.timedelta(0):
        raise ValidationError(f"{label} must use UTC: {value!r}")
    return parsed


def parse_date(value: str, label: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValidationError(f"{label} must be YYYY-MM-DD: {value!r}") from error


def validate_nonempty_string(value, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be a non-empty string.")
    return value


def validate_https_url(value, label: str) -> str:
    value = validate_nonempty_string(value, label)
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValidationError(f"{label} must be an absolute HTTPS URL: {value!r}")
    if parsed.username or parsed.password:
        raise ValidationError(f"{label} must not contain URL credentials: {value!r}")
    return value


def validate_source(source, label: str, generated_date: dt.date) -> None:
    if not isinstance(source, dict) or set(source) != SOURCE_KEYS:
        raise ValidationError(f"{label} must contain exactly {sorted(SOURCE_KEYS)}.")
    validate_nonempty_string(source["title"], f"{label}.title")
    validate_https_url(source["url"], f"{label}.url")
    verified_at = parse_date(source["verifiedAt"], f"{label}.verifiedAt")
    if verified_at > generated_date:
        raise ValidationError(
            f"{label}.verifiedAt {verified_at} is later than package date {generated_date}."
        )


def expected_source_site_id(record_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{SOURCE_SITE_ID_ROOT}{record_id}"))


def validate_media(media, record_id: str, generated_date: dt.date) -> None:
    if not isinstance(media, dict) or not media:
        raise ValidationError(f"{record_id}.media must be a non-empty object when present.")
    if not set(media).issubset({"hero", "logo"}):
        raise ValidationError(f"{record_id}.media supports only hero and logo assets.")
    required = {
        "assetPath",
        "sourceURL",
        "attribution",
        "license",
        "permissionNotes",
        "verifiedAt",
    }
    for role, asset in media.items():
        label = f"{record_id}.media.{role}"
        if not isinstance(asset, dict) or set(asset) != required:
            raise ValidationError(f"{label} must contain exactly {sorted(required)}.")
        asset_path = validate_nonempty_string(asset["assetPath"], f"{label}.assetPath")
        prefix = "v1/assets/star-party-astrosites/"
        if not asset_path.startswith(prefix) or ".." in Path(asset_path).parts:
            raise ValidationError(f"{label}.assetPath must stay under {prefix}.")
        if not (REPO_ROOT / asset_path).is_file():
            raise ValidationError(f"{label}.assetPath does not exist: {asset_path}")
        validate_https_url(asset["sourceURL"], f"{label}.sourceURL")
        validate_nonempty_string(asset["attribution"], f"{label}.attribution")
        validate_nonempty_string(asset["license"], f"{label}.license")
        validate_nonempty_string(asset["permissionNotes"], f"{label}.permissionNotes")
        verified_at = parse_date(asset["verifiedAt"], f"{label}.verifiedAt")
        if verified_at > generated_date:
            raise ValidationError(f"{label}.verifiedAt cannot be in the future.")


def validate_record(record, path: Path, generated_date: dt.date) -> None:
    if not isinstance(record, dict):
        raise ValidationError(f"{path} must contain a JSON object.")
    keys = set(record)
    if not RECORD_REQUIRED_KEYS.issubset(keys) or not keys.issubset(
        RECORD_REQUIRED_KEYS | RECORD_OPTIONAL_KEYS
    ):
        raise ValidationError(
            f"{path} has invalid keys; required={sorted(RECORD_REQUIRED_KEYS)}, "
            f"optional={sorted(RECORD_OPTIONAL_KEYS)}."
        )
    if record["schemaVersion"] != 1 or record["recordKind"] != "starPartyAstroSite":
        raise ValidationError(f"{path} must be a starPartyAstroSite schemaVersion 1 record.")

    record_id = validate_nonempty_string(record["id"], f"{path}.id")
    if not ID_PATTERN.fullmatch(record_id):
        raise ValidationError(f"{path}.id must be a lowercase kebab-case identifier.")
    if path.parent.name != record_id or path.name != "record.json":
        raise ValidationError(f"{path} must live at records/{record_id}/record.json.")
    validate_nonempty_string(record["displayName"], f"{record_id}.displayName")
    description = validate_nonempty_string(record["description"], f"{record_id}.description")
    if not 40 <= len(description) <= 320:
        raise ValidationError(f"{record_id}.description must contain 40-320 characters.")

    description_sources = record["descriptionSources"]
    if not isinstance(description_sources, list) or not description_sources:
        raise ValidationError(f"{record_id}.descriptionSources must not be empty.")
    for index, source in enumerate(description_sources):
        validate_source(source, f"{record_id}.descriptionSources[{index}]", generated_date)

    astro_site = record["astroSite"]
    required_astro_site = {
        "schemaVersion",
        "sourceSiteID",
        "name",
        "latitude",
        "longitude",
        "preferredPathPreviewCenterDirectionRaw",
    }
    if not isinstance(astro_site, dict) or not required_astro_site.issubset(astro_site):
        raise ValidationError(f"{record_id}.astroSite is missing required portable site fields.")
    if not set(astro_site).issubset(required_astro_site | {"elevationMeters"}):
        raise ValidationError(f"{record_id}.astroSite contains unsupported fields.")
    if astro_site["schemaVersion"] != 1:
        raise ValidationError(f"{record_id}.astroSite.schemaVersion must be 1.")
    if astro_site["sourceSiteID"] != expected_source_site_id(record_id):
        raise ValidationError(
            f"{record_id}.astroSite.sourceSiteID must be the deterministic UUIDv5 for its ID."
        )
    validate_nonempty_string(astro_site["name"], f"{record_id}.astroSite.name")
    latitude = astro_site["latitude"]
    longitude = astro_site["longitude"]
    if isinstance(latitude, bool) or not isinstance(latitude, (int, float)) or not -90 <= latitude <= 90:
        raise ValidationError(f"{record_id}.astroSite.latitude must be within -90...90.")
    if isinstance(longitude, bool) or not isinstance(longitude, (int, float)) or not -180 <= longitude <= 180:
        raise ValidationError(f"{record_id}.astroSite.longitude must be within -180...180.")
    elevation = astro_site.get("elevationMeters")
    if elevation is not None and (
        isinstance(elevation, bool)
        or not isinstance(elevation, (int, float))
        or not -500 <= elevation <= 9000
    ):
        raise ValidationError(f"{record_id}.astroSite.elevationMeters is out of range.")
    preview_direction = astro_site["preferredPathPreviewCenterDirectionRaw"]
    if preview_direction is not None and not isinstance(preview_direction, str):
        raise ValidationError(
            f"{record_id}.astroSite.preferredPathPreviewCenterDirectionRaw must be string or null."
        )

    location = record["location"]
    required_location = {
        "venueName",
        "locality",
        "region",
        "countryCode",
        "countryName",
        "timezone",
        "coordinateSource",
    }
    if not isinstance(location, dict) or not required_location.issubset(location):
        raise ValidationError(f"{record_id}.location is missing required fields.")
    if not set(location).issubset(required_location | {"relatedDarkSkyPlaceID"}):
        raise ValidationError(f"{record_id}.location contains unsupported fields.")
    for key in required_location - {"coordinateSource"}:
        validate_nonempty_string(location[key], f"{record_id}.location.{key}")
    if location["venueName"] != astro_site["name"]:
        raise ValidationError(f"{record_id}.location.venueName must match astroSite.name.")
    if not COUNTRY_CODE_PATTERN.fullmatch(location["countryCode"]):
        raise ValidationError(f"{record_id}.location.countryCode must be ISO alpha-2.")
    try:
        ZoneInfo(location["timezone"])
    except (ZoneInfoNotFoundError, TypeError) as error:
        raise ValidationError(f"{record_id}.location.timezone is not a valid IANA zone.") from error
    validate_source(location["coordinateSource"], f"{record_id}.location.coordinateSource", generated_date)
    if "relatedDarkSkyPlaceID" in location:
        related_id = validate_nonempty_string(
            location["relatedDarkSkyPlaceID"],
            f"{record_id}.location.relatedDarkSkyPlaceID",
        )
        if not related_id.startswith("darksky:"):
            raise ValidationError(f"{record_id}.location.relatedDarkSkyPlaceID must use darksky: ID.")

    official_urls = record["officialURLs"]
    if not isinstance(official_urls, list) or not official_urls:
        raise ValidationError(f"{record_id}.officialURLs must not be empty.")
    seen_official_urls = set()
    for index, official in enumerate(official_urls):
        label = f"{record_id}.officialURLs[{index}]"
        if not isinstance(official, dict) or set(official) != {"role", "url"}:
            raise ValidationError(f"{label} must contain exactly role and url.")
        validate_nonempty_string(official["role"], f"{label}.role")
        validate_https_url(official["url"], f"{label}.url")
        key = (official["role"], official["url"])
        if key in seen_official_urls:
            raise ValidationError(f"{label} duplicates an official URL row.")
        seen_official_urls.add(key)

    events = record["events"]
    if not isinstance(events, list) or not events:
        raise ValidationError(f"{record_id}.events must contain at least one dated instance.")
    for index, event in enumerate(events):
        label = f"{record_id}.events[{index}]"
        required_event = {"id", "name", "start", "end", "status", "url", "source"}
        if not isinstance(event, dict) or set(event) != required_event:
            raise ValidationError(f"{label} must contain exactly {sorted(required_event)}.")
        event_id = validate_nonempty_string(event["id"], f"{label}.id")
        if not ID_PATTERN.fullmatch(event_id):
            raise ValidationError(f"{label}.id must be a lowercase kebab-case identifier.")
        validate_nonempty_string(event["name"], f"{label}.name")
        start = parse_date(event["start"], f"{label}.start")
        end = parse_date(event["end"], f"{label}.end")
        if end < start:
            raise ValidationError(f"{label}.end cannot be earlier than start.")
        if event["status"] not in EVENT_STATUSES:
            raise ValidationError(f"{label}.status must be one of {sorted(EVENT_STATUSES)}.")
        if event["status"] == "completed" and end >= generated_date:
            raise ValidationError(f"{label} cannot be completed before its end date.")
        if event["status"] == "scheduled" and end < generated_date:
            raise ValidationError(f"{label} has passed and must not remain scheduled.")
        validate_https_url(event["url"], f"{label}.url")
        validate_source(event["source"], f"{label}.source", generated_date)

    if "media" in record:
        validate_media(record["media"], record_id, generated_date)


def validate_unique_identities(records: list[dict]) -> None:
    record_ids = set()
    source_site_ids = set()
    event_ids = set()
    for record in records:
        if record["id"] in record_ids:
            raise ValidationError(f"Duplicate record ID: {record['id']}")
        if record["astroSite"]["sourceSiteID"] in source_site_ids:
            raise ValidationError(f"Duplicate sourceSiteID: {record['astroSite']['sourceSiteID']}")
        record_ids.add(record["id"])
        source_site_ids.add(record["astroSite"]["sourceSiteID"])
        for event in record["events"]:
            if event["id"] in event_ids:
                raise ValidationError(f"Duplicate event ID: {event['id']}")
            event_ids.add(event["id"])


def load_and_validate_records(generated_at: str) -> list[dict]:
    generated_date = parse_utc_timestamp(generated_at, "generatedAt").date()
    paths = sorted(SOURCE_ROOT.glob("*/record.json"))
    if not paths:
        raise ValidationError(f"No source records found under {SOURCE_ROOT}.")

    records = []
    for path in paths:
        record = read_json(path)
        validate_record(record, path, generated_date)
        records.append(record)
    validate_unique_identities(records)
    return records


def normalized_record(record: dict) -> dict:
    normalized = copy.deepcopy(record)
    normalized["descriptionSources"] = sorted(
        normalized["descriptionSources"], key=lambda row: (row["url"], row["title"])
    )
    normalized["officialURLs"] = sorted(
        normalized["officialURLs"], key=lambda row: (row["role"], row["url"])
    )
    normalized["events"] = sorted(
        normalized["events"], key=lambda row: (row["start"], row["end"], row["id"])
    )
    return normalized


def build_package(records: list[dict], generated_at: str) -> dict:
    generated_date = parse_utc_timestamp(generated_at, "generatedAt").date()
    normalized = sorted((normalized_record(record) for record in records), key=lambda row: row["id"])
    events = [event for record in normalized for event in record["events"]]
    return {
        "schemaVersion": 1,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": f"star-party-astrosites-v1-{generated_date:%Y%m%d}",
        "generatedAt": generated_at,
        "scope": {
            "siteCount": len(normalized),
            "eventCount": len(events),
            "scheduledEventCount": sum(event["status"] == "scheduled" for event in events),
            "completedEventCount": sum(event["status"] == "completed" for event in events),
            "cancelledEventCount": sum(event["status"] == "cancelled" for event in events),
            "countryCount": len({record["location"]["countryCode"] for record in normalized}),
        },
        "starPartyAstroSites": normalized,
    }


def validate_package(package: dict) -> None:
    if package.get("schemaVersion") != 1:
        raise ValidationError("Package schemaVersion must be 1.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise ValidationError(f"Package family must be {PACKAGE_FAMILY}.")
    generated_at = package.get("generatedAt")
    records = load_and_validate_records(generated_at)
    expected = build_package(records, generated_at)
    if package != expected:
        raise ValidationError("Checked-in package does not match its curated source records.")


def package_descriptor(
    package: dict,
    data: bytes,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict:
    scope = package["scope"]
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
        "siteCount": scope["siteCount"],
        "eventCount": scope["eventCount"],
        "scheduledEventCount": scope["scheduledEventCount"],
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": CACHE_TTL_SECONDS,
        "fallbackNotes": (
            "Clients that support this family should retain a bundled or cached validated "
            "snapshot and hide Star Parties when no compatible package exists. Expired cached "
            "data remains usable until replaced by a validated refresh."
        ),
    }


def sort_packages(packages: list[dict]) -> list[dict]:
    family_order = {family: index for index, family in enumerate(FAMILY_ORDER)}
    band_order = {band: index for index, band in enumerate(LATITUDE_BAND_ORDER)}

    def key(entry: dict) -> tuple[int, int, str, str]:
        family = entry.get("family") or entry.get("packageFamily") or ""
        return (
            family_order.get(family, len(family_order)),
            band_order.get(str(entry.get("latitudeBand") or ""), len(band_order)),
            family,
            str(entry.get("packageVersion") or ""),
        )

    return sorted(packages, key=key)


def validate_manifest_descriptor(package: dict, data: bytes) -> None:
    manifest = read_json(MANIFEST_PATH)
    matches = [entry for entry in manifest["packages"] if entry.get("family") == PACKAGE_FAMILY]
    if len(matches) != 1:
        raise ValidationError(f"Stable manifest must contain exactly one {PACKAGE_FAMILY} entry.")
    entry = matches[0]
    expected = package_descriptor(
        package,
        data,
        entry.get("minSupportedAppVersion"),
        entry.get("minSupportedBuild"),
    )
    if entry != expected:
        raise ValidationError("Stable manifest descriptor does not match the package artifact.")
    if manifest["packages"] != sort_packages(manifest["packages"]):
        raise ValidationError("Stable manifest packages are not canonically ordered.")


def validate_checked_in_artifacts() -> None:
    package = read_json(REPO_ROOT / PACKAGE_PATH)
    validate_package(package)
    data = (REPO_ROOT / PACKAGE_PATH).read_bytes()
    if data != json_bytes(package):
        raise ValidationError("Checked-in package JSON formatting is not canonical.")
    validate_manifest_descriptor(package, data)


def main() -> int:
    args = parse_args()
    if args.validate_only:
        validate_checked_in_artifacts()
        package = read_json(REPO_ROOT / PACKAGE_PATH)
        print(
            f"Validated {PACKAGE_FAMILY}: {package['scope']['siteCount']} sites, "
            f"{package['scope']['eventCount']} events."
        )
        return 0

    generated_at = args.generated_at or utc_now()
    records = load_and_validate_records(generated_at)
    package = build_package(records, generated_at)
    data = write_json(REPO_ROOT / PACKAGE_PATH, package)

    manifest = read_json(MANIFEST_PATH)
    descriptor = package_descriptor(
        package,
        data,
        args.min_supported_app_version,
        args.min_supported_build,
    )
    packages = [
        entry for entry in manifest.get("packages", []) if entry.get("family") != PACKAGE_FAMILY
    ]
    packages.append(descriptor)
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sort_packages(packages)
    write_json(MANIFEST_PATH, manifest)

    print(
        f"{PACKAGE_FAMILY}: {descriptor['packageVersion']} "
        f"{descriptor['siteCount']} sites {descriptor['eventCount']} events "
        f"{descriptor['byteSize']} bytes {descriptor['checksum']['value']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
