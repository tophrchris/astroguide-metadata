#!/usr/bin/env python3
"""Import curator-reviewed telescope reference-price evidence.

The input is intentionally transient: it may contain exact source URLs needed
to establish evidence, but only source type, price, and an opaque URL hash are
written to repository state. This provides a deterministic bulk-import lane
without turning the public metadata repository into a retailer directory.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any

import update_telescope_reference_prices as prices


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Import curator-reviewed, exact-product reference-price evidence."
    )
    parser.add_argument("input", type=Path, help="Transient curated evidence JSON.")
    parser.add_argument("--catalog", type=Path, default=prices.DEFAULT_CATALOG)
    parser.add_argument("--smart-catalog", type=Path, default=prices.DEFAULT_SMART_CATALOG)
    parser.add_argument("--config", type=Path, default=prices.DEFAULT_CONFIG)
    parser.add_argument("--state", type=Path, default=prices.DEFAULT_STATE)
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Allow imported records to replace retained estimates for the same IDs.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the validated import. Without this flag, perform a dry run.",
    )
    return parser.parse_args()


def load_import(path: Path) -> dict[str, Any]:
    payload = prices.read_json(path)
    if payload.get("schema_version") != 1:
        raise prices.ReferencePriceError("Curated import must use schema_version 1.")
    prices.parse_timestamp(payload.get("observed_at"), field="observed_at")
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise prices.ReferencePriceError("Curated import requires a nonempty records array.")
    return payload


def import_estimate(
    record: dict[str, Any],
    *,
    observed_at: str,
    telescope_ids: set[str],
    config: dict[str, Any],
) -> dict[str, Any]:
    allowed_fields = {
        "equipment_id",
        "price_usd",
        "source_price",
        "source_currency",
        "usd_conversion_rate",
        "price_basis",
        "market_status",
        "match_basis",
        "match_confidence",
        "estimate_confidence",
        "source_type",
        "source_url",
        "note",
    }
    if set(record) - allowed_fields:
        raise prices.ReferencePriceError(
            f"Curated record has unsupported fields: {sorted(set(record) - allowed_fields)}"
        )
    equipment_id = str(record.get("equipment_id") or "")
    if equipment_id not in telescope_ids:
        raise prices.ReferencePriceError(
            f"Curated record references an unknown canonical telescope: {equipment_id}"
        )
    policy = config["estimate_policy"]
    direct_amount = record.get("price_usd")
    converted_fields = {
        "source_price",
        "source_currency",
        "usd_conversion_rate",
    }
    has_converted_fields = any(field in record for field in converted_fields)
    if direct_amount is not None and has_converted_fields:
        raise prices.ReferencePriceError(
            f"Curated evidence must use price_usd or source-currency fields, not both: {equipment_id}"
        )
    conversion_evidence: dict[str, Any] = {}
    if has_converted_fields:
        if not converted_fields <= set(record):
            raise prices.ReferencePriceError(
                f"Curated source-currency evidence is incomplete: {equipment_id}"
            )
        source_price = record.get("source_price")
        source_currency = str(record.get("source_currency") or "")
        conversion_rate = record.get("usd_conversion_rate")
        if (
            not prices.finite_positive_number(source_price)
            or not prices.finite_positive_number(conversion_rate)
            or not re.fullmatch(r"[A-Z]{3}", source_currency)
            or source_currency == "USD"
        ):
            raise prices.ReferencePriceError(
                f"Curated source-currency evidence is invalid: {equipment_id}"
            )
        amount = round(float(source_price) * float(conversion_rate), 2)
        conversion_evidence = {
            "source_price": round(float(source_price), 2),
            "source_currency": source_currency,
            "usd_conversion_rate": round(float(conversion_rate), 6),
        }
    else:
        amount = direct_amount
    if not prices.finite_positive_number(amount) or not float(policy["minimum_price"]) <= float(
        amount
    ) <= float(policy["maximum_price"]):
        raise prices.ReferencePriceError(f"Curated evidence price is implausible: {equipment_id}")
    basis = record.get("price_basis")
    market_status = record.get("market_status")
    if basis not in prices.PRICE_BASES or market_status not in prices.MARKET_STATUSES:
        raise prices.ReferencePriceError(
            f"Curated price basis or market status is invalid: {equipment_id}"
        )
    if basis == "last_known_new_retail" and market_status != "discontinued":
        raise prices.ReferencePriceError(
            f"Last-known new-retail evidence must be discontinued: {equipment_id}"
        )
    source_type = record.get("source_type")
    if source_type not in prices.SOURCE_TYPES - {"other"}:
        raise prices.ReferencePriceError(f"Curated source type is invalid: {equipment_id}")
    url = prices.canonical_url(str(record.get("source_url") or ""))
    match_confidence = prices.probability(
        record.get("match_confidence"), field=f"{equipment_id}.match_confidence"
    )
    estimate_confidence = prices.probability(
        record.get("estimate_confidence"), field=f"{equipment_id}.estimate_confidence"
    )
    if match_confidence < float(policy["minimum_match_confidence"]):
        raise prices.ReferencePriceError(
            f"Curated product-identity confidence is below threshold: {equipment_id}"
        )
    if estimate_confidence < float(policy["minimum_estimate_confidence"]):
        raise prices.ReferencePriceError(
            f"Curated estimate confidence is below threshold: {equipment_id}"
        )
    match_basis = record.get("match_basis", "exact_product")
    if match_basis not in {"exact_product", "generation_proxy"}:
        raise prices.ReferencePriceError(f"Curated match basis is invalid: {equipment_id}")
    if match_basis == "generation_proxy":
        match_confidence = min(match_confidence, 0.94)
    increment = int(policy["rounding_increment"])
    note = " ".join(str(record.get("note") or "").split())[:300] or None
    if match_basis == "generation_proxy" and "generation" not in (note or "").casefold():
        note = f"Same-spec generation proxy. {note or ''}".strip()[:300]
    estimate = {
        "equipment_id": equipment_id,
        "estimated_at": observed_at,
        "price_amount": prices.round_to_increment(float(amount), increment),
        "currency": "USD",
        "price_basis": basis,
        "precision": increment,
        "market_status": market_status,
        "match_confidence": match_confidence,
        "estimate_confidence": min(estimate_confidence, 0.75),
        "method": "curated_structured_source",
        "match_basis": match_basis,
        "model": None,
        "evidence": [
            {
                "source_type": source_type,
                "price_amount": round(float(amount), 2),
                "source_key": prices.source_key(url),
                **conversion_evidence,
            }
        ],
        "note": note,
        "last_refresh_attempt_at": observed_at,
        "last_refresh_status": "success",
        "last_refresh_error": None,
        "pending_candidate": None,
    }
    prices.validate_state_estimate(estimate, telescope_ids, config)
    return estimate


def merge_import(
    state: dict[str, Any],
    imported: list[dict[str, Any]],
    *,
    observed_at: str,
    telescope_ids: set[str],
    config: dict[str, Any],
    replace_existing: bool,
) -> dict[str, Any]:
    result = copy.deepcopy(state)
    by_id = prices.state_index(result.get("estimates") or [])
    duplicates = sorted(item["equipment_id"] for item in imported if item["equipment_id"] in by_id)
    if duplicates and not replace_existing:
        raise prices.ReferencePriceError(
            "Curated import would replace retained estimates without --replace-existing: "
            + ", ".join(duplicates[:10])
        )
    for item in imported:
        by_id[item["equipment_id"]] = item
    result["last_scan_completed_at"] = observed_at
    result["estimates"] = [by_id[key] for key in sorted(by_id)]
    prices.validate_state(result, telescope_ids, config)
    return result


def main() -> int:
    args = parse_args()
    payload = load_import(args.input)
    config = prices.read_json(args.config)
    prices.validate_config(config)
    _, cleansed_telescopes = prices.load_catalog(args.catalog)
    _, smart_telescopes = prices.load_smart_catalog(args.smart_catalog)
    telescopes = prices.merge_canonical_telescopes(cleansed_telescopes, smart_telescopes)
    telescope_ids = set(telescopes)
    state = prices.read_json(args.state)
    prices.validate_state(state, telescope_ids, config)
    seen: set[str] = set()
    imported = []
    for record in payload["records"]:
        if not isinstance(record, dict):
            raise prices.ReferencePriceError("Every curated import record must be an object.")
        estimate = import_estimate(
            record,
            observed_at=payload["observed_at"],
            telescope_ids=telescope_ids,
            config=config,
        )
        if estimate["equipment_id"] in seen:
            raise prices.ReferencePriceError(
                f"Curated import contains a duplicate ID: {estimate['equipment_id']}"
            )
        seen.add(estimate["equipment_id"])
        imported.append(estimate)
    merged = merge_import(
        state,
        imported,
        observed_at=payload["observed_at"],
        telescope_ids=telescope_ids,
        config=config,
        replace_existing=args.replace_existing,
    )
    if args.write:
        prices.write_json(args.state, merged)
    action = "Imported" if args.write else "Validated"
    print(
        f"{action} {len(imported)} curated reference-price records; "
        f"retained total would be {len(merged['estimates'])}."
    )
    print("Exact source URLs were intentionally not written to repository state.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except prices.ReferencePriceError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
