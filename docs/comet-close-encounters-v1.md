# Comet Close Encounters v1

The `cometCloseEncounters` package family publishes global, geocentric
closest-approach events between curated AstroGuide comets and static catalog
DSO target groups.

This is the first comet close-call proof point for the systematic event model:

- Dynamic to Static: generated for Comet to DSO.
- Dynamic to Dynamic: scaffolded in the package metadata but not generated in
  this PR.
- DSO to DSO: intentionally not generated because static catalog targets do
  not move relative to each other.

## Package Shape

The stable manifest references a compact index package:

```text
v1/packages/comet-close-encounters/comet_close_encounter_metadata_v1.json
```

The index references checksummed monthly compact-JSON shards:

```text
v1/packages/comet-close-encounters/shards/comet_close_encounters_YYYY_MM_v1.json
```

The generated `2026-08-11` package covers:

- window: `2026-08-11T00:00:00Z` through `2027-07-12T00:00:00Z`
- source comet streams: 20
- candidate DSO target groups: 617
- events: 247
- monthly shards: 12
- event target groups: 179

## Event Shape

```json
{
  "id": "comet-target-close-encounter-COMET-10P-M45-20260812",
  "eventFamily": "closeEncounter",
  "type": "cometTargetCloseEncounter",
  "eventTimeUTC": "2026-08-12T04:05:06Z",
  "closestApproachUTC": "2026-08-12T04:05:06Z",
  "minimumSeparationDegrees": 1.25,
  "participants": [
    {
      "kind": "comet",
      "id": "COMET:10P",
      "designation": "10P",
      "displayName": "10P/Tempel",
      "magnitude": 13.2,
      "coordinate": {
        "rightAscensionHours": 3.2,
        "declinationDegrees": 24.1
      }
    },
    {
      "kind": "deepSkyObject",
      "id": "M45",
      "catalogID": "M45",
      "displayName": "Pleiades",
      "objectType": "Open_cluster",
      "magnitude": 1.6,
      "coordinate": {
        "rightAscensionHours": 3.783333,
        "declinationDegrees": 24.1167
      }
    }
  ]
}
```

Event IDs use the stable comet ID, canonical target-group ID, and UTC
closest-approach date. Event timestamps are true UTC closest-approach instants.
The app is responsible for local night-of grouping.

## Generation Policy

The generator exposes policy knobs for:

- maximum angular separation
- optional comet magnitude limit
- optional target magnitude limit
- DSO target subset through the same presentation-focused lunar/planet target
  filter
- ranking cap per comet
- monthly UTC shard range
- source sample cadence and refinement cadence

The default package uses all 20 comet snapshot streams, including faint curated
objects. Site-specific nighttime, altitude, horizon/obstruction, and
observability filters remain app-side.

## Source And Accuracy

Comet positions are interpolated from the deterministic `cometSnapshot`
geocentric RA/Dec/magnitude samples. Static DSO positions come from the
AstroGuide catalog target groups. The package source metadata records the
comet snapshot package version/checksum, catalog SHA-256, target metadata paths,
coordinate frames, and algorithm description.

This v1 package is planning metadata. It is not a replacement for on-demand JPL
Horizons queries when sub-sample precision is required.

## Dynamic To Dynamic Gap

The index includes a `generationModel.dynamicDynamic` scaffold marked
`scaffoldedNotGenerated`. A future generator should pair comet streams with
Moon/planet streams over a shared UTC range, apply the same policy model, and
emit the same standardized close-encounter shape with both participants dynamic.

## Rebuild And Validation

```bash
/tmp/astroguide-comet-events-venv/bin/python \
  scripts/build_comet_close_encounter_package.py \
  --app-repo ../DSOPlanneriOS \
  --start-date 2026-08-11T00:00:00Z \
  --end-date 2027-07-12T00:00:00Z \
  --generated-at 2026-08-11T00:00:00Z

/tmp/astroguide-comet-events-venv/bin/python \
  scripts/build_comet_close_encounter_package.py --validate-only
```

The builder validates index/shard schema, sorted events, stable IDs, participant
coordinates, thresholds, per-shard checksums, byte sizes, and stable manifest
linkage.

## iOS Boundary

Existing app builds ignore this unknown manifest family. DSOPlanneriOS follow-up
should add family registration, bundled fallback/sync support, index and shard
decoding, TimelineEvent close-encounter mapping, local observability filtering,
and comet-detail presentation.
