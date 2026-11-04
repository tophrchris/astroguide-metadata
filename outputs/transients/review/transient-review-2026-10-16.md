# TNS transient opportunity review — 2026-10-16

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `3d85ca7dd0a5f416`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 4 approve, 1 hold, 0 reject
- 18 eligible opportunities before the top-5 review cap
- 652 staged rows collapsed to 609 unique TNS objects (43 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026afec](https://www.wis-tns.org/object/2026afec) | transient_candidate | 5 | 16.32 | NGC578 (Galaxy) | 1.29392° | near-field match | 93 | approve |
| urgent | [SN2026adyr](https://www.wis-tns.org/object/2026adyr) | SN Ia | 14 | 18.34 | IC 1894 (Galaxy) | 1.56111° | near-field match | 90 | hold |
| urgent | [AT2026aexm](https://www.wis-tns.org/object/2026aexm) | transient_candidate | 7 | 16.78 | NGC3423 (Galaxy) | 1.41770° | near-field match | 83 | approve |
| urgent | [AT2026aeyw](https://www.wis-tns.org/object/2026aeyw) | transient_candidate | 7 | 18.24 | NGC3348 (Galaxy) | 1.74484° | near-field match | 83 | approve |
| urgent | [AT2026afge](https://www.wis-tns.org/object/2026afge) | transient_candidate | 6 | 18.24 | IC1696 (Galaxy) | 1.64345° | near-field match | 83 | approve |

## Candidate dossiers

### 1. [AT2026afec](https://www.wis-tns.org/object/2026afec) near NGC578

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC578 as this object's host. The 1.29392° (77.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-11T13:53:16Z · 5 days · 16.32 L |
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
| Subject | **NGC578** · `NGC578` |
| Catalog display name | NGC578 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.1 · 4.82′ × 2.92′ |
| Distance | 18,250 kpc |
| Separation | 1.29392° · 77.64′ |
| Catalog description | NGC 578 is a spiral galaxy in the constellation Cetus. The galaxy lies about 60 million light years away from Earth, which means, given its apparent dimensions, that NGC 578 is approximately 110,000 light years across. It was discovered by John Herschel on November 11, 1835. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afec) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.897502%20-21.560473&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026adyr](https://www.wis-tns.org/object/2026adyr) near IC 1894

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1894 as this object's host. The 1.56111° (93.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.037 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-02T06:01:38Z · 14 days · 18.34 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3957....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR3957....1R/abstract) |
| Classification references | — |
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
| Separation | 1.56111° · 93.67′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1894 has the different designation IC 1101 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.7884737%2020.9663579&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026aexm](https://www.wis-tns.org/object/2026aexm) near NGC3423

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3423 as this object's host. The 1.41770° (85.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T12:47:47Z · 7 days · 16.78 r |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aexm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=163.1286794%207.2215449&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026aeyw](https://www.wis-tns.org/object/2026aeyw) near NGC3348

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3348 as this object's host. The 1.74484° (104.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T11:41:14Z · 7 days · 18.24 r |
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
| Subject | **NGC3348** · `NGC3348` |
| Catalog display name | NGC3348 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.9 · 2.13′ × 2.13′ |
| Distance | 32,200 kpc |
| Separation | 1.74484° · 104.69′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeyw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.6799599%2071.6261472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026afge](https://www.wis-tns.org/object/2026afge) near IC1696

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.64345° (98.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-10T11:01:09Z · 6 days · 18.24 w |
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
| Subject | **IC1696** · `IC1696` |
| Catalog display name | IC1696 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.6 · 0.83′ × 0.75′ |
| Distance | 72,050 kpc |
| Separation | 1.64345° · 98.61′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afge) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.0182666%20-3.2600203&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
