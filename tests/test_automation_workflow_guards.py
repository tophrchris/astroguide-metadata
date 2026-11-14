"""Static regression guards for workflow failures before metadata generation.

Keep these checks standard-library-only, like the metadata workflow test suites.
YAML syntax validation is a separate check.
"""

import re
import unittest
from pathlib import Path


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github" / "workflows"


def workflow_steps(filename):
    text = (WORKFLOWS / filename).read_text(encoding="utf-8")
    # These workflows have one job and named steps at this indentation.
    parts = re.split(r"^      - name: ", text, flags=re.MULTILINE)
    return parts[0], [part.split("\n", 1) for part in parts[1:]]


class AutomationWorkflowGuardsTests(unittest.TestCase):
    def test_aerith_job_does_not_use_runner_context(self):
        header, _ = workflow_steps("update-aerith-comet-metadata.yml")
        self.assertNotRegex(header, r"\$\{\{[^}]*\brunner\.")

    def test_aerith_summary_producer_and_consumer_share_runner_temp_path(self):
        _, steps = workflow_steps("update-aerith-comet-metadata.yml")
        steps = dict(steps)
        path = '"$RUNNER_TEMP/aerith-pr-summary.md"'
        self.assertIn(
            "--output " + path, steps["Summarize reviewer-facing changes"]
        )
        self.assertIn(
            "cat " + path + ' >> "$body"', steps["Open or update pull request"]
        )

    def test_tns_identity_is_configured_before_review_branch_merge(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        merge_index = next(
            i for i, (_, body) in enumerate(steps)
            if "git merge --no-edit origin/main" in body
        )
        identity_steps = [
            (i, body) for i, (_, body) in enumerate(steps)
            if 'git config user.name "github-actions[bot]"' in body
            and 'git config user.email '
            '"41898282+github-actions[bot]@users.noreply.github.com"' in body
        ]
        self.assertEqual(len(identity_steps), 1)
        identity_index, identity_body = identity_steps[0]
        self.assertLess(identity_index, merge_index)
        checkout_index = next(
            i for i, (_, body) in enumerate(steps)
            if "uses: actions/checkout@" in body
            and "path: astroguide-metadata" in body
        )
        self.assertLess(checkout_index, identity_index)
        for body in (identity_body, steps[merge_index][1]):
            self.assertIn("working-directory: astroguide-metadata\n", body)
        self.assertNotRegex(identity_body, r"(?m)^\s*if[: ]")

    def test_tns_latest_review_fallback_excludes_decisions_registry(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        steps = dict(steps)
        build_step = steps["Build review queue from staged TNS deltas"]
        self.assertIn(
            "-name 'transient-review-????-??-??.json'",
            build_step,
        )
        self.assertNotIn("-name 'transient-review-*.json'", build_step)

    def test_tns_review_branch_reconciliation_handles_only_generated_manifest(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        steps = dict(steps)
        reconcile = steps["Continue the existing review branch when present"]
        self.assertIn(
            'git merge-base --is-ancestor "origin/$BRANCH_NAME" origin/main',
            reconcile,
        )
        self.assertIn(
            "mapfile -t conflicts < <(git diff --name-only --diff-filter=U)",
            reconcile,
        )
        self.assertIn(
            '[[ "${conflicts[0]}" == "v1/channels/stable/manifest.json" ]]',
            reconcile,
        )
        self.assertIn(
            "git checkout --theirs -- v1/channels/stable/manifest.json",
            reconcile,
        )
        self.assertIn("git commit --no-edit", reconcile)
        self.assertIn("git merge --abort", reconcile)

    def test_tns_reconciled_branch_is_pushed_without_new_queue_changes(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        steps = dict(steps)
        publish = steps["Open or update review pull request"]
        commit_position = publish.index('if [[ "$has_changes" == true ]]')
        push_position = publish.index('git push origin "$BRANCH_NAME"')
        closing_position = publish.index("fi", commit_position)
        self.assertGreater(push_position, closing_position)
        self.assertIn(
            'remote_head="$(git rev-parse --verify "origin/$BRANCH_NAME"',
            publish,
        )

    def test_tns_pr_body_enforces_total_github_size_budget(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        publish = dict(steps)["Open or update review pull request"]
        self.assertIn("body_limit=60000", publish)
        self.assertIn("append_markdown_section", publish)
        self.assertIn('if (( body_bytes > body_limit )); then', publish)
        self.assertIn("Decision registry summary", publish)
        self.assertIn("Latest review dossier", publish)

    def test_tns_existing_unpublished_branch_can_recreate_missing_pr(self):
        _, steps = workflow_steps("update-tns-transient-review.yml")
        publish = dict(steps)["Open or update review pull request"]
        self.assertIn('git diff --quiet origin/main...HEAD', publish)
        self.assertIn('branch_has_diff=true', publish)
        self.assertIn(
            'elif [[ "$has_changes" == true || "$branch_has_diff" == true ]]',
            publish,
        )


if __name__ == "__main__":
    unittest.main()
