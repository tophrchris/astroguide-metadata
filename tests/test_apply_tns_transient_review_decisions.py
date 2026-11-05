import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "apply_tns_transient_review_decisions.py"
)
SPEC = importlib.util.spec_from_file_location("apply_tns_transient_review_decisions", SCRIPT_PATH)
decisions = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = decisions
assert SPEC.loader is not None
SPEC.loader.exec_module(decisions)


def candidate(*, magnitude=17.2, expires="2026-10-10T00:00:00Z"):
    return {
        "id": "tns:1",
        "source": "TNS",
        "sourceId": "1",
        "sourceObjectName": "SN2026abc",
        "sourceURL": "https://www.wis-tns.org/object/2026abc",
        "title": "Supernova SN2026abc near NGC 1",
        "shortTitle": "SN2026abc",
        "eventType": "transientOpportunity",
        "reviewOnly": True,
        "urgency": "urgent",
        "recommendedReviewAction": "approve",
        "recommendedDecision": "approve",
        "reviewDecision": "pending",
        "activeWindow": {
            "startsAtUTC": "2026-09-10T00:00:00Z",
            "expiresAtUTC": expires,
        },
        "discovery": {"dateUTC": "2026-09-10T00:00:00Z", "magnitude": magnitude},
        "classification": {"kind": "supernova", "type": "SN Ia"},
        "coordinates": {"raDegrees": 1.0, "decDegrees": 2.0},
        "astroGuideObject": {"id": "NGC1", "displayName": "NGC 1"},
        "angularSeparationDegrees": 0.1,
        "relationship": {"type": "near_field", "wording": "near-field match"},
        "lastModifiedUTC": "2026-09-20T00:00:00Z",
        "provenance": {"inputRecords": [{"rowNumber": 1}]},
    }


class ApplyTNSReviewDecisionsTests(unittest.TestCase):
    def test_score_activation_is_explicit_and_local_runtime_keeps_reasons(self):
        import copy
        import sys
        sys.path.insert(0, str(SCRIPT_PATH.parent))
        item = candidate(magnitude=21.0)
        item["score"] = 70
        disabled = decisions.sync_decisions(None, None, {"tns:1": copy.deepcopy(item)}, self.provenance,
            generated_at="2026-09-20T00:00:00Z")
        self.assertEqual(disabled["decisions"][0]["status"], "pending")
        candidates = {"tns:1": item}
        enabled = decisions.sync_decisions(None, None, candidates, self.provenance,
            generated_at="2026-09-20T00:00:00Z", early_opportunities=True)
        runtime = decisions.build_runtime(None, enabled, candidates, as_of_date="2026-09-20",
            generated_at="2026-09-20T00:00:00Z")
        emitted = runtime["opportunities"][0]
        self.assertFalse(emitted["reviewOnly"])
        self.assertEqual(emitted["promotionReasons"][0]["confidence"], "score_eligibility")
        self.assertEqual(emitted["activeWindow"]["expiresAtUTC"], "2026-12-09T00:00:00Z")
        trigger = emitted["promotionReasons"][0]["stableTriggerID"]
        refreshed_candidates = {"tns:1": candidate(magnitude=21.0)}
        refreshed_candidates["tns:1"]["score"] = 70
        refreshed = decisions.sync_decisions(enabled, runtime, refreshed_candidates, self.provenance,
            generated_at="2026-09-21T00:00:00Z", early_opportunities=True)
        self.assertEqual(refreshed["decisions"][0]["status"], "approved")
        self.assertEqual(refreshed_candidates["tns:1"]["promotionReasons"][0]["stableTriggerID"], trigger)
        expired = decisions.build_runtime(None, refreshed, refreshed_candidates, as_of_date="2026-12-10",
            generated_at="2026-12-10T00:00:00Z")
        self.assertEqual(expired["opportunities"], [])

    def test_provisional_rise_is_never_auto_approved_even_with_high_score(self):
        import sys
        sys.path.insert(0, str(SCRIPT_PATH.parent))
        item = candidate()
        item.update(score=100, classification={"kind": "transient_candidate", "type": None})
        item["tnsContext"] = {"publicPhotometry": [
            dict(observationDateUTC=stamp, value=value, error=0.05, band="r", units="mag",
                 system="AB", correction="uncorrected", source="synthetic contract test")
            for stamp, value in [("2026-09-18T00:00:00Z", 21), ("2026-09-19T00:00:00Z", 20)]
        ]}
        candidates = {"tns:1": item}
        registry = decisions.sync_decisions(None, None, candidates, self.provenance,
            generated_at="2026-09-20T00:00:00Z", early_opportunities=True)
        self.assertEqual(registry["decisions"][0]["status"], "pending")
        self.assertEqual(item["promotionReasons"][0]["code"], "rapid_rise")
        self.assertFalse(item["promotionReasons"][0]["automaticEligible"])
        runtime = decisions.build_runtime(None, registry, candidates, as_of_date="2026-09-20",
            generated_at="2026-09-20T00:00:00Z")
        self.assertEqual(runtime["opportunities"], [])

    def test_opt_in_score_promotion_and_owner_veto_survive_refresh(self):
        import copy
        import sys
        sys.path.insert(0, str(SCRIPT_PATH.parent))
        item = candidate()
        item["score"] = 70
        item["classification"]["kind"] = "supernova"
        candidates = {"tns:1": item}
        registry = decisions.sync_decisions(None, None, candidates, self.provenance,
            generated_at="2026-09-20T00:00:00Z", early_opportunities=True)
        self.assertEqual(registry["decisions"][0]["status"], "approved")
        self.assertEqual(item["promotionReasons"][0]["code"], "classified_score")
        for status in ("hold", "rejected"):
            veto = copy.deepcopy(registry)
            veto["decisions"][0].update(status=status, decidedBy="owner")
            changed = copy.deepcopy(item)
            changed["score"] = 99
            refreshed = decisions.sync_decisions(veto, None, {"tns:1": changed}, self.provenance,
                generated_at="2026-09-21T00:00:00Z", early_opportunities=True)
            self.assertEqual(refreshed["decisions"][0]["status"], status)
            self.assertEqual(refreshed["decisions"][0]["decidedBy"], "owner")

    def setUp(self):
        self.candidate = candidate()
        self.candidates = {"tns:1": self.candidate}
        self.provenance = {
            "tns:1": {
                "sourceReviewQueue": "transient-review-2026-09-20.json",
                "reviewSetID": "review-set-1",
                "asOfDate": "2026-09-20",
            }
        }

    def test_new_candidate_starts_pending_and_is_not_published(self):
        registry = decisions.sync_decisions(
            None,
            None,
            self.candidates,
            self.provenance,
            generated_at="2026-09-20T00:00:00Z",
        )
        runtime = decisions.build_runtime(
            None,
            registry,
            self.candidates,
            as_of_date="2026-09-20",
            generated_at="2026-09-20T00:00:00Z",
        )

        self.assertEqual(registry["decisions"][0]["status"], "pending")
        self.assertEqual(runtime["opportunities"], [])
        self.assertEqual(runtime["counts"]["pending"], 1)

    def test_approved_candidate_is_materialized_for_runtime(self):
        registry = decisions.sync_decisions(
            None,
            None,
            self.candidates,
            self.provenance,
            generated_at="2026-09-20T00:00:00Z",
        )
        decision = registry["decisions"][0]
        decision.update(
            {
                "status": "approved",
                "decidedBy": "project-owner",
                "decidedAtUTC": "2026-09-20T12:00:00Z",
            }
        )
        decisions.validate_decisions(registry)
        runtime = decisions.build_runtime(
            None,
            registry,
            self.candidates,
            as_of_date="2026-09-20",
            generated_at="2026-09-20T12:00:00Z",
        )

        self.assertEqual(len(runtime["opportunities"]), 1)
        published = runtime["opportunities"][0]
        self.assertFalse(published["reviewOnly"])
        self.assertEqual(published["review"]["status"], "approved")
        self.assertNotIn("reviewDecision", published)
        self.assertNotIn("recommendedDecision", published)

    def test_changed_evidence_resets_approval_and_withdraws_candidate(self):
        registry = decisions.sync_decisions(
            None,
            None,
            self.candidates,
            self.provenance,
            generated_at="2026-09-20T00:00:00Z",
        )
        registry["decisions"][0].update(
            {
                "status": "approved",
                "decidedBy": "project-owner",
                "decidedAtUTC": "2026-09-20T12:00:00Z",
            }
        )
        changed = candidate(magnitude=18.4)
        refreshed = decisions.sync_decisions(
            registry,
            None,
            {"tns:1": changed},
            self.provenance,
            generated_at="2026-09-21T00:00:00Z",
        )
        runtime = decisions.build_runtime(
            None,
            refreshed,
            {"tns:1": changed},
            as_of_date="2026-09-21",
            generated_at="2026-09-21T00:00:00Z",
        )

        reset = refreshed["decisions"][0]
        self.assertEqual(reset["status"], "pending")
        self.assertIn("Evidence changed", reset["note"])
        self.assertEqual(runtime["opportunities"], [])

    def test_initial_registry_preserves_legacy_runtime_approval(self):
        legacy = decisions.promote_candidate(
            self.candidate,
            {
                "decidedBy": "project-owner",
                "decidedAtUTC": "2026-09-19T12:00:00Z",
                "sourceReviewQueue": "legacy-review.json",
                "reviewSetID": "legacy-set",
                "evidenceHash": "legacy-evidence",
            },
        )
        previous_runtime = {
            "asOfDate": "2026-09-19",
            "generatedAtUTC": "2026-09-19T12:00:00Z",
            "opportunities": [legacy],
        }

        registry = decisions.sync_decisions(
            None,
            previous_runtime,
            self.candidates,
            self.provenance,
            generated_at="2026-09-20T00:00:00Z",
        )

        migrated = registry["decisions"][0]
        self.assertEqual(migrated["status"], "approved")
        self.assertEqual(migrated["evidenceHash"], decisions.evidence_hash(self.candidate))
        self.assertIn("Migrated", migrated["note"])

    def test_old_thirty_day_expiry_does_not_drop_approved_candidate(self):
        expired = candidate(expires="2026-09-19T00:00:00Z")
        registry = decisions.sync_decisions(
            None,
            None,
            {"tns:1": expired},
            self.provenance,
            generated_at="2026-09-20T00:00:00Z",
        )
        registry["decisions"][0].update(
            {
                "status": "approved",
                "decidedBy": "project-owner",
                "decidedAtUTC": "2026-09-18T12:00:00Z",
            }
        )
        runtime = decisions.build_runtime(
            None,
            registry,
            {"tns:1": expired},
            as_of_date="2026-09-20",
            generated_at="2026-09-20T00:00:00Z",
        )

        self.assertEqual(len(runtime["opportunities"]), 1)
        published = runtime["opportunities"][0]
        self.assertEqual(published["activeWindow"]["expiresAtUTC"], "2026-12-09T00:00:00Z")
        self.assertEqual(published["previousCurationWindow"]["expiresAtUTC"], "2026-09-19T00:00:00Z")
        self.assertEqual(published["discovery"], expired["discovery"])
        self.assertFalse(runtime["curationPolicy"]["visibilityPrediction"])

    def test_temporary_window_boundaries_and_pending_exclusion(self):
        registry = decisions.sync_decisions(None, None, self.candidates, self.provenance,
                                           generated_at="2026-09-20T00:00:00Z")
        decision = registry["decisions"][0]
        decision.update(status="approved", decidedBy="project-owner", decidedAtUTC="2026-09-20T00:00:00Z")
        def runtime(at):
            return decisions.build_runtime(None, registry, self.candidates,
                                           as_of_date="2026-09-20", generated_at=at)
        self.assertEqual(len(runtime("2026-09-10T00:00:00Z")["opportunities"]), 1)
        self.assertEqual(runtime("2026-09-09T23:59:59Z")["opportunities"], [])
        self.assertEqual(len(runtime("2026-12-08T23:59:59Z")["opportunities"]), 1)
        self.assertEqual(runtime("2026-12-09T00:00:00Z")["opportunities"], [])
        for status in ["pending", "hold", "rejected"]:
            decision["status"] = status
            self.assertEqual(runtime("2026-11-01T00:00:00Z")["opportunities"], [])

    def test_changed_evidence_never_falls_back_to_old_runtime(self):
        registry = decisions.sync_decisions(None, None, self.candidates, self.provenance,
                                           generated_at="2026-09-20T00:00:00Z")
        decision = registry["decisions"][0]
        decision.update(status="approved", decidedBy="project-owner", decidedAtUTC="2026-09-20T00:00:00Z")
        old = {"opportunities": [decisions.promote_candidate(self.candidate, decision)]}
        runtime = decisions.build_runtime(old, registry, {"tns:1": candidate(magnitude=18.4)},
                                          as_of_date="2026-11-01", generated_at="2026-11-01T00:00:00Z")
        self.assertEqual(runtime["opportunities"], [])

    def test_policy_preserves_watch_assessment_and_rejects_missing_anchor(self):
        watch = candidate()
        watch["urgency"] = "watch"
        registry = decisions.sync_decisions(None, None, {"tns:1": watch}, self.provenance,
                                           generated_at="2026-09-20T00:00:00Z")
        registry["decisions"][0].update(status="approved", decidedBy="project-owner",
                                       decidedAtUTC="2026-09-20T00:00:00Z")
        runtime = decisions.build_runtime(None, registry, {"tns:1": watch},
                                          as_of_date="2026-09-20", generated_at="2026-11-01T00:00:00Z")
        self.assertEqual(runtime["opportunities"][0]["urgency"], "watch")
        self.assertEqual(watch["activeWindow"]["expiresAtUTC"], "2026-10-10T00:00:00Z")
        for value in [None, "invalid"]:
            invalid = candidate()
            invalid["discovery"]["dateUTC"] = value
            self.assertFalse(decisions.apply_temporary_curation_window(invalid))

    def test_old_runtime_fallback_requires_matching_approved_review(self):
        registry = decisions.sync_decisions(None, None, self.candidates, self.provenance,
                                           generated_at="2026-09-20T00:00:00Z")
        decision = registry["decisions"][0]
        decision.update(status="approved", decidedBy="project-owner", decidedAtUTC="2026-09-20T00:00:00Z")
        old = decisions.promote_candidate(self.candidate, decision)
        def runtime():
            return decisions.build_runtime({"opportunities": [old]}, registry, {},
                                           as_of_date="2026-09-20", generated_at="2026-11-01T00:00:00Z")
        self.assertEqual(len(runtime()["opportunities"]), 1)
        old["review"]["status"] = "pending"
        self.assertEqual(runtime()["opportunities"], [])
        old["review"]["status"] = "approved"
        old["review"]["evidenceHash"] = "stale-evidence"
        self.assertEqual(runtime()["opportunities"], [])

    def test_unnamed_or_invalid_dated_approval_is_not_promoted(self):
        registry = decisions.sync_decisions(None, None, self.candidates, self.provenance,
                                           generated_at="2026-09-20T00:00:00Z")
        decision = registry["decisions"][0]
        decision.update(status="approved", decidedBy=" ", decidedAtUTC="2026-09-20T00:00:00Z")
        def runtime():
            return decisions.build_runtime(None, registry, self.candidates,
                                           as_of_date="2026-09-20", generated_at="2026-11-01T00:00:00Z")
        self.assertEqual(runtime()["opportunities"], [])
        decision.update(decidedBy="project-owner", decidedAtUTC="bad")
        self.assertEqual(runtime()["opportunities"], [])


if __name__ == "__main__":
    unittest.main()
