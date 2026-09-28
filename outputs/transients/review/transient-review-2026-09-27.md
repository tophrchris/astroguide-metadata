# TNS transient opportunity review — 2026-09-27

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `919eb23a2d3f84fd`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 5 urgent, 0 watch, 0 expired
- Recommendations: 5 approve, 0 hold, 0 reject
- 28 eligible opportunities before the top-5 review cap
- 1088 staged rows collapsed to 1032 unique TNS objects (56 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026aaiv](https://www.wis-tns.org/object/2026aaiv) | SN Ia | 26 | 17.32 | Caldwell 30 (Galaxy) | 0.00802° | near-field match | 100 | approve |
| urgent | [SN2026acjs](https://www.wis-tns.org/object/2026acjs) | SN II | 7 | 17.87 | IC4784 (Galaxy) | 0.44672° | near-field match | 100 | approve |
| urgent | [AT2026acuq](https://www.wis-tns.org/object/2026acuq) | transient_candidate | 5 | 15 | NGC797 (Galaxy) | 0.19644° | near-field match | 100 | approve |
| urgent | [AT2026acwi](https://www.wis-tns.org/object/2026acwi) | transient_candidate | 5 | 16.45 | Messier 96 (M96) (Galaxy) | 0.85972° | near-field match | 100 | approve |
| urgent | [AT2026acwl](https://www.wis-tns.org/object/2026acwl) | transient_candidate | 5 | 16.6 | NGC 3226 (Galaxy) | 0.17409° | near-field match | 100 | approve |

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
| Discovery | 2026-09-01T11:23:32Z · 26 days · 17.32 orange |
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

### 2. [SN2026acjs](https://www.wis-tns.org/object/2026acjs) near IC4784

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4784 as this object's host. The 0.44672° (26.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.0155 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-20T09:28:57Z · 7 days · 17.87 L |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=283.6349108%20-62.8586925&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [AT2026acuq](https://www.wis-tns.org/object/2026acuq) near NGC797

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 0.19644° (11.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 5 days · 15 Other |
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

### 4. [AT2026acwi](https://www.wis-tns.org/object/2026acwi) near Messier 96 (M96)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 96 (M96) as this object's host. The 0.85972° (51.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 5 days · 16.45 Other |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acwi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=162.3456%2011.2345&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026acwl](https://www.wis-tns.org/object/2026acwl) near NGC 3226

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3226 as this object's host. The 0.17409° (10.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-22T00:00:00Z · 5 days · 16.6 Other |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acwl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.6789%2019.8765&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
