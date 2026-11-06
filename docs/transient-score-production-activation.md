# Classified-score production activation (#95 / iOS #1147)

## Authorized scope and provenance

Chris authorized production score approval, a scoped metadata PR merge, and actual
hosted verification on November 6, 2026. Rapid-rise approval, new notifications,
Actions dispatch/testing, and iOS/website/schema changes remain out of scope.

Dedicated branch: `codex/95-transient-score-production`, based on merged main
`e440f9b3d2240d140cc2fa843fa8fc67597f4a4a` (PR94). Latest PR96 review branch
`530021d4b691d0f8aac2ffc87246da813209c318` was fast-forwarded into this branch
before generating any decisions. Its registry and November 5 review were retained,
not replaced by the older #95 preview registry. Historical review JSON/Markdown
is byte-identical to PR96. No TNS credentials were present in this local process;
there was no new source fetch or invented photometry. Retained evidence is dated,
not a claim of live photometry or future brightening.

## Active rule

`--auto-approve-classified-score` activates `tns-classified-score-v1`. A supported,
explicit, non-uncertain type consistent with its kind and score >=70 is eligible.
Unclassified events cannot qualify by score alone. There is no absolute magnitude
cutoff. Finite coordinates, consistent TNS identity/URL, valid catalog context,
dated evidence and the discovery-anchored 90-day listing window are required.
Contaminant/unsupported types, inconsistent authoritative classification context,
catalog identity warnings, source holds/rejections and warnings fail closed.

Owner `hold` / `rejected` decisions survive evidence changes, even when an actor
alias was not changed with the status. Their original evidence hash is retained.
Changed approvals require fresh rule validation, not grandfathered approval of
changed science. Every retained candidate gets an auditable evaluation. Automatic
approval uses `astroguide:classified-score-policy-v1`, not a human identity.
Reason metadata records policy, score, classification, source/review provenance,
evidence hash/time, first eligibility time and stable trigger ID. Score eligibility
is explicitly not an observed threshold crossing or brightness prediction.

Runtime generation rechecks automatic eligibility and current evidence. Missing
current candidates, altered evidence/proof, expired windows or injected rapid-rise
reasons cannot materialize automatic approvals. General publication safety also
withholds unsafe historical approvals without rewriting the owner's decision.
Rapid-rise evaluation is not wired into this production implementation at all;
its approval and notifications remain explicitly disabled in the published policy.

Policy activation persists in the registry so authenticated owner decision handling
does not silently turn it off. The daily workflow explicitly passes activation and
check flags. It retains all 90-day near-field candidates without a discovery-magnitude
gate; a requested summary limit never truncates retention or evaluation.

## Candidate publication

- Version: `transient-event-feed-v1-20261106T223559Z-classified-score-v1`.
- Evaluation/generation time: `2026-11-06T22:35:59Z`; latest review as-of November 5.
- 74 registry entries reevaluated; 23 new automatic approvals.
- 40 active published entries: 23 automatic and 17 retained owner approvals.
- 32 pending entries. No actual registry owner hold/rejected entries existed in
  this snapshot; synthetic tests verify both vetoes remain protected. Eleven
  candidates have source/catalog-warning exclusions from automatic eligibility.
- Two previously approved entries are withheld: one expired and SN2026aars
  (`tns:219464`), whose catalog ID IC 1803 is labeled NGC 3910 in the retained
  source. Its historical owner approval remains in the registry, not republished
  as safe catalog context. No catalog repair or identity conflation was attempted.
- SN2026ahvu (`tns:224706`, SN Ia, score100) is automatically approved. Discovery
  `2026-11-02T04:20:36Z`; expiry `2027-01-31T04:20:36Z`. Supporting review:
  `transient-review-2026-11-05.json`; evidence hash `80705f0a94be7137`.
- Package: 151700 bytes; SHA256
  `20c182f210b53595c21d5be9757c3d2472e67bdc1031c80e5943afc0a857e07c`.
- Local manifest SHA256:
  `68e5015bcdb3302e8a9af93b17edc71bb00faea498fc68ae5060f2840dd7a8ab`.
- Every non-transient descriptor is unchanged from main. No image/website/iOS
  files or historical review facts are modified.

## Local validation and future schedule

Full local suite: 189 tests passed, including real CLI/check idempotence, threshold
edges, unknown/uncertain classes, invalid dates/coordinates/identity, contaminants,
source/catalog warnings, protected owner decisions, changed evidence, immutable
trigger IDs and disabled rapid-rise materialization. Tests also guard explicit
workflow activation flags and unlimited retention. Existing automation workflow
guards pass; workflow YAML parses successfully. All five generated artifacts are
byte-identical on repeat generation at a fixed evaluation time. Both production
`--check` and publisher `--validate-only` pass. No hosted Actions test run was used.

The existing daily schedule remains 13:17 UTC. It fetches the configured permitted
staged deltas, retains/evaluates all candidates, and places approved eligible results
in the automation review PR. The existing bounded Get Object lookup budget remains
five; no new photometry acquisition or backfill guarantee is implied. Future review
PRs still require merge to publish; this change does not introduce automatic PR
merges or alerts. This activation is published through the separately authorized
scoped PR merge and existing main-branch legacy Pages hosting.

Commits use `[skip ci]` to avoid the existing pull-request Actions test trigger.
No workflow dispatch, CI label or PR comment decision command is used. Publication
is not complete until canonical hosted manifest and package bytes/checksums match
the candidate and SN2026ahvu is observed in that hosted package. Verification evidence
is retained under `/Volumes/AstroArchive/CodexWorktrees/transient-score-production/validation/`.

## Publication and watch-recommendation follow-up

Initial activation PR97 merged as `9f8e11605902dfdee59139f33208881b8046c711`
(source `e0177d5b003cca369012ee877d7833485c1fba25`). Its 40-entry package and
canonical manifest were verified byte-for-byte on the host, including SN2026ahvu.
Final pipeline review then identified a distinction that needed a follow-up:
the queue's generated `watch` recommendation uses `hold`, which must not veto an
otherwise eligible classified score merely because discovery magnitude is faint.

A reasonless generated watch hold is now distinct from an owner's registry hold
or an explicit detail-source hold. Explicit detail holds are always marked with
a reason; owner holds/rejections and catalog/contaminant/unknown warnings remain
protected. A regression test passes magnitude21 through the actual recommendation
helper and explicit detail-hold merge path. Counts remain unchanged for the current
74-record snapshot; this removes the unintended cutoff for future eligible objects.
First eligibility times and stable trigger IDs survive this repeat evaluation.
The candidate hashes/version above are for this follow-up publication.
