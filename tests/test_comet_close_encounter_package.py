import datetime as dt
import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_comet_close_encounter_package.py"
)
SPEC = importlib.util.spec_from_file_location(
    "build_comet_close_encounter_package",
    SCRIPT_PATH,
)
encounters = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = encounters
assert SPEC.loader is not None
SPEC.loader.exec_module(encounters)


class CometCloseEncounterPackageTests(unittest.TestCase):
    def setUp(self):
        self.package_start = dt.datetime(2026, 8, 11, tzinfo=dt.UTC)
        self.package_end = dt.datetime(2027, 7, 12, tzinfo=dt.UTC)
        self.shard_start = dt.datetime(2026, 8, 1, tzinfo=dt.UTC)
        self.shard_end = dt.datetime(2026, 9, 1, tzinfo=dt.UTC)
        self.comet_ids = {"COMET:10P"}
        self.dynamic_body_ids = {"moon", "mars"}
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
        event_id = encounters.event_identifier("COMET:10P", "M45", timestamp)
        return {
            "id": event_id,
            "eventFamily": encounters.EVENT_FAMILY,
            "type": encounters.EVENT_TYPE,
            "eventTimeUTC": timestamp_text,
            "closestApproachUTC": timestamp_text,
            "minimumSeparationDegrees": separation,
            "participants": [
                {
                    "kind": "comet",
                    "id": "COMET:10P",
                    "designation": "10P",
                    "displayName": "10P/Tempel",
                    "magnitude": 13.2,
                    "coordinate": {
                        "rightAscensionHours": 3.2,
                        "declinationDegrees": 24.1,
                    },
                },
                {
                    "kind": "deepSkyObject",
                    "id": "M45",
                    "catalogID": "M45",
                    "displayName": "Pleiades",
                    "objectType": "Open_cluster",
                    "magnitude": 1.6,
                    "coordinate": {
                        "rightAscensionHours": 3.783333,
                        "declinationDegrees": 24.1167,
                    },
                },
            ],
            "source": {
                "packageFamily": encounters.PACKAGE_FAMILY,
                "packageVersion": "comet-close-encounters-v1-test",
                "recordID": event_id,
                "sourceDescription": "Unit test",
            },
        }

    def make_dynamic_event(self, separation=0.75):
        timestamp = dt.datetime(2026, 8, 13, 4, 5, 6, tzinfo=dt.UTC)
        timestamp_text = encounters.lunar.isoformat_z(timestamp)
        event_id = encounters.event_identifier(
            "COMET:10P",
            "moon",
            timestamp,
            event_type=encounters.COMET_DYNAMIC_EVENT_TYPE,
        )
        return {
            "id": event_id,
            "eventFamily": encounters.EVENT_FAMILY,
            "type": encounters.COMET_DYNAMIC_EVENT_TYPE,
            "eventTimeUTC": timestamp_text,
            "closestApproachUTC": timestamp_text,
            "minimumSeparationDegrees": separation,
            "participants": [
                {
                    "kind": "comet",
                    "id": "COMET:10P",
                    "designation": "10P",
                    "displayName": "10P/Tempel",
                    "magnitude": 13.2,
                    "coordinate": {
                        "rightAscensionHours": 3.2,
                        "declinationDegrees": 24.1,
                    },
                },
                {
                    "kind": "moon",
                    "id": "moon",
                    "displayName": "Moon",
                    "magnitude": -10.1,
                    "coordinate": {
                        "rightAscensionHours": 3.25,
                        "declinationDegrees": 24.3,
                    },
                    "illuminationFraction": 0.42,
                    "phaseLabel": "Waxing Crescent",
                },
            ],
            "source": {
                "packageFamily": encounters.PACKAGE_FAMILY,
                "packageVersion": "comet-close-encounters-v1-test",
                "recordID": event_id,
                "sourceDescription": "Unit test",
            },
        }

    def validate(self, events):
        return encounters.validate_events(
            events,
            threshold=5.0,
            package_start=self.package_start,
            package_end=self.package_end,
            shard_start=self.shard_start,
            shard_end=self.shard_end,
            comet_ids=self.comet_ids,
            target_groups=self.target_groups,
            dynamic_body_ids=self.dynamic_body_ids,
        )

    def test_stable_id_uses_pair_and_utc_date(self):
        morning = dt.datetime(2026, 8, 12, 0, 0, tzinfo=dt.UTC)
        evening = dt.datetime(2026, 8, 12, 23, 59, tzinfo=dt.UTC)

        self.assertEqual(
            encounters.event_identifier("COMET:10P", "M 45", morning),
            encounters.event_identifier("COMET:10P", "M 45", evening),
        )
        self.assertEqual(
            encounters.event_identifier("COMET:10P", "M 45", morning),
            "comet-target-close-encounter-COMET-10P-M-45-20260812",
        )
        self.assertEqual(
            encounters.event_identifier(
                "COMET:10P",
                "moon",
                morning,
                event_type=encounters.COMET_DYNAMIC_EVENT_TYPE,
            ),
            "comet-dynamic-close-encounter-COMET-10P-moon-20260812",
        )

    def test_valid_event_checks_timestamp_identity_threshold_coordinates_and_source(self):
        counts = self.validate([self.make_event()])

        self.assertEqual(
            counts,
            {
                "events": 1,
                "eventsByType": {encounters.COMET_TARGET_EVENT_TYPE: 1},
                "eventsByComet": {"COMET:10P": 1},
                "eventsByTarget": {"M45": 1},
                "eventsBySolarSystemBody": {},
            },
        )

    def test_valid_dynamic_event_checks_moon_participant_shape(self):
        counts = self.validate([self.make_dynamic_event()])

        self.assertEqual(
            counts,
            {
                "events": 1,
                "eventsByType": {encounters.COMET_DYNAMIC_EVENT_TYPE: 1},
                "eventsByComet": {"COMET:10P": 1},
                "eventsByTarget": {},
                "eventsBySolarSystemBody": {"moon": 1},
            },
        )

    def test_separation_above_threshold_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "outside the package threshold"):
            self.validate([self.make_event(separation=5.0001)])

    def test_missing_coordinate_is_rejected(self):
        event = self.make_event()
        del event["participants"][0]["coordinate"]

        with self.assertRaisesRegex(RuntimeError, "missing coordinates"):
            self.validate([event])

    def test_unknown_dynamic_body_is_rejected(self):
        event = self.make_dynamic_event()
        event["participants"][1]["id"] = "pluto"

        with self.assertRaisesRegex(RuntimeError, "unknown dynamic body"):
            self.validate([event])

    def test_dynamic_event_uses_dynamic_threshold(self):
        with self.assertRaisesRegex(RuntimeError, "outside the package threshold"):
            encounters.validate_events(
                [self.make_dynamic_event(separation=0.75)],
                threshold=5.0,
                dynamic_threshold=0.7,
                package_start=self.package_start,
                package_end=self.package_end,
                shard_start=self.shard_start,
                shard_end=self.shard_end,
                comet_ids=self.comet_ids,
                target_groups=self.target_groups,
                dynamic_body_ids=self.dynamic_body_ids,
            )

    def test_interpolates_right_ascension_across_zero_hours(self):
        stream = encounters.CometStream(
            stable_id="COMET:WRAP",
            designation="C/2026 W1",
            display_name="Wrap Comet",
            orbit_class=None,
            samples=[
                encounters.CometSample(
                    timestamp=dt.datetime(2026, 8, 11, 0, 0, tzinfo=dt.UTC),
                    right_ascension_hours=23.9,
                    declination_degrees=0.0,
                    magnitude=12.0,
                ),
                encounters.CometSample(
                    timestamp=dt.datetime(2026, 8, 11, 12, 0, tzinfo=dt.UTC),
                    right_ascension_hours=0.1,
                    declination_degrees=2.0,
                    magnitude=14.0,
                ),
            ],
        )

        state = encounters.interpolate_comet_state(
            stream,
            dt.datetime(2026, 8, 11, 6, 0, tzinfo=dt.UTC),
        )

        self.assertAlmostEqual(state.right_ascension_hours, 0.0, places=6)
        self.assertAlmostEqual(state.declination_degrees, 1.0, places=6)
        self.assertAlmostEqual(state.magnitude, 13.0, places=6)


if __name__ == "__main__":
    unittest.main()
