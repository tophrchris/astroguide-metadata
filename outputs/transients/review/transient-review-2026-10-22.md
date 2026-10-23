# TNS transient opportunity review — 2026-10-22

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `c3c863b1a015a4a1`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 3 approve, 2 hold, 0 reject
- 23 eligible opportunities before the top-5 review cap
- 960 staged rows collapsed to 913 unique TNS objects (47 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026afsw](https://www.wis-tns.org/object/2026afsw) | SN Ia | 5 | 18.23 | IC 1600 (Galaxy) | 1.66251° | near-field match | 98 | hold |
| urgent | [AT2026afsg](https://www.wis-tns.org/object/2026afsg) | transient_candidate | 4 | 16.4 | NGC 2207 / IC 2163 (Galaxy) | 1.22593° | near-field match | 93 | approve |
| urgent | [SN2026adyr](https://www.wis-tns.org/object/2026adyr) | SN Ia | 20 | 18.34 | IC 1894 (Galaxy) | 1.56109° | near-field match | 90 | hold |
| urgent | [SN2026aela](https://www.wis-tns.org/object/2026aela) | SN Ia | 17 | 18.14 | NGC797 (Galaxy) | 1.46986° | near-field match | 90 | approve |
| urgent | [SN2026aexm](https://www.wis-tns.org/object/2026aexm) | SN Ia | 13 | 16.78 | NGC3423 (Galaxy) | 1.41770° | near-field match | 90 | approve |

## Candidate dossiers

### 1. [SN2026afsw](https://www.wis-tns.org/object/2026afsw) near IC 1600

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 98/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1600 as this object's host. The 1.66251° (99.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.05499 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T04:57:05Z · 5 days · 18.23 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1600** · `IC 1600` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.8′ × 0.47′ |
| Distance | — |
| Separation | 1.66251° · 99.75′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1600 has the different designation IC 1101 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afsw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=14.6142185%20-22.0569355&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [AT2026afsg](https://www.wis-tns.org/object/2026afsg) near NGC 2207 / IC 2163

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.22593° (73.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T20:55:20Z · 4 days · 16.4 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2207 / IC 2163** · `IC 2992` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | — · 0.63′ × 0.52′ |
| Distance | 81 ly |
| Separation | 1.22593° · 73.56′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afsg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=180.5123246%2029.8447081&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026adyr](https://www.wis-tns.org/object/2026adyr) near IC 1894

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1894 as this object's host. The 1.56109° (93.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.037 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-02T06:01:38Z · 20 days · 18.34 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3957....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR3957....1R/abstract) |
| Classification references | [2026TNSCR4091....1F](https://ui.adsabs.harvard.edu/abs/2026TNSCR4091....1F/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1894** · `IC 1894` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.78′ × 0.52′ |
| Distance | — |
| Separation | 1.56109° · 93.67′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1894 has the different designation IC 1101 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.7885158%2020.9663643&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [SN2026aela](https://www.wis-tns.org/object/2026aela) near NGC797

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.46986° (88.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0503 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T20:31:24Z · 17 days · 18.14 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4020....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4020....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC797** · `IC 510 NED01` |
| Catalog display name | NGC797 |
| Type / constellation | Galaxy · Hya |
| Catalog magnitude / angular size | — · 0.33′ × 0.18′ |
| Distance | — |
| Separation | 1.46986° · 88.19′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aela) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=129.4776153%20-1.8406808&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [SN2026aexm](https://www.wis-tns.org/object/2026aexm) near NGC3423

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3423 as this object's host. The 1.41770° (85.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0205 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T12:47:47Z · 13 days · 16.78 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4071....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4071....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3423** · `NGC3423` |
| Catalog display name | NGC3423 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 11.2 · 3.56′ × 3.03′ |
| Distance | — |
| Separation | 1.41770° · 85.06′ |
| Catalog description | NGC 3423 is a spiral galaxy in the constellation Sextans. The galaxy lies about 45 million light years away from Earth, which means, given its apparent dimensions, that NGC 3423 is approximately 50,000 light years across. It was discovered by William Herschel on February 23, 1784. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aexm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=163.1286794%207.2215449&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
