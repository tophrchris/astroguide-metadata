# PR-comment candidate decisions

TNS review PRs accept candidate decisions from **tophrchris**, verified against both
GitHub login and immutable user ID **18682191**. The processor re-fetches the comment
and PR through authenticated GitHub API calls. PR reviews/approvals are not candidate
decisions. No command merges a PR, publishes to main, or sends device notifications.

## Commands

Review the dated JSON/Markdown dossier at a specific PR commit, then copy its full
40-character commit SHA into a new issue comment on the review PR:

```text
/metadata tns approve queue at FULL_40_CHARACTER_SHA
/metadata tns hold SN2026adhk at FULL_40_CHARACTER_SHA
/metadata tns reject AT2026adgl, AT2026adgn at FULL_40_CHARACTER_SHA
```

Replace the SHA placeholder; it is not a literal command argument. `queue` selects
exactly the candidates in the latest dated dossier **at that revision**, not every
historical registry entry and not a newly refreshed queue. Names are case-insensitive
exact `sourceObjectName`/`shortTitle` values or IDs such as `tns:221314`. Comma-separated
names are supported. Aliased duplicates, missing names, abbreviated SHAs, multiple
commands, and ambiguous prose receive clarification without changing decisions.
Only `approve`, `hold`, and `reject` are supported. A curator may deliberately override
a recommendation (including a catalog identity warning); the underlying warning and
near-field-only relationship are preserved. A catalog match is not a confirmed host.

The full SHA must belong to the same-repository `automation/tns-transient-review`
branch targeting `main`. Every selected candidate must still have exactly the reviewed
evidence hash in the latest consolidated evidence and synchronized registry. Validation
is all-or-nothing. Older commands cannot override later decisions. Changed evidence
resets status to pending under the existing synchronization rules and removes its
active `decisionComment` reference; the immutable receipt remains as historical audit.

## Publication and audit

The existing decision and package builders remain authoritative. The command commits
only the registry and its Markdown summary, runtime source, stable transient package,
stable manifest, and `outputs/transients/decisions/comment-receipts-v1.json`.
Every still-active approved entry is generated, not just the selected queue. Pending,
hold, and rejected entries are excluded. Unrelated stable manifest descriptors are
preserved. Merging the review PR is the publication gate.

Each receipt records comment ID/URL, actor ID/login, original and updated timestamps,
comment fingerprint, full reviewed commit, dated queue path, review-set ID, full queue
SHA256, per-candidate evidence hashes and previous statuses. Each decision has a
compatible additive `decisionComment` field; no runtime schema change is required.

## Activation and permissions

Merge the implementation PR to install the `issue_comment` workflow on `main`.
GitHub Actions must be enabled and repository policy must permit its `GITHUB_TOKEN`
to write contents and PR comments. No new secret, private iOS catalog access, TNS API
access, phone credential, or PAT is needed. The existing daily review workflow also
has a decision-only manual replay path; this path skips all TNS/catalog/network jobs.

The issue-comment workflow executes **only main's trusted scripts**. PR trees supply
JSON data in an isolated temporary worktree, never executable code. Symlinked inputs
and outputs are refused, git hooks are disabled, subprocess calls use argument arrays,
and comment text is never interpolated into shell. Forks and other branches are refused.
Read-only PR tests have no persisted checkout credentials. A manual workflow dispatch
executes the operator-selected ref; only dispatch a reviewed, trusted implementation
ref. It is not an escape hatch for running untrusted PR code.

## Retries, edits, races, and recovery

- Commands are immutable: any edited comment is refused, including edits before its
  first run. Post a new command. Editing or deleting an already applied comment does
  not revoke its committed decision; use a new hold/reject command.
- The receipt is committed atomically with generated outputs. Re-running the same
  comment performs no new decision or commit, even if a refresh has since reset its
  approval. If the push succeeded but acknowledgment failed, replay repairs the missing
  acknowledgment. A marker prevents duplicate acknowledgments on normal retries.
- A newly posted identical command gets its own receipt, with `changed: false` when
  its target already has that status. The latest explicit actor/time remains auditable.
- Both workflows share `update-tns-transient-review` concurrency with cancellation of
  running jobs disabled. GitHub can replace a *pending* run when another enters the
  same concurrency group; operators must replay a command that has no receipt or
  acknowledgment after the running refresh completes. The ledger, not workflow arrival,
  is the source of truth for successful processing.
- Before writing, the processor re-reads the comment and PR state. All branch pushes
  are normal fast-forward pushes, including the daily refresh. A competing update
  rejects the push instead of overwriting decisions. Retry re-fetches and revalidates
  evidence; changed evidence requires a new reviewed command. No automatic force push.
- A failed generation, authentication/API call, or git push does not post a success
  acknowledgment. A refusal explains what needs review; transport failures are visible
  in the Actions log. A temporary worktree is removed after processing. No main ref
  is changed. A network failure after successful push is recovered by receipt lookup.

Manual replay after the workflow is on main:

```sh
gh workflow run update-tns-transient-review.yml \
  --repo tophrchris/astroguide-metadata --ref main \
  -f decision_pr=80 -f decision_comment_id=5970403109
```

Local trusted-code preflight (uses normal authenticated `gh`; dry run is default):

```sh
python3 scripts/process_metadata_review_comment.py --pr 80 --comment-id 5970403109
# Add --write only when applying the command and posting its acknowledgment is intended.
```

Older comments do not automatically receive an `issue_comment` event when this workflow
is installed. Explicitly replay them. General old prose is not inferred from current PR
body text. The one migration exception is PR #80's exact unedited comment
[5970403109](https://github.com/tophrchris/astroguide-metadata/pull/80#issuecomment-5970403109):

> I'm ok to APPROVE all 5 items in the review queue, and deploy them as live metadata for app consumption

It is bound to `4866f46f8a726f55fec17b2af2c09b0a30548abe`, latest dated queue
`transient-review-2026-10-02.json`, review set `299f555bcd8c85d0`. Authenticated inspection
found this commit at 2026-10-03 14:39:13 UTC, the successful daily workflow completed at
14:41:00 UTC, and the unedited approval followed at 15:06:26 UTC. PR timeline inspection
found no subsequent commit or force-push event before processing. The fixture pins the
five candidates and their evidence hashes; refreshed evidence must pass the same checks.

| Object | Candidate | Reviewed evidence hash |
| --- | --- | --- |
| AT2026adgl | tns:221314 | dcd98e4c249db33f |
| SN2026adhk | tns:221339 | 479acff48c2d5d12 |
| SN2026acjs | tns:220685 | 1700bdcf62f281e5 |
| SN2026adgw | tns:221325 | f3bb4195e24dcf17 |
| AT2026adgn | tns:221316 | e75441f66884412e |

AT2026adgn's recommendation was hold due to the IC 1419 / NGC 1198 catalog identity
conflict. The explicit approval of all five overrides the recommendation; it does not
resolve that conflict. All five associations remain near-field context.

## Extension point and validation

`ADAPTERS` separates family decision semantics from authenticated GitHub transport and
command parsing. Only TNS is enabled. Another family needs its own evidence validator,
materializer, allowed branch/paths, and tests; never load adapters from PR code.

Run standard-library tests:

```sh
python3 -m unittest discover -s tests -p 'test_metadata_review_comment.py'
python3 -m unittest discover -s tests -p 'test_*tns*.py'
python3 -m unittest discover -s tests -p 'test_automation_workflow_guards.py'
```

Tests include the historical five, identity/fork checks, strict parsing, changed evidence,
immutable edits, duplicate/replayed commands, real local git transactions, a competing
push, acknowledgment recovery after a successful push, and package/manifest consistency.
Local tests are distinct from a successful hosted decision-only workflow run.
