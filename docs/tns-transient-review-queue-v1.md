# TNS transient opportunity review queue v1

## Purpose and boundary

The TNS transient review queue is a small, review-first pipeline for finding
recent supernova, nova, and other transient candidates in fields near
AstroGuide catalog subjects. It produces dated JSON and Markdown artifacts
under `outputs/transients/review/` for human review.

The JSON deliberately resembles a future `transientOpportunities` event
source, but it is not a published runtime package and is not listed in the
stable manifest. Approval, app publication, iOS UI, and notifications remain
separate work.

## Source contract

The builder consumes one or more TNS staged daily `.csv` or `.csv.zip` deltas.
These are change deltas, not new-object feeds. Rows are grouped by `objid`; the
record with the newest `lastmodified` timestamp wins, while every contributing
input filename, row number, and timestamp remains in provenance.

When fetching directly, the builder makes one bounded request per UTC date to:

```text
https://www.wis-tns.org/system/files/tns_public_objects/tns_public_objects_YYYYMMDD.csv.zip
```

The complete approved TNS marker must be supplied through `TNS_USER_AGENT` or
`--tns-user-agent`. Do not commit the marker. The scheduled workflow expects a
repository secret named `TNS_USER_AGENT` whose value begins with
`tns_marker{`. The iOS catalog checkout uses the existing read-only
`DSOPLANNERIOS_READ_SSH_KEY` deploy-key contract.

## Local usage

With already-downloaded staged files:

```bash
python3 scripts/build_tns_transient_review_queue.py \
  --catalog ../DSOPlanneriOS/App/Resources/Catalog/catalog.sqlite \
  --as-of 2026-09-09 \
  path/to/tns_public_objects_20260908.csv.zip \
  path/to/tns_public_objects_20260909.csv.zip
```

Or fetch a bounded seven-day window:

```bash
TNS_USER_AGENT='tns_marker{...}' \
python3 scripts/build_tns_transient_review_queue.py \
  --catalog ../DSOPlanneriOS/App/Resources/Catalog/catalog.sqlite \
  --as-of 2026-09-09 \
  --fetch-days 7
```

Validate an existing queue without fetching or rebuilding it:

```bash
python3 scripts/build_tns_transient_review_queue.py \
  --catalog ../DSOPlanneriOS/App/Resources/Catalog/catalog.sqlite \
  --validate-only outputs/transients/review/transient-review-2026-09-09.json
```

## Review policy

Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, artifacts, and
unsupported classifications are rejected before matching. The queue then:

- keeps discoveries no more than 45 days old, so days 31–45 can appear as
  explicit expired review items;
- prefers discovery age at most 30 days;
- prefers discovery magnitude at most 18.5 and retains a watch band through
  19.5;
- requires a nearest AstroGuide catalog subject within 2 degrees;
- strongly boosts separation at most 0.25 degrees, galaxy subjects, bright
  discoveries, and recognizable Messier/NGC/IC subjects.

After that broad pass, a conservative review gate retains confirmed
high-interest classifications, candidates within 0.25 degrees, and
unclassified candidates at magnitude 18.5 or brighter near catalog galaxies.
Confirmed or very close candidates in the 18.5–19.5 band remain watch-only.

Scores are deterministic policy hints, not scientific classifications.
`urgent`, `watch`, and `expired` are review states. Discovery magnitude is not
a claim about current brightness.

## Relationship terminology

`relationship.type = near_field` and the wording `near-field match` mean only
angular proximity to an AstroGuide catalog subject. They do not claim a host,
physical association, or instrument-specific field of view.

The builder uses `tns_reported_host` only when an explicit source host field
normalizes to the matched AstroGuide object's identifier, name, catalog name,
or alias. It otherwise preserves any source host text only as provenance and
keeps the relationship `near_field`.

## Automation

`update-tns-transient-review.yml` runs each Monday and Thursday and also
supports manual dispatch. It checks out the private iOS repository for the
canonical catalog, fetches up to 14 bounded daily TNS deltas, runs focused
tests and validation, and opens or updates one
`automation/tns-transient-review` pull request.

With `--skip-unchanged`, a new dated artifact is written only when the material
opportunity records differ from the latest checked-in review artifact. Input
filename/row provenance and counts alone do not create review churn;
classification, score, age/status, source modification time, or candidate-set
changes do.
