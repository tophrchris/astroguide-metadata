# TNS transient opportunity review queue v1

## Purpose and boundary

The TNS transient review queue is a small, review-first pipeline for finding
recent supernova, nova, and other transient candidates in fields near
AstroGuide catalog subjects. It produces dated JSON and Markdown artifacts
under `outputs/transients/review/` for human review.

The dated review JSON remains immutable decision-support evidence and is not
itself a runtime package. Human decisions live in
`outputs/transients/review/transient-review-decisions-v1.json`. The automation
materializes every still-active entry with status `approved` into the runtime
source, generated `transientEventFeed` package, and stable manifest in the same
pull request. Merging that pull request therefore publishes the approved set
through the normal dynamic-metadata channel. Pending, held, rejected, expired,
or stale-evidence entries are not published.

## Source contract

The builder consumes one or more TNS staged daily `.csv` or `.csv.zip` deltas.
These are change deltas, not new-object feeds. Rows are grouped by `objid`; the
record with the newest `lastmodified` timestamp wins, while every contributing
input filename, row number, and timestamp remains in provenance.

The staged records are also the bounded pre-enrichment source. They can supply
the stable TNS object ID and name, coordinates, classification type and
redshift, discovery date/magnitude/filter, reporting and discovery-source
groups, internal names, discovery and classification ADS bibcodes, creation
time, and last-modified time. Candidate filtering, AstroGuide catalog matching,
scoring, sorting, and the configured review cap are all applied from these
staged fields before any per-object API request is considered.

When fetching directly, the builder makes one bounded request per UTC date to:

```text
https://www.wis-tns.org/system/files/tns_public_objects/tns_public_objects_YYYYMMDD.csv.zip
```

An HTTP 404 for one requested date is treated as an explicit source gap: the
builder warns and continues with other available dates. Other HTTP failures,
invalid ZIP responses, and a window with no usable inputs remain fatal.

The complete approved TNS marker must be supplied through `TNS_USER_AGENT` or
`--tns-user-agent`. Do not commit the marker. The scheduled workflow expects a
repository secret named `TNS_USER_AGENT` whose value begins with
`tns_marker{`. The iOS catalog checkout uses the existing read-only
`DSOPLANNERIOS_READ_SSH_KEY` deploy-key contract.

The scheduled workflow also requires a Tailscale exit-node path so that TNS sees
a stable, approved outbound IP rather than a rotating GitHub-hosted runner IP.
The workflow joins the tailnet using `tailscale/github-action`, applies
`tag:github-actions`, selects `TS_EXIT_NODE`, and verifies that
`https://api.ipify.org` returns `TS_EXPECTED_PUBLIC_IP` before making any TNS
request. `TS_EXPECTED_PUBLIC_IP` is the exit node's public WAN IP, not its
Tailscale 100.x address, and it must match the Bot IP allowlist in TNS.

Required GitHub repository secrets for the scheduled fetch path:

- `TNS_USER_AGENT`: the approved full `tns_marker{...}` user-agent string.
- `DSOPLANNERIOS_READ_SSH_KEY`: read-only deploy key for the iOS catalog repo.
- `TS_OAUTH_CLIENT_ID`: Tailscale OAuth client ID.
- `TS_OAUTH_SECRET`: Tailscale OAuth client secret.
- `TS_EXIT_NODE`: approved exit-node machine name or Tailscale 100.x address.
- `TS_EXPECTED_PUBLIC_IP`: public IP that TNS should see after exit-node
  routing.

Detailed per-object enrichment is optional and additionally requires:

- `TNS_API_KEY`: the API key for the same TNS Bot identified by
  `TNS_USER_AGENT`.

When enabled, the builder makes one exact-name or object-ID request for each
already-ranked and capped candidate to the official TNS Get Object endpoint:

```text
https://www.wis-tns.org/api/get/object
```

The request may include public photometry and spectra so that the review record
can carry current classification/host context, the latest public photometric
detection or upper limit, and compact classification evidence. The builder
must honor the TNS response rate-limit headers and must not replace this bounded
lookup with Search API or cone-search fan-out.

Only public information is eligible for the review artifact. Normalize and
retain compact facts such as the current type, object and host redshift,
TNS-reported host, latest public photometry with date/value-or-limit/units/filter
and instrument, latest public spectrum date/instrument/source group, ADS and
certificate links, and the enrichment timestamp. Do not persist proprietary
entries, complete raw API replies, downloaded spectra, or credentials. Missing
optional source values stay explicitly unavailable rather than being inferred.

Tailnet prerequisites:

- Create or reuse `tag:github-actions`.
- Give the OAuth client writable auth-key scope and permission to issue nodes
  tagged `tag:github-actions`.
- Ensure the iMac advertises itself as an exit node and is approved in the
  Tailscale admin console.
- If the tailnet uses custom access controls, allow `tag:github-actions` to
  reach `autogroup:internet`; granting access to the exit-node machine itself
  is not sufficient for internet egress.

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

Detailed enrichment does not change the initial candidate ranking or expand
the number of TNS API calls. It supplies evidence for the human decision after
the staged-data gate has selected the bounded review list.

## Relationship terminology

`relationship.type = near_field` and the wording `near-field match` mean only
angular proximity to an AstroGuide catalog subject. They do not claim a host,
physical association, or instrument-specific field of view.

The builder uses `tns_reported_host` only when an explicit source host field
normalizes to the matched AstroGuide object's identifier, name, catalog name,
or alias. It otherwise preserves any source host text only as provenance and
keeps the relationship `near_field`.

## Review presentation and thumbnails

The review page may show an AstroGuide catalog-subject thumbnail only when the
matched target resolves to a governed record in the stable `targetImageAssets`
package documented by `docs/target-image-assets-v1.md`. Use that record's
metadata-hosted `thumbnail160` or `thumbnail320` URL and preserve its attribution
and target identity. TNS object pages can display third-party survey cutouts,
but those images are not TNS-owned review assets and must not be treated as an
AstroGuide thumbnail or hotlinked into the queue.

When no governed target image exists, omit the image URL and render an explicit
no-image fallback while retaining the target name, object type, coordinates,
and source links. A missing thumbnail must never block candidate review or be
silently replaced with an unrelated nearby image.

The page separates enrichment state from an `approve`, `hold`, or `reject`
recommendation. The generated queue keeps `reviewDecision` pending because the
dated queue is evidence, not the decision surface. Curated status lives in the
decision registry and must be one of `pending`, `approved`, `hold`, or
`rejected`. Non-pending decisions require stable `decidedBy` and
`decidedAtUTC` values.

Each decision records a candidate evidence hash. If the source evidence changes,
the workflow resets the decision to pending and requires review again. The
workflow also dismisses GitHub approvals attached to an older PR head. Before
merge, it regenerates the runtime source, stable package, and manifest from the
decision registry and validates that they agree. The merge publishes only the
still-active approved entries; PR approval alone does not change statuses,
alter iOS UI, or send notifications.

## Automation

`update-tns-transient-review.yml` runs daily and also supports manual dispatch.
It checks out the private iOS repository for the canonical catalog, fetches up
to 14 bounded daily TNS deltas, runs focused tests and validation, and opens or
updates one `automation/tns-transient-review` pull request. Scheduled runs
publish at most five review candidates; manual dispatch can override that cap.
The workflow ranks and caps candidates before optional Get Object enrichment,
so the scheduled default performs no more than five detailed TNS lookups.
An unavailable staged date is reported and skipped when another requested date
is available, while a fully unavailable window still fails closed.

With `--skip-unchanged`, a new dated artifact is written only when the material
opportunity records differ from the latest checked-in review artifact. Input
filename/row provenance and counts alone do not create review churn;
classification, score, age/status, source modification time, or candidate-set
changes do.

The workflow continues the existing review branch, merges the current metadata
`main` branch, synchronizes new candidates into the decision registry as
pending, and preserves unchanged human decisions. It then runs:

```bash
python3 scripts/apply_tns_transient_review_decisions.py
python3 scripts/publish_tns_transient_opportunities.py
python3 scripts/apply_tns_transient_review_decisions.py --check
python3 scripts/publish_tns_transient_opportunities.py --validate-only
```

To publish a candidate, edit only the canonical decision registry: set its
status to `approved`, fill `decidedBy` with a stable project alias, and record an
ISO-8601 `decidedAtUTC`. Rerun the workflow so the generated runtime/package
files and PR body reflect the decision. Merge the PR only after those generated
files are current. The existing metadata hosting path then exposes the updated
stable manifest and package to compatible AstroGuide clients on their normal
dynamic-data refresh cadence.
