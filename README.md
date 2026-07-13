# AstroGuide Metadata

This repository is the lightweight hosted metadata origin for AstroGuide.

The app always ships with bundled metadata snapshots as its offline and release-safety baseline. Files published here are optional validated override packages for small JSON metadata families such as seasonal recommendation candidates, target metadata overlays, equipment catalog metadata, comet snapshots, transient event feeds, and lunar close-pass data.

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
v1/packages/dark-sky-places/dark_sky_places_v1.json
v1/packages/comets/comet_snapshot_v1.json
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

The equipment catalog package is generated from the app's bundled smart telescope and filter catalog:

```bash
scripts/build_equipment_catalog_package.py --app-repo ../DSOPlanneriOS
```

The builder writes the equipment package envelope, refreshes the stable manifest, and recalculates byte size and SHA-256 checksum.

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

The builder writes the comet package envelope, refreshes the stable manifest, and recalculates byte size and SHA-256 checksum while preserving the other manifest packages.

## Operational Notes

Metadata changes should be reviewed through pull requests against this repository. After GitHub Pages publishes the merged branch, AstroGuide clients can silently refresh compatible packages. If the origin is unavailable or validation fails, the app continues using the bundled snapshot.
