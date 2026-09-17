import contextlib
import datetime as dt
import importlib.util
import io
import json
import sqlite3
import sys
import tempfile
import unittest
import urllib.error
import zipfile
from pathlib import Path
from unittest import mock


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

    def test_can_limit_review_queue_to_top_ranked_opportunities(self):
        catalog, grid = queue_builder.load_catalog(self.catalog_path)
        queue = queue_builder.build_queue(
            queue_builder.load_source_records(self.inputs),
            catalog,
            grid,
            as_of=dt.date(2026, 9, 9),
            max_opportunities=2,
        )

        self.assertEqual(queue["counts"]["eligibleReviewOpportunities"], 3)
        self.assertEqual(queue["counts"]["reviewOpportunitiesLimit"], 2)
        self.assertEqual(queue["counts"]["reviewOpportunities"], 2)
        self.assertEqual([item["sourceId"] for item in queue["opportunities"]], ["1001", "1003"])
        self.assertIn(
            "3 eligible opportunities before the top-2 review cap",
            queue_builder.render_markdown(queue),
        )

    def test_fetch_skips_missing_staged_delta_when_other_days_are_available(self):
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, "w") as archive:
            archive.writestr("tns.csv", "objid,name\n")
        requested_urls = []

        def open_staged_delta(request, timeout):
            del timeout
            requested_urls.append(request.full_url)
            if "20260902" in request.full_url:
                raise urllib.error.HTTPError(request.full_url, 404, "Not Found", None, None)
            return io.BytesIO(payload.getvalue())

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with mock.patch.object(queue_builder.urllib.request, "urlopen", side_effect=open_staged_delta):
                paths = queue_builder.fetch_staged_deltas(
                    as_of=dt.date(2026, 9, 3),
                    days=3,
                    destination=self.root / "staged",
                    user_agent='tns_marker{"tns_id": 1}',
                )

        self.assertEqual(len(requested_urls), 3)
        self.assertTrue(any("20260902" in url for url in requested_urls))
        self.assertIn("missing: 20260902", stderr.getvalue())
        self.assertEqual(
            [path.name for path in paths],
            [
                "tns_public_objects_20260901.csv.zip",
                "tns_public_objects_20260903.csv.zip",
            ],
        )

    def test_main_fails_when_no_staged_deltas_are_available(self):
        def missing_staged_delta(request, timeout):
            del timeout
            raise urllib.error.HTTPError(request.full_url, 404, "Not Found", None, None)

        arguments = [
            str(SCRIPT_PATH),
            "--catalog",
            str(self.catalog_path),
            "--as-of",
            "2026-09-03",
            "--fetch-days",
            "3",
            "--staging-dir",
            str(self.root / "staged"),
            "--output-dir",
            str(self.root / "outputs"),
            "--tns-user-agent",
            'tns_marker{"tns_id": 1}',
        ]
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with mock.patch.object(sys, "argv", arguments):
                with mock.patch.object(queue_builder.urllib.request, "urlopen", side_effect=missing_staged_delta):
                    with self.assertRaises(SystemExit) as raised:
                        queue_builder.main()

        self.assertEqual(raised.exception.code, 2)
        self.assertIn("no usable staged inputs were provided or fetched", stderr.getvalue())
        self.assertFalse((self.root / "outputs").exists())

    def test_fetch_does_not_mask_non_404_http_errors(self):
        def forbidden_staged_delta(request, timeout):
            del timeout
            raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", None, None)

        with mock.patch.object(queue_builder.urllib.request, "urlopen", side_effect=forbidden_staged_delta):
            with self.assertRaises(urllib.error.HTTPError) as raised:
                queue_builder.fetch_staged_deltas(
                    as_of=dt.date(2026, 9, 3),
                    days=1,
                    destination=self.root / "staged",
                    user_agent='tns_marker{"tns_id": 1}',
                )
        raised.exception.close()


if __name__ == "__main__":
    unittest.main()
