# TNS transient opportunity review — 2026-09-18

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `22ee0fae39cd2d4f`. A pull-request approval is the editorial rubber stamp for this artifact; treat any changed PR head or evidence hash as requiring re-approval. Merge still does not publish it to the app or change `reviewDecision` from `pending`.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 19 eligible opportunities before the top-5 review cap
- 692 staged rows collapsed to 656 unique TNS objects (36 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026aaom](https://www.wis-tns.org/object/2026aaom) | Nova | 14 | 18.2 | Andromeda Galaxy (Galaxy) | 0.05081° | near-field match | 100 | approve |
| urgent | [AT2026abyx](https://www.wis-tns.org/object/2026abyx) | transient_candidate | 1 | 18.3 | Great Nebula in Andromeda (Galaxy) | 0.01298° | near-field match | 100 | approve |
| urgent | [AT2026ably](https://www.wis-tns.org/object/2026ably) | transient_candidate | 11 | 14.52 | NGC265 (Open cluster) | 0.09236° | near-field match | 95 | approve |
| urgent | [AT2026abys](https://www.wis-tns.org/object/2026abys) | transient_candidate | 1 | 18.08 | Caldwell 7 (C7) (Galaxy) | 0.62232° | near-field match | 90 | approve |
| urgent | [AT2026acfn](https://www.wis-tns.org/object/2026acfn) | transient_candidate | 1 | 18.2 | IC5003 (Galaxy) | 0.67314° | near-field match | 90 | approve |

## Candidate dossiers

### 1. [AT2026aaom](https://www.wis-tns.org/object/2026aaom) near Andromeda Galaxy

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 0.05081° (3.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | Nova |
| Redshift | 0.0 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-04T03:37:43Z · 14 days · 18.2 Clear |
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

### 2. [AT2026abyx](https://www.wis-tns.org/object/2026abyx) near Great Nebula in Andromeda

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.01298° (0.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T21:25:12Z · 1 days · 18.3 Clear |
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
| Subject | **Great Nebula in Andromeda** · `NGC224` |
| Catalog display name | Great Nebula in Andromeda |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 3.4 · 177.83′ × 69.66′ |
| Distance | 674.509 kpc |
| Separation | 0.01298° · 0.78′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abyx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.670573%2041.260308&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026ably](https://www.wis-tns.org/object/2026ably) near NGC265

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC265 as this object's host. The 0.09236° (5.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-07T03:25:55Z · 11 days · 14.52 R |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3684....1B](https://ui.adsabs.harvard.edu/abs/2026TNSTR3684....1B/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC265** · `NGC265` |
| Catalog display name | NGC265 |
| Type / constellation | Open cluster · Tucana |
| Catalog magnitude / angular size | 12.2 · 1.2′ × 1.2′ |
| Distance | — |
| Separation | 0.09236° · 5.54′ |
| Catalog description | NGC 265 is an open cluster of stars in the southern constellation of Tucana. It is located in the Small Magellanic Cloud, a nearby dwarf galaxy. The cluster was discovered by English astronomer John Herschel on April 11, 1834. J. L. E. Dreyer described it as, "faint, pretty small, round", and added it as the 265th entry in his New General Catalogue. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤16.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ably) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.725962%20-73.567631&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026abys](https://www.wis-tns.org/object/2026abys) near Caldwell 7 (C7)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 7 (C7) as this object's host. The 0.62232° (37.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T04:35:54Z · 1 days · 18.08 wide |
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
| Subject | **Caldwell 7 (C7)** · `C7` |
| Catalog display name | Caldwell 7 (C7) |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 8.9 · 18′ × 10′ |
| Distance | — |
| Separation | 0.62232° · 37.34′ |
| Catalog description | NGC 2403 is an intermediate spiral galaxy in the constellation Camelopardalis. It is an outlying member of the M81 Group, and is approximately 8 million light-years distant. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abys) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.7759913%2065.0075553&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026acfn](https://www.wis-tns.org/object/2026acfn) near IC5003

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5003 as this object's host. The 0.67314° (40.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T02:25:24Z · 1 days · 18.2 Other |
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
| Subject | **IC5003** · `IC5003` |
| Catalog display name | IC5003 |
| Type / constellation | Galaxy · Microscopium |
| Catalog magnitude / angular size | 12.9 · 2.36′ × 0.66′ |
| Distance | 28,600 kpc |
| Separation | 0.67314° · 40.39′ |
| Catalog description | very faint, considerably small in angular size, round, 2 stars (pl.) south following irregular north little (adv.); long (adj.) irregular north extremely, excessively |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acfn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=310.754458%20-30.524917&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
