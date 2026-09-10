import datetime as dt
import importlib.util
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_tns_transient_review_queue.py"
SPEC = importlib.util.spec_from_file_location("build_tns_transient_review_queue", SCRIPT_PATH)
queue_builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = queue_builder
assert SPEC.loader is not None
SPEC.loader.exec_module(queue_builder)


class TNSTransientReviewQueueTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.catalog_path = self.root / "catalog.sqlite"
        connection = sqlite3.connect(self.catalog_path)
        connection.execute(
            """
            CREATE TABLE deep_sky_objects (
                object_id TEXT PRIMARY KEY,
                primary_name TEXT NOT NULL,
                catalog_name TEXT NOT NULL,
                object_type TEXT NOT NULL,
                magnitude REAL,
                ra_hours REAL,
                dec_degrees REAL,
                aliases TEXT NOT NULL DEFAULT ''
            )
            """
        )
        connection.executemany(
            """
            INSERT INTO deep_sky_objects
                (object_id, primary_name, catalog_name, object_type, magnitude, ra_hours, dec_degrees, aliases)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                ("M 100", "Example Galaxy", "M M 100", "Galaxy", 10.5, 10.0 / 15.0, 20.0, "NGC 999"),
                ("IC 200", "Example Nebula", "IC IC 200", "Nebula", None, 30.0 / 15.0, 10.0, ""),
            ],
        )
        connection.commit()
        connection.close()
        self.inputs = [
            ROOT / "tests/fixtures/tns/tns_delta_20260908.csv",
            ROOT / "tests/fixtures/tns/tns_delta_20260909.csv",
        ]

    def tearDown(self):
        self.temporary_directory.cleanup()

    def build(self, inputs=None):
        catalog, grid = queue_builder.load_catalog(self.catalog_path)
        return queue_builder.build_queue(
            queue_builder.load_source_records(inputs or self.inputs),
            catalog,
            grid,
            as_of=dt.date(2026, 9, 9),
        )

    def test_parses_coverage_line_and_deduplicates_by_newest_lastmodified(self):
        queue = self.build()

        self.assertEqual(queue["counts"]["rawRows"], 8)
        self.assertEqual(queue["counts"]["duplicateRowsCollapsed"], 1)
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")
        self.assertEqual(candidate["sourceObjectName"], "SN2026abc")
        self.assertEqual(candidate["classification"]["type"], "SN II")
        self.assertEqual(candidate["discovery"]["magnitude"], 16.2)
        self.assertEqual(len(candidate["provenance"]["inputRecords"]), 2)

    def test_rejects_contaminants_and_faint_candidates(self):
        queue = self.build()
        ids = {item["sourceId"] for item in queue["opportunities"]}

        self.assertNotIn("1002", ids)
        self.assertNotIn("1005", ids)
        self.assertNotIn("1006", ids)
        self.assertEqual(queue["counts"]["contaminantsRejected"], 2)
        self.assertEqual(queue["counts"]["fainterThanWatchBand"], 1)

    def test_scores_strong_supernova_as_urgent_and_old_candidate_as_expired(self):
        queue = self.build()
        by_id = {item["sourceId"]: item for item in queue["opportunities"]}

        self.assertEqual(by_id["1001"]["urgency"], "urgent")
        self.assertIn("separation_le_0_25_deg", by_id["1001"]["reasonTags"])
        self.assertIn("nearby_catalog_object_is_galaxy", by_id["1001"]["reasonTags"])
        self.assertEqual(by_id["1004"]["urgency"], "expired")

    def test_faint_watch_band_requires_close_match_and_is_never_urgent(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1003")

        self.assertEqual(candidate["urgency"], "watch")
        self.assertLessEqual(candidate["angularSeparationDegrees"], 0.25)

    def test_near_field_terminology_does_not_infer_host_association(self):
        queue = self.build()
        for item in queue["opportunities"]:
            self.assertEqual(item["relationship"]["type"], "near_field")
            self.assertEqual(item["relationship"]["wording"], "near-field match")
        rendered = json.dumps(queue).lower()
        self.assertNotIn("host/association", rendered)

    def test_tns_source_url_strips_supported_display_prefixes(self):
        self.assertEqual(
            queue_builder.source_url("TDE2026xyz"),
            "https://www.wis-tns.org/object/2026xyz",
        )

    def test_default_fetch_as_of_uses_previous_utc_day(self):
        self.assertEqual(
            queue_builder.default_fetch_as_of(dt.date(2026, 9, 10)),
            dt.date(2026, 9, 9),
        )

    def test_json_and_markdown_are_deterministic_across_input_order(self):
        first = self.build(self.inputs)
        second = self.build(list(reversed(self.inputs)))

        self.assertEqual(
            json.dumps(first, sort_keys=True),
            json.dumps(second, sort_keys=True),
        )
        self.assertEqual(
            queue_builder.render_markdown(first),
            queue_builder.render_markdown(second),
        )


if __name__ == "__main__":
    unittest.main()
