# TNS transient opportunity review — 2026-11-03

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `cf42c6dc47e11dbe`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 3 approve, 2 hold, 0 reject
- 36 eligible opportunities before the top-5 review cap
- 1052 staged rows collapsed to 963 unique TNS objects (89 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026aguw](https://www.wis-tns.org/object/2026aguw) | SN Ia | 9 | 17.67 | IC 4747 (Galaxy) | 0.23524° | near-field match | 100 | hold |
| urgent | [SN2026agwm](https://www.wis-tns.org/object/2026agwm) | SN Ia | 7 | 18.33 | IC4931 (Galaxy) | 0.65936° | near-field match | 100 | approve |
| urgent | [AT2026ahvi](https://www.wis-tns.org/object/2026ahvi) | transient_candidate | 1 | 16.1 | NGC4216 (Galaxy) | 0.39366° | near-field match | 100 | approve |
| urgent | [SN2026ahvu](https://www.wis-tns.org/object/2026ahvu) | SN Ia | 1 | 17.06 | NGC1433 (Galaxy) | 0.01649° | near-field match | 100 | approve |
| urgent | [AT2026ahxs](https://www.wis-tns.org/object/2026ahxs) | transient_candidate | 6 | 17.5 | IC 1777 (Galaxy) | 0.07735° | near-field match | 100 | hold |

## Candidate dossiers

### 1. [SN2026aguw](https://www.wis-tns.org/object/2026aguw) near IC 4747

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 100/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4747 as this object's host. The 0.23524° (14.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.05 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T00:35:40Z · 9 days · 17.67 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4274....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4274....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 4747** · `IC 4747` |
| Catalog display name | NGC 5555 |
| Type / constellation | Galaxy · Pav |
| Catalog magnitude / angular size | — · 1.1′ × 0.37′ |
| Distance | 538.83 ly |
| Separation | 0.23524° · 14.11′ |
| Catalog description | NGC 5555 is a spiral galaxy located in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 11200 ± 20 km/s, which corresponds to a Hubble distance of 165.20 ± 11.57 Mpc. It was originally discovered in 1886 by the American astronomer, Ormond Stone. NGC 5555 is situated close to the celestial equator and given its visual magnitude of 15.53, NGC 5555 is visible only through long exposure photography. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4747 has the different designation NGC 5555 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aguw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=281.8984011%20-72.8314256&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026agwm](https://www.wis-tns.org/object/2026agwm) near IC4931

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4931 as this object's host. The 0.65936° (39.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.02 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T00:01:05Z · 7 days · 18.33 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4297....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4297....1T/abstract) |
| Classification references | [2026TNSCR4355....1N](https://ui.adsabs.harvard.edu/abs/2026TNSCR4355....1N/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC4931** · `IC4931` |
| Catalog display name | IC4931 |
| Type / constellation | Galaxy · Sagittarius |
| Catalog magnitude / angular size | 11.9 · 2.28′ × 1.43′ |
| Distance | 67,000 kpc |
| Separation | 0.65936° · 39.56′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, a star of 8th magnitude following (eastward) 20s , following (eastward) of 2 |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=299.7725657%20-38.0113271&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026ahvi](https://www.wis-tns.org/object/2026ahvi) near NGC4216

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4216 as this object's host. The 0.39366° (23.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T19:55:53Z · 1 days · 16.1 Clear |
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
| Subject | **NGC4216** · `NGC4216` |
| Catalog display name | NGC4216 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 9.9 · 7.82′ × 1.84′ |
| Distance | — |
| Separation | 0.39366° · 23.62′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.460042%2013.424472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [SN2026ahvu](https://www.wis-tns.org/object/2026ahvu) near NGC1433

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1433 as this object's host. The 0.01649° (0.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.003589 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T04:20:36Z · 1 days · 17.06 cyan |
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
| Subject | **NGC1433** · `NGC1433` |
| Catalog display name | NGC1433 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 9.9 · 6.19′ × 2.96′ |
| Distance | — |
| Separation | 0.01649° · 0.99′ |
| Catalog description | NGC 1433 is a barred spiral galaxy with a double ring structure located in the constellation of Horologium. It was discovered by James Dunlop on 28 September 1826, and lies a distance of 46 million light-years from Earth. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=55.4812957%20-47.2276079&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026ahxs](https://www.wis-tns.org/object/2026ahxs) near IC 1777

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 100/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1777 as this object's host. The 0.07735° (4.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T05:26:42Z · 6 days · 17.5 g |
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
| Subject | **IC 1777** · `IC 1777` |
| Catalog display name | IC 3370 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.91′ × 0.91′ |
| Distance | 156 ly |
| Separation | 0.07735° · 4.64′ |
| Catalog description | IC 3370 is an elliptical galaxy located in the constellation of Centaurus. It is located 156 million light-years from Earth. It was discovered by American astronomer Lewis Swift on 30 January 1898. According to the SIMBAD database, IC 3370 is said to be a LINER galaxy but also a Seyfert type II galaxy. The luminosity of the galaxy is estimated to have a B magnitude of -22.3, similar to other elliptical galaxies. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1777 has the different designation IC 3370 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.5459%2015.1326871&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
