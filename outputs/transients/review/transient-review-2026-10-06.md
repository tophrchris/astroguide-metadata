# TNS transient opportunity review — 2026-10-06

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `aa92ca6f7e41083c`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 25 eligible opportunities before the top-5 review cap
- 1199 staged rows collapsed to 1066 unique TNS objects (133 duplicate/change rows)
- 3 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026adgl](https://www.wis-tns.org/object/2026adgl) | transient_candidate | 7 | 17.4 | Great Nebula in Andromeda (Galaxy) | 0.04483° | near-field match | 100 | approve |
| urgent | [SN2026adhk](https://www.wis-tns.org/object/2026adhk) | SN Ia | 6 | 18.41 | IC2166 (Galaxy) | 1.38799° | near-field match | 98 | approve |
| urgent | [SN2026adgw](https://www.wis-tns.org/object/2026adgw) | SN Ia | 7 | 18.46 | White-Eyed Pea nebula (Planetary nebula) | 0.91717° | near-field match | 95 | approve |
| urgent | [AT2026admi](https://www.wis-tns.org/object/2026admi) | transient_candidate | 7 | 18.35 | Collinder 22 (CR22) (Open cluster) | 0.17124° | near-field match | 93 | approve |
| urgent | [AT2026aejp](https://www.wis-tns.org/object/2026aejp) | transient_candidate | 6 | 18.24 | IC2183 (Nebula) | 0.16658° | near-field match | 93 | approve |

## Candidate dossiers

### 1. [AT2026adgl](https://www.wis-tns.org/object/2026adgl) near Great Nebula in Andromeda

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.04483° (2.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T18:17:05Z · 7 days · 17.4 Clear |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.652667%2041.230611&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026adhk](https://www.wis-tns.org/object/2026adhk) near IC2166

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 98/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2166 as this object's host. The 1.38799° (83.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.055 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-30T05:52:35Z · 6 days · 18.41 L |
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

### 3. [SN2026adgw](https://www.wis-tns.org/object/2026adgw) near White-Eyed Pea nebula

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify White-Eyed Pea nebula as this object's host. The 0.91717° (55.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.037 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T02:43:07Z · 7 days · 18.46 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3930....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR3930....1S/abstract) |
| Classification references | [2026TNSCR3950....1F](https://ui.adsabs.harvard.edu/abs/2026TNSCR3950....1F/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **White-Eyed Pea nebula** · `IC 4593` |
| Catalog display name | White-Eyed Pea nebula |
| Type / constellation | Planetary nebula · Her |
| Catalog magnitude / angular size | — · 0.2′ × 0.17′ |
| Distance | — |
| Separation | 0.91717° · 55.03′ |
| Catalog description | IC 4593 is a planetary nebula in the constellation Hercules. It was first discovered in 1907 by astronomer Williamina Fleming. The nebula is approximately 0.96 light-years across. At the center of the nebula is a hot white dwarf that's known as HD 145649, which is an O-type star with a spectral type of O7f. The temperature of the white dwarf is approximately 30,000 to 40,000 K. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=243.0531324%2011.1584604&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026admi](https://www.wis-tns.org/object/2026admi) near Collinder 22 (CR22)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 22 (CR22) as this object's host. The 0.17124° (10.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T01:28:42Z · 7 days · 18.35 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3936....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR3936....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 22 (CR22)** · `CR22` |
| Catalog display name | Collinder 22 (CR22) |
| Type / constellation | Open cluster · Perseus |
| Catalog magnitude / angular size | 7.9 · 11.7′ × 11.7′ |
| Distance | 1.207 kpc |
| Separation | 0.17124° · 10.27′ |
| Catalog description | NGC 744 is a small open cluster located in the Perseus constellation containing approximately 140 stars. It was discovered by 19th century English astronomer John Herschel on 28 November 1831. NGC 744 has a visual magnitude of 7.9 and is visible with the help of a telescope having an aperture of 1.50 inches (40mm) or more, and is moving towards the Sun with a radial velocity of -25.47 km/s±0.15. It is located approximately 4478.13 light years,, from the Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026admi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.8621137%2055.57792&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026aejp](https://www.wis-tns.org/object/2026aejp) near IC2183

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2183 as this object's host. The 0.16658° (9.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-30T12:19:58Z · 6 days · 18.24 i |
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

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
