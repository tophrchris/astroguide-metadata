# AstroGuide Metadata

This repository is the lightweight hosted metadata origin for AstroGuide.

The app always ships with bundled metadata snapshots as its offline and release-safety baseline. Files published here are optional validated override packages for small JSON metadata families such as seasonal recommendation candidates, target metadata overlays, equipment catalog metadata, comet snapshots, transient event feeds, and lunar close-pass data.

Large or asset-heavy payloads do not belong in this repository. In particular, this origin should not host `catalog.sqlite`, sky-brightness grid binaries, survey atlas images, or payloads that require resumable downloads or user-visible storage management.

## Layout

```text
CNAME
v1/channels/stable/manifest.json
v1/packages/seasonal-recommendations/seasonal_recommendation_candidates_north_mid_30_60n_v1.json
```

The stable manifest is served at:

```text
https://metadata.astroguide.space/v1/channels/stable/manifest.json
```

Package entries include schema, family, package version, checksum, byte size, app compatibility, cache TTL, and fallback notes. The app validates package descriptors and payload envelopes before caching remote data.

## Operational Notes

Metadata changes should be reviewed through pull requests against this repository. After GitHub Pages publishes the merged branch, AstroGuide clients can silently refresh compatible packages. If the origin is unavailable or validation fails, the app continues using the bundled snapshot.
