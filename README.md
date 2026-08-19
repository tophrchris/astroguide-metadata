# AstroGuide Metadata

This repository is the lightweight hosted metadata origin for AstroGuide.

The app always ships with bundled metadata snapshots as its offline and release-safety baseline. Files published here are optional validated override packages for small JSON metadata families such as seasonal recommendation candidates, target metadata overlays, equipment catalog metadata, comet snapshots, transient event feeds, and lunar event data.

Large or asset-heavy payloads do not belong in this repository. In particular, this origin should not host `catalog.sqlite`, sky-brightness grid binaries, survey atlas images, or payloads that require resumable downloads or user-visible storage management.

Human-curated source inputs for generated metadata packages may live under
`sources/` when they are small enough for normal Git review. AstroGuide clients
consume only the validated runtime packages under `v1/packages`.

## Layout

```text
CNAME
v1/channels/stable/manifest.json
v1/packages/target-metadata/target_metadata_overlay_v1.json
v1/packages/target-neighborhoods/target_neighborhood_definitions_v1.json
v1/packages/equipment/equipment_catalog_v1.json
v1/packages/equipment/astrophotography_equipment_catalog_v1.json
v1/packages/equipment/astrophotography_equipment_sanitized_catalog_v1.json
v1/packages/dark-sky-places/dark_sky_places_v1.json
v1/packages/comets/comet_snapshot_v1.json
v1/packages/comet-orbit-geometry/comet_orbit_geometry_v1.json
v1/packages/planet-catalog/planet_catalog_v1.json
v1/packages/lunar-events/lunar_event_metadata_v1.json
v1/packages/lunar-events/shards/lunar_events_YYYY_MM_v1.json
v1/packages/full-moon-name-aliases/full_moon_name_alias_metadata_v1.json
v1/packages/planet-target-close-encounters/planet_target_close_encounter_metadata_v1.json
v1/packages/planet-target-close-encounters/shards/planet_target_close_encounters_YYYY_MM_v1.json
v1/packages/comet-close-encounters/comet_close_encounter_metadata_v1.json
v1/packages/comet-close-encounters/shards/comet_close_encounters_YYYY_MM_v1.json
v1/packages/seasonal-recommendations/seasonal_recommendation_candidates_north_mid_30_60n_v1.json
sources/target-metadata-overlay/2026-05-curated-workbooks/
```

The stable manifest is served at:

```text
https://metadata.astroguide.space/v1/channels/stable/manifest.json
```

Package entries include schema, family, package version, checksum, byte size, app compatibility, cache TTL, and fallback notes. The app validates package descriptors and payload envelopes before caching remote data.

## Rebuilding Target Metadata Packages

Target metadata overlay and neighborhood packages are generated from the app's bundled target metadata resources:

```bash
scripts/build_target_metadata_packages.py --app-repo ../DSOPlanneriOS
```

The builder writes the package envelopes, refreshes the stable manifest, and recalculates byte sizes and SHA-256 checksums.

## Rebuilding Equipment Catalog Packages

The equipment catalog packages are generated from the app's bundled smart
telescope/filter catalog and Telescope Workshop optics/imaging component
catalog:

```bash
scripts/build_equipment_catalog_package.py --app-repo ../DSOPlanneriOS --package all
```

The builder writes the equipment package envelopes, refreshes the stable
manifest, and recalculates byte sizes and SHA-256 checksums.

To update only the Telescope Workshop optics/imaging package, use:

```bash
scripts/build_equipment_catalog_package.py --app-repo ../DSOPlanneriOS --package astrophotography
```

The app consumes the raw Telescope Workshop package above and applies the
bundled curation rules at runtime. A second sanitized projection is available
for other consumers, review tools, and web experiences that need the same rows
the app renders without re-implementing the app's filtering logic:

```bash
scripts/build_equipment_catalog_package.py --app-repo ../DSOPlanneriOS --package astrophotography-sanitized
```

## Rebuilding Planet Catalog Packages

The planet catalog package is generated from the app's bundled dynamic metadata snapshot:

```bash
scripts/build_planet_catalog_package.py --app-repo ../DSOPlanneriOS
```

The builder writes the planet catalog package envelope, refreshes the stable manifest, and recalculates byte size and SHA-256 checksum.

## Rebuilding Lunar Event Packages

The lunar event metadata package is generated from the app's bundled catalog SQLite database plus Skyfield/JPL ephemerides:

```bash
python3 -m venv /tmp/astroguide-lunar-events-venv
/tmp/astroguide-lunar-events-venv/bin/python -m pip install -r scripts/requirements-lunar-events.txt
/tmp/astroguide-lunar-events-venv/bin/python scripts/build_lunar_event_package.py \
  --app-repo ../DSOPlanneriOS \
  --start-date 2026-08-05T00:00:00Z \
  --end-date 2028-08-05T00:00:00Z
```

The payload uses the `lunarEvents` dynamic metadata family. The manifest points
at a compact JSON index, and the index points at monthly compact JSON event
shards so clients can fetch only the visible timeline range. This is optimized
for the Lunar Mode default of the next 30 days rather than forcing a two-year
decode up front.

The DSO close-encounter candidate set is intentionally presentation-focused:
curated target metadata and curated seasonal recommendation rows, named target
neighborhood showcase IDs, Messier targets, and NGC/IC targets with known
magnitude at or brighter than 10.0. Unknown-magnitude back-catalog targets are
excluded unless they are explicitly covered by those curated/showcase sources.

Event shards remain compact JSON instead of CSV. CSV is thinner for a flattened
export, but these lunar events carry nested subject, Moon, eclipse, and timing
details that map cleanly to Codable-style app models and leave room for schema
evolution without parallel sidecar files or embedded JSON columns. The monthly
compact JSON shards are small enough for lightweight dynamic fetch and decode.

The package includes Moon close encounters with filtered catalog DSOs and major
planets, lunar eclipses, and lunar phase markers. It intentionally does not
publish supermoon or micromoon labels or booleans; app clients should derive
those dynamically from full-moon distance or apparent diameter only for rows
they display.

## Rebuilding Full Moon Name/Alias Packages

The `fullMoonNameAliases` catalog is generated from a small, reviewed source
file in this repository. It provides 12 UTC Gregorian-month entries, a fixed
North American Popular primary name, and source-attributed aliases from the
mixed-provenance popular alternatives, English / Medieval, and Modern Pagan
libraries:

```bash
python3 scripts/build_full_moon_name_alias_package.py
python3 scripts/build_full_moon_name_alias_package.py --validate-only
```

The package contains names and provenance only. Clients calculate the
New-Moon-to-New-Moon cycle, contained Full Moon, phase events, seasonal labels,
distance categories, eclipses, close encounters, and observer-specific
circumstances at runtime. Duplicate alias text is collapsed for display while
independent library/source claims remain attached.

The package contract, source caveats, and app-consumer boundary are documented
in [`docs/full-moon-name-aliases-v1.md`](docs/full-moon-name-aliases-v1.md).

## Rebuilding Planet/Target Close-Encounter Packages

The `planetTargetCloseEncounters` package is generated from the same catalog,
target canonicalization, presentation-focused candidate filter, Skyfield/JPL
ephemeris dependency, and monthly shard philosophy as `lunarEvents`:

```bash
/tmp/astroguide-lunar-events-venv/bin/python \
  scripts/build_planet_target_close_encounter_package.py \
  --app-repo ../DSOPlanneriOS
```

By default the generator publishes the next 24 months of global/geocentric
closest approaches for Mercury through Neptune at a maximum separation of 5
degrees. It does not include comets or meteor showers. Site, nighttime,
altitude, horizon/obstruction, and observability filtering remain app-side.

The index and shard schema, event-ID convention, candidate-filter rationale,
and DSOPlanneriOS integration boundary are documented in
[`docs/planet-target-close-encounters-v1.md`](docs/planet-target-close-encounters-v1.md).

## Rebuilding Comet Orbit Geometry Packages

The `cometOrbitGeometry` package wraps the bundled comet orbit/trajectory
geometry contract in a hosted metadata envelope, separate from `cometSnapshot`:

```bash
scripts/build_comet_orbit_geometry_package.py --app-repo ../DSOPlanneriOS
scripts/build_comet_orbit_geometry_package.py --validate-only
```

The package preserves the comet snapshot stable IDs, coordinate/sample frame
metadata, rendering kind, heliocentric path samples, dated heliocentric samples,
and anti-solar tail model metadata. Long-period, non-periodic, hyperbolic,
parabolic, or poorly closed objects remain `trajectoryArc` records.

The package contract is documented in
[`docs/comet-orbit-geometry-v1.md`](docs/comet-orbit-geometry-v1.md).

## Rebuilding Comet Close-Encounter Packages

The `cometCloseEncounters` package publishes comet close encounters using the
systematic Dynamic to Static and Dynamic to Dynamic models: comet snapshot
ephemeris streams against static AstroGuide catalog target groups, plus
Skyfield/JPL Moon and major-planet positions.

```bash
/tmp/astroguide-comet-events-venv/bin/python \
  scripts/build_comet_close_encounter_package.py \
  --app-repo ../DSOPlanneriOS

/tmp/astroguide-comet-events-venv/bin/python \
  scripts/build_comet_close_encounter_package.py --validate-only
```

The generated `2026-08-11` package contains 298 true-UTC closest-approach events
across 12 monthly shards: 247 Comet to DSO events and 51 Comet to Moon/major
planet events. It intentionally does not generate DSO to DSO events.

The package contract is documented in
[`docs/comet-close-encounters-v1.md`](docs/comet-close-encounters-v1.md).

## Rebuilding Comet Snapshot Packages

The comet snapshot package can be generated from the app's bundled comet seed and ephemeris resources:

```bash
scripts/build_comet_snapshot_package.py --app-repo ../DSOPlanneriOS
```

It can also publish a generated `cometSnapshot` package from the AstroActive comet/lunar close-pass experiment:

```bash
scripts/build_comet_snapshot_package.py \
  --source-package /Volumes/AstroActive/nsns_experiments/comet_lunar_close_passes_2026/outputs/comet_snapshot_next365_cobs_horizons_20_package.json
```

Aerith's weekly comet pages can be normalized as a small review/source snapshot
and then used to enrich the hosted comet package with near-real-time magnitude
updates:

```bash
scripts/build_aerith_comet_source.py \
  --output sources/comets/aerith_current_comets_v1.json

scripts/build_comet_snapshot_package.py \
  --source-package /Volumes/AstroActive/nsns_experiments/comet_lunar_close_passes_2026/outputs/comet_snapshot_next365_cobs_horizons_20_package.json \
  --aerith-source sources/comets/aerith_current_comets_v1.json \
  --apply-aerith-magnitudes \
  --package-version comet-snapshot-v1-YYYY-MM-DD-cobs-horizons-20-aerith
```

Aerith permission was received from Seiichi Yoshida on 2026-08-15 for the
requested AstroGuide use: comet designation/name, Aerith detail-page URL,
current and next-week magnitude estimates, and small cached copies of selected
weekly comet thumbnail/images. Aerith should be credited where shown, with links
back to the relevant detail page.

Do not hotlink Aerith images from app clients. The comet snapshot package keeps
Aerith image URLs as source references only. Publish approved image copies and
per-comet brightness/commentary payloads through the lazy comet detail package:

```bash
scripts/build_comet_detail_metadata_package.py \
  --source-package v1/packages/comets/comet_snapshot_v1.json \
  --aerith-source sources/comets/aerith_current_comets_v1.json \
  --orbit-geometry v1/packages/comet-orbit-geometry/comet_orbit_geometry_v1.json \
  --image-limit 50 \
  --package-version comet-detail-metadata-v1-YYYYMMDD-aerith

scripts/build_comet_detail_metadata_package.py --validate-only
```

The builder writes the comet package envelope, per-comet shards, cached Aerith
image assets, and stable-manifest descriptor while preserving other manifest
packages. The detail index carries list-friendly summaries for visibility
state, brightness trend/range, orbital classification, and ephemeris windows;
full brightness/commentary/media payloads remain in lazy per-comet shards.

## Refreshing Aerith Comet Detail Metadata

Aerith comet detail metadata is refreshed by a scheduled GitHub Actions workflow
every Monday. The workflow can also be run manually from the Actions tab. It
fetches Aerith's weekly bright-comet pages, compares the normalized source data
against the checked-in snapshot, and opens or updates an `automation/aerith-comet-metadata`
pull request only when the comet data materially changes.

The local equivalent is:

```bash
scripts/update_aerith_comet_metadata.py
scripts/build_comet_detail_metadata_package.py --validate-only
python -m unittest tests/test_aerith_comet_source.py tests/test_comet_detail_metadata_package.py
```

The automation preserves the permission and attribution requirements documented
for Aerith: cached image assets are served from AstroGuide metadata, not
hotlinked, and the generated metadata retains Aerith / Seiichi Yoshida credit
plus the relevant Aerith detail-page URLs.

## Operational Notes

Metadata changes should be reviewed through pull requests against this repository. After GitHub Pages publishes the merged branch, AstroGuide clients can silently refresh compatible packages. If the origin is unavailable or validation fails, the app continues using the bundled snapshot.
