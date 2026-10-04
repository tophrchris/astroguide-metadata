# HH Companion v1

Local implementation for metadata #84 and iOS #1135. HHs remain contextual
features of existing DSOs; no new planning targets, canonical parquet edits,
stable-manifest entries, workflows or hosted datasets.

## Build and Validate

Python 3.11+; use a virtual environment and the pinned dependencies:

```bash
python3 -m venv /tmp/astroguide-hh-venv
/tmp/astroguide-hh-venv/bin/pip install -r scripts/requirements-hh.txt
RESEARCH="$HOME/Library/Mobile Documents/com~apple~CloudDocs/VS Code Projects/Deep Space Catalog Building/analysis/hh_coverage_20261004"
CATALOG="$HOME/codex sandbox/DSOPlanneriOS/App/Resources/Catalog/catalog.sqlite"
/tmp/astroguide-hh-venv/bin/python scripts/build_hh_packages.py \
  --research "$RESEARCH" --catalog "$CATALOG"
/tmp/astroguide-hh-venv/bin/python scripts/build_hh_packages.py \
  --validate outputs/hh/review
/tmp/astroguide-hh-venv/bin/python -m unittest discover -s tests -v
HH_RESEARCH="$RESEARCH" HH_CATALOG="$CATALOG" \
  /tmp/astroguide-hh-venv/bin/python -m unittest discover -s tests -p 'test_hh_packages.py' -v
```

Default output is ignored `outputs/hh/review/`, never hosted `v1/`.
Generation is deterministic: sorted compact JSON, fixed source retrieval dates,
no wall-clock timestamps. Independent `--enrichment-version`/`--media-version`
options version optional families without changing core. Descriptor hashes,
bytes, versions, schema, joins, permissions and limits are checked on readback.

`sources/hh/input-pins.json` pins the catalog version/hash, audited identity map
hash, and independently retrieved SIMBAD/V104 hashes. Changing a pin is an
explicit reviewed dataset migration, not a silent refresh. No credential is
required to use the supplied local evidence. The repository does not contain
raw external exports; a fresh machine needs the pinned staged exports and DSO
map (or a reviewed regenerated snapshot/pin). SHA failures fail closed.

Core-only independent rebuild without even reading V104:

```bash
/tmp/astroguide-hh-venv/bin/python scripts/build_hh_packages.py \
  --research "$RESEARCH" --catalog "$CATALOG" --exclude-source V104 \
  --output /tmp/hh-core-review --audit-output /tmp/hh-core-audit.json
```

`--exclude-source` is repeatable and prevents reading excluded core sources;
optional fields/assets from the excluded source are removed too. Exclude
SIMBAD and V104 to exercise complete core withdrawal. `Chen2026` is never
read even if not explicitly excluded. Core-only consumers can simply omit
the optional files. A replacement core removing a withdrawn source must replace
the cache atomically; do not merge withdrawn records back from older snapshots.

## Identity and Geometry

Parent IDs use normalized HH numbers or SIMBAD OIDs for unnumbered records.
Component IDs use immutable source OIDs, never positions or array indexes.
All numbered components count once under their parent. Main-type non-HH SIMBAD
entries are not accepted as HHs; conflicting aliases/types from the independent
named export remain flagged with their divergent type in `classifications`.
Ambiguous cross-number aliases are quarantined. Historical V104 entries, when
locally audited, remain historical classifications rather than being silently
reclassified. A source-listed HH is not independent spectroscopic confirmation.

Select a located parent first, then located SIMBAD before historical V104,
then natural designation order. If no parent position exists, explicitly use
`representative_component_proxy`. Keep all alternatives/provenance; do not
average knots or imply a physical system centroid. Unlocated groups are reported
but ineligible; components with unknown positions may accompany an eligible parent.

Astropy transforms V104 FK4/B1950 to ICRS; SIMBAD positions are ICRS. Unknown
epoch, uncertainty and precision remain null. A converted equinox is not an
observation epoch. No artificial precision/uncertainty is inferred from CSV digits.

Eligibility uses the MAIN portrait S30 Pro 2.24 x 3.99 degree PA0 gnomonic
rectangle with inclusive 1e-12 tangent tolerance. Tests independently compare
Astropy sky-offset projections and cover RA wrap, polar fields, back hemisphere,
corners and boundaries. Static membership is spatial containment, not physical
association/detectability or visibility in selected Capture Studio framing.

The research identity map uses unique SIMBAD IDs, then reciprocal aliases
within 1 arcminute for unresolved rows without conflicting resolved IDs.
Its pinned representative is the single count center for every alias member.
Aliases with conflicting centers do not union footprints or increase counts;
offsets over 1 arcminute are separately reported. Missing representative
coordinates mean unknown/null, never zero. Rebuilding identity policy requires
re-review of those offsets and a new map pin; the builder does not re-resolve
remote identities during an offline build.

## Source and Rights Matrix

Review date: 2026-10-04. Decisions are limited to factual/core versus optional
fields below; third-party material is not blanket-relicensed.

| Field | Candidate Source | Decision / Evidence |
| --- | --- | --- |
| Parent/component IDs, aliases | SIMBAD independent CSV | Included factual fields; [official service page](https://simbad.cds.unistra.fr/simbad/) explicitly specifies ODbL |
| RA/Dec, source object type | SIMBAD | Included with retrieval/hash and source classification; same ODbL basis |
| Observation epoch, uncertainty, precision | Source CSV has no values | Null; do not invent |
| Historical coordinates/type | V104 | Local audit only; [ReadMe](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/V/104?format=html) gives FK4/B1950/citation, but exact dataset license unresolved |
| V104 notes, distance, exciting source | V104 | Withheld independently of positional audit; no note copying |
| All compilation fields, figures, prose | Chen & Wu 2026 | Withheld; no granted permission; NC/ND reported in handoff is not paid-app/adaptation clearance |
| Original short HH24 prose | ESA/Hubble caption | Two-sentence editorial paraphrase with source/credit/CC-BY-4.0; no paper text |
| Original short HH212 prose | ESO POTW | Editorial paraphrase with source/credit/CC-BY-4.0; no paper text |
| Distances/methods/cloud attribution | No curated verified evidence | Omitted; schema permits measured/adopted/inferred with units/range/method |
| Driving stars/confidence/alternatives | No curated verified evidence | Omitted; schema distinguishes candidates/confirmed |
| HH24 dedicated media | ESA/Hubble heic1526a | Found, identity/resolution/reuse terms checked; full asset credit |
| HH24 regional survey view | ESA/Hubble heic1526b | Found/reusable under that archive's terms; contextual, emission not verified |
| HH212 dedicated media | ESO potw1541a | Found, identity/resolution/reuse terms checked; full asset credit |
| Arbitrary survey cutouts or scientific figures | Not checked | Not imported; Aladin/ESA/ESO access is not blanket permission for other archives |

Authoritative optional-material terms: [ESA/Hubble](https://esahubble.org/copyright/)
and [ESO](https://www.eso.org/public/outreach/copyright/). Individual image pages
and full credits are in `sources/hh/media-candidates.json`. No raw images copied.
Source pages, not binary URLs, are exported; downstream hero asset preparation
and visual crop QA are separate work. No hero should be shown without a usable
prepared asset, full visible credit, source/license link and appropriate crop.

SIMBAD core is a separate ODbL-derived companion database. Generated core embeds
license URI/source notices; stage also contains `NOTICE.md`. Follow
[ODbL](https://opendatacommons.org/licenses/odbl/1-0/) attribution, share-alike,
machine-readable access and distribution-measures obligations before public
app use. No permission to publish is inferred by this local generator. The
app feature can be paid while database rights remain open. Keep app code,
canonical DSO catalog and independently licensed optional materials separate.
Legal/product review and authorized access/notice delivery remain release gates.

## Counts and Scope Loss

Machine-readable exact integer histograms, sums, pins, examples, source exclusions,
center conflicts and omitted-parent worklist: `reports/hh/latest.json`.

| Population | Covered Parents | Identity Pairs | Hit DSO Identities |
| --- | ---: | ---: | ---: |
| Independent SIMBAD+V104, no Chen (local audit) | 1249 | 17739 | 1325 |
| SIMBAD-only rights-filtered stage | 1206 | 17211 | 1272 |

Both use 6410 deduplicated DSO identities: 6305 located / 105 unknown; all 7622
app rows receive alias-aware links. Delivery has 1392 input parent groups:
1266 located (60 uncovered) / 126 unlocated, and 2889 eligible parent+component
records. Without V104, some remaining parents use a different component center,
so do not subtract historical selected-center counts to predict eligibility.
The actual recomputation loses 43 groups, 528 pairs and 53 hit DSO identities.
`scopeLoss.independentGroupsOmitted` is the exact replacement/omission worklist;
restore only with independently sourced identity/coordinate/rights evidence.

Compared with the initial full exploratory union, the handoff reported another
44 covered groups requiring Chen-only position replacement/omission (one of 45
had a component alternative). That is a reported research result, not a new
permission decision or the current runtime census. Those positions and original
reference snippets are not imported. The functioning baseline accepts the loss.

Sample counts (audit / delivery): NGC7000 38/38, IC5070 16/16, IC5067 11/11,
NGC281 0/0, M8 11/11, M20 11/11, M42 255/249, M78 27/26, NGC1333 132/131,
IC348 19/18. M8/M20 share overlapping frames; counts do not imply association.

## Hero Feasibility

Bounded audit of the checked-in official archive inventory, not exhaustive web
coverage. Every eligible parent is accounted for in `runtimeHeroAudit`; no-image
IDs mean no verified asset in this inventory, not that no image exists anywhere.

| Category | Found HHs | Reusable HHs | Deduplicated Assets |
| --- | ---: | ---: | ---: |
| Dedicated | 2 | 2 | 2 |
| Regional, HH emission identified | 0 | 0 | 0 |
| Survey context/cutout | 1 | 1 | 1 |

Union: 2/1206 deliverable HHs have found and verified reusable references,
3 assets, 1204 have no verified inventory asset. Dedicated and survey overlap
for HH24, so do not sum group numerators. Audit-only independent population:
2/1249 with references, 1247 without. Source pages establish identity,
dimensions and credits; actual prepared/downloaded crops are not visually
verified or distributed. Survey context explicitly does not claim detected HH.

## Consumer and Offline Contract

See `HANDOFF-HH.md` for exact envelope/record keys and limits. This is NOT a new
family silently inserted into the existing stable channel. Proposed local
resource delivery must be agreed with iOS first. Bundle compatible reviewed core
with the matching catalog. Validate schema/checksum/size/version/catalog pin
before accepting a complete override; swap atomically. Last good compatible
core and bundled fallback work offline; stale optional joins are ignored.
Unknown attributes have no placeholder scientific value, and no media means no
hero. Do not make network enrichment block the count/list/detail flows.

Examples (schematic, not full schema-valid packages):

```json
{"targetID":"NGC281","identityID":"NGC281","status":"located","hhIDs":[]}
```

```json
{"targetID":"missing-position","identityID":"missing-position","status":"unknown","hhIDs":null}
```

```json
{"schemaVersion":1,"packageVersion":"core-only-example","records":[]}
```

The last example is a valid absent enrichment or media envelope. Full synthetic
core-only packages are generated by `fixture_packages()` in the HH tests,
including aliases/components/null positions; no third-party material needed.

## Remaining Gates

- V104 exact license or independent replacement positions: unresolved, safely omitted.
- Chen & Wu permission: not granted, safely omitted; no request sent here.
- Broad enrichment and exhaustive image discovery: not claimed; optional baseline is intentionally sparse.
- Prepared hero binary/crop verification and iOS consumption: separate ownership.
- ODbL access/notices and commercial distribution compliance: verify before authorized release.
- Publication/PR/deployment: not authorized or performed. Canonical parquet remains unchanged.
