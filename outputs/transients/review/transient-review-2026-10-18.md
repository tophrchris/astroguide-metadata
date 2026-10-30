# TNS transient opportunity review — 2026-10-18

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `90f98d1982380740`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 5 review opportunities: 2 urgent, 3 watch, 0 expired
- Recommendations: 2 approve, 3 hold, 0 reject
- 14 eligible opportunities before the top-5 review cap
- 619 staged rows collapsed to 583 unique TNS objects (36 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [AT2026afpx](https://www.wis-tns.org/object/2026afpx) | transient_candidate | 3 | 18.44 | NGC2822 (Galaxy) | 1.08397° | near-field match | 83 | approve |
| urgent | [SN2026aesj](https://www.wis-tns.org/object/2026aesj) | SN Ia | 11 | 18.43 | Headphone nebula (Planetary nebula) | 1.79431° | near-field match | 72 | approve |
| watch | [SN2026acyb](https://www.wis-tns.org/object/2026acyb) | SN Ia | 28 | 19.45 | IC 1403 (Galaxy) | 0.18470° | near-field match | 100 | hold |
| watch | [AT2026afoh](https://www.wis-tns.org/object/2026afoh) | transient_candidate | 4 | 19.38 | Bode's Galaxy (Galaxy) | 0.05271° | near-field match | 93 | hold |
| watch | [AT2026afol](https://www.wis-tns.org/object/2026afol) | transient_candidate | 4 | 19.04 | Caldwell 101 (C101) (Galaxy) | 0.19075° | near-field match | 93 | hold |

## Candidate dossiers

### 1. [AT2026afpx](https://www.wis-tns.org/object/2026afpx) near NGC2822

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2822 as this object's host. The 1.08397° (65.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-15T02:21:21Z · 3 days · 18.44 orange |
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
| Subject | **NGC2822** · `NGC2822` |
| Catalog display name | NGC2822 |
| Type / constellation | Galaxy · Carina |
| Catalog magnitude / angular size | 11.4 · 3.96′ × 2.72′ |
| Distance | — |
| Separation | 1.08397° · 65.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afpx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=136.336623%20-70.453035&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026aesj](https://www.wis-tns.org/object/2026aesj) near Headphone nebula

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Headphone nebula as this object's host. The 1.79431° (107.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.019095 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T13:27:06Z · 11 days · 18.43 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4031....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4031....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Headphone nebula** · `JnEr1` |
| Catalog display name | Headphone nebula |
| Type / constellation | Planetary nebula · Lyn |
| Catalog magnitude / angular size | — · 6.3′ × 6.3′ |
| Distance | 1,600 ly |
| Separation | 1.79431° · 107.66′ |
| Catalog description | Jones-Emberson 1, also known as the Headphone Nebula, is a 14th magnitude planetary nebula in the constellation Lynx at a distance of 1600 light years. It is a larger planetary with low surface brightness. The 16.8-magnitude central star is a very blue white dwarf. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aesj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.1667664%2054.6120616&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026acyb](https://www.wis-tns.org/object/2026acyb) near IC 1403

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 100/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1403 as this object's host. The 0.18470° (11.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.059 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-20T05:57:46Z · 28 days · 19.45 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3890....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR3890....1R/abstract) |
| Classification references | [2026TNSCR3921....1F](https://ui.adsabs.harvard.edu/abs/2026TNSCR3921....1F/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1403** · `IC 1403` |
| Catalog display name | IC 1613 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.49′ × 0.35′ |
| Distance | — |
| Separation | 0.18470° · 11.08′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1403 has the different designation IC 1613 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026acyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=327.7320721%20-2.863965&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026afoh](https://www.wis-tns.org/object/2026afoh) near Bode's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Bode's Galaxy as this object's host. The 0.05271° (3.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T22:15:23Z · 4 days · 19.38 Clear |
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
| Subject | **Bode's Galaxy** · `M81` |
| Catalog display name | Bode's Galaxy |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 6.9 · 21′ × 10′ |
| Distance | 3,679.217 kpc |
| Separation | 0.05271° · 3.16′ |
| Catalog description | Messier 81 (also known as NGC 3031 or Bode's Galaxy) is a grand design spiral galaxy about 12 million light-years away in the constellation Ursa Major. It has a D25 isophotal diameter of 29.44 kiloparsecs (96,000 light-years). Because of its relative proximity to the Milky Way galaxy, large size, and active galactic nucleus (which harbors a 70 million M☉ supermassive black hole), Messier 81 has been studied extensively by professional astronomers. The galaxy's large size and relatively high brightness also makes it a popular target for amateur astronomers. In late February 2022, astronomers reported that M81 may be the source of FRB 20200120E, a repeating fast radio burst. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afoh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=149.003292%2069.104222&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026afol](https://www.wis-tns.org/object/2026afol) near Caldwell 101 (C101)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 101 (C101) as this object's host. The 0.19075° (11.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T18:43:07Z · 4 days · 19.04 orange |
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
| Subject | **Caldwell 101 (C101)** · `C101` |
| Catalog display name | Caldwell 101 (C101) |
| Type / constellation | Galaxy · Pavo |
| Catalog magnitude / angular size | 9 · 16′ × 10′ |
| Distance | — |
| Separation | 0.19075° · 11.45′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afol) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=287.40082%20-63.64733&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
