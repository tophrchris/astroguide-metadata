# Telescope Reference Prices v1

## Purpose and scope

`telescopeReferencePrices` is an optional, independently refreshed metadata
package for broad portfolio visualization. It provides approximate US
new-retail reference prices rounded to the nearest $50. A value is editorial
reference data, not a live offer, retailer comparison, quote, MSRP, or promise
that the product is currently purchasable.

This package deliberately supersedes the unshipped `telescopeRetailPrices`
prototype. The earlier contract represented exact current offers and required
retailer provenance. Removing product links and source attribution makes that
claim unverifiable to a consumer, so v1 uses a distinct package family and
honest estimate semantics instead of weakening the retail-price contract.

The rapid release is US/USD only. It excludes affiliate links, product links,
retailer names, tax, shipping, coupons, historical charts, alerts, geographic
personalization, used-market values, browser automation, and generalized
crawling.

## Canonical join and publishing

The production input is
`v1/packages/equipment/astrophotography_equipment_sanitized_catalog_v1.json`.
Every `catalog.opticalComponents[]` row whose `component_type` is
`optical_tube` receives exactly one output row. `equipment_id` is copied from
that row's canonical `component_id`; no parallel identity system exists.

The output is
`v1/packages/telescope-reference-prices/telescope_reference_prices_v1.json`
and is registered in `v1/channels/stable/manifest.json`. A missing estimate is
represented by a complete row with `price_amount: null`; it never blocks the
equipment package.

## Public contract

Each `referencePrices` row contains exactly:

- `equipment_id`: canonical sanitized-catalog `component_id`.
- `price_amount`: approximate USD major-unit amount rounded to `precision`, or
  null.
- `currency`: `USD` when an estimate exists, otherwise null.
- `price_basis`: `typical_new_retail` or `last_known_new_retail`, otherwise
  null. The latter is permitted only for discontinued products with
  reproducible new-retail evidence.
- `precision`: `50` when an estimate exists, otherwise null.
- `estimated_at`: UTC time when the retained estimate was established,
  otherwise null.
- `market_status`: `current`, `discontinued`, or `unknown`.
- `match_confidence`: 0-1 confidence that evidence describes the exact
  canonical product/configuration.
- `estimate_confidence`: 0-1 confidence in the approximate amount. It is
  distinct from identity confidence.
- `evidence_count`: count of qualifying evidence items. Evidence identities
  are not published.
- `manual_override`: true when a curator suppressed or replaced the generated
  result.
- `note`: concise identity, estimate, or override context.

There are intentionally no retailer, source, product URL, or affiliate fields.
Consumers should display the amount as approximate (for example, `about
$1,300`) and must not use it as an exact purchasable price.

## Estimation and qualification

The updater uses the OpenAI Responses API with web search, a pinned model
snapshot, and strict structured output. Model memory alone is never accepted.
`store` is false. Returned
evidence URLs must also appear in the API's web-search source list. Exact URLs
are used only in memory during that process and are never written to the
repository, package, or report.

The request includes the canonical manufacturer, model, aperture, focal
length, and focal ratio. Each evidence item must explicitly identify itself as
the exact sold product. The pipeline rejects bundle/kit, accessory,
used/refurbished, marketplace, financing/deposit, or other configurations even
if the model marks the listing as a name match.

Qualifying evidence is limited to manufacturer, established astronomy
specialty retailer, and reputable authorized-retailer pages. A single source
is accepted only when it is a manufacturer or astronomy specialty retailer,
and estimate confidence is then capped at 0.75. Multiple evidence prices are
reduced to their median and rounded to $50. Excessive evidence spread, weak
identity confidence, weak estimate confidence, an uncited URL, or a material
model/evidence disagreement sends the item to review instead of publication.

The launch plausibility range is $25-$250,000 so both entry-level and
observatory-class instruments can be represented. A change of at least 35%
and an adaptive dollar floor is retained for review rather than automatically
replacing the prior estimate.

## Stored state and curator control

Files are separated by responsibility:

- `sources/telescope-reference-prices/config.json`: model, thresholds,
  cadence, bounds, and rounding policy.
- `sources/telescope-reference-prices/estimates.json`: last successful rounded
  estimates, source-type summaries, opaque SHA-256 source keys, and refresh
  attempts. It contains no source names, domains, or URLs.
- `sources/telescope-reference-prices/overrides.json`: version-controlled
  curator suppressions, replacements, and rejected opaque evidence keys.
- `reports/telescope-reference-prices/latest.json`: scan counts, failures,
  review items, changes, new IDs, and stale estimates.
- `v1/packages/telescope-reference-prices/telescope_reference_prices_v1.json`:
  deterministic public projection.

A `suppress` override needs `equipment_id`, `action`, and `note`. A `replace`
override additionally supplies `result` fields matching the public contract
other than `equipment_id`, `manual_override`, and `note`, which the generator
sets. Overrides are applied after generated estimates and survive rescans.
Removing or revising the override returns control to the retained automatic
estimate. `rejected_evidence` can permanently reject an opaque `source_key`
without retaining its URL.

## Freshness, incrementality, and failure behavior

The scheduled job runs weekly, considers at most 50 due records per routine
run, refreshes a successful estimate after 120 days, and reports it stale after
180 days. Missing and review outcomes retain their last attempt time so the
same ambiguous first batch cannot starve the rest of the catalog. Newly added
canonical telescope IDs are prioritized automatically.

A failed or ambiguous refresh preserves the last successful amount and its
original `estimated_at`. The new attempt and diagnostic are recorded
separately. One API or malformed-response failure is isolated to that
telescope. Consumers use `estimated_at` and their own presentation policy for
staleness; v1 does not introduce a second public stale enum.

## Operations

Local commands:

```bash
OPENAI_API_KEY=... python3 scripts/update_telescope_reference_prices.py
OPENAI_API_KEY=... python3 scripts/update_telescope_reference_prices.py \
  --equipment-id optical-tube-zwo-ff65-apo-quintuplet-32011 --force
python3 scripts/update_telescope_reference_prices.py --offline
python3 scripts/update_telescope_reference_prices.py --validate-only
python3 -m unittest tests/test_telescope_reference_prices.py -v
```

Do not paste an API key into source, logs, issues, pull requests, or chat. The
weekly workflow requires the repository secret `OPENAI_API_KEY` and opens or
updates a reviewable automation pull request; it does not write directly to
`main`. A manual dispatch can target one canonical ID for an announcement-time
refresh without increasing the normal batch rate.

The workflow does not crawl arbitrary sites, authenticate to retailers, solve
CAPTCHAs, bypass access controls, or imitate human browsing. Web retrieval is
performed by the supported search tool. If evidence cannot be returned through
that legitimate path, the item remains missing or enters review.

## Launch coverage and known limitations

The seed covers 20 high-confidence exact configurations across refractors,
astrographs, SCT/Maksutov designs, Dobsonians/Newtonians, integrated systems,
and observatory-class instruments. The other catalog rows are explicit nulls
until researched. Reliable partial coverage is intentional.

Deferred: exhaustive coverage, exact live offers, retailer/source disclosure,
affiliate integration, international markets/currencies, current inventory,
preorder/backorder status, lowest-price comparison, price history, alerts,
shipping/tax calculations, coupon optimization, and used-market values.
