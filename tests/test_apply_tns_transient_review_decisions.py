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

    def test_expired_approved_candidate_is_not_published(self):
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

        self.assertEqual(runtime["opportunities"], [])
        self.assertEqual(runtime["counts"]["expiredApproved"], 1)


if __name__ == "__main__":
    unittest.main()
