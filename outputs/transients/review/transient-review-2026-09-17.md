# TNS transient opportunity review — 2026-09-17

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `087e69360b03ad75`. A pull-request approval is the editorial rubber stamp for this artifact; treat any changed PR head or evidence hash as requiring re-approval. Merge still does not publish it to the app or change `reviewDecision` from `pending`.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 19 eligible opportunities before the top-5 review cap
- 552 staged rows collapsed to 516 unique TNS objects (36 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026aaom](https://www.wis-tns.org/object/2026aaom) | Nova | 13 | 18.2 | Andromeda Galaxy (Galaxy) | 0.05081° | near-field match | 100 | approve |
| urgent | [AT2026ably](https://www.wis-tns.org/object/2026ably) | transient_candidate | 10 | 14.52 | NGC265 (Open cluster) | 0.09236° | near-field match | 95 | approve |
| urgent | [AT2026abys](https://www.wis-tns.org/object/2026abys) | transient_candidate | 0 | 18.08 | Caldwell 7 (C7) (Galaxy) | 0.62232° | near-field match | 90 | approve |
| urgent | [AT2026abbx](https://www.wis-tns.org/object/2026abbx) | Nova | 9 | 12.6 | Lynds Dark Nebula 161 (LDN161) (Dark nebula) | 0.37662° | near-field match | 89 | approve |
| urgent | [AT2026abuf](https://www.wis-tns.org/object/2026abuf) | transient_candidate | 19 | 17.89 | Wild Duck cluster (Open cluster) | 0.20167° | near-field match | 85 | approve |

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
| Discovery | 2026-09-04T03:37:43Z · 13 days · 18.2 Clear |
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

### 2. [AT2026ably](https://www.wis-tns.org/object/2026ably) near NGC265

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC265 as this object's host. The 0.09236° (5.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-07T03:25:55Z · 10 days · 14.52 R |
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

### 3. [AT2026abys](https://www.wis-tns.org/object/2026abys) near Caldwell 7 (C7)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 7 (C7) as this object's host. The 0.62232° (37.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T04:35:54Z · 0 days · 18.08 wide |
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

### 4. [AT2026abbx](https://www.wis-tns.org/object/2026abbx) near Lynds Dark Nebula 161 (LDN161)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 89/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 161 (LDN161) as this object's host. The 0.37662° (22.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | Nova |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-08T18:57:36Z · 9 days · 12.6 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3631....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR3631....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 161 (LDN161)** · `LDN161` |
| Catalog display name | Lynds Dark Nebula 161 (LDN161) |
| Type / constellation | Dark nebula · Sagittarius |
| Catalog magnitude / angular size | — · 23.16′ × 23.16′ |
| Distance | — |
| Separation | 0.37662° · 22.60′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤16.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026abbx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=268.02833%20-23.72242&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026abuf](https://www.wis-tns.org/object/2026abuf) near Wild Duck cluster

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 85/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Wild Duck cluster as this object's host. The 0.20167° (12.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-08-29T16:27:06Z · 19 days · 17.89 Clear |
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
| Subject | **Wild Duck cluster** · `CR391` |
| Catalog display name | Wild Duck cluster |
| Type / constellation | Open cluster · Scutum |
| Catalog magnitude / angular size | 5.8 · 9′ × 9′ |
| Distance | 1.877 kpc |
| Separation | 0.20167° · 12.10′ |
| Catalog description | The Wild Duck Cluster is an open cluster of stars in the constellation Scutum. It was discovered by Gottfried Kirch in 1681. Charles Messier included it in his catalogue of diffuse objects in 1764. Its popular name derives from the brighter stars forming a triangle which could resemble a flying flock of ducks. The cluster is located just to the east of the Scutum Star Cloud midpoint. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abuf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=282.749417%20-6.066639&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
