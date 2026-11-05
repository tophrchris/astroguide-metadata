# Early transient opportunities: local first pass (#95 / iOS #1147)

Initial base: origin/main 1d857ba plus then-unmerged PR94 d6ef88e, fast-forwarded
only in this feature worktree. PR94 branch is unchanged. No regenerated runtime,
stable package, manifest, owner registry, publication or notification in this pass.

## Local evaluation contract

`build_queue(..., early_opportunities=True)` (CLI `--early-opportunities`)
retains valid near-field candidates discovered within 90 days regardless of
discovery magnitude. Supply local historical staged inputs for backfill; this
does not fetch historic sources itself. All eligible records remain retained,
even when a caller requests a summary cap. Per-object exclusion reasons accompany
aggregate counts. The existing bounded API lookup budget is deliberately unchanged:
retention is not evidence that every object received recent photometry.

`sync_decisions(..., early_opportunities=True)` enables classified-score evaluation
in memory. Production CLI/workflows do NOT enable it. Use the read-only preview:

```sh
python3 scripts/preview_transient_early_opportunities.py LOCAL_QUEUE.json \
  --registry outputs/transients/review/transient-review-decisions-v1.json \
  --generated-at 2026-11-05T21:00:00Z
```

Preview emits JSON to stdout, not a publishable runtime package. Classified supported
types at score >=70 qualify; missing/uncertain type or unclassified score alone
does not. Owner hold/rejected statuses survive changed evidence. Invalid/catalog
warnings and contaminant warnings fail closed. Existing publication still validates
dates, current evidence and discovery-anchored PR94 expiry; score never extends expiry.

## Provisional rise policy, NOT approved for automatic decisions

Configurable `RisePolicy` defaults: 0.3 magnitude/day, >=3-sigma difference,
0.25-7 day interval, latest evidence <=3 days old. These are exploratory engineering
defaults, not owner-approved scientific thresholds. Rapid-rise reasons always have
`automaticEligible=false`, even if a caller changes the numeric values.

Compare dated finite detections with positive uncertainties, matching nonempty band,
magnitude system and correction context, magnitude units and source provenance.
Upper limits are retained but never treated as detections or used to compute slopes.
Missing system/correction metadata is not guessed. Uncertainty uses independent
measurement errors in quadrature; calibration correlations/systematic errors remain
an explicit scientific review gap. Multi-point fits, outlier/quality filtering and
approved source-specific calibration are not implemented. No future brightening is
predicted. Before/after imaging of measured change is the rationale.

TNS normalization retains every public photometry entry, including bands/errors,
dates, instruments and limits. It does not manufacture missing calibration context.
Local normalized detail files may provide that context when its provenance is known.
No new source credentials or access permissions are introduced.

Reasons include code, evidence, confidence, evidence time and stable trigger ID.
Score means eligibility, NOT an observed score-threshold crossing. Rapid-rise ID
uses the earliest qualifying pair, stable under append-only fresh refreshes; corrected
evidence intentionally changes identity. A stale pair is not an indefinitely active
trigger. No notification cooldown/state is implemented and this is not a device
notification delivery guarantee.

## Open gates

- SN2026yum and SN2026afqd require authentic dated historical source replay; current
  tests are explicitly synthetic, not evidence that either historical miss is solved.
- Independent rise *evaluation* exists; automatic rise publication remains disabled
  pending approved numeric policy, source permissions and scientific quality review.
- Backfill/current photometry scheduling and rotating lookup fairness remain work;
  the existing five-lookup API budget can still delay enrichment, not retention.
- Older genuinely renewed activity beyond 90 days needs a separate evidence-anchored
  renewal policy; no lifetime extension or perpetual active status is implemented.
- Host context remains distinct: TNS reported host versus closest catalog context.
  Separation is catalog angular proximity, not a physical-host assertion. Missing
  reported-host coordinates/separation are unknown, not inferred from catalog context.
- Producer changes are opt-in for automatic approval; production activation and
  package regeneration require a separate review. No Actions/remote operations here.

## Integration validation (2026-11-05)

Final producer code commits on `codex/95-early-transients`: `7dffae2`,
`735338c` and `398c763` (the last fixes independent evidence and backfill status).
These are local commits, not a production deployment or an approval to merge PR94.

Full suite: **192 tests passed** using
`/Volumes/AstroArchive/XcodeDerivedData/planet-pair-producer-venv/bin/python -m unittest discover -s tests`.
The earlier system-Python missing-numpy gap is resolved by the existing environment.
New contract tests exercise the actual decision sync and runtime builder, not only
the isolated evaluator: score70 at magnitude21 approves only with explicit local
opt-in; emitted score reason survives the runtime conversion; fresh reevaluation
preserves its stable ID; December expiry remains discovery-anchored, not refreshed.
Unclassified score100 with credible synthetic rise stays pending and emits no
runtime entry. Invalid/nonfinite/string/bool scores cannot approve; naive/missing
evaluation time is refused. Hold/rejected decisions survive changed evidence.
The generated classification-only hold recommendation no longer masks independent
rise evaluation; actual owner holds/rejections and catalog/contaminant/unknown
warnings remain protected. Opt-in 90-day backfill retains older candidates without
incorrectly assigning an expired-at-30-days urgency. Default production mode is
unchanged. A final focused rerun passed 41 TNS tests and 10 early-policy tests.
Full suite log: `/Volumes/AstroArchive/CodexWorktrees/early-transients/validation/metadata-full-final.log`.

Production activation is **still disabled**: the publication CLI does not pass
`early_opportunities=True`; only the stdout preview and explicit test/API callers
opt in. There is no switch that enables automatic rise decisions; every rapid-rise
reason remains `automaticEligible=false`, irrespective of configured numeric rates.
No source-acquisition/notification functionality is implied by this validation.

PR94 was rechecked OPEN/unmerged at `d6ef88e7e2f1cb478060e7ea37bc18c5d377e052`.
No checked-in decision registry, runtime source, stable package or manifest was
changed by this feature relative to that dependency. No production endpoint was
updated or asserted current. Local tests mock publication/comment operations; their
printed receipts are test output, not actual GitHub changes. Chris authorized only
Locke's separate final integrated local owner-only TestFlight, not metadata publishing.

## Merged PR94 reconciliation (2026-11-05)

This section supersedes the earlier unmerged-PR94 status. GitHub now confirms PR94
MERGED at `e440f9b3d2240d140cc2fa843fa8fc67597f4a4a`, with final PR head
`0bb456a3396bdce9ae7360fa17e2b64f84fcea31`, merged at 22:54:53 UTC.
That upstream merge was performed outside this feature work; this reconciliation
did not publish, merge a remote branch, or activate a producer policy.

Local feature branch `codex/95-early-transients` reconciles the merged baseline via
merge commit `52c7bff36fe47a5f7796c79779694f83de2bcc3e` (parents: prior feature
handoff `ac09031` and merged `origin/main` `e440f9b`). The merge was clean, with
no conflict resolutions or code rewrites. The merged PR94 commit is verified as
an ancestor of this branch. Original #95 implementation commits remain preserved.

Overlap audit:

- Upstream since the original `d6ef88e` dependency changed only review queues,
  decision/generated review artifacts, runtime, stable package and manifest.
- No overlapping changes to producer scripts or tests; those remain byte-identical
  to the feature's previous `ac09031` state after the merge.
- `git diff --exit-code origin/main HEAD -- outputs v1 sources` succeeds: inherited
  publication artifacts match the merged upstream baseline exactly. No feature
  artifact regeneration, curation action or new automatic approval was performed.
- Relative to merged main, the feature changes remain the same eight scoped code,
  test and handoff files, not generated publication data.

Post-reconciliation validation: **192 tests passed**, using the established astronomy
venv and the complete test-discovery command above. Log:
`/Volumes/AstroArchive/CodexWorktrees/early-transients/validation/metadata-post-pr94-merge.log`.

Activation boundary rechecked: `sync_decisions` defaults to
`early_opportunities=False`, and the publication CLI does not pass an opt-in.
Only the local stdout preview explicitly opts in. Rapid-rise reasons remain hard
`automaticEligible=false`; no numeric policy or notification capability was enabled.
Production #95 publishing/activation remains unauthorized. The GitHub ancestry and
checked-in artifact state were verified; no live HTTP endpoint or deployment state
is claimed here. No iOS changes were needed; the prior tested consumer handoff stands.
