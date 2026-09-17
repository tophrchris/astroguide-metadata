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
import urllib.parse
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
                constellation TEXT,
                magnitude REAL,
                angular_size_arcmin REAL,
                angular_size_maj_arcmin REAL,
                angular_size_min_arcmin REAL,
                ra_hours REAL,
                dec_degrees REAL,
                aliases TEXT NOT NULL DEFAULT '',
                distance TEXT,
                description TEXT
            )
            """
        )
        connection.executemany(
            """
            INSERT INTO deep_sky_objects
                (object_id, primary_name, catalog_name, object_type, constellation,
                 magnitude, angular_size_arcmin, angular_size_maj_arcmin,
                 angular_size_min_arcmin, ra_hours, dec_degrees, aliases,
                 distance, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    "M 100", "Example Galaxy", "M M 100", "Galaxy", "Com",
                    10.5, 7.4, 7.4, 6.3, 10.0 / 15.0, 20.0, "NGC 999",
                    "55 Mly", "A face-on spiral galaxy used by the queue tests.",
                ),
                (
                    "IC 200", "Example Nebula", "IC IC 200", "Nebula", "Ori",
                    None, 12.0, 12.0, 8.0, 30.0 / 15.0, 10.0, "", None,
                    "A test nebula.",
                ),
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

    def test_preserves_staged_redshift_reporters_and_bibliographic_context(self):
        staged = self.root / "enriched.csv"
        staged.write_text(
            '"objid","name_prefix","name","ra","declination","redshift","type",'
            '"discoverydate","discoverymag","discmagfilter","reporters","time_received",'
            '"Discovery_ADS_bibcode","Class_ADS_bibcodes","creationdate","lastmodified"\n'
            '"2001","SN","2026rich","10.0000","20.0000","0.0123","SN Ia",'
            '"2026-09-08 01:00:00","16.4","r","A. Reporter",'
            '"2026-09-08 02:00:00","2026TNSTR.1A","2026TNSCR.1B, 2026TNSCR.1C",'
            '"2026-09-08 01:30:00","2026-09-09 03:00:00"\n',
            encoding="utf-8",
        )

        candidate = self.build([staged])["opportunities"][0]
        context = candidate["tnsContext"]

        self.assertEqual(context["redshift"], 0.0123)
        self.assertEqual(context["reporters"], "A. Reporter")
        self.assertEqual(context["receivedAtUTC"], "2026-09-08T02:00:00Z")
        self.assertEqual(context["discoveryReference"]["bibcode"], "2026TNSTR.1A")
        self.assertEqual(
            [item["bibcode"] for item in context["classificationReferences"]],
            ["2026TNSCR.1B", "2026TNSCR.1C"],
        )

    def test_resolves_only_hosted_target_image_package_thumbnail(self):
        package_path = self.root / "target-images.json"
        package_path.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "packageFamily": "targetImageAssets",
                    "packageRole": "index",
                    "packageVersion": "target-image-assets-v1-test",
                    "targets": [
                        {
                            "canonicalTargetID": "A00",
                            "catalogObjectID": "A00",
                            "assetID": "alias-asset",
                            "aliases": ["M 100"],
                            "variants": {
                                "thumbnail160": {
                                    "url": "https://metadata.astroguide.space/v1/assets/target-images/A00/wrong.jpg",
                                    "path": "v1/assets/target-images/A00/wrong.jpg",
                                    "width": 160,
                                    "height": 160,
                                    "byteSize": 100,
                                    "sha256": "0" * 64,
                                }
                            },
                            "source": {
                                "attribution": "Alias image",
                                "sourcePackageID": "package-0",
                            },
                        },
                        {
                            "canonicalTargetID": "M100",
                            "catalogObjectID": "M100",
                            "assetID": "asset-1",
                            "assetOwnerTargetID": "M100",
                            "aliases": ["NGC 999"],
                            "variants": {
                                "thumbnail160": {
                                    "url": "https://metadata.astroguide.space/v1/assets/target-images/M100/thumb.jpg",
                                    "path": "v1/assets/target-images/M100/thumb.jpg",
                                    "width": 160,
                                    "height": 160,
                                    "byteSize": 120,
                                    "sha256": "a" * 64,
                                }
                            },
                            "source": {
                                "attribution": "Approved AstroGuide image",
                                "sourcePackageID": "package-1",
                            },
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        catalog, grid = queue_builder.load_catalog(self.catalog_path)
        queue = queue_builder.build_queue(
            queue_builder.load_source_records(self.inputs),
            catalog,
            grid,
            as_of=dt.date(2026, 9, 9),
            target_image_index=queue_builder.load_target_image_index(package_path),
        )
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")
        thumbnail = candidate["astroGuideObject"]["catalogThumbnail"]

        self.assertEqual(thumbnail["status"], "available")
        self.assertEqual(
            thumbnail["url"],
            "https://metadata.astroguide.space/v1/assets/target-images/M100/thumb.jpg",
        )
        self.assertEqual(thumbnail["attribution"], "Approved AstroGuide image")

    def test_detail_enrichment_can_promote_an_explicit_tns_host_match(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")

        queue_builder.merge_tns_detail(
            candidate,
            {
                "currentType": "SN Ia",
                "redshift": 0.012,
                "host": {"name": "NGC 999", "redshift": 0.0118},
                "latestPhotometry": {
                    "observationDateUTC": "2026-09-09T04:00:00Z",
                    "value": 15.4,
                    "error": 0.1,
                    "units": "ABMag",
                    "band": "r",
                    "instrument": "TestCam",
                    "telescope": None,
                    "isUpperLimit": False,
                },
                "spectra": {"count": 1, "latest": {"instrument": "SpecCam"}},
            },
            retrieved_at="2026-09-10T00:00:00Z",
            source_kind="tns_get_object_api",
        )

        self.assertEqual(candidate["relationship"]["type"], "tns_reported_host")
        self.assertEqual(candidate["relationship"]["wording"], "TNS-reported host match")
        self.assertEqual(candidate["tnsContext"]["latestPublicPhotometry"]["value"], 15.4)
        self.assertEqual(candidate["reportedMagnitude"]["value"], 15.4)
        self.assertEqual(candidate["reportedMagnitude"]["observedAtUTC"], "2026-09-09T04:00:00Z")
        self.assertEqual(candidate["enrichment"]["status"], "complete")
        rendered = queue_builder.render_markdown(queue)
        self.assertIn("Host evidence", rendered)
        self.assertIn("15.4 · ABMag · r · TestCam", rendered)

    def test_detail_enrichment_keeps_flux_photometry_out_of_reported_magnitude(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")
        staged_magnitude = dict(candidate["reportedMagnitude"])

        queue_builder.merge_tns_detail(
            candidate,
            {
                "latestPhotometry": {
                    "observationDateUTC": "2026-09-09T04:00:00Z",
                    "value": 2.5,
                    "units": "mJy",
                    "band": "radio",
                    "isUpperLimit": False,
                }
            },
            retrieved_at="2026-09-10T00:00:00Z",
            source_kind="tns_get_object_api",
        )

        self.assertEqual(candidate["tnsContext"]["latestPublicPhotometry"]["units"], "mJy")
        self.assertEqual(candidate["reportedMagnitude"], staged_magnitude)

    def test_get_object_api_uses_exact_selected_object_and_compacts_public_data(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")
        response = io.BytesIO(
            json.dumps(
                {
                    "id_code": 200,
                    "id_message": "OK",
                    "data": {
                        "reply": {
                            "type": {"name": "SN Ia"},
                            "redshift": "0.012",
                            "hostname": "NGC 999",
                            "host_redshift": "0.0118",
                            "photometry": [
                                {
                                    "obsdate": "2026-09-09 04:00:00",
                                    "flux": "15.4",
                                    "fluxerr": "0.1",
                                    "flux_unit": {"name": "ABMag"},
                                    "filters": {"name": "r"},
                                    "instruments": {"name": "TestCam"},
                                    "public": 1,
                                },
                                {
                                    "obsdate": "2026-09-10 04:00:00",
                                    "flux": "14.0",
                                    "public": 0,
                                },
                            ],
                            "spectra": [],
                        }
                    },
                }
            ).encode("utf-8")
        )
        response.headers = {"x-rate-limit-remaining": "9"}

        with mock.patch.object(queue_builder.urllib.request, "urlopen", return_value=response) as mocked:
            detail, _ = queue_builder.fetch_tns_object_detail(
                candidate,
                api_key="secret",
                user_agent='tns_marker{"tns_id": 1, "type": "bot", "name": "test"}',
            )

        request = mocked.call_args.args[0]
        form = urllib.parse.parse_qs(request.data.decode("utf-8"))
        self.assertEqual(json.loads(form["data"][0])["objname"], "2026abc")
        self.assertEqual(detail["latestPhotometry"]["value"], 15.4)
        self.assertEqual(detail["host"]["name"], "NGC 999")

    def test_detail_normalization_is_fail_closed_and_preserves_zero_and_limits(self):
        detail = queue_builder.normalize_tns_detail(
            {
                "type": {"name": "Nova"},
                "redshift": 0,
                "hostname": "M 100",
                "host_redshift": 0,
                "photometry": [
                    {
                        "obsdate": "2026-09-10 03:00:00",
                        "flux": "12.0",
                    },
                    {
                        "obsdate": "2026-09-09 03:00:00",
                        "flux": "",
                        "limflux": "20.1",
                        "flux_unit": {"name": "ABMag"},
                        "public": 1,
                    },
                ],
                "spectra": [],
            }
        )

        self.assertEqual(detail["redshift"], 0.0)
        self.assertEqual(detail["host"]["redshift"], 0.0)
        self.assertEqual(detail["latestPhotometry"]["value"], 20.1)
        self.assertTrue(detail["latestPhotometry"]["isUpperLimit"])

    def test_authoritative_contaminant_classification_forces_reject(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")

        queue_builder.merge_tns_detail(
            candidate,
            {
                "currentType": "CV",
                "redshift": None,
                "host": {},
                "latestPhotometry": None,
                "spectra": None,
            },
            retrieved_at="2026-09-10T00:00:00Z",
            source_kind="tns_get_object_api",
        )

        self.assertEqual(candidate["classification"]["kind"], "contaminant")
        self.assertEqual(candidate["recommendedDecision"], "reject")
        self.assertEqual(candidate["enrichment"]["status"], "partial")

    def test_get_object_retries_json_rate_limit_response(self):
        queue = self.build()
        candidate = next(item for item in queue["opportunities"] if item["sourceId"] == "1001")

        def response(payload, headers):
            result = io.BytesIO(json.dumps(payload).encode("utf-8"))
            result.headers = headers
            return result

        throttled = response(
            {"id_code": 429, "id_message": "rate limited", "data": {"reply": {}}},
            {"Retry-After": "1"},
        )
        successful = response(
            {"id_code": 200, "id_message": "OK", "data": {"reply": {"type": "SN Ia"}}},
            {"x-rate-limit-remaining": "9"},
        )

        with mock.patch.object(
            queue_builder.urllib.request,
            "urlopen",
            side_effect=[throttled, successful],
        ) as mocked:
            with mock.patch.object(queue_builder.time, "sleep") as sleeper:
                detail, _ = queue_builder.fetch_tns_object_detail(
                    candidate,
                    api_key="secret",
                    user_agent='tns_marker{"tns_id": 1, "type": "bot", "name": "test"}',
                )

        self.assertEqual(mocked.call_count, 2)
        sleeper.assert_called_once_with(1)
        self.assertEqual(detail["currentType"], "SN Ia")

    def test_detail_api_failure_degrades_one_candidate_and_continues(self):
        queue = self.build()
        detail = {
            "currentType": "SN Ia",
            "redshift": 0.01,
            "host": {},
            "latestPhotometry": {
                "observationDateUTC": "2026-09-09T00:00:00Z",
                "value": 15.0,
                "band": "r",
                "units": "ABMag",
                "isUpperLimit": False,
            },
            "spectra": {"count": 0, "latest": None},
        }

        with contextlib.redirect_stderr(io.StringIO()):
            with mock.patch.object(
                queue_builder,
                "fetch_tns_object_detail",
                side_effect=[OSError("temporary failure"), (detail, {"x-rate-limit-remaining": "9"})],
            ) as mocked:
                queue_builder.enrich_queue_from_tns_api(
                    queue,
                    api_key="secret",
                    user_agent='tns_marker{"tns_id": 1, "type": "bot", "name": "test"}',
                    max_lookups=2,
                )

        self.assertEqual(mocked.call_count, 2)
        self.assertEqual(queue["opportunities"][0]["enrichment"]["status"], "partial")
        self.assertEqual(
            queue["opportunities"][0]["enrichment"]["detailLookupError"],
            "tns_detail_lookup_failed",
        )
        self.assertEqual(queue["opportunities"][1]["reportedMagnitude"]["value"], 15.0)

    def test_rate_limit_exhaustion_after_success_marks_remaining_candidates_partial(self):
        queue = self.build()
        detail = {
            "currentType": "SN Ia",
            "redshift": 0.01,
            "host": {},
            "latestPhotometry": None,
            "spectra": {"count": 0, "latest": None},
        }

        with contextlib.redirect_stderr(io.StringIO()):
            with mock.patch.object(
                queue_builder,
                "fetch_tns_object_detail",
                return_value=(detail, {"x-rate-limit-remaining": "0", "Retry-After": "120"}),
            ) as mocked:
                with mock.patch.object(queue_builder.time, "sleep") as sleeper:
                    queue_builder.enrich_queue_from_tns_api(
                        queue,
                        api_key="secret",
                        user_agent='tns_marker{"tns_id": 1, "type": "bot", "name": "test"}',
                        max_lookups=2,
                    )

        self.assertEqual(mocked.call_count, 1)
        sleeper.assert_not_called()
        self.assertEqual(
            queue["opportunities"][1]["enrichment"]["detailLookupError"],
            "tns_rate_limited_before_lookup",
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
