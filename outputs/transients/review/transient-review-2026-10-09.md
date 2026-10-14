# TNS transient opportunity review — 2026-10-09

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `6a8e8e99c2d6829f`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 26 eligible opportunities before the top-5 review cap
- 996 staged rows collapsed to 909 unique TNS objects (87 duplicate/change rows)
- 2 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026adgl](https://www.wis-tns.org/object/2026adgl) | transient_candidate | 10 | 17.4 | Great Nebula in Andromeda (Galaxy) | 0.04483° | near-field match | 95 | approve |
| urgent | [AT2026aeru](https://www.wis-tns.org/object/2026aeru) | transient_candidate | 2 | 18.09 | NGC 3003 (Galaxy) | 0.80299° | near-field match | 90 | approve |
| urgent | [AT2026aevv](https://www.wis-tns.org/object/2026aevv) | transient_candidate | 3 | 18.36 | IC4796 (Galaxy) | 0.79651° | near-field match | 90 | approve |
| urgent | [SN2026adgw](https://www.wis-tns.org/object/2026adgw) | SN Ia | 10 | 18.46 | White-Eyed Pea nebula (Planetary nebula) | 0.91717° | near-field match | 87 | approve |
| urgent | [AT2026admi](https://www.wis-tns.org/object/2026admi) | transient_candidate | 10 | 18.35 | Collinder 22 (CR22) (Open cluster) | 0.17124° | near-field match | 85 | approve |

## Candidate dossiers

### 1. [AT2026adgl](https://www.wis-tns.org/object/2026adgl) near Great Nebula in Andromeda

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.04483° (2.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T18:17:05Z · 10 days · 17.4 Clear |
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

### 2. [AT2026aeru](https://www.wis-tns.org/object/2026aeru) near NGC 3003

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3003 as this object's host. The 0.80299° (48.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T11:50:49Z · 2 days · 18.09 r |
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

### 3. [AT2026aevv](https://www.wis-tns.org/object/2026aevv) near IC4796

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4796 as this object's host. The 0.79651° (47.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-06T18:32:24Z · 3 days · 18.36 orange |
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
| Subject | **IC4796** · `IC4796` |
| Catalog display name | IC4796 |
| Type / constellation | Galaxy · Telescopium |
| Catalog magnitude / angular size | 12.3 · 1.95′ × 1.08′ |
| Distance | 35,700 kpc |
| Separation | 0.79651° · 47.79′ |
| Catalog description | 14m, brighter middle, or in the middle, near extremely, excessively diameter gradually extremely, excessively of plate |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aevv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=283.3047525%20-53.575282&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [SN2026adgw](https://www.wis-tns.org/object/2026adgw) near White-Eyed Pea nebula

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify White-Eyed Pea nebula as this object's host. The 0.91717° (55.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.037 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T02:43:07Z · 10 days · 18.46 r |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=243.0531324%2011.1584604&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026admi](https://www.wis-tns.org/object/2026admi) near Collinder 22 (CR22)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 85/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 22 (CR22) as this object's host. The 0.17124° (10.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T01:28:42Z · 10 days · 18.35 wide |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026admi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.8621137%2055.57792&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
