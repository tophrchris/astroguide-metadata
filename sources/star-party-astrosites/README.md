# Star Party AstroSite sources

Each public observing venue has one reviewable source record at
`records/<stable-id>/record.json`. The runtime package is generated from these
records; do not hand-edit the package artifact.

To add or update an event:

1. Copy an existing record folder and choose a durable, lowercase kebab-case
   venue/event identity. One venue can contain multiple independently organized
   events, as Cherry Springs demonstrates.
2. Derive `astroSite.sourceSiteID` as UUIDv5 using the URL namespace and
   `https://metadata.astroguide.space/star-party-astrosites/<record-id>`.
3. Use a public venue point. Record an official or authoritative public source
   for the coordinates, every event date, and the short factual description.
4. Store concrete dated event instances, not recurrence rules. Update status
   when a dated instance has passed or is cancelled.
5. Add a `horizonResources` entry only when its exact viewpoint, azimuth/north
   offset, projection, horizontal and vertical field of view, vertical scale,
   provenance, and rights status can be stated explicitly. Unknown values must
   remain unknown. Use `visual_panorama_only` unless the evidence supports a
   calibrated obstruction profile.
6. Cache a panorama only with an explicit redistribution license or permission.
   Link-only research and permission-pending sources must not include an asset.
   A calculation-ready `.hrz` must use azimuth/altitude degree pairs and declare
   the `average` WIND16 aggregation used by AstroGuide.
7. Run `python3 scripts/build_star_party_astrosite_package.py`, inspect the
   package and manifest diff, then run the validation command documented in the
   repository README.

The machine-readable authoring contract is
`star-party-astrosite-source-v1.schema.json`. The builder performs the stronger
cross-record, filesystem, chronology, timezone, URL, deterministic-ID, and
manifest checks that JSON Schema alone cannot express.

Do not publish private observing-site coordinates. Media may be added only
when redistribution rights are explicit; it must be cached under
`v1/assets/star-party-astrosites/` with attribution, license, permission notes,
and provenance in the source record. Never hotlink an event image or logo.
The same rights rule applies to horizon panoramas; public availability alone is
not permission to cache or redistribute an image.
