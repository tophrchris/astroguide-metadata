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


class PlanetPairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import time
        cls.sky = encounters.lunar.load_skyfield_modules()
        cache = encounters.DEFAULT_EPHEMERIS_CACHE
        if not (cache / "de421.bsp").exists():
            raise unittest.SkipTest("Real-engine check requires existing local DE421; never fetch in tests")
        loader = cls.sky.Loader(str(cache))
        cls.eph = loader("de421.bsp")
        cls.ts = loader.timescale(builtin=True)
        cls.subjects = [encounters.lunar.PlanetSubject(*row) for row in encounters.lunar.PLANET_SUBJECTS]
        cls.start = dt.datetime(2026, 8, 8, tzinfo=dt.UTC)
        cls.end = dt.datetime(2028, 8, 8, tzinfo=dt.UTC)
        started = time.monotonic()
        cls.events = cls.generate(cls.subjects, cls.start, cls.end)
        cls.elapsed = time.monotonic() - started
        print(f"Real DE421 pair scan: {len(cls.events)} records / 21 pairs / 731 days / {cls.elapsed:.2f}s")

    @classmethod
    def generate(cls, subjects, start, end):
        return encounters.compute_planet_pair_encounters(
            sky=cls.sky, planet_subjects=subjects, start=start, end=end,
            max_separation_degrees=5, earth=cls.eph["earth"], eph=cls.eph, ts=cls.ts,
        )

    def test_real_minima_not_daily_threshold_crossings(self):
        self.assertGreater(len(self.events), 10)
        self.assertLess(self.elapsed, 120)
        for row in self.events:
            participants = row["participants"]
            subjects = {p.planet_id: p for p in self.subjects}
            bodies = [self.eph[subjects[p["id"]].ephemeris_key] for p in participants]
            timestamp = encounters.lunar.parse_utc_datetime(row["closestApproachUTC"])
            observer = self.eph["earth"].at(self.ts.from_datetimes([
                timestamp - dt.timedelta(minutes=10), timestamp,
                timestamp + dt.timedelta(minutes=10),
            ]))
            values = observer.observe(bodies[0]).apparent().separation_from(
                observer.observe(bodies[1]).apparent()
            ).degrees
            self.assertLessEqual(values[1], min(values[0], values[2]) + 1e-8)
            self.assertAlmostEqual(values[1], row["minimumSeparationDegrees"], delta=0.000051)
            self.assertTrue(self.start <= timestamp < self.end)

    def test_pair_order_and_renewal_stable_ids(self):
        first, second = self.subjects[:2]
        forward = self.generate([first, second], self.start, self.end)
        reverse = self.generate([second, first], self.start, self.end)
        self.assertEqual(forward, reverse)
        self.assertEqual(len({r["id"] for r in self.events}), len(self.events))
        for row in self.events:
            ids = [p["id"] for p in row["participants"]]
            self.assertEqual(ids, sorted(set(ids)))

    def test_boundary_padding_keeps_minima_on_window_edges(self):
        row = self.events[0]
        center = encounters.lunar.parse_utc_datetime(row["closestApproachUTC"])
        ids = {p["id"] for p in row["participants"]}
        subjects = [p for p in self.subjects if p.planet_id in ids]
        before = self.generate(subjects, center - dt.timedelta(hours=1), center + dt.timedelta(seconds=1))
        after = self.generate(subjects, center + dt.timedelta(seconds=1), center + dt.timedelta(hours=1))
        self.assertEqual([r["id"] for r in before], [row["id"]])
        self.assertEqual(after, [])

    def test_reject_invalid_pair_and_horizon(self):
        for subjects, start, end in (
            ([self.subjects[0]] * 2, self.start, self.end),
            (self.subjects, self.end, self.start),
            (self.subjects, self.start, self.end + dt.timedelta(days=1000)),
        ):
            with self.assertRaises(ValueError):
                self.generate(subjects, start, end)

    def test_existing_validator_accepts_pairs_and_rejects_bad_identity(self):
        row = self.events[0]
        timestamp = encounters.lunar.parse_utc_datetime(row["closestApproachUTC"])
        kwargs = dict(threshold=5, package_start=self.start, package_end=self.end,
                      shard_start=self.start, shard_end=self.end,
                      planet_ids={p.planet_id for p in self.subjects}, target_groups={})
        self.assertEqual(encounters.validate_events([row], **kwargs)["events"], 1)
        for participants in ([row["participants"][0]] * 2, list(reversed(row["participants"]))):
            with self.assertRaises(RuntimeError):
                encounters.validate_events([{**row, "participants": participants}], **kwargs)
        with self.assertRaises(RuntimeError):
            encounters.validate_events([{**row, "id": "wrong"}], **kwargs)
        self.assertEqual(encounters.pair_identifier("venus", "mars", timestamp),
                         encounters.pair_identifier("mars", "venus", timestamp))


if __name__ == "__main__":
    unittest.main()
