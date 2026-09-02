# Star Party AstroSites v1

## Purpose and product placement

`starPartyAstroSites` is a small, curated metadata family for the Star Parties
folder under Sites, immediately after Dark Skies. It models the public observing
venue as an AstroSite-compatible core and attaches one or more concrete event
instances. A shared venue therefore remains one site even when separate
organizations hold different events there.

Consumers can calculate two useful sort keys without changing the payload:

- **Next**: the earliest non-cancelled event whose `end` has not passed in the
  venue timezone. A completed-only record sorts after upcoming records.
- **Distance**: a device-local great-circle calculation from the venue
  `latitude` and `longitude`. The package never stores a user's position.

The package is optional. The manifest's `1.4.1` compatibility floor reflects
the first app version with verified unknown-family skip behavior; it does not
claim that version has a Star Party consumer. Unknown-family clients must skip
it safely. A client that supports the family should validate and cache it
before replacement, keep the last valid cache through a failed refresh, and
hide Star Parties when no compatible bundled or cached data exists.

## Public package contract

The envelope follows the repository convention:

- `schemaVersion`, `packageFamily`, `packageVersion`, and `generatedAt`
- `scope`, with site, event, status, country, horizon-resource, cached-horizon,
  and obstruction-profile counts
- `starPartyAstroSites`, sorted by stable record `id`

Each record contains:

- stable `id`, `displayName`, a concise factual `description`, and
  `descriptionSources`
- `astroSite`, with the portable v1 site fields `sourceSiteID`, `name`,
  `latitude`, `longitude`, optional `elevationMeters`, and optional path-preview
  direction
- `location`, with venue, locality, region, ISO country identity, IANA
  `timezone`, coordinate provenance, and an optional `relatedDarkSkyPlaceID`
- typed `officialURLs`
- one or more dated `events`, each with a globally stable ID, name, inclusive
  local-calendar `start` and `end`, status, official URL, source, and
  `verifiedAt`
- optional `media.hero` and `media.logo` metadata for approved cached assets
- optional `horizonResources` with source, rights, calibration, disposition,
  and an explicitly bounded visual or obstruction role

Dates are local calendar dates in `location.timezone`; they are deliberately
not UTC instants or recurrence rules. An event's status is one of `scheduled`,
`completed`, or `cancelled`. Keeping separately sourced concrete instances
avoids guessing how an organizer's dates recur from year to year.

`astroSite.sourceSiteID` is a deterministic UUIDv5 derived from
`https://metadata.astroguide.space/star-party-astrosites/<record-id>`. Stable
identity lets a later consumer update a venue without duplicating it.

## Horizon-resource and obstruction boundary

A panorama is not automatically an obstruction profile. Each
`horizonResources` entry records its exact source link, creator when known,
redistribution status, viewpoint relationship, north/azimuth offset, projection,
horizontal and vertical field of view, vertical scale, and whether the evidence
is suitable for calculations. Unknown calibration values remain `null` or
`unknown`; the package does not infer them from the image's aspect ratio.

The quality vocabulary is deliberately explicit:

- `authoritative_hrz`: a venue-authoritative azimuth/altitude profile
- `manual_trace_from_panorama`: a reviewed skyline trace from a sufficiently
  calibrated panorama
- `estimated_from_panorama`: a lower-confidence calibrated derivation
- `visual_panorama_only`: decorative or research context that must not drive
  rise/set, visibility, or obstruction calculations

Cached files require explicit redistribution rights. A public web link without
a reuse grant remains link-only. The builder rejects cached horizon images that
do not have a `licensed_for_redistribution` status, verifies cached-image size,
dimensions, and SHA-256, and rejects `visual_panorama_only` resources marked as
calculation-ready.

The optional `.hrz` bridge matches AstroGuide's current import convention:
UTF-8 text, blank and comment lines ignored, and the first two
whitespace/comma/semicolon-separated values interpreted as azimuth and altitude
degrees. Azimuth must be 0...360 and altitude 0...90. A future checked-in HRZ
must declare its sample count and maps to WIND16 buckets using `average`
aggregation. No current star-party resource satisfies that contract.

## AstroSite compatibility boundary

The `astroSite` object deliberately uses the same core naming, coordinate,
elevation, and stable-source-ID concepts as AstroGuide's AstroSite site payload.
It is an exploded, reviewable metadata representation, not a claim that the
current `.astrosite` ZIP importer can directly import this JSON. Today's archive
contract also requires an obstruction payload and archive manifest, while star
party dates, official URLs, and descriptions are extensions that need a
family-aware consumer. Elevation is optional here because it is omitted when an
official source does not establish it; clients that require elevation must
resolve or explicitly default it before constructing an import archive.

## Source and validation policy

Human-curated inputs live at
`sources/star-party-astrosites/records/<id>/record.json`; the matching JSON
Schema is beside the source README. Official organizer, venue, park, or public
planning sources are retained in every record. Public event/campground points
are permitted. Private or personal observing locations are not.

The builder validates:

- schema and allowed fields
- record, event, and source-site ID uniqueness
- deterministic source-site UUIDs and folder identity
- latitude/longitude and optional elevation ranges
- IANA timezones and ISO country codes
- absolute HTTPS URLs with no embedded credentials
- ISO dates, `end >= start`, status/date consistency, and non-future
  verification dates
- required description, coordinate, and event provenance
- optional media paths, local file presence, attribution, license, permission,
  and source metadata
- optional horizon source, rights, calibration, cached-asset checksum/size/
  dimensions, and HRZ sample validation
- deterministic package ordering and exact stable-manifest checksum, size, and
  counts

Build and validate with:

```bash
python3 scripts/build_star_party_astrosite_package.py
python3 scripts/build_star_party_astrosite_package.py --validate-only
python3 -m unittest tests.test_star_party_astrosite_package
```

For a byte-for-byte reproducible editorial rebuild, pass the checked-in UTC
timestamp through `--generated-at`.

## Initial curated coverage

The first package contains 15 public venues and 19 dated event instances:

- Texas, Winter, Okie-Tex, Oregon, Nebraska, and Almost Heaven Star Parties
- one Cherry Springs venue with Cherry Springs and Black Forest events
- Kelling Heath Autumn Equinox Sky Camp, Starfest Canada, and OzSky Star Safari
- Stellafane Convention, Mount Kobau Star Party, and Kielder Star Camp
- Washington State Star Party and Grand Canyon Star Party

Completed 2026 instances are retained when an organizer has not yet published
the next date. This makes the record useful and sourced without inventing a
future recurrence.

## Deferred candidates, media omissions, and horizon research

- **South Pacific Star Party** is deferred because the Astronomical Society of
  New South Wales says the next event is postponed indefinitely; the package
  requires at least one concrete dated instance. Recheck
  <https://www.asnsw.com/spsp/> during the next editorial update.
- **Golden State Star Party** is deferred because its official FAQ describes
  the site as private property. Publishing a coordinate would conflict with the
  privacy rule, while omitting coordinates would violate the v1 package
  contract. Recheck <https://goldenstatestarparty.org/golden-state-star-party/faq/>
  only if the organizer publishes a clearly approved public event point.

No hero images or logos are included in v1. The available event pages do not
consistently establish redistribution rights, so the package keeps media empty
instead of hotlinking or copying uncertain assets. The optional media contract
is ready for a future explicitly licensed or permission-backed cached asset.

The 2026-09-02 horizon research pass found three useful panorama leads but no
machine-usable public `.hrz`/Stellarium horizon profile for any of the 15
venues:

- **Cherry Springs:** Wikimedia Commons identifies the 2009 panorama as a
  roughly 340-degree, 13-photo Autostitch panorama by user Ruhrfisch under
  CC BY-SA 3.0 (and GFDL). The package caches a 3840-by-281-pixel resize with
  attribution and checksum. Its exact camera point, north offset, projection
  model, vertical field of view, and vertical scale are not supplied, so it is
  `visual_panorama_only`, not an obstruction input. Source:
  <https://commons.wikimedia.org/wiki/File:Cherry_Springs_State_Park_panorama.jpg>.
- **Almost Heaven / Spruce Knob Mountain Center:** the official maps page links
  a panorama from the entrance area toward the Green Lot. The site reserves
  rights and gives no image-specific reuse license, so the package retains only
  the source link with `permission_required`. The JPEG has no embedded heading,
  location, projection, or field-of-view metadata and is
  `visual_panorama_only`. Source: <https://www.ahsp.org/maps-and-directions/>.
- **Oregon Star Party:** the official maps page links an external OSP panorama,
  but no redistribution license was found and the external host presented an
  invalid TLS certificate during verification. It remains an uncached,
  `visual_panorama_only` research lead. Source:
  <https://oregonstarparty.org/osp/osp-site-maps/>.

Two other leads were deliberately excluded from records. A permissively
licensed Spruce Knob panorama was photographed from the summit observation
tower, not the Spruce Knob Mountain Center observing field. TheSkyX documentation
mentions Winter Star Party panoramas supplied courtesy of a photographer, but
that acknowledgement does not grant this repository redistribution rights or
provide a public calibrated source file. Neither lead is suitable for
calculation or caching here.

## Maintenance boundary

This is deliberately curator-maintained. There is no crawler, scraper,
scheduled generator, unattended publication job, or workflow change. A future
editorial pass should verify official dates, coordinates, timezones, status,
descriptions, and links; rebuild locally; inspect the diff; and submit it for
review.
