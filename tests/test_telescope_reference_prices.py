import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_telescope_reference_prices.py"
FIXTURES = ROOT / "tests" / "fixtures" / "telescope-reference-prices"
SPEC = importlib.util.spec_from_file_location("telescope_reference_prices", SCRIPT)
prices = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = prices
SPEC.loader.exec_module(prices)


def fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def config():
    return {
        "schema_version": 1,
        "api": {
            "endpoint": "https://api.openai.com/v1/responses",
            "model": "gpt-5.4-mini-2026-03-17",
            "search_context_size": "medium",
            "timeout_seconds": 30,
            "max_attempts": 2,
            "max_response_bytes": 100000,
        },
        "estimate_policy": {
            "country": "US",
            "currency": "USD",
            "rounding_increment": 50,
            "minimum_price": 25,
            "maximum_price": 750000,
            "minimum_match_confidence": 0.9,
            "minimum_estimate_confidence": 0.65,
            "single_source_allowed_types": [
                "manufacturer",
                "astronomy_specialty_retailer",
            ],
            "maximum_evidence_spread_ratio": 0.3,
            "maximum_model_median_difference_ratio": 0.2,
            "suspicious_change_ratio": 0.35,
            "suspicious_change_minimum_usd": 250,
            "suspicious_change_adaptive_ratio": 0.1,
        },
        "freshness_policy": {
            "routine_scan_cadence_days": 7,
            "routine_batch_size": 50,
            "refresh_after_days": 120,
            "stale_after_days": 180,
        },
    }


def equipment(equipment_id="scope-1"):
    return {
        "component_id": equipment_id,
        "component_type": "optical_tube",
        "manufacturer": "Example Optics",
        "model": "Exact 100 OTA",
        "display_name": "Example Optics Exact 100 OTA",
        "aperture_mm": 100,
        "native_focal_length_mm": 500,
        "native_focal_ratio": 5,
    }


def result_response(**updates):
    result = {
        "equipment_id": "scope-1",
        "status": "estimated",
        "price_basis": "typical_new_retail",
        "market_status": "current",
        "estimated_price_usd": 1000,
        "match_confidence": 0.98,
        "estimate_confidence": 0.85,
        "reason": "Exact product identity and configuration.",
        "evidence": [
            {
                "url": "https://maker.example/products/scope-1",
                "source_type": "manufacturer",
                "price_usd": 999,
                "identity_match": True,
                "qualifying_new_retail": True,
                "configuration": "exact_product",
            }
        ],
    }
    result.update(updates)
    return {
        "id": "resp_test",
        "status": "completed",
        "output": [
            {
                "type": "web_search_call",
                "action": {
                    "sources": [
                        {"url": item["url"]}
                        for item in result.get("evidence", [])
                    ]
                },
            },
            {
                "type": "message",
                "content": [
                    {"type": "output_text", "text": json.dumps(result)}
                ],
            },
        ],
    }


def retained_estimate(**updates):
    result = {
        "equipment_id": "scope-1",
        "estimated_at": "2026-01-01T00:00:00Z",
        "price_amount": 1000,
        "currency": "USD",
        "price_basis": "typical_new_retail",
        "precision": 50,
        "market_status": "current",
        "match_confidence": 0.98,
        "estimate_confidence": 0.85,
        "method": "search_grounded_evidence_median",
        "model": "gpt-5.4-mini-2026-03-17",
        "evidence": [
            {
                "source_type": "manufacturer",
                "price_amount": 999,
                "source_key": "a" * 64,
            }
        ],
        "note": None,
        "last_refresh_attempt_at": "2026-01-01T00:00:00Z",
        "last_refresh_status": "success",
        "last_refresh_error": None,
        "pending_candidate": None,
    }
    result.update(updates)
    return result


def smart_catalog_package():
    return {
        "schemaVersion": 1,
        "packageFamily": "equipmentCatalog",
        "packageVersion": "equipment-catalog-v1-fixture",
        "catalog": {
            "categories": [
                {
                    "id": "telescopes",
                    "items": [
                        {
                            "id": "smart-scope-1",
                            "manufacturer": "Example Smart",
                            "name": "Smart Scope 1",
                            "aperture_mm": 50,
                            "focal_length_mm": 250,
                            "notes": "Canonical smart telescope.",
                        },
                        {
                            "id": "legacy-traditional-1",
                            "manufacturer": "Example",
                            "name": "Traditional Scope",
                            "notes": "Traditional telescope: retained for compatibility.",
                        },
                    ],
                }
            ]
        },
    }


class TelescopeReferencePriceTests(unittest.TestCase):
    def test_curator_coverage_batch_publishes_exactly_100_reviewable_prices(self):
        overrides = prices.read_json(prices.DEFAULT_OVERRIDES)["overrides"]
        self.assertEqual(len(overrides), 100)
        self.assertEqual(len({item["equipment_id"] for item in overrides}), 100)
        retained_ids = {
            item["equipment_id"]
            for item in prices.read_json(prices.DEFAULT_STATE)["estimates"]
        }
        self.assertTrue(
            retained_ids.isdisjoint(item["equipment_id"] for item in overrides)
        )

        published_package = prices.read_json(prices.DEFAULT_PACKAGE)
        manual = [
            record
            for record in published_package["referencePrices"]
            if record["manual_override"]
        ]
        self.assertEqual(len(manual), 100)
        self.assertTrue(all(record["price_amount"] > 0 for record in manual))
        self.assertTrue(all(record["price_amount"] % 50 == 0 for record in manual))
        self.assertTrue(all(record["evidence_count"] == 0 for record in manual))
        self.assertEqual(
            sum(record["market_status"] == "current" for record in manual),
            36,
        )
        self.assertEqual(
            sum(record["market_status"] == "discontinued" for record in manual),
            64,
        )

    def test_seestar_s50_pro_launch_profile_and_price_are_published(self):
        smart_package = prices.read_json(prices.DEFAULT_SMART_CATALOG)
        telescope_items = next(
            category["items"]
            for category in smart_package["catalog"]["categories"]
            if category["id"] == "telescopes"
        )
        profile = next(
            item for item in telescope_items if item["id"] == "zwo-seestar-s50-pro"
        )
        self.assertEqual(profile["aperture_mm"], 50)
        self.assertEqual(profile["focal_length_mm"], 260)
        self.assertEqual(profile["sensor_model"], "IMX585")
        self.assertEqual(profile["native_resolution_width_px"], 2160)
        self.assertEqual(profile["native_resolution_height_px"], 3840)

        published_package = prices.read_json(prices.DEFAULT_PACKAGE)
        published = next(
            record
            for record in published_package["referencePrices"]
            if record["equipment_id"] == "zwo-seestar-s50-pro"
        )
        self.assertEqual(published["price_amount"], 900)
        self.assertEqual(published["precision"], 50)
        self.assertEqual(published["market_status"], "current")

    def test_smart_catalog_uses_canonical_ids_and_excludes_labeled_traditional_rows(self):
        telescopes = prices.smart_telescopes_from_package(smart_catalog_package())
        self.assertEqual(set(telescopes), {"smart-scope-1"})
        smart = telescopes["smart-scope-1"]
        self.assertEqual(smart["component_id"], "smart-scope-1")
        self.assertEqual(smart["component_type"], "smart_telescope")
        self.assertEqual(smart["native_focal_ratio"], 5.0)

    def test_canonical_catalog_union_rejects_duplicate_ids(self):
        with self.assertRaisesRegex(prices.ReferencePriceError, "overlap"):
            prices.merge_canonical_telescopes(
                {"duplicate": equipment("duplicate")},
                {"duplicate": equipment("duplicate")},
            )

    def test_package_describes_both_canonical_catalogs(self):
        records = [prices.missing_record("clean-1"), prices.missing_record("smart-1")]
        package = prices.build_package(
            {
                "packageFamily": "astrophotographyEquipmentSanitizedCatalog",
                "packageVersion": "clean-v1",
            },
            records,
            config(),
            "2026-08-25T12:00:00Z",
            smart_catalog_package=smart_catalog_package(),
            cleansed_telescope_count=1,
            smart_telescope_count=1,
        )
        prices.validate_package(
            package,
            {"clean-1", "smart-1"},
            config(),
            cleansed_telescope_ids={"clean-1"},
            smart_telescope_ids={"smart-1"},
        )
        self.assertEqual(package["catalog"], package["catalogs"][0])
        self.assertEqual(package["counts"]["eligible_smart_telescopes"], 1)

    def test_request_is_search_grounded_structured_and_not_stored(self):
        request = prices.build_api_request(equipment(), config())
        self.assertFalse(request["store"])
        self.assertEqual(request["tool_choice"], "required")
        self.assertEqual(request["tools"][0]["type"], "web_search")
        self.assertTrue(request["text"]["format"]["strict"])
        schema = request["text"]["format"]["schema"]
        evidence = schema["properties"]["evidence"]["items"]
        self.assertIn("configuration", evidence["required"])

    def test_exact_product_uses_evidence_median_and_nearest_50(self):
        estimate, audit = prices.validate_estimate_response(
            equipment(), fixture("exact_two_sources.json"), config(), "2026-08-24T20:00:00Z"
        )
        self.assertEqual(estimate["price_amount"], 1000)
        self.assertEqual(len(estimate["evidence"]), 2)
        self.assertEqual(audit["response_id"], "resp_fixture_exact")

    def test_same_spec_generation_proxy_is_labeled_and_confidence_capped(self):
        response = result_response(match_confidence=0.99)
        output = json.loads(response["output"][1]["content"][0]["text"])
        output["evidence"][0]["configuration"] = "generation_proxy"
        output["reason"] = (
            "Same aperture, focal length, optical design, and sold configuration."
        )
        response["output"][1]["content"][0]["text"] = json.dumps(output)
        estimate, _ = prices.validate_estimate_response(
            equipment(), response, config(), "2026-08-24T20:00:00Z"
        )
        self.assertEqual(estimate["match_basis"], "generation_proxy")
        self.assertEqual(estimate["match_confidence"], 0.94)
        self.assertIn("generation proxy", estimate["note"].casefold())

    def test_retained_generation_proxy_requires_label_and_confidence_cap(self):
        proxy = retained_estimate(
            match_basis="generation_proxy",
            match_confidence=0.95,
            note="Same-spec generation proxy.",
        )
        with self.assertRaisesRegex(prices.ReferencePriceError, "documented cap"):
            prices.validate_state_estimate(proxy, {"scope-1"}, config())

        proxy["match_confidence"] = 0.94
        proxy["note"] = None
        with self.assertRaisesRegex(prices.ReferencePriceError, "explicit note"):
            prices.validate_state_estimate(proxy, {"scope-1"}, config())

    def test_retained_and_public_data_omit_source_names_and_urls(self):
        estimate, _ = prices.validate_estimate_response(
            equipment(), fixture("exact_two_sources.json"), config(), "2026-08-24T20:00:00Z"
        )
        serialized = json.dumps(estimate)
        self.assertNotIn("http", serialized)
        self.assertNotIn("maker.example", serialized)
        public = prices.published_estimate(estimate)
        self.assertEqual(set(public), prices.PUBLIC_FIELDS)
        self.assertFalse(any("url" in field or "retailer" in field for field in public))

    def test_wrong_equipment_id_is_not_guessed(self):
        with self.assertRaises(prices.EstimateReviewRequired):
            prices.validate_estimate_response(
                equipment(),
                result_response(equipment_id="near-name-different-generation"),
                config(),
                "2026-08-24T20:00:00Z",
            )

    def test_ota_bundle_is_rejected(self):
        with self.assertRaisesRegex(prices.EstimateReviewRequired, "No qualifying evidence"):
            prices.validate_estimate_response(
                equipment(), fixture("bundle_only.json"), config(), "2026-08-24T20:00:00Z"
            )

    def test_used_refurbished_marketplace_financing_and_accessory_are_rejected(self):
        for configuration in (
            "used_or_refurbished",
            "marketplace",
            "financing_or_deposit",
            "accessory",
        ):
            response = result_response()
            output = json.loads(response["output"][1]["content"][0]["text"])
            output["evidence"][0]["configuration"] = configuration
            response["output"][1]["content"][0]["text"] = json.dumps(output)
            with self.subTest(configuration=configuration):
                with self.assertRaises(prices.EstimateReviewRequired):
                    prices.validate_estimate_response(
                        equipment(), response, config(), "2026-08-24T20:00:00Z"
                    )

    def test_uncited_url_is_rejected(self):
        response = result_response()
        response["output"][0]["action"]["sources"] = [
            {"url": "https://different.example/not-the-evidence"}
        ]
        with self.assertRaises(prices.EstimateReviewRequired):
            prices.validate_estimate_response(
                equipment(), response, config(), "2026-08-24T20:00:00Z"
            )

    def test_single_authoritative_source_caps_estimate_confidence(self):
        estimate, _ = prices.validate_estimate_response(
            equipment(), result_response(estimate_confidence=0.99), config(), "2026-08-24T20:00:00Z"
        )
        self.assertEqual(estimate["estimate_confidence"], 0.75)

    def test_single_other_source_is_insufficient(self):
        evidence = copy.deepcopy(
            json.loads(result_response()["output"][1]["content"][0]["text"])["evidence"]
        )
        evidence[0]["source_type"] = "other"
        with self.assertRaises(prices.EstimateReviewRequired):
            prices.validate_estimate_response(
                equipment(), result_response(evidence=evidence), config(), "2026-08-24T20:00:00Z"
            )

    def test_discontinued_last_known_price_is_supported(self):
        estimate, _ = prices.validate_estimate_response(
            equipment(),
            result_response(
                price_basis="last_known_new_retail",
                market_status="discontinued",
            ),
            config(),
            "2026-08-24T20:00:00Z",
        )
        self.assertEqual(estimate["market_status"], "discontinued")
        self.assertEqual(estimate["price_basis"], "last_known_new_retail")

    def test_insufficient_evidence_surfaces_review(self):
        with self.assertRaisesRegex(prices.EstimateReviewRequired, "Ambiguous generation"):
            prices.validate_estimate_response(
                equipment(),
                result_response(
                    status="ambiguous",
                    price_basis=None,
                    estimated_price_usd=None,
                    reason="Ambiguous generation",
                    evidence=[],
                ),
                config(),
                "2026-08-24T20:00:00Z",
            )

    def test_malformed_structured_output_isolated_as_error(self):
        with self.assertRaises(prices.ReferencePriceError):
            prices.validate_estimate_response(
                equipment(), fixture("malformed.json"), config(), "2026-08-24T20:00:00Z"
            )

    def test_suspicious_change_is_flagged_but_small_change_is_allowed(self):
        prior = retained_estimate(price_amount=1000)
        self.assertIsNone(
            prices.suspicious_price_change(prior, retained_estimate(price_amount=1100), config())
        )
        message = prices.suspicious_price_change(
            prior, retained_estimate(price_amount=500), config()
        )
        self.assertIn("50.0%", message)

    def test_failed_refresh_retains_original_estimate_timestamp(self):
        prior = retained_estimate()
        retained = prices.mark_refresh_failure(prior, "2026-08-24T20:00:00Z", "source failed")
        self.assertEqual(retained["price_amount"], 1000)
        self.assertEqual(retained["estimated_at"], "2026-01-01T00:00:00Z")
        self.assertEqual(retained["last_refresh_attempt_at"], "2026-08-24T20:00:00Z")
        self.assertEqual(retained["last_refresh_status"], "failed")

    def test_recent_missing_attempt_does_not_starve_later_catalog_batches(self):
        recent_attempt = {
            "equipment_id": "scope-1",
            "attempted_at": "2026-08-20T00:00:00Z",
            "status": "review",
        }
        self.assertFalse(
            prices.refresh_due(
                None,
                recent_attempt,
                "2026-08-24T20:00:00Z",
                config(),
                force=False,
            )
        )
        self.assertTrue(
            prices.refresh_due(
                None,
                recent_attempt,
                "2026-12-24T20:00:00Z",
                config(),
                force=False,
            )
        )

    def test_manual_suppress_and_replace_survive_generated_results(self):
        automatic = prices.published_estimate(retained_estimate())
        suppressed = prices.apply_override(
            automatic,
            {"action": "suppress", "note": "Configuration disputed."},
        )
        self.assertTrue(suppressed["manual_override"])
        self.assertIsNone(suppressed["price_amount"])
        replaced = prices.apply_override(
            automatic,
            {
                "action": "replace",
                "note": "Curator-reviewed correction.",
                "result": {
                    "price_amount": 25000,
                    "currency": "USD",
                    "price_basis": "typical_new_retail",
                    "precision": 50,
                    "estimated_at": "2026-08-24T20:00:00Z",
                    "market_status": "current",
                    "match_confidence": 1.0,
                    "estimate_confidence": 1.0,
                    "evidence_count": 1,
                },
            },
        )
        self.assertEqual(replaced["price_amount"], 25000)
        self.assertTrue(replaced["manual_override"])

    def test_missing_price_is_a_valid_complete_contract_row(self):
        missing = prices.missing_record("scope-1")
        prices.validate_record(missing, {"scope-1"}, config())
        self.assertIsNone(missing["price_amount"])
        self.assertEqual(missing["market_status"], "unknown")

    def test_one_request_failure_does_not_erase_another_estimate(self):
        telescopes = {"scope-1": equipment(), "scope-2": equipment("scope-2")}

        def requester(item, _config, *, api_key):
            if item["component_id"] == "scope-1":
                raise prices.ReferencePriceError("fixture source failure")
            return result_response(equipment_id="scope-2")

        records, result = prices.scan(
            catalog_package={
                "packageFamily": "astrophotographyEquipmentSanitizedCatalog",
                "packageVersion": "fixture-catalog-v1",
            },
            telescopes=telescopes,
            config=config(),
            prior_estimates=[retained_estimate()],
            prior_attempts=[],
            known_equipment_ids={"scope-1"},
            overrides={"schema_version": 1, "overrides": [], "rejected_evidence": []},
            generated_at="2026-08-24T20:00:00Z",
            selected_ids=None,
            force=True,
            offline=False,
            limit=None,
            api_key="fixture-key",
            requester=requester,
        )
        by_id = {record["equipment_id"]: record for record in records}
        self.assertEqual(by_id["scope-1"]["price_amount"], 1000)
        self.assertEqual(by_id["scope-2"]["price_amount"], 1000)
        self.assertEqual(result["report"]["summary"]["source_failure_count"], 1)
        self.assertEqual(result["report"]["summary"]["new_telescope_record_count"], 1)

    def test_rejected_evidence_is_removed_before_recomputing_estimate(self):
        rejected_key = prices.source_key("https://maker.example/products/scope-1")
        records, _ = prices.scan(
            catalog_package={
                "packageFamily": "astrophotographyEquipmentSanitizedCatalog",
                "packageVersion": "fixture-catalog-v1",
            },
            telescopes={"scope-1": equipment()},
            config=config(),
            prior_estimates=[],
            prior_attempts=[],
            known_equipment_ids={"scope-1"},
            overrides={
                "schema_version": 1,
                "overrides": [],
                "rejected_evidence": [
                    {
                        "equipment_id": "scope-1",
                        "source_key": rejected_key,
                        "reason": "Curator rejected the manufacturer mapping.",
                    }
                ],
            },
            generated_at="2026-08-24T20:00:00Z",
            selected_ids=None,
            force=True,
            offline=False,
            limit=1,
            api_key="fixture-key",
            requester=lambda *_args, **_kwargs: fixture("exact_two_sources.json"),
        )
        self.assertEqual(records[0]["price_amount"], 1050)
        self.assertEqual(records[0]["evidence_count"], 1)
        self.assertEqual(records[0]["estimate_confidence"], 0.75)

    def test_force_refresh_still_honors_batch_limit(self):
        calls = []

        def requester(item, _config, *, api_key):
            calls.append(item["component_id"])
            return result_response(equipment_id=item["component_id"])

        telescopes = {
            equipment_id: equipment(equipment_id)
            for equipment_id in ("scope-1", "scope-2", "scope-3")
        }
        _, result = prices.scan(
            catalog_package={
                "packageFamily": "astrophotographyEquipmentSanitizedCatalog",
                "packageVersion": "fixture-catalog-v1",
            },
            telescopes=telescopes,
            config=config(),
            prior_estimates=[],
            prior_attempts=[],
            known_equipment_ids=set(telescopes),
            overrides={"schema_version": 1, "overrides": [], "rejected_evidence": []},
            generated_at="2026-08-24T20:00:00Z",
            selected_ids=None,
            force=True,
            offline=False,
            limit=1,
            api_key="fixture-key",
            requester=requester,
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(result["report"]["summary"]["attempted_refresh_count"], 1)

    def test_price_scale_supports_hundreds_through_observatory_systems(self):
        records = [prices.missing_record(f"scope-{index}") for index in range(5)]
        for record, amount in zip(records, [300, 1000, 7500, 25000, 600000]):
            record["price_amount"] = amount
        self.assertEqual(
            prices.price_scale_counts(records),
            {
                "under_500": 1,
                "500_to_1999": 1,
                "2000_to_9999": 1,
                "10000_to_49999": 1,
                "50000_and_up": 1,
            },
        )


if __name__ == "__main__":
    unittest.main()
