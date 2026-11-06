import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import apply_tns_transient_review_decisions as policy

NOW = "2026-11-06T17:00:00Z"


def candidate():
    return dict(id="tns:synthetic", source="TNS", sourceId="synthetic",
                sourceObjectName="Synthetic policy test", sourceURL="https://www.wis-tns.org/object/synthetic",
                eventType="transientOpportunity", reviewOnly=True, urgency="watch", recommendedDecision="approve",
                reviewDecision="pending", score=70,
                classification=dict(kind="supernova", type="SN Ia"),
                coordinates=dict(raDegrees=10.0, decDegrees=-20.0),
                discovery=dict(dateUTC="2026-11-02T00:00:00Z", magnitude=21.0),
                activeWindow=dict(startsAtUTC="2026-11-02T00:00:00Z", expiresAtUTC="2026-12-02T00:00:00Z"),
                astroGuideObject=dict(id="NGC1"), angularSeparationDegrees=0.1,
                lastModifiedUTC="2026-11-05T00:00:00Z")


class ProductionScorePolicyTests(unittest.TestCase):
    def sync(self, item, registry=None, enabled=True):
        self.candidates = {item["id"]: item}
        provenance = {item["id"]: dict(sourceReviewQueue="synthetic.json", reviewSetID="synthetic", asOfDate="2026-11-05")}
        return policy.sync_decisions(registry, None, self.candidates, provenance,
                                     generated_at=NOW, auto_approve_classified_score=enabled)

    def runtime(self, registry):
        return policy.build_runtime(None, registry, self.candidates, as_of_date="2026-11-05", generated_at=NOW)

    def test_flag_threshold_and_no_brightness_cutoff(self):
        self.assertEqual(self.sync(candidate(), enabled=False)["decisions"][0]["status"], "pending")
        for score, expected in [(69, "pending"), (70, "approved"), (100, "approved")]:
            item = candidate(); item["score"] = score
            registry = self.sync(item)
            self.assertEqual(registry["decisions"][0]["status"], expected)
            self.assertEqual(len(self.runtime(registry)["opportunities"]), int(expected == "approved"))
        approved = self.runtime(registry)["opportunities"][0]
        self.assertEqual(approved["review"]["approvedBy"], policy.AUTOMATED_ACTOR)
        self.assertEqual(approved["promotionReasons"][0]["code"], "classified_score")
        self.assertFalse(registry["automaticApprovalPolicy"]["rapidRiseEnabled"])
        self.assertFalse(registry["automaticApprovalPolicy"]["notificationsEnabled"])

    def test_unknown_uncertain_mismatched_types_never_pass_score(self):
        for kind, value in [("transient_candidate", None), ("supernova", "SN Ia?"),
                            ("supernova", "SN candidate"), ("nova", "SN Ia"), ("supernova", "AGN")]:
            item = candidate(); item["score"] = 100
            item["classification"] = dict(kind=kind, type=value)
            item["tnsContext"] = {"publicPhotometry": [{"value": 20}, {"value": 18}]}
            registry = self.sync(item)
            self.assertEqual(registry["decisions"][0]["status"], "pending")
            self.assertEqual(self.runtime(registry)["opportunities"], [])

    def test_supported_classes(self):
        for kind, value in [("supernova", "SN II"), ("superluminous_supernova", "SLSN-I"),
                            ("nova", "Nova"), ("tidal_disruption_event", "TDE-featureless")]:
            item = candidate(); item["classification"] = dict(kind=kind, type=value)
            self.assertEqual(self.sync(item)["decisions"][0]["status"], "approved")

    def test_invalid_and_warning_evidence_fail_closed(self):
        mutations = [dict(score="100"), dict(score=True), dict(score=float("inf")),
                     dict(coordinates=dict(raDegrees=360, decDegrees=0)),
                     dict(discovery=dict(dateUTC="2026-08-08T00:00:00Z")),
                     dict(discovery=dict(dateUTC="2026-11-07T00:00:00Z")),
                     dict(discovery=dict(dateUTC="2026-11-02")),
                     dict(lastModifiedUTC="2026-11-07T00:00:00Z"),
                     dict(astroGuideObject=dict(id="NGC1", identityWarning="conflict")),
                     dict(sourceURL="https://example.com/forged"),
                     dict(sourceId="mismatched"),
                     dict(tnsContext=dict(remarks=["Possible variable star contaminant"])),
                     dict(tnsContext=dict(currentType="SN II")),
                     dict(recommendedDecision="hold", decisionReason="Explicit detail hold")]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                item = candidate(); item.update(mutation)
                self.assertEqual(self.sync(item)["decisions"][0]["status"], "pending")

    def test_owner_veto_survives_evidence_change_even_if_actor_alias_not_edited(self):
        for status in ("hold", "rejected"):
            item = candidate(); registry = self.sync(item)
            registry["decisions"][0]["status"] = status
            original_hash = registry["decisions"][0]["evidenceHash"]
            item["score"] = 99
            refreshed = self.sync(item, registry)
            self.assertEqual(refreshed["decisions"][0]["status"], status)
            self.assertEqual(refreshed["decisions"][0]["ownerDecisionEvidenceHash"], original_hash)
            self.assertEqual(self.runtime(refreshed)["opportunities"], [])

    def test_refresh_stable_and_changed_invalid_evidence_withdrawn(self):
        item = candidate(); first = self.sync(item)
        second = self.sync(copy.deepcopy(item), first)
        self.assertEqual(first, second)
        self.assertEqual(first, self.sync(copy.deepcopy(item), first, enabled=False))
        self.assertEqual(first["decisions"][0]["promotionReasons"], second["decisions"][0]["promotionReasons"])
        item["score"] = 80
        refreshed = self.sync(item, second)
        self.assertEqual(refreshed["decisions"][0]["promotionReasons"][0]["stableTriggerID"], first["decisions"][0]["promotionReasons"][0]["stableTriggerID"])
        item["classification"] = dict(kind="contaminant", type="CV")
        self.assertEqual(self.sync(item, refreshed)["decisions"][0]["status"], "pending")

    def test_runtime_revalidates_current_evidence_and_rejects_rapid_reason(self):
        item = candidate(); registry = self.sync(item)
        item["score"] = 1
        self.assertEqual(self.runtime(registry)["opportunities"], [])
        item["score"] = 70
        registry["decisions"][0]["promotionReasons"][0]["code"] = "rapid_rise"
        self.assertEqual(self.runtime(registry)["opportunities"], [])
        self.candidates = {}
        self.assertEqual(self.runtime(registry)["opportunities"], [])

    def test_historical_owner_approval_cannot_publish_a_catalog_warning(self):
        item = candidate(); registry = self.sync(item)
        decision = registry["decisions"][0]
        decision["decidedBy"] = "project-owner"
        item["astroGuideObject"]["identityWarning"] = "identity conflict"
        decision["evidenceHash"] = policy.evidence_hash(item)
        runtime = self.runtime(registry)
        self.assertEqual(runtime["opportunities"], [])
        self.assertIn("source_or_catalog_warning", runtime["publicationExclusions"][0]["reasons"])
        self.assertEqual(decision["status"], "approved")

    def test_cli_and_check_are_idempotent_and_workflow_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "transient-review-2026-11-05.json").write_text(json.dumps(dict(
                schemaVersion=1, reviewOnly=True, family="transientOpportunities", asOfDate="2026-11-05",
                generatedAtUTC=NOW, reviewSetID="synthetic", opportunities=[candidate()])))
            outputs = [root / "decisions.json", root / "decisions.md", root / "runtime.json"]
            command = [sys.executable, str(ROOT / "scripts/apply_tns_transient_review_decisions.py"),
                       "--review-dir", directory, "--decisions", str(outputs[0]), "--decisions-markdown", str(outputs[1]),
                       "--runtime", str(outputs[2]), "--auto-approve-classified-score", "--generated-at", NOW]
            subprocess.run(command, check=True, capture_output=True)
            before = [hashlib.sha256(path.read_bytes()).hexdigest() for path in outputs]
            subprocess.run(command, check=True, capture_output=True)
            subprocess.run(command + ["--check"], check=True, capture_output=True)
            self.assertEqual(before, [hashlib.sha256(path.read_bytes()).hexdigest() for path in outputs])
        workflow = (ROOT / ".github/workflows/update-tns-transient-review.yml").read_text()
        self.assertIn("--auto-approve-classified-score --generated-at", workflow)
        self.assertIn("--auto-approve-classified-score --check", workflow)
        self.assertIn("--early-opportunities", workflow)
        self.assertIn("inputs.max_candidates || '0'", workflow)
        self.assertNotIn("at most five candidates", workflow)


    def test_generated_watch_is_not_an_owner_or_explicit_source_hold(self):
        import build_tns_transient_review_queue as queue
        item = candidate()
        item["recommendedDecision"] = queue.recommended_decision("watch")
        self.assertEqual(item["recommendedDecision"], "hold")
        self.assertEqual(self.sync(item)["decisions"][0]["status"], "approved")
        queue.merge_tns_detail(item, {"recommendedDecision": "hold"}, retrieved_at=NOW,
                               source_kind="synthetic_explicit_hold")
        self.assertEqual(item["decisionReason"], "Hold explicitly requested by TNS detail review.")
        self.assertEqual(self.sync(item)["decisions"][0]["status"], "pending")


if __name__ == "__main__":
    unittest.main()
