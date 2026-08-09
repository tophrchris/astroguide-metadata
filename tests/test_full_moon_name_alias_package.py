import copy
import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "build_full_moon_name_alias_package.py"
SOURCE_PATH = (
    REPO_ROOT
    / "sources"
    / "full-moon-name-aliases"
    / "full_moon_name_aliases_v1.json"
)
SPEC = importlib.util.spec_from_file_location(
    "build_full_moon_name_alias_package",
    SCRIPT_PATH,
)
moon_names = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = moon_names
assert SPEC.loader is not None
SPEC.loader.exec_module(moon_names)


class FullMoonNameAliasPackageTests(unittest.TestCase):
    def setUp(self):
        self.source = moon_names.read_json(SOURCE_PATH)
        moon_names.validate_source(self.source)
        self.package = moon_names.build_package(self.source)
        moon_names.validate_package(self.package)

    def test_contains_twelve_stable_month_entries_and_expected_primary_names(self):
        expected_names = [
            "Wolf Moon",
            "Snow Moon",
            "Worm Moon",
            "Pink Moon",
            "Flower Moon",
            "Strawberry Moon",
            "Buck Moon",
            "Sturgeon Moon",
            "Corn Moon",
            "Hunter's Moon",
            "Beaver Moon",
            "Cold Moon",
        ]

        self.assertEqual(
            [entry["id"] for entry in self.package["entries"]],
            [f"full-moon-gregorian-month-{month:02d}" for month in range(1, 13)],
        )
        self.assertEqual(
            [entry["primaryName"]["displayName"] for entry in self.package["entries"]],
            expected_names,
        )
        self.assertEqual(
            self.package["resolver"],
            {
                "id": "gregorianMonthOfContainedFullMoon",
                "version": 1,
                "calendar": "gregorian",
                "timeBasis": "utc",
                "input": "containedFullMoonInstantUTC",
                "notes": self.source["resolver"]["notes"],
            },
        )

    def test_duplicate_display_text_retains_independent_claims(self):
        january = self.package["entries"][0]
        september = self.package["entries"][8]

        self.assertEqual(
            [claim["libraryID"] for claim in january["primaryName"]["claims"]],
            ["english-medieval", "north-american-popular"],
        )
        harvest = next(
            alias for alias in september["aliases"] if alias["displayName"] == "Harvest Moon"
        )
        self.assertEqual(
            [claim["libraryID"] for claim in harvest["claims"]],
            ["mixed-provenance-popular-alternatives", "modern-pagan"],
        )
        self.assertEqual(len(september["aliases"]), 2)
        self.assertEqual(len({alias["displayName"] for alias in september["aliases"]}), 2)

    def test_library_can_be_removed_without_builder_changes(self):
        source = copy.deepcopy(self.source)
        source["libraries"] = [
            library
            for library in source["libraries"]
            if library["id"] != "modern-pagan"
        ]

        moon_names.validate_source(source)
        package = moon_names.build_package(source)
        moon_names.validate_package(package)

        self.assertEqual(package["counts"]["libraries"], 3)
        self.assertEqual(package["counts"]["nameClaims"], 36)
        september = package["entries"][8]
        harvest = next(
            alias for alias in september["aliases"] if alias["displayName"] == "Harvest Moon"
        )
        self.assertEqual(
            [claim["libraryID"] for claim in harvest["claims"]],
            ["mixed-provenance-popular-alternatives"],
        )

    def test_library_can_be_added_without_builder_changes(self):
        source = copy.deepcopy(self.source)
        source["libraries"].append(
            {
                "id": "test-additive-library",
                "displayName": "Test Additive Library",
                "displayOrder": 4,
                "role": "alias",
                "status": "active",
                "sourceIDs": ["uni-names-for-the-full-moon"],
                "attribution": {
                    "culturalContext": ["test"],
                    "regions": ["test"],
                    "hemispheres": ["none"],
                    "languageTags": ["en"],
                    "communitySpecific": False,
                    "notes": "Test-only metadata library.",
                },
                "confidence": "low",
                "provenanceQuality": "unresolvedCompilation",
                "usageReviewStatus": "researchOnly",
                "licensingNotes": "Test-only metadata library.",
                "editorialNotes": "Test-only metadata library.",
                "names": [
                    {
                        "month": month,
                        "displayName": f"Test {month} Moon",
                        "sourceNameText": f"Test {month}",
                        "sourceID": "uni-names-for-the-full-moon",
                    }
                    for month in range(1, 13)
                ],
            }
        )

        moon_names.validate_source(source)
        package = moon_names.build_package(source)
        moon_names.validate_package(package)

        self.assertEqual(package["counts"]["libraries"], 5)
        self.assertEqual(package["counts"]["nameClaims"], 60)
        self.assertIn(
            "Test 1 Moon",
            [alias["displayName"] for alias in package["entries"][0]["aliases"]],
        )

    def test_input_order_does_not_change_serialized_package(self):
        reordered = copy.deepcopy(self.source)
        reordered["sources"].reverse()
        reordered["libraries"].reverse()
        for library in reordered["libraries"]:
            library["names"].reverse()

        moon_names.validate_source(reordered)
        reordered_package = moon_names.build_package(reordered)
        moon_names.validate_package(reordered_package)

        self.assertEqual(
            moon_names.json_bytes(self.package, compact=True),
            moon_names.json_bytes(reordered_package, compact=True),
        )

    def test_runtime_lunation_fields_are_rejected(self):
        package = copy.deepcopy(self.package)
        package["entries"][0]["lunationID"] = "generated-lunation"

        with self.assertRaisesRegex(RuntimeError, "must not contain runtime field"):
            moon_names.validate_package(package)

    def test_counts_capture_deduplicated_claims(self):
        self.assertEqual(
            self.package["counts"],
            {
                "entries": 12,
                "libraries": 4,
                "sources": 2,
                "primaryNames": 12,
                "aliasNames": 25,
                "nameClaims": 48,
                "deduplicatedClaims": 11,
            },
        )


if __name__ == "__main__":
    unittest.main()
