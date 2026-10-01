# TNS transient opportunity review — 2026-09-30

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `7403569da0e3a81f`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 4 approve, 1 hold, 0 reject
- 36 eligible opportunities before the top-5 review cap
- 1082 staged rows collapsed to 1040 unique TNS objects (42 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026adgl](https://www.wis-tns.org/object/2026adgl) | transient_candidate | 1 | 17.4 | Great Nebula in Andromeda (Galaxy) | 0.04483° | near-field match | 100 | approve |
| urgent | [SN2026acjs](https://www.wis-tns.org/object/2026acjs) | SN II | 10 | 17.87 | IC4784 (Galaxy) | 0.44672° | near-field match | 97 | approve |
| urgent | [AT2026acwl](https://www.wis-tns.org/object/2026acwl) | transient_candidate | 8 | 16.6 | NGC 3226 (Galaxy) | 0.17409° | near-field match | 95 | approve |
| urgent | [AT2026adgn](https://www.wis-tns.org/object/2026adgn) | transient_candidate | 1 | 14.51 | IC 1419 (Galaxy) | 1.22724° | near-field match | 93 | hold |
| urgent | [AT2026acwi](https://www.wis-tns.org/object/2026acwi) | transient_candidate | 8 | 16.45 | Messier 96 (M96) (Galaxy) | 0.85972° | near-field match | 92 | approve |

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
| Discovery | 2026-09-29T18:17:05Z · 1 days · 17.4 Clear |
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
| Separation | 0.04483° · 2.69′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.652667%2041.230611&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026acjs](https://www.wis-tns.org/object/2026acjs) near IC4784

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 97/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4784 as this object's host. The 0.44672° (26.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.0155 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-20T09:28:57Z · 10 days · 17.87 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3796....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3796....1O/abstract) |
| Classification references | [2026TNSCR3842....1R](https://ui.adsabs.harvard.edu/abs/2026TNSCR3842....1R/abstract) |
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
| Separation | 0.44672° · 26.80′ |
| Catalog description | considerably faint, small in angular size, round, brighter middle, or in the middle |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=283.6349108%20-62.8586925&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026acwl](https://www.wis-tns.org/object/2026acwl) near NGC 3226

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3226 as this object's host. The 0.17409° (10.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 8 days · 16.6 Other |
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
| Subject | **NGC 3226** · `NGC 3226` |
| Catalog display name | NGC 3226 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 12.95 · 3.13′ × 2.26′ |
| Distance | — |
| Separation | 0.17409° · 10.45′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acwl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.6789%2019.8765&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026adgn](https://www.wis-tns.org/object/2026adgn) near IC 1419

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 93/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.22724° (73.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T17:51:06Z · 1 days · 14.51 Clear |
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
| Subject | **IC 1419** · `IC 1419` |
| Catalog display name | NGC 1198 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.54′ × 0.3′ |
| Distance | — |
| Separation | 1.22724° · 73.63′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adgn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.942875%20-11.132722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026acwi](https://www.wis-tns.org/object/2026acwi) near Messier 96 (M96)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 92/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 96 (M96) as this object's host. The 0.85972° (51.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 8 days · 16.45 Other |
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
| Subject | **Messier 96 (M96)** · `M96` |
| Catalog display name | Messier 96 (M96) |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 9.2 · 6′ × 4′ |
| Distance | 11,650.853 kpc |
| Separation | 0.85972° · 51.58′ |
| Catalog description | Messier 96 is an intermediate spiral galaxy about 31 million light-years away in the constellation Leo. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acwi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=162.3456%2011.2345&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
