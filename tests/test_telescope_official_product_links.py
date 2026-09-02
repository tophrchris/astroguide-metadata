import hashlib
import json
import unittest
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = (
    ROOT
    / "v1/packages/telescope-official-product-links/telescope_official_product_links_v1.json"
)
SANITIZED_CATALOG = (
    ROOT
    / "v1/packages/equipment/astrophotography_equipment_sanitized_catalog_v1.json"
)
SMART_CATALOG = ROOT / "v1/packages/equipment/equipment_catalog_v1.json"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


class TelescopeOfficialProductLinksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = read_json(PACKAGE)
        cls.records = cls.package["officialProductLinks"]

    def test_package_contract_is_small_independent_and_deterministic(self):
        self.assertEqual(self.package["schemaVersion"], 1)
        self.assertEqual(
            self.package["packageFamily"], "telescopeOfficialProductLinks"
        )
        self.assertEqual(self.package["scope"]["recordCount"], len(self.records))
        self.assertEqual(
            self.package["scope"]["linkedCount"],
            sum(record["official_url"] is not None for record in self.records),
        )
        self.assertEqual(
            self.package["scope"]["unresolvedCount"],
            sum(record["official_url"] is None for record in self.records),
        )
        self.assertEqual(
            [record["equipment_id"] for record in self.records],
            sorted(record["equipment_id"] for record in self.records),
        )
        self.assertEqual(
            len({record["equipment_id"] for record in self.records}),
            len(self.records),
        )
        self.assertTrue(
            all(set(record) == {"equipment_id", "official_url"} for record in self.records)
        )

    def test_every_url_is_https_and_unresolved_rows_are_explicit_nulls(self):
        linked = [record for record in self.records if record["official_url"]]
        unresolved = [record for record in self.records if record["official_url"] is None]
        self.assertTrue(linked)
        self.assertTrue(unresolved)
        for record in linked:
            parsed = urlparse(record["official_url"])
            self.assertEqual(parsed.scheme, "https", record["equipment_id"])
            self.assertTrue(parsed.netloc, record["equipment_id"])

    def test_every_record_joins_to_a_canonical_catalog_id(self):
        sanitized = read_json(SANITIZED_CATALOG)
        traditional_ids = {
            item["component_id"]
            for item in sanitized["catalog"]["opticalComponents"]
            if item.get("component_type") == "optical_tube"
        }
        smart = read_json(SMART_CATALOG)
        telescope_category = next(
            category
            for category in smart["catalog"]["categories"]
            if category["id"] == "telescopes"
        )
        smart_ids = {
            item["id"]
            for item in telescope_category["items"]
            if not str(item.get("notes") or "").startswith("Traditional telescope:")
        }
        canonical_ids = traditional_ids | smart_ids
        self.assertTrue(
            all(record["equipment_id"] in canonical_ids for record in self.records)
        )
        self.assertTrue(smart_ids.issubset({record["equipment_id"] for record in self.records}))

    def test_manifest_registers_the_package(self):
        manifest = read_json(ROOT / "v1/channels/stable/manifest.json")
        entry = next(
            package
            for package in manifest["packages"]
            if package["family"] == "telescopeOfficialProductLinks"
        )
        self.assertEqual(entry["payloadSchemaVersion"], 1)
        self.assertEqual(entry["recordCount"], len(self.records))
        self.assertEqual(entry["linkedCount"], self.package["scope"]["linkedCount"])
        package_bytes = PACKAGE.read_bytes()
        self.assertEqual(entry["byteSize"], len(package_bytes))
        self.assertEqual(
            entry["checksum"],
            {
                "algorithm": "sha256",
                "value": hashlib.sha256(package_bytes).hexdigest(),
            },
        )


if __name__ == "__main__":
    unittest.main()
