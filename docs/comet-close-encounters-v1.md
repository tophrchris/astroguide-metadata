# Comet Close Encounters v1

The `cometCloseEncounters` package family publishes global, geocentric
closest-approach events between curated AstroGuide comets, static catalog DSO
target groups, and generated Moon/major-planet positions.

This is the first comet close-call proof point for the systematic event model:

- Dynamic to Static: generated for Comet to DSO.
- Dynamic to Dynamic: generated for Comet to Moon and Comet to major planet.
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
- events: 298
- Comet to DSO events: 247
- Comet to Moon/major-planet events: 51
- monthly shards: 12
- event target groups: 179
- solar system body events: Moon 38, Mercury 7, Venus 2, Mars 2, Saturn 1,
  Uranus 1

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

Dynamic-dynamic events use the same event envelope, with the comet first and a
Moon or major-planet participant second:

```json
{
  "id": "comet-dynamic-close-encounter-COMET-65P-saturn-20270212",
  "eventFamily": "closeEncounter",
  "type": "cometDynamicCloseEncounter",
  "eventTimeUTC": "2027-02-12T03:06:37Z",
  "closestApproachUTC": "2027-02-12T03:06:37Z",
  "minimumSeparationDegrees": 2.8535,
  "participants": [
    {
      "kind": "comet",
      "id": "COMET:65P",
      "designation": "65P",
      "displayName": "65P/Gunn",
      "magnitude": 18.73,
      "coordinate": {
        "rightAscensionHours": 0.827756,
        "declinationDegrees": -0.243772
      }
    },
    {
      "kind": "majorPlanet",
      "id": "saturn",
      "displayName": "Saturn",
      "magnitude": 0.8,
      "coordinate": {
        "rightAscensionHours": 0.72882,
        "declinationDegrees": 2.193657
      },
      "distanceAU": 10.023599
    }
  ]
}
```

Event IDs use the stable comet ID, companion ID, and UTC closest-approach date.
Event timestamps are true UTC closest-approach instants. The app is responsible
for local night-of grouping.

## Generation Policy

The generator exposes policy knobs for:

- maximum angular separation
- dynamic-dynamic maximum angular separation
- optional comet magnitude limit
- optional target magnitude limit
- Moon and major-planet target subset
- DSO target subset through the same presentation-focused lunar/planet target
  filter
- ranking cap per comet
- monthly UTC shard range
- source sample cadence, dynamic sample cadence, and refinement cadence

The default package uses all 20 comet snapshot streams, including faint curated
objects. It scans Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and
Neptune; Jupiter and Neptune remain declared dynamic subjects but have no
qualifying events in the generated window. Site-specific nighttime, altitude,
horizon/obstruction, and observability filters remain app-side.

## Source And Accuracy

Comet positions are interpolated from the deterministic `cometSnapshot`
geocentric RA/Dec/magnitude samples. Static DSO positions come from the
AstroGuide catalog target groups. Moon and major-planet positions come from
Skyfield/JPL ephemerides (`de421.bsp`) using geocentric apparent equatorial
RA/Dec.

The default generated package uses the 12-hour comet source cadence, a
3-hour Moon/planet scan cadence, and 60-minute refinement around local
separation minima. The package source metadata records the comet snapshot
package version/checksum, catalog SHA-256, JPL ephemeris name, Skyfield
versions, target metadata paths, coordinate frames, and algorithm description.

This v1 package is planning metadata. It is not a replacement for on-demand JPL
Horizons queries when sub-sample precision is required.

## Dynamic To Dynamic

The index marks `generationModel.dynamicDynamic.status` as `generated`. The
generator pairs every eligible comet stream with Moon and major-planet streams
over the shared UTC range, applies the same policy model, and emits the
standardized close-encounter shape with both participants dynamic. The
`--skip-dynamic-dynamic` flag remains available for explicit diagnostic builds.

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
decoding, TimelineEvent close-encounter mapping for DSO, Moon, and major-planet
companions, local observability filtering, and comet-detail presentation.
