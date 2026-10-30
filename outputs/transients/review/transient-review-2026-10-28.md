# TNS transient opportunity review — 2026-10-28

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `dc43bb357180cfdf`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 4 approve, 1 hold, 0 reject
- 28 eligible opportunities before the top-5 review cap
- 721 staged rows collapsed to 678 unique TNS objects (43 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026afsg](https://www.wis-tns.org/object/2026afsg) | SN Ib/c | 10 | 16.4 | NGC 2207 / IC 2163 (Galaxy) | 1.22593° | near-field match | 100 | approve |
| urgent | [AT2026aguw](https://www.wis-tns.org/object/2026aguw) | transient_candidate | 3 | 17.67 | IC 4747 (Galaxy) | 0.23524° | near-field match | 100 | hold |
| urgent | [SN2026agwb](https://www.wis-tns.org/object/2026agwb) | SN Ia | 2 | 17.8 | NGC134 (Galaxy) | 0.96564° | near-field match | 100 | approve |
| urgent | [AT2026agzo](https://www.wis-tns.org/object/2026agzo) | transient_candidate | 4 | 18.14 | NGC3239 (Galaxy) | 0.15481° | near-field match | 100 | approve |
| urgent | [SN2026agpv](https://www.wis-tns.org/object/2026agpv) | SN II | 5 | 17.47 | NGC636 (Galaxy) | 1.88839° | near-field match | 98 | approve |

## Candidate dossiers

### 1. [SN2026afsg](https://www.wis-tns.org/object/2026afsg) near NGC 2207 / IC 2163

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.22593° (73.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ib/c |
| Redshift | 0.010277 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T20:55:20Z · 10 days · 16.4 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4199....1L](https://ui.adsabs.harvard.edu/abs/2026TNSTR4199....1L/abstract) |
| Classification references | [2026TNSCR4258....1B](https://ui.adsabs.harvard.edu/abs/2026TNSCR4258....1B/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afsg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=180.5123246%2029.8447081&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [AT2026aguw](https://www.wis-tns.org/object/2026aguw) near IC 4747

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 100/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4747 as this object's host. The 0.23524° (14.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T00:35:40Z · 3 days · 17.67 orange |
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
| Subject | **IC 4747** · `IC 4747` |
| Catalog display name | NGC 5555 |
| Type / constellation | Galaxy · Pav |
| Catalog magnitude / angular size | — · 1.1′ × 0.37′ |
| Distance | 538.83 ly |
| Separation | 0.23524° · 14.11′ |
| Catalog description | NGC 5555 is a spiral galaxy located in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 11200 ± 20 km/s, which corresponds to a Hubble distance of 165.20 ± 11.57 Mpc. It was originally discovered in 1886 by the American astronomer, Ormond Stone. NGC 5555 is situated close to the celestial equator and given its visual magnitude of 15.53, NGC 5555 is visible only through long exposure photography. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4747 has the different designation NGC 5555 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aguw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=281.8984011%20-72.8314256&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026agwb](https://www.wis-tns.org/object/2026agwb) near NGC134

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC134 as this object's host. The 0.96564° (57.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.061 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T09:16:41Z · 2 days · 17.8 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4285....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4285....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC134** · `NGC134` |
| Catalog display name | NGC134 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 10.3 · 8.38′ × 1.79′ |
| Distance | 17,600 kpc |
| Separation | 0.96564° · 57.94′ |
| Catalog description | NGC 134 is a barred spiral galaxy that resembles the Milky Way with its spiral arms loosely wrapped around a bright, bar-shaped central region. Its loosely bound spiral arms categorize it as Hubble-type Sbc. It is 60 million light years away, and part of the Sculptor constellation. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=6.4394233%20-33.3519633&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026agzo](https://www.wis-tns.org/object/2026agzo) near NGC3239

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.15481° (9.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:49:08Z · 4 days · 18.14 r |
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
| Subject | **NGC3239** · `NGC3239` |
| Catalog display name | NGC3239 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.4 · 3.61′ × 2.71′ |
| Distance | — |
| Separation | 0.15481° · 9.29′ |
| Catalog description | NGC 3239 is an irregular galaxy in the constellation of Leo. The galaxy was discovered in 1784 by William Herschel and is part of the New General Catalogue. It harbors a large and relatively bright H II region in its southeastern section that was first cataloged by Russian astronomer Boris Vorontsov-Velyaminov as VV95b. It's believed that NGC 3239 is the result of a galactic merger with a low-mass galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agzo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.4034933%2017.0807088&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [SN2026agpv](https://www.wis-tns.org/object/2026agpv) near NGC636

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 98/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.88839° (113.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.025111 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-23T22:30:00Z · 5 days · 17.47 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4260....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4260....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC636** · `NGC636` |
| Catalog display name | NGC636 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.4 · 2.7′ × 2.3′ |
| Distance | 26,700 kpc |
| Separation | 1.88839° · 113.30′ |
| Catalog description | NGC 636 is an elliptical galaxy in the Cetus constellation. It is located about 96 million light-years from the Milky Way. It was discovered by the German–British astronomer William Herschel in 1785. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agpv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.8529207%20-9.3994273&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
