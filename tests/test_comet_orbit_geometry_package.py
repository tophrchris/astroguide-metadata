import datetime as dt
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_comet_orbit_geometry_package.py"
)
SPEC = importlib.util.spec_from_file_location(
    "build_comet_orbit_geometry_package",
    SCRIPT_PATH,
)
geometry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = geometry
assert SPEC.loader is not None
SPEC.loader.exec_module(geometry)


class CometOrbitGeometryPackageTests(unittest.TestCase):
    def make_record(self, stable_id="COMET:TEST", rendering_kind="closedOrbit"):
        path_samples = (
            [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]
            if rendering_kind == "closedOrbit"
            else [[1.0, 0.0, 0.0], [3.0, 1.0, 0.0]]
        )
        return {
            "stableID": stable_id,
            "designation": "C/2026 T1",
            "displayName": "Test Comet",
            "orbitClass": "Periodic Comet",
            "renderingKind": rendering_kind,
            "pathSampleFrame": "heliocentric-ecliptic-j2000-au",
            "pathSamples": path_samples,
            "datedSampleFrame": "heliocentric-ecliptic-j2000-au",
            "datedSamples": [
                [2_461_000.5, 1.0, 0.0, 0.0],
                [2_461_003.5, 1.1, 0.1, 0.0],
            ],
            "tailModel": {
                "direction": "antiSolar",
                "extent": "estimatedPlanningEnvelope",
                "estimatedLengthDegrees": 1.5,
            },
        }

    def test_rendering_kind_assigns_honest_trajectory_arcs(self):
        periodic_seed = {"orbitClass": "Periodic Comet"}
        long_period_seed = {"orbitClass": "Non-periodic Comet"}

        self.assertEqual(
            geometry.rendering_kind(periodic_seed, {"e": 0.55, "per": 1_900.0}),
            "closedOrbit",
        )
        self.assertEqual(
            geometry.rendering_kind(long_period_seed, {"e": 0.55, "per": 1_900.0}),
            "trajectoryArc",
        )
        self.assertEqual(
            geometry.rendering_kind(periodic_seed, {"e": 1.01, "per": None}),
            "trajectoryArc",
        )

    def test_build_package_validates_seed_coverage_and_serializes_deterministically(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source_path = temp_path / "comet_orbits.json"
            seeds_path = temp_path / "comet_seeds.json"
            source_package = {
                "schemaVersion": 1,
                "generatedAt": "2026-08-11T00:00:00Z",
                "source": {
                    "name": "Unit Test",
                    "url": "https://example.com",
                    "seedPath": "comet_seeds.json",
                    "algorithmVersion": "test-v1",
                    "notes": ["fixture"],
                },
                "recordCount": 2,
                "records": [
                    self.make_record("COMET:B", "trajectoryArc"),
                    self.make_record("COMET:A", "closedOrbit"),
                ],
            }
            seed_bundle = {
                "generatedAt": "2026-08-11T00:00:00Z",
                "comets": [
                    {"stableID": "COMET:A"},
                    {"stableID": "COMET:B"},
                ],
            }
            source_path.write_bytes(geometry.json_bytes(source_package))
            seeds_path.write_bytes(geometry.json_bytes(seed_bundle))

            package = geometry.build_package(
                source_package=source_package,
                source_package_path=source_path,
                seed_bundle=seed_bundle,
                seeds_path=seeds_path,
                app_repo=temp_path,
                generated_at="2026-08-11T00:00:00Z",
                package_version="comet-orbit-geometry-v1-test",
            )

        geometry.validate_package(package)
        self.assertEqual(package["packageFamily"], geometry.PACKAGE_FAMILY)
        self.assertEqual([record["stableID"] for record in package["records"]], ["COMET:A", "COMET:B"])
        self.assertEqual(package["counts"]["renderingKinds"], {"closedOrbit": 1, "trajectoryArc": 1})
        self.assertEqual(
            geometry.json_bytes(package, compact=True),
            geometry.json_bytes(package, compact=True),
        )

    def test_closed_orbit_samples_must_close(self):
        record = self.make_record()
        record["pathSamples"][-1] = [2.0, 0.0, 0.0]

        with self.assertRaisesRegex(RuntimeError, "does not close"):
            geometry.validate_records([record], seed_ids=None)

    def test_trajectory_arc_samples_need_not_close(self):
        counts = geometry.validate_records(
            [self.make_record(rendering_kind="trajectoryArc")],
            seed_ids=None,
        )

        self.assertEqual(counts["renderingKinds"], {"trajectoryArc": 1})


if __name__ == "__main__":
    unittest.main()
