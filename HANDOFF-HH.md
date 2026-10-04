# HH Consumer Contract v1

Metadata worktree: `/Users/chollander/codex sandbox/astroguide-metadata-hh`.
Branch: `codex/hh-metadata`. Owner: metadata #84 only.

Contract: three physically separate JSON envelopes, `hh-core-v1`,
`hh-enrichment-v1`, `hh-media-v1`; each has `schemaVersion: 1`,
`packageVersion`, and `records`. Core additionally has `catalog`, `footprint`,
and `dsoLinks`. Companion manifest descriptors include SHA-256 and byte size.
No stable-channel registration or hosted publication is part of this work.

Core record keys: `id`, `parentID` (null for parents), `name`, `aliases`,
`kind` (`parent`/`component`), `classification`, `position`, `provenance`.
Numbered parent ID: `hh:1`; components: `hh:1:component:simbad-<oid>`.
Unnumbered IDs: `hh:simbad:<oid>`. Never derive IDs from coordinates.
Position is ICRS/J2000 RA/Dec degrees with `role`, nullable `epoch`,
`uncertaintyArcsec`, and `precisionArcsec`. Proxy positions are explicit.
Source classifications remain source-specific; conflicting types are flagged.

`dsoLinks`: `targetID` (app primary identifier), `identityID`, `hhIDs`
(unique parent IDs), `status` (`located`/`unknown`). Unknown coordinates yield
null `hhIDs`, not an empty list. Alias members share one audited representative
center; links are spatial containment, not physical association/detectability.
Catalog SHA/version and identity-map SHA are mandatory pins.

Static eligibility: S30 Pro MAIN portrait 2.24 x 3.99 degrees, PA0,
gnomonic rectangle, inclusive boundary (1e-12 tangent-space tolerance), one reference center per parent.
Capture Studio must reproject positions using actual selected framing; static
eligibility/counts are not selected-frame visibility.

Enrichment records join on `id` only and contain nullable source-attributed
`fields`; media records join on `id`, describe `role`, rights, credits and
source URL. Missing enrichment/media means no enhanced details/hero, not error.
No permission-dependent prose/images are bundled. An empty core is valid when
all sources are withheld; do not substitute research data into a release.

Offline baseline: bundle reviewed core + matching catalog as release resources;
never require network at startup. Retain last validated compatible core override,
fall back to bundle on malformed/hash/version/size failure. Optional families
are independently removable; stale joins are ignored. Proposed limits: 8 MiB
core, 2 MiB enrichment, 1 MiB media, 20000 records, 8000 DSO links; no binaries.
An empty baseline supports graceful absence but does not fulfill useful coverage.
Consumer implementation must validate before use, not trust manifest labels.

## Delivered Local Stage

Generator: `scripts/build_hh_packages.py`; schemas/rights/pins/curation:
`sources/hh/`; tests: `tests/test_hh_packages.py`. Runbook and source/rights
matrix: `docs/hh-companion-v1.md`. Audit: `reports/hh/latest.json`.
Generated packages (ignored by Git, not published):
`/Users/chollander/codex sandbox/astroguide-metadata-hh/outputs/hh/review/`.
Use `hh-core-v1.json` as the proposed reviewed offline resource, not a DSO catalog.
This local artifact exists and validates; bundling in iOS is the iOS owner's work.

Core stage: 1206 covered parents / 2889 total parent+component records,
17211 identity-level pairs, 1272 hit DSO identities of 6305 located; 105 unknown.
Core approximately 4.45 MB; optional enrichment 2 records; media 3 asset records
for HH24/HH212. Image metadata only, no binaries. Media URLs identify source pages,
not runtime image-byte URLs; no automatic remote hero loading is promised.
Details must handle omitted distances/exciting sources and no image gracefully.

SIMBAD's official service page explicitly specifies ODbL. Core carries
`databaseLicense`, `databaseLicenseURL`, `sourceNotices`, with `NOTICE.md`.
Paid feature gating does NOT change the open database license. Before public
app use: make the derived companion/complete alteration material freely
available as required, retain attribution/license notices and comply with
ODbL distribution restrictions. No publication or iOS license UI integration
was authorized/performed here. Keep canonical catalog and app code separate.

V104 remains unresolved and is omitted from the deliverable; Chen2026 is never
read. Independent no-Chen audit reproduces 1249 groups / 17739 pairs / 1325 hit
DSOs. Excluding V104 additionally loses 43 groups, 528 pairs and 53 hit identities;
IDs/worklist are in audit `scopeLoss`. No fabricated replacements or grants.
The baseline is useful without those sources; their restoration is a separate
rights/independent-coordinate task, not a blocker for the current local pipeline.

Hero audit: bounded official archive inventory, 2/1206 groups found and reusable,
3 deduplicated assets (2 dedicated, 1 survey-context); 1204 no verified asset in
that inventory. This is not an exhaustive all-web absence claim. Survey imagery
is positional context, not a detected HH. Display full visible asset credit and
license/source links; significant alterations must be identified.

Local validation: full repository suite 194 tests passed (including all local
integration tests); focused HH suite 28 passed. Schema/checksum/byte-limit
readback passed. Core-only rebuild with V104 fully excluded has byte-identical
core and manifest versus default rights-filtered generation. Complete source
withdrawal tested without calling either reader. Canonical parquet and app
SQLite SHA-256 still match the original research pins. No PR/push/Actions,
publishing, iOS build, deployment or release performed.
