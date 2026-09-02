import copy
import datetime as dt
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PATH = (
    ROOT / "v1/packages/star-party-astrosites/star_party_astrosites_v1.json"
)
MANIFEST_PATH = ROOT / "v1/channels/stable/manifest.json"
SCHEMA_PATH = (
    ROOT
    / "sources/star-party-astrosites/star-party-astrosite-source-v1.schema.json"
)
BUILDER_PATH = ROOT / "scripts/build_star_party_astrosite_package.py"

SPEC = importlib.util.spec_from_file_location("star_party_builder", BUILDER_PATH)
BUILDER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BUILDER)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class StarPartyAstroSitePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.package = read_json(PACKAGE_PATH)
        cls.records = cls.package["starPartyAstroSites"]
        cls.by_id = {record["id"]: record for record in cls.records}

    def test_package_contract_counts_and_order_are_deterministic(self):
        self.assertEqual(self.package["schemaVersion"], 1)
        self.assertEqual(self.package["packageFamily"], "starPartyAstroSites")
        self.assertEqual(self.package["packageVersion"], "star-party-astrosites-v1-20260902")
        self.assertEqual(self.package["scope"]["siteCount"], 15)
        self.assertEqual(self.package["scope"]["eventCount"], 19)
        self.assertEqual(self.package["scope"]["scheduledEventCount"], 16)
        self.assertEqual(self.package["scope"]["completedEventCount"], 3)
        self.assertEqual(self.package["scope"]["cancelledEventCount"], 0)
        self.assertEqual(self.package["scope"]["countryCount"], 4)
        self.assertEqual(self.package["scope"]["horizonResourceCount"], 3)
        self.assertEqual(self.package["scope"]["cachedHorizonAssetCount"], 1)
        self.assertEqual(self.package["scope"]["obstructionProfileCount"], 0)
        ids = [record["id"] for record in self.records]
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), len(set(ids)))
        for record in self.records:
            events = record["events"]
            self.assertEqual(
                [(event["start"], event["end"], event["id"]) for event in events],
                sorted((event["start"], event["end"], event["id"]) for event in events),
            )

    def test_initial_seed_and_sourceable_extras_are_present(self):
        expected = {
            "texas-star-party",
            "winter-star-party",
            "okie-tex-star-party",
            "oregon-star-party",
            "cherry-springs-star-parties",
            "nebraska-star-party",
            "almost-heaven-star-party",
            "kelling-heath-autumn-equinox-sky-camp",
            "starfest-canada",
            "ozsky-star-safari",
            "stellafane-convention",
            "mount-kobau-star-party",
            "kielder-star-camp",
            "washington-state-star-party",
            "grand-canyon-star-party",
        }
        self.assertEqual(set(self.by_id), expected)
        self.assertNotIn("south-pacific-star-party", self.by_id)
        self.assertNotIn("golden-state-star-party", self.by_id)

    def test_shared_cherry_springs_venue_has_both_events(self):
        record = self.by_id["cherry-springs-star-parties"]
        self.assertEqual(
            {event["id"] for event in record["events"]},
            {"black-forest-star-party-2026", "cherry-springs-star-party-2027"},
        )
        self.assertEqual(
            record["location"]["relatedDarkSkyPlaceID"],
            "darksky:cherry-springs-state-park-dark-sky-park",
        )

    def test_records_have_portable_sites_descriptions_and_provenance(self):
        generated_date = dt.datetime.fromisoformat(
            self.package["generatedAt"].replace("Z", "+00:00")
        ).date()
        source_site_ids = set()
        event_ids = set()
        for record in self.records:
            with self.subTest(record=record["id"]):
                site = record["astroSite"]
                self.assertEqual(site["schemaVersion"], 1)
                self.assertEqual(
                    site["sourceSiteID"], BUILDER.expected_source_site_id(record["id"])
                )
                self.assertNotIn(site["sourceSiteID"], source_site_ids)
                source_site_ids.add(site["sourceSiteID"])
                self.assertGreaterEqual(site["latitude"], -90)
                self.assertLessEqual(site["latitude"], 90)
                self.assertGreaterEqual(site["longitude"], -180)
                self.assertLessEqual(site["longitude"], 180)
                self.assertGreaterEqual(len(record["description"]), 40)
                self.assertTrue(record["descriptionSources"])
                ZoneInfo(record["location"]["timezone"])

                for source in record["descriptionSources"] + [
                    record["location"]["coordinateSource"]
                ]:
                    self.assertLessEqual(dt.date.fromisoformat(source["verifiedAt"]), generated_date)
                    self.assertEqual(urlparse(source["url"]).scheme, "https")

                for event in record["events"]:
                    self.assertNotIn(event["id"], event_ids)
                    event_ids.add(event["id"])
                    self.assertLessEqual(
                        dt.date.fromisoformat(event["start"]),
                        dt.date.fromisoformat(event["end"]),
                    )
                    self.assertEqual(urlparse(event["url"]).scheme, "https")
                    self.assertTrue(event["source"]["title"])
                    self.assertTrue(event["source"]["verifiedAt"])

    def test_package_exactly_matches_reviewable_source_records(self):
        records = BUILDER.load_and_validate_records(self.package["generatedAt"])
        rebuilt = BUILDER.build_package(records, self.package["generatedAt"])
        self.assertEqual(rebuilt, self.package)
        source_paths = sorted(
            (ROOT / "sources/star-party-astrosites/records").glob("*/record.json")
        )
        self.assertEqual(len(source_paths), len(self.records))

    def test_schema_declares_optional_cached_media_and_horizon_resources(self):
        schema = read_json(SCHEMA_PATH)
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertIn("astroSite", schema["properties"])
        self.assertIn("events", schema["properties"])
        self.assertEqual(set(schema["properties"]["media"]["properties"]), {"hero", "logo"})
        self.assertTrue(all("media" not in record for record in self.records))
        self.assertIn("horizonResources", schema["properties"])
        self.assertEqual(
            set(schema["$defs"]["horizonResource"]["properties"]["quality"]["enum"]),
            {
                "authoritative_hrz",
                "manual_trace_from_panorama",
                "estimated_from_panorama",
                "visual_panorama_only",
            },
        )

    def test_horizon_resources_keep_visual_references_out_of_obstruction_math(self):
        resources = {
            resource["id"]: resource
            for record in self.records
            for resource in record.get("horizonResources", [])
        }
        self.assertEqual(
            set(resources),
            {
                "cherry-springs-state-park-panorama-2009",
                "almost-heaven-entrance-to-green-lot-panorama",
                "oregon-star-party-panorama",
            },
        )
        for resource in resources.values():
            with self.subTest(resource=resource["id"]):
                self.assertEqual(resource["quality"], "visual_panorama_only")
                self.assertFalse(
                    resource["calibration"]["suitableForObstructionCalculations"]
                )
                self.assertNotIn("obstructionProfile", resource)

        cherry = resources["cherry-springs-state-park-panorama-2009"]
        self.assertEqual(cherry["disposition"], "cached_visual_reference")
        self.assertEqual(
            cherry["rights"]["permissionStatus"], "licensed_for_redistribution"
        )
        self.assertEqual(cherry["rights"]["licenseName"], "CC BY-SA 3.0")
        asset = cherry["asset"]
        asset_path = ROOT / asset["path"]
        asset_bytes = asset_path.read_bytes()
        self.assertEqual(hashlib.sha256(asset_bytes).hexdigest(), asset["sha256"])
        self.assertEqual(len(asset_bytes), asset["byteSize"])
        self.assertEqual(BUILDER.image_dimensions(asset_path), (3840, 281))

        almost_heaven = resources["almost-heaven-entrance-to-green-lot-panorama"]
        self.assertEqual(almost_heaven["disposition"], "link_only_pending_permission")
        self.assertEqual(almost_heaven["rights"]["permissionStatus"], "permission_required")
        self.assertNotIn("asset", almost_heaven)

        oregon = resources["oregon-star-party-panorama"]
        self.assertEqual(oregon["disposition"], "link_only_research")
        self.assertEqual(oregon["rights"]["permissionStatus"], "unknown")
        self.assertNotIn("asset", oregon)

    def test_manifest_registers_exact_artifact(self):
        manifest = read_json(MANIFEST_PATH)
        entries = [
            entry for entry in manifest["packages"] if entry["family"] == "starPartyAstroSites"
        ]
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        package_bytes = PACKAGE_PATH.read_bytes()
        self.assertEqual(entry["payloadSchemaVersion"], 1)
        self.assertEqual(entry["minSupportedAppVersion"], "1.4.1")
        self.assertEqual(entry["siteCount"], len(self.records))
        self.assertEqual(entry["eventCount"], self.package["scope"]["eventCount"])
        self.assertEqual(
            entry["horizonResourceCount"], self.package["scope"]["horizonResourceCount"]
        )
        self.assertEqual(
            entry["cachedHorizonAssetCount"],
            self.package["scope"]["cachedHorizonAssetCount"],
        )
        self.assertEqual(
            entry["obstructionProfileCount"],
            self.package["scope"]["obstructionProfileCount"],
        )
        self.assertEqual(entry["byteSize"], len(package_bytes))
        self.assertEqual(
            entry["checksum"],
            {
                "algorithm": "sha256",
                "value": hashlib.sha256(package_bytes).hexdigest(),
            },
        )

    def test_validator_rejects_invalid_coordinates_dates_urls_timezones_and_sources(self):
        base = copy.deepcopy(self.by_id["texas-star-party"])
        path = (
            ROOT
            / "sources/star-party-astrosites/records/texas-star-party/record.json"
        )
        generated_date = dt.date(2026, 9, 2)

        invalid = []
        bad = copy.deepcopy(base)
        bad["astroSite"]["latitude"] = 91
        invalid.append(("coordinate", bad))
        bad = copy.deepcopy(base)
        bad["location"]["timezone"] = "Mars/Olympus_Mons"
        invalid.append(("timezone", bad))
        bad = copy.deepcopy(base)
        bad["officialURLs"][0]["url"] = "http://example.com/not-secure"
        invalid.append(("url", bad))
        bad = copy.deepcopy(base)
        bad["events"][0]["end"] = "2027-05-01"
        invalid.append(("date order", bad))
        bad = copy.deepcopy(base)
        del bad["events"][0]["source"]
        invalid.append(("missing source", bad))

        for label, record in invalid:
            with self.subTest(case=label):
                with self.assertRaises(BUILDER.ValidationError):
                    BUILDER.validate_record(record, path, generated_date)

    def test_validator_rejects_duplicate_record_and_event_ids(self):
        records = copy.deepcopy(self.records[:2])
        records[1]["id"] = records[0]["id"]
        with self.assertRaisesRegex(BUILDER.ValidationError, "Duplicate record ID"):
            BUILDER.validate_unique_identities(records)

        records = copy.deepcopy(self.records[:2])
        records[1]["events"][0]["id"] = records[0]["events"][0]["id"]
        with self.assertRaisesRegex(BUILDER.ValidationError, "Duplicate event ID"):
            BUILDER.validate_unique_identities(records)

    def test_validator_rejects_uncalibrated_or_unlicensed_horizon_use(self):
        resource = copy.deepcopy(
            self.by_id["cherry-springs-star-parties"]["horizonResources"][0]
        )

        resource["calibration"]["suitableForObstructionCalculations"] = True
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_horizon_resources(
                [resource], "cherry-springs-star-parties", dt.date(2026, 9, 2)
            )

        resource = copy.deepcopy(
            self.by_id["cherry-springs-star-parties"]["horizonResources"][0]
        )
        resource["rights"]["permissionStatus"] = "permission_required"
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_horizon_resources(
                [resource], "cherry-springs-star-parties", dt.date(2026, 9, 2)
            )

    def test_hrz_parser_matches_astroguide_azimuth_altitude_convention(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.hrz"
            path.write_text("# azimuth altitude\n0 3\n90,4.5\n180; 2\n", encoding="utf-8")
            self.assertEqual(BUILDER.validate_hrz_asset(path, "test.hrz"), 3)

            path.write_text("361 2\n", encoding="utf-8")
            with self.assertRaises(BUILDER.ValidationError):
                BUILDER.validate_hrz_asset(path, "test.hrz")


if __name__ == "__main__":
    unittest.main()
