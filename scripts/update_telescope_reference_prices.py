#!/usr/bin/env python3
"""Estimate, validate, and publish approximate telescope reference prices.

This deliberately does not crawl retailer pages. Online refreshes ask the
OpenAI Responses API to perform web search, require structured evidence, and
retain only rounded estimates plus non-link source summaries. The exact search
URLs are transient and are never written to the public metadata repository.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import math
import os
import re
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Callable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = (
    REPO_ROOT
    / "v1/packages/equipment/astrophotography_equipment_sanitized_catalog_v1.json"
)
DEFAULT_SMART_CATALOG = REPO_ROOT / "v1/packages/equipment/equipment_catalog_v1.json"
DEFAULT_CONFIG = REPO_ROOT / "sources/telescope-reference-prices/config.json"
DEFAULT_STATE = REPO_ROOT / "sources/telescope-reference-prices/estimates.json"
DEFAULT_OVERRIDES = REPO_ROOT / "sources/telescope-reference-prices/overrides.json"
DEFAULT_PACKAGE = (
    REPO_ROOT / "v1/packages/telescope-reference-prices/telescope_reference_prices_v1.json"
)
DEFAULT_REPORT = REPO_ROOT / "reports/telescope-reference-prices/latest.json"
DEFAULT_MANIFEST = REPO_ROOT / "v1/channels/stable/manifest.json"

PACKAGE_FAMILY = "telescopeReferencePrices"
CATALOG_FAMILY = "astrophotographyEquipmentSanitizedCatalog"
SMART_CATALOG_FAMILY = "equipmentCatalog"
PACKAGE_SCHEMA_VERSION = 1
METADATA_ORIGIN = "https://metadata.astroguide.space"
PACKAGE_URL_PATH = "/v1/packages/telescope-reference-prices/telescope_reference_prices_v1.json"
USER_AGENT = "AstroGuideMetadataReferencePriceEstimator/1.0 (+https://metadata.astroguide.space/docs/telescope-reference-prices-v1)"
PRICE_BASES = {"typical_new_retail", "last_known_new_retail"}
MARKET_STATUSES = {"current", "discontinued", "unknown"}
SOURCE_TYPES = {"manufacturer", "astronomy_specialty_retailer", "authorized_retailer", "other"}
EVIDENCE_CONFIGURATIONS = {
    "exact_product",
    "generation_proxy",
    "bundle_or_kit",
    "accessory",
    "used_or_refurbished",
    "marketplace",
    "financing_or_deposit",
    "other",
}
PUBLIC_FIELDS = {
    "equipment_id",
    "price_amount",
    "currency",
    "price_basis",
    "precision",
    "estimated_at",
    "market_status",
    "match_confidence",
    "estimate_confidence",
    "evidence_count",
    "manual_override",
    "note",
}
FAMILY_ORDER = [
    "targetMetadataOverlay",
    "targetNeighborhoodDefinitions",
    "targetImageAssets",
    "equipmentCatalog",
    "astrophotographyEquipmentCatalog",
    "astrophotographyEquipmentSanitizedCatalog",
    "telescopeReferencePrices",
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


class ReferencePriceError(RuntimeError):
    pass


class EstimateReviewRequired(ReferencePriceError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh search-grounded telescope reference-price estimates."
    )
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--smart-catalog", type=Path, default=DEFAULT_SMART_CATALOG)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES)
    parser.add_argument("--output", type=Path, default=DEFAULT_PACKAGE)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--generated-at")
    parser.add_argument("--equipment-id", action="append", dest="equipment_ids")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--min-supported-app-version", default="0.1.2")
    parser.add_argument("--min-supported-build", default="1")
    return parser.parse_args()


def read_json(path: Path, *, required: bool = True) -> dict[str, Any]:
    if not path.exists():
        if required:
            raise ReferencePriceError(f"Required JSON file is missing: {path}")
        return {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise ReferencePriceError(f"Could not read JSON from {path}: {error}") from error
    if not isinstance(payload, dict):
        raise ReferencePriceError(f"Expected a JSON object in {path}.")
    return payload


def write_json(path: Path, payload: dict[str, Any]) -> bytes:
    data = (json.dumps(payload, indent=2, ensure_ascii=True, sort_keys=False) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: Any, *, field: str = "timestamp") -> dt.datetime:
    if not isinstance(value, str) or not value.strip():
        raise ReferencePriceError(f"{field} must be a UTC ISO 8601 string.")
    candidate = value.strip()
    if candidate.endswith("Z"):
        candidate = candidate[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(candidate)
    except ValueError as error:
        raise ReferencePriceError(f"{field} is not valid ISO 8601: {value}") from error
    if parsed.tzinfo is None or parsed.utcoffset() != dt.timedelta(0):
        raise ReferencePriceError(f"{field} must use UTC: {value}")
    return parsed.astimezone(dt.UTC)


def timestamp_token(value: str) -> str:
    return parse_timestamp(value, field="generated_at").strftime("%Y%m%dT%H%M%SZ")


def finite_positive_number(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and float(value) > 0
    )


def probability(value: Any, *, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ReferencePriceError(f"{field} must be numeric on a 0-1 range.")
    result = float(value)
    if not math.isfinite(result) or not 0 <= result <= 1:
        raise ReferencePriceError(f"{field} must be numeric on a 0-1 range.")
    return round(result, 3)


def round_to_increment(value: float, increment: int) -> int:
    if increment <= 0:
        raise ReferencePriceError("Rounding increment must be positive.")
    rounded = (Decimal(str(value)) / Decimal(increment)).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    ) * Decimal(increment)
    return int(rounded)


def canonical_url(value: str) -> str:
    parsed = urllib.parse.urlparse(str(value).strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ReferencePriceError(f"Invalid evidence URL: {value!r}")
    host = parsed.hostname.casefold()
    port = f":{parsed.port}" if parsed.port else ""
    path = re.sub(r"/+", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    return urllib.parse.urlunparse((parsed.scheme.casefold(), host + port, path, "", "", ""))


def source_domain(value: str) -> str:
    host = urllib.parse.urlparse(canonical_url(value)).hostname or ""
    return host[4:] if host.startswith("www.") else host


def source_key(value: str) -> str:
    return hashlib.sha256(canonical_url(value).encode("utf-8")).hexdigest()


def load_catalog(path: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    package = read_json(path)
    if package.get("schemaVersion") != 1 or package.get("packageFamily") != CATALOG_FAMILY:
        raise ReferencePriceError(f"{path} is not the canonical sanitized equipment package.")
    components = package.get("catalog", {}).get("opticalComponents") or []
    eligible = [
        component
        for component in components
        if component.get("component_type") == "optical_tube"
        and str(component.get("component_id") or "").strip()
    ]
    telescopes = {str(component["component_id"]): component for component in eligible}
    if not telescopes:
        raise ReferencePriceError("The canonical package contained no optical_tube records.")
    if len(telescopes) != len(eligible):
        raise ReferencePriceError("Canonical telescope component IDs are not unique.")
    return package, telescopes


def smart_telescopes_from_package(
    package: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    if (
        package.get("schemaVersion") != 1
        or package.get("packageFamily") != SMART_CATALOG_FAMILY
    ):
        raise ReferencePriceError("Expected the canonical smart-telescope equipment package.")
    categories = package.get("catalog", {}).get("categories") or []
    telescope_categories = [item for item in categories if item.get("id") == "telescopes"]
    if len(telescope_categories) != 1:
        raise ReferencePriceError(
            "The canonical smart-telescope package must contain one telescopes category."
        )
    raw_items = telescope_categories[0].get("items") or []
    eligible = []
    for item in raw_items:
        equipment_id = str(item.get("id") or "").strip()
        notes = str(item.get("notes") or "").strip()
        if not equipment_id or notes.casefold().startswith("traditional telescope:"):
            continue
        normalized = copy.deepcopy(item)
        normalized.update(
            {
                "component_id": equipment_id,
                "component_type": "smart_telescope",
                "model": item.get("name"),
                "display_name": " ".join(
                    part
                    for part in (
                        str(item.get("manufacturer") or "").strip(),
                        str(item.get("name") or "").strip(),
                    )
                    if part
                ),
                "native_focal_length_mm": item.get("focal_length_mm"),
            }
        )
        aperture = item.get("aperture_mm")
        focal_length = item.get("focal_length_mm")
        if finite_positive_number(aperture) and finite_positive_number(focal_length):
            normalized["native_focal_ratio"] = round(float(focal_length) / float(aperture), 3)
        eligible.append(normalized)
    telescopes = {str(item["component_id"]): item for item in eligible}
    if not telescopes:
        raise ReferencePriceError(
            "The canonical smart-telescope package contained no eligible rows."
        )
    if len(telescopes) != len(eligible):
        raise ReferencePriceError("Canonical smart-telescope IDs are not unique.")
    return telescopes


def load_smart_catalog(path: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    package = read_json(path)
    return package, smart_telescopes_from_package(package)


def merge_canonical_telescopes(
    cleansed: dict[str, dict[str, Any]], smart: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    duplicate_ids = sorted(set(cleansed) & set(smart))
    if duplicate_ids:
        raise ReferencePriceError(
            "Canonical equipment IDs overlap across telescope catalogs: "
            + ", ".join(duplicate_ids[:10])
        )
    return {**cleansed, **smart}


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != 1:
        raise ReferencePriceError("Reference-price config must use schema_version 1.")
    api = config.get("api") or {}
    endpoint = canonical_url(str(api.get("endpoint") or ""))
    if endpoint != "https://api.openai.com/v1/responses":
        raise ReferencePriceError("Only the documented OpenAI Responses endpoint is supported.")
    if not str(api.get("model") or "").strip():
        raise ReferencePriceError("A pinned OpenAI API model is required.")
    if api.get("search_context_size") not in {"low", "medium", "high"}:
        raise ReferencePriceError("search_context_size must be low, medium, or high.")
    if not finite_positive_number(api.get("timeout_seconds")):
        raise ReferencePriceError("api.timeout_seconds must be positive.")
    if not isinstance(api.get("max_attempts"), int) or not 1 <= api["max_attempts"] <= 5:
        raise ReferencePriceError("api.max_attempts must be an integer from 1 through 5.")
    policy = config.get("estimate_policy") or {}
    if policy.get("currency") != "USD" or policy.get("country") != "US":
        raise ReferencePriceError("Launch reference-price estimates must use the US/USD market.")
    for field in ("minimum_price", "maximum_price", "rounding_increment"):
        if not finite_positive_number(policy.get(field)):
            raise ReferencePriceError(f"estimate_policy.{field} must be positive.")
    if float(policy["minimum_price"]) >= float(policy["maximum_price"]):
        raise ReferencePriceError("Reference-price plausibility bounds are invalid.")
    for field in ("minimum_match_confidence", "minimum_estimate_confidence"):
        probability(policy.get(field), field=f"estimate_policy.{field}")
    for field in (
        "maximum_evidence_spread_ratio",
        "maximum_model_median_difference_ratio",
        "suspicious_change_ratio",
        "suspicious_change_adaptive_ratio",
    ):
        value = policy.get(field)
        if not finite_positive_number(value) or float(value) > 2:
            raise ReferencePriceError(f"estimate_policy.{field} must be greater than 0 and at most 2.")
    if not finite_positive_number(policy.get("suspicious_change_minimum_usd")):
        raise ReferencePriceError("estimate_policy.suspicious_change_minimum_usd must be positive.")
    allowed = policy.get("single_source_allowed_types")
    if not isinstance(allowed, list) or not allowed or not set(allowed) <= SOURCE_TYPES - {"other"}:
        raise ReferencePriceError("single_source_allowed_types contains an unsupported source type.")
    freshness = config.get("freshness_policy") or {}
    for field in ("routine_scan_cadence_days", "refresh_after_days", "stale_after_days"):
        if not finite_positive_number(freshness.get(field)):
            raise ReferencePriceError(f"freshness_policy.{field} must be positive.")
    if freshness["stale_after_days"] < freshness["refresh_after_days"]:
        raise ReferencePriceError("stale_after_days cannot be shorter than refresh_after_days.")
    if not isinstance(freshness.get("routine_batch_size"), int) or freshness["routine_batch_size"] <= 0:
        raise ReferencePriceError("routine_batch_size must be a positive integer.")


def descriptor_text(equipment: dict[str, Any]) -> str:
    parts = [
        f"manufacturer={equipment.get('manufacturer') or 'unknown'}",
        f"model={equipment.get('model') or equipment.get('display_name') or 'unknown'}",
    ]
    for key, label in (
        ("aperture_mm", "aperture_mm"),
        ("native_focal_length_mm", "focal_length_mm"),
        ("native_focal_ratio", "focal_ratio"),
    ):
        value = equipment.get(key)
        if finite_positive_number(value):
            parts.append(f"{label}={float(value):g}")
    return ", ".join(parts)


def research_prompt(equipment: dict[str, Any]) -> str:
    return f"""Research an approximate US new-retail reference price for exactly this canonical telescope:

equipment_id={equipment['component_id']}
{descriptor_text(equipment)}

This is editorial reference data, not a live offer or shopping comparison. Search the web and identify the exact canonical sold configuration. Prefer manufacturer pages and established astronomy retailers. A current normal or unconditional sale price may be evidence. For discontinued equipment, a reproducible last-known new-retail price may be used only with price_basis=last_known_new_retail.

Reject used, open-box, refurbished, marketplace, auction, financing/monthly, coupon-dependent, deposit, reservation, accessory, reducer, flattener, focuser, mount-only, camera, and inferred bundle-equivalent prices. Do not substitute a kit or bundle for an OTA, or an OTA for an integrated telescope configuration. A newer or older generation may be used as a generation_proxy only when aperture, focal length, optical design, and sold configuration all match the canonical record; say so in reason and keep match_confidence at or below 0.94. Treat aperture variants, optical-design variants, EdgeHD/RASA/HyperStar/reducer configurations, and materially different packages as different products.

Return insufficient_evidence instead of guessing. Evidence URLs must be pages actually found by web search. The estimate should represent the typical exact-product new-retail price before shipping and tax, not the lowest anomalous price. Do not round; the publishing pipeline applies its own precision."""


ESTIMATE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "equipment_id",
        "status",
        "price_basis",
        "market_status",
        "estimated_price_usd",
        "match_confidence",
        "estimate_confidence",
        "reason",
        "evidence",
    ],
    "properties": {
        "equipment_id": {"type": "string"},
        "status": {"type": "string", "enum": ["estimated", "insufficient_evidence", "ambiguous"]},
        "price_basis": {
            "type": ["string", "null"],
            "enum": ["typical_new_retail", "last_known_new_retail", None],
        },
        "market_status": {"type": "string", "enum": sorted(MARKET_STATUSES)},
        "estimated_price_usd": {"type": ["number", "null"]},
        "match_confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "estimate_confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "reason": {"type": "string"},
        "evidence": {
            "type": "array",
            "maxItems": 8,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "url",
                    "source_type",
                    "price_usd",
                    "identity_match",
                    "qualifying_new_retail",
                    "configuration",
                ],
                "properties": {
                    "url": {"type": "string"},
                    "source_type": {"type": "string", "enum": sorted(SOURCE_TYPES)},
                    "price_usd": {"type": ["number", "null"]},
                    "identity_match": {"type": "boolean"},
                    "qualifying_new_retail": {"type": "boolean"},
                    "configuration": {
                        "type": "string",
                        "enum": sorted(EVIDENCE_CONFIGURATIONS),
                    },
                },
            },
        },
    },
}


def build_api_request(equipment: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    api = config["api"]
    return {
        "model": api["model"],
        "store": False,
        "instructions": (
            "You are a careful astronomy equipment researcher. Use web search for every estimate. "
            "Product identity and configuration accuracy are more important than coverage."
        ),
        "input": research_prompt(equipment),
        "tools": [
            {
                "type": "web_search",
                "search_context_size": api["search_context_size"],
                "user_location": {"type": "approximate", "country": "US"},
            }
        ],
        "tool_choice": "required",
        "include": ["web_search_call.action.sources"],
        "text": {
            "verbosity": "low",
            "format": {
                "type": "json_schema",
                "name": "telescope_reference_price_estimate",
                "strict": True,
                "schema": ESTIMATE_SCHEMA,
            },
        },
        "max_output_tokens": 2400,
        "metadata": {"equipment_id": equipment["component_id"][:512]},
    }


def request_api(
    equipment: dict[str, Any],
    config: dict[str, Any],
    *,
    api_key: str,
    opener: Callable[..., Any] = urllib.request.urlopen,
) -> dict[str, Any]:
    body = json.dumps(build_api_request(equipment, config), separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(
        config["api"]["endpoint"],
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    max_attempts = int(config["api"]["max_attempts"])
    timeout = float(config["api"]["timeout_seconds"])
    for attempt in range(1, max_attempts + 1):
        try:
            with opener(request, timeout=timeout) as response:
                if response.status != 200:
                    raise ReferencePriceError(f"OpenAI Responses API returned HTTP {response.status}.")
                raw = response.read(int(config["api"].get("max_response_bytes", 2_000_000)) + 1)
                if len(raw) > int(config["api"].get("max_response_bytes", 2_000_000)):
                    raise ReferencePriceError("OpenAI response exceeded the configured size cap.")
                payload = json.loads(raw)
                if not isinstance(payload, dict):
                    raise ReferencePriceError("OpenAI response was not a JSON object.")
                return payload
        except urllib.error.HTTPError as error:
            transient = error.code in {408, 409, 429, 500, 502, 503, 504}
            if not transient or attempt == max_attempts:
                raise ReferencePriceError(f"OpenAI Responses API HTTP {error.code}.") from error
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            if attempt == max_attempts:
                raise ReferencePriceError(f"OpenAI Responses API request failed: {error}") from error
        time.sleep(min(2 ** (attempt - 1), 8))
    raise ReferencePriceError("OpenAI Responses API request failed without a response.")


def response_output_text(response: dict[str, Any]) -> str:
    if isinstance(response.get("output_text"), str) and response["output_text"].strip():
        return response["output_text"]
    for item in response.get("output") or []:
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for content in item.get("content") or []:
            if isinstance(content, dict) and content.get("type") == "output_text":
                text = content.get("text")
                if isinstance(text, str) and text.strip():
                    return text
    raise ReferencePriceError("OpenAI response did not contain structured output text.")


def response_source_urls(response: dict[str, Any]) -> set[str]:
    urls: set[str] = set()
    for item in response.get("output") or []:
        if not isinstance(item, dict):
            continue
        if item.get("type") == "web_search_call":
            action = item.get("action") or {}
            for source in action.get("sources") or []:
                if isinstance(source, dict) and source.get("url"):
                    try:
                        urls.add(canonical_url(source["url"]))
                    except ReferencePriceError:
                        pass
        if item.get("type") == "message":
            for content in item.get("content") or []:
                if not isinstance(content, dict):
                    continue
                for annotation in content.get("annotations") or []:
                    if isinstance(annotation, dict) and annotation.get("url"):
                        try:
                            urls.add(canonical_url(annotation["url"]))
                        except ReferencePriceError:
                            pass
    return urls


def parse_model_estimate(response: dict[str, Any]) -> dict[str, Any]:
    if response.get("status") != "completed":
        error = response.get("error") or response.get("incomplete_details") or response.get("status")
        raise ReferencePriceError(f"OpenAI response did not complete: {error}")
    try:
        result = json.loads(response_output_text(response))
    except json.JSONDecodeError as error:
        raise ReferencePriceError("Structured estimate output was malformed JSON.") from error
    if not isinstance(result, dict):
        raise ReferencePriceError("Structured estimate output must be an object.")
    return result


def validate_estimate_response(
    equipment: dict[str, Any],
    response: dict[str, Any],
    config: dict[str, Any],
    generated_at: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    result = parse_model_estimate(response)
    equipment_id = equipment["component_id"]
    if result.get("equipment_id") != equipment_id:
        raise EstimateReviewRequired("Structured output returned the wrong canonical equipment ID.")
    if result.get("status") != "estimated":
        reason = str(result.get("reason") or result.get("status") or "insufficient evidence")
        raise EstimateReviewRequired(reason[:500])
    basis = result.get("price_basis")
    market_status = result.get("market_status")
    if basis not in PRICE_BASES or market_status not in MARKET_STATUSES:
        raise EstimateReviewRequired("Estimate basis or market status was invalid.")
    match_confidence = probability(result.get("match_confidence"), field="match_confidence")
    estimate_confidence = probability(result.get("estimate_confidence"), field="estimate_confidence")
    policy = config["estimate_policy"]
    if match_confidence < float(policy["minimum_match_confidence"]):
        raise EstimateReviewRequired("Product-identity confidence was below the publication threshold.")
    if estimate_confidence < float(policy["minimum_estimate_confidence"]):
        raise EstimateReviewRequired("Estimate confidence was below the publication threshold.")

    returned_sources = response_source_urls(response)
    if not returned_sources:
        raise EstimateReviewRequired("The web-search response did not expose any citable sources.")
    qualifying = []
    seen_source_keys = set()
    for evidence in result.get("evidence") or []:
        if not isinstance(evidence, dict):
            continue
        try:
            url = canonical_url(str(evidence.get("url") or ""))
        except ReferencePriceError:
            continue
        if url not in returned_sources:
            continue
        if (
            not evidence.get("identity_match")
            or not evidence.get("qualifying_new_retail")
            or evidence.get("configuration") not in {"exact_product", "generation_proxy"}
        ):
            continue
        source_type = evidence.get("source_type")
        if source_type not in SOURCE_TYPES or source_type == "other":
            continue
        amount = evidence.get("price_usd")
        if not finite_positive_number(amount):
            continue
        amount = float(amount)
        if not float(policy["minimum_price"]) <= amount <= float(policy["maximum_price"]):
            continue
        key = source_key(url)
        if key in seen_source_keys:
            continue
        seen_source_keys.add(key)
        qualifying.append(
            {
                "source_type": source_type,
                "source_domain": source_domain(url),
                "price_amount": round(amount, 2),
                "source_key": key,
                "configuration": evidence["configuration"],
            }
        )
    if not qualifying:
        raise EstimateReviewRequired("No qualifying evidence URL matched the returned web-search sources.")

    independent_domains = {item["source_domain"] for item in qualifying}
    if len(independent_domains) < 2:
        if qualifying[0]["source_type"] not in set(policy["single_source_allowed_types"]):
            raise EstimateReviewRequired("A single non-authoritative source is insufficient.")
        estimate_confidence = min(estimate_confidence, 0.75)
    match_basis = (
        "generation_proxy"
        if any(item["configuration"] == "generation_proxy" for item in qualifying)
        else "exact_product"
    )
    if match_basis == "generation_proxy":
        match_confidence = min(match_confidence, 0.94)
    prices = [item["price_amount"] for item in qualifying]
    median_price = float(statistics.median(prices))
    spread = (max(prices) - min(prices)) / median_price if median_price else math.inf
    if len(prices) >= 2 and spread > float(policy["maximum_evidence_spread_ratio"]):
        raise EstimateReviewRequired(f"Qualifying evidence prices disagreed by {spread:.1%}.")
    model_estimate = result.get("estimated_price_usd")
    if not finite_positive_number(model_estimate):
        raise EstimateReviewRequired("The model did not return a positive reference estimate.")
    model_difference = abs(float(model_estimate) - median_price) / median_price
    if model_difference > float(policy["maximum_model_median_difference_ratio"]):
        raise EstimateReviewRequired("The proposed estimate disagreed materially with its evidence median.")

    increment = int(policy["rounding_increment"])
    rounded_price = round_to_increment(median_price, increment)
    reason = " ".join(str(result.get("reason") or "").split())[:300] or None
    if match_basis == "generation_proxy" and "generation" not in (reason or "").casefold():
        reason = f"Same-spec generation proxy. {reason or ''}".strip()[:300]
    state_estimate = {
        "equipment_id": equipment_id,
        "estimated_at": generated_at,
        "price_amount": rounded_price,
        "currency": "USD",
        "price_basis": basis,
        "precision": increment,
        "market_status": market_status,
        "match_confidence": match_confidence,
        "estimate_confidence": estimate_confidence,
        "method": "search_grounded_evidence_median",
        "match_basis": match_basis,
        "model": config["api"]["model"],
        "evidence": [
            {
                "source_type": item["source_type"],
                "price_amount": item["price_amount"],
                "source_key": item["source_key"],
            }
            for item in qualifying
        ],
        "note": reason,
        "last_refresh_attempt_at": generated_at,
        "last_refresh_status": "success",
        "last_refresh_error": None,
        "pending_candidate": None,
    }
    transient_audit = {
        "equipment_id": equipment_id,
        "response_id": response.get("id"),
        "source_urls": sorted(returned_sources),
        "model_output": result,
    }
    return state_estimate, transient_audit


def validate_state_estimate(
    estimate: dict[str, Any], telescope_ids: set[str], config: dict[str, Any]
) -> None:
    equipment_id = str(estimate.get("equipment_id") or "")
    if equipment_id not in telescope_ids:
        raise ReferencePriceError(f"Estimate references an unknown canonical telescope: {equipment_id}")
    parse_timestamp(estimate.get("estimated_at"), field=f"{equipment_id}.estimated_at")
    parse_timestamp(
        estimate.get("last_refresh_attempt_at"), field=f"{equipment_id}.last_refresh_attempt_at"
    )
    policy = config["estimate_policy"]
    amount = estimate.get("price_amount")
    if not finite_positive_number(amount) or not float(policy["minimum_price"]) <= float(amount) <= float(
        policy["maximum_price"]
    ):
        raise ReferencePriceError(f"Estimate price is outside plausibility bounds: {equipment_id}")
    increment = int(policy["rounding_increment"])
    if int(amount) % increment:
        raise ReferencePriceError(f"Estimate is not rounded to the configured increment: {equipment_id}")
    if estimate.get("currency") != "USD" or estimate.get("price_basis") not in PRICE_BASES:
        raise ReferencePriceError(f"Estimate currency or basis is invalid: {equipment_id}")
    if estimate.get("precision") != increment or estimate.get("market_status") not in MARKET_STATUSES:
        raise ReferencePriceError(f"Estimate precision or market status is invalid: {equipment_id}")
    match_confidence = probability(
        estimate.get("match_confidence"), field=f"{equipment_id}.match_confidence"
    )
    probability(estimate.get("estimate_confidence"), field=f"{equipment_id}.estimate_confidence")
    if estimate.get("last_refresh_status") not in {"success", "failed"}:
        raise ReferencePriceError(f"Invalid refresh status: {equipment_id}")
    evidence = estimate.get("evidence") or []
    if not isinstance(evidence, list) or not evidence:
        raise ReferencePriceError(f"Estimate requires summarized evidence: {equipment_id}")
    for item in evidence:
        base_fields = {"source_type", "price_amount", "source_key"}
        conversion_fields = {"source_price", "source_currency", "usd_conversion_rate"}
        if set(item) not in {frozenset(base_fields), frozenset(base_fields | conversion_fields)}:
            raise ReferencePriceError(f"Evidence fields are invalid: {equipment_id}")
        if item["source_type"] not in SOURCE_TYPES:
            raise ReferencePriceError(f"Evidence source summary is invalid: {equipment_id}")
        if not finite_positive_number(item["price_amount"]):
            raise ReferencePriceError(f"Evidence price is invalid: {equipment_id}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(item["source_key"])):
            raise ReferencePriceError(f"Evidence source key is invalid: {equipment_id}")
        if conversion_fields <= set(item):
            if (
                not finite_positive_number(item["source_price"])
                or not finite_positive_number(item["usd_conversion_rate"])
                or not re.fullmatch(r"[A-Z]{3}", str(item["source_currency"]))
                or item["source_currency"] == "USD"
            ):
                raise ReferencePriceError(f"Evidence currency conversion is invalid: {equipment_id}")
    match_basis = estimate.get("match_basis", "exact_product")
    if match_basis not in {"exact_product", "generation_proxy"}:
        raise ReferencePriceError(f"Estimate match basis is invalid: {equipment_id}")
    if match_basis == "generation_proxy":
        if match_confidence > 0.94:
            raise ReferencePriceError(
                f"Generation-proxy confidence exceeds the documented cap: {equipment_id}"
            )
        if "generation" not in str(estimate.get("note") or "").casefold():
            raise ReferencePriceError(
                f"Generation-proxy estimate requires an explicit note: {equipment_id}"
            )


def validate_state(
    payload: dict[str, Any], telescope_ids: set[str], config: dict[str, Any]
) -> list[dict[str, Any]]:
    if payload.get("schema_version") != 1:
        raise ReferencePriceError("Estimate state must use schema_version 1.")
    estimates = payload.get("estimates") or []
    if not isinstance(estimates, list):
        raise ReferencePriceError("Estimate state requires an estimates array.")
    known_ids = payload.get("known_equipment_ids")
    if not isinstance(known_ids, list) or len(known_ids) != len(set(known_ids)):
        raise ReferencePriceError("Estimate state requires unique known_equipment_ids.")
    if not set(known_ids) <= telescope_ids:
        raise ReferencePriceError("Estimate state contains unknown known_equipment_ids.")
    attempts = payload.get("refresh_attempts")
    if not isinstance(attempts, list):
        raise ReferencePriceError("Estimate state requires a refresh_attempts array.")
    attempt_ids = set()
    for attempt in attempts:
        equipment_id = str(attempt.get("equipment_id") or "")
        if equipment_id not in telescope_ids or equipment_id in attempt_ids:
            raise ReferencePriceError(f"Refresh attempt equipment ID is invalid: {equipment_id}")
        attempt_ids.add(equipment_id)
        parse_timestamp(attempt.get("attempted_at"), field=f"{equipment_id}.attempted_at")
        if attempt.get("status") not in {"success", "review", "failed"}:
            raise ReferencePriceError(f"Refresh attempt status is invalid: {equipment_id}")
    seen = set()
    for estimate in estimates:
        if not isinstance(estimate, dict):
            raise ReferencePriceError("Every state estimate must be an object.")
        validate_state_estimate(estimate, telescope_ids, config)
        if estimate["equipment_id"] in seen:
            raise ReferencePriceError(f"Duplicate retained estimate: {estimate['equipment_id']}")
        seen.add(estimate["equipment_id"])
    return estimates


def validate_overrides(payload: dict[str, Any], telescope_ids: set[str], config: dict[str, Any]) -> None:
    if payload.get("schema_version") != 1:
        raise ReferencePriceError("Reference-price overrides must use schema_version 1.")
    seen = set()
    for override in payload.get("overrides") or []:
        equipment_id = str(override.get("equipment_id") or "")
        if equipment_id not in telescope_ids or equipment_id in seen:
            raise ReferencePriceError(f"Override equipment ID is invalid or duplicated: {equipment_id}")
        seen.add(equipment_id)
        if override.get("action") not in {"suppress", "replace"}:
            raise ReferencePriceError(f"Unsupported override action: {equipment_id}")
        if not str(override.get("note") or "").strip():
            raise ReferencePriceError(f"Override requires an explanatory note: {equipment_id}")
        if override["action"] == "replace":
            replacement = override.get("result") or {}
            record = missing_record(equipment_id)
            record.update(replacement)
            record["equipment_id"] = equipment_id
            record["manual_override"] = True
            record["note"] = override["note"]
            validate_record(record, telescope_ids, config)
    for rejection in payload.get("rejected_evidence") or []:
        if rejection.get("equipment_id") not in telescope_ids:
            raise ReferencePriceError("Rejected evidence references an unknown telescope.")
        if not re.fullmatch(r"[0-9a-f]{64}", str(rejection.get("source_key") or "")):
            raise ReferencePriceError("Rejected evidence requires a SHA-256 source key.")
        if not str(rejection.get("reason") or "").strip():
            raise ReferencePriceError("Rejected evidence requires a reason.")


def state_index(estimates: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {estimate["equipment_id"]: estimate for estimate in estimates}


def refresh_due(
    prior: dict[str, Any] | None,
    prior_attempt: dict[str, Any] | None,
    generated_at: str,
    config: dict[str, Any],
    *,
    force: bool,
) -> bool:
    if force or not prior:
        if force or not prior_attempt:
            return True
    attempt = (
        (prior_attempt or {}).get("attempted_at")
        or (prior or {}).get("last_refresh_attempt_at")
        or (prior or {}).get("estimated_at")
    )
    elapsed = parse_timestamp(generated_at, field="generated_at") - parse_timestamp(
        attempt, field="last_refresh_attempt_at"
    )
    return elapsed >= dt.timedelta(days=float(config["freshness_policy"]["refresh_after_days"]))


def mark_refresh_failure(
    prior: dict[str, Any] | None, generated_at: str, error: str
) -> dict[str, Any] | None:
    if not prior:
        return None
    retained = copy.deepcopy(prior)
    retained["last_refresh_attempt_at"] = generated_at
    retained["last_refresh_status"] = "failed"
    retained["last_refresh_error"] = str(error)[:500]
    return retained


def suspicious_price_change(
    prior: dict[str, Any] | None, candidate: dict[str, Any], config: dict[str, Any]
) -> str | None:
    if not prior:
        return None
    old = prior.get("price_amount")
    new = candidate.get("price_amount")
    if not finite_positive_number(old) or not finite_positive_number(new):
        return None
    absolute = abs(float(new) - float(old))
    ratio = absolute / float(old)
    policy = config["estimate_policy"]
    adaptive_floor = max(
        float(policy["suspicious_change_minimum_usd"]),
        float(old) * float(policy["suspicious_change_adaptive_ratio"]),
    )
    if ratio >= float(policy["suspicious_change_ratio"]) and absolute >= adaptive_floor:
        return f"Reference estimate changed {ratio:.1%} from {float(old):.0f} to {float(new):.0f}."
    return None


def missing_record(equipment_id: str) -> dict[str, Any]:
    return {
        "equipment_id": equipment_id,
        "price_amount": None,
        "currency": None,
        "price_basis": None,
        "precision": None,
        "estimated_at": None,
        "market_status": "unknown",
        "match_confidence": 0.0,
        "estimate_confidence": 0.0,
        "evidence_count": 0,
        "manual_override": False,
        "note": None,
    }


def published_estimate(estimate: dict[str, Any]) -> dict[str, Any]:
    return {
        "equipment_id": estimate["equipment_id"],
        "price_amount": estimate["price_amount"],
        "currency": estimate["currency"],
        "price_basis": estimate["price_basis"],
        "precision": estimate["precision"],
        "estimated_at": estimate["estimated_at"],
        "market_status": estimate["market_status"],
        "match_confidence": estimate["match_confidence"],
        "estimate_confidence": estimate["estimate_confidence"],
        "evidence_count": len(estimate.get("evidence") or []),
        "manual_override": False,
        "note": estimate.get("note"),
    }


def apply_override(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    if override["action"] == "suppress":
        result = missing_record(base["equipment_id"])
    else:
        result = missing_record(base["equipment_id"])
        result.update(override.get("result") or {})
        result["equipment_id"] = base["equipment_id"]
    result["manual_override"] = True
    result["note"] = str(override["note"]).strip()
    return result


def build_records(
    telescope_ids: list[str], estimates: list[dict[str, Any]], overrides: dict[str, Any]
) -> list[dict[str, Any]]:
    by_equipment = state_index(estimates)
    by_override = {item["equipment_id"]: item for item in overrides.get("overrides") or []}
    records = []
    for equipment_id in telescope_ids:
        base = (
            published_estimate(by_equipment[equipment_id])
            if equipment_id in by_equipment
            else missing_record(equipment_id)
        )
        if equipment_id in by_override:
            base = apply_override(base, by_override[equipment_id])
        records.append(base)
    return records


def validate_record(
    record: dict[str, Any], telescope_ids: set[str], config: dict[str, Any]
) -> None:
    if set(record) != PUBLIC_FIELDS:
        raise ReferencePriceError(
            f"Published fields differ; missing={sorted(PUBLIC_FIELDS - set(record))}, "
            f"extra={sorted(set(record) - PUBLIC_FIELDS)}"
        )
    equipment_id = record["equipment_id"]
    if equipment_id not in telescope_ids:
        raise ReferencePriceError(f"Published estimate references unknown telescope: {equipment_id}")
    amount = record["price_amount"]
    if amount is None:
        for field in ("currency", "price_basis", "precision", "estimated_at"):
            if record[field] is not None:
                raise ReferencePriceError(f"Missing estimate must have null {field}: {equipment_id}")
        if record["evidence_count"] != 0 and not record["manual_override"]:
            raise ReferencePriceError(f"Missing automatic estimate cannot expose evidence: {equipment_id}")
    else:
        policy = config["estimate_policy"]
        if not finite_positive_number(amount) or not float(policy["minimum_price"]) <= float(
            amount
        ) <= float(policy["maximum_price"]):
            raise ReferencePriceError(f"Published estimate is implausible: {equipment_id}")
        if int(amount) % int(policy["rounding_increment"]):
            raise ReferencePriceError(f"Published estimate is not rounded: {equipment_id}")
        if record["currency"] != "USD" or record["price_basis"] not in PRICE_BASES:
            raise ReferencePriceError(f"Published estimate currency or basis is invalid: {equipment_id}")
        if record["precision"] != int(policy["rounding_increment"]):
            raise ReferencePriceError(f"Published estimate precision is invalid: {equipment_id}")
        parse_timestamp(record["estimated_at"], field=f"{equipment_id}.estimated_at")
    if record["market_status"] not in MARKET_STATUSES:
        raise ReferencePriceError(f"Published market status is invalid: {equipment_id}")
    probability(record["match_confidence"], field=f"{equipment_id}.match_confidence")
    probability(record["estimate_confidence"], field=f"{equipment_id}.estimate_confidence")
    if not isinstance(record["evidence_count"], int) or record["evidence_count"] < 0:
        raise ReferencePriceError(f"evidence_count must be a nonnegative integer: {equipment_id}")
    if not isinstance(record["manual_override"], bool):
        raise ReferencePriceError(f"manual_override must be boolean: {equipment_id}")
    if record["note"] is not None and not isinstance(record["note"], str):
        raise ReferencePriceError(f"note must be a string or null: {equipment_id}")


def validate_package(
    package: dict[str, Any],
    telescope_ids: set[str],
    config: dict[str, Any],
    *,
    cleansed_telescope_ids: set[str] | None = None,
    smart_telescope_ids: set[str] | None = None,
) -> None:
    if package.get("schemaVersion") != PACKAGE_SCHEMA_VERSION:
        raise ReferencePriceError("Unsupported telescope reference-price schemaVersion.")
    if package.get("packageFamily") != PACKAGE_FAMILY:
        raise ReferencePriceError("Wrong telescope reference-price packageFamily.")
    parse_timestamp(package.get("generatedAt"), field="generatedAt")
    prices = package.get("referencePrices")
    if not isinstance(prices, list):
        raise ReferencePriceError("Reference-price package requires a referencePrices array.")
    seen = set()
    for record in prices:
        if not isinstance(record, dict):
            raise ReferencePriceError("Every reference-price row must be an object.")
        validate_record(record, telescope_ids, config)
        if record["equipment_id"] in seen:
            raise ReferencePriceError(f"Duplicate reference-price row: {record['equipment_id']}")
        seen.add(record["equipment_id"])
    if seen != telescope_ids:
        raise ReferencePriceError("Package must contain exactly one row per canonical telescope.")
    estimated = sum(record["price_amount"] is not None for record in prices)
    if package.get("counts", {}).get("eligible_telescopes") != len(telescope_ids):
        raise ReferencePriceError("Package eligible count is invalid.")
    if package.get("counts", {}).get("estimated_telescopes") != estimated:
        raise ReferencePriceError("Package estimated count is invalid.")
    if cleansed_telescope_ids is not None and smart_telescope_ids is not None:
        counts = package.get("counts") or {}
        if counts.get("eligible_cleansed_telescopes") != len(cleansed_telescope_ids):
            raise ReferencePriceError("Package cleansed-telescope count is invalid.")
        if counts.get("eligible_smart_telescopes") != len(smart_telescope_ids):
            raise ReferencePriceError("Package smart-telescope count is invalid.")
        catalogs = package.get("catalogs") or []
        if [item.get("packageFamily") for item in catalogs] != [
            CATALOG_FAMILY,
            SMART_CATALOG_FAMILY,
        ]:
            raise ReferencePriceError("Package canonical catalog descriptors are invalid.")


def price_scale_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    buckets = {
        "under_500": 0,
        "500_to_1999": 0,
        "2000_to_9999": 0,
        "10000_to_49999": 0,
        "50000_and_up": 0,
    }
    for record in records:
        amount = record.get("price_amount")
        if amount is None:
            continue
        if amount < 500:
            buckets["under_500"] += 1
        elif amount < 2000:
            buckets["500_to_1999"] += 1
        elif amount < 10000:
            buckets["2000_to_9999"] += 1
        elif amount < 50000:
            buckets["10000_to_49999"] += 1
        else:
            buckets["50000_and_up"] += 1
    return buckets


def build_package(
    catalog_package: dict[str, Any],
    records: list[dict[str, Any]],
    config: dict[str, Any],
    generated_at: str,
    *,
    smart_catalog_package: dict[str, Any] | None = None,
    cleansed_telescope_count: int | None = None,
    smart_telescope_count: int = 0,
) -> dict[str, Any]:
    estimated = sum(record["price_amount"] is not None for record in records)
    primary_catalog = {
        "packageFamily": catalog_package["packageFamily"],
        "packageVersion": catalog_package["packageVersion"],
        "idField": "catalog.opticalComponents[].component_id",
        "eligibleComponentType": "optical_tube",
    }
    catalogs = [primary_catalog]
    if smart_catalog_package:
        catalogs.append(
            {
                "packageFamily": smart_catalog_package["packageFamily"],
                "packageVersion": smart_catalog_package["packageVersion"],
                "idField": "catalog.categories[id=telescopes].items[].id",
                "eligibleRule": "exclude_rows_labeled_traditional_telescope",
            }
        )
    cleansed_count = (
        len(records) - smart_telescope_count
        if cleansed_telescope_count is None
        else cleansed_telescope_count
    )
    return {
        "schemaVersion": PACKAGE_SCHEMA_VERSION,
        "packageFamily": PACKAGE_FAMILY,
        "packageVersion": f"telescope-reference-prices-v1-{timestamp_token(generated_at)}",
        "generatedAt": generated_at,
        "catalog": primary_catalog,
        "catalogs": catalogs,
        "market": {
            "country": "US",
            "currency": "USD",
            "taxIncluded": False,
            "shippingIncluded": False,
        },
        "methodology": {
            "priceMeaning": "Approximate typical new-retail reference price; not a live offer.",
            "roundingIncrement": int(config["estimate_policy"]["rounding_increment"]),
            "publicSourceLinksIncluded": False,
            "affiliateLinksIncluded": False,
            "modelMemoryAloneAllowed": False,
            "generationProxyAllowed": True,
            "generationProxyRule": (
                "newer_or_older_generation_only_when_aperture_focal_length_"
                "optical_design_and_sold_configuration_match"
            ),
            "failedRefreshBehavior": "retain_last_successful_estimate_and_original_estimated_at",
        },
        "counts": {
            "eligible_telescopes": len(records),
            "eligible_cleansed_telescopes": cleansed_count,
            "eligible_smart_telescopes": smart_telescope_count,
            "estimated_telescopes": estimated,
            "missing_estimate_telescopes": len(records) - estimated,
            "manual_overrides": sum(record["manual_override"] for record in records),
            "price_scale": price_scale_counts(records),
        },
        "referencePrices": records,
    }


def package_descriptor(
    package: dict[str, Any],
    data: bytes,
    *,
    min_supported_app_version: str,
    min_supported_build: str,
) -> dict[str, Any]:
    return {
        "family": PACKAGE_FAMILY,
        "packageVersion": package["packageVersion"],
        "payloadSchemaVersion": package["schemaVersion"],
        "packageURL": METADATA_ORIGIN + PACKAGE_URL_PATH,
        "checksum": {"algorithm": "sha256", "value": hashlib.sha256(data).hexdigest()},
        "byteSize": len(data),
        "minSupportedAppVersion": min_supported_app_version,
        "minSupportedBuild": min_supported_build,
        "cacheTTLSeconds": 604800,
        "fallbackNotes": (
            "Optional approximate telescope reference prices. Values are rounded to the published precision, "
            "are not live offers, and may be null without affecting equipment publication."
        ),
    }


def manifest_sort_key(package: dict[str, Any]) -> tuple[int, int, str]:
    family = package.get("family") or package.get("packageFamily") or ""
    family_index = FAMILY_ORDER.index(family) if family in FAMILY_ORDER else len(FAMILY_ORDER)
    band = str(package.get("latitudeBand") or "")
    band_index = LATITUDE_BAND_ORDER.index(band) if band in LATITUDE_BAND_ORDER else len(
        LATITUDE_BAND_ORDER
    )
    return family_index, band_index, str(package.get("packageVersion") or "")


def update_manifest(path: Path, descriptor: dict[str, Any], generated_at: str) -> None:
    manifest = read_json(path)
    if manifest.get("schemaVersion") != 1 or not manifest.get("channel"):
        raise ReferencePriceError("Stable manifest must use schemaVersion 1 and a channel.")
    retired_families = {PACKAGE_FAMILY, "telescopeRetailPrices"}
    packages = [
        package
        for package in manifest.get("packages") or []
        if (package.get("family") or package.get("packageFamily")) not in retired_families
    ]
    packages.append(descriptor)
    manifest["generatedAt"] = generated_at
    manifest["publishedAt"] = generated_at
    manifest["packages"] = sorted(packages, key=manifest_sort_key)
    write_json(path, manifest)


def build_report(
    *,
    catalog_package: dict[str, Any],
    records: list[dict[str, Any]],
    estimates: list[dict[str, Any]],
    diagnostics: list[dict[str, Any]],
    changed: list[dict[str, Any]],
    new_ids: list[str],
    attempted_refresh_count: int,
    generated_at: str,
    config: dict[str, Any],
    smart_catalog_package: dict[str, Any] | None = None,
    smart_telescope_count: int = 0,
) -> dict[str, Any]:
    now = parse_timestamp(generated_at, field="generated_at")
    stale_after = dt.timedelta(days=float(config["freshness_policy"]["stale_after_days"]))
    stale = [
        {"equipment_id": item["equipment_id"], "estimated_at": item["estimated_at"]}
        for item in estimates
        if now - parse_timestamp(item["estimated_at"], field="estimated_at") > stale_after
    ]
    estimated = sum(record["price_amount"] is not None for record in records)
    review = [item for item in diagnostics if item.get("review_required")]
    failures = [item for item in diagnostics if item.get("category") == "source_failure"]
    catalogs = [
        {
            "package_family": catalog_package["packageFamily"],
            "package_version": catalog_package["packageVersion"],
        }
    ]
    if smart_catalog_package:
        catalogs.append(
            {
                "package_family": smart_catalog_package["packageFamily"],
                "package_version": smart_catalog_package["packageVersion"],
            }
        )
    return {
        "schema_version": 1,
        "scan_completed_at": generated_at,
        "catalog_package_family": catalog_package["packageFamily"],
        "catalog_package_version": catalog_package["packageVersion"],
        "catalogs": catalogs,
        "summary": {
            "eligible_telescope_count": len(records),
            "eligible_cleansed_telescope_count": len(records) - smart_telescope_count,
            "eligible_smart_telescope_count": smart_telescope_count,
            "attempted_refresh_count": attempted_refresh_count,
            "estimated_telescope_count": estimated,
            "missing_estimate_count": len(records) - estimated,
            "ambiguous_review_count": len(review),
            "source_failure_count": len(failures),
            "changed_estimate_count": len(changed),
            "new_telescope_record_count": len(new_ids),
            "stale_estimate_count": len(stale),
            "manual_override_count": sum(record["manual_override"] for record in records),
            "price_scale": price_scale_counts(records),
        },
        "changed_estimates": changed,
        "new_telescope_records": new_ids,
        "review_queue": review,
        "stale_estimates": stale,
        "diagnostics": diagnostics,
    }


def scan(
    *,
    catalog_package: dict[str, Any],
    telescopes: dict[str, dict[str, Any]],
    config: dict[str, Any],
    prior_estimates: list[dict[str, Any]],
    prior_attempts: list[dict[str, Any]],
    known_equipment_ids: set[str],
    overrides: dict[str, Any],
    generated_at: str,
    selected_ids: set[str] | None,
    force: bool,
    offline: bool,
    limit: int | None,
    api_key: str | None,
    requester: Callable[..., dict[str, Any]] = request_api,
    smart_catalog_package: dict[str, Any] | None = None,
    smart_telescope_ids: set[str] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    prior_index = state_index(prior_estimates)
    attempt_index = {item["equipment_id"]: item for item in prior_attempts}
    new_ids = sorted(set(telescopes) - known_equipment_ids)
    diagnostics: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []
    transient_audits: list[dict[str, Any]] = []
    refreshed_index = copy.deepcopy(prior_index)
    rejected = {
        (item["equipment_id"], item["source_key"])
        for item in overrides.get("rejected_evidence") or []
    }
    due_ids = [
        equipment_id
        for equipment_id in sorted(telescopes)
        if (selected_ids is None or equipment_id in selected_ids)
        and refresh_due(
            prior_index.get(equipment_id),
            attempt_index.get(equipment_id),
            generated_at,
            config,
            force=force,
        )
    ]
    due_ids.sort(key=lambda equipment_id: (equipment_id not in new_ids, equipment_id))
    effective_limit = limit if limit is not None else int(config["freshness_policy"]["routine_batch_size"])
    if effective_limit <= 0:
        raise ReferencePriceError("--limit must be a positive integer.")
    due_ids = due_ids[:effective_limit]
    if offline:
        due_ids = []
    if due_ids and not api_key:
        raise ReferencePriceError(
            "OPENAI_API_KEY is required for online refreshes. Use --offline to rebuild retained estimates."
        )

    for equipment_id in due_ids:
        prior = prior_index.get(equipment_id)
        try:
            response = requester(telescopes[equipment_id], config, api_key=api_key or "")
            candidate, audit = validate_estimate_response(
                telescopes[equipment_id], response, config, generated_at
            )
            candidate["evidence"] = [
                item
                for item in candidate["evidence"]
                if (equipment_id, item["source_key"]) not in rejected
            ]
            if not candidate["evidence"]:
                raise EstimateReviewRequired("All qualifying evidence was explicitly rejected by a curator.")
            if len(candidate["evidence"]) == 1:
                source_type = candidate["evidence"][0]["source_type"]
                if source_type not in set(config["estimate_policy"]["single_source_allowed_types"]):
                    raise EstimateReviewRequired(
                        "Rejected evidence left only a non-authoritative single source."
                    )
                candidate["estimate_confidence"] = min(candidate["estimate_confidence"], 0.75)
            candidate["price_amount"] = round_to_increment(
                float(statistics.median(item["price_amount"] for item in candidate["evidence"])),
                int(config["estimate_policy"]["rounding_increment"]),
            )
            suspicious = suspicious_price_change(prior, candidate, config)
            if suspicious:
                attempt_index[equipment_id] = {
                    "equipment_id": equipment_id,
                    "attempted_at": generated_at,
                    "status": "review",
                }
                if prior:
                    retained = mark_refresh_failure(prior, generated_at, suspicious)
                    assert retained is not None
                    retained["pending_candidate"] = {
                        key: candidate[key]
                        for key in (
                            "price_amount",
                            "currency",
                            "price_basis",
                            "precision",
                            "market_status",
                            "match_confidence",
                            "estimate_confidence",
                        )
                    }
                    refreshed_index[equipment_id] = retained
                diagnostics.append(
                    {
                        "category": "suspicious_price_change",
                        "equipment_id": equipment_id,
                        "message": suspicious,
                        "review_required": True,
                    }
                )
                continue
            refreshed_index[equipment_id] = candidate
            attempt_index[equipment_id] = {
                "equipment_id": equipment_id,
                "attempted_at": generated_at,
                "status": "success",
            }
            transient_audits.append(audit)
            if prior and prior.get("price_amount") != candidate.get("price_amount"):
                changed.append(
                    {
                        "equipment_id": equipment_id,
                        "previous_price_amount": prior.get("price_amount"),
                        "new_price_amount": candidate.get("price_amount"),
                    }
                )
        except EstimateReviewRequired as error:
            attempt_index[equipment_id] = {
                "equipment_id": equipment_id,
                "attempted_at": generated_at,
                "status": "review",
            }
            retained = mark_refresh_failure(prior, generated_at, str(error))
            if retained:
                refreshed_index[equipment_id] = retained
            diagnostics.append(
                {
                    "category": "ambiguous_or_insufficient",
                    "equipment_id": equipment_id,
                    "message": str(error),
                    "review_required": True,
                }
            )
        except Exception as error:  # isolate one telescope/API failure from all others
            attempt_index[equipment_id] = {
                "equipment_id": equipment_id,
                "attempted_at": generated_at,
                "status": "failed",
            }
            retained = mark_refresh_failure(prior, generated_at, str(error))
            if retained:
                refreshed_index[equipment_id] = retained
            diagnostics.append(
                {
                    "category": "source_failure",
                    "equipment_id": equipment_id,
                    "message": str(error)[:500],
                    "review_required": False,
                }
            )

    estimates = [refreshed_index[key] for key in sorted(refreshed_index)]
    state_payload = {
        "schema_version": 1,
        "catalog_package_family": catalog_package["packageFamily"],
        "catalog_package_version": catalog_package["packageVersion"],
        "last_scan_completed_at": generated_at,
        "known_equipment_ids": sorted(telescopes),
        "refresh_attempts": [attempt_index[key] for key in sorted(attempt_index)],
        "estimates": estimates,
    }
    if smart_catalog_package:
        state_payload["smart_catalog_package_family"] = smart_catalog_package["packageFamily"]
        state_payload["smart_catalog_package_version"] = smart_catalog_package["packageVersion"]
    records = build_records(sorted(telescopes), estimates, overrides)
    report = build_report(
        catalog_package=catalog_package,
        records=records,
        estimates=estimates,
        diagnostics=diagnostics,
        changed=changed,
        new_ids=new_ids,
        attempted_refresh_count=len(due_ids),
        generated_at=generated_at,
        config=config,
        smart_catalog_package=smart_catalog_package,
        smart_telescope_count=len(smart_telescope_ids or set()),
    )
    return records, {
        "state": state_payload,
        "report": report,
        "transient_audits": transient_audits,
    }


def validate_manifest_descriptor(manifest: dict[str, Any], package_path: Path) -> None:
    if manifest.get("schemaVersion") != 1 or not manifest.get("channel"):
        raise ReferencePriceError("Stable manifest must use schemaVersion 1 and a channel.")
    parse_timestamp(manifest.get("generatedAt"), field="manifest.generatedAt")
    parse_timestamp(manifest.get("publishedAt"), field="manifest.publishedAt")
    descriptors = [
        item
        for item in manifest.get("packages") or []
        if (item.get("family") or item.get("packageFamily")) == PACKAGE_FAMILY
    ]
    if len(descriptors) != 1:
        raise ReferencePriceError("Stable manifest must contain exactly one reference-price descriptor.")
    descriptor = descriptors[0]
    if descriptor.get("packageURL") != METADATA_ORIGIN + PACKAGE_URL_PATH:
        raise ReferencePriceError("Reference-price manifest packageURL is invalid.")
    if descriptor.get("payloadSchemaVersion") != PACKAGE_SCHEMA_VERSION:
        raise ReferencePriceError("Reference-price manifest payload schema is invalid.")
    data = package_path.read_bytes()
    if descriptor.get("byteSize") != len(data):
        raise ReferencePriceError("Reference-price manifest byteSize does not match the package.")
    checksum = hashlib.sha256(data).hexdigest()
    if descriptor.get("checksum") != {"algorithm": "sha256", "value": checksum}:
        raise ReferencePriceError("Reference-price manifest checksum does not match the package.")
    retired = [
        item
        for item in manifest.get("packages") or []
        if (item.get("family") or item.get("packageFamily")) == "telescopeRetailPrices"
    ]
    if retired:
        raise ReferencePriceError("Retired telescopeRetailPrices descriptors must not remain published.")
    if manifest.get("packages") != sorted(manifest.get("packages") or [], key=manifest_sort_key):
        raise ReferencePriceError("Stable manifest package ordering is not deterministic.")


def main() -> int:
    args = parse_args()
    generated_at = args.generated_at or utc_now()
    parse_timestamp(generated_at, field="generated_at")
    config = read_json(args.config)
    validate_config(config)
    catalog_package, cleansed_telescopes = load_catalog(args.catalog)
    smart_catalog_package, smart_telescopes = load_smart_catalog(args.smart_catalog)
    telescopes = merge_canonical_telescopes(cleansed_telescopes, smart_telescopes)
    telescope_ids = set(telescopes)
    state_payload = read_json(args.state)
    estimates = validate_state(state_payload, telescope_ids, config)
    overrides = read_json(args.overrides)
    validate_overrides(overrides, telescope_ids, config)

    if args.validate_only:
        package = read_json(args.output)
        validate_package(
            package,
            telescope_ids,
            config,
            cleansed_telescope_ids=set(cleansed_telescopes),
            smart_telescope_ids=set(smart_telescopes),
        )
        validate_manifest_descriptor(read_json(args.manifest), args.output)
        print(
            f"Validated {len(package['referencePrices'])} canonical telescope reference-price rows."
        )
        return 0

    selected_ids = set(args.equipment_ids or []) or None
    if selected_ids:
        unknown = selected_ids - telescope_ids
        if unknown:
            raise ReferencePriceError(f"Unknown canonical equipment IDs: {sorted(unknown)}")
    records, scan_result = scan(
        catalog_package=catalog_package,
        telescopes=telescopes,
        config=config,
        prior_estimates=estimates,
        prior_attempts=state_payload["refresh_attempts"],
        known_equipment_ids=set(state_payload["known_equipment_ids"]),
        overrides=overrides,
        generated_at=generated_at,
        selected_ids=selected_ids,
        force=args.force,
        offline=args.offline,
        limit=args.limit,
        api_key=os.environ.get("OPENAI_API_KEY"),
        smart_catalog_package=smart_catalog_package,
        smart_telescope_ids=set(smart_telescopes),
    )
    summary = scan_result["report"]["summary"]
    if not args.offline and summary["attempted_refresh_count"] == 0:
        print(json.dumps(summary, indent=2, sort_keys=False))
        print("No reference-price records were due; generated files were left unchanged.")
        return 0
    validate_state(scan_result["state"], telescope_ids, config)
    for record in records:
        validate_record(record, telescope_ids, config)
    package = build_package(
        catalog_package,
        records,
        config,
        generated_at,
        smart_catalog_package=smart_catalog_package,
        cleansed_telescope_count=len(cleansed_telescopes),
        smart_telescope_count=len(smart_telescopes),
    )
    validate_package(
        package,
        telescope_ids,
        config,
        cleansed_telescope_ids=set(cleansed_telescopes),
        smart_telescope_ids=set(smart_telescopes),
    )
    write_json(args.state, scan_result["state"])
    package_data = write_json(args.output, package)
    descriptor = package_descriptor(
        package,
        package_data,
        min_supported_app_version=args.min_supported_app_version,
        min_supported_build=args.min_supported_build,
    )
    update_manifest(args.manifest, descriptor, generated_at)
    write_json(args.report, scan_result["report"])
    print(json.dumps(summary, indent=2, sort_keys=False))
    if scan_result["transient_audits"]:
        print(
            "Exact research URLs were validated transiently and intentionally not written to the repository.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReferencePriceError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
