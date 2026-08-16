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
                        "orbitClass": "Periodic Comet",
                        "aliases": ["0220P"],
                        "ephemerisValidStart": "2026-08-01T00:00:00Z",
                        "ephemerisValidEnd": "2026-09-01T00:00:00Z",
                    }
                ],
            },
            "ephemeris": {
                "generatedAt": "2026-08-15T00:00:00Z",
                "anchorTimestamp": "2026-08-08T00:00:00Z",
                "sampleStepHours": 24,
                "sampleCount": 8,
                "comets": {
                    "COMET:220P": [
                        [2.70, 9.50, 16.8],
                        [2.71, 9.51, 16.3],
                        [2.72, 9.52, 15.8],
                        [2.73, 9.53, 15.2],
                        [2.74, 9.54, 14.8],
                        [2.75, 9.55, 14.7],
                        [2.76, 9.56, 14.8],
                        [2.77, 9.57, 15.0],
                    ]
                },
            },
        }

    def make_orbit_geometry(self):
        return {
            "schemaVersion": 1,
            "packageFamily": "cometOrbitGeometry",
            "records": [
                {
                    "stableID": "COMET:220P",
                    "orbitClass": "Periodic Comet",
                    "jplOrbitClassCode": "JFc",
                    "inclinationDegrees": 8.1,
                    "orbitalPeriodDays": 2007.8,
                    "eccentricity": 0.5,
                }
            ],
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
                            {
                                "date": "2026-08-08",
                                "magnitude": 7.3,
                                "bestAltitudeDegrees": 53.0,
                                "elongationDegrees": 93.0,
                            },
                            {
                                "date": "2026-08-15",
                                "magnitude": 8.0,
                                "bestAltitudeDegrees": 56.0,
                                "elongationDegrees": 97.0,
                            },
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
                    orbit_geometry=self.make_orbit_geometry(),
                    generated_at="2026-08-15T00:00:00Z",
                    cache_images=True,
                    image_limit=1,
                    max_image_bytes=128,
                    brightness_lookback_days=90,
                    useful_magnitude_limit=16.0,
                    fetcher=lambda _: b"fake image bytes",
                )
            finally:
                detail.REPO_ROOT = original_root

        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record["stableID"], "COMET:220P")
        self.assertEqual(record["source"]["permissionReceived"], "2026-08-15")
        self.assertTrue(record["media"]["thumbnail"]["url"].startswith("https://metadata.astroguide.space/"))
        self.assertEqual(record["media"]["thumbnail"]["cachedPath"], "v1/assets/comets/aerith/comet_220p_43044b9f977e.jpg")
        self.assertEqual(record["media"]["hero"]["kind"], "hero")
        self.assertIn("aerith.net/pictures", record["media"]["thumbnail"]["originalURL"])
        self.assertEqual(record["media"]["thumbnail"]["sourceURL"], record["detailURL"])
        self.assertEqual(record["visibilitySummary"]["state"], "current")
        self.assertEqual(record["classification"]["orbitalFamily"], "jupiter_family")
        self.assertEqual(record["classification"]["inclinationClass"], "low_inclination")
        self.assertEqual(record["classification"]["returnStatus"], "returning")
        self.assertEqual(record["brightnessChart"]["availableStartDate"], "2026-06-03")
        self.assertEqual(record["brightnessChart"]["availableEndDate"], "2026-08-15")
        self.assertTrue(record["brightnessChart"]["containsProjection"])
        self.assertEqual(record["brightnessTrend"]["direction"], "fading")
        self.assertEqual(record["ephemerisSummary"]["firstFutureUsefulDate"], "2026-08-10")
        significant = [point for point in record["brightness"] if point.get("isSignificant")]
        self.assertTrue(significant)
        self.assertIn("outburst", significant[0].get("significanceKind", ""))
        self.assertTrue(
            any("outburst" in point.get("commentary", "").lower() for point in record["brightness"])
        )

    def test_visibility_summary_has_first_class_coming_soon_state(self):
        source = self.make_aerith_source()
        source["comets"][0]["weeklyRowsByHemisphere"]["north"] = [
            {
                "date": "2026-08-08",
                "magnitude": 17.2,
                "bestAltitudeDegrees": 4.0,
                "elongationDegrees": 20.0,
            },
            {
                "date": "2026-08-15",
                "magnitude": 14.8,
                "bestAltitudeDegrees": 35.0,
                "elongationDegrees": 70.0,
            },
        ]

        records = detail.build_records(
            self.make_comet_snapshot(),
            source,
            orbit_geometry=self.make_orbit_geometry(),
            generated_at="2026-08-15T00:00:00Z",
            cache_images=False,
            image_limit=0,
            max_image_bytes=128,
        )

        self.assertEqual(records[0]["visibilitySummary"]["state"], "comingSoon")
        self.assertEqual(records[0]["visibilitySummary"]["aerithNextUsefulDate"], "2026-08-15")

    def test_validate_package_rejects_hotlinked_cached_media(self):
        original_root = detail.REPO_ROOT
        with tempfile.TemporaryDirectory() as temp_dir:
            detail.REPO_ROOT = Path(temp_dir)
            try:
                records = detail.build_records(
                    self.make_comet_snapshot(),
                    self.make_aerith_source(),
                    orbit_geometry=self.make_orbit_geometry(),
                    generated_at="2026-08-15T00:00:00Z",
                    cache_images=True,
                    image_limit=1,
                    max_image_bytes=128,
                    fetcher=lambda _: b"fake image bytes",
                )
                descriptor = detail.write_detail_package(
                    records,
                    package_version="comet-detail-metadata-v1-test",
                    generated_at="2026-08-15T00:00:00Z",
                    min_supported_app_version="1.4.1",
                    min_supported_build="1",
                    update_manifest_path=None,
                )
                package_path = detail.REPO_ROOT / detail.PACKAGE_PATH
                package = detail.read_json(package_path)
                detail.validate_package(package, package_path)
                self.assertEqual(descriptor["recordCount"], 1)

                shard_path = detail.REPO_ROOT / package["comets"][0]["path"]
                shard = detail.read_json(shard_path)
                shard["record"]["media"]["thumbnail"]["url"] = "http://www.aerith.net/pictures/hotlink.jpg"
                detail.write_json(shard_path, shard)
                package["comets"][0]["byteSize"] = shard_path.stat().st_size
                package["comets"][0]["checksum"] = detail.hashlib.sha256(shard_path.read_bytes()).hexdigest()
                detail.write_json(package_path, package)

                with self.assertRaises(RuntimeError):
                    detail.validate_package(package, package_path)
            finally:
                detail.REPO_ROOT = original_root

    def test_report_dates_are_resolved_against_source_page_year(self):
        date = detail.date_from_report_text("Aug. 5", detail.source_page_date(self.make_aerith_source()))

        self.assertEqual(date, "2026-08-05")


if __name__ == "__main__":
    unittest.main()
