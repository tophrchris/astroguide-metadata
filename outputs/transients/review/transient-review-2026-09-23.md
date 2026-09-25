# TNS transient opportunity review — 2026-09-23

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `29286ea0d4772a2a`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 21 eligible opportunities before the top-5 review cap
- 815 staged rows collapsed to 755 unique TNS objects (60 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026aaiv](https://www.wis-tns.org/object/2026aaiv) | SN Ia | 22 | 17.32 | Caldwell 30 (Galaxy) | 0.00802° | near-field match | 100 | approve |
| urgent | [AT2026aaom](https://www.wis-tns.org/object/2026aaom) | Nova | 19 | 18.2 | Andromeda Galaxy (Galaxy) | 0.05081° | near-field match | 100 | approve |
| urgent | [AT2026abyx](https://www.wis-tns.org/object/2026abyx) | transient_candidate | 6 | 18.3 | Great Nebula in Andromeda (Galaxy) | 0.01298° | near-field match | 100 | approve |
| urgent | [SN2026acjs](https://www.wis-tns.org/object/2026acjs) | SN II | 3 | 17.87 | IC4784 (Galaxy) | 0.44666° | near-field match | 100 | approve |
| urgent | [AT2026acuq](https://www.wis-tns.org/object/2026acuq) | transient_candidate | 1 | 15 | NGC797 (Galaxy) | 0.19644° | near-field match | 100 | approve |

## Candidate dossiers

### 1. [SN2026aaiv](https://www.wis-tns.org/object/2026aaiv) near Caldwell 30

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 30 as this object's host. The 0.00802° (0.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.002722 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-01T11:23:32Z · 22 days · 17.32 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3537....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR3537....1T/abstract) |
| Classification references | [2026TNSCR3548....1B](https://ui.adsabs.harvard.edu/abs/2026TNSCR3548....1B/abstract), [2026TNSCR3579....1V](https://ui.adsabs.harvard.edu/abs/2026TNSCR3579....1V/abstract), [2026TNSCR3581....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR3581....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Caldwell 30** · `C30` |
| Catalog display name | Caldwell 30 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 9.5 · 11′ × 4′ |
| Distance | — |
| Separation | 0.00802° · 0.48′ |
| Catalog description | NGC 7331, also known as Caldwell 30, is an unbarred spiral galaxy about 13.427 megaparsecs away in the constellation Pegasus. It was discovered by William Herschel on 6 September 1784. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aaiv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=339.2734487%2034.409775&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [AT2026aaom](https://www.wis-tns.org/object/2026aaom) near Andromeda Galaxy

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 0.05081° (3.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | Nova |
| Redshift | 0.0 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-04T03:37:43Z · 19 days · 18.2 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3573....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR3573....1F/abstract) |
| Classification references | [2026TNSCR3675....1B](https://ui.adsabs.harvard.edu/abs/2026TNSCR3675....1B/abstract), [2026TNSCR3698....1Z](https://ui.adsabs.harvard.edu/abs/2026TNSCR3698....1Z/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Andromeda Galaxy** · `M31` |
| Catalog display name | Andromeda Galaxy |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 3.4 · 178′ × 63′ |
| Distance | 889.144 kpc |
| Separation | 0.05081° · 3.05′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aaom) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.709944%2041.3158936&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026abyx](https://www.wis-tns.org/object/2026abyx) near Great Nebula in Andromeda

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.01298° (0.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T21:25:12Z · 6 days · 18.3 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3774....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR3774....1F/abstract) |
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
| Separation | 0.01298° · 0.78′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abyx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.670573%2041.260308&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [SN2026acjs](https://www.wis-tns.org/object/2026acjs) near IC4784

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4784 as this object's host. The 0.44666° (26.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.0155 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-20T09:28:57Z · 3 days · 17.87 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3796....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3796....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC4784** · `IC4784` |
| Catalog display name | IC4784 |
| Type / constellation | Galaxy · Pavo |
| Catalog magnitude / angular size | 13.7 · 1.51′ × 1.21′ |
| Distance | 65,600 kpc |
| Separation | 0.44666° · 26.80′ |
| Catalog description | considerably faint, small in angular size, round, brighter middle, or in the middle |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=283.634771%20-62.858732&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026acuq](https://www.wis-tns.org/object/2026acuq) near NGC797

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 0.19644° (11.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 1 days · 15 Other |
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
| Subject | **NGC797** · `IC 720 NED01` |
| Catalog display name | NGC797 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 1.05′ × 0.93′ |
| Distance | — |
| Separation | 0.19644° · 11.79′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acuq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=175.429167%208.654167&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
