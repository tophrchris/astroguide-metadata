# Telescope Official Product Links v1

## Purpose and scope

`telescopeOfficialProductLinks` is an optional metadata package that maps a
canonical telescope equipment ID to the corresponding manufacturer or
brand-owner product page. It is intentionally separate from equipment and
reference-price metadata so link maintenance does not rewrite either catalog.

The initial package is a one-time research snapshot covering the ten
manufacturers with the most records in the AstroGuide backyard-market
projection on 2026-09-02, plus every canonical smart-telescope profile. The
selected manufacturers are Celestron, Sky-Watcher, Astro-Tech, Omegon, Askar,
Takahashi, Meade, William Optics, Orion, and Altair. This is a scoped launch
artifact, not a repeatable crawler or a claim of complete catalog coverage.

## Public contract

The package envelope uses the normal AstroGuide `schemaVersion`,
`packageFamily`, `packageVersion`, and `generatedAt` fields. Each
`officialProductLinks` record contains exactly:

- `equipment_id`: stable canonical ID from the cleansed optical-tube catalog
  or canonical smart-telescope catalog.
- `official_url`: exact HTTPS manufacturer or brand-owner product URL, or
  `null` when no qualifying page was found.

Consumers must join only on `equipment_id`. A missing record or `null` URL is
not an error and must simply hide the official-link affordance. Consumers must
not synthesize URLs, fall back to an unrelated retailer, or infer that a linked
page means a product is currently sold or supported.

## Collection policy

The initial pass inspected public manufacturer product catalogs and sitemaps,
then retained exact model matches. Ambiguous bundles, accessories, category
pages, search pages, and ordinary retailer listings were rejected. A few
brand-owner storefronts are the canonical official source even though their
domain differs from the display brand; Astro-Tech, for example, is published
through Astronomics. Askar products are published by their manufacturer on the
Sharpstar/Askar site.

Discontinued products remain in scope because the telescope catalog and the
Upgrade Advisor intentionally support used-market ownership. When an exact
manufacturer archive page exists it may be linked. When a manufacturer has
removed the historical page, the record remains present with `official_url:
null`. This is preferable to linking a different generation or an unofficial
listing.

No crawler, generated match report, retailer data, or transient search result
is committed. The checked-in JSON is the reviewed result of the one-time pass.
Any future refresh should be a deliberate editorial update to this independent
package.

## Initial coverage and limitations

The 2026-09-02 snapshot contains 461 scoped records: 438 rows from the top-ten
manufacturer selection and 23 canonical smart-telescope profiles. It has 161
exact official URLs and 300 explicit unresolved rows. Coverage is uneven
because several manufacturers have removed retired product pages, changed
domains, blocked catalog indexing, or now expose only current-generation
products.

An official link is provenance and further reading, not a live offer,
availability statement, endorsement, affiliate link, or purchasing
recommendation. Retail price metadata remains a separate concern.
