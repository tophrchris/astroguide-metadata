# Target Image Assets v1

`targetImageAssets` publishes approved AstroGuide Capture Harvest imagery as a
small dynamic metadata package. It is intended for target detail/list enrichment
in DSOPlanneriOS and AstroGuide:Explore without placing metadata-host URLs in
the core catalog.

The stable manifest points to:

```text
v1/packages/target-images/target_image_assets_v1.json
```

The package lists one record per canonical catalog target ID. Each record
contains:

- `canonicalTargetID` / `catalogObjectID` for app and Explore matching
- optional `aliases` and `alternateIDs` from the existing target metadata overlay
  and Capture Harvest associated subjects
- `assetID`, `assetOwnerTargetID`, and shared-asset fields
- `variants.hero`, `variants.thumbnail320`, and `variants.thumbnail160`
- per-variant relative `path`, metadata-origin `url`, width, height, byte size,
  SHA-256, and original source package path
- source result provenance, capture date, WCS method, framing/crop geometry,
  north-up/east-left orientation metadata, and human-selection quality flags

Assets are cached under AstroGuide metadata paths:

```text
v1/assets/target-images/{assetOwnerTargetID}/{assetID}/hero.jpg
v1/assets/target-images/{assetOwnerTargetID}/{assetID}/thumbnail-320.jpg
v1/assets/target-images/{assetOwnerTargetID}/{assetID}/thumbnail-160.jpg
```

When multiple targets intentionally share the same crop, the image files are
stored once under the deterministic first manifest target for that asset. Every
target record still points at the same hosted relative paths and lists the full
`sharedWithTargetIDs` set.

Clients should treat package paths as relative to
`https://metadata.astroguide.space/`. The package also includes absolute
metadata-origin URLs for convenience, but source gallery paths are provenance
only and must not be hotlinked. If the package is absent, expired, or invalid,
clients should fall back to bundled thumbnails or hide hosted-image affordances.

Existing app builds safely ignore this unknown manifest family. Supporting
clients should validate the manifest descriptor, package envelope, record count,
asset paths, byte sizes, and SHA-256 values before using hosted images.
