# Telescope Reference Price Manual Validation — 2026-08-25

## Method

The rapid coverage expansion was checked against canonical production-equipment
IDs from both telescope catalogs, sold configuration, aperture, focal length,
optical design, approximate $50 rounding, and generated public records. A
different generation was
accepted only when all four identity/configuration dimensions still matched;
those records are labeled `generation_proxy` internally, capped at 0.94 match
confidence, and explained in the public note.

Exact product links and source identities are intentionally absent from this
report. Evidence is identified only as manufacturer or established astronomy
specialty retailer.

## Representative sample

| Canonical equipment ID | Class / risk sampled | Approximate result | Finding |
| --- | --- | ---: | --- |
| `optical-tube-svbony-sv503-70ed-33194` | Small ED refractor | $400 | Pass; exact 70 mm / 420 mm OTA |
| `optical-tube-stellalyra-8-f-6-dobsonian-16425` | Integrated Dobsonian | $600 | Pass; exact 203 mm / 1200 mm sold configuration |
| `optical-tube-celestron-c11-edge-hd-120` | SCT variant discrimination | $4,500 | Pass; EdgeHD OTA retained, not standard C11 or mount bundle |
| `optical-tube-celestron-114-gt-1825` | Same-spec generation proxy | $500 | Pass; 114 mm / 1000 mm Newtonian GoTo configuration retained |
| `optical-tube-sky-watcher-star-discovery-150p-157` | Same-spec generation proxy | $850 | Pass; 150 mm / 750 mm Newtonian GoTo configuration retained |
| `optical-tube-sky-watcher-explorer-190mn-ds-pro-18` | Maksutov-Newtonian versus Newtonian | $2,100 | Pass; exact 190 mm / 1000 mm optical design and OTA |
| `optical-tube-explore-scientific-208-f3-9-newtonian-1844` | Discontinued generation | $700 | Pass; last-known new-retail basis and discontinued status retained |
| `optical-tube-apm-lzos-130-780-4598` | Foreign-currency expensive refractor | $9,000 | Pass; exact 130 mm / 780 mm model, auditable conversion before rounding |
| `optical-tube-planewave-cdk700-4340` | Observatory-class instrument | $235,000 | Pass; exact CDK700, within the configured plausibility ceiling |
| `optical-tube-planewave-pw1000-533` | Extreme-price integrated system | $600,000 | Pass; same-spec current CDK1000 generation, 1000 mm / 6000 mm f/6 integrated system; proxy labeled and confidence-capped |
| `optical-tube-tec-apo250vt-f-8-8-31826` | Very expensive refractor | $72,000 | Pass; exact 250 mm / 2200 mm f/8.8 OTA |
| `optical-tube-astro-physics-rh305-1534` | Discontinued premium astrograph | $17,500 | Pass; exact 305 mm / 1160 mm configuration, last-known new-retail basis and discontinued status retained |
| `optical-tube-gso-16-rc-various-34598` | Large Ritchey-Chretien | $8,750 | Pass; exact 406 mm f/8 truss OTA, with only nominal focal-length rounding |
| `optical-tube-altair-wave-130-edt-535` | Premium triplet refractor | $2,850 | Pass; exact 130 mm / 905 mm OTA |
| `optical-tube-orion-eon-130-324` | Discontinued refractor | $2,000 | Pass; exact 130 mm / 910 mm OTA, last-known new-retail basis and discontinued status retained |
| `optical-tube-svbony-sv550-122-apo-33191` | Standalone OTA versus bundle | $1,700 | Pass; exact 122 mm / 854 mm standalone OTA, accessory bundles excluded |
| `zwo-seestar-s30-pro` | New dual-camera smart telescope | $700 | Pass; exact integrated S30 Pro system, telephoto profile |
| `zwo-seestar-s30-pro-wide` | Same smart system, wide profile | $700 | Pass; canonical wide-camera profile correctly shares the full S30 Pro system price rather than pricing its camera as an accessory |
| `dwarflab-dwarf-ii` | Discontinued smart telescope | $300 | Pass; last-known new-retail system price retained, refurbished offers excluded |
| `vaonis-vespera-ii` | Foreign-currency smart telescope | $1,850 | Pass; exact instrument-only configuration converted at the scan-time rate, optional tripod packs excluded |
| `unistellar-evscope-2` | Premium smart telescope | $5,000 | Pass; exact complete system with included tripod, refurbished listing excluded |
| `celestron-origin-mark-ii` | Integrated smart observatory | $4,300 | Pass; exact Mark II system, used units and camera-only upgrade excluded |
| `optical-tube-apertura-carbonstar-150-33199` | OTA versus accessory bundle | $950 | Pass; OTA-only reference retained, no bundle arithmetic |
| `optical-tube-stellarvue-102t-209` | Older/newer model generation | $3,100 | Pass; 102 mm / 714 mm triplet OTA proxy labeled and confidence-capped |
| `optical-tube-takahashi-fsq-106-16` | Similar generation naming | $7,350 | Pass; 106 mm / 530 mm four-element OTA proxy labeled; availability unknown |

## Errors and corrections found

- Two Astro Fi 6-inch SCT candidates incorrectly resolved to a 130 mm
  Newtonian page. Both were rejected.
- An Omegon 96 mm triplet candidate used a 575 mm current product for a 530 mm
  canonical focal length. It was rejected.
- A Sky-Watcher Esprit 100 candidate used the current 550 mm generation for a
  canonical 500 mm configuration. It was rejected.
- A William Optics FLT132 candidate used a 924 mm current product for a 910 mm
  canonical configuration. It was rejected.
- Current SVBONY SV406P results exposed camera-adapter bundles rather than a
  reproducible standalone telescope price. The canonical row remains unpriced.
- A current SVBONY SA405 page described an 85 mm / 482.6 mm instrument, not the
  canonical 80 mm / 450 mm configuration. It was rejected.
- A GSO classical Cassegrain candidate described 203 mm / 2436 mm, not the
  canonical 203 mm / 2346 mm configuration. It was rejected.
- Current Astro-Physics products with reused family names did not preserve the
  focal lengths of several older canonical rows. Those rows remain unpriced.
- The original DWARF, Vespera, eVscope, and eQuinox profiles lacked sufficiently
  reproducible exact new-retail evidence. They remain explicit nulls.
- Open-box and refurbished smart-telescope listings were rejected even when
  they were cheaper than qualifying new-retail examples.
- The newly announced Seestar S50 Pro was matched to its exact launch listing.
  Its official 50 mm / 260 mm tele profile and $899 launch sale are represented
  by a canonical smart-catalog row and a $900 rounded reference estimate.
- Several mount bundles, accessories, and different optical designs surfaced
  during candidate generation and were left unpriced rather than used to meet
  the coverage target.
- A separate curator-approved approximate batch adds exactly 100 previously
  missing rows across Meade (33), Sky-Watcher (30), William Optics (17), Orion
  (16), and Altair (4). The batch separates 36 current references from 64
  discontinued last-known new-retail references, uses lower estimate
  confidence, and marks every published row as a manual override.

## Generated-output checks

- 712 eligible canonical optical-tube rows plus 23 canonical smart-telescope
  profiles, producing 735 unique output rows.
- 518 estimated rows and 217 explicit missing rows: 70.5% coverage overall.
- Smart-telescope coverage is 19 of 23; cleansed optical-tube coverage remains
  499 of 712.
- Exactly 100 rows are manual overrides: 36 current and 64 discontinued.
- 31 retained rows use the documented same-spec generation-proxy rule;
  all are labeled and have match confidence no higher than 0.94.
- Price-scale coverage: 81 under $500; 245 from $500-$1,999; 169 from
  $2,000-$9,999; 19 from $10,000-$49,999; 4 at $50,000 or more.
- The documented $750,000 plausibility ceiling accepts the reviewed $600,000
  observatory-system outlier while continuing to reject larger parser errors.
- No retailer name, product URL, affiliate URL, source domain, or evidence URL
  appears in retained state, the report, or the public package.
- Package checksum and byte size match the stable-manifest descriptor.
