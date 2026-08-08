# Planet/Target Close Encounters v1

The `planetTargetCloseEncounters` package family publishes global, geocentric
closest approaches between AstroGuide catalog targets and the seven major
planets other than Earth: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and
Neptune. Comets and meteor showers are intentionally outside this v1 slice.

The stable manifest references a compact index package. The index records the
source catalog and astronomy algorithm, defines the supported subjects, and
references checksummed monthly compact-JSON shards. Each shard event uses a
generic participant array so the iOS close-encounter foundation can later
generalize beyond a Moon-specific host/subject model.

## Event shape

```json
{
  "id": "planet-target-close-encounter-mars-M45-20260812",
  "eventFamily": "closeEncounter",
  "type": "planetTargetCloseEncounter",
  "eventTimeUTC": "2026-08-12T04:05:06Z",
  "closestApproachUTC": "2026-08-12T04:05:06Z",
  "minimumSeparationDegrees": 1.25,
  "participants": [
    {
      "kind": "majorPlanet",
      "id": "mars",
      "displayName": "Mars",
      "magnitude": 1.2
    },
    {
      "kind": "deepSkyObject",
      "id": "M45",
      "catalogID": "M45",
      "displayName": "Pleiades",
      "objectType": "Open_cluster",
      "magnitude": 1.6
    }
  ]
}
```

Event IDs use the stable planet ID, canonical target-group ID, and UTC
closest-approach date. The generator rejects duplicate or nonconforming IDs.
Planet magnitude is included when Skyfield's planetary magnitude model returns
a finite value; target magnitude is included when the catalog provides one.

Window and duration fields are omitted in v1. Slow outer planets can remain
within the default 5-degree threshold through more than one local minimum, so a
single threshold-duration interval can be ambiguous. The closest-approach
instant remains deterministic and compact.

## Candidate and observability boundaries

The DSO candidate set matches the presentation-focused lunar-events filter:
curated target metadata, priority-1 seasonal recommendations, named target
neighborhood showcase IDs, Messier targets, and NGC/IC targets with a known
magnitude of 10.0 or brighter. This excludes the unknown-magnitude back catalog
unless a target is explicitly curated and keeps the hosted package lightweight.

Generated events are not site-specific. A consuming app must filter for the
active site, selected time range, nighttime, altitude, horizon/obstructions,
and observability. Equipment/FOV filtering is a later presentation refinement,
not a package-generation requirement.

## iOS integration boundary

Existing app builds safely ignore the unknown manifest family. DSOPlanneriOS
follow-up for issues #1018 and #1019 must add the package family, bundled
fallback/sync support, index and shard decoding, generic close-encounter or
`TimelineEvent` mapping, local observability filtering, and planet-detail
presentation. The manifest compatibility version should be reviewed against
the app release that first implements those pieces.
