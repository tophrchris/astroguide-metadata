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


if __name__ == "__main__":
    unittest.main()
