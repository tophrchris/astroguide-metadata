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
- `visibilityState` / `visibilitySummary` for list-row copy: `current`, `comingSoon`, `futureVisible`, `notCurrentlyUseful`, or `unknown`
- `brightnessChart` with up to the latest 90 days of available Aerith reported/weekly estimate points, plus the true available start/end date and point count
- `brightnessTrend` with current magnitude, comparison magnitude/date/window, signed delta, direction (`brightening`, `fading`, `stable`, or `uncertain`), and notable-change markers
- brightness points for the detail graph, including reported or weekly-estimate magnitude, projection marker, qualifier, source URL, optional source commentary, optional generated interpretation, magnitude delta, and significance flags
- `classification` with stable enum-like `orbitalFamily`, `inclinationClass`, and `returnStatus` values
- `ephemerisSummary` with cometSnapshot validity dates, source package version, useful-magnitude window, and enough date fields for clients to calculate nights remaining or visible-again copy without scraping Aerith

Classification values are intentionally conservative:

- `orbitalFamily`: `jupiter_family`, `halley_type`, `long_period`, `oort_cloud`, `main_belt`, `interstellar`, `unknown`
- `inclinationClass`: `low_inclination`, `moderate_inclination`, `high_inclination`, `retrograde`, `unknown`
- `returnStatus`: `returning`, `first_observed_return`, `dynamically_new`, `non_periodic_or_uncertain`, `unknown`

When an orbital fact is missing or ambiguous, generators must emit `unknown`
or the closest documented uncertain value rather than omitting the field.

Images must be cached under AstroGuide metadata paths such as:

```text
v1/assets/comets/aerith/
```

App clients should never hotlink Aerith image URLs. When imagery, source commentary, or interpretation is shown, credit Aerith / Seiichi Yoshida and link to the relevant Aerith detail page when available.

Cached media records expose both the app-safe AstroGuide metadata URL/path and
the original Aerith image URL for provenance. App UI must load only `url` /
`cachedURL` under `metadata.astroguide.space`, while attribution and outbound
links should use `aerithDetailURL` / `sourceURL`.

Existing app builds safely ignore this unknown manifest family. DSOPlanneriOS builds that support it should lazy-load only the opened comet's shard and hide Aerith detail affordances when the package is absent, expired, or invalid.
