import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_comet_detail_metadata_package.py"
)
SPEC = importlib.util.spec_from_file_location("build_comet_detail_metadata_package", SCRIPT_PATH)
detail = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = detail
assert SPEC.loader is not None
SPEC.loader.exec_module(detail)


class CometDetailMetadataPackageTests(unittest.TestCase):
    def make_comet_snapshot(self):
        return {
            "schemaVersion": 1,
            "packageFamily": "cometSnapshot",
            "packageVersion": "comet-snapshot-v1-test",
            "generatedAt": "2026-08-15T00:00:00Z",
            "seeds": {
                "comets": [
                    {
                        "stableID": "COMET:220P",
                        "designation": "220P",
                        "displayName": "220P/McNaught",
                        "aliases": ["0220P"],
                    }
                ],
            },
            "ephemeris": {"comets": {"COMET:220P": []}},
        }

    def make_aerith_source(self):
        return {
            "schemaVersion": 1,
            "generatedAt": "2026-08-15T00:00:00Z",
            "source": {
                "name": "Aerith Weekly Information about Bright Comets",
                "sourceURL": "http://www.aerith.net/comet/weekly/current.html",
                "permissionStatus": "permission-granted",
                "permissionReceived": "2026-08-15",
            },
            "pages": [{"pageDate": "2026-08-08"}],
            "comets": [
                {
                    "aerithName": "220P/McNaught",
                    "normalizedDesignation": "220P",
                    "sourcePageURLs": {"north": "http://www.aerith.net/comet/weekly/current.html"},
                    "detailURL": "http://www.aerith.net/comet/catalog/0220P/2026.html",
                    "thumbnailImageURL": "http://www.aerith.net/pictures/fichtl/s/220P.jpg",
                    "sourceCommentaries": ["Another major outburst occurred on Aug. 5."],
                    "reportedMagnitudes": [
                        {
                            "magnitude": 8.3,
                            "reportedDateText": "June 3",
                            "observer": "Marco Goiato",
                        },
                        {
                            "magnitude": 7.0,
                            "reportedDateText": "Aug. 5",
                            "observer": "Giuseppe Pappa",
                        },
                    ],
                    "weeklyRowsByHemisphere": {
                        "north": [
                            {"date": "2026-08-08", "magnitude": 7.3},
                            {"date": "2026-08-15", "magnitude": 8.0},
                        ]
                    },
                }
            ],
        }

    def test_build_records_emits_aerith_brightness_comments_and_cached_media(self):
        original_root = detail.REPO_ROOT
        with tempfile.TemporaryDirectory() as temp_dir:
            detail.REPO_ROOT = Path(temp_dir)
            try:
                records = detail.build_records(
                    self.make_comet_snapshot(),
                    self.make_aerith_source(),
                    generated_at="2026-08-15T00:00:00Z",
                    cache_images=True,
                    image_limit=1,
                    max_image_bytes=128,
                    fetcher=lambda _: b"fake image bytes",
                )
            finally:
                detail.REPO_ROOT = original_root

        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record["stableID"], "COMET:220P")
        self.assertEqual(record["source"]["permissionReceived"], "2026-08-15")
        self.assertTrue(record["media"]["thumbnail"]["url"].startswith("https://metadata.astroguide.space/"))
        self.assertEqual(record["media"]["thumbnail"]["sourceURL"], record["detailURL"])
        significant = [point for point in record["brightness"] if point.get("isSignificant")]
        self.assertTrue(significant)
        self.assertIn("outburst", significant[0].get("significanceKind", ""))
        self.assertTrue(
            any("outburst" in point.get("commentary", "").lower() for point in record["brightness"])
        )

    def test_report_dates_are_resolved_against_source_page_year(self):
        date = detail.date_from_report_text("Aug. 5", detail.source_page_date(self.make_aerith_source()))

        self.assertEqual(date, "2026-08-05")


if __name__ == "__main__":
    unittest.main()
