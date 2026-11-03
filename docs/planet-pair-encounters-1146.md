# Planet-pair close encounters (#1146)

Local producer candidate only; no remote publication, stable-manifest change,
candidate approval, or transient-policy change is authorized by this work.

## Contract and compatibility

The existing `planetTargetCloseEncounters` schema-1 monthly shards can encode two
`majorPlanet` participants using the existing event family/type. No new family is
needed. The current iOS candidate at de0baaa decodes those participants but drops
the record in its planet/DSO mapper. Its detail matching, site filter, specialized
sheet and saved-event reopening also require compatibility fixes. Publishing
this data alone does not make planet pairs work in that app. Existing DSO events
remain consumable by older clients; additive pairs are ignored by that mapper.

## Generation

The maintained producer now adds each unordered pair of the seven supported
major planets exactly once (21 pairs; Earth and Pluto excluded). Both positions
are geocentric apparent positions from JPL DE421 through Skyfield, including its
light-time/apparent corrections. Outer-planet barycenters follow the existing
producer body definitions. Angular proximity is not physical association,
occultation, local observability, or a safe solar-observing recommendation.

Skyfield `find_minima` searches apparent angular separation with a six-hour
initial step and 0.5-second numerical time tolerance. The horizon is positive and
at most 1096 days. Two-day padding finds minima at requested-window boundaries;
only start-inclusive/end-exclusive minima at or below the requested threshold
are retained. The default threshold remains 5 degrees. Separation is serialized
to four decimals. Numerical tolerance is not a claim of observational accuracy.
No device performs this search. Search documentation:
https://rhodesmill.org/skyfield/searches.html

Pair IDs sort stable planet IDs and append the UTC date of the minimum. Same-day
identity collisions fail rather than silently discarding a minimum. Pair order
and package version do not change bookmark identity. All record, shard,
checksum and package validators remain in use, with additional distinct-known-
planet, canonical-order and identity checks for pairs.

## Local evidence

- Real cached DE421, Skyfield 1.55: 34 pairs over 2026-08-08 through 2028-08-08.
- All 21 pairs over 731 days took 0.84 seconds in the focused test run.
- Ten focused producer tests passed, including the five existing DSO tests.
- Real minima checked at +/-10 minutes, threshold, two-year bounds, symmetry,
  stable IDs, invalid participant/order/identity, and padded edge behavior.
- Maintained full producer and package validator passed using the exact combined
  iOS catalog pin `6b4922a085135d0df79820fad3dfe71ff534aa0e314013036a354284470a547b`.
- Package `planet-target-close-encounters-v1-20261103-planet-pairs`: 380 events,
  25 monthly shards. Its 346 existing iOS DSO event objects are exactly unchanged;
  34 planet-pair records were added. Stable channel manifest is unchanged.
- Example: Jupiter/Mars minimum 2026-11-16T02:04:50Z, 1.1933 degrees.

No independent HORIZONS cross-check, physical-device observation, deployment or
public-feed delivery is claimed. iOS path/visibility calculations retain the
existing approximate display engine and must not replace the producer's
authoritative closest-approach instant/separation. Publication requires separate
coordination with the compatible app candidate; this branch is not published.
