# Early transient opportunities: local first pass (#95 / iOS #1147)

Base: current origin/main 1d857ba plus unmerged PR94 d6ef88e, fast-forwarded
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
