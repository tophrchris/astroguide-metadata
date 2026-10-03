import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import process_metadata_review_comment as processor
from test_apply_tns_transient_review_decisions import candidate

decisions = processor.decisions


def comment(body=None, cid=1):
    return {"id": cid, "body": body or f"/metadata tns approve queue at {'a' * 40}",
            "created_at": "2026-10-03T15:06:26Z", "updated_at": "2026-10-03T15:06:26Z",
            "user": {**processor.ACTOR, "type": "User"},
            "html_url": f"https://github.com/{processor.REPO}/pull/80#issuecomment-{cid}",
            "issue_url": f"https://api.github.com/repos/{processor.REPO}/issues/80"}


def pr():
    return {"number": 80, "state": "open", "base": {"ref": "main", "repo": {"full_name": processor.REPO}},
            "head": {"ref": processor.BRANCH, "repo": {"full_name": processor.REPO}, "sha": "a" * 40}}


class DecisionCommentTests(unittest.TestCase):
    def setUp(self):
        self.queue = {"reviewOnly": True, "family": "transientOpportunities", "asOfDate": "2026-10-02",
                      "generatedAtUTC": "2026-10-02T00:00:00Z", "reviewSetID": "abc", "opportunities": [candidate()]}
        self.current = {"tns:1": self.queue["opportunities"][0]}
        self.registry = decisions.sync_decisions(None, None, self.current, {"tns:1": {
            "sourceReviewQueue": "transient-review-2026-10-02.json", "reviewSetID": "abc", "asOfDate": "2026-10-02"}},
            generated_at=self.queue["generatedAtUTC"])
        self.ledger = {"schemaVersion": 1, "receipts": {}}

    def apply(self, **overrides):
        args = dict(registry=self.registry, ledger=self.ledger, comment=comment(), revision="a" * 40,
                    queue_path="transient-review-2026-10-02.json", queue=self.queue,
                    selected=self.queue["opportunities"], current=self.current, status="approved")
        args.update(overrides)
        return processor.apply_tns(**args)

    def test_authorized_identity(self):
        processor.authorize(comment(), pr())

    def test_identity_needs_both_login_and_numeric_id(self):
        for field, value in (("login", "stranger"), ("id", 99), ("type", "Bot")):
            c = comment()
            c["user"][field] = value
            with self.subTest(field=field), self.assertRaises(processor.Refused):
                processor.authorize(c, pr())

    def test_wrong_pr_fork_closed_base_and_branch_rejected(self):
        for change in (lambda p: p.update(state="closed"),
                       lambda p: p["head"]["repo"].update(full_name="attacker/repo"),
                       lambda p: p["base"].update(ref="other"),
                       lambda p: p["head"].update(ref="other")):
            p = pr()
            change(p)
            with self.assertRaises(processor.Refused):
                processor.authorize(comment(), p)
        c = comment()
        c["issue_url"] += "1"
        with self.assertRaises(processor.Refused):
            processor.authorize(c, pr())

    def test_edited_comment_never_applied(self):
        c = comment()
        c["updated_at"] = "2026-10-03T16:00:00Z"
        with self.assertRaisesRegex(processor.Refused, "Edited"):
            processor.authorize(c, pr())

    def test_grammar_all_actions_named_or_queue(self):
        for action, status in processor.STATUSES.items():
            for target in ("queue", "SN2026abc", "tns:1, SN2026xyz"):
                parsed = processor.parse_command(comment(f"/metadata tns {action} {target} at {'a'*40}"), 80)
                self.assertEqual(parsed[1], status)
                self.assertEqual(parsed[2], [s.strip() for s in target.split(',')])

    def test_ambiguous_prose_short_sha_injection_duplicate_and_multiline_rejected(self):
        for body in ("approve all", "LGTM", "Approved", "please hold SN2026abc",
                     "/metadata tns approve queue at abc", f"/metadata tns approve $(touchx) at {'a'*40}",
                     f"/metadata tns approve queue,SN2026abc at {'a'*40}",
                     f"/metadata tns approve SN2026abc,SN2026abc at {'a'*40}",
                     f"/metadata tns approve queue at {'a'*40}\nreject everything"):
            with self.subTest(body=body), self.assertRaises(processor.Refused):
                processor.parse_command(comment(body), 80)

    def test_legacy_approval_exact_identity_and_five_historical_objects(self):
        c = comment(processor.LEGACY_BODY, processor.LEGACY_ID)
        parsed = processor.parse_command(c, 80)
        self.assertEqual(parsed[3], processor.LEGACY_SHA)
        q = json.loads((ROOT / "tests/fixtures/tns-comments/pr80-reviewed-five.json").read_text())
        selected = processor.select_candidates(q, parsed[2], parsed[4])
        self.assertEqual([x["sourceObjectName"] for x in selected],
                         ["AT2026adgl", "SN2026adhk", "SN2026acjs", "SN2026adgw", "AT2026adgn"])
        self.assertEqual([decisions.evidence_hash(x) for x in selected],
                         ["dcd98e4c249db33f", "479acff48c2d5d12", "1700bdcf62f281e5", "f3bb4195e24dcf17", "e75441f66884412e"])
        self.assertEqual(selected[-1]["recommendedDecision"], "hold")
        with self.assertRaises(processor.Refused):
            processor.select_candidates(self.queue, ["queue"], 5)
        for c, number in ((comment(processor.LEGACY_BODY, 2), 80), (c, 81)):
            with self.assertRaises(processor.Refused):
                processor.parse_command(c, number)

    def test_selection_missing_or_aliased_duplicates_rejected(self):
        self.assertEqual(processor.select_candidates(self.queue, ["sn2026abc"]), self.queue["opportunities"])
        for names in (["unknown"], ["tns:1", "SN2026abc"]):
            with self.assertRaises(processor.Refused):
                processor.select_candidates(self.queue, names)

    def test_changed_evidence_fails_atomically(self):
        current = copy.deepcopy(self.current)
        current["tns:1"]["discovery"]["magnitude"] = 19
        before = copy.deepcopy(self.registry)
        with self.assertRaisesRegex(processor.Refused, "Evidence changed"):
            self.apply(current=current)
        self.assertEqual(self.registry, before)
        self.assertEqual(self.ledger["receipts"], {})

    def test_missing_candidate_and_registry_hash_fail(self):
        with self.assertRaises(processor.Refused):
            self.apply(current={})
        self.registry["decisions"][0]["evidenceHash"] = "new"
        with self.assertRaises(processor.Refused):
            self.apply()

    def test_idempotency_and_edited_retry(self):
        registry, ledger, receipt, fresh = self.apply()
        self.assertTrue(fresh)
        retry = self.apply(registry=registry, ledger=ledger)
        self.assertEqual(retry, (registry, ledger, receipt, False))
        c = comment("edited")
        with self.assertRaisesRegex(processor.Refused, "edited"):
            self.apply(registry=registry, ledger=ledger, comment=c)

    def test_replay_after_refresh_never_reapproves_changed_evidence(self):
        registry, ledger, receipt, _ = self.apply()
        changed = copy.deepcopy(self.current)
        changed["tns:1"]["discovery"]["magnitude"] = 19
        provenance = {"tns:1": {"sourceReviewQueue": "next.json", "reviewSetID": "new", "asOfDate": "2026-10-03"}}
        refreshed = decisions.sync_decisions(registry, None, changed, provenance, generated_at="2026-10-03T00:00:00Z")
        result = self.apply(registry=refreshed, ledger=ledger, current=changed)
        self.assertFalse(result[3])
        self.assertEqual(result[0]["decisions"][0]["status"], "pending")
        self.assertNotIn("decisionComment", result[0]["decisions"][0])

    def test_duplicate_new_comment_records_no_status_change(self):
        registry, ledger, _, _ = self.apply()
        result = self.apply(registry=registry, ledger=ledger, comment=comment(cid=2))
        self.assertFalse(result[2]["candidates"][0]["changed"])
        self.assertEqual(len(result[1]["receipts"]), 2)

    def test_older_comment_cannot_override_newer_decision(self):
        self.registry["decisions"][0]["decidedAtUTC"] = "2026-10-03T16:00:00Z"
        with self.assertRaisesRegex(processor.Refused, "newer"):
            self.apply()

    def test_same_second_older_id_cannot_override_newer_decision(self):
        registry, ledger, _, _ = self.apply(comment=comment(cid=2))
        with self.assertRaisesRegex(processor.Refused, "newer"):
            self.apply(registry=registry, ledger=ledger, comment=comment(cid=1), status="hold")

    def test_existing_active_approval_survives_new_selection(self):
        other = copy.deepcopy(candidate())
        other["id"] = "tns:2"
        current = {**self.current, "tns:2": other}
        registry, _, _, _ = self.apply()
        entry = copy.deepcopy(registry["decisions"][0])
        entry.update(id="tns:2", evidenceHash=decisions.evidence_hash(other))
        self.registry["decisions"].append(entry)
        updated, _, _, _ = self.apply(current=current)
        runtime = decisions.build_runtime(None, updated, current, as_of_date="2026-10-02", generated_at="2026-10-03T00:00:00Z")
        self.assertEqual({x["id"] for x in runtime["opportunities"]}, {"tns:1", "tns:2"})

    def test_approve_hold_reject_feed_consistency(self):
        for status in ("approved", "hold", "rejected"):
            registry, _, _, _ = self.apply(status=status)
            runtime = decisions.build_runtime(None, registry, self.current, as_of_date="2026-10-02", generated_at="2026-10-03T00:00:00Z")
            self.assertEqual(len(runtime["opportunities"]), int(status == "approved"))
            package = processor.publish.normalize_package(runtime)
            self.assertEqual(package["opportunities"], runtime["opportunities"])

    def test_receipt_has_provenance_and_keeps_near_field_semantics(self):
        registry, _, receipt, _ = self.apply()
        self.assertEqual(receipt["actor"], processor.ACTOR)
        self.assertEqual(receipt["queueRevision"], "a" * 40)
        self.assertEqual(receipt["commentURL"], comment()["html_url"])
        self.assertEqual(receipt["createdAtUTC"], comment()["created_at"])
        self.assertEqual(len(receipt["queueSHA256"]), 64)
        promoted = decisions.promote_candidate(candidate(), registry["decisions"][0])
        self.assertEqual(promoted["relationship"]["type"], "near_field")

    def test_acknowledgment_retry_is_deduplicated(self):
        c = comment("<!-- metadata-decision:1 --> Done")
        with patch.object(processor, "pages", return_value=[c]), patch.object(processor, "api") as api:
            processor.acknowledge(80, 1, "done")
            api.assert_not_called()
        c["user"]["id"] = 99
        with patch.object(processor, "pages", return_value=[c]), patch.object(processor, "api") as api:
            processor.acknowledge(80, 1, "done")
            api.assert_called_once()

    def test_symlink_output_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "outputs").symlink_to("/tmp")
            with self.assertRaises(processor.Refused):
                processor.safe_paths(root)


class GitTransactionTests(unittest.TestCase):
    """Exercise real generation, git CAS and recovery with a local bare remote."""
    def setUp(self):
        DecisionCommentTests.setUp(self)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.remote = Path(self.temp.name) / "remote.git"
        def git(*args, cwd=None):
            return subprocess.check_output(["git", "-c", "core.hooksPath=/dev/null", *map(str, args)],
                                           cwd=cwd or self.repo, text=True, stderr=subprocess.DEVNULL).strip()
        self.git = git
        git("init", "--bare", self.remote, cwd=Path(self.temp.name))
        git("init", self.repo, cwd=Path(self.temp.name))
        git("config", "user.name", "test")
        git("config", "user.email", "test@example.invalid")
        git("remote", "add", "origin", self.remote)
        git("checkout", "-b", processor.BRANCH)
        path = self.repo / "outputs/transients/review/transient-review-2026-10-02.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(self.queue))
        manifest = self.repo / processor.publish.MANIFEST_PATH
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"packages": []}))
        git("add", ".")
        subprocess.run(["git", "commit", "-m", "fixture"], cwd=self.repo,
                       env={**__import__('os').environ, "GIT_AUTHOR_DATE": "2026-10-02T00:00:00Z",
                            "GIT_COMMITTER_DATE": "2026-10-02T00:00:00Z"}, check=True, capture_output=True)
        git("push", "origin", processor.BRANCH)
        self.sha = git("rev-parse", "HEAD")
        self.command = comment(f"/metadata tns approve queue at {self.sha}")
        self.responses = []
        self.fail_ack = False
        self.reads = 0
        self.race = False
        self.addCleanup(setattr, decisions, "REPO_ROOT", ROOT)
        self.addCleanup(setattr, processor.publish, "REPO_ROOT", ROOT)

    def api(self, path, data=None):
        if path.endswith("/pulls/80"):
            self.reads += 1
            p = pr()
            p["head"]["sha"] = self.git("rev-parse", processor.BRANCH, cwd=self.remote)
            if self.race and self.reads == 2:
                p["head"]["sha"] = "b" * 40
            return p
        if path.endswith("/issues/comments/1"):
            return self.command
        if data is not None:
            if self.fail_ack:
                raise RuntimeError("simulated response outage after successful push")
            self.responses.append(data)
            return {"id": 99}
        if "/issues/80/comments?" in path:
            return [{"body": d["body"], "user": processor.ACTOR} for d in self.responses]
        raise AssertionError(path)

    def process(self, write=True):
        with patch.object(processor, "git", side_effect=self.git), patch.object(processor, "api", side_effect=self.api):
            return processor.process(80, 1, write)

    def test_real_push_and_retry_after_ack_failure(self):
        self.fail_ack = True
        with self.assertRaisesRegex(RuntimeError, "outage"):
            self.process()
        applied = self.git("rev-parse", processor.BRANCH, cwd=self.remote)
        self.assertNotEqual(applied, self.sha)
        self.fail_ack = False
        self.process()
        self.process()
        self.assertEqual(self.git("rev-parse", processor.BRANCH, cwd=self.remote), applied)
        self.assertEqual(len(self.responses), 1)
        registry = json.loads(self.git("show", f"{applied}:{decisions.DEFAULT_DECISIONS_PATH}"))
        source = json.loads(self.git("show", f"{applied}:{decisions.DEFAULT_RUNTIME_PATH}"))
        package = json.loads(self.git("show", f"{applied}:{processor.publish.PACKAGE_PATH}"))
        manifest = json.loads(self.git("show", f"{applied}:{processor.publish.MANIFEST_PATH}"))
        self.assertEqual(registry["decisions"][0]["status"], "approved")
        self.assertEqual(processor.publish.normalize_package(source), package)
        self.assertEqual(manifest["packages"][0]["checksum"]["value"],
                         __import__('hashlib').sha256(processor.publish.json_bytes(package)).hexdigest())
        self.assertEqual(set(self.git("diff", "--name-only", self.sha, applied).splitlines()),
                         {str(p) for p in processor.FILES})

    def test_dry_run_does_not_push_or_acknowledge(self):
        self.process(False)
        self.assertEqual(self.git("rev-parse", processor.BRANCH, cwd=self.remote), self.sha)
        self.assertEqual(self.responses, [])

    def test_refresh_race_refuses_before_push(self):
        self.race = True
        with self.assertRaisesRegex(processor.Refused, "changed during"):
            self.process()
        self.assertEqual(self.git("rev-parse", processor.BRANCH, cwd=self.remote), self.sha)
        self.assertEqual(self.responses, [])

    def test_non_fast_forward_push_fails_without_receipt(self):
        original = self.git
        def raced_git(*args, cwd=None):
            if args[0] == "push":
                original("commit", "--allow-empty", "-m", "daily refresh")
                original("push", "origin", processor.BRANCH)
            return original(*args, cwd=cwd)
        self.git = raced_git
        with self.assertRaises(subprocess.CalledProcessError):
            self.process()
        current = original("rev-parse", processor.BRANCH, cwd=self.remote)
        self.assertNotEqual(current, self.sha)
        with self.assertRaises(subprocess.CalledProcessError):
            original("show", f"{current}:{processor.LEDGER}")
        self.assertEqual(self.responses, [])


class WorkflowSafetyTests(unittest.TestCase):
    def test_privileged_handler_does_not_checkout_or_execute_pr_code(self):
        workflow = (ROOT / ".github/workflows/metadata-review-comment.yml").read_text()
        self.assertIn("ref: refs/heads/main", workflow)
        self.assertNotIn("pull_request_target:", workflow)
        self.assertNotIn("comment.body", workflow)
        self.assertIn("18682191", workflow)
        self.assertNotIn("secrets.", workflow)
        processor_source = (ROOT / "scripts/process_metadata_review_comment.py").read_text()
        self.assertNotIn("shell=True", processor_source)
        self.assertNotIn("--force-with-lease", processor_source)

    def test_shared_lock_and_daily_fast_forward_push(self):
        for filename in ("metadata-review-comment.yml", "update-tns-transient-review.yml"):
            text = (ROOT / ".github/workflows" / filename).read_text()
            self.assertIn("group: update-tns-transient-review", text)
            self.assertIn("cancel-in-progress: false", text)
            self.assertNotIn("--force", text)


if __name__ == "__main__":
    unittest.main()
