import copy
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transient_early_policy import RisePolicy, evaluate


class EarlyPolicyTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 5, tzinfo=dt.UTC)
        self.candidate = {"id": "synthetic:1", "classification": {"kind": "transient_candidate"},
                          "score": 100, "tnsContext": {"publicPhotometry": [
                              self.point("2026-11-03T00:00:00Z", 21),
                              self.point("2026-11-04T00:00:00Z", 20)]}}

    def point(self, stamp, value):
        return dict(observationDateUTC=stamp, value=value, error=0.05, band="r",
                    units="mag", system="AB", correction="uncorrected", source="synthetic")

    def evaluate(self):
        return evaluate(self.candidate, now=self.now)[0]

    def test_faint_unclassified_rise_is_independent_and_nonpublishing(self):
        reasons = self.evaluate()
        self.assertEqual([r["code"] for r in reasons], ["rapid_rise"])
        self.assertFalse(reasons[0]["automaticEligible"])

    def test_classification_only_hold_does_not_hide_independent_rise_evidence(self):
        self.candidate["recommendedDecision"] = "hold"
        self.candidate["decisionReason"] = "Hold pending a confirmed high-interest classification."
        self.assertEqual([reason["code"] for reason in self.evaluate()], ["rapid_rise"])
        self.candidate["reviewDecision"] = "hold"
        self.assertEqual(self.evaluate(), [])
        self.candidate["reviewDecision"] = "pending"
        self.candidate["astroGuideObject"] = {"identityWarning": "unresolved identity"}
        self.assertEqual(self.evaluate(), [])

    def test_score_boundary_and_unclassified(self):
        self.candidate["tnsContext"] = {}
        self.assertEqual(self.evaluate(), [])
        self.candidate["classification"]["kind"] = "supernova"
        self.candidate["classification"]["type"] = "SN Ia"
        for score, count in [(69, 0), (70, 1), (71, 1)]:
            self.candidate["score"] = score
            self.assertEqual(len(self.evaluate()), count)

    def test_incompatible_bands_limits_and_missing_uncertainty(self):
        original = copy.deepcopy(self.candidate)
        for key, value in [("band", "g"), ("isUpperLimit", True), ("error", None),
                           ("system", None), ("correction", "dereddened"), ("value", float("nan"))]:
            self.candidate = copy.deepcopy(original)
            self.candidate["tnsContext"]["publicPhotometry"][1][key] = value
            self.assertEqual(self.evaluate(), [])

    def test_stable_on_append_and_stale_fails(self):
        first = self.evaluate()[0]["stableTriggerID"]
        self.candidate["tnsContext"]["publicPhotometry"].append(self.point("2026-11-05T00:00:00Z", 19))
        self.assertEqual(self.evaluate()[0]["stableTriggerID"], first)
        self.assertEqual(evaluate(self.candidate, now=self.now + dt.timedelta(days=10))[0], [])

    def test_protect_contaminants_and_explicit_warnings(self):
        for key, value in [("recommendedDecision", "reject"), ("decisionReason", "owner hold")]:
            self.candidate[key] = value
            self.assertEqual(self.evaluate(), [])
            del self.candidate[key]

    def test_rate_threshold_is_configurable(self):
        self.assertEqual(evaluate(self.candidate, now=self.now, policy=RisePolicy(minimum_rate=2))[0], [])
        with self.assertRaises(ValueError):
            RisePolicy(minimum_rate=-1)

    def test_uncertain_classification_never_qualifies_by_score(self):
        self.candidate["tnsContext"] = {}
        for type_name in (None, "SN Ia?", "SN candidate", "unclassified"):
            self.candidate["classification"] = {"kind": "supernova", "type": type_name}
            self.assertEqual(self.evaluate(), [])

    def test_invalid_scores_do_not_approve_and_time_must_be_explicit(self):
        self.candidate["tnsContext"] = {}
        self.candidate["classification"] = {"kind": "supernova", "type": "SN Ia"}
        for score in ("70", True, float("nan"), float("inf"), -1, 101, None):
            self.candidate["score"] = score
            self.assertEqual(self.evaluate(), [])
        with self.assertRaises(ValueError):
            evaluate(self.candidate, now=dt.datetime(2026, 11, 5))

    def test_zero_interval_future_and_negative_errors_fail(self):
        points = self.candidate["tnsContext"]["publicPhotometry"]
        points[1]["observationDateUTC"] = points[0]["observationDateUTC"]
        self.assertEqual(self.evaluate(), [])
        points[1]["observationDateUTC"] = "2026-11-06T00:00:00Z"
        self.assertEqual(self.evaluate(), [])
        points[1]["observationDateUTC"] = "2026-11-04T00:00:00Z"
        points[1]["error"] = -1
        self.assertEqual(self.evaluate(), [])
