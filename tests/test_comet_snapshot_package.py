import datetime as dt
import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_comet_snapshot_package.py"
)
SPEC = importlib.util.spec_from_file_location("build_comet_snapshot_package", SCRIPT_PATH)
snapshot = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = snapshot
assert SPEC.loader is not None
SPEC.loader.exec_module(snapshot)


class CometSnapshotPackageTests(unittest.TestCase):
    def make_package(self):
        anchor = dt.datetime(2026, 8, 8, tzinfo=dt.UTC)
        return {
            "schemaVersion": 1,
            "packageFamily": "cometSnapshot",
            "packageVersion": "comet-snapshot-v1-test",
            "generatedAt": "2026-08-14T00:00:00Z",
            "source": {"name": "Unit Test"},
            "seeds": {
                "generatedAt": "2026-08-14T00:00:00Z",
                "comets": [
                    {
                        "stableID": "COMET:220P",
                        "designation": "220P",
                        "displayName": "220P/McNaught",
                        "aliases": ["0220"],
                    }
                ],
            },
            "ephemeris": {
                "generatedAt": "2026-08-14T00:00:00Z",
                "anchorTimestamp": anchor.isoformat().replace("+00:00", "Z"),
                "sampleStepHours": 24,
                "sampleCount": 8,
                "comets": {
                    "COMET:220P": [
                        [2.70, 9.50, 16.5],
                        [2.71, 9.51, 16.6],
                        [2.72, 9.52, 16.7],
                        [2.73, 9.53, 16.8],
                        [2.74, 9.54, 16.9],
                        [2.75, 9.55, 17.0],
                        [2.76, 9.56, 17.1],
                        [2.77, 9.57, 17.2],
                    ]
                },
            },
        }

    def make_aerith_source(self):
        return {
            "schemaVersion": 1,
            "generatedAt": "2026-08-14T00:00:00Z",
            "source": {
                "name": "Aerith Weekly Information about Bright Comets",
                "sourceURL": "http://www.aerith.net/comet/weekly/current.html",
                "permissionStatus": "permission-requested",
            },
            "comets": [
                {
                    "aerithName": "220P/McNaught",
                    "normalizedDesignation": "220P",
                    "hemispheres": ["north"],
                    "pageRanks": {"north": 1},
                    "sourcePageURLs": {"north": "http://www.aerith.net/comet/weekly/current.html"},
                    "detailURL": "http://www.aerith.net/comet/catalog/0220P/2026.html",
                    "thumbnailImageURL": "http://www.aerith.net/pictures/fichtl/s/220P.jpg",
                    "imagePermissionStatus": "permission-requested",
                    "weeklyRowsByHemisphere": {
                        "north": [
                            {"date": "2026-08-08", "magnitude": 7.3},
                            {"date": "2026-08-15", "magnitude": 8.0},
                        ]
                    },
                    "currentMagnitude": 7.3,
                    "nextWeekMagnitude": 8.0,
                }
            ],
        }

    def test_aerith_source_adds_candidate_media_without_promoting_images_by_default(self):
        package = snapshot.apply_aerith_source(
            self.make_package(),
            self.make_aerith_source(),
            apply_magnitudes=False,
            promote_images=False,
        )

        seed = package["seeds"]["comets"][0]
        self.assertNotIn("heroImageURL", seed)
        self.assertEqual(
            seed["source"]["aerithWeekly"]["candidateHeroImageURL"],
            "http://www.aerith.net/pictures/fichtl/s/220P.jpg",
        )
        self.assertEqual(
            package["source"]["aerithWeeklySource"]["imageUsage"],
            "candidate-only",
        )

    def test_aerith_magnitudes_patch_ephemeris_samples_between_weekly_rows(self):
        package = snapshot.apply_aerith_source(
            self.make_package(),
            self.make_aerith_source(),
            apply_magnitudes=True,
            promote_images=False,
        )

        samples = package["ephemeris"]["comets"]["COMET:220P"]
        self.assertEqual(samples[0][2], 7.3)
        self.assertEqual(samples[-1][2], 8.0)
        self.assertAlmostEqual(samples[3][2], 7.6)
        self.assertEqual(package["source"]["aerithMagnitudePatches"][0]["sampleCount"], 8)

    def test_aerith_images_can_be_promoted_after_permission(self):
        package = snapshot.apply_aerith_source(
            self.make_package(),
            self.make_aerith_source(),
            apply_magnitudes=False,
            promote_images=True,
        )

        seed = package["seeds"]["comets"][0]
        self.assertEqual(
            seed["heroImageURL"],
            "http://www.aerith.net/pictures/fichtl/s/220P.jpg",
        )
        self.assertEqual(
            package["source"]["aerithWeeklySource"]["imageUsage"],
            "promoted-to-heroImageURL",
        )


if __name__ == "__main__":
    unittest.main()
