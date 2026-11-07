# TNS transient opportunity review — 2026-11-06

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `fd99fc9c4f2c327a`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 284 review opportunities: 22 urgent, 262 watch, 0 expired
- Recommendations: 18 approve, 266 hold, 0 reject
- 284 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 667 staged rows collapsed to 605 unique TNS objects (62 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026aguw](https://www.wis-tns.org/object/2026aguw) | SN Ia | 12 | 17.67 | IC 4747 (Galaxy) | 0.23524° | near-field match | 100 | hold |
| urgent | [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) | SN Ia | 4 | 16.1 | NGC4216 (Galaxy) | 0.39324° | near-field match | 100 | approve |
| urgent | [SN2026ahvu](https://www.wis-tns.org/object/2026ahvu) | SN Ia | 4 | 17.06 | NGC1433 (Galaxy) | 0.01649° | near-field match | 100 | approve |
| urgent | [SN2026agwb](https://www.wis-tns.org/object/2026agwb) | SN Ia | 11 | 17.8 | NGC134 (Galaxy) | 0.96564° | near-field match | 97 | approve |
| urgent | [SN2026agwm](https://www.wis-tns.org/object/2026agwm) | SN Ia | 10 | 18.33 | IC4931 (Galaxy) | 0.65936° | near-field match | 97 | approve |
| urgent | [AT2026ahxs](https://www.wis-tns.org/object/2026ahxs) | transient_candidate | 9 | 17.5 | IC 1777 (Galaxy) | 0.07735° | near-field match | 95 | hold |
| urgent | [SN2026agpv](https://www.wis-tns.org/object/2026agpv) | SN II | 14 | 17.47 | NGC636 (Galaxy) | 1.88833° | near-field match | 90 | approve |
| urgent | [SN2026agvs](https://www.wis-tns.org/object/2026agvs) | SN IIb | 12 | 18.35 | IC2104 (Galaxy) | 1.31532° | near-field match | 90 | approve |
| urgent | [SN2026agzw](https://www.wis-tns.org/object/2026agzw) | SN Ia | 9 | 18.09 | IC1657 (Galaxy) | 1.30068° | near-field match | 90 | approve |
| urgent | [AT2026ahyf](https://www.wis-tns.org/object/2026ahyf) | transient_candidate | 3 | 18.49 | IC 2405 (Galaxy) | 0.45056° | near-field match | 90 | hold |
| urgent | [AT2026ahzh](https://www.wis-tns.org/object/2026ahzh) | transient_candidate | 3 | 18.28 | NGC3665 (Galaxy) | 0.91138° | near-field match | 90 | approve |
| urgent | [AT2026aicq](https://www.wis-tns.org/object/2026aicq) | transient_candidate | 2 | 18.48 | IC 369 (Galaxy) | 0.91864° | near-field match | 90 | hold |
| urgent | [AT2026aikg](https://www.wis-tns.org/object/2026aikg) | transient_candidate | 3 | 17.95 | NGC4414 (Galaxy) | 0.85966° | near-field match | 90 | approve |
| urgent | [SN2026ahoe](https://www.wis-tns.org/object/2026ahoe) | SN Ia | 6 | 18.05 | Caldwell 87 (C87) (Globular cluster) | 1.22814° | near-field match | 88 | approve |
| urgent | [AT2026ahod](https://www.wis-tns.org/object/2026ahod) | transient_candidate | 6 | 18.34 | IC5176 (Galaxy) | 1.17052° | near-field match | 83 | approve |
| urgent | [AT2026ahrc](https://www.wis-tns.org/object/2026ahrc) | transient_candidate | 6 | 18.02 | IC396 (Galaxy) | 1.65285° | near-field match | 83 | approve |
| urgent | [AT2026ahxu](https://www.wis-tns.org/object/2026ahxu) | transient_candidate | 4 | 17.94 | IC4831 (Galaxy) | 1.39323° | near-field match | 83 | approve |
| urgent | [AT2026ahqt](https://www.wis-tns.org/object/2026ahqt) | transient_candidate | 8 | 18.3 | IC5250 (Galaxy) | 0.89448° | near-field match | 82 | approve |
| urgent | [AT2026ahqx](https://www.wis-tns.org/object/2026ahqx) | transient_candidate | 8 | 17.16 | NGC1559 (Galaxy) | 0.93510° | near-field match | 82 | approve |
| urgent | [AT2026aict](https://www.wis-tns.org/object/2026aict) | transient_candidate | 2 | 18.31 | Dumbbell Nebula (Planetary nebula) | 0.76955° | near-field match | 80 | approve |
| urgent | [AT2026agtx](https://www.wis-tns.org/object/2026agtx) | transient_candidate | 12 | 18.44 | IC4808 (Galaxy) | 1.73758° | near-field match | 75 | approve |
| urgent | [AT2026agvn](https://www.wis-tns.org/object/2026agvn) | transient_candidate | 12 | 18.12 | NGC3486 (Galaxy) | 1.16846° | near-field match | 75 | approve |
| watch | [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) | SN II | 5 | 18.71 | IC 3 (Spiral galaxy) | 0.47363° | near-field match | 95 | hold |
| watch | [AT2026aikp](https://www.wis-tns.org/object/2026aikp) | transient_candidate | 2 | 19.14 | Great Nebula in Andromeda (Galaxy) | 0.10297° | near-field match | 93 | hold |
| watch | [SN2026afqk](https://www.wis-tns.org/object/2026afqk) | SN Ia | 20 | 19.37 | IC240 (Nebula) | 0.22339° | near-field match | 90 | hold |
| watch | [SN2026ahna](https://www.wis-tns.org/object/2026ahna) | SN Ia | 9 | 18.9 | IC1933 (Galaxy) | 0.88139° | near-field match | 87 | hold |
| watch | [AT2026ahyy](https://www.wis-tns.org/object/2026ahyy) | transient_candidate | 9 | 19.41 | IC 1996 (Galaxy) | 0.23846° | near-field match | 85 | hold |
| watch | [SN2026afkh](https://www.wis-tns.org/object/2026afkh) | SN Ia | 23 | 19.36 | IC5309 (Galaxy) | 1.91597° | near-field match | 80 | hold |
| watch | [SN2026afql](https://www.wis-tns.org/object/2026afql) | SN Ia | 20 | 18.74 | IC449 (Galaxy) | 1.98969° | near-field match | 80 | hold |
| watch | [SN2026aguc](https://www.wis-tns.org/object/2026aguc) | SN Ia-91T-like | 12 | 19.18 | IC382 (Galaxy) | 1.38071° | near-field match | 80 | hold |
| watch | [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) | transient_candidate | 7 | 19.31 | IC 2017 (Galaxy) | 0.36966° | near-field match | 80 | hold |
| watch | [AT2026ahvg](https://www.wis-tns.org/object/2026ahvg) | transient_candidate | 6 | 19.39 | IC5152 (Galaxy) | 0.90775° | near-field match | 80 | hold |
| watch | [AT2026ahyj](https://www.wis-tns.org/object/2026ahyj) | transient_candidate | 4 | 19.41 | NGC3646 (Galaxy) | 0.80341° | near-field match | 80 | hold |
| watch | [AT2026ahyq](https://www.wis-tns.org/object/2026ahyq) | transient_candidate | 3 | 18.91 | NGC4125 (Galaxy) | 0.59101° | near-field match | 80 | hold |
| watch | [AT2026ahzb](https://www.wis-tns.org/object/2026ahzb) | transient_candidate | 3 | 18.52 | IC 3107 (Galaxy) | 0.67614° | near-field match | 80 | hold |
| watch | [AT2026ahzc](https://www.wis-tns.org/object/2026ahzc) | transient_candidate | 3 | 19.04 | IC5065 (Galaxy) | 0.96030° | near-field match | 80 | hold |
| watch | [AT2026aijt](https://www.wis-tns.org/object/2026aijt) | transient_candidate | 3 | 19.16 | IC 673 (Galaxy) | 0.58117° | near-field match | 80 | hold |
| watch | [AT2026aguv](https://www.wis-tns.org/object/2026aguv) | transient_candidate | 12 | 18.78 | NGC2404 (HII) | 0.01585° | near-field match | 75 | hold |
| watch | [AT2026ahqz](https://www.wis-tns.org/object/2026ahqz) | transient_candidate | 6 | 18.84 | Lynds Bright Nebula 221 (LBN221) (HII) | 0.23961° | near-field match | 75 | hold |
| watch | [AT2026ahnc](https://www.wis-tns.org/object/2026ahnc) | transient_candidate | 7 | 19.41 | IC 1799 (Galaxy) | 1.38869° | near-field match | 73 | hold |
| watch | [AT2026ahqu](https://www.wis-tns.org/object/2026ahqu) | transient_candidate | 6 | 18.85 | IC5267 (Galaxy) | 1.68442° | near-field match | 73 | hold |
| watch | [AT2026ahtg](https://www.wis-tns.org/object/2026ahtg) | transient_candidate | 5 | 19.25 | IC1953 (Galaxy) | 1.01025° | near-field match | 73 | hold |
| watch | [AT2026ahuu](https://www.wis-tns.org/object/2026ahuu) | transient_candidate | 4 | 18.69 | IC449 (Galaxy) | 1.92939° | near-field match | 73 | hold |
| watch | [AT2026ahuv](https://www.wis-tns.org/object/2026ahuv) | transient_candidate | 4 | 19.06 | NGC2985 (Galaxy) | 1.76577° | near-field match | 73 | hold |
| watch | [AT2026ahxp](https://www.wis-tns.org/object/2026ahxp) | transient_candidate | 6 | 19.27 | IC5141 (Galaxy) | 1.51041° | near-field match | 73 | hold |
| watch | [AT2026ahys](https://www.wis-tns.org/object/2026ahys) | transient_candidate | 3 | 18.52 | NGC3998 (Galaxy) | 1.18163° | near-field match | 73 | hold |
| watch | [AT2026ahze](https://www.wis-tns.org/object/2026ahze) | transient_candidate | 3 | 18.71 | NGC797 (Galaxy) | 1.92283° | near-field match | 73 | hold |
| watch | [AT2026ahzg](https://www.wis-tns.org/object/2026ahzg) | transient_candidate | 3 | 18.77 | IC2152 (Galaxy) | 1.50615° | near-field match | 73 | hold |
| watch | [AT2026ahzi](https://www.wis-tns.org/object/2026ahzi) | transient_candidate | 3 | 19.05 | IC2166 (Galaxy) | 1.06003° | near-field match | 73 | hold |
| watch | [AT2026aiaf](https://www.wis-tns.org/object/2026aiaf) | transient_candidate | 3 | 19.19 | Messier 32 (Galaxy) | 1.66908° | near-field match | 73 | hold |
| watch | [AT2026aiag](https://www.wis-tns.org/object/2026aiag) | transient_candidate | 3 | 19.72 | IC 2814 (Galaxy) | 0.21281° | near-field match | 73 | hold |
| watch | [AT2026aiaz](https://www.wis-tns.org/object/2026aiaz) | transient_candidate | 4 | 19.46 | NGC2655 (Galaxy) | 1.67391° | near-field match | 73 | hold |
| watch | [AT2026aijg](https://www.wis-tns.org/object/2026aijg) | transient_candidate | 0 | 19.19 | IC 5016 (Galaxy) | 1.00177° | near-field match | 73 | hold |
| watch | [AT2026aijv](https://www.wis-tns.org/object/2026aijv) | transient_candidate | 3 | 18.99 | NGC3521 (Galaxy) | 1.27193° | near-field match | 73 | hold |
| watch | [AT2026aguy](https://www.wis-tns.org/object/2026aguy) | transient_candidate | 13 | 18.82 | NGC 2207 / IC 2163 (Galaxy) | 0.60878° | near-field match | 72 | hold |
| watch | [AT2026ahaj](https://www.wis-tns.org/object/2026ahaj) | transient_candidate | 9 | 19.21 | NGC1398 (Galaxy) | 0.30038° | near-field match | 72 | hold |
| watch | [AT2026ahnl](https://www.wis-tns.org/object/2026ahnl) | transient_candidate | 9 | 19.39 | NGC2217 (Galaxy) | 0.79462° | near-field match | 72 | hold |
| watch | [AT2026ahtt](https://www.wis-tns.org/object/2026ahtt) | transient_candidate | 8 | 18.64 | NGC2559 (Galaxy) | 0.63978° | near-field match | 72 | hold |
| watch | [AT2026aica](https://www.wis-tns.org/object/2026aica) | transient_candidate | 9 | 18.78 | IC1914 (Galaxy) | 0.56142° | near-field match | 72 | hold |
| watch | [SN2026agpk](https://www.wis-tns.org/object/2026agpk) | SN II | 14 | 18.85 | NGC2399 (Nebula) | 1.83747° | near-field match | 70 | hold |
| watch | [SN2026ahmz](https://www.wis-tns.org/object/2026ahmz) | SN II | 9 | 19.33 | IC2084 (Nebula) | 1.11286° | near-field match | 70 | hold |
| watch | [AT2026ahya](https://www.wis-tns.org/object/2026ahya) | transient_candidate | 3 | 19.4 | NGC1655 (Nebula) | 0.84874° | near-field match | 70 | hold |
| watch | [AT2026agvt](https://www.wis-tns.org/object/2026agvt) | transient_candidate | 19 | 18.75 | NGC3610 (Galaxy) | 1.92890° | near-field match | 65 | hold |
| watch | [AT2026agwa](https://www.wis-tns.org/object/2026agwa) | transient_candidate | 12 | 18.08 | IC2988 (Nebula) | 1.54834° | near-field match | 65 | hold |
| watch | [AT2026ahab](https://www.wis-tns.org/object/2026ahab) | transient_candidate | 9 | 19.2 | IC 530 (Galaxy) | 1.84652° | near-field match | 65 | hold |
| watch | [AT2026ahaq](https://www.wis-tns.org/object/2026ahaq) | transient_candidate | 9 | 21.91 | NGC1532 (Galaxy) | 0.03031° | near-field match | 65 | hold |
| watch | [AT2026ahch](https://www.wis-tns.org/object/2026ahch) | transient_candidate | 8 | 19.49 | NGC1792 (Galaxy) | 1.51662° | near-field match | 65 | hold |
| watch | [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) | transient_candidate | 8 | 19.41 | IC1933 (Galaxy) | 1.58832° | near-field match | 65 | hold |
| watch | [AT2026ahss](https://www.wis-tns.org/object/2026ahss) | transient_candidate | 9 | 19.4 | IC 1913 (Galaxy) | 1.87107° | near-field match | 65 | hold |
| watch | [AT2026ahun](https://www.wis-tns.org/object/2026ahun) | transient_candidate | 8 | 22.34 | IC 1481 (Galaxy) | 0.10755° | near-field match | 65 | hold |
| watch | [AT2026ahxr](https://www.wis-tns.org/object/2026ahxr) | transient_candidate | 3 | 18.86 | Wolf-Lundmark-Melotte (Galaxy) | 1.11363° | near-field match | 65 | hold |
| watch | [AT2026ahxx](https://www.wis-tns.org/object/2026ahxx) | transient_candidate | 12 | 19.86 | IC310 (Galaxy) | 0.17679° | near-field match | 65 | hold |
| watch | [AT2026ahyr](https://www.wis-tns.org/object/2026ahyr) | transient_candidate | 19 | 19.44 | NGC3610 (Galaxy) | 1.92150° | near-field match | 65 | hold |
| watch | [AT2026aiju](https://www.wis-tns.org/object/2026aiju) | transient_candidate | 8 | 19.02 | IC630 (Galaxy) | 1.80723° | near-field match | 65 | hold |
| watch | [AT2026ahra](https://www.wis-tns.org/object/2026ahra) | transient_candidate | 6 | 19.18 | NGC796 (Open cluster) | 1.40753° | near-field match | 63 | hold |
| watch | [AT2026ahrd](https://www.wis-tns.org/object/2026ahrd) | transient_candidate | 5 | 18.58 | NGC2117 (Open cluster) | 1.91418° | near-field match | 63 | hold |
| watch | [AT2026ahti](https://www.wis-tns.org/object/2026ahti) | transient_candidate | 5 | 18.69 | Melotte 53 (MEL53) (Globular cluster) | 1.56930° | near-field match | 63 | hold |
| watch | [AT2026ahvx](https://www.wis-tns.org/object/2026ahvx) | transient_candidate | 3 | 19.25 | Caldwell 1 (C1) (Open cluster) | 1.60616° | near-field match | 63 | hold |
| watch | [AT2026ahyn](https://www.wis-tns.org/object/2026ahyn) | transient_candidate | 3 | 21 | NGC272 (Open cluster) | 0.21538° | near-field match | 63 | hold |
| watch | [AT2026ahzj](https://www.wis-tns.org/object/2026ahzj) | transient_candidate | 3 | 18.72 | NGC2879 (Nebula) | 1.72703° | near-field match | 63 | hold |
| watch | [AT2026aiba](https://www.wis-tns.org/object/2026aiba) | transient_candidate | 4 | 19 | NGC2404 (HII) | 1.36391° | near-field match | 63 | hold |
| watch | [AT2026aibq](https://www.wis-tns.org/object/2026aibq) | transient_candidate | 2 | 19.07 | NGC6669 (Nebula) | 1.81749° | near-field match | 63 | hold |
| watch | [AT2026aiep](https://www.wis-tns.org/object/2026aiep) | transient_candidate | 2 | 19.17 | IC5194 (Nebula) | 1.65298° | near-field match | 63 | hold |
| watch | [AT2026aihy](https://www.wis-tns.org/object/2026aihy) | transient_candidate | 1 | 19.5 | NGC56 (Nebula) | 1.97482° | near-field match | 63 | hold |
| watch | [AT2026aija](https://www.wis-tns.org/object/2026aija) | transient_candidate | 0 | 19.1 | NGC796 (Open cluster) | 1.18846° | near-field match | 63 | hold |
| watch | [SN2026afqd](https://www.wis-tns.org/object/2026afqd) | SN IIP | 20 | 19.18 | Lynds Bright Nebula 556 (LBN556) (HII) | 1.09316° | near-field match | 62 | hold |
| watch | [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) | transient_candidate | 3 | 19.39 | Lynds Bright Nebula 718 (LBN718) (HII) | 0.53253° | near-field match | 62 | hold |
| watch | [AT2026aiap](https://www.wis-tns.org/object/2026aiap) | transient_candidate | 3 | 18.98 | Lynds Bright Nebula 437 (LBN437) (HII) | 0.83711° | near-field match | 62 | hold |
| watch | [AT2026ahsf](https://www.wis-tns.org/object/2026ahsf) | transient_candidate | 7 | 20.36 | IC1892 (Galaxy) | 0.43441° | near-field match | 60 | hold |
| watch | [AT2026ahsl](https://www.wis-tns.org/object/2026ahsl) | transient_candidate | 7 | 20.07 | NGC1300 (Galaxy) | 0.61843° | near-field match | 60 | hold |
| watch | [AT2026ahtr](https://www.wis-tns.org/object/2026ahtr) | transient_candidate | 5 | 21.33 | IC163 (Galaxy) | 0.83764° | near-field match | 60 | hold |
| watch | [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) | transient_candidate | 5 | 19.59 | IC1933 (Galaxy) | 0.59209° | near-field match | 60 | hold |
| watch | [AT2026ahup](https://www.wis-tns.org/object/2026ahup) | transient_candidate | 7 | 22.12 | NGC488 (Galaxy) | 0.66908° | near-field match | 60 | hold |
| watch | [AT2026ahwx](https://www.wis-tns.org/object/2026ahwx) | transient_candidate | 7 | 22.16 | Caldwell 51 (C51) (Galaxy) | 0.76630° | near-field match | 60 | hold |
| watch | [AT2026ahwz](https://www.wis-tns.org/object/2026ahwz) | transient_candidate | 7 | 22.01 | NGC741 (Galaxy) | 0.95545° | near-field match | 60 | hold |
| watch | [AT2026ahxf](https://www.wis-tns.org/object/2026ahxf) | transient_candidate | 5 | 22.12 | IC 1746 (Galaxy) | 0.76507° | near-field match | 60 | hold |
| watch | [AT2026ahye](https://www.wis-tns.org/object/2026ahye) | transient_candidate | 3 | 20.17 | IC2421 (Galaxy) | 0.96852° | near-field match | 60 | hold |
| watch | [AT2026aiax](https://www.wis-tns.org/object/2026aiax) | transient_candidate | 7 | 22.27 | NGC1527 (Galaxy) | 0.49618° | near-field match | 60 | hold |
| watch | [AT2026aicj](https://www.wis-tns.org/object/2026aicj) | transient_candidate | 2 | 20.1 | IC1531 (Galaxy) | 0.49233° | near-field match | 60 | hold |
| watch | [AT2026aiij](https://www.wis-tns.org/object/2026aiij) | transient_candidate | 0 | 23.51 | IC2000 (Galaxy) | 0.81942° | near-field match | 60 | hold |
| watch | [AT2026aike](https://www.wis-tns.org/object/2026aike) | transient_candidate | 0 | 22.75 | NGC1543 (Galaxy) | 0.28536° | near-field match | 60 | hold |
| watch | [AT2026aikf](https://www.wis-tns.org/object/2026aikf) | transient_candidate | 0 | 21.83 | NGC1543 (Galaxy) | 0.39139° | near-field match | 60 | hold |
| watch | [AT2026aiki](https://www.wis-tns.org/object/2026aiki) | transient_candidate | 0 | 20.27 | IC 230 (Galaxy) | 0.98290° | near-field match | 60 | hold |
| watch | [SN2026agpt](https://www.wis-tns.org/object/2026agpt) | SN Ia | 17 | 20.26 | IC353 (Nebula) | 0.25824° | near-field match | 57 | hold |
| watch | [AT2026agxx](https://www.wis-tns.org/object/2026agxx) | transient_candidate | 10 | 19.03 | NGC7134 (Nebula) | 1.77788° | near-field match | 55 | hold |
| watch | [AT2026ahfn](https://www.wis-tns.org/object/2026ahfn) | transient_candidate | 7 | 19.21 | Lynds Bright Nebula 870 (LBN870) (HII) | 1.01310° | near-field match | 55 | hold |
| watch | [AT2026ahrb](https://www.wis-tns.org/object/2026ahrb) | transient_candidate | 33 | 13 | IC1788 (Galaxy) | 0.89675° | near-field match | 55 | hold |
| watch | [AT2026ahsh](https://www.wis-tns.org/object/2026ahsh) | transient_candidate | 9 | 19.05 | NGC1498 (Open cluster) | 1.89281° | near-field match | 55 | hold |
| watch | [AT2026ahxo](https://www.wis-tns.org/object/2026ahxo) | transient_candidate | 3 | 18.88 | Lynds Bright Nebula 484 (LBN484) (HII) | 1.59750° | near-field match | 55 | hold |
| watch | [AT2026ahxq](https://www.wis-tns.org/object/2026ahxq) | transient_candidate | 3 | 19.18 | Lynds Bright Nebula 100 (LBN100) (HII) | 1.77430° | near-field match | 55 | hold |
| watch | [AT2026aibu](https://www.wis-tns.org/object/2026aibu) | transient_candidate | 13 | 19.47 | IC640 (Nebula) | 1.43879° | near-field match | 55 | hold |
| watch | [AT2026agyh](https://www.wis-tns.org/object/2026agyh) | transient_candidate | 18 | 19.13 | Lynds Bright Nebula 1024 (LBN1024) (HII) | 0.77188° | near-field match | 54 | hold |
| watch | [AT2026ahho](https://www.wis-tns.org/object/2026ahho) | transient_candidate | 7 | 21.9 | IC1495 (Galaxy) | 1.70871° | near-field match | 53 | hold |
| watch | [AT2026ahif](https://www.wis-tns.org/object/2026ahif) | transient_candidate | 7 | 20.62 | IC2000 (Galaxy) | 1.45000° | near-field match | 53 | hold |
| watch | [AT2026ahiv](https://www.wis-tns.org/object/2026ahiv) | transient_candidate | 7 | 22.17 | IC1495 (Galaxy) | 1.93793° | near-field match | 53 | hold |
| watch | [AT2026ahom](https://www.wis-tns.org/object/2026ahom) | transient_candidate | 6 | 23.23 | IC2000 (Galaxy) | 1.66970° | near-field match | 53 | hold |
| watch | [AT2026ahoo](https://www.wis-tns.org/object/2026ahoo) | transient_candidate | 6 | 23.17 | IC2000 (Galaxy) | 1.20295° | near-field match | 53 | hold |
| watch | [AT2026ahop](https://www.wis-tns.org/object/2026ahop) | transient_candidate | 6 | 22.66 | NGC1527 (Galaxy) | 1.32446° | near-field match | 53 | hold |
| watch | [AT2026ahor](https://www.wis-tns.org/object/2026ahor) | transient_candidate | 6 | 23.03 | NGC1527 (Galaxy) | 1.72801° | near-field match | 53 | hold |
| watch | [AT2026ahos](https://www.wis-tns.org/object/2026ahos) | transient_candidate | 6 | 22.84 | IC2035 (Galaxy) | 1.49867° | near-field match | 53 | hold |
| watch | [AT2026ahpa](https://www.wis-tns.org/object/2026ahpa) | transient_candidate | 6 | 23.22 | IC2035 (Galaxy) | 1.23294° | near-field match | 53 | hold |
| watch | [AT2026ahpb](https://www.wis-tns.org/object/2026ahpb) | transient_candidate | 6 | 23.84 | NGC1527 (Galaxy) | 1.25162° | near-field match | 53 | hold |
| watch | [AT2026ahqo](https://www.wis-tns.org/object/2026ahqo) | transient_candidate | 7 | 20.04 | NGC524 (Galaxy) | 1.20553° | near-field match | 53 | hold |
| watch | [AT2026ahqw](https://www.wis-tns.org/object/2026ahqw) | transient_candidate | 7 | 21.24 | IC2035 (Galaxy) | 1.30880° | near-field match | 53 | hold |
| watch | [AT2026ahsg](https://www.wis-tns.org/object/2026ahsg) | transient_candidate | 7 | 20.33 | IC1914 (Galaxy) | 1.33500° | near-field match | 53 | hold |
| watch | [AT2026ahsw](https://www.wis-tns.org/object/2026ahsw) | transient_candidate | 7 | 20.18 | IC1812 (Galaxy) | 1.90241° | near-field match | 53 | hold |
| watch | [AT2026ahud](https://www.wis-tns.org/object/2026ahud) | transient_candidate | 5 | 20.6 | NGC1209 (Galaxy) | 1.34437° | near-field match | 53 | hold |
| watch | [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) | transient_candidate | 6 | 19.8 | IC1401 (Galaxy) | 1.09402° | near-field match | 53 | hold |
| watch | [AT2026ahuq](https://www.wis-tns.org/object/2026ahuq) | transient_candidate | 6 | 22.18 | NGC 2207 / IC 2163 (Galaxy) | 1.22452° | near-field match | 53 | hold |
| watch | [AT2026ahvb](https://www.wis-tns.org/object/2026ahvb) | transient_candidate | 5 | 20.07 | NGC 2207 / IC 2163 (Galaxy) | 1.81892° | near-field match | 53 | hold |
| watch | [AT2026ahvp](https://www.wis-tns.org/object/2026ahvp) | transient_candidate | 4 | 19.66 | NGC3359 (Galaxy) | 1.87119° | near-field match | 53 | hold |
| watch | [AT2026ahwu](https://www.wis-tns.org/object/2026ahwu) | transient_candidate | 7 | 22.47 | IC 1507 (Galaxy) | 1.63058° | near-field match | 53 | hold |
| watch | [AT2026ahxa](https://www.wis-tns.org/object/2026ahxa) | transient_candidate | 5 | 21.94 | IC 1481 (Galaxy) | 1.79834° | near-field match | 53 | hold |
| watch | [AT2026ahxb](https://www.wis-tns.org/object/2026ahxb) | transient_candidate | 5 | 22.15 | IC 1507 (Galaxy) | 1.18297° | near-field match | 53 | hold |
| watch | [AT2026ahyt](https://www.wis-tns.org/object/2026ahyt) | transient_candidate | 3 | 19.72 | IC2378 (Galaxy) | 1.23433° | near-field match | 53 | hold |
| watch | [AT2026ahyx](https://www.wis-tns.org/object/2026ahyx) | transient_candidate | 4 | 21.31 | IC 1931 (Galaxy) | 1.88856° | near-field match | 53 | hold |
| watch | [AT2026ahyz](https://www.wis-tns.org/object/2026ahyz) | transient_candidate | 7 | 20.14 | IC1650 (Galaxy) | 1.70126° | near-field match | 53 | hold |
| watch | [AT2026ahza](https://www.wis-tns.org/object/2026ahza) | transient_candidate | 5 | 20.03 | IC1997 (Galaxy) | 1.88878° | near-field match | 53 | hold |
| watch | [AT2026aian](https://www.wis-tns.org/object/2026aian) | transient_candidate | 3 | 21.33 | NGC720 (Galaxy) | 1.33774° | near-field match | 53 | hold |
| watch | [AT2026aiar](https://www.wis-tns.org/object/2026aiar) | transient_candidate | 3 | 20.11 | NGC 2207 / IC 2163 (Galaxy) | 1.27730° | near-field match | 53 | hold |
| watch | [AT2026aibw](https://www.wis-tns.org/object/2026aibw) | transient_candidate | 2 | 19.69 | NGC 2207 / IC 2163 (Galaxy) | 1.77222° | near-field match | 53 | hold |
| watch | [AT2026aick](https://www.wis-tns.org/object/2026aick) | transient_candidate | 2 | 19.75 | NGC7410 (Galaxy) | 1.11460° | near-field match | 53 | hold |
| watch | [AT2026aicm](https://www.wis-tns.org/object/2026aicm) | transient_candidate | 5 | 19.97 | IC 2039 (Galaxy) | 1.00001° | near-field match | 53 | hold |
| watch | [AT2026aicx](https://www.wis-tns.org/object/2026aicx) | transient_candidate | 3 | 20.09 | IC 21 (Galaxy) | 1.65570° | near-field match | 53 | hold |
| watch | [AT2026aiin](https://www.wis-tns.org/object/2026aiin) | transient_candidate | 3 | 20.59 | NGC1084 (Galaxy) | 1.58124° | near-field match | 53 | hold |
| watch | [AT2026aiiw](https://www.wis-tns.org/object/2026aiiw) | transient_candidate | 5 | 19.98 | IC5325 (Galaxy) | 1.36152° | near-field match | 53 | hold |
| watch | [AT2026aijo](https://www.wis-tns.org/object/2026aijo) | transient_candidate | 1 | 20.25 | NGC1055 (Galaxy) | 1.04239° | near-field match | 53 | hold |
| watch | [AT2026aijx](https://www.wis-tns.org/object/2026aijx) | transient_candidate | 0 | 21.8 | NGC1527 (Galaxy) | 1.48110° | near-field match | 53 | hold |
| watch | [AT2026aijz](https://www.wis-tns.org/object/2026aijz) | transient_candidate | 4 | 19.8 | IC522 (Galaxy) | 1.16708° | near-field match | 53 | hold |
| watch | [AT2026aika](https://www.wis-tns.org/object/2026aika) | transient_candidate | 3 | 20.36 | IC 1776 (Galaxy) | 1.83590° | near-field match | 53 | hold |
| watch | [AT2026aikd](https://www.wis-tns.org/object/2026aikd) | transient_candidate | 7 | 20.95 | NGC7606 (Galaxy) | 1.84563° | near-field match | 53 | hold |
| watch | [AT2026aikq](https://www.wis-tns.org/object/2026aikq) | transient_candidate | 3 | 20.18 | NGC 4150 (Galaxy) | 1.54182° | near-field match | 53 | hold |
| watch | [AT2026aikv](https://www.wis-tns.org/object/2026aikv) | transient_candidate | 3 | 20.5 | NGC628 (Galaxy) | 1.77250° | near-field match | 53 | hold |
| watch | [AT2026aikw](https://www.wis-tns.org/object/2026aikw) | transient_candidate | 3 | 20.06 | IC 186 A (Galaxy) | 1.01615° | near-field match | 53 | hold |
| watch | [AT2026aikx](https://www.wis-tns.org/object/2026aikx) | transient_candidate | 1 | 20.65 | IC 1730 (Galaxy) | 1.43755° | near-field match | 53 | hold |
| watch | [AT2026aikz](https://www.wis-tns.org/object/2026aikz) | transient_candidate | 2 | 19.88 | Arp 147 (Galaxy) | 1.07092° | near-field match | 53 | hold |
| watch | [AT2026ahph](https://www.wis-tns.org/object/2026ahph) | transient_candidate | 20 | 22.33 | IC 1481 (Galaxy) | 0.96485° | near-field match | 52 | hold |
| watch | [AT2026ahpp](https://www.wis-tns.org/object/2026ahpp) | transient_candidate | 8 | 21.96 | NGC 2207 / IC 2163 (Galaxy) | 0.84219° | near-field match | 52 | hold |
| watch | [AT2026ahse](https://www.wis-tns.org/object/2026ahse) | transient_candidate | 9 | 19.72 | IC1895 (Galaxy) | 0.30451° | near-field match | 52 | hold |
| watch | [AT2026ahsm](https://www.wis-tns.org/object/2026ahsm) | transient_candidate | 9 | 19.9 | IC1796 (Galaxy) | 0.47424° | near-field match | 52 | hold |
| watch | [AT2026ahuh](https://www.wis-tns.org/object/2026ahuh) | transient_candidate | 8 | 21.93 | NGC488 (Galaxy) | 0.95820° | near-field match | 52 | hold |
| watch | [AT2026ahui](https://www.wis-tns.org/object/2026ahui) | transient_candidate | 10 | 20.95 | Caldwell 51 (C51) (Galaxy) | 0.83601° | near-field match | 52 | hold |
| watch | [AT2026ahwa](https://www.wis-tns.org/object/2026ahwa) | transient_candidate | 28 | 22.58 | Caldwell 51 (C51) (Galaxy) | 0.49323° | near-field match | 52 | hold |
| watch | [AT2026ahwd](https://www.wis-tns.org/object/2026ahwd) | transient_candidate | 25 | 22.89 | IC 1757 (Galaxy) | 0.87137° | near-field match | 52 | hold |
| watch | [AT2026ahwk](https://www.wis-tns.org/object/2026ahwk) | transient_candidate | 9 | 21.37 | IC 74 (Galaxy) | 0.68493° | near-field match | 52 | hold |
| watch | [AT2026aibf](https://www.wis-tns.org/object/2026aibf) | transient_candidate | 20 | 21.48 | IC1784 (Galaxy) | 0.51346° | near-field match | 52 | hold |
| watch | [AT2026ahog](https://www.wis-tns.org/object/2026ahog) | transient_candidate | 6 | 21.93 | NGC894 (Nebula) | 0.76220° | near-field match | 50 | hold |
| watch | [AT2026ahoh](https://www.wis-tns.org/object/2026ahoh) | transient_candidate | 6 | 22.97 | NGC894 (Nebula) | 0.47015° | near-field match | 50 | hold |
| watch | [AT2026ahoi](https://www.wis-tns.org/object/2026ahoi) | transient_candidate | 6 | 23.04 | IC2055 (Nebula) | 0.73212° | near-field match | 50 | hold |
| watch | [AT2026ahok](https://www.wis-tns.org/object/2026ahok) | transient_candidate | 6 | 21.69 | NGC894 (Nebula) | 0.85717° | near-field match | 50 | hold |
| watch | [AT2026ahol](https://www.wis-tns.org/object/2026ahol) | transient_candidate | 6 | 23.1 | NGC894 (Nebula) | 0.78403° | near-field match | 50 | hold |
| watch | [AT2026ahov](https://www.wis-tns.org/object/2026ahov) | transient_candidate | 6 | 22.83 | NGC894 (Nebula) | 0.71377° | near-field match | 50 | hold |
| watch | [AT2026ahoy](https://www.wis-tns.org/object/2026ahoy) | transient_candidate | 6 | 23.46 | NGC894 (Nebula) | 0.87851° | near-field match | 50 | hold |
| watch | [AT2026ahoz](https://www.wis-tns.org/object/2026ahoz) | transient_candidate | 6 | 22.52 | NGC894 (Nebula) | 0.47970° | near-field match | 50 | hold |
| watch | [AT2026ahru](https://www.wis-tns.org/object/2026ahru) | transient_candidate | 6 | 20.33 | IC1376 (Nebula) | 0.31912° | near-field match | 50 | hold |
| watch | [AT2026ahvt](https://www.wis-tns.org/object/2026ahvt) | transient_candidate | 3 | 19.79 | Blue Flash (Planetary nebula) | 0.96606° | near-field match | 50 | hold |
| watch | [AT2026ahwv](https://www.wis-tns.org/object/2026ahwv) | transient_candidate | 7 | 22.18 | IC5385 (Nebula) | 0.77310° | near-field match | 50 | hold |
| watch | [AT2026aias](https://www.wis-tns.org/object/2026aias) | transient_candidate | 7 | 20.04 | IC333 (Nebula) | 0.69484° | near-field match | 50 | hold |
| watch | [AT2026aiat](https://www.wis-tns.org/object/2026aiat) | transient_candidate | 5 | 19.61 | Collinder 163 (CR163) (Open cluster) | 0.39314° | near-field match | 50 | hold |
| watch | [AT2026aiko](https://www.wis-tns.org/object/2026aiko) | transient_candidate | 0 | 19.85 | NGC7158 (Nebula) | 0.38099° | near-field match | 50 | hold |
| watch | [AT2026agua](https://www.wis-tns.org/object/2026agua) | transient_candidate | 13 | 19.33 | Lynds Dark Nebula 1571 (LDN1571) (Dark nebula) | 1.07129° | near-field match | 47 | hold |
| watch | [AT2026ahtk](https://www.wis-tns.org/object/2026ahtk) | transient_candidate | 8 | 19.35 | Sharpless 304 (SH2-304) (HII) | 1.80080° | near-field match | 47 | hold |
| watch | [AT2026afiy](https://www.wis-tns.org/object/2026afiy) | transient_candidate | 29 | 22.59 | IC 197 (Galaxy) | 1.75779° | near-field match | 45 | hold |
| watch | [AT2026afvg](https://www.wis-tns.org/object/2026afvg) | transient_candidate | 19 | 20.34 | IC 1931 (Galaxy) | 1.30858° | near-field match | 45 | hold |
| watch | [AT2026agyb](https://www.wis-tns.org/object/2026agyb) | transient_candidate | 10 | 19.63 | IC5201 (Galaxy) | 1.07201° | near-field match | 45 | hold |
| watch | [AT2026ahbv](https://www.wis-tns.org/object/2026ahbv) | transient_candidate | 9 | 19.86 | IC1495 (Galaxy) | 1.53637° | near-field match | 45 | hold |
| watch | [AT2026ahby](https://www.wis-tns.org/object/2026ahby) | transient_candidate | 9 | 19.7 | IC1438 (Galaxy) | 1.07179° | near-field match | 45 | hold |
| watch | [AT2026ahpj](https://www.wis-tns.org/object/2026ahpj) | transient_candidate | 8 | 22.85 | IC 5241 (Galaxy) | 1.94319° | near-field match | 45 | hold |
| watch | [AT2026ahpm](https://www.wis-tns.org/object/2026ahpm) | transient_candidate | 8 | 22.13 | IC 1507 (Galaxy) | 1.81899° | near-field match | 45 | hold |
| watch | [AT2026ahpo](https://www.wis-tns.org/object/2026ahpo) | transient_candidate | 8 | 22.21 | NGC488 (Galaxy) | 1.37026° | near-field match | 45 | hold |
| watch | [AT2026ahrl](https://www.wis-tns.org/object/2026ahrl) | transient_candidate | 8 | 21.11 | Silver Sliver Galaxy (Galaxy) | 1.54257° | near-field match | 45 | hold |
| watch | [AT2026ahrm](https://www.wis-tns.org/object/2026ahrm) | transient_candidate | 8 | 21.2 | IC239 (Galaxy) | 1.51986° | near-field match | 45 | hold |
| watch | [AT2026ahsu](https://www.wis-tns.org/object/2026ahsu) | transient_candidate | 24 | 20.05 | NGC1574 (Galaxy) | 1.88880° | near-field match | 45 | hold |
| watch | [AT2026ahsz](https://www.wis-tns.org/object/2026ahsz) | transient_candidate | 8 | 19.73 | IC1783 (Galaxy) | 1.16689° | near-field match | 45 | hold |
| watch | [AT2026ahta](https://www.wis-tns.org/object/2026ahta) | transient_candidate | 8 | 20.35 | IC1616 (Galaxy) | 1.32685° | near-field match | 45 | hold |
| watch | [AT2026ahub](https://www.wis-tns.org/object/2026ahub) | transient_candidate | 10 | 19.85 | IC1528 (Galaxy) | 1.92115° | near-field match | 45 | hold |
| watch | [AT2026ahum](https://www.wis-tns.org/object/2026ahum) | transient_candidate | 9 | 21.42 | NGC 2207 / IC 2163 (Galaxy) | 1.36722° | near-field match | 45 | hold |
| watch | [AT2026ahur](https://www.wis-tns.org/object/2026ahur) | transient_candidate | 26 | 21.19 | Mirach's Ghost (Galaxy) | 1.36361° | near-field match | 45 | hold |
| watch | [AT2026ahuw](https://www.wis-tns.org/object/2026ahuw) | transient_candidate | 12 | 19.83 | Collinder 205 (CR205) (Galaxy) | 1.48052° | near-field match | 45 | hold |
| watch | [AT2026ahvy](https://www.wis-tns.org/object/2026ahvy) | transient_candidate | 24 | 22.73 | IC 197 (Galaxy) | 1.74336° | near-field match | 45 | hold |
| watch | [AT2026ahwb](https://www.wis-tns.org/object/2026ahwb) | transient_candidate | 25 | 22.35 | IC 173 (Galaxy) | 1.50173° | near-field match | 45 | hold |
| watch | [AT2026ahxh](https://www.wis-tns.org/object/2026ahxh) | transient_candidate | 28 | 21.42 | IC1733 (Galaxy) | 1.07502° | near-field match | 45 | hold |
| watch | [AT2026ahxj](https://www.wis-tns.org/object/2026ahxj) | transient_candidate | 18 | 21.1 | Silver Sliver Galaxy (Galaxy) | 1.84591° | near-field match | 45 | hold |
| watch | [AT2026ahyo](https://www.wis-tns.org/object/2026ahyo) | transient_candidate | 8 | 19.76 | NGC 2207 / IC 2163 (Galaxy) | 1.39543° | near-field match | 45 | hold |
| watch | [AT2026ahzu](https://www.wis-tns.org/object/2026ahzu) | transient_candidate | 8 | 20.04 | IC 1600 (Galaxy) | 1.85166° | near-field match | 45 | hold |
| watch | [AT2026aibd](https://www.wis-tns.org/object/2026aibd) | transient_candidate | 9 | 21.48 | NGC741 (Galaxy) | 1.35024° | near-field match | 45 | hold |
| watch | [AT2026aibz](https://www.wis-tns.org/object/2026aibz) | transient_candidate | 11 | 19.66 | IC334 (Galaxy) | 1.51904° | near-field match | 45 | hold |
| watch | [AT2026aico](https://www.wis-tns.org/object/2026aico) | transient_candidate | 9 | 19.65 | IC 33 (Galaxy) | 1.03221° | near-field match | 45 | hold |
| watch | [AT2026aicp](https://www.wis-tns.org/object/2026aicp) | transient_candidate | 9 | 20.02 | IC5270 (Galaxy) | 1.45156° | near-field match | 45 | hold |
| watch | [AT2026aicw](https://www.wis-tns.org/object/2026aicw) | transient_candidate | 8 | 19.96 | IC1574 (Galaxy) | 1.16074° | near-field match | 45 | hold |
| watch | [AT2026aiit](https://www.wis-tns.org/object/2026aiit) | transient_candidate | 11 | 20.1 | IC 536 (Galaxy) | 1.35010° | near-field match | 45 | hold |
| watch | [AT2026aiiu](https://www.wis-tns.org/object/2026aiiu) | transient_candidate | 8 | 20.2 | IC1729 (Galaxy) | 1.95901° | near-field match | 45 | hold |
| watch | [AT2026ahnn](https://www.wis-tns.org/object/2026ahnn) | transient_candidate | 7 | 19.59 | IC333 (Nebula) | 1.07697° | near-field match | 43 | hold |
| watch | [AT2026ahoj](https://www.wis-tns.org/object/2026ahoj) | transient_candidate | 6 | 22.52 | NGC894 (Nebula) | 1.83043° | near-field match | 43 | hold |
| watch | [AT2026ahon](https://www.wis-tns.org/object/2026ahon) | transient_candidate | 6 | 22.75 | IC2055 (Nebula) | 1.64509° | near-field match | 43 | hold |
| watch | [AT2026ahoq](https://www.wis-tns.org/object/2026ahoq) | transient_candidate | 6 | 22.44 | NGC894 (Nebula) | 1.10782° | near-field match | 43 | hold |
| watch | [AT2026ahot](https://www.wis-tns.org/object/2026ahot) | transient_candidate | 6 | 22.67 | NGC894 (Nebula) | 1.19701° | near-field match | 43 | hold |
| watch | [AT2026ahou](https://www.wis-tns.org/object/2026ahou) | transient_candidate | 6 | 21.91 | NGC894 (Nebula) | 1.52046° | near-field match | 43 | hold |
| watch | [AT2026ahpc](https://www.wis-tns.org/object/2026ahpc) | transient_candidate | 6 | 22.38 | NGC894 (Nebula) | 1.17408° | near-field match | 43 | hold |
| watch | [AT2026ahqf](https://www.wis-tns.org/object/2026ahqf) | transient_candidate | 7 | 21.92 | IC1457 (Nebula) | 1.37958° | near-field match | 43 | hold |
| watch | [AT2026ahtl](https://www.wis-tns.org/object/2026ahtl) | transient_candidate | 5 | 20.91 | IC1497 (Nebula) | 1.19170° | near-field match | 43 | hold |
| watch | [AT2026ahuc](https://www.wis-tns.org/object/2026ahuc) | transient_candidate | 5 | 19.59 | NGC1479 (Nebula) | 1.96261° | near-field match | 43 | hold |
| watch | [AT2026ahva](https://www.wis-tns.org/object/2026ahva) | transient_candidate | 5 | 19.64 | Spirograph Nebula (Planetary nebula) | 1.39512° | near-field match | 43 | hold |
| watch | [AT2026ahws](https://www.wis-tns.org/object/2026ahws) | transient_candidate | 7 | 22.49 | NGC7565 (Nebula) | 1.12986° | near-field match | 43 | hold |
| watch | [AT2026ahxd](https://www.wis-tns.org/object/2026ahxd) | transient_candidate | 5 | 22.58 | NGC7565 (Nebula) | 1.79660° | near-field match | 43 | hold |
| watch | [AT2026ahyb](https://www.wis-tns.org/object/2026ahyb) | transient_candidate | 3 | 19.75 | NGC1707 (Nebula) | 1.35320° | near-field match | 43 | hold |
| watch | [AT2026ahyc](https://www.wis-tns.org/object/2026ahyc) | transient_candidate | 3 | 20.18 | IC274 (Nebula) | 1.51881° | near-field match | 43 | hold |
| watch | [AT2026ahyd](https://www.wis-tns.org/object/2026ahyd) | transient_candidate | 3 | 19.53 | IC5366 (Nebula) | 1.01813° | near-field match | 43 | hold |
| watch | [AT2026ahyh](https://www.wis-tns.org/object/2026ahyh) | transient_candidate | 3 | 19.57 | NGC2399 (Nebula) | 1.47903° | near-field match | 43 | hold |
| watch | [AT2026ahyu](https://www.wis-tns.org/object/2026ahyu) | transient_candidate | 7 | 20.24 | NGC1147 (Nebula) | 1.49197° | near-field match | 43 | hold |
| watch | [AT2026aiay](https://www.wis-tns.org/object/2026aiay) | transient_candidate | 3 | 20 | Messier 40 (M40) (Double star) | 1.14193° | near-field match | 43 | hold |
| watch | [AT2026aiid](https://www.wis-tns.org/object/2026aiid) | transient_candidate | 3 | 19.8 | IC1415 (Nebula) | 1.79157° | near-field match | 43 | hold |
| watch | [AT2026aiif](https://www.wis-tns.org/object/2026aiif) | transient_candidate | 3 | 20.25 | IC2013 (Nebula) | 1.67634° | near-field match | 43 | hold |
| watch | [AT2026aiih](https://www.wis-tns.org/object/2026aiih) | transient_candidate | 0 | 23.45 | IC2055 (Nebula) | 1.30155° | near-field match | 43 | hold |
| watch | [AT2026aiik](https://www.wis-tns.org/object/2026aiik) | transient_candidate | 0 | 23.13 | IC1992 (Nebula) | 1.50046° | near-field match | 43 | hold |
| watch | [AT2026aijr](https://www.wis-tns.org/object/2026aijr) | transient_candidate | 2 | 20.08 | NGC7447 (Nebula) | 1.89148° | near-field match | 43 | hold |
| watch | [AT2026aila](https://www.wis-tns.org/object/2026aila) | transient_candidate | 1 | 19.91 | NGC2586 (Nebula) | 1.95896° | near-field match | 43 | hold |
| watch | [AT2026ailb](https://www.wis-tns.org/object/2026ailb) | transient_candidate | 1 | 19.83 | IC518 (Nebula) | 1.97027° | near-field match | 43 | hold |
| watch | [AT2026ahbr](https://www.wis-tns.org/object/2026ahbr) | transient_candidate | 9 | 19.81 | IC1533 (Nebula) | 0.70152° | near-field match | 42 | hold |
| watch | [AT2026ahpk](https://www.wis-tns.org/object/2026ahpk) | transient_candidate | 8 | 22.3 | NGC7565 (Nebula) | 0.97844° | near-field match | 42 | hold |
| watch | [AT2026ahqn](https://www.wis-tns.org/object/2026ahqn) | transient_candidate | 9 | 19.65 | IC1475 (Nebula) | 0.66956° | near-field match | 42 | hold |
| watch | [AT2026ahrg](https://www.wis-tns.org/object/2026ahrg) | transient_candidate | 20 | 20.36 | IC 2275 (Star) | 0.45086° | near-field match | 42 | hold |
| watch | [AT2026ahro](https://www.wis-tns.org/object/2026ahro) | transient_candidate | 8 | 20.12 | IC1800 (Nebula) | 0.47926° | near-field match | 42 | hold |
| watch | [AT2026ahtn](https://www.wis-tns.org/object/2026ahtn) | transient_candidate | 5 | 19.87 | Lynds Bright Nebula 644 (LBN644) (HII) | 0.61734° | near-field match | 42 | hold |
| watch | [AT2026ahuo](https://www.wis-tns.org/object/2026ahuo) | transient_candidate | 7 | 22.5 | Lynds Bright Nebula 188 (LBN188) (HII) | 0.95066° | near-field match | 42 | hold |
| watch | [AT2026ahxt](https://www.wis-tns.org/object/2026ahxt) | transient_candidate | 29 | 20.75 | NGC1479 (Nebula) | 0.26734° | near-field match | 42 | hold |
| watch | [AT2026ahxw](https://www.wis-tns.org/object/2026ahxw) | transient_candidate | 17 | 20.84 | Collinder 154 (CR154) (Open cluster) | 0.75676° | near-field match | 42 | hold |
| watch | [AT2026ahzy](https://www.wis-tns.org/object/2026ahzy) | transient_candidate | 3 | 19.73 | Lynds Bright Nebula 114 (LBN114) (HII) | 0.63998° | near-field match | 42 | hold |
| watch | [AT2026aibk](https://www.wis-tns.org/object/2026aibk) | transient_candidate | 8 | 21.26 | NGC843 (Nebula) | 0.80016° | near-field match | 42 | hold |
| watch | [AT2026aiic](https://www.wis-tns.org/object/2026aiic) | transient_candidate | 3 | 20.55 | Lynds Bright Nebula 220 (LBN220) (HII) | 0.80240° | near-field match | 42 | hold |
| watch | [AT2026aiio](https://www.wis-tns.org/object/2026aiio) | transient_candidate | 17 | 20.63 | NGC930 (Nebula) | 0.95799° | near-field match | 42 | hold |
| watch | [AT2026ahpi](https://www.wis-tns.org/object/2026ahpi) | transient_candidate | 19 | 22.57 | IC5385 (Nebula) | 1.37483° | near-field match | 35 | hold |
| watch | [AT2026ahrk](https://www.wis-tns.org/object/2026ahrk) | transient_candidate | 9 | 20.02 | NGC603 (Nebula) | 1.73907° | near-field match | 35 | hold |
| watch | [AT2026ahso](https://www.wis-tns.org/object/2026ahso) | transient_candidate | 9 | 20.22 | IC1475 (Nebula) | 1.54946° | near-field match | 35 | hold |
| watch | [AT2026ahuk](https://www.wis-tns.org/object/2026ahuk) | transient_candidate | 9 | 21.89 | IC5385 (Nebula) | 1.31983° | near-field match | 35 | hold |
| watch | [AT2026ahux](https://www.wis-tns.org/object/2026ahux) | transient_candidate | 8 | 20.27 | NGC611 (Nebula) | 1.75896° | near-field match | 35 | hold |
| watch | [AT2026ahuz](https://www.wis-tns.org/object/2026ahuz) | transient_candidate | 4 | 19.92 | Lynds Bright Nebula 1025 (LBN1025) (HII) | 1.74006° | near-field match | 35 | hold |
| watch | [AT2026ahve](https://www.wis-tns.org/object/2026ahve) | transient_candidate | 16 | 19.59 | Collinder 120 (CR120) (Open cluster) | 1.02417° | near-field match | 35 | hold |
| watch | [AT2026ahwr](https://www.wis-tns.org/object/2026ahwr) | transient_candidate | 7 | 22.4 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.72552° | near-field match | 35 | hold |
| watch | [AT2026ahxv](https://www.wis-tns.org/object/2026ahxv) | transient_candidate | 3 | 19.84 | Lynds Bright Nebula 530 (LBN530) (HII) | 1.03366° | near-field match | 35 | hold |
| watch | [AT2026ahyv](https://www.wis-tns.org/object/2026ahyv) | transient_candidate | 4 | 21.02 | Lynds Bright Nebula 799 (LBN799) (HII) | 1.12214° | near-field match | 35 | hold |
| watch | [AT2026ahzq](https://www.wis-tns.org/object/2026ahzq) | transient_candidate | 5 | 20.23 | Lynds Bright Nebula 991 (LBN991) (HII) | 1.87296° | near-field match | 35 | hold |
| watch | [AT2026aiak](https://www.wis-tns.org/object/2026aiak) | transient_candidate | 3 | 19.6 | Lynds Bright Nebula 753 (LBN753) (HII) | 1.72475° | near-field match | 35 | hold |
| watch | [AT2026aial](https://www.wis-tns.org/object/2026aial) | transient_candidate | 3 | 20.94 | Lynds Bright Nebula 711 (LBN711) (HII) | 1.61980° | near-field match | 35 | hold |
| watch | [AT2026aidb](https://www.wis-tns.org/object/2026aidb) | transient_candidate | 2 | 20.12 | Sharpless 246 (SH2-246) (HII) | 1.22301° | near-field match | 35 | hold |
| watch | [AT2026aiip](https://www.wis-tns.org/object/2026aiip) | transient_candidate | 17 | 20.62 | NGC1639 (Nebula) | 1.39017° | near-field match | 35 | hold |
| watch | [AT2026aikj](https://www.wis-tns.org/object/2026aikj) | transient_candidate | 1 | 20.02 | Lynds Bright Nebula 1010 (LBN1010) (HII) | 1.53192° | near-field match | 35 | hold |
| watch | [AT2026ahrf](https://www.wis-tns.org/object/2026ahrf) | transient_candidate | 20 | 20.74 | Lynds Bright Nebula 715 (LBN715) (HII) | 0.40429° | near-field match | 34 | hold |
| watch | [AT2026ahvq](https://www.wis-tns.org/object/2026ahvq) | transient_candidate | 12 | 20.36 | Headphone nebula (Planetary nebula) | 0.64976° | near-field match | 34 | hold |
| watch | [AT2026aiir](https://www.wis-tns.org/object/2026aiir) | transient_candidate | 30 | 20.1 | Lynds Bright Nebula 790 (LBN790) (HII) | 0.58443° | near-field match | 34 | hold |
| watch | [SN2026abza](https://www.wis-tns.org/object/2026abza) | SN II | 57 | 20.22 | NGC1637 (Galaxy) | 0.27656° | near-field match | 30 | hold |
| watch | [AT2026adph](https://www.wis-tns.org/object/2026adph) | transient_candidate | 43 | 19.38 | IC 1749 (Galaxy) | 1.01030° | near-field match | 28 | hold |
| watch | [AT2026aflk](https://www.wis-tns.org/object/2026aflk) | transient_candidate | 29 | 22.07 | Lynds Bright Nebula 639 (LBN639) (HII) | 1.56774° | near-field match | 27 | hold |
| watch | [AT2026ahbl](https://www.wis-tns.org/object/2026ahbl) | transient_candidate | 9 | 19.99 | Lynds Bright Nebula 157 (LBN157) (HII) | 1.08937° | near-field match | 27 | hold |
| watch | [AT2026ahvo](https://www.wis-tns.org/object/2026ahvo) | transient_candidate | 20 | 19.6 | Lynds Bright Nebula 141 (LBN141) (HII) | 1.06337° | near-field match | 27 | hold |
| watch | [AT2026ahwi](https://www.wis-tns.org/object/2026ahwi) | transient_candidate | 19 | 22.19 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.87304° | near-field match | 27 | hold |
| watch | [AT2026ahwn](https://www.wis-tns.org/object/2026ahwn) | transient_candidate | 8 | 22.55 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.79970° | near-field match | 27 | hold |
| watch | [AT2026ahpq](https://www.wis-tns.org/object/2026ahpq) | transient_candidate | 36 | 21.74 | Messier 32 (M32) (Galaxy) | 0.33280° | near-field match | 15 | hold |
| watch | [AT2026ahwf](https://www.wis-tns.org/object/2026ahwf) | transient_candidate | 36 | 21.45 | NGC741 (Galaxy) | 0.55155° | near-field match | 15 | hold |
| watch | [AT2026aiiq](https://www.wis-tns.org/object/2026aiiq) | transient_candidate | 31 | 19.77 | IC 1962 (Galaxy) | 0.89936° | near-field match | 15 | hold |
| watch | [AT2026ahwg](https://www.wis-tns.org/object/2026ahwg) | transient_candidate | 33 | 22.94 | IC 1481 (Galaxy) | 1.28105° | near-field match | 8 | hold |
| watch | [AT2026aibe](https://www.wis-tns.org/object/2026aibe) | transient_candidate | 33 | 21.74 | Silver Sliver Galaxy (Galaxy) | 1.67355° | near-field match | 8 | hold |
| watch | [AT2026aepe](https://www.wis-tns.org/object/2026aepe) | transient_candidate | 36 | 19.97 | IC 1623 (CiG) | 1.22702° | near-field match | 0 | hold |
| watch | [AT2026aghp](https://www.wis-tns.org/object/2026aghp) | transient_candidate | 33 | 20.88 | NGC894 (Nebula) | 1.58735° | near-field match | 0 | hold |

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
| Discovery | 2026-10-25T00:35:40Z · 12 days · 17.67 orange |
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

### 2. [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) near NGC4216

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4216 as this object's host. The 0.39324° (23.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.006997 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T19:55:53Z · 4 days · 16.1 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4401....1I](https://ui.adsabs.harvard.edu/abs/2026TNSTR4401....1I/abstract) |
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
| Separation | 0.39324° · 23.59′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.460208%2013.424028&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026ahvu](https://www.wis-tns.org/object/2026ahvu) near NGC1433

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1433 as this object's host. The 0.01649° (0.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.003589 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T04:20:36Z · 4 days · 17.06 cyan |
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

### 4. [SN2026agwb](https://www.wis-tns.org/object/2026agwb) near NGC134

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 97/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC134 as this object's host. The 0.96564° (57.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.061 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T09:16:41Z · 11 days · 17.8 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4285....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4285....1T/abstract) |
| Classification references | [2026TNSCR4322....1N](https://ui.adsabs.harvard.edu/abs/2026TNSCR4322....1N/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=6.4394233%20-33.3519633&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [SN2026agwm](https://www.wis-tns.org/object/2026agwm) near IC4931

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 97/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4931 as this object's host. The 0.65936° (39.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.02 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T00:01:05Z · 10 days · 18.33 orange |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=299.7725657%20-38.0113271&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 6. [AT2026ahxs](https://www.wis-tns.org/object/2026ahxs) near IC 1777

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 95/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1777 as this object's host. The 0.07735° (4.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T05:26:42Z · 9 days · 17.5 g |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.5459%2015.1326871&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 7. [SN2026agpv](https://www.wis-tns.org/object/2026agpv) near NGC636

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.88833° (113.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.025111 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-23T22:30:00Z · 14 days · 17.47 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4260....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4260....1T/abstract) |
| Classification references | [2026TNSCR4306....1W](https://ui.adsabs.harvard.edu/abs/2026TNSCR4306....1W/abstract) |
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
| Separation | 1.88833° · 113.30′ |
| Catalog description | NGC 636 is an elliptical galaxy in the Cetus constellation. It is located about 96 million light-years from the Milky Way. It was discovered by the German–British astronomer William Herschel in 1785. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agpv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.852939%20-9.39937&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 8. [SN2026agvs](https://www.wis-tns.org/object/2026agvs) near IC2104

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2104 as this object's host. The 1.31532° (78.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIb |
| Redshift | 0.022 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T11:03:12Z · 12 days · 18.35 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4289....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4289....1R/abstract) |
| Classification references | [2026TNSCR4355....1N](https://ui.adsabs.harvard.edu/abs/2026TNSCR4355....1N/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2104** · `IC2104` |
| Catalog display name | IC2104 |
| Type / constellation | Galaxy · Lepus |
| Catalog magnitude / angular size | 13.8 · 2.11′ × 1.14′ |
| Distance | 80,000 kpc |
| Separation | 1.31532° · 78.92′ |
| Catalog description | faint, extended, gradually brighter middle, or in the middle |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agvs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.3884315%20-16.1663595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 9. [SN2026agzw](https://www.wis-tns.org/object/2026agzw) near IC1657

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.30068° (78.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.056022 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T11:27:06Z · 9 days · 18.09 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4313....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4313....1O/abstract) |
| Classification references | [2026TNSCR4323....1L](https://ui.adsabs.harvard.edu/abs/2026TNSCR4323....1L/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1657** · `IC1657` |
| Catalog display name | IC1657 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 13.1 · 2.32′ × 0.52′ |
| Distance | — |
| Separation | 1.30068° · 78.04′ |
| Catalog description | extremely, excessively faint, small in angular size, very much / magnitude extended |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agzw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.7565825%20-33.9376075&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 10. [AT2026ahyf](https://www.wis-tns.org/object/2026ahyf) near IC 2405

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2405 as this object's host. The 0.45056° (27.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:36Z · 3 days · 18.49 g |
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
| Subject | **IC 2405** · `IC 2405` |
| Catalog display name | NGC 4329 |
| Type / constellation | Galaxy · Lyn |
| Catalog magnitude / angular size | — · 0.76′ × 0.57′ |
| Distance | — |
| Separation | 0.45056° · 27.03′ |
| Catalog description | NGC 4329 is an elliptical galaxy located 144 million light-years away in the constellation Corvus. The galaxy was discovered by astronomer John Herschel on March 9, 1828. NGC 4329 is host a supermassive black hole with an estimated mass of 3.1×108 solar masses. NGC 4329 is a member of a group of 5 galaxies known as [T2015] nest 100478. NGC 4329 is the brightest member of this group and the group includes the galaxies IC 785, IC 786, MCG-02-32-006, and LEDA 170189. The redshift of NGC 4329 places it in the within the bounds of the Hydra-Centaurus supercluster. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2405 has the different designation NGC 4329 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=132.0534498%2036.7792244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 11. [AT2026ahzh](https://www.wis-tns.org/object/2026ahzh) near NGC3665

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3665 as this object's host. The 0.91138° (54.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T14:39:22Z · 3 days · 18.28 orange |
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
| Subject | **NGC3665** · `NGC3665` |
| Catalog display name | NGC3665 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 4.06′ × 3′ |
| Distance | — |
| Separation | 0.91138° · 54.68′ |
| Catalog description | NGC 3665 is a lenticular galaxy located in the constellation Ursa Major. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that NGC 3665 is about 85,000 light years across. It was discovered by William Herschel on March 23, 1789. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=171.485602%2039.642764&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 12. [AT2026aicq](https://www.wis-tns.org/object/2026aicq) near IC 369

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 369 as this object's host. The 0.91864° (55.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T13:00:09Z · 2 days · 18.48 L |
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
| Subject | **IC 369** · `IC 369` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Eri |
| Catalog magnitude / angular size | — · 0.76′ × 0.76′ |
| Distance | — |
| Separation | 0.91864° · 55.12′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 369 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.25439%20-12.627323&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 13. [AT2026aikg](https://www.wis-tns.org/object/2026aikg) near NGC4414

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4414 as this object's host. The 0.85966° (51.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:55:21Z · 3 days · 17.95 r |
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
| Subject | **NGC4414** · `NGC4414` |
| Catalog display name | NGC4414 |
| Type / constellation | Galaxy · Coma Berenices |
| Catalog magnitude / angular size | 10.2 · 1.95′ × 1.12′ |
| Distance | — |
| Separation | 0.85966° · 51.58′ |
| Catalog description | NGC 4414, also known as the Dusty Spiral Galaxy, is an unbarred spiral galaxy about 62 million light-years away in the constellation Coma Berenices. It was discovered by German-British astronomer William Herschel on 13 March 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=187.5700185%2031.4889297&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 14. [SN2026ahoe](https://www.wis-tns.org/object/2026ahoe) near Caldwell 87 (C87)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 88/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 87 (C87) as this object's host. The 1.22814° (73.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.105 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:45:21Z · 6 days · 18.05 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4377....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4377....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Caldwell 87 (C87)** · `C87` |
| Catalog display name | Caldwell 87 (C87) |
| Type / constellation | Globular cluster · Horologium |
| Catalog magnitude / angular size | 8.4 · 7′ × 7′ |
| Distance | 16.4 kpc |
| Separation | 1.22814° · 73.69′ |
| Catalog description | NGC 1261 is a globular cluster of stars in the southern constellation of Horologium, first discovered by Scottish astronomer James Dunlop in 1826. The cluster is located at a distance of 53 kilolight-years from the Sun, and 59 kilolight-years from the Galactic Center. It is about 10.24 billion years old with 341,000 times the mass of the Sun. The cluster does not display the normal indications of core collapse, but evidence suggests it may have instead passed through a post core-collapse bounce state within the past two billion years. The central luminosity density is 2.22 L☉·pc−3, which is low for a globular cluster. Despite this, it has a Shapley–Sawyer Concentration Class of II, indicating a dense central concentration. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.5925543%20-56.41624&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 15. [AT2026ahod](https://www.wis-tns.org/object/2026ahod) near IC5176

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5176 as this object's host. The 1.17052° (70.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T02:16:31Z · 6 days · 18.34 cyan |
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
| Subject | **IC5176** · `IC5176` |
| Catalog display name | IC5176 |
| Type / constellation | Galaxy · Tucana |
| Catalog magnitude / angular size | 13.6 · 4.51′ × 0.63′ |
| Distance | 26,400 kpc |
| Separation | 1.17052° · 70.23′ |
| Catalog description | very faint, small in angular size, extremely, excessively extended 30deg , a single star north |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahod) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.0412267%20-67.3762883&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 16. [AT2026ahrc](https://www.wis-tns.org/object/2026ahrc) near IC396

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC396 as this object's host. The 1.65285° (99.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T18:17:26Z · 6 days · 18.02 Clear |
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
| Subject | **IC396** · `IC396` |
| Catalog display name | IC396 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 13.1 · 2.38′ × 1.45′ |
| Distance | — |
| Separation | 1.65285° · 99.17′ |
| Catalog description | faint, small in angular size, round, brighter middle, or in the middle nucleus, or to a nucleus, faint double a single star south following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=73.7905%2069.957306&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 17. [AT2026ahxu](https://www.wis-tns.org/object/2026ahxu) near IC4831

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4831 as this object's host. The 1.39323° (83.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T00:13:40Z · 4 days · 17.94 cyan |
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
| Subject | **IC4831** · `IC4831` |
| Catalog display name | IC4831 |
| Type / constellation | Galaxy · Pavo |
| Catalog magnitude / angular size | 12.1 · 3.67′ × 0.84′ |
| Distance | 49,900 kpc |
| Separation | 1.39323° · 83.59′ |
| Catalog description | NGC 6782 is a barred spiral galaxy located in the southern constellation of Pavo, at a distance of approximately 173 megalight-years from the Milky Way. It was discovered on July 12, 1834 by English astronomer John Herschel. John L. E. Dreyer described it as, "considerably faint, considerably small, round, a little brighter middle, 9th magnitude star to south". The morphological classification of NGC 6782 is (R1R′2)SB(r)a, indicating a barred spiral galaxy with a multiple ring system and tightly-wound spiral arms. It is seen nearly face-on, being inclined by an angle of 27.2°±0.2° to the line of sight from the Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=290.1199289%20-63.5014956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 18. [AT2026ahqt](https://www.wis-tns.org/object/2026ahqt) near IC5250

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 82/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5250 as this object's host. The 0.89448° (53.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T02:28:33Z · 8 days · 18.3 orange |
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
| Subject | **IC5250** · `IC5250` |
| Catalog display name | IC5250 |
| Type / constellation | Galaxy · Tucana |
| Catalog magnitude / angular size | 11.1 · 3.5′ × 3.5′ |
| Distance | — |
| Separation | 0.89448° · 53.67′ |
| Catalog description | considerably bright, small in angular size, round, faint a single star following (eastward) 0'.5 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.938518%20-65.1845187&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 19. [AT2026ahqx](https://www.wis-tns.org/object/2026ahqx) near NGC1559

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 82/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1559 as this object's host. The 0.93510° (56.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T06:12:16Z · 8 days · 17.16 orange |
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
| Subject | **NGC1559** · `NGC1559` |
| Catalog display name | NGC1559 |
| Type / constellation | Galaxy · Reticulum |
| Catalog magnitude / angular size | 10.6 · 4.19′ × 2.18′ |
| Distance | — |
| Separation | 0.93510° · 56.11′ |
| Catalog description | NGC 1559 is a barred spiral galaxy in the constellation Reticulum. It was discovered on 6 November 1826 by Scottish astronomer James Dunlop. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.3805521%20-63.0228989&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 20. [AT2026aict](https://www.wis-tns.org/object/2026aict) near Dumbbell Nebula

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Dumbbell Nebula as this object's host. The 0.76955° (46.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T05:43:56Z · 2 days · 18.31 orange |
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
| Subject | **Dumbbell Nebula** · `M27` |
| Catalog display name | Dumbbell Nebula |
| Type / constellation | Planetary nebula · Vulpecula |
| Catalog magnitude / angular size | 7.4 · 8′ × 5.7′ |
| Distance | 0.383 kpc |
| Separation | 0.76955° · 46.17′ |
| Catalog description | The Dumbbell Nebula is a planetary nebula in the constellation Vulpecula, at a distance of about 1360 light-years. It was the first such nebula to be discovered, by Charles Messier in 1764. At its brightness of visual magnitude 7.5 and diameter of about 8 arcminutes, it is easily visible in binoculars and is a popular observing target in amateur telescopes. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aict) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=299.076118%2022.597135&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 21. [AT2026agtx](https://www.wis-tns.org/object/2026agtx) near IC4808

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4808 as this object's host. The 1.73758° (104.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T00:06:39Z · 12 days · 18.44 orange |
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
| Subject | **IC4808** · `IC4808` |
| Catalog display name | IC4808 |
| Type / constellation | Galaxy · Corona Australis |
| Catalog magnitude / angular size | 12.7 · 2.26′ × 0.87′ |
| Distance | 49,500 kpc |
| Separation | 1.73758° · 104.25′ |
| Catalog description | very faint, considerably large, considerably extended 45deg , little (adv.); long (adj.) brighter middle, or in the middle, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agtx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=283.93788%20-46.780955&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 22. [AT2026agvn](https://www.wis-tns.org/object/2026agvn) near NGC3486

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3486 as this object's host. The 1.16846° (70.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T12:50:15Z · 12 days · 18.12 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4273....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR4273....1F/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3486** · `NGC3486` |
| Catalog display name | NGC3486 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10.6 · 5.82′ × 4.12′ |
| Distance | — |
| Separation | 1.16846° · 70.11′ |
| Catalog description | NGC 3486 is an intermediate barred spiral galaxy located about 27.4 million light years away in the constellation of Leo Minor. It has a morphological classification of SAB(r)c, which indicates it is a weakly barred spiral with an inner ring and loosely wound arms. This is a borderline, low-luminosity Seyfert galaxy with an active nucleus. However, no radio or X-ray emission has been detected from the core, and it may only have a small supermassive black hole with less than a million times the mass of the Sun. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agvn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.4183589%2029.1451487&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 23. [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 95/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 0.47363° (28.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.039 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:53:54Z · 5 days · 18.71 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 3** · `IC 3` |
| Catalog display name | IC 342 |
| Type / constellation | Spiral galaxy · Psc |
| Catalog magnitude / angular size | — · 0.93′ × 0.67′ |
| Distance | 10.7 ly |
| Separation | 0.47363° · 28.42′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=3.1673559%20-0.0368725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 24. [AT2026aikp](https://www.wis-tns.org/object/2026aikp) near Great Nebula in Andromeda

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.10297° (6.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T13:24:24Z · 2 days · 19.14 Clear |
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
| Separation | 0.10297° · 6.18′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.585333%2041.341056&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 25. [SN2026afqk](https://www.wis-tns.org/object/2026afqk) near IC240

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC240 as this object's host. The 0.22339° (13.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T01:04:03Z · 20 days · 19.37 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4168....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4168....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC240** · `IC240` |
| Catalog display name | IC240 |
| Type / constellation | Nebula · Perseus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.22339° · 13.40′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afqk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=39.6538897%2041.9330121&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 26. [SN2026ahna](https://www.wis-tns.org/object/2026ahna) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 0.88139° (52.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.072 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:47:57Z · 9 days · 18.9 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4367....1P](https://ui.adsabs.harvard.edu/abs/2026TNSTR4367....1P/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1933** · `IC1933` |
| Catalog display name | IC1933 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.6 · 2.27′ × 1.21′ |
| Distance | 17,500 kpc |
| Separation | 0.88139° · 52.88′ |
| Catalog description | little (adv.); long (adj.) extended south preceding north following |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahna) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.5402983%20-53.494825&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 27. [AT2026ahyy](https://www.wis-tns.org/object/2026ahyy) near IC 1996

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 85/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1996 as this object's host. The 0.23846° (14.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:47:57Z · 9 days · 19.41 L |
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
| Subject | **IC 1996** · `IC 1996` |
| Catalog display name | IC 10 |
| Type / constellation | Galaxy · Ret |
| Catalog magnitude / angular size | — · 0.92′ × 0.21′ |
| Distance | 2.5 ly |
| Separation | 0.23846° · 14.31′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1996 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.625555%20-57.475175&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 28. [SN2026afkh](https://www.wis-tns.org/object/2026afkh) near IC5309

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5309 as this object's host. The 1.91597° (114.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.04244 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T04:28:59Z · 23 days · 19.36 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4138....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4138....1S/abstract) |
| Classification references | [2026TNSCR4217....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4217....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5309** · `IC5309` |
| Catalog display name | IC5309 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 13.6 · 1.29′ × 0.61′ |
| Distance | 51,600 kpc |
| Separation | 1.91597° · 114.96′ |
| Catalog description | faint, small in angular size, fan-shaped, a single star attached suddenly (abruptly) / south |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afkh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.8985138%207.7357484&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [SN2026afql](https://www.wis-tns.org/object/2026afql) near IC449

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC449 as this object's host. The 1.98969° (119.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T03:40:41Z · 20 days · 18.74 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4168....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4168....1T/abstract) |
| Classification references | [2026TNSCR4271....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4271....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC449** · `IC449` |
| Catalog display name | IC449 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 13.7 · 1.77′ × 1.34′ |
| Distance | — |
| Separation | 1.98969° · 119.38′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, small in angular size, round, brighter middle, or in the middle, between 2 double stars (pl.) |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afql) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=95.8225774%2070.5541956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 30. [SN2026aguc](https://www.wis-tns.org/object/2026aguc) near IC382

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC382 as this object's host. The 1.38071° (82.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.035 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T09:42:27Z · 12 days · 19.18 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4280....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4280....1S/abstract) |
| Classification references | [2026TNSCR4374....1W](https://ui.adsabs.harvard.edu/abs/2026TNSCR4374....1W/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC382** · `IC382` |
| Catalog display name | IC382 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 13.5 · 1.99′ × 1.18′ |
| Distance | 52,700 kpc |
| Separation | 1.38071° · 82.84′ |
| Catalog description | Messier 25, also known as IC 4725, is an open cluster of stars in the southern constellation of Sagittarius. The first recorded observation of this cluster was made by Philippe Loys de Chéseaux in 1745 and it was included in Charles Messier's list of nebulous objects in 1764. The cluster is located near some obscuring features, with a dark lane passing near the center. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aguc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=69.5172127%20-10.8720977&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 31. [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) near IC 2017

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2017 as this object's host. The 0.36966° (22.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:43:45Z · 7 days · 19.31 L |
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
| Subject | **IC 2017** · `IC 2017` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Ret |
| Catalog magnitude / angular size | — · 1.11′ × 0.74′ |
| Distance | — |
| Separation | 0.36966° · 22.18′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2017 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.416894%20-59.741514&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 32. [AT2026ahvg](https://www.wis-tns.org/object/2026ahvg) near IC5152

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5152 as this object's host. The 0.90775° (54.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T01:42:48Z · 6 days · 19.39 cyan |
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
| Subject | **IC5152** · `IC5152` |
| Catalog display name | IC5152 |
| Type / constellation | Galaxy · Indus |
| Catalog magnitude / angular size | 10.7 · 5.13′ × 3.6′ |
| Distance | — |
| Separation | 0.90775° · 54.46′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.1332733%20-50.4544467&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 33. [AT2026ahyj](https://www.wis-tns.org/object/2026ahyj) near NGC3646

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3646 as this object's host. The 0.80341° (48.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:57:22Z · 4 days · 19.41 r |
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
| Subject | **NGC3646** · `NGC3646` |
| Catalog display name | NGC3646 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.2 · 3.09′ × 1.48′ |
| Distance | — |
| Separation | 0.80341° · 48.20′ |
| Catalog description | NGC 3646 is a galaxy in the Leo constellation that has variously been described as "a strange spiral galaxy" of morphological classification Sc or SAa, or as "a ring-shaped galaxy". It was discovered by German-British astronomer William Herschel on 15 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.7944213%2019.443348&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026ahyq](https://www.wis-tns.org/object/2026ahyq) near NGC4125

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4125 as this object's host. The 0.59101° (35.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:46:27Z · 3 days · 18.91 r |
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
| Subject | **NGC4125** · `NGC4125` |
| Catalog display name | NGC4125 |
| Type / constellation | Galaxy · Draco |
| Catalog magnitude / angular size | 9.7 · 5.87′ × 4.58′ |
| Distance | — |
| Separation | 0.59101° · 35.46′ |
| Catalog description | NGC 4125 is an elliptical galaxy in the constellation Draco. It was discovered on 4 January 1850 by English astronomer John Russell Hind. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.3621378%2064.6542206&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 35. [AT2026ahzb](https://www.wis-tns.org/object/2026ahzb) near IC 3107

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3107 as this object's host. The 0.67614° (40.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:59:09Z · 3 days · 18.52 r |
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
| Subject | **IC 3107** · `IC 3107` |
| Catalog display name | NGC 243 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 1.25′ × 0.55′ |
| Distance | — |
| Separation | 0.67614° · 40.57′ |
| Catalog description | NGC 243 is a lenticular galaxy located in the constellation Andromeda. It was discovered on October 18, 1881 by Édouard Stephan. NGC 243 is a lenticular galaxy located in the constellation Andromeda. It was discovered on October 18, 1881 by Édouard Stephan. According to A.M. Garcia, NGC 243 is a member of the NGC 315 Group (also known as LGG 14). This group contains 42 galaxies, including NGC 226, NGC 262, NGC 266, NGC 311, NGC 315, NGC 338, IC 43, IC 66, AND IC 69, among others. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3107 has the different designation NGC 243 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=184.5768909%2010.1809435&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 36. [AT2026ahzc](https://www.wis-tns.org/object/2026ahzc) near IC5065

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5065 as this object's host. The 0.96030° (57.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:45:38Z · 3 days · 19.04 cyan |
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
| Subject | **IC5065** · `IC5065` |
| Catalog display name | IC5065 |
| Type / constellation | Galaxy · Microscopium |
| Catalog magnitude / angular size | 13.6 · 1.5′ × 0.92′ |
| Distance | 76,200 kpc |
| Separation | 0.96030° · 57.62′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=311.95576%20-30.2949067&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 37. [AT2026aijt](https://www.wis-tns.org/object/2026aijt) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 0.58117° (34.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:53:54Z · 3 days · 19.16 r |
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
| Subject | **IC 673** · `IC 673` |
| Catalog display name | NGC673 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 1.29′ × 0.59′ |
| Distance | — |
| Separation | 0.58117° · 34.87′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=167.1827248%200.4571874&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 38. [AT2026aguv](https://www.wis-tns.org/object/2026aguv) near NGC2404

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2404 as this object's host. The 0.01585° (0.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T08:53:19Z · 12 days · 18.78 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4280....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4280....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2404** · `NGC2404` |
| Catalog display name | NGC2404 |
| Type / constellation | HII · Camelopardalis |
| Catalog magnitude / angular size | — · 0.4′ × 0.4′ |
| Distance | — |
| Separation | 0.01585° · 0.95′ |
| Catalog description | NGC 2404 is a massive H II region inside NGC 2403, a spiral galaxy in Camelopardalis. It was discovered on February 2, 1886 by Gulliaume Bigourdan. NGC 2404 is approximately 940 ly in diameter, making it one of the largest H II regions so far known. It is the largest H II region in NGC 2403, and lies at the outskirts of the galaxy, making for a striking similarity with NGC 604 in M33, both in size and location in the host galaxy. This H II region contains 30-40 Wolf-Rayet stars, and unlike the Tarantula Nebula, but similar to NGC 604, NGC 2404's open cluster is probably much less compact, so it probably looks like a large stellar association. This H II region is probably only a few million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aguv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=114.2689556%2065.5951549&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 39. [AT2026ahqz](https://www.wis-tns.org/object/2026ahqz) near Lynds Bright Nebula 221 (LBN221)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 221 (LBN221) as this object's host. The 0.23961° (14.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T07:37:43Z · 6 days · 18.84 orange |
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
| Subject | **Lynds Bright Nebula 221 (LBN221)** · `LBN221` |
| Catalog display name | Lynds Bright Nebula 221 (LBN221) |
| Type / constellation | HII · Cygnus |
| Catalog magnitude / angular size | — · 52′ × 10′ |
| Distance | — |
| Separation | 0.23961° · 14.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°.

[TNS object](https://www.wis-tns.org/object/2026ahqz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=296.9275633%2042.4788867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [AT2026ahnc](https://www.wis-tns.org/object/2026ahnc) near IC 1799

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1799 as this object's host. The 1.38869° (83.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:30:23Z · 7 days · 19.41 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4365....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4365....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1799** · `IC 1799` |
| Catalog display name | NGC 2685 |
| Type / constellation | Galaxy · And |
| Catalog magnitude / angular size | — · 0.79′ × 0.37′ |
| Distance | — |
| Separation | 1.38869° · 83.32′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1799 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahnc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.2080229%2045.8180814&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 41. [AT2026ahqu](https://www.wis-tns.org/object/2026ahqu) near IC5267

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5267 as this object's host. The 1.68442° (101.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T02:18:29Z · 6 days · 18.85 cyan |
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
| Subject | **IC5267** · `IC5267` |
| Catalog display name | IC5267 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 10.4 · 5.58′ × 4.06′ |
| Distance | — |
| Separation | 1.68442° · 101.07′ |
| Catalog description | The Telescopium−Grus Cloud is a galaxy filament in the constellations of Pavo, Indus, and Telescopium. It was first defined by astronomer Brent Tully in his book The Nearby Galaxies Atlas and its companion book The Nearby Galaxies Catalog. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.8782367%20-45.0295417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 42. [AT2026ahtg](https://www.wis-tns.org/object/2026ahtg) near IC1953

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1953 as this object's host. The 1.01025° (60.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:49:51Z · 5 days · 19.25 L |
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
| Subject | **IC1953** · `IC1953` |
| Catalog display name | IC1953 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 12 · 2.26′ × 1.19′ |
| Distance | 22,900 kpc |
| Separation | 1.01025° · 60.62′ |
| Catalog description | IC 1953 is a barred spiral galaxy situated in the constellation of Eridanus. Located about 83.4 million light years away, it is a member of the Eridanus Cluster of galaxies, a cluster of about 200 galaxies. It was discovered by DeLisle Stewart in 1899. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.238713%20-22.474669&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 43. [AT2026ahuu](https://www.wis-tns.org/object/2026ahuu) near IC449

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC449 as this object's host. The 1.92939° (115.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:07:43Z · 4 days · 18.69 g |
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
| Subject | **IC449** · `IC449` |
| Catalog display name | IC449 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 13.7 · 1.77′ × 1.34′ |
| Distance | — |
| Separation | 1.92939° · 115.76′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, small in angular size, round, brighter middle, or in the middle, between 2 double stars (pl.) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.94736%2069.420988&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 44. [AT2026ahuv](https://www.wis-tns.org/object/2026ahuv) near NGC2985

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2985 as this object's host. The 1.76577° (105.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:08:19Z · 4 days · 19.06 r |
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
| Subject | **NGC2985** · `NGC2985` |
| Catalog display name | NGC2985 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.5 · 3.61′ × 2.92′ |
| Distance | — |
| Separation | 1.76577° · 105.95′ |
| Catalog description | NGC 2985 is a spiral galaxy located in the constellation Ursa Major. It is located at a distance of circa 70 million light years from Earth, which, given its apparent dimensions, means that NGC 2985 is about 95,000 light years across. It was discovered by William Herschel on April 3, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=148.7314991%2074.01329&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 45. [AT2026ahxp](https://www.wis-tns.org/object/2026ahxp) near IC5141

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5141 as this object's host. The 1.51041° (90.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T01:48:39Z · 6 days · 19.27 cyan |
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
| Subject | **IC5141** · `IC5141` |
| Catalog display name | IC5141 |
| Type / constellation | Galaxy · Indus |
| Catalog magnitude / angular size | 13.5 · 1.5′ × 1.18′ |
| Distance | 53,700 kpc |
| Separation | 1.51041° · 90.62′ |
| Catalog description | planetary nebula , stellar, pointlike, 15 mag |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.5794117%20-60.99851&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 46. [AT2026ahys](https://www.wis-tns.org/object/2026ahys) near NGC3998

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3998 as this object's host. The 1.18163° (70.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:46:48Z · 3 days · 18.52 g |
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
| Subject | **NGC3998** · `NGC3998` |
| Catalog display name | NGC3998 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.3 · 2.78′ × 2.26′ |
| Distance | — |
| Separation | 1.18163° · 70.90′ |
| Catalog description | NGC 3998 is a lenticular galaxy located in the constellation Ursa Major. It was discovered on April 14, 1789, by German-British astronomer William Herschel. At a distance of 45 million light-years, it is located relatively nearby, making it a well-studied object. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahys) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.2979519%2056.0480714&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 47. [AT2026ahze](https://www.wis-tns.org/object/2026ahze) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.92283° (115.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:33:40Z · 3 days · 18.71 g |
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
| Subject | **NGC797** · `IC 510 NED01` |
| Catalog display name | NGC797 |
| Type / constellation | Galaxy · Hya |
| Catalog magnitude / angular size | — · 0.33′ × 0.18′ |
| Distance | — |
| Separation | 1.92283° · 115.37′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahze) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.1394246%20-1.8788168&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 48. [AT2026ahzg](https://www.wis-tns.org/object/2026ahzg) near IC2152

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2152 as this object's host. The 1.50615° (90.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:43:26Z · 3 days · 18.77 orange |
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
| Subject | **IC2152** · `IC2152` |
| Catalog display name | IC2152 |
| Type / constellation | Galaxy · Lepus |
| Catalog magnitude / angular size | 13.5 · 1.65′ × 1.15′ |
| Distance | 29,000 kpc |
| Separation | 1.50615° · 90.37′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, several bright stars (pl.) following (eastward) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.57385%20-21.7961986&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 49. [AT2026ahzi](https://www.wis-tns.org/object/2026ahzi) near IC2166

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2166 as this object's host. The 1.06003° (63.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:14:55Z · 3 days · 19.05 orange |
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
| Subject | **IC2166** · `IC2166` |
| Catalog display name | IC2166 |
| Type / constellation | Galaxy · Lynx |
| Catalog magnitude / angular size | 12.4 · 2.2′ × 1.08′ |
| Distance | — |
| Separation | 1.06003° · 63.60′ |
| Catalog description | nebula; faint a single star preceding (westward) / pretty (adv., before F. B. L, S) 1', double a single star following (eastward) 3' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=96.8429833%2060.13855&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 50. [AT2026aiaf](https://www.wis-tns.org/object/2026aiaf) near Messier 32

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 32 as this object's host. The 1.66908° (100.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:53:43Z · 3 days · 19.19 r |
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
| Subject | **Messier 32** · `IC 1817 NED02` |
| Catalog display name | Messier 32 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.67′ × 0.43′ |
| Distance | 2.49 ly |
| Separation | 1.66908° · 100.14′ |
| Catalog description | Messier 32 is a dwarf "early-type" galaxy about 2,490,000 light-years (760,000 pc) from the Solar System, appearing in the constellation Andromeda. M32 is a satellite galaxy of the Andromeda Galaxy (M31) and was discovered by Guillaume Le Gentil in 1749. Messier 32 (also known as M32 and NGC 221) is a dwarf "early-type" galaxy about 2,490,000 light-years (760,000 pc) from the Solar System, appearing in the constellation Andromeda. M32 is a satellite galaxy of the Andromeda Galaxy (M31) and was discovered by Guillaume Le Gentil in 1749. The galaxy is a prototype of the relatively rare compact elliptical (cE) class. Half the stars are concentrated within the inner core, which has an effective radius of 330 light-years (100 pc). Densities in the central stellar cusp increase steeply, exceeding 3×107 M☉ pc−3 (30 million solar masses per cubic parsec) at the smallest sub-radii resolved by Hubble Space Telescope, and the half-light radius of this central star cluster is around 6 pc (20 light-years). Like more ordinary elliptical galaxies, M32 contains mostly old faint red and yellow stars with practically no dust or gas and consequently no current star formation. It does, however, show hints of star formation in the relatively recent past. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiaf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=38.7996362%209.5678786&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 51. [AT2026aiag](https://www.wis-tns.org/object/2026aiag) near IC 2814

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2814 as this object's host. The 0.21281° (12.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:56:06Z · 3 days · 19.72 r |
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
| Subject | **IC 2814** · `IC 2814` |
| Catalog display name | IC 2814 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 0.4′ × 0.29′ |
| Distance | — |
| Separation | 0.21281° · 12.77′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiag) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=171.3809651%209.8104808&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 52. [AT2026aiaz](https://www.wis-tns.org/object/2026aiaz) near NGC2655

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2655 as this object's host. The 1.67391° (100.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:42:07Z · 4 days · 19.46 g |
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
| Subject | **NGC2655** · `NGC2655` |
| Catalog display name | NGC2655 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 10.1 · 3.93′ × 2.06′ |
| Distance | 24,400 kpc |
| Separation | 1.67391° · 100.43′ |
| Catalog description | NGC 2655 is a lenticular galaxy in the constellation Camelopardalis. It is at a distance of 60 million light years from Earth. NGC 2655 is a Seyfert galaxy. The galaxy has asymmetric dust lanes in the centre of the galaxy, tidal arms and extended neutral hydrogen gas and may have recently experienced a merger. The complex dynamics of the HI and optical tails suggest the galaxy may have undergone more mergers in the past. A weak bar has been detected in infrared H band. The diameter of the disk of the galaxy is estimated to be 60 Kpc. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiaz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.9111933%2077.9501758&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 53. [AT2026aijg](https://www.wis-tns.org/object/2026aijg) near IC 5016

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5016 as this object's host. The 1.00177° (60.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T01:37:49Z · 0 days · 19.19 cyan |
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
| Subject | **IC 5016** · `IC 5016` |
| Catalog display name | NGC 568 |
| Type / constellation | Galaxy · Pav |
| Catalog magnitude / angular size | — · 0.63′ × 0.48′ |
| Distance | 266,000,000 ly |
| Separation | 1.00177° · 60.11′ |
| Catalog description | NGC 568, also commonly referred as IC 1709 is an unbarred lenticular galaxy in the constellation of Sculptor. The galaxy is 266 million light-years from Earth and was discovered by John Herschel on November 29, 1837, and Lewis Swift, an American astronomer who listed it and gave it the name IC 1709 on September 4, 1897. NGC 568, also commonly referred as IC 1709 is an unbarred lenticular galaxy in the constellation of Sculptor. The galaxy is 266 million light-years from Earth and was discovered by John Herschel on November 29, 1837, and Lewis Swift, an American astronomer who listed it and gave it the name IC 1709 on September 4, 1897. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5016 has the different designation NGC 568 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=306.021335%20-73.4669033&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 54. [AT2026aijv](https://www.wis-tns.org/object/2026aijv) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.27193° (76.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:53:54Z · 3 days · 18.99 r |
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
| Subject | **NGC3521** · `NGC3521` |
| Catalog display name | NGC3521 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 9.1 · 8.32′ × 4.47′ |
| Distance | — |
| Separation | 1.27193° · 76.32′ |
| Catalog description | NGC 3521, also known as the Bubble Galaxy, is a flocculent intermediate spiral galaxy located in the constellation Leo. Its velocity with respect to the cosmic microwave background is 1167 ± 26 km/s, which corresponds to a Hubble distance of 56.1 ± 4.1 Mly (17.21 ± 1.26 Mpc). However, 26 non-redshift measurements give a much closer distance of 37.17 ± 1.83 Mly (11.395 ± 0.56 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=165.6690592%20-1.1648599&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 55. [AT2026aguy](https://www.wis-tns.org/object/2026aguy) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.60878° (36.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:42:26Z · 13 days · 18.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4277....1P](https://ui.adsabs.harvard.edu/abs/2026TNSTR4277....1P/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2207 / IC 2163** · `IC 2617` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | — · 0.89′ × 0.45′ |
| Distance | 81 ly |
| Separation | 0.60878° · 36.53′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aguy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=165.222067%2038.105975&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 56. [AT2026ahaj](https://www.wis-tns.org/object/2026ahaj) near NGC1398

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1398 as this object's host. The 0.30038° (18.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:11:29Z · 9 days · 19.21 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4314....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4314....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1398** · `NGC1398` |
| Catalog display name | NGC1398 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 9.6 · 6.95′ × 4.91′ |
| Distance | — |
| Separation | 0.30038° · 18.02′ |
| Catalog description | NGC 1398 is an isolated barred spiral galaxy exhibiting a double ring structure. It is located 65 million light years from the Earth, in the constellation of Fornax. The galaxy, with a diameter of approximately 292,000 light years, is bigger than the Milky Way. Over 100 billion stars are in the galaxy. The discovery credit for NGC 1398 is often given to Friedrich Winnecke of Karlsruhe, Germany, who observed it on 17 December 1868, while he was searching for comets. German astronomer Wilhelm Tempel had first observed it on 9 October 1861, but he did not publish his observation until 1882. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahaj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.6838%20-26.636774&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 57. [AT2026ahnl](https://www.wis-tns.org/object/2026ahnl) near NGC2217

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2217 as this object's host. The 0.79462° (47.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:45:22Z · 9 days · 19.39 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4363....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4363....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2217** · `NGC2217` |
| Catalog display name | NGC2217 |
| Type / constellation | Galaxy · Canis Major |
| Catalog magnitude / angular size | 10.6 · 4.63′ × 4.12′ |
| Distance | — |
| Separation | 0.79462° · 47.68′ |
| Catalog description | NGC 2217 is a intergalactic celestial object of about 100 thousand light-years across that lies roughly 65 million light years from Earth in the constellation of Canis Major. It is part of the NGC 2217 Group of galaxies. It is classified as a barred spiral galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahnl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=94.641266%20-26.8343656&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 58. [AT2026ahtt](https://www.wis-tns.org/object/2026ahtt) near NGC2559

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2559 as this object's host. The 0.63978° (38.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T17:55:23Z · 8 days · 18.64 L |
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
| Subject | **NGC2559** · `NGC2559` |
| Catalog display name | NGC2559 |
| Type / constellation | Galaxy · Puppis |
| Catalog magnitude / angular size | 11.3 · 2.81′ × 1.34′ |
| Distance | 17,600 kpc |
| Separation | 0.63978° · 38.39′ |
| Catalog description | NGC 2559 is a barred spiral galaxy in the constellation Puppis. The galaxy lies about 60 million light years away from Earth based on redshift independent methods, which means, given its apparent dimensions, that NGC 2559 is approximately 90,000 light years across. It was discovered by John Herschel on February 5, 1837. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=124.384341%20-26.823491&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 59. [AT2026aica](https://www.wis-tns.org/object/2026aica) near IC1914

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1914 as this object's host. The 0.56142° (33.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:03:29Z · 9 days · 18.78 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4428....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4428....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1914** · `IC1914` |
| Catalog display name | IC1914 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 13 · 1.95′ × 1.45′ |
| Distance | 20,800 kpc |
| Separation | 0.56142° · 33.69′ |
| Catalog description | spiral? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aica) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.5925925%20-49.3085475&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 60. [SN2026agpk](https://www.wis-tns.org/object/2026agpk) near NGC2399

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2399 as this object's host. The 1.83747° (110.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.039 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-23T01:36:00Z · 14 days · 18.85 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4247....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4247....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2399** · `NGC2399` |
| Catalog display name | NGC2399 |
| Type / constellation | Nebula · Canis Minor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.83747° · 110.25′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agpk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=110.5360755%200.4624137&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 61. [SN2026ahmz](https://www.wis-tns.org/object/2026ahmz) near IC2084

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2084 as this object's host. The 1.11286° (66.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.04 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T14:16:05Z · 9 days · 19.33 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4367....1P](https://ui.adsabs.harvard.edu/abs/2026TNSTR4367....1P/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2084** · `IC2084` |
| Catalog display name | IC2084 |
| Type / constellation | Nebula · Caelum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.11286° · 66.77′ |
| Catalog description | faint, small in angular size, round, suspected |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahmz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.7003267%20-49.3084067&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 62. [AT2026ahya](https://www.wis-tns.org/object/2026ahya) near NGC1655

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1655 as this object's host. The 0.84874° (50.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T08:10:08Z · 3 days · 19.4 i |
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
| Subject | **NGC1655** · `NGC1655` |
| Catalog display name | NGC1655 |
| Type / constellation | Nebula · Taurus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.84874° · 50.92′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahya) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=72.2051321%2020.1663915&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 63. [AT2026agvt](https://www.wis-tns.org/object/2026agvt) near NGC3610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3610 as this object's host. The 1.92890° (115.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T11:54:34Z · 19 days · 18.75 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4287....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4287....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3610** · `NGC3610` |
| Catalog display name | NGC3610 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 2.39′ × 2.37′ |
| Distance | — |
| Separation | 1.92890° · 115.73′ |
| Catalog description | NGC 3610 is an elliptical galaxy in the constellation Ursa Major. It was discovered on 8 April 1793 by German-British astronomer William Herschel. This galaxy is located at a distance of 106 million light-years (32.5 Mpc) from the Milky Way, and is receding with a galacto-centric radial velocity of 1,819 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agvt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.0796722%2059.4570377&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 64. [AT2026agwa](https://www.wis-tns.org/object/2026agwa) near IC2988

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2988 as this object's host. The 1.54834° (92.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T12:58:52Z · 12 days · 18.08 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4287....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4287....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2988** · `IC2988` |
| Catalog display name | IC2988 |
| Type / constellation | Nebula · Virgo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.54834° · 92.90′ |
| Catalog description | extremely, excessively faint, resolvable (mottled, not resolved), a single star 11.5 south following 2'.7 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.0985899%201.8906472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 65. [AT2026ahab](https://www.wis-tns.org/object/2026ahab) near IC 530

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 530 as this object's host. The 1.84652° (110.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T11:45:47Z · 9 days · 19.2 V-crts |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4319....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4319....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 530** · `IC 530` |
| Catalog display name | NGC 530 |
| Type / constellation | Galaxy · Cnc |
| Catalog magnitude / angular size | — · 1.93′ × 0.31′ |
| Distance | — |
| Separation | 1.84652° · 110.79′ |
| Catalog description | NGC 530, also known as IC 106, is a lenticular galaxy in the constellation Cetus. It is approximately 226 million light years from the Milky Way and has a diameter of around 140,000 light years. The object was discovered on November 20, 1886, by the American astronomer Lewis A. Swift, who listed it as NGC 530, and rediscovered on November 16, 1887, by Guillaume Bigourdan, who listed it as IC 106. It is a member of the Abell 194 galaxy cluster. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 530 has the different designation NGC 530 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahab) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=137.76176%2013.4160957&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 66. [AT2026ahaq](https://www.wis-tns.org/object/2026ahaq) near NGC1532

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1532 as this object's host. The 0.03031° (1.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T07:00:34Z · 9 days · 21.91 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4318....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4318....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1532** · `NGC1532` |
| Catalog display name | NGC1532 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.1 · 11.27′ × 3.09′ |
| Distance | 17,800 kpc |
| Separation | 0.03031° · 1.82′ |
| Catalog description | NGC 1532, also known as Haley's Coronet, is an edge-on barred spiral galaxy located approximately 58 million light-years from the Solar System in the constellation Eridanus. The galaxy was discovered by James Dunlop on 29 October 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahaq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.028588%20-32.845618&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 67. [AT2026ahch](https://www.wis-tns.org/object/2026ahch) near NGC1792

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1792 as this object's host. The 1.51662° (91.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T14:57:59Z · 8 days · 19.49 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4340....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4340....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1792** · `NGC1792` |
| Catalog display name | NGC1792 |
| Type / constellation | Galaxy · Columba |
| Catalog magnitude / angular size | 10.2 · 5.52′ × 2.76′ |
| Distance | — |
| Separation | 1.51662° · 91.00′ |
| Catalog description | NGC 1792 is a spiral galaxy located in the southern Columba constellation. It was discovered by Scottish astronomer James Dunlop on October 4, 1826. This galaxy is located at a distance of about 36.4 million light-years and is receding from the Milky Way with a heliocentric radial velocity of 1,208 km/s. NGC 1792 is a member of the NGC 1808 cluster of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahch) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.54099%20-39.486475&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 68. [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 1.58832° (95.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:59:41Z · 8 days · 19.41 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4379....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4379....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1933** · `IC1933` |
| Catalog display name | IC1933 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.6 · 2.27′ × 1.21′ |
| Distance | 17,500 kpc |
| Separation | 1.58832° · 95.30′ |
| Catalog description | little (adv.); long (adj.) extended south preceding north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=48.7930337%20-52.69595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 69. [AT2026ahss](https://www.wis-tns.org/object/2026ahss) near IC 1913

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1913 as this object's host. The 1.87107° (112.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:11:30Z · 9 days · 19.4 L |
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
| Subject | **IC 1913** · `IC 1913` |
| Catalog display name | IC 1913 |
| Type / constellation | Galaxy · For |
| Catalog magnitude / angular size | — · 1.96′ × 0.41′ |
| Distance | 20.4 ly |
| Separation | 1.87107° · 112.26′ |
| Catalog description | IC 1913 is a barred spiral galaxy in the constellation Fornax. It belongs to the Fornax Cluster, which contains approximately 200 galaxies. IC 1913 is a barred spiral galaxy in the constellation Fornax. It belongs to the Fornax Cluster, which contains approximately 200 galaxies. It is 66.5 million light years distant from Earth, and based on its size on the night sky and distance, it is 37,000 light years in diameter. It was discovered by DeLisle Stewart in 1899. It is visible from the Southern Hemisphere using a telescope, but not with a naked eye. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahss) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.211946%20-30.686437&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 70. [AT2026ahun](https://www.wis-tns.org/object/2026ahun) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.10755° (6.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:56:09Z · 8 days · 22.34 g |
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
| Subject | **IC 1481** · `IC 1481` |
| Catalog display name | IC 1481 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.73′ × 0.65′ |
| Distance | 289 ly |
| Separation | 0.10755° · 6.45′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahun) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.926%205.825344&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 71. [AT2026ahxr](https://www.wis-tns.org/object/2026ahxr) near Wolf-Lundmark-Melotte

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Wolf-Lundmark-Melotte as this object's host. The 1.11363° (66.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T04:56:00Z · 3 days · 18.86 cyan |
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
| Subject | **Wolf-Lundmark-Melotte** · `WLM` |
| Catalog display name | Wolf-Lundmark-Melotte |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11 · 11.5′ × 4.2′ |
| Distance | 989 kpc |
| Separation | 1.11363° · 66.82′ |
| Catalog description | The Wolf–Lundmark–Melotte Galaxy (WLM) is a barred irregular galaxy discovered in 1909 by Max Wolf, located on the outer edges of the Local Group. The discovery of the nature of the galaxy was accredited to Knut Lundmark and Philibert Jacques Melotte in 1926. It is located in the constellation of Cetus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy.

[TNS object](https://www.wis-tns.org/object/2026ahxr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.27725%20-16.555155&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 72. [AT2026ahxx](https://www.wis-tns.org/object/2026ahxx) near IC310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC310 as this object's host. The 0.17679° (10.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T09:56:10Z · 12 days · 19.86 r |
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
| Subject | **IC310** · `IC310` |
| Catalog display name | IC310 |
| Type / constellation | Galaxy · Perseus |
| Catalog magnitude / angular size | 12.7 · 1.5′ × 1.42′ |
| Distance | 76,300 kpc |
| Separation | 0.17679° · 10.61′ |
| Catalog description | IC 310 is a lenticular galaxy located in the constellation Perseus. It is located 265 million light-years from Earth, which means, given its apparent dimensions, it is about 117,000 light-years across. The galaxy was discovered by Edward D. Swift on November 3, 1888. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.1658094%2041.5016248&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 73. [AT2026ahyr](https://www.wis-tns.org/object/2026ahyr) near NGC3610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3610 as this object's host. The 1.92150° (115.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T11:54:34Z · 19 days · 19.44 r |
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
| Subject | **NGC3610** · `NGC3610` |
| Catalog display name | NGC3610 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 2.39′ × 2.37′ |
| Distance | — |
| Separation | 1.92150° · 115.29′ |
| Catalog description | NGC 3610 is an elliptical galaxy in the constellation Ursa Major. It was discovered on 8 April 1793 by German-British astronomer William Herschel. This galaxy is located at a distance of 106 million light-years (32.5 Mpc) from the Milky Way, and is receding with a galacto-centric radial velocity of 1,819 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.2636622%2059.6648763&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 74. [AT2026aiju](https://www.wis-tns.org/object/2026aiju) near IC630

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC630 as this object's host. The 1.80723° (108.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:05:29Z · 8 days · 19.02 r |
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
| Subject | **IC630** · `IC630` |
| Catalog display name | IC630 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.5 · 2.12′ × 1.67′ |
| Distance | — |
| Separation | 1.80723° · 108.43′ |
| Catalog description | faint, extremely, excessively small in angular size, stellar, a single star 9.5 south preceding 1'.5 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiju) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.8376667%20-6.8961635&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 75. [AT2026ahra](https://www.wis-tns.org/object/2026ahra) near NGC796

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC796 as this object's host. The 1.40753° (84.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:37:04Z · 6 days · 19.18 orange |
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
| Subject | **NGC796** · `NGC796` |
| Catalog display name | NGC796 |
| Type / constellation | Open cluster · Hydrus |
| Catalog magnitude / angular size | — · 1.2′ × 1.1′ |
| Distance | 40 kpc |
| Separation | 1.40753° · 84.45′ |
| Catalog description | NGC 796 is a massive young open cluster located in the Hydrus constellation, with an estimated mass of 990M☉ and an estimated core radius of 4.56 ly. It is located in the Magellanic Bridge, between both Magellanic Clouds at an approximate distance of 192,432 light years, from the Earth and was discovered by 19th century English astronomer John Herschel on 18 September, 1835. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahra) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.22426%20-74.59953&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026ahrd](https://www.wis-tns.org/object/2026ahrd) near NGC2117

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2117 as this object's host. The 1.91418° (114.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T00:39:44Z · 5 days · 18.58 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4389....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4389....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2117** · `NGC2117` |
| Catalog display name | NGC2117 |
| Type / constellation | Open cluster · Dorado |
| Catalog magnitude / angular size | 11.7 · 2′ × 1.8′ |
| Distance | — |
| Separation | 1.91418° · 114.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.8697988%20-65.6966712&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 77. [AT2026ahti](https://www.wis-tns.org/object/2026ahti) near Melotte 53 (MEL53)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Melotte 53 (MEL53) as this object's host. The 1.56930° (94.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T16:08:18Z · 5 days · 18.69 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Melotte 53 (MEL53)** · `MEL53` |
| Catalog display name | Melotte 53 (MEL53) |
| Type / constellation | Globular cluster · Puppis |
| Catalog magnitude / angular size | 9.3 · 4.8′ × 4.8′ |
| Distance | 10.7 kpc |
| Separation | 1.56930° · 94.16′ |
| Catalog description | NGC 2298 is a globular cluster in the southern constellation of Puppis. Discovered by James Dunlop on May 30, 1826, it is probably a former member of the disputed Canis Major Dwarf galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahti) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=102.9086867%20-37.4819989&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 78. [AT2026ahvx](https://www.wis-tns.org/object/2026ahvx) near Caldwell 1 (C1)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 1 (C1) as this object's host. The 1.60616° (96.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T06:38:25Z · 3 days · 19.25 g |
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
| Subject | **Caldwell 1 (C1)** · `C1` |
| Catalog display name | Caldwell 1 (C1) |
| Type / constellation | Open cluster · Cepheus |
| Catalog magnitude / angular size | 8.1 · 14′ × 14′ |
| Distance | 2.047 kpc |
| Separation | 1.60616° · 96.37′ |
| Catalog description | NGC 188 is an open cluster in the constellation Cepheus. It was discovered by John Herschel in 1825. Unlike most open clusters that drift apart after a few million years because of the gravitational interaction of our Milky Way galaxy, NGC 188 lies far above the plane of the galaxy and is one of the most ancient of open clusters known, at approximately 6.8 billion years old. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.4141093%2085.8611066&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 79. [AT2026ahyn](https://www.wis-tns.org/object/2026ahyn) near NGC272

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC272 as this object's host. The 0.21538° (12.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:51:42Z · 3 days · 21 w |
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
| Subject | **NGC272** · `NGC272` |
| Catalog display name | NGC272 |
| Type / constellation | Open cluster · Andromeda |
| Catalog magnitude / angular size | — · 5′ × 5′ |
| Distance | — |
| Separation | 0.21538° · 12.92′ |
| Catalog description | NGC 272 is an open cluster located in the constellation Andromeda. It was discovered on August 2, 1864, by Heinrich d'Arrest. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=13.0629487%2035.9550818&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 80. [AT2026ahzj](https://www.wis-tns.org/object/2026ahzj) near NGC2879

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2879 as this object's host. The 1.72703° (103.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T14:05:41Z · 3 days · 18.72 orange |
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
| Subject | **NGC2879** · `NGC2879` |
| Catalog display name | NGC2879 |
| Type / constellation | Nebula · Hydra |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.72703° · 103.62′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=142.933285%20-12.3994325&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 81. [AT2026aiba](https://www.wis-tns.org/object/2026aiba) near NGC2404

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2404 as this object's host. The 1.36391° (81.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T11:08:40Z · 4 days · 19 g |
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
| Subject | **NGC2404** · `NGC2404` |
| Catalog display name | NGC2404 |
| Type / constellation | HII · Camelopardalis |
| Catalog magnitude / angular size | — · 0.4′ × 0.4′ |
| Distance | — |
| Separation | 1.36391° · 81.83′ |
| Catalog description | NGC 2404 is a massive H II region inside NGC 2403, a spiral galaxy in Camelopardalis. It was discovered on February 2, 1886 by Gulliaume Bigourdan. NGC 2404 is approximately 940 ly in diameter, making it one of the largest H II regions so far known. It is the largest H II region in NGC 2403, and lies at the outskirts of the galaxy, making for a striking similarity with NGC 604 in M33, both in size and location in the host galaxy. This H II region contains 30-40 Wolf-Rayet stars, and unlike the Tarantula Nebula, but similar to NGC 604, NGC 2404's open cluster is probably much less compact, so it probably looks like a large stellar association. This H II region is probably only a few million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiba) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.5782174%2065.6846644&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 82. [AT2026aibq](https://www.wis-tns.org/object/2026aibq) near NGC6669

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC6669 as this object's host. The 1.81749° (109.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T05:22:11Z · 2 days · 19.07 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4425....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4425....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC6669** · `NGC6669` |
| Catalog display name | NGC6669 |
| Type / constellation | Nebula · Hercules |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.81749° · 109.05′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=279.5271757%2024.0024549&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 83. [AT2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65298° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 2 days · 19.17 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4450....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4450....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5194** · `IC5194` |
| Catalog display name | IC5194 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · 0.2′ × 0.2′ |
| Distance | — |
| Separation | 1.65298° · 99.18′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiep) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=335.3713668%20-14.6685598&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 84. [AT2026aihy](https://www.wis-tns.org/object/2026aihy) near NGC56

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC56 as this object's host. The 1.97482° (118.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T14:28:11Z · 1 days · 19.5 Clear |
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
| Subject | **NGC56** · `NGC56` |
| Catalog display name | NGC56 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.97482° · 118.49′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aihy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.9740682%2013.2279393&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 85. [AT2026aija](https://www.wis-tns.org/object/2026aija) near NGC796

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC796 as this object's host. The 1.18846° (71.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T02:00:00Z · 0 days · 19.1 cyan |
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
| Subject | **NGC796** · `NGC796` |
| Catalog display name | NGC796 |
| Type / constellation | Open cluster · Hydrus |
| Catalog magnitude / angular size | — · 1.2′ × 1.1′ |
| Distance | 40 kpc |
| Separation | 1.18846° · 71.31′ |
| Catalog description | NGC 796 is a massive young open cluster located in the Hydrus constellation, with an estimated mass of 990M☉ and an estimated core radius of 4.56 ly. It is located in the Magellanic Bridge, between both Magellanic Clouds at an approximate distance of 192,432 light years, from the Earth and was discovered by 19th century English astronomer John Herschel on 18 September, 1835. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aija) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.309077%20-74.807716&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 86. [SN2026afqd](https://www.wis-tns.org/object/2026afqd) near Lynds Bright Nebula 556 (LBN556)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 556 (LBN556) as this object's host. The 1.09316° (65.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIP |
| Redshift | 0.014657 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T02:14:46Z · 20 days · 19.18 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4169....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4169....1O/abstract) |
| Classification references | [2026TNSCR4207....1W](https://ui.adsabs.harvard.edu/abs/2026TNSCR4207....1W/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 556 (LBN556)** · `LBN556` |
| Catalog display name | Lynds Bright Nebula 556 (LBN556) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 60′ × 10′ |
| Distance | — |
| Separation | 1.09316° · 65.59′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026afqd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=6.3660803%2020.2437034&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 87. [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) near Lynds Bright Nebula 718 (LBN718)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 718 (LBN718) as this object's host. The 0.53253° (31.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:11:33Z · 3 days · 19.39 r |
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
| Subject | **Lynds Bright Nebula 718 (LBN718)** · `LBN718` |
| Catalog display name | Lynds Bright Nebula 718 (LBN718) |
| Type / constellation | HII · Perseus |
| Catalog magnitude / angular size | — · 210′ × 30′ |
| Distance | — |
| Separation | 0.53253° · 31.95′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahxz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.307368%2038.0685243&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 88. [AT2026aiap](https://www.wis-tns.org/object/2026aiap) near Lynds Bright Nebula 437 (LBN437)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 437 (LBN437) as this object's host. The 0.83711° (50.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T00:08:34Z · 3 days · 18.98 wide |
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
| Subject | **Lynds Bright Nebula 437 (LBN437)** · `LBN437` |
| Catalog display name | Lynds Bright Nebula 437 (LBN437) |
| Type / constellation | HII · Lacerta |
| Catalog magnitude / angular size | — · 75′ × 20′ |
| Distance | — |
| Separation | 0.83711° · 50.23′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiap) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=337.1977485%2040.0120338&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 89. [AT2026ahsf](https://www.wis-tns.org/object/2026ahsf) near IC1892

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1892 as this object's host. The 0.43441° (26.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:03:20Z · 7 days · 20.36 L |
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
| Subject | **IC1892** · `IC1892` |
| Catalog display name | IC1892 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 13.8 · 1.78′ × 0.98′ |
| Distance | — |
| Separation | 0.43441° · 26.06′ |
| Catalog description | very faint, large, near 1230 |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.040398%20-23.485108&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 90. [AT2026ahsl](https://www.wis-tns.org/object/2026ahsl) near NGC1300

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1300 as this object's host. The 0.61843° (37.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:21:58Z · 7 days · 20.07 L |
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
| Subject | **NGC1300** · `NGC1300` |
| Catalog display name | NGC1300 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.5 · 5.96′ × 3.06′ |
| Distance | — |
| Separation | 0.61843° · 37.11′ |
| Catalog description | NGC 1300 is a barred spiral galaxy located about 69 million light-years away in the constellation Eridanus. The galaxy is about 130,000 light-years across. It is a member of the Eridanus Cluster, a cluster of 200 galaxies, in a subgroup of 2-4 galaxies in the cluster known as the NGC 1300 Group. It was discovered by John Herschel in 1835. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.82466%20-20.023126&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 91. [AT2026ahtr](https://www.wis-tns.org/object/2026ahtr) near IC163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC163 as this object's host. The 0.83764° (50.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T06:58:54Z · 5 days · 21.33 w |
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
| Subject | **IC163** · `IC163` |
| Catalog display name | IC163 |
| Type / constellation | Galaxy · Aries |
| Catalog magnitude / angular size | 13.3 · 1.62′ × 0.73′ |
| Distance | 25,600 kpc |
| Separation | 0.83764° · 50.26′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.4337882%2020.8937263&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 92. [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 0.59209° (35.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:45:50Z · 5 days · 19.59 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1933** · `IC1933` |
| Catalog display name | IC1933 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.6 · 2.27′ × 1.21′ |
| Distance | 17,500 kpc |
| Separation | 0.59209° · 35.53′ |
| Catalog description | little (adv.); long (adj.) extended south preceding north following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.618572%20-52.441701&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 93. [AT2026ahup](https://www.wis-tns.org/object/2026ahup) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.66908° (40.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:50:52Z · 7 days · 22.12 r |
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
| Subject | **NGC488** · `NGC488` |
| Catalog display name | NGC488 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 10.3 · 5.05′ × 3.66′ |
| Distance | 28,100 kpc |
| Separation | 0.66908° · 40.14′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahup) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.104083%205.145006&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 94. [AT2026ahwx](https://www.wis-tns.org/object/2026ahwx) near Caldwell 51 (C51)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 51 (C51) as this object's host. The 0.76630° (45.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:37:55Z · 7 days · 22.16 r |
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
| Subject | **Caldwell 51 (C51)** · `C51` |
| Catalog display name | Caldwell 51 (C51) |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 9 · 12′ × 11′ |
| Distance | — |
| Separation | 0.76630° · 45.98′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.538583%202.512672&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 95. [AT2026ahwz](https://www.wis-tns.org/object/2026ahwz) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.95545° (57.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:05:16Z · 7 days · 22.01 r |
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
| Subject | **NGC741** · `NGC741` |
| Catalog display name | NGC741 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 11.3 · 2.83′ × 2.33′ |
| Distance | — |
| Separation | 0.95545° · 57.33′ |
| Catalog description | NGC 741, also known as PGC 7252, is a formerly active radio galaxy in the constellation of Pisces. Located 74.13 Mpc away, NGC 741 is part of a group of galaxies including NGC 742 and PGC 7250. NGC 741 and NGC 742 recently collided, although the disruption was minor. Radio filaments have been found connecting NGC 741 to NGC 742, and due to the bent structure of the radio filaments, NGC 741 is estimated to be moving at 1400 km/s with respect to its local group, suggesting that ram-pressure stripping was created as a product of the former merger. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.021708%205.409361&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 96. [AT2026ahxf](https://www.wis-tns.org/object/2026ahxf) near IC 1746

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1746 as this object's host. The 0.76507° (45.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:00:00Z · 5 days · 22.12 r |
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
| Subject | **IC 1746** · `IC 1746` |
| Catalog display name | NGC 502 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.58′ × 0.47′ |
| Distance | 113 ly |
| Separation | 0.76507° · 45.90′ |
| Catalog description | NGC 502, also occasionally referred to as PGC 5034 or UGC 922, is a lenticular galaxy in the constellation Pisces. It is located approximately 113 million light-years from the Solar System and was discovered on 25 September 1862 by German astronomer Heinrich Louis d'Arrest. When the Morphological Catalogue of Galaxies was published between 1962 and 1974, the identifications of NGC 502 and NGC 505 were reversed. In reality, NGC 502 is equal to MGC +01-04-041 and not MCG +01-04-043 as noted in the catalogue. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1746 has the different designation NGC 502 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.932833%204.427867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 97. [AT2026ahye](https://www.wis-tns.org/object/2026ahye) near IC2421

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2421 as this object's host. The 0.96852° (58.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:36Z · 3 days · 20.17 g |
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
| Subject | **IC2421** · `IC2421` |
| Catalog display name | IC2421 |
| Type / constellation | Galaxy · Cancer |
| Catalog magnitude / angular size | 13.3 · 1.41′ × 0.95′ |
| Distance | 19,500 kpc |
| Separation | 0.96852° · 58.11′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, diffused, difficult |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahye) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=134.123407%2031.8249174&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 98. [AT2026aiax](https://www.wis-tns.org/object/2026aiax) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.49618° (29.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:23:51Z · 7 days · 22.27 g |
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
| Subject | **NGC1527** · `NGC1527` |
| Catalog display name | NGC1527 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 10.8 · 4.58′ × 1.79′ |
| Distance | 17,500 kpc |
| Separation | 0.49618° · 29.77′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiax) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=61.4588819%20-47.6509559&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 99. [AT2026aicj](https://www.wis-tns.org/object/2026aicj) near IC1531

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1531 as this object's host. The 0.49233° (29.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T10:12:50Z · 2 days · 20.1 L |
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
| Subject | **IC1531** · `IC1531` |
| Catalog display name | IC1531 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 13.5 · 1.89′ × 1.31′ |
| Distance | 93,400 kpc |
| Separation | 0.49233° · 29.54′ |
| Catalog description | very faint, very small in angular size, round, double a single star north |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=2.349332%20-31.786248&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 100. [AT2026aiij](https://www.wis-tns.org/object/2026aiij) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 0.81942° (49.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 0 days · 23.51 r |
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
| Subject | **IC2000** · `IC2000` |
| Catalog display name | IC2000 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.4 · 4.88′ × 0.85′ |
| Distance | 18,700 kpc |
| Separation | 0.81942° · 49.17′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiij) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.4981881%20-49.0327579&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 101. [AT2026aike](https://www.wis-tns.org/object/2026aike) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.28536° (17.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T07:22:35Z · 0 days · 22.75 r |
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
| Subject | **NGC1543** · `NGC1543` |
| Catalog display name | NGC1543 |
| Type / constellation | Galaxy · Reticulum |
| Catalog magnitude / angular size | 10.2 · 3.66′ × 0.86′ |
| Distance | — |
| Separation | 0.28536° · 17.12′ |
| Catalog description | NGC 1543 is a barred lenticular galaxy in the constellation Reticulum. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 1543 is approximately 100,000 light years across. It was discovered by James Dunlop on November 5, 1826. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aike) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.78206%20-57.547554&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 102. [AT2026aikf](https://www.wis-tns.org/object/2026aikf) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.39139° (23.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T07:22:35Z · 0 days · 21.83 r |
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
| Subject | **NGC1543** · `NGC1543` |
| Catalog display name | NGC1543 |
| Type / constellation | Galaxy · Reticulum |
| Catalog magnitude / angular size | 10.2 · 3.66′ × 0.86′ |
| Distance | — |
| Separation | 0.39139° · 23.48′ |
| Catalog description | NGC 1543 is a barred lenticular galaxy in the constellation Reticulum. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 1543 is approximately 100,000 light years across. It was discovered by James Dunlop on November 5, 1826. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.461379%20-57.819915&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 103. [AT2026aiki](https://www.wis-tns.org/object/2026aiki) near IC 230

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 230 as this object's host. The 0.98290° (58.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T11:50:45Z · 0 days · 20.27 L |
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
| Subject | **IC 230** · `IC 230` |
| Catalog display name | NGC 945 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.64′ × 0.42′ |
| Distance | — |
| Separation | 0.98290° · 58.97′ |
| Catalog description | NGC 945 is a barred spiral galaxy in the constellation Cetus, located south of the celestial equator. It is estimated to be 200 million light-years from the Milky Way, and about 135,000 light-years in diameter. The object was discovered by astronomer William Herschel on November 28, 1785. It is near NGC 948, with which it forms a gravitationally bound pair of galaxies. In the same area of the sky there are the galaxies NGC 942, NGC 943, NGC 950, and IC 230. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 230 has the different designation NGC 945 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiki) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.84479%20-9.911554&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 104. [SN2026agpt](https://www.wis-tns.org/object/2026agpt) near IC353

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 57/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC353 as this object's host. The 0.25824° (15.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.068 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T07:25:21Z · 17 days · 20.26 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4268....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4268....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC353** · `IC353` |
| Catalog display name | IC353 |
| Type / constellation | Nebula · Taurus |
| Catalog magnitude / angular size | — · 181.97′ × 30.2′ |
| Distance | — |
| Separation | 0.25824° · 15.49′ |
| Catalog description | IC 4040 is a type SABc spiral galaxy with a bar in Coma Berenices. It is located 353 million light-years away from the Solar System and has an estimated diameter of 105,000 light-years making it slightly larger than the Milky Way. IC 4040 was discovered on April 12, 1891, by Guillaume Bigourdan and is a member of the Coma Cluster. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agpt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.5279961%2025.9254397&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 105. [AT2026agxx](https://www.wis-tns.org/object/2026agxx) near NGC7134

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7134 as this object's host. The 1.77788° (106.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T09:33:30Z · 10 days · 19.03 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4298....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4298....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7134** · `NGC7134` |
| Catalog display name | NGC7134 |
| Type / constellation | Nebula · Capricornus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.77788° · 106.67′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agxx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=325.8262356%20-14.3304511&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 106. [AT2026ahfn](https://www.wis-tns.org/object/2026ahfn) near Lynds Bright Nebula 870 (LBN870)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 870 (LBN870) as this object's host. The 1.01310° (60.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:42:00Z · 7 days · 19.21 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4362....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4362....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 870 (LBN870)** · `LBN870` |
| Catalog display name | Lynds Bright Nebula 870 (LBN870) |
| Type / constellation | HII · Eridanus |
| Catalog magnitude / angular size | — · 65′ × 2′ |
| Distance | — |
| Separation | 1.01310° · 60.79′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahfn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.3395103%20-10.0928893&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 107. [AT2026ahrb](https://www.wis-tns.org/object/2026ahrb) near IC1788

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1788 as this object's host. The 0.89675° (53.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T23:49:19Z · 33 days · 13 Other |
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
| Subject | **IC1788** · `IC1788` |
| Catalog display name | IC1788 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 12.4 · 2.53′ × 1.07′ |
| Distance | 49,500 kpc |
| Separation | 0.89675° · 53.80′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, 2 stars (pl.) north following |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.866792%20-30.762833&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 108. [AT2026ahsh](https://www.wis-tns.org/object/2026ahsh) near NGC1498

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1498 as this object's host. The 1.89281° (113.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T16:59:57Z · 9 days · 19.05 L |
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
| Subject | **NGC1498** · `NGC1498` |
| Catalog display name | NGC1498 |
| Type / constellation | Open cluster · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.89281° · 113.57′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.3124105%20-12.7978488&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 109. [AT2026ahxo](https://www.wis-tns.org/object/2026ahxo) near Lynds Bright Nebula 484 (LBN484)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 484 (LBN484) as this object's host. The 1.59750° (95.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T00:17:28Z · 3 days · 18.88 wide |
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
| Subject | **Lynds Bright Nebula 484 (LBN484)** · `LBN484` |
| Catalog display name | Lynds Bright Nebula 484 (LBN484) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 60′ × 40′ |
| Distance | — |
| Separation | 1.59750° · 95.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahxo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.472256%2028.5747&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 110. [AT2026ahxq](https://www.wis-tns.org/object/2026ahxq) near Lynds Bright Nebula 100 (LBN100)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 100 (LBN100) as this object's host. The 1.77430° (106.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:05:52Z · 3 days · 19.18 cyan |
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
| Subject | **Lynds Bright Nebula 100 (LBN100)** · `LBN100` |
| Catalog display name | Lynds Bright Nebula 100 (LBN100) |
| Type / constellation | HII · Aquila |
| Catalog magnitude / angular size | — · 40′ × 12′ |
| Distance | — |
| Separation | 1.77430° · 106.46′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahxq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=298.01156%20-7.68013&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 111. [AT2026aibu](https://www.wis-tns.org/object/2026aibu) near IC640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC640 as this object's host. The 1.43879° (86.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:42:26Z · 13 days · 19.47 r |
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
| Subject | **IC640** · `IC640` |
| Catalog display name | IC640 |
| Type / constellation | Nebula · Leo Minor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.43879° · 86.33′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, extended, double ? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.320873%2033.8973004&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 112. [AT2026agyh](https://www.wis-tns.org/object/2026agyh) near Lynds Bright Nebula 1024 (LBN1024)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1024 (LBN1024) as this object's host. The 0.77188° (46.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T11:37:00Z · 18 days · 19.13 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4300....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4300....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 1024 (LBN1024)** · `LBN1024` |
| Catalog display name | Lynds Bright Nebula 1024 (LBN1024) |
| Type / constellation | HII · Monoceros |
| Catalog magnitude / angular size | — · 90′ × 20′ |
| Distance | — |
| Separation | 0.77188° · 46.31′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026agyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=108.198208%20-8.243386&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 113. [AT2026ahho](https://www.wis-tns.org/object/2026ahho) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.70871° (102.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:59:10Z · 7 days · 21.9 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4361....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR4361....1F/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1495** · `IC1495` |
| Catalog display name | IC1495 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13 · 1.33′ × 0.83′ |
| Distance | 80,650 kpc |
| Separation | 1.70871° · 102.52′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahho) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.8608986%20-11.9832835&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 114. [AT2026ahif](https://www.wis-tns.org/object/2026ahif) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.45000° (87.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:26:25Z · 7 days · 20.62 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4361....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR4361....1F/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2000** · `IC2000` |
| Catalog display name | IC2000 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.4 · 4.88′ × 0.85′ |
| Distance | 18,700 kpc |
| Separation | 1.45000° · 87.00′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahif) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.6453789%20-50.0041359&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 115. [AT2026ahiv](https://www.wis-tns.org/object/2026ahiv) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.93793° (116.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:33:32Z · 7 days · 22.17 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4361....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR4361....1F/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1495** · `IC1495` |
| Catalog display name | IC1495 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13 · 1.33′ × 0.83′ |
| Distance | 80,650 kpc |
| Separation | 1.93793° · 116.28′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahiv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.4642577%20-15.4103602&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 116. [AT2026ahom](https://www.wis-tns.org/object/2026ahom) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.66970° (100.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:26:35Z · 6 days · 23.23 r |
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
| Subject | **IC2000** · `IC2000` |
| Catalog display name | IC2000 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.4 · 4.88′ × 0.85′ |
| Distance | 18,700 kpc |
| Separation | 1.66970° · 100.18′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahom) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.9314983%20-50.1374614&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 117. [AT2026ahoo](https://www.wis-tns.org/object/2026ahoo) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.20295° (72.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:26:35Z · 6 days · 23.17 r |
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
| Subject | **IC2000** · `IC2000` |
| Catalog display name | IC2000 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 12.4 · 4.88′ × 0.85′ |
| Distance | 18,700 kpc |
| Separation | 1.20295° · 72.18′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.0994545%20-48.758164&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 118. [AT2026ahop](https://www.wis-tns.org/object/2026ahop) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.32446° (79.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:27:15Z · 6 days · 22.66 r |
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
| Subject | **NGC1527** · `NGC1527` |
| Catalog display name | NGC1527 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 10.8 · 4.58′ × 1.79′ |
| Distance | 17,500 kpc |
| Separation | 1.32446° · 79.47′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahop) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.890858%20-47.3516731&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 119. [AT2026ahor](https://www.wis-tns.org/object/2026ahor) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.72801° (103.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:26:35Z · 6 days · 23.03 r |
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
| Subject | **NGC1527** · `NGC1527` |
| Catalog display name | NGC1527 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 10.8 · 4.58′ × 1.79′ |
| Distance | 17,500 kpc |
| Separation | 1.72801° · 103.68′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahor) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.9427897%20-48.8632099&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 120. [AT2026ahos](https://www.wis-tns.org/object/2026ahos) near IC2035

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2035 as this object's host. The 1.49867° (89.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:27:15Z · 6 days · 22.84 r |
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
| Subject | **IC2035** · `IC2035` |
| Catalog display name | IC2035 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 11.8 · 1.41′ × 1.17′ |
| Distance | 9,590 kpc |
| Separation | 1.49867° · 89.92′ |
| Catalog description | faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahos) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.9054844%20-46.4820715&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 121. [AT2026ahpa](https://www.wis-tns.org/object/2026ahpa) near IC2035

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2035 as this object's host. The 1.23294° (73.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:27:15Z · 6 days · 23.22 r |
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
| Subject | **IC2035** · `IC2035` |
| Catalog display name | IC2035 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 11.8 · 1.41′ × 1.17′ |
| Distance | 9,590 kpc |
| Separation | 1.23294° · 73.98′ |
| Catalog description | faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.7085336%20-46.7095625&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 122. [AT2026ahpb](https://www.wis-tns.org/object/2026ahpb) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.25162° (75.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:26:35Z · 6 days · 23.84 r |
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
| Subject | **NGC1527** · `NGC1527` |
| Catalog display name | NGC1527 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 10.8 · 4.58′ × 1.79′ |
| Distance | 17,500 kpc |
| Separation | 1.25162° · 75.10′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.2902276%20-48.218699&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 123. [AT2026ahqo](https://www.wis-tns.org/object/2026ahqo) near NGC524

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC524 as this object's host. The 1.20553° (72.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:05:28Z · 7 days · 20.04 L |
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
| Subject | **NGC524** · `NGC524` |
| Catalog display name | NGC524 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 10.3 · 3.37′ × 3.35′ |
| Distance | — |
| Separation | 1.20553° · 72.33′ |
| Catalog description | NGC 524 is a lenticular galaxy in the constellation Pisces. It is at a distance of about 90 million light-years away from Earth. In the central bulge of the galaxy is visible gas forming a spiral structure. It is the largest galaxy in the small NGC 524 group of galaxies, which is associated with NGC 488 and its group. It was discovered by William Herschel on 4 September 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.174893%208.877251&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 124. [AT2026ahqw](https://www.wis-tns.org/object/2026ahqw) near IC2035

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2035 as this object's host. The 1.30880° (78.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:23:51Z · 7 days · 21.24 g |
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
| Subject | **IC2035** · `IC2035` |
| Catalog display name | IC2035 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 11.8 · 1.41′ × 1.17′ |
| Distance | 9,590 kpc |
| Separation | 1.30880° · 78.53′ |
| Catalog description | faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.861781%20-46.195377&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 125. [AT2026ahsg](https://www.wis-tns.org/object/2026ahsg) near IC1914

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1914 as this object's host. The 1.33500° (80.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:11:34Z · 7 days · 20.33 L |
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
| Subject | **IC1914** · `IC1914` |
| Catalog display name | IC1914 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 13 · 1.95′ × 1.45′ |
| Distance | 20,800 kpc |
| Separation | 1.33500° · 80.10′ |
| Catalog description | spiral? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=48.310725%20-48.725807&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 126. [AT2026ahsw](https://www.wis-tns.org/object/2026ahsw) near IC1812

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1812 as this object's host. The 1.90241° (114.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:23:14Z · 7 days · 20.18 L |
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
| Subject | **IC1812** · `IC1812` |
| Catalog display name | IC1812 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 12.2 · 2.08′ × 1.6′ |
| Distance | 70,300 kpc |
| Separation | 1.90241° · 114.14′ |
| Catalog description | very faint, brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.53445%20-44.613158&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 127. [AT2026ahud](https://www.wis-tns.org/object/2026ahud) near NGC1209

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1209 as this object's host. The 1.34437° (80.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:45:08Z · 5 days · 20.6 w |
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
| Subject | **NGC1209** · `NGC1209` |
| Catalog display name | NGC1209 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 11.4 · 2.25′ × 0.94′ |
| Distance | — |
| Separation | 1.34437° · 80.66′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahud) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.7878629%20-14.2934618&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 128. [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) near IC1401

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1401 as this object's host. The 1.09402° (65.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:14:32Z · 6 days · 19.8 i |
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
| Subject | **IC1401** · `IC1401` |
| Catalog display name | IC1401 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13.7 · 1.68′ × 0.56′ |
| Distance | 67,900 kpc |
| Separation | 1.09402° · 65.64′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=325.76423%202.5100968&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026ahuq](https://www.wis-tns.org/object/2026ahuq) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.22452° (73.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T14:49:55Z · 6 days · 22.18 g |
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
| Subject | **NGC 2207 / IC 2163** · `IC 214` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.58′ × 0.45′ |
| Distance | 81 ly |
| Separation | 1.22452° · 73.47′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.310833%205.377731&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026ahvb](https://www.wis-tns.org/object/2026ahvb) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.81892° (109.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:58:17Z · 5 days · 20.07 L |
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
| Subject | **NGC 2207 / IC 2163** · `IC 2064` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Eri |
| Catalog magnitude / angular size | — · 0.53′ × 0.47′ |
| Distance | 81 ly |
| Separation | 1.81892° · 109.14′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=67.116014%20-17.048814&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026ahvp](https://www.wis-tns.org/object/2026ahvp) near NGC3359

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3359 as this object's host. The 1.87119° (112.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:37:26Z · 4 days · 19.66 r |
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
| Subject | **NGC3359** · `NGC3359` |
| Catalog display name | NGC3359 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.6 · 4.07′ × 2.83′ |
| Distance | — |
| Separation | 1.87119° · 112.27′ |
| Catalog description | NGC 3359 is a barred spiral galaxy located 59 million light-years from Earth, in the constellation of Ursa Major. It was discovered on November 28, 1793, by the astronomer William Herschel. The central bar is approximately 500 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=165.2708425%2064.1887255&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026ahwu](https://www.wis-tns.org/object/2026ahwu) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.63058° (97.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:20:38Z · 7 days · 22.47 r |
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
| Subject | **IC 1507** · `IC 1507` |
| Catalog display name | IC 1613 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.29′ × 0.47′ |
| Distance | — |
| Separation | 1.63058° · 97.83′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=357.743625%200.781817&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 133. [AT2026ahxa](https://www.wis-tns.org/object/2026ahxa) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.79834° (107.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:14:24Z · 5 days · 21.94 g |
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
| Subject | **IC 1481** · `IC 1481` |
| Catalog display name | IC 1481 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.73′ × 0.65′ |
| Distance | 289 ly |
| Separation | 1.79834° · 107.90′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.875542%204.395161&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 134. [AT2026ahxb](https://www.wis-tns.org/object/2026ahxb) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.18297° (70.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:24:28Z · 5 days · 22.15 g |
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
| Subject | **IC 1507** · `IC 1507` |
| Catalog display name | IC 1613 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.29′ × 0.47′ |
| Distance | — |
| Separation | 1.18297° · 70.98′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=356.521833%202.864158&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 135. [AT2026ahyt](https://www.wis-tns.org/object/2026ahyt) near IC2378

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2378 as this object's host. The 1.23433° (74.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:41:55Z · 3 days · 19.72 g |
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
| Subject | **IC2378** · `IC2378` |
| Catalog display name | IC2378 |
| Type / constellation | Galaxy · Cancer |
| Catalog magnitude / angular size | 13.2 · 1.31′ × 0.92′ |
| Distance | 198,000 kpc |
| Separation | 1.23433° · 74.06′ |
| Catalog description | faint, small in angular size, round, gradually little (adv.); long (adj.) brighter middle, or in the middle, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=128.486987%2030.0472358&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 136. [AT2026ahyx](https://www.wis-tns.org/object/2026ahyx) near IC 1931

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1931 as this object's host. The 1.88856° (113.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T11:24:58Z · 4 days · 21.31 w |
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
| Subject | **IC 1931** · `IC 1931` |
| Catalog display name | NGC5162 |
| Type / constellation | Galaxy · Tau |
| Catalog magnitude / angular size | — · 0.8′ × 0.76′ |
| Distance | — |
| Separation | 1.88856° · 113.31′ |
| Catalog description | NGC 5162 is a very large spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 7125 ± 20 km/s, which corresponds to a Hubble distance of 342.8 ± 24.0 Mly (105.09 ± 7.36 Mpc). In addition, 11 non redshift measurements give a distance of 303.71 ± 12.41 Mly (93.118 ± 3.806 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 15 March 1784. It was also observed by Lewis Swift on 19 April 1887, resulting in the galaxy being included twice in the New General Catalogue, as both NGC 5162 and NGC 5174. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1931 has the different designation NGC5162 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.7503675%203.5693118&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 137. [AT2026ahyz](https://www.wis-tns.org/object/2026ahyz) near IC1650

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1650 as this object's host. The 1.70126° (102.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:11:01Z · 7 days · 20.14 L |
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
| Subject | **IC1650** · `IC1650` |
| Catalog display name | IC1650 |
| Type / constellation | Galaxy · Phoenix |
| Catalog magnitude / angular size | 13.6 · 1.32′ × 0.65′ |
| Distance | 92,400 kpc |
| Separation | 1.70126° · 102.08′ |
| Catalog description | considerably faint, small in angular size, much / magnitude extended 55deg , considerably brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.658835%20-50.868134&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 138. [AT2026ahza](https://www.wis-tns.org/object/2026ahza) near IC1997

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1997 as this object's host. The 1.88878° (113.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:53:54Z · 5 days · 20.03 L |
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
| Subject | **IC1997** · `IC1997` |
| Catalog display name | IC1997 |
| Type / constellation | Galaxy · Reticulum |
| Catalog magnitude / angular size | 13.5 · 1.01′ × 0.7′ |
| Distance | 74,800 kpc |
| Separation | 1.88878° · 113.33′ |
| Catalog description | extremely, excessively faint, very small in angular size, round, considerably brighter middle, or in the middle, stellar, pointlike nucleus, or to a nucleus |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahza) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.793404%20-59.885527&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 139. [AT2026aian](https://www.wis-tns.org/object/2026aian) near NGC720

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC720 as this object's host. The 1.33774° (80.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T08:28:12Z · 3 days · 21.33 w |
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
| Subject | **NGC720** · `NGC720` |
| Catalog display name | NGC720 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 10.1 · 4.49′ × 2.37′ |
| Distance | — |
| Separation | 1.33774° · 80.26′ |
| Catalog description | NGC 720 is an elliptical galaxy located in the constellation Cetus. It is located at a distance of about 80 million light years from Earth, which, given its apparent dimensions, means that NGC 720 is about 110,000 light years across. It was discovered by William Herschel on October 3, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies about three and a half degrees south and slightly east from zeta Ceti. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aian) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.2017832%20-14.6085502&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 140. [AT2026aiar](https://www.wis-tns.org/object/2026aiar) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.27730° (76.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:41:48Z · 3 days · 20.11 w |
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
| Subject | **NGC 2207 / IC 2163** · `IC 2196` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Gem |
| Catalog magnitude / angular size | — · 1.67′ × 0.86′ |
| Distance | 81 ly |
| Separation | 1.27730° · 76.64′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiar) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=112.1559399%2030.9283846&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 141. [AT2026aibw](https://www.wis-tns.org/object/2026aibw) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.77222° (106.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:27:34Z · 2 days · 19.69 g |
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
| Subject | **NGC 2207 / IC 2163** · `IC 2544` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · LMi |
| Catalog magnitude / angular size | — · 0.52′ × 0.4′ |
| Distance | 81 ly |
| Separation | 1.77222° · 106.33′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.6193386%2035.0706017&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 142. [AT2026aick](https://www.wis-tns.org/object/2026aick) near NGC7410

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7410 as this object's host. The 1.11460° (66.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:52:52Z · 2 days · 19.75 L |
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
| Subject | **NGC7410** · `NGC7410` |
| Catalog display name | NGC7410 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 11.2 · 6.01′ × 1.77′ |
| Distance | 42,700 kpc |
| Separation | 1.11460° · 66.88′ |
| Catalog description | NGC 7410 is a barred spiral galaxy located in the constellation Grus. It is about 122 million light-years away. It was discovered on 15 July 1826, by James Dunlop. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aick) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.576605%20-39.014223&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 143. [AT2026aicm](https://www.wis-tns.org/object/2026aicm) near IC 2039

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2039 as this object's host. The 1.00001° (60.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:09:56Z · 5 days · 19.97 L |
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
| Subject | **IC 2039** · `IC 2039` |
| Catalog display name | NGC 1533 |
| Type / constellation | Galaxy · Dor |
| Catalog magnitude / angular size | — · 1.09′ × 0.93′ |
| Distance | 62 ly |
| Separation | 1.00001° · 60.00′ |
| Catalog description | NGC 1533 is a barred lenticular galaxy with faint spiral structure in the constellation Dorado. The seventh-brightest member of the Dorado Group and 1° off the group's center, it is surrounded by a vast arc or ring of H I which is connected to IC 2038 and IC 2039. The ring orbits around 32 kpc from the center.[b] As is typical of lenticular galaxies, star formation is weak in NGC 1533. Using both the surface brightness fluctuation (SBF) and globular cluster luminosity function (GCLF) methods, its distance was estimated in 2007 to be 19.4 ± 1.1 Mpc and 18.6 ± 2.0 Mpc respectively. Averaging these together gives a distance of around 19 million parsecs or 62 million light-years from earth.[a] In 1970, a supernova was detected in NGC 1533. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2039 has the different designation NGC 1533 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.531499%20-56.281986&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026aicx](https://www.wis-tns.org/object/2026aicx) near IC 21

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 21 as this object's host. The 1.65570° (99.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:38Z · 3 days · 20.09 L |
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
| Subject | **IC 21** · `IC 21` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.49′ × 0.45′ |
| Distance | — |
| Separation | 1.65570° · 99.34′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 21 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=8.80088%200.521113&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026aiin](https://www.wis-tns.org/object/2026aiin) near NGC1084

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1084 as this object's host. The 1.58124° (94.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:02:50Z · 3 days · 20.59 g |
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
| Subject | **NGC1084** · `NGC1084` |
| Catalog display name | NGC1084 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.6 · 3.4′ × 2.25′ |
| Distance | — |
| Separation | 1.58124° · 94.87′ |
| Catalog description | NGC 1084 is an unbarred spiral galaxy in the constellation Eridanus. It is located at a distance of about 63 million light-years away from the Milky Way. The galaxy was discovered by William Herschel on 10 January 1785. It has multiple spiral arms, which are not well defined. It belongs in the same galaxy group with NGC 988, NGC 991, NGC 1022, NGC 1035, NGC 1042, NGC 1047, NGC 1052 and NGC 1110. This group is in turn associated with the Messier 77 group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiin) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=42.8451324%20-7.5704687&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026aiiw](https://www.wis-tns.org/object/2026aiiw) near IC5325

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5325 as this object's host. The 1.36152° (81.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:09:22Z · 5 days · 19.98 L |
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
| Subject | **IC5325** · `IC5325` |
| Catalog display name | IC5325 |
| Type / constellation | Galaxy · Phoenix |
| Catalog magnitude / angular size | 11.3 · 2.88′ × 2.62′ |
| Distance | — |
| Separation | 1.36152° · 81.69′ |
| Catalog description | IC 5325 is a spiral galaxy in the constellation Phoenix. The galaxy lies about 70 million light years away from Earth, which means, given its apparent dimensions, that IC 5325 is approximately 75,000 light years across. It was discovered by Lewis Swift in 1897. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiiw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.764581%20-40.490264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 147. [AT2026aijo](https://www.wis-tns.org/object/2026aijo) near NGC1055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1055 as this object's host. The 1.04239° (62.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T12:08:33Z · 1 days · 20.25 L |
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
| Subject | **NGC1055** · `NGC1055` |
| Catalog display name | NGC1055 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 10.6 · 6.92′ × 3.53′ |
| Distance | — |
| Separation | 1.04239° · 62.54′ |
| Catalog description | NGC 1055 is an edge-on spiral galaxy located in the constellation Cetus. The galaxy has a prominent nuclear bulge crossed by a wide, knotty, dark lane of dust and gas. The spiral arm structure appears to be elevated above the galaxy's plane and obscures the upper half of the bulge. It was discovered by German-British astronomer William Herschel on December 18, 1783, from his home in Slough, England. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=39.606568%20-0.186235&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026aijx](https://www.wis-tns.org/object/2026aijx) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.48110° (88.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:31Z · 0 days · 21.8 r |
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
| Subject | **NGC1527** · `NGC1527` |
| Catalog display name | NGC1527 |
| Type / constellation | Galaxy · Horologium |
| Catalog magnitude / angular size | 10.8 · 4.58′ × 1.79′ |
| Distance | 17,500 kpc |
| Separation | 1.48110° · 88.87′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=61.2381112%20-49.2640016&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026aijz](https://www.wis-tns.org/object/2026aijz) near IC522

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC522 as this object's host. The 1.16708° (70.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T11:06:29Z · 4 days · 19.8 g |
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
| Subject | **IC522** · `IC522` |
| Catalog display name | IC522 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 13.9 · 1.24′ × 1.02′ |
| Distance | — |
| Separation | 1.16708° · 70.02′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, brighter middle, or in the middle (2 extremely, excessively faint stars (pl.) inv?) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.5650403%2057.4916495&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 150. [AT2026aika](https://www.wis-tns.org/object/2026aika) near IC 1776

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1776 as this object's host. The 1.83590° (110.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:55:04Z · 3 days · 20.36 r |
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
| Subject | **IC 1776** · `IC 1776` |
| Catalog display name | IC 2574 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.26′ × 1′ |
| Distance | — |
| Separation | 1.83590° · 110.15′ |
| Catalog description | IC 2574, also known as Coddington's Nebula, is a dwarf spiral galaxy discovered by American astronomer Edwin Foster Coddington in 1898. Located in Ursa Major, a constellation in the northern sky, it is an outlying member of the M81 Group. It is believed that 90% of its mass is in the form of dark matter. IC 2574 does not show evidence of interaction with other galaxies. It is currently forming stars; a UV analysis showed clumps of star formation 85 to 500 light-years in size. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1776 has the different designation IC 2574 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aika) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.2256751%207.7038288&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 151. [AT2026aikd](https://www.wis-tns.org/object/2026aikd) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.84563° (110.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:34:20Z · 7 days · 20.95 i |
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
| Subject | **NGC7606** · `NGC7606` |
| Catalog display name | NGC7606 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 11 · 5.26′ × 4.47′ |
| Distance | — |
| Separation | 1.84563° · 110.74′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.3976846%20-9.385282&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 152. [AT2026aikq](https://www.wis-tns.org/object/2026aikq) near NGC 4150

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4150 as this object's host. The 1.54182° (92.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:55:21Z · 3 days · 20.18 r |
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
| Subject | **NGC 4150** · `NGC 4150` |
| Catalog display name | NGC 4150 |
| Type / constellation | Galaxy · Com |
| Catalog magnitude / angular size | 11.69 · 1.99′ × 1.33′ |
| Distance | — |
| Separation | 1.54182° · 92.51′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.7375655%2029.0737624&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026aikv](https://www.wis-tns.org/object/2026aikv) near NGC628

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC628 as this object's host. The 1.77250° (106.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:08:13Z · 3 days · 20.5 r |
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
| Subject | **NGC628** · `NGC628` |
| Catalog display name | NGC628 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 9.3 · 9.89′ × 9.33′ |
| Distance | 10.731 kpc |
| Separation | 1.77250° · 106.35′ |
| Catalog description | Messier 74 is a large spiral galaxy in the equatorial constellation Pisces. It is about 32 million light-years away from Earth. The galaxy contains two clearly defined spiral arms and is therefore used as an archetypal example of a grand design spiral galaxy. The galaxy's low surface brightness makes it the most difficult Messier object for amateur astronomers to observe. Its relatively large angular size and the galaxy's face-on orientation make it an ideal object for professional astronomers who want to study spiral arm structure and spiral density waves. It is estimated that M74 hosts about 100 billion stars. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=22.4484902%2016.4188975&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 154. [AT2026aikw](https://www.wis-tns.org/object/2026aikw) near IC 186 A

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 186 A as this object's host. The 1.01615° (60.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:59:53Z · 3 days · 20.06 r |
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
| Subject | **IC 186 A** · `IC 186 A` |
| Catalog display name | NGC 5746 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 1.21′ × 0.76′ |
| Distance | 99 ly |
| Separation | 1.01615° · 60.97′ |
| Catalog description | NGC 5746 is a barred spiral galaxy located in the eastern part of the constellation of Virgo. It was discovered on 24 February 1786 by German-British astronomer William Herschel. It is the lead member of the NGC 5746 Group of galaxies, itself one of the Virgo III Groups strung out to the east of the Virgo Supercluster of galaxies. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 186 A has the different designation NGC 5746 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.1141987%20-1.8010337&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 155. [AT2026aikx](https://www.wis-tns.org/object/2026aikx) near IC 1730

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1730 as this object's host. The 1.43755° (86.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T08:41:41Z · 1 days · 20.65 g |
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
| Subject | **IC 1730** · `IC 1730` |
| Catalog display name | NGC 680 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.75′ × 0.48′ |
| Distance | 123 ly |
| Separation | 1.43755° · 86.25′ |
| Catalog description | NGC 680 is an elliptical galaxy located in the constellation Aries. It is located at a distance of circa 120 million light years from Earth, which, given its apparent dimensions, means that NGC 680 is about 100,000 light years across. It was discovered by William Herschel on September 15, 1784. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1730 has the different designation NGC 680 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.7607552%2023.4280316&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 156. [AT2026aikz](https://www.wis-tns.org/object/2026aikz) near Arp 147

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Arp 147 as this object's host. The 1.07092° (64.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:35:00Z · 2 days · 19.88 L |
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
| Subject | **Arp 147** · `IC 5319` |
| Catalog display name | Arp 147 |
| Type / constellation | Galaxy · Peg |
| Catalog magnitude / angular size | — · 0.73′ × 0.64′ |
| Distance | 430 ly |
| Separation | 1.07092° · 64.26′ |
| Catalog description | Arp 147 is an interacting pair of ring galaxies. It lies 430 million to 440 million light years away in the constellation Cetus and does not appear to be part of any significant galaxy group. The system was originally discovered in 1893 by Stephane Javelle and is listed in the Atlas of Peculiar Galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.991108%2015.047429&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 157. [AT2026ahph](https://www.wis-tns.org/object/2026ahph) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.96485° (57.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T12:51:50Z · 20 days · 22.33 r |
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
| Subject | **IC 1481** · `IC 1481` |
| Catalog display name | IC 1481 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.73′ × 0.65′ |
| Distance | 289 ly |
| Separation | 0.96485° · 57.89′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahph) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.824625%205.898225&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 158. [AT2026ahpp](https://www.wis-tns.org/object/2026ahpp) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.84219° (50.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T17:52:48Z · 8 days · 21.96 g |
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
| Subject | **NGC 2207 / IC 2163** · `IC 214` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.58′ × 0.45′ |
| Distance | 81 ly |
| Separation | 0.84219° · 50.53′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.750792%204.362147&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 159. [AT2026ahse](https://www.wis-tns.org/object/2026ahse) near IC1895

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1895 as this object's host. The 0.30451° (18.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:07:33Z · 9 days · 19.72 L |
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
| Subject | **IC1895** · `IC1895` |
| Catalog display name | IC1895 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 13.3 · 1.4′ × 1.05′ |
| Distance | — |
| Separation | 0.30451° · 18.27′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, 2 stars (pl.) close preceding (westward) / pretty (adv., before F. B. L, S) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahse) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.661585%20-25.0621062&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 160. [AT2026ahsm](https://www.wis-tns.org/object/2026ahsm) near IC1796

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1796 as this object's host. The 0.47424° (28.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T12:27:19Z · 9 days · 19.9 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1796** · `IC1796` |
| Catalog display name | IC1796 |
| Type / constellation | Galaxy · Phoenix |
| Catalog magnitude / angular size | 13.7 · 1.07′ × 0.7′ |
| Distance | 73,600 kpc |
| Separation | 0.47424° · 28.45′ |
| Catalog description | very faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.230035%20-41.0515263&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 161. [AT2026ahuh](https://www.wis-tns.org/object/2026ahuh) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.95820° (57.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T17:28:19Z · 8 days · 21.93 g |
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
| Subject | **NGC488** · `NGC488` |
| Catalog display name | NGC488 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 10.3 · 5.05′ × 3.66′ |
| Distance | 28,100 kpc |
| Separation | 0.95820° · 57.49′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.803417%204.539956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 162. [AT2026ahui](https://www.wis-tns.org/object/2026ahui) near Caldwell 51 (C51)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 51 (C51) as this object's host. The 0.83601° (50.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T17:15:21Z · 10 days · 20.95 r |
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
| Subject | **Caldwell 51 (C51)** · `C51` |
| Catalog display name | Caldwell 51 (C51) |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 9 · 12′ × 11′ |
| Distance | — |
| Separation | 0.83601° · 50.16′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahui) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.131333%202.951297&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 163. [AT2026ahwa](https://www.wis-tns.org/object/2026ahwa) near Caldwell 51 (C51)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 51 (C51) as this object's host. The 0.49323° (29.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T15:34:33Z · 28 days · 22.58 r |
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
| Subject | **Caldwell 51 (C51)** · `C51` |
| Catalog display name | Caldwell 51 (C51) |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 9 · 12′ × 11′ |
| Distance | — |
| Separation | 0.49323° · 29.59′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.289292%201.633472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 164. [AT2026ahwd](https://www.wis-tns.org/object/2026ahwd) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 0.87137° (52.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T16:53:45Z · 25 days · 22.89 g |
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
| Subject | **IC 1757** · `IC 1757` |
| Catalog display name | IC 5152 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.4′ × 0.24′ |
| Distance | 5.87 ly |
| Separation | 0.87137° · 52.28′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.880042%200.173897&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 165. [AT2026ahwk](https://www.wis-tns.org/object/2026ahwk) near IC 74

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 74 as this object's host. The 0.68493° (41.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T16:45:07Z · 9 days · 21.37 r |
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
| Subject | **IC 74** · `IC 74` |
| Catalog display name | IC 10 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.57′ × 0.46′ |
| Distance | 2.5 ly |
| Separation | 0.68493° · 41.10′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 74 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.088625%203.529731&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 166. [AT2026aibf](https://www.wis-tns.org/object/2026aibf) near IC1784

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1784 as this object's host. The 0.51346° (30.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T19:14:52Z · 20 days · 21.48 r |
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
| Subject | **IC1784** · `IC1784` |
| Catalog display name | IC1784 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 13.1 · 1.4′ × 0.74′ |
| Distance | 86,550 kpc |
| Separation | 0.51346° · 30.81′ |
| Catalog description | faint, large, extended preceding-following, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.184208%2032.148697&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 167. [AT2026ahog](https://www.wis-tns.org/object/2026ahog) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.76220° (45.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:23:47Z · 6 days · 21.93 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.76220° · 45.73′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahog) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.1200412%20-4.7976467&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 168. [AT2026ahoh](https://www.wis-tns.org/object/2026ahoh) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.47015° (28.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 22.97 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.47015° · 28.21′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.788329%20-5.7656064&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 169. [AT2026ahoi](https://www.wis-tns.org/object/2026ahoi) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 0.73212° (43.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:30:43Z · 6 days · 23.04 z |
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
| Subject | **IC2055** · `IC2055` |
| Catalog display name | IC2055 |
| Type / constellation | Nebula · Dorado |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.73212° · 43.93′ |
| Catalog description | faint, small in angular size, considerably extended north-south, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.938228%20-48.2749101&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 170. [AT2026ahok](https://www.wis-tns.org/object/2026ahok) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.85717° (51.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 21.69 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.85717° · 51.43′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahok) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.1306276%20-5.9508091&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026ahol](https://www.wis-tns.org/object/2026ahol) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.78403° (47.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 23.1 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.78403° · 47.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahol) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.7767915%20-6.0005592&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 172. [AT2026ahov](https://www.wis-tns.org/object/2026ahov) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.71377° (42.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:23:47Z · 6 days · 22.83 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.71377° · 42.83′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahov) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.1132665%20-4.8525046&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 173. [AT2026ahoy](https://www.wis-tns.org/object/2026ahoy) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.87851° (52.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 23.46 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.87851° · 52.71′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.0006547%20-4.8746442&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 174. [AT2026ahoz](https://www.wis-tns.org/object/2026ahoz) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.47970° (28.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 22.52 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.47970° · 28.78′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.9296557%20-5.6468867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 175. [AT2026ahru](https://www.wis-tns.org/object/2026ahru) near IC1376

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1376 as this object's host. The 0.31912° (19.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:13:56Z · 6 days · 20.33 w |
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
| Subject | **IC1376** · `IC1376` |
| Catalog display name | IC1376 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.31912° · 19.15′ |
| Catalog description | no descr |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=320.9078844%20-5.9252208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 176. [AT2026ahvt](https://www.wis-tns.org/object/2026ahvt) near Blue Flash

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Blue Flash as this object's host. The 0.96606° (57.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:18:49Z · 3 days · 19.79 r |
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
| Subject | **Blue Flash** · `NGC 6905` |
| Catalog display name | Blue Flash |
| Type / constellation | Planetary nebula · Del |
| Catalog magnitude / angular size | — · 0.73′ × 0.63′ |
| Distance | 7,500 ly |
| Separation | 0.96606° · 57.96′ |
| Catalog description | NGC 6905, also known as the Blue Flash Nebula, is a planetary nebula in the constellation Delphinus. It was discovered by William Herschel in 1784. The central star is 14.0 mag. The distance of the nebula, as with most planetary nebulae, is not well determined and estimates range between 1.7 and 2.6 kpc. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=304.9634898%2019.3385092&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 177. [AT2026ahwv](https://www.wis-tns.org/object/2026ahwv) near IC5385

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5385 as this object's host. The 0.77310° (46.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:29:16Z · 7 days · 22.18 r |
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
| Subject | **IC5385** · `IC5385` |
| Catalog display name | IC5385 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.77310° · 46.39′ |
| Catalog description | extremely, excessively faint (not verified) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.577833%200.696219&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 178. [AT2026aias](https://www.wis-tns.org/object/2026aias) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 0.69484° (41.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:13:26Z · 7 days · 20.04 L |
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
| Subject | **IC333** · `IC333` |
| Catalog display name | IC333 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.69484° · 41.69′ |
| Catalog description | extremely, excessively faint, a single star 8.8 north following 4' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aias) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.972708%20-4.063139&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 179. [AT2026aiat](https://www.wis-tns.org/object/2026aiat) near Collinder 163 (CR163)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 163 (CR163) as this object's host. The 0.39314° (23.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:14Z · 5 days · 19.61 L |
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
| Subject | **Collinder 163 (CR163)** · `CR163` |
| Catalog display name | Collinder 163 (CR163) |
| Type / constellation | Open cluster · Puppis |
| Catalog magnitude / angular size | 10.2 · 4.5′ × 4.5′ |
| Distance | — |
| Separation | 0.39314° · 23.59′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiat) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=116.824398%20-21.640891&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 180. [AT2026aiko](https://www.wis-tns.org/object/2026aiko) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38099° (22.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:02:26Z · 0 days · 19.85 r |
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
| Subject | **NGC7158** · `NGC7158` |
| Catalog display name | NGC7158 |
| Type / constellation | Nebula · Capricornus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.38099° · 22.86′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiko) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.4036743%20-11.2132738&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 181. [AT2026agua](https://www.wis-tns.org/object/2026agua) near Lynds Dark Nebula 1571 (LDN1571)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1571 (LDN1571) as this object's host. The 1.07129° (64.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T11:03:46Z · 13 days · 19.33 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4280....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4280....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 1571 (LDN1571)** · `LDN1571` |
| Catalog display name | Lynds Dark Nebula 1571 (LDN1571) |
| Type / constellation | Dark nebula · Orion |
| Catalog magnitude / angular size | — · 31.25′ × 31.25′ |
| Distance | — |
| Separation | 1.07129° · 64.28′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026agua) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.4774615%2010.1813155&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 182. [AT2026ahtk](https://www.wis-tns.org/object/2026ahtk) near Sharpless 304 (SH2-304)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 304 (SH2-304) as this object's host. The 1.80080° (108.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T16:31:09Z · 8 days · 19.35 L |
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
| Subject | **Sharpless 304 (SH2-304)** · `SH2-304` |
| Catalog display name | Sharpless 304 (SH2-304) |
| Type / constellation | HII · Canis Major |
| Catalog magnitude / angular size | — · 200′ × 200′ |
| Distance | — |
| Separation | 1.80080° · 108.05′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahtk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.016047%20-23.267067&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 183. [AT2026afiy](https://www.wis-tns.org/object/2026afiy) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.75779° (105.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-08T17:22:33Z · 29 days · 22.59 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4129....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4129....1X/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 197** · `IC 197` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.01′ × 0.53′ |
| Distance | — |
| Separation | 1.75779° · 105.47′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afiy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.6559828%201.1477685&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 184. [AT2026afvg](https://www.wis-tns.org/object/2026afvg) near IC 1931

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1931 as this object's host. The 1.30858° (78.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T08:10:04Z · 19 days · 20.34 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4204....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4204....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1931** · `IC 1931` |
| Catalog display name | NGC5162 |
| Type / constellation | Galaxy · Tau |
| Catalog magnitude / angular size | — · 0.8′ × 0.76′ |
| Distance | — |
| Separation | 1.30858° · 78.51′ |
| Catalog description | NGC 5162 is a very large spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 7125 ± 20 km/s, which corresponds to a Hubble distance of 342.8 ± 24.0 Mly (105.09 ± 7.36 Mpc). In addition, 11 non redshift measurements give a distance of 303.71 ± 12.41 Mly (93.118 ± 3.806 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 15 March 1784. It was also observed by Lewis Swift on 19 April 1887, resulting in the galaxy being included twice in the New General Catalogue, as both NGC 5162 and NGC 5174. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1931 has the different designation NGC5162 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afvg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.4652846%202.2134044&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 185. [AT2026agyb](https://www.wis-tns.org/object/2026agyb) near IC5201

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5201 as this object's host. The 1.07201° (64.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T10:28:36Z · 10 days · 19.63 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4298....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4298....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5201** · `IC5201` |
| Catalog display name | IC5201 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 11.4 · 6.7′ × 2.86′ |
| Distance | — |
| Separation | 1.07201° · 64.32′ |
| Catalog description | IC 5201 is a barred spiral galaxy located in the constellation Grus. It is located at a distance of about 35 million light years from Earth, which, given its apparent dimensions, means that IC 5201 is about 90,000 light years across. It was discovered by Joseph Lunt in 1900. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=336.0659457%20-46.9435557&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 186. [AT2026ahbv](https://www.wis-tns.org/object/2026ahbv) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.53637° (92.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T10:02:19Z · 9 days · 19.86 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4344....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4344....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1495** · `IC1495` |
| Catalog display name | IC1495 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13 · 1.33′ × 0.83′ |
| Distance | 80,650 kpc |
| Separation | 1.53637° · 92.18′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahbv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=353.5659575%20-14.7693613&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 187. [AT2026ahby](https://www.wis-tns.org/object/2026ahby) near IC1438

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1438 as this object's host. The 1.07179° (64.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T09:45:39Z · 9 days · 19.7 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4342....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4342....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1438** · `IC1438` |
| Catalog display name | IC1438 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 12.8 · 2.33′ × 2.16′ |
| Distance | 34,250 kpc |
| Separation | 1.07179° · 64.31′ |
| Catalog description | faint, binuclear |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahby) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=335.075825%20-22.032155&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 188. [AT2026ahpj](https://www.wis-tns.org/object/2026ahpj) near IC 5241

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5241 as this object's host. The 1.94319° (116.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:41:45Z · 8 days · 22.85 g |
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
| Subject | **IC 5241** · `IC 5241` |
| Catalog display name | NGC 804 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.91′ × 0.74′ |
| Distance | — |
| Separation | 1.94319° · 116.59′ |
| Catalog description | NGC 804 is a lenticular galaxy located in the Triangulum constellation about 231 million light-years from the Milky Way. It was discovered by the American astronomer Lewis Swift in 1885. This galaxy was also observed by the French astronomer Guillaume Bigourdan on December 24, 1897, and it has been added to the Index Catalogue under the symbol IC 1773. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5241 has the different designation NGC 804 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.353375%202.738317&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 189. [AT2026ahpm](https://www.wis-tns.org/object/2026ahpm) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.81899° (109.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:09:07Z · 8 days · 22.13 g |
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
| Subject | **IC 1507** · `IC 1507` |
| Catalog display name | IC 1613 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.29′ × 0.47′ |
| Distance | — |
| Separation | 1.81899° · 109.14′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.882833%200.667186&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 190. [AT2026ahpo](https://www.wis-tns.org/object/2026ahpo) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.37026° (82.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T17:19:40Z · 8 days · 22.21 g |
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
| Subject | **NGC488** · `NGC488` |
| Catalog display name | NGC488 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 10.3 · 5.05′ × 3.66′ |
| Distance | 28,100 kpc |
| Separation | 1.37026° · 82.22′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.085%205.487356&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 191. [AT2026ahrl](https://www.wis-tns.org/object/2026ahrl) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.54257° (92.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:19:12Z · 8 days · 21.11 r |
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
| Subject | **Silver Sliver Galaxy** · `C23` |
| Catalog display name | Silver Sliver Galaxy |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 9.9 · 14′ × 2′ |
| Distance | — |
| Separation | 1.54257° · 92.55′ |
| Catalog description | NGC 891 is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda. It was discovered by William Herschel on October 6, 1784. The galaxy is a member of the NGC 1023 group of galaxies in the Local Supercluster. It has an H II nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.121292%2041.298872&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 192. [AT2026ahrm](https://www.wis-tns.org/object/2026ahrm) near IC239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC239 as this object's host. The 1.51986° (91.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:22:04Z · 8 days · 21.2 r |
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
| Subject | **IC239** · `IC239` |
| Catalog display name | IC239 |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 11.2 · 4.25′ × 4.01′ |
| Distance | 11,400 kpc |
| Separation | 1.51986° · 91.19′ |
| Catalog description | IC 239 is a spiral galaxy in the constellation Andromeda. The galaxy lies about 35 million light years away from Earth, which means, given its apparent dimensions, that IC 239 is approximately 50,000 light years across. It was discovered by Isaac Roberts in 1893. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.398125%2039.712997&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 193. [AT2026ahsu](https://www.wis-tns.org/object/2026ahsu) near NGC1574

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1574 as this object's host. The 1.88880° (113.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-13T16:17:12Z · 24 days · 20.05 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1574** · `NGC1574` |
| Catalog display name | NGC1574 |
| Type / constellation | Galaxy · Reticulum |
| Catalog magnitude / angular size | 10.2 · 4.13′ × 2.32′ |
| Distance | 19,300 kpc |
| Separation | 1.88880° · 113.33′ |
| Catalog description | NGC 1574 is a lenticular galaxy in the constellation Reticulum. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 1574 is approximately 75,000 light years across. It was discovered by John Herschel on December 4, 1834. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.11196%20-58.2388475&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 194. [AT2026ahsz](https://www.wis-tns.org/object/2026ahsz) near IC1783

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1783 as this object's host. The 1.16689° (70.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:07:30Z · 8 days · 19.73 L |
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
| Subject | **IC1783** · `IC1783` |
| Catalog display name | IC1783 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 12.5 · 1.98′ × 0.8′ |
| Distance | 46,000 kpc |
| Separation | 1.16689° · 70.01′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, very small in angular size, much / magnitude extended north-south, faint a single star preceding (westward) / pretty (adv., before F. B. L, S) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.553673%20-34.10651&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 195. [AT2026ahta](https://www.wis-tns.org/object/2026ahta) near IC1616

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1616 as this object's host. The 1.32685° (79.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:33:11Z · 8 days · 20.35 L |
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
| Subject | **IC1616** · `IC1616` |
| Catalog display name | IC1616 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 12.9 · 1.63′ × 1.5′ |
| Distance | — |
| Separation | 1.32685° · 79.61′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, 3 stars (pl.) irregular north little (adv.); long (adj.) irregular north extremely, excessively near |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahta) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.045177%20-28.440811&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026ahub](https://www.wis-tns.org/object/2026ahub) near IC1528

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1528 as this object's host. The 1.92115° (115.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T04:43:52Z · 10 days · 19.85 r |
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
| Subject | **IC1528** · `IC1528` |
| Catalog display name | IC1528 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.6 · 2.15′ × 0.85′ |
| Distance | 48,500 kpc |
| Separation | 1.92115° · 115.27′ |
| Catalog description | no description |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahub) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.2109433%20-5.4868622&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 197. [AT2026ahum](https://www.wis-tns.org/object/2026ahum) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.36722° (82.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:21:07Z · 9 days · 21.42 r |
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
| Subject | **NGC 2207 / IC 2163** · `IC 214` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.58′ × 0.45′ |
| Distance | 81 ly |
| Separation | 1.36722° · 82.03′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahum) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.967542%203.879736&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 198. [AT2026ahur](https://www.wis-tns.org/object/2026ahur) near Mirach's Ghost

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Mirach's Ghost as this object's host. The 1.36361° (81.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-11T20:29:45Z · 26 days · 21.19 g |
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
| Subject | **Mirach's Ghost** · `NGC404` |
| Catalog display name | Mirach's Ghost |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 10.6 · 3.4′ × 3.37′ |
| Distance | — |
| Separation | 1.36361° · 81.82′ |
| Catalog description | NGC 404 is a field galaxy located about 10 million light years away in the constellation Andromeda. It was discovered by William Herschel in 1784, and is visible through small telescopes. NGC 404 lies just beyond the Local Group and does not appear gravitationally bound to it. It is located within 7 arc-minutes of second magnitude star Mirach, making it a difficult target to observe or photograph and granting it the nickname "Mirach's Ghost". |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahur) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.8725%2036.324733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 199. [AT2026ahuw](https://www.wis-tns.org/object/2026ahuw) near Collinder 205 (CR205)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 205 (CR205) as this object's host. The 1.48052° (88.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T10:20:11Z · 12 days · 19.83 r |
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
| Subject | **Collinder 205 (CR205)** · `CR205` |
| Catalog display name | Collinder 205 (CR205) |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 7.8 · 1.53′ × 0.46′ |
| Distance | 55,700 kpc |
| Separation | 1.48052° · 88.83′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=133.7543221%2060.7624997&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 200. [AT2026ahvy](https://www.wis-tns.org/object/2026ahvy) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.74336° (104.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-13T15:37:26Z · 24 days · 22.73 r |
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
| Subject | **IC 197** · `IC 197` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.01′ × 0.53′ |
| Distance | — |
| Separation | 1.74336° · 104.60′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.637125%202.130481&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 201. [AT2026ahwb](https://www.wis-tns.org/object/2026ahwb) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 1.50173° (90.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T16:22:04Z · 25 days · 22.35 r |
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
| Subject | **IC 173** · `IC 173` |
| Catalog display name | IC 3418 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.92′ × 0.72′ |
| Distance | — |
| Separation | 1.50173° · 90.10′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.44925%202.714442&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026ahxh](https://www.wis-tns.org/object/2026ahxh) near IC1733

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1733 as this object's host. The 1.07502° (64.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T20:57:07Z · 28 days · 21.42 r |
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
| Subject | **IC1733** · `IC1733` |
| Catalog display name | IC1733 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 13 · 1.54′ × 1.43′ |
| Distance | 139,000 kpc |
| Separation | 1.07502° · 64.50′ |
| Catalog description | faint, very small in angular size, preceding (westward) / pretty (adv., before F. B. L, S) round, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.899417%2033.940811&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 203. [AT2026ahxj](https://www.wis-tns.org/object/2026ahxj) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.84591° (110.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T21:36:00Z · 18 days · 21.1 g |
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
| Subject | **Silver Sliver Galaxy** · `C23` |
| Catalog display name | Silver Sliver Galaxy |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 9.9 · 14′ × 2′ |
| Distance | — |
| Separation | 1.84591° · 110.75′ |
| Catalog description | NGC 891 is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda. It was discovered by William Herschel on October 6, 1784. The galaxy is a member of the NGC 1023 group of galaxies in the Local Supercluster. It has an H II nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.247625%2043.891353&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 204. [AT2026ahyo](https://www.wis-tns.org/object/2026ahyo) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.39543° (83.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:02:34Z · 8 days · 19.76 r |
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
| Subject | **NGC 2207 / IC 2163** · `IC 2992` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | — · 0.63′ × 0.52′ |
| Distance | 81 ly |
| Separation | 1.39543° · 83.73′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=179.7051072%2031.0528992&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 205. [AT2026ahzu](https://www.wis-tns.org/object/2026ahzu) near IC 1600

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1600 as this object's host. The 1.85166° (111.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:45:16Z · 8 days · 20.04 L |
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
| Subject | **IC 1600** · `IC 1600` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.8′ × 0.47′ |
| Distance | — |
| Separation | 1.85166° · 111.10′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1600 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=14.831495%20-21.954499&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 206. [AT2026aibd](https://www.wis-tns.org/object/2026aibd) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 1.35024° (81.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:19:40Z · 9 days · 21.48 r |
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
| Subject | **NGC741** · `NGC741` |
| Catalog display name | NGC741 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 11.3 · 2.83′ × 2.33′ |
| Distance | — |
| Separation | 1.35024° · 81.01′ |
| Catalog description | NGC 741, also known as PGC 7252, is a formerly active radio galaxy in the constellation of Pisces. Located 74.13 Mpc away, NGC 741 is part of a group of galaxies including NGC 742 and PGC 7250. NGC 741 and NGC 742 recently collided, although the disruption was minor. Radio filaments have been found connecting NGC 741 to NGC 742, and due to the bent structure of the radio filaments, NGC 741 is estimated to be moving at 1400 km/s with respect to its local group, suggesting that ram-pressure stripping was created as a product of the former merger. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.34275%205.117756&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 207. [AT2026aibz](https://www.wis-tns.org/object/2026aibz) near IC334

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC334 as this object's host. The 1.51904° (91.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T09:21:30Z · 11 days · 19.66 r |
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
| Subject | **IC334** · `IC334` |
| Catalog display name | IC334 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 11.5 · 2.34′ × 1.85′ |
| Distance | — |
| Separation | 1.51904° · 91.14′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, small in angular size, a star of 13th magnitude involved, involving south following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.7529198%2078.0612284&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 208. [AT2026aico](https://www.wis-tns.org/object/2026aico) near IC 33

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 33 as this object's host. The 1.03221° (61.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T11:14:08Z · 9 days · 19.65 L |
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
| Subject | **IC 33** · `IC 33` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.78′ × 0.58′ |
| Distance | — |
| Separation | 1.03221° · 61.93′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 33 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aico) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.249415%20-1.222683&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 209. [AT2026aicp](https://www.wis-tns.org/object/2026aicp) near IC5270

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5270 as this object's host. The 1.45156° (87.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T09:54:42Z · 9 days · 20.02 L |
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
| Subject | **IC5270** · `IC5270` |
| Catalog display name | IC5270 |
| Type / constellation | Galaxy · Piscis Austrinus |
| Catalog magnitude / angular size | 12.9 · 3.29′ × 1.81′ |
| Distance | 24,300 kpc |
| Separation | 1.45156° · 87.09′ |
| Catalog description | The Telescopium−Grus Cloud is a galaxy filament in the constellations of Pavo, Indus, and Telescopium. It was first defined by astronomer Brent Tully in his book The Nearby Galaxies Atlas and its companion book The Nearby Galaxies Catalog. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.252848%20-35.694828&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 210. [AT2026aicw](https://www.wis-tns.org/object/2026aicw) near IC1574

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1574 as this object's host. The 1.16074° (69.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:16:36Z · 8 days · 19.96 L |
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
| Subject | **IC1574** · `IC1574` |
| Catalog display name | IC1574 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.9 · 1.83′ × 0.7′ |
| Distance | 4,910 kpc |
| Separation | 1.16074° · 69.64′ |
| Catalog description | IC 1574 is an irregular galaxy 17 million light-years from Earth. It is a member of the Sculptor Group, a group of galaxies near the Local Group. It was discovered by DeLisle Stewart on 3 November 1898. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.521497%20-22.084216&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 211. [AT2026aiit](https://www.wis-tns.org/object/2026aiit) near IC 536

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 536 as this object's host. The 1.35010° (81.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T12:16:17Z · 11 days · 20.1 g |
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
| Subject | **IC 536** · `IC 536` |
| Catalog display name | IC 10 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 1.09′ × 0.22′ |
| Distance | 2.5 ly |
| Separation | 1.35010° · 81.01′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 536 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiit) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.6407975%2026.3743345&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 212. [AT2026aiiu](https://www.wis-tns.org/object/2026aiiu) near IC1729

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1729 as this object's host. The 1.95901° (117.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:03:28Z · 8 days · 20.2 L |
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
| Subject | **IC1729** · `IC1729` |
| Catalog display name | IC1729 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 12.5 · 2.22′ × 1.25′ |
| Distance | — |
| Separation | 1.95901° · 117.54′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, extremely, excessively small in angular size, almost stellar, pointlike, rr? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiiu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.940411%20-26.754605&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 213. [AT2026ahnn](https://www.wis-tns.org/object/2026ahnn) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 1.07697° (64.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:01:28Z · 7 days · 19.59 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4363....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4363....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC333** · `IC333` |
| Catalog display name | IC333 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.07697° · 64.62′ |
| Catalog description | extremely, excessively faint, a single star 8.8 north following 4' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahnn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.76688%20-5.6316323&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 214. [AT2026ahoj](https://www.wis-tns.org/object/2026ahoj) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.83043° (109.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:43:55Z · 6 days · 22.52 z |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.83043° · 109.83′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.9653809%20-3.7714011&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 215. [AT2026ahon](https://www.wis-tns.org/object/2026ahon) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 1.64509° (98.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T04:26:35Z · 6 days · 22.75 r |
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
| Subject | **IC2055** · `IC2055` |
| Catalog display name | IC2055 |
| Type / constellation | Nebula · Dorado |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.64509° · 98.71′ |
| Catalog description | faint, small in angular size, considerably extended north-south, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahon) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.1761355%20-49.6355733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 216. [AT2026ahoq](https://www.wis-tns.org/object/2026ahoq) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.10782° (66.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:23:47Z · 6 days · 22.44 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.10782° · 66.47′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahoq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.0088869%20-4.4700934&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 217. [AT2026ahot](https://www.wis-tns.org/object/2026ahot) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.19701° (71.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 6 days · 22.67 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.19701° · 71.82′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahot) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.1407197%20-6.447163&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 218. [AT2026ahou](https://www.wis-tns.org/object/2026ahou) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.52046° (91.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:23:47Z · 6 days · 21.91 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.52046° · 91.23′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahou) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.0324518%20-4.1303287&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 219. [AT2026ahpc](https://www.wis-tns.org/object/2026ahpc) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.17408° (70.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:23:47Z · 6 days · 22.38 i |
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
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.17408° · 70.44′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.2186939%20-5.3877425&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 220. [AT2026ahqf](https://www.wis-tns.org/object/2026ahqf) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.37958° (82.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:22:28Z · 7 days · 21.92 r |
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
| Subject | **IC1457** · `IC1457` |
| Catalog display name | IC1457 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.37958° · 82.77′ |
| Catalog description | extremely, excessively faint, a star of 10th magnitude south following 1' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.632912%20-4.427647&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 221. [AT2026ahtl](https://www.wis-tns.org/object/2026ahtl) near IC1497

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1497 as this object's host. The 1.19170° (71.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T08:29:13Z · 5 days · 20.91 w |
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
| Subject | **IC1497** · `IC1497` |
| Catalog display name | IC1497 |
| Type / constellation | Nebula · Pegasus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.19170° · 71.50′ |
| Catalog description | extremely, excessively faint, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.325964%2010.9914387&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 222. [AT2026ahuc](https://www.wis-tns.org/object/2026ahuc) near NGC1479

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1479 as this object's host. The 1.96261° (117.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:53:40Z · 5 days · 19.59 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4392....1C](https://ui.adsabs.harvard.edu/abs/2026TNSTR4392....1C/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1479** · `NGC1479` |
| Catalog display name | NGC1479 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.96261° · 117.76′ |
| Catalog description | A galaxy is a system of stars, stellar remnants, interstellar gas, dust, and dark matter bound together by gravity. The word is derived from the Greek galaxias (γαλαξίας), literally'milky', a reference to the Milky Way galaxy that contains the Solar System. Galaxies, averaging an estimated 100 million stars, range in size from dwarfs with less than a thousand stars, to the largest galaxies known – supergiants with one hundred trillion stars, each orbiting its galaxy's centre of mass. Most of the mass in a typical galaxy is in the form of dark matter, with only a few percent of that mass visible in the form of stars and nebulae. Supermassive black holes are a common feature at the centres of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.7144283%20-9.5291483&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 223. [AT2026ahva](https://www.wis-tns.org/object/2026ahva) near Spirograph Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Spirograph Nebula as this object's host. The 1.39512° (83.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:01:55Z · 5 days · 19.64 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4399....1L](https://ui.adsabs.harvard.edu/abs/2026TNSTR4399....1L/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Spirograph Nebula** · `IC 418` |
| Catalog display name | Spirograph Nebula |
| Type / constellation | Planetary nebula · Lep |
| Catalog magnitude / angular size | — · 0.23′ × 0.18′ |
| Distance | 3.6 ly |
| Separation | 1.39512° · 83.71′ |
| Catalog description | IC 418, also known as the Spirograph Nebula, is a bright planetary nebula located in the constellation of Lepus about 3,600 ly away from Earth. It spans 0.3 light-years across. The central star of the planetary nebula, HD 35914, is an O-type star with a spectral type of O7fp. The nebula formed a few thousand years ago during the star's last stages of its red giant phase. Material from the star's outer layers was ejected from the star into the surrounding space. The nebula's glow is caused by the central star's ultraviolet radiation interacting with the gas. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahva) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=81.3013116%20-13.9806938&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 224. [AT2026ahws](https://www.wis-tns.org/object/2026ahws) near NGC7565

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7565 as this object's host. The 1.12986° (67.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:59:02Z · 7 days · 22.49 r |
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
| Subject | **NGC7565** · `NGC7565` |
| Catalog display name | NGC7565 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.12986° · 67.79′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahws) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.959667%200.094028&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 225. [AT2026ahxd](https://www.wis-tns.org/object/2026ahxd) near NGC7565

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7565 as this object's host. The 1.79660° (107.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:24:57Z · 5 days · 22.58 r |
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
| Subject | **NGC7565** · `NGC7565` |
| Catalog display name | NGC7565 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.79660° · 107.80′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.308333%20-0.361856&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 226. [AT2026ahyb](https://www.wis-tns.org/object/2026ahyb) near NGC1707

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1707 as this object's host. The 1.35320° (81.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:57:21Z · 3 days · 19.75 r |
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
| Subject | **NGC1707** · `NGC1707` |
| Catalog display name | NGC1707 |
| Type / constellation | Nebula · Orion |
| Catalog magnitude / angular size | — · 1′ × 1′ |
| Distance | — |
| Separation | 1.35320° · 81.19′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.7652928%207.5597387&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 227. [AT2026ahyc](https://www.wis-tns.org/object/2026ahyc) near IC274

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC274 as this object's host. The 1.51881° (91.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T06:46:18Z · 3 days · 20.18 g |
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
| Subject | **IC274** · `IC274` |
| Catalog display name | IC274 |
| Type / constellation | Nebula · Perseus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.51881° · 91.13′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, very difficult |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=42.9034281%2044.1691452&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 228. [AT2026ahyd](https://www.wis-tns.org/object/2026ahyd) near IC5366

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5366 as this object's host. The 1.01813° (61.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:20:44Z · 3 days · 19.53 r |
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
| Subject | **IC5366** · `IC5366` |
| Catalog display name | IC5366 |
| Type / constellation | Nebula · Cassiopeia |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.01813° · 61.09′ |
| Catalog description | extremely, excessively large, much / magnitude extended (30'by 10') |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.7728239%2051.7970796&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 229. [AT2026ahyh](https://www.wis-tns.org/object/2026ahyh) near NGC2399

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2399 as this object's host. The 1.47903° (88.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:06:34Z · 3 days · 19.57 r |
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
| Subject | **NGC2399** · `NGC2399` |
| Catalog display name | NGC2399 |
| Type / constellation | Nebula · Canis Minor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.47903° · 88.74′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=112.455104%201.2647398&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 230. [AT2026ahyu](https://www.wis-tns.org/object/2026ahyu) near NGC1147

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1147 as this object's host. The 1.49197° (89.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:17:59Z · 7 days · 20.24 L |
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
| Subject | **NGC1147** · `NGC1147` |
| Catalog display name | NGC1147 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.49197° · 89.52′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=42.279912%20-9.021378&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 231. [AT2026aiay](https://www.wis-tns.org/object/2026aiay) near Messier 40 (M40)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 40 (M40) as this object's host. The 1.14193° (68.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:47:29Z · 3 days · 20 g |
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
| Subject | **Messier 40 (M40)** · `M40` |
| Catalog display name | Messier 40 (M40) |
| Type / constellation | Double star · Ursa Major |
| Catalog magnitude / angular size | 8.4 · 0.8′ × 0.8′ |
| Distance | 0.156 kpc |
| Separation | 1.14193° · 68.52′ |
| Catalog description | Winnecke 4 is an optical double star consisting of two unrelated stars in a northerly zone of the sky, Ursa Major. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiay) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=184.0197272%2058.8908936&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 232. [AT2026aiid](https://www.wis-tns.org/object/2026aiid) near IC1415

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1415 as this object's host. The 1.79157° (107.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:32:38Z · 3 days · 19.8 r |
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
| Subject | **IC1415** · `IC1415` |
| Catalog display name | IC1415 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.79157° · 107.49′ |
| Catalog description | extremely, excessively faint, a single star 9.5 south following 8' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiid) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.9471744%200.0887744&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 233. [AT2026aiif](https://www.wis-tns.org/object/2026aiif) near IC2013

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2013 as this object's host. The 1.67634° (100.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:10:44Z · 3 days · 20.25 g |
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
| Subject | **IC2013** · `IC2013` |
| Catalog display name | IC2013 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.67634° · 100.58′ |
| Catalog description | considerably bright, considerably large, much / magnitude extended 170deg , considerably brighter middle, or in the middle, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiif) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.0959348%20-15.7970213&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 234. [AT2026aiih](https://www.wis-tns.org/object/2026aiih) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 1.30155° (78.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 0 days · 23.45 r |
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
| Subject | **IC2055** · `IC2055` |
| Catalog display name | IC2055 |
| Type / constellation | Nebula · Dorado |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.30155° · 78.09′ |
| Catalog description | faint, small in angular size, considerably extended north-south, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiih) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.5938607%20-49.3939256&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 235. [AT2026aiik](https://www.wis-tns.org/object/2026aiik) near IC1992

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1992 as this object's host. The 1.50046° (90.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 0 days · 23.13 r |
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
| Subject | **IC1992** · `IC1992` |
| Catalog display name | IC1992 |
| Type / constellation | Nebula · Horologium |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.50046° · 90.03′ |
| Catalog description | stellar, pointlike |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiik) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.4062941%20-50.3402917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 236. [AT2026aijr](https://www.wis-tns.org/object/2026aijr) near NGC7447

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7447 as this object's host. The 1.89148° (113.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:48:34Z · 2 days · 20.08 L |
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
| Subject | **NGC7447** · `NGC7447` |
| Catalog display name | NGC7447 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.89148° · 113.49′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.702783%20-12.327509&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 237. [AT2026aila](https://www.wis-tns.org/object/2026aila) near NGC2586

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2586 as this object's host. The 1.95896° (117.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T17:46:45Z · 1 days · 19.91 L |
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
| Subject | **NGC2586** · `NGC2586` |
| Catalog display name | NGC2586 |
| Type / constellation | Nebula · Hydra |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.95896° · 117.54′ |
| Catalog description | A galaxy is a system of stars, stellar remnants, interstellar gas, dust, and dark matter bound together by gravity. The word is derived from the Greek galaxias (γαλαξίας), literally'milky', a reference to the Milky Way galaxy that contains the Solar System. Galaxies, averaging an estimated 100 million stars, range in size from dwarfs with less than a thousand stars, to the largest galaxies known – supergiants with one hundred trillion stars, each orbiting its galaxy's centre of mass. Most of the mass in a typical galaxy is in the form of dark matter, with only a few percent of that mass visible in the form of stars and nebulae. Supermassive black holes are a common feature at the centres of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aila) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.799932%20-4.535496&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 238. [AT2026ailb](https://www.wis-tns.org/object/2026ailb) near IC518

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC518 as this object's host. The 1.97027° (118.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T17:46:45Z · 1 days · 19.83 L |
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
| Subject | **IC518** · `IC518` |
| Catalog display name | IC518 |
| Type / constellation | Nebula · Hydra |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.97027° · 118.22′ |
| Catalog description | very faint (vS Cl?) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ailb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=130.415062%20-0.70376&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 239. [AT2026ahbr](https://www.wis-tns.org/object/2026ahbr) near IC1533

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1533 as this object's host. The 0.70152° (42.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T10:30:17Z · 9 days · 19.81 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4342....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4342....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1533** · `IC1533` |
| Catalog display name | IC1533 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.70152° · 42.09′ |
| Catalog description | most extremely faint, very small in angular size, round, very difficult; a single star 7.5 north, a star of 9th magnitude suddenly (abruptly) / south |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahbr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=2.7192486%20-6.7169882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 240. [AT2026ahpk](https://www.wis-tns.org/object/2026ahpk) near NGC7565

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7565 as this object's host. The 0.97844° (58.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:50:24Z · 8 days · 22.3 g |
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
| Subject | **NGC7565** · `NGC7565` |
| Catalog display name | NGC7565 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.97844° · 58.71′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.87275%200.897806&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 241. [AT2026ahqn](https://www.wis-tns.org/object/2026ahqn) near IC1475

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1475 as this object's host. The 0.66956° (40.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T10:18:48Z · 9 days · 19.65 L |
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
| Subject | **IC1475** · `IC1475` |
| Catalog display name | IC1475 |
| Type / constellation | Nebula · Sculptor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.66956° · 40.17′ |
| Catalog description | nebula a single star |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahqn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.285313%20-27.78244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 242. [AT2026ahrg](https://www.wis-tns.org/object/2026ahrg) near IC 2275

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2275 as this object's host. The 0.45086° (27.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T22:26:24Z · 20 days · 20.36 r |
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
| Subject | **IC 2275** · `IC 2275` |
| Catalog display name | NGC 1360 |
| Type / constellation | Star · Cnc |
| Catalog magnitude / angular size | — · 11′ × 7.5′ |
| Distance | — |
| Separation | 0.45086° · 27.05′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2275 has the different designation NGC 1360 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=124.282583%2018.043678&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 243. [AT2026ahro](https://www.wis-tns.org/object/2026ahro) near IC1800

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1800 as this object's host. The 0.47926° (28.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:33:36Z · 8 days · 20.12 r |
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
| Subject | **IC1800** · `IC1800` |
| Catalog display name | IC1800 |
| Type / constellation | Nebula · Triangulum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.47926° · 28.76′ |
| Catalog description | extremely, excessively faint, small in angular size; extremely, excessively small in angular size Cl? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahro) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.800875%2031.021253&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 244. [AT2026ahtn](https://www.wis-tns.org/object/2026ahtn) near Lynds Bright Nebula 644 (LBN644)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 644 (LBN644) as this object's host. The 0.61734° (37.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T06:54:50Z · 5 days · 19.87 w |
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
| Subject | **Lynds Bright Nebula 644 (LBN644)** · `LBN644` |
| Catalog display name | Lynds Bright Nebula 644 (LBN644) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 270′ × 20′ |
| Distance | — |
| Separation | 0.61734° · 37.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahtn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.8985869%2017.0245849&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 245. [AT2026ahuo](https://www.wis-tns.org/object/2026ahuo) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 0.95066° (57.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:48:57Z · 7 days · 22.5 r |
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
| Subject | **Lynds Bright Nebula 188 (LBN188)** · `LBN188` |
| Catalog display name | Lynds Bright Nebula 188 (LBN188) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 22′ × 12′ |
| Distance | — |
| Separation | 0.95066° · 57.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahuo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.612667%200.441208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 246. [AT2026ahxt](https://www.wis-tns.org/object/2026ahxt) near NGC1479

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1479 as this object's host. The 0.26734° (16.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-08T11:02:14Z · 29 days · 20.75 r |
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
| Subject | **NGC1479** · `NGC1479` |
| Catalog display name | NGC1479 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.26734° · 16.04′ |
| Catalog description | A galaxy is a system of stars, stellar remnants, interstellar gas, dust, and dark matter bound together by gravity. The word is derived from the Greek galaxias (γαλαξίας), literally'milky', a reference to the Milky Way galaxy that contains the Solar System. Galaxies, averaging an estimated 100 million stars, range in size from dwarfs with less than a thousand stars, to the largest galaxies known – supergiants with one hundred trillion stars, each orbiting its galaxy's centre of mass. Most of the mass in a typical galaxy is in the form of dark matter, with only a few percent of that mass visible in the form of stars and nebulae. Supermassive black holes are a common feature at the centres of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.3130896%20-10.1816499&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 247. [AT2026ahxw](https://www.wis-tns.org/object/2026ahxw) near Collinder 154 (CR154)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 154 (CR154) as this object's host. The 0.75676° (45.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T10:50:01Z · 17 days · 20.84 g |
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
| Subject | **Collinder 154 (CR154)** · `CR154` |
| Catalog display name | Collinder 154 (CR154) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 8.3 · 7.5′ × 7.5′ |
| Distance | 2.48 kpc |
| Separation | 0.75676° · 45.41′ |
| Catalog description | NGC 2420 is an open cluster in the constellation Gemini. It was discovered by German-British astronomer William Herschel on 19 November 1783. The cluster is about two billion years old and it is located 10,000 light years away. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=115.2644247%2022.0068357&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 248. [AT2026ahzy](https://www.wis-tns.org/object/2026ahzy) near Lynds Bright Nebula 114 (LBN114)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 114 (LBN114) as this object's host. The 0.63998° (38.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:15:24Z · 3 days · 19.73 r |
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
| Subject | **Lynds Bright Nebula 114 (LBN114)** · `LBN114` |
| Catalog display name | Lynds Bright Nebula 114 (LBN114) |
| Type / constellation | HII · Aquila |
| Catalog magnitude / angular size | — · 85′ × 30′ |
| Distance | — |
| Separation | 0.63998° · 38.40′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahzy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=307.8490526%20-3.1156172&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 249. [AT2026aibk](https://www.wis-tns.org/object/2026aibk) near NGC843

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC843 as this object's host. The 0.80016° (48.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:32:09Z · 8 days · 21.26 r |
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
| Subject | **NGC843** · `NGC843` |
| Catalog display name | NGC843 |
| Type / constellation | Nebula · Triangulum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.80016° · 48.01′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.838792%2032.103825&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 250. [AT2026aiic](https://www.wis-tns.org/object/2026aiic) near Lynds Bright Nebula 220 (LBN220)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 220 (LBN220) as this object's host. The 0.80240° (48.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T04:23:06Z · 3 days · 20.55 g |
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
| Subject | **Lynds Bright Nebula 220 (LBN220)** · `LBN220` |
| Catalog display name | Lynds Bright Nebula 220 (LBN220) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 25′ × 10′ |
| Distance | — |
| Separation | 0.80240° · 48.14′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiic) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=326.4638195%2021.6260721&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 251. [AT2026aiio](https://www.wis-tns.org/object/2026aiio) near NGC930

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC930 as this object's host. The 0.95799° (57.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T06:44:12Z · 17 days · 20.63 r |
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
| Subject | **NGC930** · `NGC930` |
| Catalog display name | NGC930 |
| Type / constellation | Nebula · Aries |
| Catalog magnitude / angular size | — · 0.1′ × 0.1′ |
| Distance | — |
| Separation | 0.95799° · 57.48′ |
| Catalog description | NGC 932 is a spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 3,837±17 km/s, which corresponds to a Hubble distance of 184.6 ± 12.9 Mly (56.59 ± 3.97 Mpc). It was discovered by German-British astronomer William Herschel on 29 November 1785. There has been a longstanding confusion between this galaxy and NGC 930, which is a nonexistent object. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiio) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.1442194%2021.2845878&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 252. [AT2026ahpi](https://www.wis-tns.org/object/2026ahpi) near IC5385

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5385 as this object's host. The 1.37483° (82.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T15:05:45Z · 19 days · 22.57 r |
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
| Subject | **IC5385** · `IC5385` |
| Catalog display name | IC5385 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.37483° · 82.49′ |
| Catalog description | extremely, excessively faint (not verified) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.431958%201.288361&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 253. [AT2026ahrk](https://www.wis-tns.org/object/2026ahrk) near NGC603

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC603 as this object's host. The 1.73907° (104.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T19:50:52Z · 9 days · 20.02 g |
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
| Subject | **NGC603** · `NGC603` |
| Catalog display name | NGC603 |
| Type / constellation | Nebula · Triangulum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.73907° · 104.34′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahrk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.305708%2029.217428&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 254. [AT2026ahso](https://www.wis-tns.org/object/2026ahso) near IC1475

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1475 as this object's host. The 1.54946° (92.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T10:18:48Z · 9 days · 20.22 L |
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
| Subject | **IC1475** · `IC1475` |
| Catalog display name | IC1475 |
| Type / constellation | Nebula · Sculptor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.54946° · 92.97′ |
| Catalog description | nebula a single star |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahso) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.76849%20-27.345293&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 255. [AT2026ahuk](https://www.wis-tns.org/object/2026ahuk) near IC5385

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5385 as this object's host. The 1.31983° (79.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T14:02:24Z · 9 days · 21.89 g |
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
| Subject | **IC5385** · `IC5385` |
| Catalog display name | IC5385 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.31983° · 79.19′ |
| Catalog description | extremely, excessively faint (not verified) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=2.1745%20-1.262897&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 256. [AT2026ahux](https://www.wis-tns.org/object/2026ahux) near NGC611

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC611 as this object's host. The 1.75896° (105.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:02:54Z · 8 days · 20.27 L |
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
| Subject | **NGC611** · `NGC611` |
| Catalog display name | NGC611 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.75896° · 105.54′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahux) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=23.338686%20-18.382799&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 257. [AT2026ahuz](https://www.wis-tns.org/object/2026ahuz) near Lynds Bright Nebula 1025 (LBN1025)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1025 (LBN1025) as this object's host. The 1.74006° (104.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T15:20:18Z · 4 days · 19.92 L |
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
| Subject | **Lynds Bright Nebula 1025 (LBN1025)** · `LBN1025` |
| Catalog display name | Lynds Bright Nebula 1025 (LBN1025) |
| Type / constellation | HII · Lepus |
| Catalog magnitude / angular size | — · 140′ × 90′ |
| Distance | — |
| Separation | 1.74006° · 104.40′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahuz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=89.54669%20-16.595882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 258. [AT2026ahve](https://www.wis-tns.org/object/2026ahve) near Collinder 120 (CR120)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 120 (CR120) as this object's host. The 1.02417° (61.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-21T12:40:27Z · 16 days · 19.59 cyan |
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
| Subject | **Collinder 120 (CR120)** · `CR120` |
| Catalog display name | Collinder 120 (CR120) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 10 · 4.8′ × 4.8′ |
| Distance | 4.4 kpc |
| Separation | 1.02417° · 61.45′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahve) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=102.7245067%2018.0992333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 259. [AT2026ahwr](https://www.wis-tns.org/object/2026ahwr) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.72552° (103.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T12:57:36Z · 7 days · 22.4 r |
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
| Subject | **Lynds Bright Nebula 188 (LBN188)** · `LBN188` |
| Catalog display name | Lynds Bright Nebula 188 (LBN188) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 22′ × 12′ |
| Distance | — |
| Separation | 1.72552° · 103.53′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahwr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.032833%20-0.692419&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 260. [AT2026ahxv](https://www.wis-tns.org/object/2026ahxv) near Lynds Bright Nebula 530 (LBN530)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 530 (LBN530) as this object's host. The 1.03366° (62.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T06:36:05Z · 3 days · 19.84 g |
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
| Subject | **Lynds Bright Nebula 530 (LBN530)** · `LBN530` |
| Catalog display name | Lynds Bright Nebula 530 (LBN530) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 25′ × 12′ |
| Distance | — |
| Separation | 1.03366° · 62.02′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahxv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.6408241%2019.9527472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 261. [AT2026ahyv](https://www.wis-tns.org/object/2026ahyv) near Lynds Bright Nebula 799 (LBN799)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 799 (LBN799) as this object's host. The 1.12214° (67.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T14:09:40Z · 4 days · 21.02 w |
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
| Subject | **Lynds Bright Nebula 799 (LBN799)** · `LBN799` |
| Catalog display name | Lynds Bright Nebula 799 (LBN799) |
| Type / constellation | HII · Taurus |
| Catalog magnitude / angular size | — · 140′ × 10′ |
| Distance | — |
| Separation | 1.12214° · 67.33′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahyv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.8616662%2022.8301281&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 262. [AT2026ahzq](https://www.wis-tns.org/object/2026ahzq) near Lynds Bright Nebula 991 (LBN991)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 991 (LBN991) as this object's host. The 1.87296° (112.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:01:55Z · 5 days · 20.23 L |
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
| Subject | **Lynds Bright Nebula 991 (LBN991)** · `LBN991` |
| Catalog display name | Lynds Bright Nebula 991 (LBN991) |
| Type / constellation | HII · Lepus |
| Catalog magnitude / angular size | — · 70′ × 5′ |
| Distance | — |
| Separation | 1.87296° · 112.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahzq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.45043%20-13.814005&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 263. [AT2026aiak](https://www.wis-tns.org/object/2026aiak) near Lynds Bright Nebula 753 (LBN753)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 753 (LBN753) as this object's host. The 1.72475° (103.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T08:08:20Z · 3 days · 19.6 w |
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
| Subject | **Lynds Bright Nebula 753 (LBN753)** · `LBN753` |
| Catalog display name | Lynds Bright Nebula 753 (LBN753) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 100′ × 60′ |
| Distance | — |
| Separation | 1.72475° · 103.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiak) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=41.946462%2018.4070461&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 264. [AT2026aial](https://www.wis-tns.org/object/2026aial) near Lynds Bright Nebula 711 (LBN711)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 711 (LBN711) as this object's host. The 1.61980° (97.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T08:01:58Z · 3 days · 20.94 w |
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
| Subject | **Lynds Bright Nebula 711 (LBN711)** · `LBN711` |
| Catalog display name | Lynds Bright Nebula 711 (LBN711) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 30′ × 10′ |
| Distance | — |
| Separation | 1.61980° · 97.19′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aial) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=38.7166617%2019.6411068&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 265. [AT2026aidb](https://www.wis-tns.org/object/2026aidb) near Sharpless 246 (SH2-246)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 246 (SH2-246) as this object's host. The 1.22301° (73.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T12:14:40Z · 2 days · 20.12 r |
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
| Subject | **Sharpless 246 (SH2-246)** · `SH2-246` |
| Catalog display name | Sharpless 246 (SH2-246) |
| Type / constellation | HII · Orion |
| Catalog magnitude / angular size | — · 65′ × 65′ |
| Distance | — |
| Separation | 1.22301° · 73.38′ |
| Catalog description | Sh 2-308, also designated as Sharpless 308, RCW 11, or LBN 1052, and commonly known as the Dolphin-Head Nebula, is an H II region located near the center of the constellation Canis Major, composed of ionised hydrogen. It is about 8 degrees south of Sirius, the brightest star in the night sky. The nebula is bubble-like and surrounds a Wolf–Rayet star named EZ Canis Majoris. This star is in the brief, pre-supernova phase of its stellar evolution. The nebula is about 4,530 light-years away from Earth, but some sources indicate that both the star and the nebula are up to 5,870 ly (1,800 pc) away. Yet others indicate the nebula is as close as 1,875 ly (575 pc) from Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aidb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.5778549%2014.7204123&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 266. [AT2026aiip](https://www.wis-tns.org/object/2026aiip) near NGC1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1639 as this object's host. The 1.39017° (83.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T09:31:11Z · 17 days · 20.62 g |
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
| Subject | **NGC1639** · `NGC1639` |
| Catalog display name | NGC1639 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.39017° · 83.41′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiip) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.8114254%20-17.7870937&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 267. [AT2026aikj](https://www.wis-tns.org/object/2026aikj) near Lynds Bright Nebula 1010 (LBN1010)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1010 (LBN1010) as this object's host. The 1.53192° (91.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:17:28Z · 1 days · 20.02 L |
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
| Subject | **Lynds Bright Nebula 1010 (LBN1010)** · `LBN1010` |
| Catalog display name | Lynds Bright Nebula 1010 (LBN1010) |
| Type / constellation | HII · Lepus |
| Catalog magnitude / angular size | — · 200′ × 10′ |
| Distance | — |
| Separation | 1.53192° · 91.92′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aikj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=85.7871569%20-14.4729707&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 268. [AT2026ahrf](https://www.wis-tns.org/object/2026ahrf) near Lynds Bright Nebula 715 (LBN715)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 715 (LBN715) as this object's host. The 0.40429° (24.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T21:37:26Z · 20 days · 20.74 r |
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
| Subject | **Lynds Bright Nebula 715 (LBN715)** · `LBN715` |
| Catalog display name | Lynds Bright Nebula 715 (LBN715) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 60′ × 8′ |
| Distance | — |
| Separation | 0.40429° · 24.26′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahrf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.611792%2013.025892&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 269. [AT2026ahvq](https://www.wis-tns.org/object/2026ahvq) near Headphone nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Headphone nebula as this object's host. The 0.64976° (38.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T10:19:30Z · 12 days · 20.36 r |
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
| Subject | **Headphone nebula** · `JnEr1` |
| Catalog display name | Headphone nebula |
| Type / constellation | Planetary nebula · Lyn |
| Catalog magnitude / angular size | — · 6.3′ × 6.3′ |
| Distance | 1,600 ly |
| Separation | 0.64976° · 38.99′ |
| Catalog description | Jones-Emberson 1, also known as the Headphone Nebula, is a 14th magnitude planetary nebula in the constellation Lynx at a distance of 1600 light years. It is a larger planetary with low surface brightness. The 16.8-magnitude central star is a very blue white dwarf. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahvq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.8250717%2054.0266035&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 270. [AT2026aiir](https://www.wis-tns.org/object/2026aiir) near Lynds Bright Nebula 790 (LBN790)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 790 (LBN790) as this object's host. The 0.58443° (35.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T11:44:01Z · 30 days · 20.1 r |
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
| Subject | **Lynds Bright Nebula 790 (LBN790)** · `LBN790` |
| Catalog display name | Lynds Bright Nebula 790 (LBN790) |
| Type / constellation | HII · Lynx |
| Catalog magnitude / angular size | — · 30′ × 10′ |
| Distance | — |
| Separation | 0.58443° · 35.07′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiir) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=118.8242602%2046.6763504&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 271. [SN2026abza](https://www.wis-tns.org/object/2026abza) near NGC1637

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 30/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1637 as this object's host. The 0.27656° (16.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.062 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-10T11:57:31Z · 57 days · 20.22 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3781....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR3781....1S/abstract) |
| Classification references | [2026TNSCR4209....1K](https://ui.adsabs.harvard.edu/abs/2026TNSCR4209....1K/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1637** · `NGC1637` |
| Catalog display name | NGC1637 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.8 · 3.18′ × 2.74′ |
| Distance | — |
| Separation | 0.27656° · 16.59′ |
| Catalog description | NGC 1637 is an isolated, non-interacting intermediate spiral galaxy in the constellation Eridanus, about a degree to the WNW of the star Mu Eridani. It was discovered by German-British astronomer William Herschel on 1 February 1786. It is located at a distance of about 9.77 ± 1.82 Mpc (31.9 ± 5.9 Mly) from the Milky Way. The galaxy is inclined at an angle of 31.1° to the line of sight from the Earth and the long axis is oriented along a position angle of 16.3°. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abza) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=70.2756302%20-3.1191577&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 272. [AT2026adph](https://www.wis-tns.org/object/2026adph) near IC 1749

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 28/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1749 as this object's host. The 1.01030° (60.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-24T04:35:55Z · 43 days · 19.38 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3938....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3938....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1749** · `IC 1749` |
| Catalog display name | NGC 1701 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.06′ × 0.69′ |
| Distance | 282 ly |
| Separation | 1.01030° · 60.62′ |
| Catalog description | NGC 1701, also known as the Trekkie Galaxy, is a large unbarred spiral galaxy located in the constellation Caelum. Its speed relative to the cosmic microwave background is 5,836 ± 24 km/s, which corresponds to a Hubble distance of 86.1 ± 6.0 Mpc. It was discovered by the British astronomer John Herschel in 1834. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1749 has the different designation NGC 1701 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adph) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.1636656%207.7485115&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 273. [AT2026aflk](https://www.wis-tns.org/object/2026aflk) near Lynds Bright Nebula 639 (LBN639)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 639 (LBN639) as this object's host. The 1.56774° (94.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-08T19:36:28Z · 29 days · 22.07 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4136....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4136....1X/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 639 (LBN639)** · `LBN639` |
| Catalog display name | Lynds Bright Nebula 639 (LBN639) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 25′ × 8′ |
| Distance | — |
| Separation | 1.56774° · 94.06′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aflk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.6138792%2018.1456856&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 274. [AT2026ahbl](https://www.wis-tns.org/object/2026ahbl) near Lynds Bright Nebula 157 (LBN157)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 157 (LBN157) as this object's host. The 1.08937° (65.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T20:02:06Z · 9 days · 19.99 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4342....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4342....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 157 (LBN157)** · `LBN157` |
| Catalog display name | Lynds Bright Nebula 157 (LBN157) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 90′ × 20′ |
| Distance | — |
| Separation | 1.08937° · 65.36′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahbl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=327.6610713%2012.1553591&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 275. [AT2026ahvo](https://www.wis-tns.org/object/2026ahvo) near Lynds Bright Nebula 141 (LBN141)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 141 (LBN141) as this object's host. The 1.06337° (63.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T04:59:43Z · 20 days · 19.6 g |
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
| Subject | **Lynds Bright Nebula 141 (LBN141)** · `LBN141` |
| Catalog display name | Lynds Bright Nebula 141 (LBN141) |
| Type / constellation | HII · Delphinus |
| Catalog magnitude / angular size | — · 160′ × 60′ |
| Distance | — |
| Separation | 1.06337° · 63.80′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahvo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=306.5934253%2021.036538&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 276. [AT2026ahwi](https://www.wis-tns.org/object/2026ahwi) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.87304° (112.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T14:26:52Z · 19 days · 22.19 r |
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
| Subject | **Lynds Bright Nebula 188 (LBN188)** · `LBN188` |
| Catalog display name | Lynds Bright Nebula 188 (LBN188) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 22′ × 12′ |
| Distance | — |
| Separation | 1.87304° · 112.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahwi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.257083%20-1.301314&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 277. [AT2026ahwn](https://www.wis-tns.org/object/2026ahwn) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.79970° (107.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:48:57Z · 8 days · 22.55 g |
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
| Subject | **Lynds Bright Nebula 188 (LBN188)** · `LBN188` |
| Catalog display name | Lynds Bright Nebula 188 (LBN188) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 22′ × 12′ |
| Distance | — |
| Separation | 1.79970° · 107.98′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahwn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.873375%20-1.063175&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 278. [AT2026ahpq](https://www.wis-tns.org/object/2026ahpq) near Messier 32 (M32)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 32 (M32) as this object's host. The 0.33280° (19.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T19:04:48Z · 36 days · 21.74 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4384....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4384....1X/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Messier 32 (M32)** · `M32` |
| Catalog display name | Messier 32 (M32) |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 8.1 · 8′ × 6′ |
| Distance | 889.144 kpc |
| Separation | 0.33280° · 19.97′ |
| Catalog description | Messier 32 is a dwarf "early-type" galaxy about 2,490,000 light-years (760,000 pc) from the Solar System, appearing in the constellation Andromeda. M32 is a satellite galaxy of the Andromeda Galaxy (M31) and was discovered by Guillaume Le Gentil in 1749. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.104667%2040.795192&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 279. [AT2026ahwf](https://www.wis-tns.org/object/2026ahwf) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.55155° (33.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T15:27:21Z · 36 days · 21.45 g |
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
| Subject | **NGC741** · `NGC741` |
| Catalog display name | NGC741 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 11.3 · 2.83′ × 2.33′ |
| Distance | — |
| Separation | 0.55155° · 33.09′ |
| Catalog description | NGC 741, also known as PGC 7252, is a formerly active radio galaxy in the constellation of Pisces. Located 74.13 Mpc away, NGC 741 is part of a group of galaxies including NGC 742 and PGC 7250. NGC 741 and NGC 742 recently collided, although the disruption was minor. Radio filaments have been found connecting NGC 741 to NGC 742, and due to the bent structure of the radio filaments, NGC 741 is estimated to be moving at 1400 km/s with respect to its local group, suggesting that ram-pressure stripping was created as a product of the former merger. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.186458%205.086264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 280. [AT2026aiiq](https://www.wis-tns.org/object/2026aiiq) near IC 1962

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1962 as this object's host. The 0.89936° (53.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-06T08:56:10Z · 31 days · 19.77 i |
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
| Subject | **IC 1962** · `IC 1962` |
| Catalog display name | NGC 568 |
| Type / constellation | Galaxy · Eri |
| Catalog magnitude / angular size | — · 2.25′ × 0.5′ |
| Distance | 266,000,000 ly |
| Separation | 0.89936° · 53.96′ |
| Catalog description | NGC 568, also commonly referred as IC 1709 is an unbarred lenticular galaxy in the constellation of Sculptor. The galaxy is 266 million light-years from Earth and was discovered by John Herschel on November 29, 1837, and Lewis Swift, an American astronomer who listed it and gave it the name IC 1709 on September 4, 1897. NGC 568, also commonly referred as IC 1709 is an unbarred lenticular galaxy in the constellation of Sculptor. The galaxy is 266 million light-years from Earth and was discovered by John Herschel on November 29, 1837, and Lewis Swift, an American astronomer who listed it and gave it the name IC 1709 on September 4, 1897. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1962 has the different designation NGC 568 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiiq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.5822419%20-20.4471705&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 281. [AT2026ahwg](https://www.wis-tns.org/object/2026ahwg) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.28105° (76.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T14:36:57Z · 33 days · 22.94 g |
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
| Subject | **IC 1481** · `IC 1481` |
| Catalog display name | IC 1481 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.73′ × 0.65′ |
| Distance | 289 ly |
| Separation | 1.28105° · 76.86′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahwg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.908417%205.037917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 282. [AT2026aibe](https://www.wis-tns.org/object/2026aibe) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.67355° (100.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T21:50:24Z · 33 days · 21.74 r |
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
| Subject | **Silver Sliver Galaxy** · `C23` |
| Catalog display name | Silver Sliver Galaxy |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 9.9 · 14′ × 2′ |
| Distance | — |
| Separation | 1.67355° · 100.41′ |
| Catalog description | NGC 891 is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda. It was discovered by William Herschel on October 6, 1784. The galaxy is a member of the NGC 1023 group of galaxies in the Local Supercluster. It has an H II nucleus. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aibe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.019667%2043.531639&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 283. [AT2026aepe](https://www.wis-tns.org/object/2026aepe) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 1.22702° (73.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T11:47:52Z · 36 days · 19.97 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4019....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4019....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1623** · `IC 1623` |
| Catalog display name | IC 1623 |
| Type / constellation | CiG · Cet |
| Catalog magnitude / angular size | — · 1.2′ × 1.2′ |
| Distance | 269,000,000 ly |
| Separation | 1.22702° · 73.62′ |
| Catalog description | IC 1623 is a galaxy merger in the constellation Cetus. The galaxy lies about 250 million light years away from Earth, which means, given its apparent dimensions, that IC 1623 is approximately 115,000 light years across. It was discovered by Lewis Swift on November 19, 1897. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aepe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.909193%20-0.561916&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 284. [AT2026aghp](https://www.wis-tns.org/object/2026aghp) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.58735° (95.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T11:47:23Z · 33 days · 20.88 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4244....1C](https://ui.adsabs.harvard.edu/abs/2026TNSTR4244....1C/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC894** · `NGC894` |
| Catalog display name | NGC894 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.58735° · 95.24′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aghp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.9770743%20-5.3409875&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
