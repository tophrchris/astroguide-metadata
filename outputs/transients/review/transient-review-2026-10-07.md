# TNS transient opportunity review — 2026-10-07

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `b6c54d5815e65d90`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 4 approve, 1 hold, 0 reject
- 26 eligible opportunities before the top-5 review cap
- 1183 staged rows collapsed to 1071 unique TNS objects (112 duplicate/change rows)
- 3 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026adhk](https://www.wis-tns.org/object/2026adhk) | SN Ia | 7 | 18.41 | IC2166 (Galaxy) | 1.38799° | near-field match | 98 | approve |
| urgent | [AT2026adgl](https://www.wis-tns.org/object/2026adgl) | transient_candidate | 8 | 17.4 | Great Nebula in Andromeda (Galaxy) | 0.04483° | near-field match | 95 | approve |
| urgent | [AT2026aejp](https://www.wis-tns.org/object/2026aejp) | transient_candidate | 7 | 18.24 | IC2183 (Nebula) | 0.16658° | near-field match | 93 | approve |
| urgent | [AT2026aeru](https://www.wis-tns.org/object/2026aeru) | transient_candidate | 0 | 18.09 | NGC 3003 (Galaxy) | 0.80299° | near-field match | 90 | approve |
| urgent | [AT2026aesu](https://www.wis-tns.org/object/2026aesu) | transient_candidate | 6 | 17.89 | IC 589 (Galaxy) | 0.61267° | near-field match | 90 | hold |

## Candidate dossiers

### 1. [SN2026adhk](https://www.wis-tns.org/object/2026adhk) near IC2166

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 98/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2166 as this object's host. The 1.38799° (83.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.055 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-30T05:52:35Z · 7 days · 18.41 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3924....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR3924....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2166** · `IC2166` |
| Catalog display name | IC2166 |
| Type / constellation | Galaxy · Lynx |
| Catalog magnitude / angular size | 12.4 · 2.2′ × 1.08′ |
| Distance | — |
| Separation | 1.38799° · 83.28′ |
| Catalog description | nebula; faint a single star preceding (westward) / pretty (adv., before F. B. L, S) 1', double a single star following (eastward) 3' |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adhk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.1005196%2058.4365348&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [AT2026adgl](https://www.wis-tns.org/object/2026adgl) near Great Nebula in Andromeda

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.04483° (2.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T18:17:05Z · 8 days · 17.4 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3913....1C](https://ui.adsabs.harvard.edu/abs/2026TNSTR3913....1C/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Great Nebula in Andromeda** · `NGC224` |
| Catalog display name | Great Nebula in Andromeda |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 3.4 · 177.83′ × 69.66′ |
| Distance | 674.509 kpc |
| Separation | 0.04483° · 2.69′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.652667%2041.230611&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026aejp](https://www.wis-tns.org/object/2026aejp) near IC2183

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2183 as this object's host. The 0.16658° (9.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-30T12:19:58Z · 7 days · 18.24 i |
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
| Subject | **IC2183** · `IC2183` |
| Catalog display name | IC2183 |
| Type / constellation | Nebula · Canis Major |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.16658° · 9.99′ |
| Catalog description | wisp 2'north-south, 3 stars (pl.) north, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aejp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=109.05475%20-20.558483&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026aeru](https://www.wis-tns.org/object/2026aeru) near NGC 3003

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3003 as this object's host. The 0.80299° (48.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T11:50:49Z · 0 days · 18.09 r |
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
| Subject | **NGC 3003** · `NGC 3003` |
| Catalog display name | NGC 3003 |
| Type / constellation | Galaxy · LMi |
| Catalog magnitude / angular size | 11.78 · 4.74′ × 1.06′ |
| Distance | — |
| Separation | 0.80299° · 48.18′ |
| Catalog description | NGC 3003 is a nearly edge-on barred spiral galaxy in the constellation of Leo Minor, discovered by William Herschel on December 7, 1785. It has an apparent visual magnitude of 11.78, at a distance of 19.5 Mpc from the Sun. It has a recessional velocity of 1474 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=147.488661%2032.6702983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026aesu](https://www.wis-tns.org/object/2026aesu) near IC 589

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 589 as this object's host. The 0.61267° (36.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T12:49:47Z · 6 days · 17.89 r |
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
| Separation | 0.61267° · 36.76′ |
| Catalog description | NGC 3110, also known as NGC 3122 and NGC 3518, is an active spiral galaxy in the constellation Sextans. It contains extensive Hubble-type Sb star-forming regions, and is located south of the celestial equator. It is estimated to be 218 million light-years from the Milky Way and has a diameter of around 100,000 ly. Together with PGC 29184 it forms a gravitationally bound galaxy pair. Located in the same area of the sky is the galaxy IC 589. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 589 has the different designation NGC 3110 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aesu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=150.903785%20-5.0980868&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
