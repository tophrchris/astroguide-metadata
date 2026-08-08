import datetime as dt
import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_planet_target_close_encounter_package.py"
)
SPEC = importlib.util.spec_from_file_location(
    "build_planet_target_close_encounter_package",
    SCRIPT_PATH,
)
encounters = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = encounters
assert SPEC.loader is not None
SPEC.loader.exec_module(encounters)


class PlanetTargetCloseEncounterPackageTests(unittest.TestCase):
    def setUp(self):
        self.package_start = dt.datetime(2026, 8, 8, tzinfo=dt.UTC)
        self.package_end = dt.datetime(2028, 8, 8, tzinfo=dt.UTC)
        self.shard_start = dt.datetime(2026, 8, 1, tzinfo=dt.UTC)
        self.shard_end = dt.datetime(2026, 9, 1, tzinfo=dt.UTC)
        self.planet_ids = {"mars"}
        self.target_groups = {
            "M45": {
                "id": "M45",
                "displayName": "Pleiades",
                "objectType": "Open_cluster",
                "targetIDs": ["M45", "CR42"],
            }
        }

    def make_event(self, separation=1.25):
        timestamp = dt.datetime(2026, 8, 12, 4, 5, 6, tzinfo=dt.UTC)
        timestamp_text = encounters.lunar.isoformat_z(timestamp)
        return {
            "id": encounters.event_identifier("mars", "M45", timestamp),
            "eventFamily": encounters.EVENT_FAMILY,
            "type": encounters.EVENT_TYPE,
            "eventTimeUTC": timestamp_text,
            "closestApproachUTC": timestamp_text,
            "minimumSeparationDegrees": separation,
            "participants": [
                {
                    "kind": "majorPlanet",
                    "id": "mars",
                    "displayName": "Mars",
                    "magnitude": 1.2,
                },
                {
                    "kind": "deepSkyObject",
                    "id": "M45",
                    "catalogID": "M45",
                    "displayName": "Pleiades",
                    "objectType": "Open_cluster",
                    "magnitude": 1.6,
                },
            ],
        }

    def validate(self, events):
        return encounters.validate_events(
            events,
            threshold=5.0,
            package_start=self.package_start,
            package_end=self.package_end,
            shard_start=self.shard_start,
            shard_end=self.shard_end,
            planet_ids=self.planet_ids,
            target_groups=self.target_groups,
        )

    def test_stable_id_uses_pair_and_utc_date(self):
        morning = dt.datetime(2026, 8, 12, 0, 0, tzinfo=dt.UTC)
        evening = dt.datetime(2026, 8, 12, 23, 59, tzinfo=dt.UTC)

        self.assertEqual(
            encounters.event_identifier("mars", "M 45", morning),
            encounters.event_identifier("mars", "M 45", evening),
        )
        self.assertEqual(
            encounters.event_identifier("mars", "M 45", morning),
            "planet-target-close-encounter-mars-M-45-20260812",
        )

    def test_valid_event_checks_timestamp_identity_and_threshold(self):
        counts = self.validate([self.make_event()])

        self.assertEqual(counts, {"events": 1, "eventsByPlanet": {"mars": 1}})

    def test_separation_above_threshold_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "outside the package threshold"):
            self.validate([self.make_event(separation=5.0001)])

    def test_noncanonical_event_id_is_rejected(self):
        event = self.make_event()
        event["id"] = "unstable-id"

        with self.assertRaisesRegex(RuntimeError, "stable ID convention"):
            self.validate([event])

    def test_duplicate_event_ids_are_rejected(self):
        event = self.make_event()

        with self.assertRaisesRegex(RuntimeError, "Duplicate event ID"):
            self.validate([event, dict(event)])


if __name__ == "__main__":
    unittest.main()
