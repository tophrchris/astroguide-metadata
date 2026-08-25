# Telescope Reference Price Manual Validation — 2026-08-24

## Method

The launch seed was checked against the canonical sanitized equipment row,
exact sold configuration, qualifying new-retail evidence, $50 rounding, and
the generated public record. Exact product links and retailer identities are
intentionally omitted from this report. Evidence was classified only as
manufacturer or established astronomy specialty retailer.

## Representative sample

| Canonical equipment ID | Class / risk sampled | Approximate result | Evidence | Finding |
| --- | --- | ---: | --- | --- |
| `optical-tube-celestron-c90-mak-1792` | Low-cost Maksutov; standard spotting configuration | $300 | Specialty | Pass; $318.95 rounds to $300 |
| `optical-tube-apertura-ad8-8-dobsonian-5675` | Integrated 8-inch Dobsonian, not OTA-only | $700 | Specialty | Pass; exact AD8 sold configuration |
| `optical-tube-apertura-ad12-12-dobsonian-5340` | Larger Dobsonian aperture variant | $1,300 | Specialty | Pass; not confused with AD8/AD10 |
| `optical-tube-apertura-carbonstar-150-33199` | Imaging Newtonian OTA | $950 | Specialty | Pass; no mount/bundle substitution |
| `optical-tube-askar-sqa55-34583` | Small flat-field refractor/astrograph | $800 | Specialty | Pass; exact SQA55 configuration |
| `optical-tube-william-optics-redcat-51-wifd-35193` | Generation-specific astrograph | $900 | Specialty | Pass; WIFD generation retained |
| `optical-tube-celestron-c6-sct-117` | SCT OTA versus integrated kit | $1,050 | Specialty | Pass; OTA evidence only |
| `optical-tube-celestron-nexstar-6se-109` | Integrated SCT/mount configuration | $1,350 | Specialty | Pass; not replaced by C6 OTA price |
| `optical-tube-celestron-c14-edge-hd-119` | Expensive EdgeHD versus standard SCT | $7,700 | Specialty | Pass; EdgeHD identity preserved |
| `optical-tube-celestron-14-rowe-ackermann-schmidt-astrograph-5741` | Expensive RASA versus C14 SCT | $15,000 | Manufacturer | Pass; exact 14-inch RASA |
| `optical-tube-planewave-17-cdk-394` | Observatory-class CDK aperture variant | $26,000 | Manufacturer | Pass; exact CDK17 OTA |
| `optical-tube-planewave-24-rc-1912` | Six-figure RC versus CDK line | $99,500 | Manufacturer | Pass; exact 24-inch RC OTA |
| `optical-tube-zwo-ff65-apo-quintuplet-32011` | Current ZWO astrograph; corroboration | $800 | Manufacturer + specialty | Pass; two evidence types agree |

## Errors and corrections found

- The first evidence schema did not independently label exact product versus
  bundle/accessory/used configurations. A required `configuration` enum and a
  deterministic `exact_product` gate were added before publication.
- The first incremental design would have retried the same unpriced first
  batch every week. Per-equipment refresh attempts are now retained so later
  catalog rows progress and new IDs remain prioritized.
- No price, rounding, canonical-ID, or OTA-versus-kit error remained in the
  representative launch sample after those corrections.

## Generated-output checks

- 712 eligible canonical optical-tube rows; 712 unique output rows.
- 20 estimated rows and 692 explicit missing rows.
- Price-scale coverage: 1 under $500; 11 from $500-$1,999; 3 from
  $2,000-$9,999; 4 from $10,000-$49,999; 1 at $50,000 or more.
- No retailer name, product URL, affiliate URL, source domain, or evidence URL
  appears in retained state, the report, or the public package.
- Package checksum/byte size match the stable-manifest descriptor.
