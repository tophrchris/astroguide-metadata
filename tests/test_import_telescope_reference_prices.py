import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import import_telescope_reference_prices as importer  # noqa: E402
import update_telescope_reference_prices as prices  # noqa: E402


def config():
    return {
        "estimate_policy": {
            "currency": "USD",
            "rounding_increment": 50,
            "minimum_price": 25,
            "maximum_price": 750000,
            "minimum_match_confidence": 0.9,
            "minimum_estimate_confidence": 0.65,
        }
    }


def curated_record(**updates):
    record = {
        "equipment_id": "scope-1",
        "price_usd": 1024.95,
        "price_basis": "typical_new_retail",
        "market_status": "current",
        "match_confidence": 0.99,
        "estimate_confidence": 0.74,
        "source_type": "manufacturer",
        "source_url": "https://maker.example/products/scope-1?campaign=ignored",
        "note": "Exact manufacturer model and sold configuration.",
    }
    record.update(updates)
    return record


class CuratedReferencePriceImportTests(unittest.TestCase):
    def test_import_rounds_and_omits_exact_source_identity(self):
        estimate = importer.import_estimate(
            curated_record(),
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        self.assertEqual(estimate["price_amount"], 1000)
        self.assertEqual(estimate["evidence"][0]["price_amount"], 1024.95)
        self.assertEqual(estimate["method"], "curated_structured_source")
        self.assertEqual(estimate["estimate_confidence"], 0.74)
        serialized = json.dumps(estimate)
        self.assertNotIn("http", serialized)
        self.assertNotIn("maker.example", serialized)

    def test_single_source_import_caps_estimate_confidence(self):
        estimate = importer.import_estimate(
            curated_record(estimate_confidence=0.98),
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        self.assertEqual(estimate["estimate_confidence"], 0.75)

    def test_generation_proxy_is_labeled_and_identity_confidence_is_capped(self):
        estimate = importer.import_estimate(
            curated_record(match_basis="generation_proxy", match_confidence=0.99),
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        self.assertEqual(estimate["match_basis"], "generation_proxy")
        self.assertEqual(estimate["match_confidence"], 0.94)
        self.assertIn("generation proxy", estimate["note"].casefold())

    def test_foreign_source_price_is_converted_to_usd_without_retaining_url(self):
        record = curated_record(
            price_usd=None,
            source_price=999,
            source_currency="GBP",
            usd_conversion_rate=1.25,
        )
        estimate = importer.import_estimate(
            record,
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        self.assertEqual(estimate["price_amount"], 1250)
        self.assertEqual(estimate["evidence"][0]["price_amount"], 1248.75)
        self.assertEqual(estimate["evidence"][0]["source_currency"], "GBP")
        self.assertEqual(estimate["evidence"][0]["source_price"], 999.0)
        self.assertNotIn("http", json.dumps(estimate))

    def test_last_known_price_requires_discontinued_status(self):
        with self.assertRaisesRegex(prices.ReferencePriceError, "must be discontinued"):
            importer.import_estimate(
                curated_record(price_basis="last_known_new_retail"),
                observed_at="2026-08-25T12:00:00Z",
                telescope_ids={"scope-1"},
                config=config(),
            )

    def test_observatory_system_price_is_valid_with_production_ceiling(self):
        estimate = importer.import_estimate(
            curated_record(price_usd=600000),
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        self.assertEqual(estimate["price_amount"], 600000)

    def test_duplicate_retained_estimate_requires_explicit_replacement(self):
        imported = importer.import_estimate(
            curated_record(),
            observed_at="2026-08-25T12:00:00Z",
            telescope_ids={"scope-1"},
            config=config(),
        )
        state = {
            "schema_version": 1,
            "known_equipment_ids": ["scope-1"],
            "refresh_attempts": [],
            "estimates": [imported],
        }
        with self.assertRaisesRegex(prices.ReferencePriceError, "--replace-existing"):
            importer.merge_import(
                state,
                [imported],
                observed_at="2026-08-25T12:00:00Z",
                telescope_ids={"scope-1"},
                config=config(),
                replace_existing=False,
            )


if __name__ == "__main__":
    unittest.main()
