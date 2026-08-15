# Comet Detail Metadata v1

`cometDetailMetadata` is a lazy, per-comet dynamic metadata family for source-backed detail-screen enrichment. It is intentionally separate from `cometSnapshot` so app startup and comet search do not load image/history payloads globally.

The stable manifest points to a compact index:

```text
v1/packages/comet-details/comet_detail_metadata_v1.json
```

The index lists matched comets and shard descriptors. Each shard contains one comet record with:

- AstroGuide stable comet ID, designation, display name, and Aerith name
- Aerith detail-page URL and attribution/source fields
- optional cached AstroGuide metadata asset references for thumbnail/hero imagery
- brightness points for the detail graph, including reported or weekly-estimate magnitude, qualifier, source URL, optional source commentary, optional generated interpretation, magnitude delta, and significance flags

Images must be cached under AstroGuide metadata paths such as:

```text
v1/assets/comets/aerith/
```

App clients should never hotlink Aerith image URLs. When imagery, source commentary, or interpretation is shown, credit Aerith / Seiichi Yoshida and link to the relevant Aerith detail page when available.

Existing app builds safely ignore this unknown manifest family. DSOPlanneriOS builds that support it should lazy-load only the opened comet's shard and hide Aerith detail affordances when the package is absent, expired, or invalid.
