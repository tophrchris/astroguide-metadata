# TNS transient opportunity review — 2026-10-15

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `ebb81c5d26950036`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 3 approve, 2 hold, 0 reject
- 20 eligible opportunities before the top-5 review cap
- 690 staged rows collapsed to 651 unique TNS objects (39 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026afec](https://www.wis-tns.org/object/2026afec) | transient_candidate | 4 | 16.32 | NGC578 (Galaxy) | 1.29392° | near-field match | 93 | approve |
| urgent | [SN2026adyr](https://www.wis-tns.org/object/2026adyr) | SN Ia | 13 | 18.34 | IC 1894 (Galaxy) | 1.56111° | near-field match | 90 | hold |
| urgent | [AT2026aexh](https://www.wis-tns.org/object/2026aexh) | transient_candidate | 7 | 18.45 | NGC 3294 (Galaxy) | 1.34695° | near-field match | 83 | approve |
| urgent | [AT2026aexm](https://www.wis-tns.org/object/2026aexm) | transient_candidate | 6 | 16.78 | NGC3423 (Galaxy) | 1.41770° | near-field match | 83 | approve |
| urgent | [AT2026aeyo](https://www.wis-tns.org/object/2026aeyo) | transient_candidate | 6 | 18 | IC 589 (Galaxy) | 1.42402° | near-field match | 83 | hold |

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
| Discovery | 2026-10-11T13:53:16Z · 4 days · 16.32 L |
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
| Discovery | 2026-10-02T06:01:38Z · 13 days · 18.34 L |
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

### 3. [AT2026aexh](https://www.wis-tns.org/object/2026aexh) near NGC 3294

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.34695° (80.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-08T12:36:55Z · 7 days · 18.45 r |
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
| Subject | **NGC 3294** · `NGC 3294` |
| Catalog display name | NGC 3294 |
| Type / constellation | Galaxy · LMi |
| Catalog magnitude / angular size | 11.68 · 3.08′ × 1.6′ |
| Distance | — |
| Separation | 1.34695° · 80.82′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aexh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.3709098%2036.0990191&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026aexm](https://www.wis-tns.org/object/2026aexm) near NGC3423

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3423 as this object's host. The 1.41770° (85.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T12:47:47Z · 6 days · 16.78 r |
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

### 5. [AT2026aeyo](https://www.wis-tns.org/object/2026aeyo) near IC 589

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 83/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 589 as this object's host. The 1.42402° (85.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T12:47:06Z · 6 days · 18 r |
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
| Subject | **IC 589** · `IC 589` |
| Catalog display name | NGC 3110 |
| Type / constellation | Galaxy · Sex |
| Catalog magnitude / angular size | — · 0.69′ × 0.51′ |
| Distance | — |
| Separation | 1.42402° · 85.44′ |
| Catalog description | NGC 3110, also known as NGC 3122 and NGC 3518, is an active spiral galaxy in the constellation Sextans. It contains extensive Hubble-type Sb star-forming regions, and is located south of the celestial equator. It is estimated to be 218 million light-years from the Milky Way and has a diameter of around 100,000 ly. Together with PGC 29184 it forms a gravitationally bound galaxy pair. Located in the same area of the sky is the galaxy IC 589. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 589 has the different designation NGC 3110 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeyo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.0092487%20-4.5802838&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
