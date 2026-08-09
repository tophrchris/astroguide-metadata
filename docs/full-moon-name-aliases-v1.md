# Full Moon Name Aliases v1

The `fullMoonNameAliases` package is AstroGuide's lightweight catalog of
English Full Moon display names and source-attributed aliases. It contains 12
stable month-resolved entries, not generated lunations or astronomical events.

The initial package has one fixed primary library and three alias libraries:

| Role | Library ID | Display name | Provenance status |
| --- | --- | --- | --- |
| Primary | `north-american-popular` | North American Popular | Mixed editorial compilation; usage review required |
| Alias | `mixed-provenance-popular-alternatives` | Mixed-Provenance Popular Alternatives | Secondary compilation with unresolved item-level provenance |
| Alias | `english-medieval` | English / Medieval | Secondary compilation; not a verified medieval canon |
| Alias | `modern-pagan` | Modern Pagan | One secondary-source list; not universal across modern Pagan traditions |

These labels deliberately do not create a generic Indigenous or global
library. Community-specific Indigenous systems, Southern Hemisphere systems,
Sri Lankan Poya, Hindu Purnima, and other distinct calendars need independent
reviewed sources and resolver models before they are added.

## Resolution contract

The package declares resolver `gregorianMonthOfContainedFullMoon` version 1.
The consuming app must:

1. calculate a New-Moon-to-New-Moon cycle;
2. locate the exact Full Moon instant inside that half-open cycle;
3. convert that instant to its Gregorian month in UTC; and
4. select the one entry whose `resolutionKey.month` matches.

Using UTC is an explicit package policy. It keeps the selected name stable for
all users when a Full Moon instant is near a local month boundary. The metadata
does not perform site-, observer-, locale-, or timezone-specific astronomy.

The Full Moon's primary name may also label its containing cycle under the
package's `namedAfterContainedFullMoon` AstroGuide convention. For example,
`Sturgeon Moon Cycle` is a product label; it does not make `New Sturgeon Moon`
or `Waxing Sturgeon Moon` historically sourced phase names.

## Entry and provenance shape

Each entry uses a stable month identity and stores one primary display record
plus deduplicated alias display records:

```json
{
  "id": "full-moon-gregorian-month-09",
  "resolutionKey": {
    "month": 9,
    "monthName": "September"
  },
  "primaryName": {
    "displayName": "Corn Moon",
    "claims": [
      {
        "libraryID": "north-american-popular",
        "sourceID": "old-farmers-almanac-full-moon-names-2026",
        "sourceNameText": "Corn Moon",
        "confidence": "mixed",
        "provenanceQuality": "editorialCompilation"
      }
    ]
  },
  "aliases": [
    {
      "displayName": "Harvest Moon",
      "claims": [
        {
          "libraryID": "mixed-provenance-popular-alternatives",
          "sourceID": "uni-names-for-the-full-moon",
          "sourceNameText": "Harvest",
          "confidence": "low",
          "provenanceQuality": "unresolvedCompilation"
        },
        {
          "libraryID": "modern-pagan",
          "sourceID": "uni-names-for-the-full-moon",
          "sourceNameText": "Harvest",
          "confidence": "low",
          "provenanceQuality": "unresolvedCompilation"
        }
      ]
    }
  ]
}
```

An alias display string occurs at most once within an entry. Its `claims`
array retains every independent library/source claim. When an alias library
uses the same display text as the primary library, its claim is retained on
the `primaryName` record instead of creating a duplicate alias row.

Attribution, cultural/region/hemisphere scope, library confidence, provenance
quality, licensing notes, and usage-review status live in `libraries[]` and
`sources[]`. A client follows each claim's `libraryID` and `sourceID` to show
that context without repeating it in every month entry.

## Source and editorial caveats

- The North American Popular primary claims follow *The Old Farmer's
  Almanac — Full Moon Names for 2026*. The package transcribes short names,
  not the source's descriptions. Its record remains `permissionRequired`
  pending consumer-publication usage review.
- The three alternative sets use the University of Northern Iowa's *Names for
  the Full Moon* table as their traceable transcription source. That page has
  no item-level historical citations or stated reuse license, so the package
  marks those claims `low` confidence with `unresolvedCompilation`
  provenance.
- Exact source spellings `Dyan` and `Lightening` are retained and explicitly
  marked unresolved instead of silently corrected.
- Harvest Moon, Hunter's Moon, and Blood Moon occur only where a named source
  library explicitly records them. The app must independently calculate any
  equinox-, sequence-, eclipse-, or color-based context and must not infer it
  from these aliases.
- The primary September base name is Corn Moon. Harvest Moon remains a runtime
  seasonal label even when a source library also supplies it as an alias.

## Runtime boundary

This package intentionally contains no lunation IDs, phase-event IDs, cycle
dates, observer locations, local timezones, supermoon/micromoon flags,
eclipses, Blue Moon calculations, or close-encounter assignments. Those values
depend on generated astronomy or product rules and remain app-side.

## Updating libraries

The reviewed source input is
`sources/full-moon-name-aliases/full_moon_name_aliases_v1.json`. Each library
declares its own identity, display order, role, attribution, sources, review
state, and 12 month claims. The builder derives the shared entry records from
that data, so adding, removing, or correcting a library does not require a
builder or app schema change.

Rebuild and validate with:

```bash
python3 scripts/build_full_moon_name_alias_package.py
python3 scripts/build_full_moon_name_alias_package.py --validate-only
python3 -m unittest tests.test_full_moon_name_alias_package -v
```

The builder emits canonical compact JSON, updates the stable manifest's
package URL, record count, byte size, and SHA-256 checksum, and validates the
entire integrity chain.
