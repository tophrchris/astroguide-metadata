# TNS transient opportunity review — 2026-11-26

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `42ddf3e53998c8c3`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 205 review opportunities: 18 urgent, 187 watch, 0 expired
- Recommendations: 16 approve, 189 hold, 0 reject
- 205 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 505 staged rows collapsed to 477 unique TNS objects (28 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026akhh](https://www.wis-tns.org/object/2026akhh) | SN Ia | 9 | 18.34 | IC2013 (Nebula) | 0.18157° | near-field match | 100 | approve |
| urgent | [SN2026aknq](https://www.wis-tns.org/object/2026aknq) | SN II | 3 | 17.99 | NGC1367 (Galaxy) | 0.76736° | near-field match | 100 | approve |
| urgent | [SN2026aizp](https://www.wis-tns.org/object/2026aizp) | SN Ia-91T-like | 17 | 18.1 | Atoms For Peace Galaxy (Galaxy) | 0.49883° | near-field match | 97 | approve |
| urgent | [AT2026ajxw](https://www.wis-tns.org/object/2026ajxw) | transient_candidate | 11 | 18.22 | IC750 (Galaxy) | 0.12312° | near-field match | 95 | approve |
| urgent | [AT2026aktu](https://www.wis-tns.org/object/2026aktu) | transient_candidate | 2 | 15.64 | NGC5054 (Galaxy) | 1.78838° | near-field match | 93 | approve |
| urgent | [AT2026aktv](https://www.wis-tns.org/object/2026aktv) | transient_candidate | 2 | 17.6 | IC4221 (Galaxy) | 0.97309° | near-field match | 90 | approve |
| urgent | [AT2026akhc](https://www.wis-tns.org/object/2026akhc) | transient_candidate | 7 | 18.43 | IC 4168 (Galaxy) | 1.48969° | near-field match | 83 | hold |
| urgent | [AT2026akoc](https://www.wis-tns.org/object/2026akoc) | transient_candidate | 3 | 16.69 | NGC5377 (Galaxy) | 1.96450° | near-field match | 83 | approve |
| urgent | [AT2026akok](https://www.wis-tns.org/object/2026akok) | transient_candidate | 2 | 18.38 | IC 1288 (Galaxy) | 1.34317° | near-field match | 83 | hold |
| urgent | [AT2026akqe](https://www.wis-tns.org/object/2026akqe) | transient_candidate | 2 | 17.34 | IC947 (Galaxy) | 1.43560° | near-field match | 83 | approve |
| urgent | [AT2026akqu](https://www.wis-tns.org/object/2026akqu) | transient_candidate | 2 | 15.4 | Caldwell 105 (C105) (Globular cluster) | 1.90156° | near-field match | 83 | approve |
| urgent | [AT2026aksh](https://www.wis-tns.org/object/2026aksh) | transient_candidate | 0 | 17.98 | IC2104 (Galaxy) | 1.67721° | near-field match | 83 | approve |
| urgent | [AT2026ahzh](https://www.wis-tns.org/object/2026ahzh) | transient_candidate | 23 | 18.28 | NGC3665 (Galaxy) | 0.91144° | near-field match | 82 | approve |
| urgent | [AT2026akod](https://www.wis-tns.org/object/2026akod) | transient_candidate | 4 | 18.26 | Collinder 166 (CR166) (Open cluster) | 0.68541° | near-field match | 80 | approve |
| urgent | [AT2026akof](https://www.wis-tns.org/object/2026akof) | transient_candidate | 4 | 17.9 | NGC1890 (Open cluster) | 0.42602° | near-field match | 80 | approve |
| urgent | [AT2026akhs](https://www.wis-tns.org/object/2026akhs) | transient_candidate | 8 | 18.03 | NGC6958 (Galaxy) | 1.67482° | near-field match | 75 | approve |
| urgent | [AT2026aklg](https://www.wis-tns.org/object/2026aklg) | transient_candidate | 15 | 17.75 | NGC5204 (Galaxy) | 1.43417° | near-field match | 75 | approve |
| urgent | [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) | transient_candidate | 12 | 18.22 | IC765 (Nebula) | 0.75219° | near-field match | 72 | approve |
| watch | [SN2026akbo](https://www.wis-tns.org/object/2026akbo) | SN Ia | 9 | 18.76 | NGC3344 (Galaxy) | 0.96185° | near-field match | 87 | hold |
| watch | [AT2026aklo](https://www.wis-tns.org/object/2026aklo) | transient_candidate | 5 | 19.28 | IC391 (Galaxy) | 0.49605° | near-field match | 80 | hold |
| watch | [AT2026akmw](https://www.wis-tns.org/object/2026akmw) | transient_candidate | 4 | 18.65 | NGC7741 (Galaxy) | 0.42553° | near-field match | 80 | hold |
| watch | [AT2026akpx](https://www.wis-tns.org/object/2026akpx) | transient_candidate | 4 | 19.36 | NGC4208 (Galaxy) | 0.33686° | near-field match | 80 | hold |
| watch | [AT2026akqm](https://www.wis-tns.org/object/2026akqm) | transient_candidate | 2 | 19.02 | IC 3591 (Galaxy) | 0.91545° | near-field match | 80 | hold |
| watch | [AT2026akqr](https://www.wis-tns.org/object/2026akqr) | transient_candidate | 4 | 19.39 | IC209 (Galaxy) | 0.27005° | near-field match | 80 | hold |
| watch | [AT2026akru](https://www.wis-tns.org/object/2026akru) | transient_candidate | 1 | 18.8 | NGC3953 (Galaxy) | 0.41812° | near-field match | 80 | hold |
| watch | [SN2026akhl](https://www.wis-tns.org/object/2026akhl) | SN Ia | 7 | 18.85 | NGC2886 (Nebula) | 1.56605° | near-field match | 78 | hold |
| watch | [AT2026akgx](https://www.wis-tns.org/object/2026akgx) | transient_candidate | 7 | 19.28 | NGC1569 (Galaxy) | 1.05967° | near-field match | 73 | hold |
| watch | [AT2026akhf](https://www.wis-tns.org/object/2026akhf) | transient_candidate | 7 | 19.45 | NGC3726 (Galaxy) | 1.78481° | near-field match | 73 | hold |
| watch | [AT2026akmg](https://www.wis-tns.org/object/2026akmg) | transient_candidate | 5 | 18.66 | NGC797 (Galaxy) | 1.94196° | near-field match | 73 | hold |
| watch | [AT2026akmz](https://www.wis-tns.org/object/2026akmz) | transient_candidate | 4 | 19.11 | NGC4546 (Galaxy) | 1.35021° | near-field match | 73 | hold |
| watch | [AT2026akna](https://www.wis-tns.org/object/2026akna) | transient_candidate | 4 | 18.85 | NGC3887 (Galaxy) | 1.45843° | near-field match | 73 | hold |
| watch | [AT2026akqa](https://www.wis-tns.org/object/2026akqa) | transient_candidate | 2 | 19.37 | NGC 3561 (Galaxy) | 1.11429° | near-field match | 73 | hold |
| watch | [AT2026akqi](https://www.wis-tns.org/object/2026akqi) | transient_candidate | 4 | 19.49 | IC 1863 (Galaxy) | 1.79631° | near-field match | 73 | hold |
| watch | [AT2026akrw](https://www.wis-tns.org/object/2026akrw) | transient_candidate | 1 | 18.92 | NGC 1954 (Galaxy) | 1.30231° | near-field match | 73 | hold |
| watch | [AT2026akse](https://www.wis-tns.org/object/2026akse) | transient_candidate | 0 | 18.56 | IC5171 (Galaxy) | 1.90262° | near-field match | 73 | hold |
| watch | [AT2026akts](https://www.wis-tns.org/object/2026akts) | transient_candidate | 0 | 19.49 | NGC3344 (Galaxy) | 1.43147° | near-field match | 73 | hold |
| watch | [AT2026aktt](https://www.wis-tns.org/object/2026aktt) | transient_candidate | 0 | 18.86 | NGC2986 (Galaxy) | 1.04778° | near-field match | 73 | hold |
| watch | [AT2026aktw](https://www.wis-tns.org/object/2026aktw) | transient_candidate | 0 | 19.03 | IC 892 (Galaxy) | 1.25329° | near-field match | 73 | hold |
| watch | [AT2026akhu](https://www.wis-tns.org/object/2026akhu) | transient_candidate | 8 | 19.35 | NGC2325 (Galaxy) | 0.61029° | near-field match | 72 | hold |
| watch | [AT2026aknb](https://www.wis-tns.org/object/2026aknb) | transient_candidate | 8 | 19.48 | IC3908 (Galaxy) | 0.25465° | near-field match | 72 | hold |
| watch | [AT2026akqc](https://www.wis-tns.org/object/2026akqc) | transient_candidate | 19 | 18.99 | IC 3954 (Galaxy) | 0.35495° | near-field match | 72 | hold |
| watch | [SN2026aiep](https://www.wis-tns.org/object/2026aiep) | SN Ia | 22 | 19.17 | IC5194 (Nebula) | 1.65297° | near-field match | 70 | hold |
| watch | [SN2026ajxu](https://www.wis-tns.org/object/2026ajxu) | SN Ia | 11 | 19.22 | Collinder 27 (CR27) (Open cluster) | 1.69919° | near-field match | 70 | hold |
| watch | [AT2026akqd](https://www.wis-tns.org/object/2026akqd) | transient_candidate | 2 | 18.76 | IC2988 (Nebula) | 0.99471° | near-field match | 70 | hold |
| watch | [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) | transient_candidate | 14 | 19.46 | NGC1169 (Galaxy) | 1.01795° | near-field match | 65 | hold |
| watch | [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) | transient_candidate | 14 | 18.82 | NGC 3294 (Galaxy) | 1.51580° | near-field match | 65 | hold |
| watch | [AT2026akhd](https://www.wis-tns.org/object/2026akhd) | transient_candidate | 8 | 18.95 | IC625 (Galaxy) | 1.99202° | near-field match | 65 | hold |
| watch | [AT2026akhx](https://www.wis-tns.org/object/2026akhx) | transient_candidate | 19 | 21.13 | NGC3640 (Galaxy) | 0.12692° | near-field match | 65 | hold |
| watch | [AT2026akir](https://www.wis-tns.org/object/2026akir) | transient_candidate | 15 | 20.71 | NGC4450 (Galaxy) | 0.23305° | near-field match | 65 | hold |
| watch | [AT2026akjq](https://www.wis-tns.org/object/2026akjq) | transient_candidate | 24 | 19.97 | NGC3348 (Galaxy) | 0.04308° | near-field match | 65 | hold |
| watch | [AT2026akju](https://www.wis-tns.org/object/2026akju) | transient_candidate | 9 | 22.1 | NGC741 (Galaxy) | 0.15603° | near-field match | 65 | hold |
| watch | [AT2026akmp](https://www.wis-tns.org/object/2026akmp) | transient_candidate | 8 | 18.76 | IC 892 (Galaxy) | 1.54281° | near-field match | 65 | hold |
| watch | [AT2026akqh](https://www.wis-tns.org/object/2026akqh) | transient_candidate | 2 | 17.63 | Lynds Bright Nebula 111 (LBN111) (HII) | 1.43721° | near-field match | 65 | hold |
| watch | [SN2026afsg](https://www.wis-tns.org/object/2026afsg) | SN Ib/c | 39 | 16.4 | NGC 2207 / IC 2163 (Galaxy) | 1.22591° | near-field match | 63 | hold |
| watch | [AT2026akhq](https://www.wis-tns.org/object/2026akhq) | transient_candidate | 7 | 19.21 | IC3668 (Nebula) | 1.11334° | near-field match | 63 | hold |
| watch | [AT2026akiv](https://www.wis-tns.org/object/2026akiv) | transient_candidate | 6 | 20 | IC488 (Nebula) | 0.01538° | near-field match | 63 | hold |
| watch | [AT2026akiw](https://www.wis-tns.org/object/2026akiw) | transient_candidate | 6 | 19.34 | IC656 (Nebula) | 1.14129° | near-field match | 63 | hold |
| watch | [AT2026aklr](https://www.wis-tns.org/object/2026aklr) | transient_candidate | 4 | 19.48 | Baxendell's unphotographable nebula (Nebula) | 1.57712° | near-field match | 63 | hold |
| watch | [AT2026akly](https://www.wis-tns.org/object/2026akly) | transient_candidate | 4 | 19.35 | NGC7453 (Nebula) | 1.92745° | near-field match | 63 | hold |
| watch | [SN2026aifu](https://www.wis-tns.org/object/2026aifu) | SN II | 22 | 19.01 | Lynds Bright Nebula 1025 (LBN1025) (HII) | 1.13184° | near-field match | 62 | hold |
| watch | [AT2026akit](https://www.wis-tns.org/object/2026akit) | transient_candidate | 8 | 19.03 | IC1560 (Nebula) | 0.48581° | near-field match | 62 | hold |
| watch | [AT2026akll](https://www.wis-tns.org/object/2026akll) | transient_candidate | 8 | 19.48 | Skull Nebula (Planetary nebula) | 0.58800° | near-field match | 62 | hold |
| watch | [SN2026aeru](https://www.wis-tns.org/object/2026aeru) | SN II | 50 | 18.09 | NGC 3003 (Galaxy) | 0.80302° | near-field match | 60 | hold |
| watch | [SN2026ahby](https://www.wis-tns.org/object/2026ahby) | SN Ia | 29 | 19.7 | IC1438 (Galaxy) | 1.07176° | near-field match | 60 | hold |
| watch | [SN2026aikx](https://www.wis-tns.org/object/2026aikx) | SN Ia | 21 | 20.65 | IC 1730 (Galaxy) | 1.43755° | near-field match | 60 | hold |
| watch | [AT2026akjk](https://www.wis-tns.org/object/2026akjk) | transient_candidate | 5 | 19.66 | IC 1753 (Galaxy) | 0.98851° | near-field match | 60 | hold |
| watch | [SN2026akpz](https://www.wis-tns.org/object/2026akpz) | SN Ia | 14 | 19.85 | NGC524 (Galaxy) | 1.04562° | near-field match | 60 | hold |
| watch | [AT2026aksi](https://www.wis-tns.org/object/2026aksi) | transient_candidate | 1 | 19.7 | IC396 (Galaxy) | 0.85301° | near-field match | 60 | hold |
| watch | [AT2026aktz](https://www.wis-tns.org/object/2026aktz) | transient_candidate | 0 | 21.48 | NGC1332 (Galaxy) | 0.54438° | near-field match | 60 | hold |
| watch | [AT2026akua](https://www.wis-tns.org/object/2026akua) | transient_candidate | 0 | 21.9 | NGC1400 (Galaxy) | 0.41736° | near-field match | 60 | hold |
| watch | [AT2026akmb](https://www.wis-tns.org/object/2026akmb) | transient_candidate | 4 | 19.22 | Lynds Bright Nebula 113 (LBN113) (HII) | 1.07949° | near-field match | 55 | hold |
| watch | [AT2026akmx](https://www.wis-tns.org/object/2026akmx) | transient_candidate | 6 | 19.2 | Lynds Bright Nebula 563 (LBN563) (HII) | 1.15190° | near-field match | 55 | hold |
| watch | [AT2026aksj](https://www.wis-tns.org/object/2026aksj) | transient_candidate | 4 | 19.4 | Lynds Bright Nebula 702 (LBN702) (HII) | 1.88761° | near-field match | 55 | hold |
| watch | [AT2026akud](https://www.wis-tns.org/object/2026akud) | transient_candidate | 4 | 19.47 | Lynds Bright Nebula 853 (LBN853) (HII) | 1.82500° | near-field match | 55 | hold |
| watch | [AT2026akjn](https://www.wis-tns.org/object/2026akjn) | transient_candidate | 5 | 19.97 | Silver Sliver Galaxy (Galaxy) | 1.99665° | near-field match | 53 | hold |
| watch | [AT2026akml](https://www.wis-tns.org/object/2026akml) | transient_candidate | 6 | 19.57 | IC600 (Galaxy) | 1.95164° | near-field match | 53 | hold |
| watch | [AT2026akob](https://www.wis-tns.org/object/2026akob) | transient_candidate | 3 | 19.57 | IC 5126 (Galaxy) | 1.19520° | near-field match | 53 | hold |
| watch | [AT2026akol](https://www.wis-tns.org/object/2026akol) | transient_candidate | 6 | 21.96 | IC651 (Galaxy) | 1.39027° | near-field match | 53 | hold |
| watch | [AT2026akow](https://www.wis-tns.org/object/2026akow) | transient_candidate | 6 | 22.21 | IC651 (Galaxy) | 1.48427° | near-field match | 53 | hold |
| watch | [AT2026akpu](https://www.wis-tns.org/object/2026akpu) | transient_candidate | 7 | 21.09 | IC598 (Galaxy) | 1.02194° | near-field match | 53 | hold |
| watch | [AT2026akpw](https://www.wis-tns.org/object/2026akpw) | transient_candidate | 7 | 21.29 | NGC3079 (Galaxy) | 1.67677° | near-field match | 53 | hold |
| watch | [AT2026akqv](https://www.wis-tns.org/object/2026akqv) | transient_candidate | 5 | 20.78 | NGC3079 (Galaxy) | 1.39713° | near-field match | 53 | hold |
| watch | [AT2026akrd](https://www.wis-tns.org/object/2026akrd) | transient_candidate | 6 | 21.86 | IC 673 (Galaxy) | 1.31615° | near-field match | 53 | hold |
| watch | [AT2026akrf](https://www.wis-tns.org/object/2026akrf) | transient_candidate | 3 | 20.86 | IC 5374 (Galaxy) | 1.30131° | near-field match | 53 | hold |
| watch | [AT2026akrr](https://www.wis-tns.org/object/2026akrr) | transient_candidate | 7 | 20.45 | NGC3079 (Galaxy) | 1.65178° | near-field match | 53 | hold |
| watch | [AT2026akrs](https://www.wis-tns.org/object/2026akrs) | transient_candidate | 7 | 21.42 | NGC2950 (Galaxy) | 1.14398° | near-field match | 53 | hold |
| watch | [AT2026akrv](https://www.wis-tns.org/object/2026akrv) | transient_candidate | 5 | 19.9 | NGC772 (Galaxy) | 1.67884° | near-field match | 53 | hold |
| watch | [AT2026aksz](https://www.wis-tns.org/object/2026aksz) | transient_candidate | 7 | 21.76 | Local Group (Galaxy) | 1.08218° | near-field match | 53 | hold |
| watch | [AT2026akto](https://www.wis-tns.org/object/2026akto) | transient_candidate | 0 | 19.61 | NGC3665 (Galaxy) | 1.92423° | near-field match | 53 | hold |
| watch | [AT2026aipd](https://www.wis-tns.org/object/2026aipd) | transient_candidate | 29 | 21.22 | IC 1746 (Galaxy) | 0.30860° | near-field match | 52 | hold |
| watch | [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) | transient_candidate | 14 | 19.72 | NGC3239 (Galaxy) | 0.74061° | near-field match | 52 | hold |
| watch | [AT2026akbv](https://www.wis-tns.org/object/2026akbv) | transient_candidate | 9 | 19.99 | NGC 3686 (Galaxy) | 0.69980° | near-field match | 52 | hold |
| watch | [AT2026akhy](https://www.wis-tns.org/object/2026akhy) | transient_candidate | 19 | 20.64 | NGC3640 (Galaxy) | 0.74894° | near-field match | 52 | hold |
| watch | [AT2026akhz](https://www.wis-tns.org/object/2026akhz) | transient_candidate | 16 | 22.82 | IC 673 (Galaxy) | 0.60410° | near-field match | 52 | hold |
| watch | [AT2026akia](https://www.wis-tns.org/object/2026akia) | transient_candidate | 14 | 20.98 | NGC3166 (Galaxy) | 0.95306° | near-field match | 52 | hold |
| watch | [AT2026akib](https://www.wis-tns.org/object/2026akib) | transient_candidate | 18 | 21.56 | NGC3521 (Galaxy) | 0.61522° | near-field match | 52 | hold |
| watch | [AT2026akic](https://www.wis-tns.org/object/2026akic) | transient_candidate | 19 | 21.72 | NGC3640 (Galaxy) | 0.77839° | near-field match | 52 | hold |
| watch | [AT2026akjt](https://www.wis-tns.org/object/2026akjt) | transient_candidate | 16 | 22.87 | IC 632 (Galaxy) | 0.59759° | near-field match | 52 | hold |
| watch | [AT2026akko](https://www.wis-tns.org/object/2026akko) | transient_candidate | 14 | 22.14 | IC2446 (Galaxy) | 0.75145° | near-field match | 52 | hold |
| watch | [AT2026akkr](https://www.wis-tns.org/object/2026akkr) | transient_candidate | 12 | 20.74 | NGC3310 (Galaxy) | 0.66200° | near-field match | 52 | hold |
| watch | [AT2026akkw](https://www.wis-tns.org/object/2026akkw) | transient_candidate | 12 | 20.93 | NGC3319 (Galaxy) | 0.73584° | near-field match | 52 | hold |
| watch | [AT2026akkz](https://www.wis-tns.org/object/2026akkz) | transient_candidate | 9 | 21.29 | IC 1540 (Galaxy) | 0.38069° | near-field match | 52 | hold |
| watch | [AT2026aklt](https://www.wis-tns.org/object/2026aklt) | transient_candidate | 8 | 19.87 | IC5338 (Galaxy) | 0.28524° | near-field match | 52 | hold |
| watch | [AT2026akmy](https://www.wis-tns.org/object/2026akmy) | transient_candidate | 18 | 21.1 | IC1495 (Galaxy) | 0.90933° | near-field match | 52 | hold |
| watch | [AT2026akot](https://www.wis-tns.org/object/2026akot) | transient_candidate | 8 | 21.69 | IC 673 (Galaxy) | 0.83806° | near-field match | 52 | hold |
| watch | [AT2026akpe](https://www.wis-tns.org/object/2026akpe) | transient_candidate | 17 | 21.67 | NGC2549 (Galaxy) | 0.43964° | near-field match | 52 | hold |
| watch | [AT2026aksb](https://www.wis-tns.org/object/2026aksb) | transient_candidate | 8 | 19.75 | NGC 2207 / IC 2163 (Galaxy) | 0.44777° | near-field match | 52 | hold |
| watch | [AT2026aksr](https://www.wis-tns.org/object/2026aksr) | transient_candidate | 19 | 22.42 | IC 186 A (Galaxy) | 0.90589° | near-field match | 52 | hold |
| watch | [AT2026akte](https://www.wis-tns.org/object/2026akte) | transient_candidate | 29 | 20.29 | Mirach's Ghost (Galaxy) | 0.94077° | near-field match | 52 | hold |
| watch | [SN2026aisi](https://www.wis-tns.org/object/2026aisi) | SN Ia | 19 | 20.26 | Collinder 133 (CR133) (Open cluster) | 1.35375° | near-field match | 50 | hold |
| watch | [SN2026aiys](https://www.wis-tns.org/object/2026aiys) | SN Ia-91T-like | 17 | 19.55 | IC5251 (Nebula) | 1.74753° | near-field match | 50 | hold |
| watch | [AT2026airi](https://www.wis-tns.org/object/2026airi) | transient_candidate | 19 | 20.14 | NGC636 (Galaxy) | 1.79681° | near-field match | 45 | hold |
| watch | [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) | transient_candidate | 14 | 19.98 | IC1657 (Galaxy) | 1.48817° | near-field match | 45 | hold |
| watch | [AT2026akcc](https://www.wis-tns.org/object/2026akcc) | transient_candidate | 9 | 19.55 | IC2143 (Galaxy) | 1.17278° | near-field match | 45 | hold |
| watch | [AT2026akcy](https://www.wis-tns.org/object/2026akcy) | transient_candidate | 8 | 19.55 | Caldwell 48 (C48) (Galaxy) | 1.31632° | near-field match | 45 | hold |
| watch | [AT2026akgw](https://www.wis-tns.org/object/2026akgw) | transient_candidate | 11 | 19.98 | NGC7457 (Galaxy) | 1.57742° | near-field match | 45 | hold |
| watch | [AT2026akho](https://www.wis-tns.org/object/2026akho) | transient_candidate | 12 | 23.08 | IC2000 (Galaxy) | 1.12255° | near-field match | 45 | hold |
| watch | [AT2026akif](https://www.wis-tns.org/object/2026akif) | transient_candidate | 12 | 22.46 | IC 197 (Galaxy) | 1.04947° | near-field match | 45 | hold |
| watch | [AT2026akix](https://www.wis-tns.org/object/2026akix) | transient_candidate | 20 | 23.81 | IC2000 (Galaxy) | 1.42748° | near-field match | 45 | hold |
| watch | [AT2026akjp](https://www.wis-tns.org/object/2026akjp) | transient_candidate | 18 | 19.82 | Caldwell 3 (C3) (Galaxy) | 1.24289° | near-field match | 45 | hold |
| watch | [AT2026akjs](https://www.wis-tns.org/object/2026akjs) | transient_candidate | 18 | 22.16 | NGC488 (Galaxy) | 1.50636° | near-field match | 45 | hold |
| watch | [AT2026akke](https://www.wis-tns.org/object/2026akke) | transient_candidate | 20 | 20.8 | NGC3310 (Galaxy) | 1.50843° | near-field match | 45 | hold |
| watch | [AT2026akkh](https://www.wis-tns.org/object/2026akkh) | transient_candidate | 17 | 21.56 | NGC2841 (Galaxy) | 1.69532° | near-field match | 45 | hold |
| watch | [AT2026akkm](https://www.wis-tns.org/object/2026akkm) | transient_candidate | 15 | 21.22 | NGC3198 (Galaxy) | 1.12242° | near-field match | 45 | hold |
| watch | [AT2026akkq](https://www.wis-tns.org/object/2026akkq) | transient_candidate | 14 | 21.92 | NGC 2782 (Galaxy) | 1.48763° | near-field match | 45 | hold |
| watch | [AT2026akks](https://www.wis-tns.org/object/2026akks) | transient_candidate | 12 | 20.65 | NGC3319 (Galaxy) | 1.31211° | near-field match | 45 | hold |
| watch | [AT2026akkx](https://www.wis-tns.org/object/2026akkx) | transient_candidate | 12 | 21.4 | NGC3319 (Galaxy) | 1.95134° | near-field match | 45 | hold |
| watch | [AT2026aklk](https://www.wis-tns.org/object/2026aklk) | transient_candidate | 8 | 20.13 | IC 5374 (Galaxy) | 1.18839° | near-field match | 45 | hold |
| watch | [AT2026akmd](https://www.wis-tns.org/object/2026akmd) | transient_candidate | 16 | 21.03 | IC2389 (Galaxy) | 1.32298° | near-field match | 45 | hold |
| watch | [AT2026akni](https://www.wis-tns.org/object/2026akni) | transient_candidate | 27 | 23.18 | IC2035 (Galaxy) | 1.74091° | near-field match | 45 | hold |
| watch | [AT2026aknn](https://www.wis-tns.org/object/2026aknn) | transient_candidate | 8 | 21.42 | IC 632 (Galaxy) | 1.46175° | near-field match | 45 | hold |
| watch | [AT2026akon](https://www.wis-tns.org/object/2026akon) | transient_candidate | 16 | 22.49 | IC 673 (Galaxy) | 1.79903° | near-field match | 45 | hold |
| watch | [AT2026akoo](https://www.wis-tns.org/object/2026akoo) | transient_candidate | 14 | 21.27 | IC651 (Galaxy) | 1.90084° | near-field match | 45 | hold |
| watch | [AT2026akoz](https://www.wis-tns.org/object/2026akoz) | transient_candidate | 30 | 19.99 | NGC2681 (Galaxy) | 1.83591° | near-field match | 45 | hold |
| watch | [AT2026akpa](https://www.wis-tns.org/object/2026akpa) | transient_candidate | 12 | 21.85 | NGC3726 (Galaxy) | 1.65954° | near-field match | 45 | hold |
| watch | [AT2026akqn](https://www.wis-tns.org/object/2026akqn) | transient_candidate | 8 | 20.15 | NGC 157 (Galaxy) | 1.29573° | near-field match | 45 | hold |
| watch | [AT2026akqq](https://www.wis-tns.org/object/2026akqq) | transient_candidate | 15 | 20.51 | Messier 81 (Galaxy) | 1.34772° | near-field match | 45 | hold |
| watch | [AT2026akra](https://www.wis-tns.org/object/2026akra) | transient_candidate | 8 | 21.55 | NGC3521 (Galaxy) | 1.47772° | near-field match | 45 | hold |
| watch | [AT2026akrg](https://www.wis-tns.org/object/2026akrg) | transient_candidate | 22 | 21.7 | NGC 2207 / IC 2163 (Galaxy) | 1.03625° | near-field match | 45 | hold |
| watch | [AT2026akrm](https://www.wis-tns.org/object/2026akrm) | transient_candidate | 12 | 20.79 | NGC3310 (Galaxy) | 1.52759° | near-field match | 45 | hold |
| watch | [AT2026akrx](https://www.wis-tns.org/object/2026akrx) | transient_candidate | 27 | 22.79 | IC2035 (Galaxy) | 1.42035° | near-field match | 45 | hold |
| watch | [AT2026aksk](https://www.wis-tns.org/object/2026aksk) | transient_candidate | 8 | 20.2 | IC512 (Galaxy) | 1.08444° | near-field match | 45 | hold |
| watch | [SN2026aggp](https://www.wis-tns.org/object/2026aggp) | SN Ia | 36 | 17.63 | IC532 (Nebula) | 1.14385° | near-field match | 43 | hold |
| watch | [AT2026akoh](https://www.wis-tns.org/object/2026akoh) | transient_candidate | 4 | 19.74 | IC5248 (Nebula) | 1.15574° | near-field match | 43 | hold |
| watch | [AT2026akrz](https://www.wis-tns.org/object/2026akrz) | transient_candidate | 4 | 19.65 | IC1547 (Nebula) | 1.08700° | near-field match | 43 | hold |
| watch | [AT2026aksx](https://www.wis-tns.org/object/2026aksx) | transient_candidate | 7 | 22.18 | NGC3387 (Nebula) | 1.06791° | near-field match | 43 | hold |
| watch | [AT2026akug](https://www.wis-tns.org/object/2026akug) | transient_candidate | 2 | 27.37 | Robin's Egg Nebula (Planetary nebula) | 1.90789° | near-field match | 43 | hold |
| watch | [AT2026akie](https://www.wis-tns.org/object/2026akie) | transient_candidate | 14 | 21.89 | NGC3229 (Nebula) | 0.80143° | near-field match | 42 | hold |
| watch | [AT2026akiy](https://www.wis-tns.org/object/2026akiy) | transient_candidate | 27 | 23.45 | NGC7453 (Nebula) | 0.48687° | near-field match | 42 | hold |
| watch | [AT2026akkb](https://www.wis-tns.org/object/2026akkb) | transient_candidate | 20 | 21.01 | Gemini nebula (Planetary nebula) | 0.94983° | near-field match | 42 | hold |
| watch | [AT2026akkc](https://www.wis-tns.org/object/2026akkc) | transient_candidate | 20 | 21.65 | Gemini nebula (Planetary nebula) | 0.26232° | near-field match | 42 | hold |
| watch | [AT2026akls](https://www.wis-tns.org/object/2026akls) | transient_candidate | 23 | 20.82 | Collinder 444 (CR444) (Open cluster) | 0.80752° | near-field match | 42 | hold |
| watch | [AT2026aklx](https://www.wis-tns.org/object/2026aklx) | transient_candidate | 17 | 20.47 | Caldwell 1 (C1) (Open cluster) | 0.94306° | near-field match | 42 | hold |
| watch | [AT2026akmh](https://www.wis-tns.org/object/2026akmh) | transient_candidate | 8 | 20.83 | IC 489 (Star) | 0.60193° | near-field match | 42 | hold |
| watch | [AT2026akmt](https://www.wis-tns.org/object/2026akmt) | transient_candidate | 8 | 20.26 | Collinder 179 (CR179) (Open cluster) | 0.40651° | near-field match | 42 | hold |
| watch | [AT2026akng](https://www.wis-tns.org/object/2026akng) | transient_candidate | 8 | 20.51 | NGC2875 (Nebula) | 0.31508° | near-field match | 42 | hold |
| watch | [AT2026akrn](https://www.wis-tns.org/object/2026akrn) | transient_candidate | 14 | 21.32 | IC2278 (Nebula) | 0.69641° | near-field match | 42 | hold |
| watch | [AT2026aksa](https://www.wis-tns.org/object/2026aksa) | transient_candidate | 4 | 19.75 | Alpha Persei Cluster (Open cluster) | 0.60304° | near-field match | 42 | hold |
| watch | [AT2026akss](https://www.wis-tns.org/object/2026akss) | transient_candidate | 14 | 22.26 | NGC3229 (Nebula) | 0.92286° | near-field match | 42 | hold |
| watch | [AT2026aktf](https://www.wis-tns.org/object/2026aktf) | transient_candidate | 21 | 21.36 | NGC737 (Nebula) | 0.32108° | near-field match | 42 | hold |
| watch | [AT2026agvn](https://www.wis-tns.org/object/2026agvn) | transient_candidate | 32 | 18.12 | NGC3486 (Galaxy) | 1.16840° | near-field match | 38 | hold |
| watch | [AT2026aijr](https://www.wis-tns.org/object/2026aijr) | transient_candidate | 22 | 20.08 | NGC7447 (Nebula) | 1.89138° | near-field match | 35 | hold |
| watch | [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) | transient_candidate | 20 | 20.91 | Intergalactic Wanderer (Globular cluster) | 1.09787° | near-field match | 35 | hold |
| watch | [AT2026akcq](https://www.wis-tns.org/object/2026akcq) | transient_candidate | 11 | 19.76 | IC2189 (Nebula) | 1.26362° | near-field match | 35 | hold |
| watch | [AT2026akhj](https://www.wis-tns.org/object/2026akhj) | transient_candidate | 9 | 19.63 | IC2328 (Nebula) | 1.00650° | near-field match | 35 | hold |
| watch | [AT2026akhw](https://www.wis-tns.org/object/2026akhw) | transient_candidate | 14 | 21.25 | NGC3229 (Nebula) | 1.62985° | near-field match | 35 | hold |
| watch | [AT2026akil](https://www.wis-tns.org/object/2026akil) | transient_candidate | 20 | 21.05 | NGC3097 (Nebula) | 1.78512° | near-field match | 35 | hold |
| watch | [AT2026akio](https://www.wis-tns.org/object/2026akio) | transient_candidate | 15 | 21.46 | Collinder 113 (CR113) (Open cluster) | 1.46002° | near-field match | 35 | hold |
| watch | [AT2026akjm](https://www.wis-tns.org/object/2026akjm) | transient_candidate | 17 | 20.64 | IC240 (Nebula) | 1.07528° | near-field match | 35 | hold |
| watch | [AT2026akkg](https://www.wis-tns.org/object/2026akkg) | transient_candidate | 17 | 21.86 | Gemini nebula (Planetary nebula) | 1.07214° | near-field match | 35 | hold |
| watch | [AT2026akkl](https://www.wis-tns.org/object/2026akkl) | transient_candidate | 15 | 21.16 | Eskimo or Clown Nebula (Planetary nebula) | 1.67199° | near-field match | 35 | hold |
| watch | [AT2026akkp](https://www.wis-tns.org/object/2026akkp) | transient_candidate | 14 | 21.28 | NGC2901 (Nebula) | 1.15866° | near-field match | 35 | hold |
| watch | [AT2026akkt](https://www.wis-tns.org/object/2026akkt) | transient_candidate | 12 | 20.11 | NGC3180 (HII) | 1.53716° | near-field match | 35 | hold |
| watch | [AT2026akkv](https://www.wis-tns.org/object/2026akkv) | transient_candidate | 12 | 20.93 | IC2610 (Nebula) | 1.26969° | near-field match | 35 | hold |
| watch | [AT2026aknk](https://www.wis-tns.org/object/2026aknk) | transient_candidate | 4 | 19.86 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.37344° | near-field match | 35 | hold |
| watch | [AT2026aknl](https://www.wis-tns.org/object/2026aknl) | transient_candidate | 23 | 20.39 | Messier 15 (M15) (Globular cluster) | 1.65930° | near-field match | 35 | hold |
| watch | [AT2026aknm](https://www.wis-tns.org/object/2026aknm) | transient_candidate | 15 | 23.05 | IC5248 (Nebula) | 1.68883° | near-field match | 35 | hold |
| watch | [AT2026aknp](https://www.wis-tns.org/object/2026aknp) | transient_candidate | 12 | 21.21 | NGC370 (Nebula) | 1.60098° | near-field match | 35 | hold |
| watch | [AT2026akog](https://www.wis-tns.org/object/2026akog) | transient_candidate | 17 | 23.18 | Robin's Egg Nebula (Planetary nebula) | 1.58533° | near-field match | 35 | hold |
| watch | [AT2026akom](https://www.wis-tns.org/object/2026akom) | transient_candidate | 16 | 22.33 | NGC3387 (Nebula) | 1.99594° | near-field match | 35 | hold |
| watch | [AT2026akph](https://www.wis-tns.org/object/2026akph) | transient_candidate | 15 | 21.04 | NGC2386 (Nebula) | 1.92748° | near-field match | 35 | hold |
| watch | [AT2026akpk](https://www.wis-tns.org/object/2026akpk) | transient_candidate | 12 | 21.74 | NGC2464 (Nebula) | 1.87997° | near-field match | 35 | hold |
| watch | [AT2026akpo](https://www.wis-tns.org/object/2026akpo) | transient_candidate | 9 | 20.77 | IC2170 (Nebula) | 1.35210° | near-field match | 35 | hold |
| watch | [AT2026akqs](https://www.wis-tns.org/object/2026akqs) | transient_candidate | 16 | 20.41 | IC5251 (Nebula) | 1.67892° | near-field match | 35 | hold |
| watch | [AT2026akrh](https://www.wis-tns.org/object/2026akrh) | transient_candidate | 20 | 21.05 | NGC3097 (Nebula) | 1.61855° | near-field match | 35 | hold |
| watch | [AT2026akrl](https://www.wis-tns.org/object/2026akrl) | transient_candidate | 15 | 21.54 | Collinder 154 (CR154) (Open cluster) | 1.12325° | near-field match | 35 | hold |
| watch | [AT2026akro](https://www.wis-tns.org/object/2026akro) | transient_candidate | 14 | 22.27 | IC 2237 (Star) | 1.50919° | near-field match | 35 | hold |
| watch | [AT2026aksv](https://www.wis-tns.org/object/2026aksv) | transient_candidate | 8 | 20.51 | NGC3708 (Nebula) | 1.64139° | near-field match | 35 | hold |
| watch | [AT2026aktb](https://www.wis-tns.org/object/2026aktb) | transient_candidate | 3 | 21.39 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.25733° | near-field match | 35 | hold |
| watch | [AT2026aktm](https://www.wis-tns.org/object/2026aktm) | transient_candidate | 9 | 21.38 | Collinder 113 (CR113) (Open cluster) | 1.01419° | near-field match | 35 | hold |
| watch | [AT2026akty](https://www.wis-tns.org/object/2026akty) | transient_candidate | 8 | 19.79 | Collinder 144 (CR144) (Open cluster) | 1.33609° | near-field match | 35 | hold |
| watch | [AT2026akcp](https://www.wis-tns.org/object/2026akcp) | transient_candidate | 9 | 20.01 | Lynds Bright Nebula 980 (LBN980) (HII) | 0.73350° | near-field match | 34 | hold |
| watch | [SN2026agyr](https://www.wis-tns.org/object/2026agyr) | SN II | 31 | 18.99 | IC5061 (Nebula) | 1.57959° | near-field match | 33 | hold |
| watch | [SN2026adfc](https://www.wis-tns.org/object/2026adfc) | SN Ia | 58 | 18.97 | Lynds Bright Nebula 429 (LBN429) (HII) | 0.65958° | near-field match | 32 | hold |
| watch | [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) | transient_candidate | 14 | 19.74 | Lynds Bright Nebula 856 (LBN856) (HII) | 1.86938° | near-field match | 27 | hold |
| watch | [AT2026akjb](https://www.wis-tns.org/object/2026akjb) | transient_candidate | 8 | 21.26 | Lynds Bright Nebula 896 (LBN896) (HII) | 1.22063° | near-field match | 27 | hold |
| watch | [AT2026akme](https://www.wis-tns.org/object/2026akme) | transient_candidate | 15 | 20.72 | Lynds Bright Nebula 693 (LBN693) (HII) | 1.56718° | near-field match | 27 | hold |
| watch | [AT2026akrp](https://www.wis-tns.org/object/2026akrp) | transient_candidate | 8 | 20.93 | Lynds Bright Nebula 418 (LBN418) (HII) | 1.28863° | near-field match | 27 | hold |
| watch | [SN2026ahxw](https://www.wis-tns.org/object/2026ahxw) | SN Ia | 37 | 20.84 | Collinder 154 (CR154) (Open cluster) | 0.75676° | near-field match | 20 | hold |
| watch | [SN2026aedz](https://www.wis-tns.org/object/2026aedz) | SN IIn | 54 | 19.78 | NGC1480 (Nebula) | 1.10868° | near-field match | 13 | hold |
| watch | [SN2026agok](https://www.wis-tns.org/object/2026agok) | SN Ia | 40 | 19.99 | Beehive cluster (Open cluster) | 1.64277° | near-field match | 13 | hold |
| watch | [AT2026aepc](https://www.wis-tns.org/object/2026aepc) | transient_candidate | 52 | 19.7 | NGC3319 (Galaxy) | 1.76492° | near-field match | 8 | hold |
| watch | [AT2026akoy](https://www.wis-tns.org/object/2026akoy) | transient_candidate | 35 | 21.27 | NGC2279 (Nebula) | 0.28704° | near-field match | 5 | hold |
| watch | [AT2026akjx](https://www.wis-tns.org/object/2026akjx) | transient_candidate | 36 | 21.13 | IC132 (HII) | 1.66808° | near-field match | 0 | hold |
| watch | [AT2026aktc](https://www.wis-tns.org/object/2026aktc) | transient_candidate | 45 | 21.16 | NGC2284 (Nebula) | 1.82461° | near-field match | 0 | hold |

## Candidate dossiers

### 1. [SN2026akhh](https://www.wis-tns.org/object/2026akhh) near IC2013

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2013 as this object's host. The 0.18157° (10.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0583 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T11:05:21Z · 9 days · 18.34 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4716....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4716....1T/abstract) |
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
| Separation | 0.18157° · 10.89′ |
| Catalog description | considerably bright, considerably large, much / magnitude extended 170deg , considerably brighter middle, or in the middle, suspected |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.9936895%20-17.0988243&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [SN2026aknq](https://www.wis-tns.org/object/2026aknq) near NGC1367

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1367 as this object's host. The 0.76736° (46.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.0216 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-23T09:24:52Z · 3 days · 17.99 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4754....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4754....1T/abstract) |
| Classification references | [2026TNSCR4784....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4784....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1367** · `NGC1367` |
| Catalog display name | NGC1367 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.7 · 4.88′ × 3.26′ |
| Distance | 24,200 kpc |
| Separation | 0.76736° · 46.04′ |
| Catalog description | NGC 1367 or NGC 1371 is a spiral galaxy in the constellation Fornax. The galaxy lies about 75 million light years away from Earth, which means, given its apparent dimensions, that NGC 1367 is approximately 130,000 light years across. It was discovered by William Herschel on November 17, 1784, and independently by Ormond Stone in 1886. It is a member of the Eridanus Cluster. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.911837%20-25.009219&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026aizp](https://www.wis-tns.org/object/2026aizp) near Atoms For Peace Galaxy

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 97/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Atoms For Peace Galaxy as this object's host. The 0.49883° (29.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.036 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T08:20:41Z · 17 days · 18.1 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4550....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4550....1T/abstract) |
| Classification references | [2026TNSCR4607....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4607....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Atoms For Peace Galaxy** · `NGC7252` |
| Catalog display name | Atoms For Peace Galaxy |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 11.4 · 1.85′ × 1.71′ |
| Distance | — |
| Separation | 0.49883° · 29.93′ |
| Catalog description | NGC 7252 is a peculiar galaxy resulting from an interaction between two galaxies that started a billion years ago. It is located 220 million light years away in the constellation Aquarius. It is also called Atoms for Peace Galaxy, a nickname which comes from its loop-like structure, made of stars, that resembles a classic diagram of an electron orbiting an atomic nucleus. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.9409829%20-25.1260593&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026ajxw](https://www.wis-tns.org/object/2026ajxw) near IC750

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC750 as this object's host. The 0.12312° (7.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T15:10:28Z · 11 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4659....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4659....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC750** · `IC750` |
| Catalog display name | IC750 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.8 · 2.11′ × 1.02′ |
| Distance | 21,600 kpc |
| Separation | 0.12312° · 7.39′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, large, little (adv.); long (adj.) extended 35deg , brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=179.6954478%2042.6003439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026aktu](https://www.wis-tns.org/object/2026aktu) near NGC5054

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC5054 as this object's host. The 1.78838° (107.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T13:26:49Z · 2 days · 15.64 r |
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
| Subject | **NGC5054** · `NGC5054` |
| Catalog display name | NGC5054 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 10.8 · 5.04′ × 2.9′ |
| Distance | — |
| Separation | 1.78838° · 107.30′ |
| Catalog description | NGC 5054 is a spiral galaxy in the constellation Virgo. The galaxy lies about 55 million light years away from Earth based on redshift-independent methods, which means, given its apparent dimensions, that NGC 5054 is approximately 85,000 light years across. Based on redshift the galaxy lies about 80 million light years away. It was discovered by William Herschel on December 31, 1785. It is included in the Herschel 400 Catalogue. It lies about 6 degrees southwest of Spica and near the star 53 Virginis. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=200.1661158%20-18.0330698&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 6. [AT2026aktv](https://www.wis-tns.org/object/2026aktv) near IC4221

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4221 as this object's host. The 0.97309° (58.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T13:26:49Z · 2 days · 17.6 r |
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
| Subject | **IC4221** · `IC4221` |
| Catalog display name | IC4221 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 13.6 · 1.54′ × 0.71′ |
| Distance | — |
| Separation | 0.97309° · 58.39′ |
| Catalog description | considerably faint, small in angular size, much / magnitude extended 165deg , considerably brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=198.6450546%20-14.8293743&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 7. [AT2026akhc](https://www.wis-tns.org/object/2026akhc) near IC 4168

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 83/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4168 as this object's host. The 1.48969° (89.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T15:05:42Z · 7 days · 18.43 cyan |
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
| Subject | **IC 4168** · `IC 4168` |
| Catalog display name | NGC 4930 |
| Type / constellation | Galaxy · CVn |
| Catalog magnitude / angular size | — · 0.65′ × 0.5′ |
| Distance | 78.4 ly |
| Separation | 1.48969° · 89.38′ |
| Catalog description | NGC 4930 is a barred spiral galaxy in the constellation Centaurus. The galaxy lies about 80 million light years away from Earth, which means, given its apparent dimensions, that NGC 4930 is approximately 80,000 light years across. It was discovered by John Herschel on June 8, 1834. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4168 has the different designation NGC 4930 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=198.183605%2040.4236725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 8. [AT2026akoc](https://www.wis-tns.org/object/2026akoc) near NGC5377

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC5377 as this object's host. The 1.96450° (117.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-23T15:09:57Z · 3 days · 16.69 orange |
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
| Subject | **NGC5377** · `NGC5377` |
| Catalog display name | NGC5377 |
| Type / constellation | Galaxy · Canes Venatici |
| Catalog magnitude / angular size | 11.3 · 3.64′ × 1.42′ |
| Distance | 26,200 kpc |
| Separation | 1.96450° · 117.87′ |
| Catalog description | NGC 5377 is an intermediate barred spiral galaxy located in the constellation Canes Venatici. Its speed relative to the cosmic microwave background is 1,951 ± 11 km/s, which corresponds to a Hubble distance of 28.8 ± 2.0 Mpc. NGC 5377 was discovered by German-British astronomer William Herschel in 1787. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akoc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=206.308654%2047.863817&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 9. [AT2026akok](https://www.wis-tns.org/object/2026akok) near IC 1288

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 83/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1288 as this object's host. The 1.34317° (80.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T04:45:03Z · 2 days · 18.38 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4766....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4766....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1288** · `IC 1288` |
| Catalog display name | NGC 1512 |
| Type / constellation | Galaxy · Lyr |
| Catalog magnitude / angular size | — · 1.09′ × 0.61′ |
| Distance | — |
| Separation | 1.34317° · 80.59′ |
| Catalog description | NGC 1512 is a barred spiral galaxy approximately 38 million light-years away from Earth in the constellation Horologium. It was discovered by Scottish astronomer James Dunlop on 29 October 1826. NGC 1512 is a barred spiral galaxy approximately 38 million light-years away from Earth in the constellation Horologium. It was discovered by Scottish astronomer James Dunlop on 29 October 1826. The galaxy displays a double ring structure, with a (nuclear) ring around the galactic nucleus and an (inner) further out in the main disk. The galaxy hosts an extended UV disc with at least 200 clusters with recent star formation activity. NGC 1512 is a member of the Dorado Group. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1288 has the different designation NGC 1512 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akok) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=276.9113566%2041.0155402&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 10. [AT2026akqe](https://www.wis-tns.org/object/2026akqe) near IC947

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC947 as this object's host. The 1.43560° (86.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T13:26:09Z · 2 days · 17.34 r |
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
| Subject | **IC947** · `IC947` |
| Catalog display name | IC947 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 13.8 · 1.67′ × 1.09′ |
| Distance | 39,350 kpc |
| Separation | 1.43560° · 86.14′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, very small in angular size, round, suddenly (abruptly) / south brighter middle, or in the middle nucleus, or to a nucleus = 12m |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=209.1055332%20-0.249334&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 11. [AT2026akqu](https://www.wis-tns.org/object/2026akqu) near Caldwell 105 (C105)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 105 (C105) as this object's host. The 1.90156° (114.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T23:58:20Z · 2 days · 15.4 Other |
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
| Subject | **Caldwell 105 (C105)** · `C105` |
| Catalog display name | Caldwell 105 (C105) |
| Type / constellation | Globular cluster · Musca |
| Catalog magnitude / angular size | 7.3 · 14′ × 14′ |
| Distance | 6.5 kpc |
| Separation | 1.90156° · 114.09′ |
| Catalog description | NGC 4833 is a globular cluster discovered by Abbe Lacaille during his 1751-1752 journey to South Africa, and catalogued in 1755. It was subsequently observed and catalogued by James Dunlop and Sir John Herschel whose instruments could resolve it into individual stars. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=199.209625%20-72.197028&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 12. [AT2026aksh](https://www.wis-tns.org/object/2026aksh) near IC2104

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2104 as this object's host. The 1.67721° (100.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T00:27:49Z · 0 days · 17.98 wide |
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
| Subject | **IC2104** · `IC2104` |
| Catalog display name | IC2104 |
| Type / constellation | Galaxy · Lepus |
| Catalog magnitude / angular size | 13.8 · 2.11′ × 1.14′ |
| Distance | 80,000 kpc |
| Separation | 1.67721° · 100.63′ |
| Catalog description | faint, extended, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.7990583%20-16.051735&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 13. [AT2026ahzh](https://www.wis-tns.org/object/2026ahzh) near NGC3665

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 82/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3665 as this object's host. The 0.91144° (54.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T14:39:22Z · 23 days · 18.28 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4409....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4409....1T/abstract) |
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
| Separation | 0.91144° · 54.69′ |
| Catalog description | NGC 3665 is a lenticular galaxy located in the constellation Ursa Major. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that NGC 3665 is about 85,000 light years across. It was discovered by William Herschel on March 23, 1789. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=171.4856415%2039.6428171&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 14. [AT2026akod](https://www.wis-tns.org/object/2026akod) near Collinder 166 (CR166)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 166 (CR166) as this object's host. The 0.68541° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T03:30:25Z · 4 days · 18.26 wide |
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
| Subject | **Collinder 166 (CR166)** · `CR166` |
| Catalog display name | Collinder 166 (CR166) |
| Type / constellation | Open cluster · Puppis |
| Catalog magnitude / angular size | 7.3 · 6.6′ × 6.6′ |
| Distance | 1.343 kpc |
| Separation | 0.68541° · 41.12′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akod) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.5395688%20-24.1870062&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 15. [AT2026akof](https://www.wis-tns.org/object/2026akof) near NGC1890

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1890 as this object's host. The 0.42602° (25.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T05:50:21Z · 4 days · 17.9 orange |
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
| Subject | **NGC1890** · `NGC1890` |
| Catalog display name | NGC1890 |
| Type / constellation | Open cluster · Mensa |
| Catalog magnitude / angular size | 12.8 · 1.1′ × 1′ |
| Distance | — |
| Separation | 0.42602° · 25.56′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akof) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=78.1297482%20-72.49358&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 16. [AT2026akhs](https://www.wis-tns.org/object/2026akhs) near NGC6958

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC6958 as this object's host. The 1.67482° (100.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T18:21:53Z · 8 days · 18.03 orange |
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
| Subject | **NGC6958** · `NGC6958` |
| Catalog display name | NGC6958 |
| Type / constellation | Galaxy · Microscopium |
| Catalog magnitude / angular size | 11.4 · 2.44′ × 1.88′ |
| Distance | 35,400 kpc |
| Separation | 1.67482° · 100.49′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=314.2312711%20-38.4392844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 17. [AT2026aklg](https://www.wis-tns.org/object/2026aklg) near NGC5204

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC5204 as this object's host. The 1.43417° (86.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:51:54Z · 15 days · 17.75 g |
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
| Subject | **NGC5204** · `NGC5204` |
| Catalog display name | NGC5204 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.3 · 4.5′ × 2.82′ |
| Distance | — |
| Separation | 1.43417° · 86.05′ |
| Catalog description | NCG 5204 is a Magellanic spiral galaxy located about 14.5 million light-years away from Earth in the constellation of Ursa Major and is a member of the M101 Group of galaxies. It has a galaxy morphological classification of SA(s)m and is highly irregular, with only the barest indication of any spiral arm structure. The galaxy's most prominent feature is an extremely powerful X-ray source designated NGC 5204 X-1. This has resulted in the galaxy being the target of several studies due to the strength of the source and its relative proximity to Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=202.8133991%2057.0016488&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 18. [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) near IC765

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC765 as this object's host. The 0.75219° (45.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:56:47Z · 12 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4645....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4645....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC765** · `IC765` |
| Catalog display name | IC765 |
| Type / constellation | Nebula · Coma Berenices |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.75219° · 45.13′ |
| Catalog description | very faint, suspected 6'north of 4152 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.4079476%2016.1252125&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 19. [SN2026akbo](https://www.wis-tns.org/object/2026akbo) near NGC3344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3344 as this object's host. The 0.96185° (57.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0173 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T06:06:39Z · 9 days · 18.76 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4673....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4673....1R/abstract) |
| Classification references | [2026TNSCR4697....1P](https://ui.adsabs.harvard.edu/abs/2026TNSCR4697....1P/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3344** · `NGC3344` |
| Catalog display name | NGC3344 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10 · 6.7′ × 6.37′ |
| Distance | — |
| Separation | 0.96185° · 57.71′ |
| Catalog description | NGC 3344 is a relatively isolated barred spiral galaxy around half the size of the Milky Way located 22.5 million light years away in the constellation Leo Minor. It was discovered by German-British astronomer William Herschel on 6 April 1785. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.9121587%2025.3204541&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 20. [AT2026aklo](https://www.wis-tns.org/object/2026aklo) near IC391

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC391 as this object's host. The 0.49605° (29.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T12:06:30Z · 5 days · 19.28 r |
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
| Subject | **IC391** · `IC391` |
| Catalog display name | IC391 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 12.7 · 1.39′ × 1.33′ |
| Distance | — |
| Separation | 0.49605° · 29.76′ |
| Catalog description | faint, small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.9076694%2078.5710324&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 21. [AT2026akmw](https://www.wis-tns.org/object/2026akmw) near NGC7741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7741 as this object's host. The 0.42553° (25.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T19:50:55Z · 4 days · 18.65 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4742....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4742....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7741** · `NGC7741` |
| Catalog display name | NGC7741 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 11.3 · 3.63′ × 2.38′ |
| Distance | — |
| Separation | 0.42553° · 25.53′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=356.0802108%2025.761938&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 22. [AT2026akpx](https://www.wis-tns.org/object/2026akpx) near NGC4208

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4208 as this object's host. The 0.33686° (20.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T13:11:55Z · 4 days · 19.36 r |
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
| Subject | **NGC4208** · `NGC4208` |
| Catalog display name | NGC4208 |
| Type / constellation | Galaxy · Coma Berenices |
| Catalog magnitude / angular size | 11.1 · 2.8′ × 1.69′ |
| Distance | 17,050 kpc |
| Separation | 0.33686° · 20.21′ |
| Catalog description | NGC 4212 is a flocculent spiral galaxy with LINER activity located about 53 million light-years away in the constellation Coma Berenices. The galaxy was discovered by astronomer William Herschel on April 8, 1784, and was listed in the NGC catalog as NGC 4208. He then observed the same galaxy and listed it as NGC 4212. Astronomer John Louis Emil Dreyer later concluded that NGC 4208 was identical to NGC 4212. NGC 4212 is a member of the Virgo Cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.7681365%2013.5952094&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 23. [AT2026akqm](https://www.wis-tns.org/object/2026akqm) near IC 3591

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3591 as this object's host. The 0.91545° (54.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T13:14:29Z · 2 days · 19.02 r |
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
| Subject | **IC 3591** · `IC 3591` |
| Catalog display name | NGC 945 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 0.79′ × 0.49′ |
| Distance | — |
| Separation | 0.91545° · 54.93′ |
| Catalog description | NGC 945 is a barred spiral galaxy in the constellation Cetus, located south of the celestial equator. It is estimated to be 200 million light-years from the Milky Way, and about 135,000 light-years in diameter. The object was discovered by astronomer William Herschel on November 28, 1785. It is near NGC 948, with which it forms a gravitationally bound pair of galaxies. In the same area of the sky there are the galaxies NGC 942, NGC 943, NGC 950, and IC 230. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3591 has the different designation NGC 945 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=190.1848411%206.9246545&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 24. [AT2026akqr](https://www.wis-tns.org/object/2026akqr) near IC209

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC209 as this object's host. The 0.27005° (16.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T04:05:25Z · 4 days · 19.39 g |
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
| Subject | **IC209** · `IC209` |
| Catalog display name | IC209 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.8 · 1.51′ × 1.03′ |
| Distance | 62,700 kpc |
| Separation | 0.27005° · 16.20′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, small in angular size, diffused |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.081476%20-6.7923506&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 25. [AT2026akru](https://www.wis-tns.org/object/2026akru) near NGC3953

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3953 as this object's host. The 0.41812° (25.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-25T14:11:30Z · 1 days · 18.8 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4774....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4774....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3953** · `NGC3953` |
| Catalog display name | NGC3953 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.1 · 6.14′ × 3.13′ |
| Distance | — |
| Separation | 0.41812° · 25.09′ |
| Catalog description | NGC 3953 is a barred spiral galaxy located in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1,236±13 km/s, which corresponds to a Hubble distance of 59.4 ± 4.2 Mly (18.22 ± 1.29 Mpc). However, 33 non-redshift measurements give a closer mean distance of 54.10 ± 1.93 Mly (16.588 ± 0.592 Mpc). It was discovered by Pierre Méchain on 12 March 1781. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=178.0500584%2052.6666896&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 26. [SN2026akhl](https://www.wis-tns.org/object/2026akhl) near NGC2886

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 78/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2886 as this object's host. The 1.56605° (93.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0403 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T14:05:33Z · 7 days · 18.85 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4716....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4716....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2886** · `NGC2886` |
| Catalog display name | NGC2886 |
| Type / constellation | Nebula · Hydra |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.56605° · 93.96′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.2788886%20-20.2123571&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 27. [AT2026akgx](https://www.wis-tns.org/object/2026akgx) near NGC1569

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1569 as this object's host. The 1.05967° (63.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T22:19:06Z · 7 days · 19.28 L |
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
| Subject | **NGC1569** · `NGC1569` |
| Catalog display name | NGC1569 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 11 · 3.91′ × 2.16′ |
| Distance | — |
| Separation | 1.05967° · 63.58′ |
| Catalog description | NGC 1569 is a dwarf irregular galaxy in Camelopardalis. The galaxy is relatively nearby and consequently, the Hubble Space Telescope can easily resolve the stars within the galaxy. The distance to the galaxy was previously believed to be only 2.4 Mpc. However, in 2008 scientists studying images from Hubble calculated the galaxy's distance at nearly 11 million light-years away, about 4 million light-years farther than previously thought, meaning it is a member of the IC 342 group of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=69.104574%2063.977763&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 28. [AT2026akhf](https://www.wis-tns.org/object/2026akhf) near NGC3726

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3726 as this object's host. The 1.78481° (107.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T14:18:10Z · 7 days · 19.45 cyan |
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
| Subject | **NGC3726** · `NGC3726` |
| Catalog display name | NGC3726 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.5 · 5.27′ × 3.54′ |
| Distance | — |
| Separation | 1.78481° · 107.09′ |
| Catalog description | NGC 3726 is a barred spiral galaxy located in the constellation Ursa Major. It is located at a distance of circa 45 million light years from Earth, which, given its apparent dimensions, means that NGC 3726 is about 85,000 light years across. It was discovered by German-British astronomer William Herschel on February 5, 1788. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.722892%2046.956158&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [AT2026akmg](https://www.wis-tns.org/object/2026akmg) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.94196° (116.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T04:26:03Z · 5 days · 18.66 wide |
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
| Subject | **NGC797** · `IC 700 NED01` |
| Catalog display name | NGC797 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 0.2′ × 0.13′ |
| Distance | — |
| Separation | 1.94196° · 116.52′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=173.2845053%2018.8699447&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 30. [AT2026akmz](https://www.wis-tns.org/object/2026akmz) near NGC4546

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4546 as this object's host. The 1.35021° (81.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T06:11:30Z · 4 days · 19.11 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4741....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4741....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC4546** · `NGC4546` |
| Catalog display name | NGC4546 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 10.6 · 3.16′ × 1.76′ |
| Distance | — |
| Separation | 1.35021° · 81.01′ |
| Catalog description | NGC 4546 is a lenticular field galaxy located in the direction of the constellation Virgo, with a total population of globular clusters estimated at 390. It is a member of the Virgo II Groups, a series of galaxies and galaxy clusters strung out from the southern edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=187.6491296%20-3.2134673&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 31. [AT2026akna](https://www.wis-tns.org/object/2026akna) near NGC3887

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3887 as this object's host. The 1.45843° (87.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T06:16:36Z · 4 days · 18.85 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4741....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4741....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3887** · `NGC3887` |
| Catalog display name | NGC3887 |
| Type / constellation | Galaxy · Crater |
| Catalog magnitude / angular size | 10.9 · 3.27′ × 2.57′ |
| Distance | 18,200 kpc |
| Separation | 1.45843° · 87.51′ |
| Catalog description | NGC 3887 is a barred spiral galaxy in the constellation Crater. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 3887 is approximately 60,000 light years across. It was discovered by William Herschel on December 31, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akna) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=176.4385479%20-15.4306451&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 32. [AT2026akqa](https://www.wis-tns.org/object/2026akqa) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.11429° (66.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T02:11:56Z · 2 days · 19.37 r |
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
| Subject | **NGC 3561** · `IC 1433 NED02` |
| Catalog display name | NGC 3561 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.18′ × 0.15′ |
| Distance | — |
| Separation | 1.11429° · 66.86′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.036833%20-13.3138147&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 33. [AT2026akqi](https://www.wis-tns.org/object/2026akqi) near IC 1863

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1863 as this object's host. The 1.79631° (107.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T06:24:04Z · 4 days · 19.49 r |
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
| Subject | **IC 1863** · `IC 1863` |
| Catalog display name | NGC 1278 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.6′ × 0.6′ |
| Distance | — |
| Separation | 1.79631° · 107.78′ |
| Catalog description | NGC 1278 is an elliptical galaxy located about 230 million light-years away in the constellation Perseus. NGC 1278 was discovered by astronomer Heinrich d'Arrest on February 14, 1863. It was then rediscovered by astronomer Guillaume Bigourdan on October 22, 1884, and later listed as IC 1907. NGC 1278 is a member of the Perseus Cluster and is a low-luminosity AGN (LLAGN). |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1863 has the different designation NGC 1278 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=44.8240807%207.3655125&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026akrw](https://www.wis-tns.org/object/2026akrw) near NGC 1954

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 1954 as this object's host. The 1.30231° (78.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-25T00:06:02Z · 1 days · 18.92 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4775....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4775....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 1954** · `IC 5378 NED02` |
| Catalog display name | NGC 1954 |
| Type / constellation | Galaxy · Peg |
| Catalog magnitude / angular size | — · 0.6′ × 0.53′ |
| Distance | — |
| Separation | 1.30231° · 78.14′ |
| Catalog description | NGC 1954 is a large spiral galaxy in the constellation of Lepus. Its velocity with respect to the cosmic microwave background is 3,172 ± 4 km/s, which corresponds to a Hubble distance of 46.8 ± 3.3 Mpc Mpc. It was discovered by German-British astronomer William Herschel on 14 December 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.2998045%2016.585116&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 35. [AT2026akse](https://www.wis-tns.org/object/2026akse) near IC5171

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5171 as this object's host. The 1.90262° (114.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T00:34:56Z · 0 days · 18.56 orange |
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
| Subject | **IC5171** · `IC5171` |
| Catalog display name | IC5171 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 13.5 · 0.74′ × 0.49′ |
| Distance | 32,500 kpc |
| Separation | 1.90262° · 114.16′ |
| Catalog description | The Telescopium−Grus Cloud is a galaxy filament in the constellations of Pavo, Indus, and Telescopium. It was first defined by astronomer Brent Tully in his book The Nearby Galaxies Atlas and its companion book The Nearby Galaxies Catalog. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akse) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.45811%20-45.0408917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 36. [AT2026akts](https://www.wis-tns.org/object/2026akts) near NGC3344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3344 as this object's host. The 1.43147° (85.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T11:09:34Z · 0 days · 19.49 g |
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
| Subject | **NGC3344** · `NGC3344` |
| Catalog display name | NGC3344 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10 · 6.7′ × 6.37′ |
| Distance | — |
| Separation | 1.43147° · 85.89′ |
| Catalog description | NGC 3344 is a relatively isolated barred spiral galaxy around half the size of the Milky Way located 22.5 million light years away in the constellation Leo Minor. It was discovered by German-British astronomer William Herschel on 6 April 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akts) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=162.4322787%2025.1859614&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 37. [AT2026aktt](https://www.wis-tns.org/object/2026aktt) near NGC2986

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2986 as this object's host. The 1.04778° (62.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T12:05:33Z · 0 days · 18.86 r |
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
| Subject | **NGC2986** · `NGC2986` |
| Catalog display name | NGC2986 |
| Type / constellation | Galaxy · Hydra |
| Catalog magnitude / angular size | 10.6 · 4.81′ × 3.85′ |
| Distance | — |
| Separation | 1.04778° · 62.87′ |
| Catalog description | NGC 2986 is an elliptical galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background is 2,637±24 km/s, which corresponds to a Hubble distance of 126.8 ± 9.0 Mly (38.89 ± 2.75 Mpc). Additionally, 18 non-redshift measurements give a distance of 116.31 ± 8.30 Mly (35.661 ± 2.544 Mpc). It was discovered by German-British astronomer William Herschel on 10 March 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=145.3248145%20-20.4922221&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 38. [AT2026aktw](https://www.wis-tns.org/object/2026aktw) near IC 892

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 892 as this object's host. The 1.25329° (75.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T13:21:56Z · 0 days · 19.03 r |
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
| Subject | **IC 892** · `IC 892` |
| Catalog display name | NGC 7300 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 1.6′ × 0.84′ |
| Distance | — |
| Separation | 1.25329° · 75.20′ |
| Catalog description | NGC 7300 is an intermediate spiral galaxy in the constellation of Aquarius. Its velocity with respect to the cosmic microwave background is 4,566±24 km/s, which corresponds to a Hubble distance of 219.7 ± 15.4 Mly (67.35 ± 4.73 Mpc). However, 15 non-redshift measurements give a closer mean distance of 181.89 ± 10.31 Mly (55.767 ± 3.162 Mpc). It was discovered by British astronomer John Herschel on 26 July 1830. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 892 has the different designation NGC 7300 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=204.1611303%20-3.0065495&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 39. [AT2026akhu](https://www.wis-tns.org/object/2026akhu) near NGC2325

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2325 as this object's host. The 0.61029° (36.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T03:25:37Z · 8 days · 19.35 wide |
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
| Subject | **NGC2325** · `NGC2325` |
| Catalog display name | NGC2325 |
| Type / constellation | Galaxy · Canis Major |
| Catalog magnitude / angular size | 11.2 · 3.97′ × 2.31′ |
| Distance | — |
| Separation | 0.61029° · 36.62′ |
| Catalog description | NGC 2325 is a elliptical galaxy in the constellation of Canis Major. Its velocity with respect to the cosmic microwave background is 2,356±25 km/s, which corresponds to a Hubble distance of 113.4 ± 8.1 Mly (34.76 ± 2.48 Mpc). However, 16 non-redshift measurements give a much closer mean distance of 74.53 ± 3.94 Mly (22.850 ± 1.209 Mpc). It was discovered by British astronomer John Herschel on 1 February 1837. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=105.9784267%20-28.15199&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [AT2026aknb](https://www.wis-tns.org/object/2026aknb) near IC3908

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC3908 as this object's host. The 0.25465° (15.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T13:14:37Z · 8 days · 19.48 r |
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
| Subject | **IC3908** · `IC3908` |
| Catalog display name | IC3908 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 13.3 · 2.43′ × 0.79′ |
| Distance | 20,950 kpc |
| Separation | 0.25465° · 15.28′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, considerably extended 160deg ; faint trail? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=194.1187155%20-7.3126105&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 41. [AT2026akqc](https://www.wis-tns.org/object/2026akqc) near IC 3954

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3954 as this object's host. The 0.35495° (21.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T13:03:32Z · 19 days · 18.99 r |
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
| Subject | **IC 3954** · `IC 3954` |
| Catalog display name | NGC 3954 |
| Type / constellation | Galaxy · Com |
| Catalog magnitude / angular size | — · 0.22′ × 0.15′ |
| Distance | — |
| Separation | 0.35495° · 21.30′ |
| Catalog description | NGC 3954 is an elliptical galaxy located 324 million light-years away in the Leo constellation. It was discovered on April 26, 1785, by the astronomer William Herschel. NGC 3954 is a LINER galaxy, and is a member of the NGC 3937 Group. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3954 has the different designation NGC 3954 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=195.1706791%2019.2002426&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 42. [SN2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65297° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.1 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 22 days · 19.17 wide |
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
| Separation | 1.65297° · 99.18′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiep) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=335.3713756%20-14.6685694&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 43. [SN2026ajxu](https://www.wis-tns.org/object/2026ajxu) near Collinder 27 (CR27)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 27 (CR27) as this object's host. The 1.69919° (101.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.028 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T09:38:01Z · 11 days · 19.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4659....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4659....1T/abstract) |
| Classification references | [2026TNSCR4752....1F](https://ui.adsabs.harvard.edu/abs/2026TNSCR4752....1F/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 27 (CR27)** · `CR27` |
| Catalog display name | Collinder 27 (CR27) |
| Type / constellation | Open cluster · Andromeda |
| Catalog magnitude / angular size | 8.9 · 4.5′ × 4.5′ |
| Distance | — |
| Separation | 1.69919° · 101.95′ |
| Catalog description | NGC 956 is an asterism in the constellation Andromeda. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=40.1534897%2045.5065724&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 44. [AT2026akqd](https://www.wis-tns.org/object/2026akqd) near IC2988

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2988 as this object's host. The 0.99471° (59.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T13:09:49Z · 2 days · 18.76 r |
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
| Subject | **IC2988** · `IC2988` |
| Catalog display name | IC2988 |
| Type / constellation | Nebula · Virgo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.99471° · 59.68′ |
| Catalog description | extremely, excessively faint, resolvable (mottled, not resolved), a single star 11.5 south following 2'.7 |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=180.9986907%202.4372625&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 45. [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) near NGC1169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1169 as this object's host. The 1.01795° (61.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T23:39:27Z · 14 days · 19.46 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4616....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4616....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1169** · `NGC1169` |
| Catalog display name | NGC1169 |
| Type / constellation | Galaxy · Perseus |
| Catalog magnitude / angular size | 11.4 · 3.31′ × 1.95′ |
| Distance | — |
| Separation | 1.01795° · 61.08′ |
| Catalog description | NGC 1169 is an intermediate barred spiral galaxy in the constellation of Perseus. NGC 1169 has a reddish center, indicating the region is dominated by older stars. In contrast, the outer ring contains larger blue-white stars, a sign of recent star formation. The entire galaxy is rotating at approximately 265 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=45.7965539%2045.3705684&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 46. [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.51580° (90.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:19:10Z · 14 days · 18.82 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4618....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4618....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 3294** · `NGC 3294` |
| Catalog display name | NGC 3294 |
| Type / constellation | Galaxy · LMi |
| Catalog magnitude / angular size | 11.68 · 3.08′ × 1.6′ |
| Distance | — |
| Separation | 1.51580° · 90.95′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.7863698%2036.2092805&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 47. [AT2026akhd](https://www.wis-tns.org/object/2026akhd) near IC625

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC625 as this object's host. The 1.99202° (119.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T06:03:30Z · 8 days · 18.95 wide |
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
| Subject | **IC625** · `IC625` |
| Catalog display name | IC625 |
| Type / constellation | Galaxy · Hydra |
| Catalog magnitude / angular size | 13.8 · 2.25′ × 0.53′ |
| Distance | 12,800 kpc |
| Separation | 1.99202° · 119.52′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) large, extended 110deg , diffused |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.6930392%20-21.9438442&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 48. [AT2026akhx](https://www.wis-tns.org/object/2026akhx) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.12692° (7.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 19 days · 21.13 r |
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
| Subject | **NGC3640** · `NGC3640` |
| Catalog display name | NGC3640 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 10.4 · 4.33′ × 3.81′ |
| Distance | — |
| Separation | 0.12692° · 7.62′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.315042%203.114375&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 49. [AT2026akir](https://www.wis-tns.org/object/2026akir) near NGC4450

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4450 as this object's host. The 0.23305° (13.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T22:35:02Z · 15 days · 20.71 g |
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
| Subject | **NGC4450** · `NGC4450` |
| Catalog display name | NGC4450 |
| Type / constellation | Galaxy · Coma Berenices |
| Catalog magnitude / angular size | 10.9 · 5.46′ × 3.78′ |
| Distance | — |
| Separation | 0.23305° · 13.98′ |
| Catalog description | NGC 4450 is a spiral galaxy in the constellation Coma Berenices. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akir) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=186.892375%2017.003683&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 50. [AT2026akjq](https://www.wis-tns.org/object/2026akjq) near NGC3348

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3348 as this object's host. The 0.04308° (2.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:08:19Z · 24 days · 19.97 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4740....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4740....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3348** · `NGC3348` |
| Catalog display name | NGC3348 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.9 · 2.13′ × 2.13′ |
| Distance | 32,200 kpc |
| Separation | 0.04308° · 2.58′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.9242991%2072.8217011&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 51. [AT2026akju](https://www.wis-tns.org/object/2026akju) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.15603° (9.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T14:21:07Z · 9 days · 22.1 r |
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
| Separation | 0.15603° · 9.36′ |
| Catalog description | NGC 741, also known as PGC 7252, is a formerly active radio galaxy in the constellation of Pisces. Located 74.13 Mpc away, NGC 741 is part of a group of galaxies including NGC 742 and PGC 7250. NGC 741 and NGC 742 recently collided, although the disruption was minor. Radio filaments have been found connecting NGC 741 to NGC 742, and due to the bent structure of the radio filaments, NGC 741 is estimated to be moving at 1400 km/s with respect to its local group, suggesting that ram-pressure stripping was created as a product of the former merger. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akju) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.226542%205.556869&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 52. [AT2026akmp](https://www.wis-tns.org/object/2026akmp) near IC 892

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 892 as this object's host. The 1.54281° (92.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T13:15:18Z · 8 days · 18.76 r |
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
| Subject | **IC 892** · `IC 892` |
| Catalog display name | NGC 7300 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 1.6′ × 0.84′ |
| Distance | — |
| Separation | 1.54281° · 92.57′ |
| Catalog description | NGC 7300 is an intermediate spiral galaxy in the constellation of Aquarius. Its velocity with respect to the cosmic microwave background is 4,566±24 km/s, which corresponds to a Hubble distance of 219.7 ± 15.4 Mly (67.35 ± 4.73 Mpc). However, 15 non-redshift measurements give a closer mean distance of 181.89 ± 10.31 Mly (55.767 ± 3.162 Mpc). It was discovered by British astronomer John Herschel on 26 July 1830. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 892 has the different designation NGC 7300 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=201.4025995%20-2.8496593&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 53. [AT2026akqh](https://www.wis-tns.org/object/2026akqh) near Lynds Bright Nebula 111 (LBN111)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 111 (LBN111) as this object's host. The 1.43721° (86.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T02:23:30Z · 2 days · 17.63 r |
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
| Subject | **Lynds Bright Nebula 111 (LBN111)** · `LBN111` |
| Catalog display name | Lynds Bright Nebula 111 (LBN111) |
| Type / constellation | HII · Aquila |
| Catalog magnitude / angular size | — · 20′ × 10′ |
| Distance | — |
| Separation | 1.43721° · 86.23′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akqh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=304.6875558%20-1.3444336&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 54. [SN2026afsg](https://www.wis-tns.org/object/2026afsg) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.22591° (73.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ib/c |
| Redshift | 0.010277 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T20:55:20Z · 39 days · 16.4 Clear |
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
| Separation | 1.22591° · 73.55′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude ≤16.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afsg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=180.5122937%2029.844743&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 55. [AT2026akhq](https://www.wis-tns.org/object/2026akhq) near IC3668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC3668 as this object's host. The 1.11334° (66.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T15:07:39Z · 7 days · 19.21 cyan |
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
| Subject | **IC3668** · `IC3668` |
| Catalog display name | IC3668 |
| Type / constellation | Nebula · Canes Venatici |
| Catalog magnitude / angular size | 13.1 · 0.79′ × 0.44′ |
| Distance | — |
| Separation | 1.11334° · 66.80′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, irregular figure, nucleus, or to a nucleus |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=189.845555%2040.088385&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 56. [AT2026akiv](https://www.wis-tns.org/object/2026akiv) near IC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC488 as this object's host. The 0.01538° (0.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T03:31:49Z · 6 days · 20 L |
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
| Subject | **IC488** · `IC488` |
| Catalog display name | IC488 |
| Type / constellation | Nebula · Cancer |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.01538° · 0.92′ |
| Catalog description | very faint, small in angular size, diffused, a star of 13th magnitude south preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akiv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=120.192318%2025.912943&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 57. [AT2026akiw](https://www.wis-tns.org/object/2026akiw) near IC656

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC656 as this object's host. The 1.14129° (68.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T05:22:04Z · 6 days · 19.34 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4718....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4718....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC656** · `IC656` |
| Catalog display name | IC656 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · 0.2′ × 0.2′ |
| Distance | — |
| Separation | 1.14129° · 68.48′ |
| Catalog description | very small in angular size, cluster, neb? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akiw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.8864309%2018.0599893&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 58. [AT2026aklr](https://www.wis-tns.org/object/2026aklr) near Baxendell's unphotographable nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Baxendell's unphotographable nebula as this object's host. The 1.57712° (94.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T02:53:59Z · 4 days · 19.48 r |
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
| Subject | **Baxendell's unphotographable nebula** · `NGC7088` |
| Catalog display name | Baxendell's unphotographable nebula |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.57712° · 94.63′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=322.0031191%200.4514292&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 59. [AT2026akly](https://www.wis-tns.org/object/2026akly) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.92745° (115.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T04:25:51Z · 4 days · 19.35 g |
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
| Subject | **NGC7453** · `NGC7453` |
| Catalog display name | NGC7453 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · 0.3′ × 0.3′ |
| Distance | — |
| Separation | 1.92745° · 115.65′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akly) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.3186661%20-8.2836285&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 60. [SN2026aifu](https://www.wis-tns.org/object/2026aifu) near Lynds Bright Nebula 1025 (LBN1025)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1025 (LBN1025) as this object's host. The 1.13184° (67.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.021892 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T10:32:52Z · 22 days · 19.01 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4457....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4457....1S/abstract) |
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
| Separation | 1.13184° · 67.91′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aifu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=90.08462%20-16.1648627&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 61. [AT2026akit](https://www.wis-tns.org/object/2026akit) near IC1560

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1560 as this object's host. The 0.48581° (29.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:18:14Z · 8 days · 19.03 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4717....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4717....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1560** · `IC1560` |
| Catalog display name | IC1560 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.48581° · 29.15′ |
| Catalog description | extremely, excessively faint; = 164? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akit) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.5744926%203.1296379&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 62. [AT2026akll](https://www.wis-tns.org/object/2026akll) near Skull Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Skull Nebula as this object's host. The 0.58800° (35.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:02:52Z · 8 days · 19.48 g |
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
| Subject | **Skull Nebula** · `C56` |
| Catalog display name | Skull Nebula |
| Type / constellation | Planetary nebula · Cetus |
| Catalog magnitude / angular size | 8 · 3.8′ × 3.8′ |
| Distance | 0.57 kpc |
| Separation | 0.58800° · 35.28′ |
| Catalog description | NGC 246 is a planetary nebula in the constellation Cetus. It was discovered in 1785 by William Herschel. The nebula and the stars associated with it are listed in several catalogs, as summarized by the SIMBAD database. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akll) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.1689126%20-11.9637191&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 63. [SN2026aeru](https://www.wis-tns.org/object/2026aeru) near NGC 3003

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3003 as this object's host. The 0.80302° (48.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.026631 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T11:50:49Z · 50 days · 18.09 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4044....1W](https://ui.adsabs.harvard.edu/abs/2026TNSTR4044....1W/abstract) |
| Classification references | [2026TNSCR4307....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4307....1S/abstract) |
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
| Separation | 0.80302° · 48.18′ |
| Catalog description | NGC 3003 is a nearly edge-on barred spiral galaxy in the constellation of Leo Minor, discovered by William Herschel on December 7, 1785. It has an apparent visual magnitude of 11.78, at a distance of 19.5 Mpc from the Sun. It has a recessional velocity of 1474 km/s. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=147.4886189%2032.67025&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 64. [SN2026ahby](https://www.wis-tns.org/object/2026ahby) near IC1438

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1438 as this object's host. The 1.07176° (64.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T09:45:39Z · 29 days · 19.7 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4342....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4342....1O/abstract) |
| Classification references | [2026TNSCR4607....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4607....1S/abstract) |
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
| Separation | 1.07176° · 64.31′ |
| Catalog description | faint, binuclear |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahby) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=335.0757838%20-22.0321726&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 65. [SN2026aikx](https://www.wis-tns.org/object/2026aikx) near IC 1730

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1730 as this object's host. The 1.43755° (86.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.073 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T08:41:41Z · 21 days · 20.65 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4481....1H](https://ui.adsabs.harvard.edu/abs/2026TNSTR4481....1H/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.7607552%2023.4280316&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 66. [AT2026akjk](https://www.wis-tns.org/object/2026akjk) near IC 1753

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1753 as this object's host. The 0.98851° (59.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T02:58:29Z · 5 days · 19.66 g |
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
| Subject | **IC 1753** · `IC 1753` |
| Catalog display name | IC438 |
| Type / constellation | Galaxy · Tri |
| Catalog magnitude / angular size | — · 0.84′ × 0.57′ |
| Distance | — |
| Separation | 0.98851° · 59.31′ |
| Catalog description | IC 438 is a spiral galaxy in the constellation of Lepus. Its velocity with respect to the cosmic microwave background is 3,199±6 km/s, which corresponds to a Hubble distance of 153.9 ± 10.8 Mly (47.18 ± 3.30 Mpc). However, 17 non-redshift measurements give a much closer distance of 136.45 ± 4.29 Mly (41.835 ± 1.314 Mpc). It was discovered by American astronomer Lewis Swift on 7 January 1891. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1753 has the different designation IC438 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.4543329%2028.5362965&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 67. [SN2026akpz](https://www.wis-tns.org/object/2026akpz) near NGC524

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC524 as this object's host. The 1.04562° (62.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.077 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:53:55Z · 14 days · 19.85 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4771....1W](https://ui.adsabs.harvard.edu/abs/2026TNSTR4771....1W/abstract) |
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
| Separation | 1.04562° · 62.74′ |
| Catalog description | NGC 524 is a lenticular galaxy in the constellation Pisces. It is at a distance of about 90 million light-years away from Earth. In the central bulge of the galaxy is visible gas forming a spiral structure. It is the largest galaxy in the small NGC 524 group of galaxies, which is associated with NGC 488 and its group. It was discovered by William Herschel on 4 September 1786. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.9691457%208.5174591&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 68. [AT2026aksi](https://www.wis-tns.org/object/2026aksi) near IC396

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC396 as this object's host. The 0.85301° (51.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-25T07:18:27Z · 1 days · 19.7 r |
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
| Separation | 0.85301° · 51.18′ |
| Catalog description | faint, small in angular size, round, brighter middle, or in the middle nucleus, or to a nucleus, faint double a single star south following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=74.2534685%2069.1720188&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 69. [AT2026aktz](https://www.wis-tns.org/object/2026aktz) near NGC1332

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1332 as this object's host. The 0.54438° (32.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T07:13:07Z · 0 days · 21.48 g |
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
| Subject | **NGC1332** · `NGC1332` |
| Catalog display name | NGC1332 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.4 · 5.31′ × 3.84′ |
| Distance | — |
| Separation | 0.54438° · 32.66′ |
| Catalog description | NGC 1332 is an almost edge-on elliptical galaxy located in constellation of Eridanus. Situated about 70 million light years away, it is a member of the Eridanus Cluster of galaxies, a cluster of about 200 galaxies. It is also the brightest member of the NGC 1332 Group. It was discovered by William Herschel on 9 December 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.781139%20-21.843267&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 70. [AT2026akua](https://www.wis-tns.org/object/2026akua) near NGC1400

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1400 as this object's host. The 0.41736° (25.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T07:13:07Z · 0 days · 21.9 g |
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
| Subject | **NGC1400** · `NGC1400` |
| Catalog display name | NGC1400 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 11.1 · 2.81′ × 2.52′ |
| Distance | — |
| Separation | 0.41736° · 25.04′ |
| Catalog description | NGC 1400 is an elliptical galaxy in the constellation Eridanus. At a distance of 65 million light-years from Earth, it was discovered by John Herschel in 1786. It is a member of the NGC 1407 group, whose brightest member is NGC 1407. The NGC 1407 group is part of the Eridanus Cluster, a cluster of 200 galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akua) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.493722%20-18.897615&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 71. [AT2026akmb](https://www.wis-tns.org/object/2026akmb) near Lynds Bright Nebula 113 (LBN113)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 113 (LBN113) as this object's host. The 1.07949° (64.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T03:08:27Z · 4 days · 19.22 i |
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
| Subject | **Lynds Bright Nebula 113 (LBN113)** · `LBN113` |
| Catalog display name | Lynds Bright Nebula 113 (LBN113) |
| Type / constellation | HII · Aquila |
| Catalog magnitude / angular size | — · 70′ × 20′ |
| Distance | — |
| Separation | 1.07949° · 64.77′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akmb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=304.1746683%20-0.2762116&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 72. [AT2026akmx](https://www.wis-tns.org/object/2026akmx) near Lynds Bright Nebula 563 (LBN563)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 563 (LBN563) as this object's host. The 1.15190° (69.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T21:08:15Z · 6 days · 19.2 L |
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
| Subject | **Lynds Bright Nebula 563 (LBN563)** · `LBN563` |
| Catalog display name | Lynds Bright Nebula 563 (LBN563) |
| Type / constellation | HII · Cassiopeia |
| Catalog magnitude / angular size | — · 60′ × 10′ |
| Distance | — |
| Separation | 1.15190° · 69.11′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akmx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.067822%2050.720838&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 73. [AT2026aksj](https://www.wis-tns.org/object/2026aksj) near Lynds Bright Nebula 702 (LBN702)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 702 (LBN702) as this object's host. The 1.88761° (113.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T05:26:43Z · 4 days · 19.4 g |
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
| Subject | **Lynds Bright Nebula 702 (LBN702)** · `LBN702` |
| Catalog display name | Lynds Bright Nebula 702 (LBN702) |
| Type / constellation | HII · Camelopardalis |
| Catalog magnitude / angular size | — · 70′ × 50′ |
| Distance | — |
| Separation | 1.88761° · 113.26′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aksj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.1052576%2064.5439958&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 74. [AT2026akud](https://www.wis-tns.org/object/2026akud) near Lynds Bright Nebula 853 (LBN853)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 853 (LBN853) as this object's host. The 1.82500° (109.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T06:22:43Z · 4 days · 19.47 r |
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
| Subject | **Lynds Bright Nebula 853 (LBN853)** · `LBN853` |
| Catalog display name | Lynds Bright Nebula 853 (LBN853) |
| Type / constellation | HII · Eridanus |
| Catalog magnitude / angular size | — · 930′ × 120′ |
| Distance | — |
| Separation | 1.82500° · 109.50′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akud) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=61.3428695%20-1.1025962&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 75. [AT2026akjn](https://www.wis-tns.org/object/2026akjn) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.99665° (119.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T04:12:52Z · 5 days · 19.97 g |
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
| Separation | 1.99665° · 119.80′ |
| Catalog description | NGC 891 is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda. It was discovered by William Herschel on October 6, 1784. The galaxy is a member of the NGC 1023 group of galaxies in the Local Supercluster. It has an H II nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.5214331%2041.1269182&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026akml](https://www.wis-tns.org/object/2026akml) near IC600

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC600 as this object's host. The 1.95164° (117.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T05:36:33Z · 6 days · 19.57 L |
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
| Subject | **IC600** · `IC600` |
| Catalog display name | IC600 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.7 · 1.92′ × 1.03′ |
| Distance | 20,600 kpc |
| Separation | 1.95164° · 117.10′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akml) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.2116425%20-3.1304625&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 77. [AT2026akob](https://www.wis-tns.org/object/2026akob) near IC 5126

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5126 as this object's host. The 1.19520° (71.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-23T02:53:05Z · 3 days · 19.57 r |
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
| Subject | **IC 5126** · `IC 5126` |
| Catalog display name | NGC 5135 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.37′ × 0.32′ |
| Distance | 194 ly |
| Separation | 1.19520° · 71.71′ |
| Catalog description | NGC 5135 is a barred spiral galaxy located in the constellation Hydra. It is located at a distance of about 200 million light years from Earth. It was discovered by John Herschel on May 8, 1834. It is a Seyfert galaxy. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5126 has the different designation NGC 5135 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akob) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=325.9013882%20-7.2540631&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 78. [AT2026akol](https://www.wis-tns.org/object/2026akol) near IC651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC651 as this object's host. The 1.39027° (83.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T21:50:24Z · 6 days · 21.96 r |
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
| Subject | **IC651** · `IC651` |
| Catalog display name | IC651 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.1 · 0.72′ × 0.71′ |
| Distance | — |
| Separation | 1.39027° · 83.42′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, gradually brighter middle, or in the middle, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akol) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.144333%20-1.838144&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 79. [AT2026akow](https://www.wis-tns.org/object/2026akow) near IC651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC651 as this object's host. The 1.48427° (89.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T22:50:52Z · 6 days · 22.21 g |
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
| Subject | **IC651** · `IC651` |
| Catalog display name | IC651 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.1 · 0.72′ × 0.71′ |
| Distance | — |
| Separation | 1.48427° · 89.06′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, gradually brighter middle, or in the middle, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akow) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.152%20-1.527228&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 80. [AT2026akpu](https://www.wis-tns.org/object/2026akpu) near IC598

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC598 as this object's host. The 1.02194° (61.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T19:19:12Z · 7 days · 21.09 g |
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
| Subject | **IC598** · `IC598` |
| Catalog display name | IC598 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 13.7 · 1.65′ × 0.41′ |
| Distance | — |
| Separation | 1.02194° · 61.32′ |
| Catalog description | very faint, very small in angular size, round, brighter middle, or in the middle, almost stellar, pointlike |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.532917%2042.839178&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 81. [AT2026akpw](https://www.wis-tns.org/object/2026akpw) near NGC3079

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3079 as this object's host. The 1.67677° (100.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T19:42:14Z · 7 days · 21.29 g |
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
| Subject | **NGC3079** · `NGC3079` |
| Catalog display name | NGC3079 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.7 · 8.18′ × 1.29′ |
| Distance | — |
| Separation | 1.67677° · 100.61′ |
| Catalog description | NGC 3079 is a barred spiral galaxy about 50 million light-years away, and located in the constellation Ursa Major. The galaxy was discovered by German-British astronomer William Herschel on 1 April 1790. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=150.958083%2057.336328&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 82. [AT2026akqv](https://www.wis-tns.org/object/2026akqv) near NGC3079

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3079 as this object's host. The 1.39713° (83.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T14:08:50Z · 5 days · 20.78 w |
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
| Subject | **NGC3079** · `NGC3079` |
| Catalog display name | NGC3079 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.7 · 8.18′ × 1.29′ |
| Distance | — |
| Separation | 1.39713° · 83.83′ |
| Catalog description | NGC 3079 is a barred spiral galaxy about 50 million light-years away, and located in the constellation Ursa Major. The galaxy was discovered by German-British astronomer William Herschel on 1 April 1790. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=148.6449596%2056.6279656&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 83. [AT2026akrd](https://www.wis-tns.org/object/2026akrd) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 1.31615° (78.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T21:59:02Z · 6 days · 21.86 r |
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
| Separation | 1.31615° · 78.97′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=167.902833%201.099214&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 84. [AT2026akrf](https://www.wis-tns.org/object/2026akrf) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.30131° (78.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-23T13:39:21Z · 3 days · 20.86 g |
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
| Subject | **IC 5374** · `IC 5374` |
| Catalog display name | NGC5374 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.67′ × 0.57′ |
| Distance | — |
| Separation | 1.30131° · 78.08′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.850833%203.267519&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 85. [AT2026akrr](https://www.wis-tns.org/object/2026akrr) near NGC3079

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3079 as this object's host. The 1.65178° (99.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T19:40:48Z · 7 days · 20.45 g |
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
| Subject | **NGC3079** · `NGC3079` |
| Catalog display name | NGC3079 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.7 · 8.18′ × 1.29′ |
| Distance | — |
| Separation | 1.65178° · 99.11′ |
| Catalog description | NGC 3079 is a barred spiral galaxy about 50 million light-years away, and located in the constellation Ursa Major. The galaxy was discovered by German-British astronomer William Herschel on 1 April 1790. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=147.65725%2056.140611&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 86. [AT2026akrs](https://www.wis-tns.org/object/2026akrs) near NGC2950

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2950 as this object's host. The 1.14398° (68.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T19:42:14Z · 7 days · 21.42 g |
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
| Subject | **NGC2950** · `NGC2950` |
| Catalog display name | NGC2950 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11 · 2.62′ × 1.65′ |
| Distance | 20,100 kpc |
| Separation | 1.14398° · 68.64′ |
| Catalog description | NGC 2950 is a lenticular galaxy in the northern constellation of Ursa Major, about 50 million light years from the Milky Way and receding with a heliocentric radial velocity of 1,329 km/s. It was discovered in 1790 by the Anglo-German astronomer William Herschel. NGC 2950 is a field galaxy, it is not part of a galaxy cluster or galaxy group, and thus is gravitationally isolated. Nine certain and four possible dwarf galaxies have been identified around NGC 2950. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=146.229958%2057.749233&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 87. [AT2026akrv](https://www.wis-tns.org/object/2026akrv) near NGC772

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC772 as this object's host. The 1.67884° (100.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T02:37:30Z · 5 days · 19.9 g |
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
| Subject | **NGC772** · `NGC772` |
| Catalog display name | NGC772 |
| Type / constellation | Galaxy · Aries |
| Catalog magnitude / angular size | 10.3 · 4.57′ × 2.52′ |
| Distance | — |
| Separation | 1.67884° · 100.73′ |
| Catalog description | NGC 772 is a large unbarred spiral galaxy approximately 106 million light-years away in the constellation Aries. It was discovered by German-British astronomer William Herschel on 29 November 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.0259275%2017.5119729&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 88. [AT2026aksz](https://www.wis-tns.org/object/2026aksz) near Local Group

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Local Group as this object's host. The 1.08218° (64.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T22:55:12Z · 7 days · 21.76 r |
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
| Subject | **Local Group** · `IC 686` |
| Catalog display name | Local Group |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 0.51′ × 0.26′ |
| Distance | — |
| Separation | 1.08218° · 64.93′ |
| Catalog description | The Local Group is the galaxy group that includes the Milky Way, where Earth is located. It consists of two collections of galaxies in a "dumbbell" shape; the Milky Way and its satellites form one lobe, and the Andromeda Galaxy and its satellites constitute the other. The two collections are separated by about 800 kiloparsecs (3×10^6 ly; 2×1019 km) and are moving toward one another with a velocity of 123 km/s. The center of the group is located at about 450 kpc (1.5 million ly) away from the Milky Way, placing it slightly closer to the Andromeda Galaxy by roughly 300 kpc (1 million ly), in which the latter may be more massive than the former in terms of mass. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.45%204.611083&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 89. [AT2026akto](https://www.wis-tns.org/object/2026akto) near NGC3665

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3665 as this object's host. The 1.92423° (115.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-26T11:30:04Z · 0 days · 19.61 g |
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
| Separation | 1.92423° · 115.45′ |
| Catalog description | NGC 3665 is a lenticular galaxy located in the constellation Ursa Major. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that NGC 3665 is about 85,000 light years across. It was discovered by William Herschel on March 23, 1789. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akto) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=172.065916%2036.9704576&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 90. [AT2026aipd](https://www.wis-tns.org/object/2026aipd) near IC 1746

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1746 as this object's host. The 0.30860° (18.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:09:36Z · 29 days · 21.22 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4512....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4512....1X/abstract) |
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
| Separation | 0.30860° · 18.52′ |
| Catalog description | NGC 502, also occasionally referred to as PGC 5034 or UGC 922, is a lenticular galaxy in the constellation Pisces. It is located approximately 113 million light-years from the Solar System and was discovered on 25 September 1862 by German astronomer Heinrich Louis d'Arrest. When the Morphological Catalogue of Galaxies was published between 1962 and 1974, the identifications of NGC 502 and NGC 505 were reversed. In reality, NGC 502 is equal to MGC +01-04-041 and not MCG +01-04-043 as noted in the catalogue. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1746 has the different designation NGC 502 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.9099339%204.8292846&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 91. [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.74061° (44.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 14 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4615....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4615....1O/abstract) |
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
| Separation | 0.74061° · 44.44′ |
| Catalog description | NGC 3239 is an irregular galaxy in the constellation of Leo. The galaxy was discovered in 1784 by William Herschel and is part of the New General Catalogue. It harbors a large and relatively bright H II region in its southeastern section that was first cataloged by Russian astronomer Boris Vorontsov-Velyaminov as VV95b. It's believed that NGC 3239 is the result of a galactic merger with a low-mass galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.0744604%2017.8811531&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 92. [AT2026akbv](https://www.wis-tns.org/object/2026akbv) near NGC 3686

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3686 as this object's host. The 0.69980° (41.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T05:07:48Z · 9 days · 19.99 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4670....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4670....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 3686** · `NGC 3686` |
| Catalog display name | NGC 3686 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.43 · 2.88′ × 2.18′ |
| Distance | — |
| Separation | 0.69980° · 41.99′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=172.3580875%2016.6545296&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 93. [AT2026akhy](https://www.wis-tns.org/object/2026akhy) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.74894° (44.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 19 days · 20.64 r |
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
| Subject | **NGC3640** · `NGC3640` |
| Catalog display name | NGC3640 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 10.4 · 4.33′ × 3.81′ |
| Distance | — |
| Separation | 0.74894° · 44.94′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.968417%203.918417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 94. [AT2026akhz](https://www.wis-tns.org/object/2026akhz) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 0.60410° (36.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T22:55:12Z · 16 days · 22.82 g |
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
| Separation | 0.60410° · 36.25′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.84275%20-0.417214&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 95. [AT2026akia](https://www.wis-tns.org/object/2026akia) near NGC3166

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3166 as this object's host. The 0.95306° (57.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:40:48Z · 14 days · 20.98 g |
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
| Subject | **NGC3166** · `NGC3166` |
| Catalog display name | NGC3166 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 10.6 · 4.5′ × 2.84′ |
| Distance | 22,000 kpc |
| Separation | 0.95306° · 57.18′ |
| Catalog description | NGC 3166 is a lenticular galaxy in the constellation Sextans. The galaxy lies about 65 million light years away from Earth, which means, given its apparent dimensions, that NGC 3166 is approximately 105,000 light years across. It was discovered by William Herschel on December 19, 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akia) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.463292%202.472008&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 96. [AT2026akib](https://www.wis-tns.org/object/2026akib) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 0.61522° (36.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:45:07Z · 18 days · 21.56 r |
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
| Separation | 0.61522° · 36.91′ |
| Catalog description | NGC 3521, also known as the Bubble Galaxy, is a flocculent intermediate spiral galaxy located in the constellation Leo. Its velocity with respect to the cosmic microwave background is 1167 ± 26 km/s, which corresponds to a Hubble distance of 56.1 ± 4.1 Mly (17.21 ± 1.26 Mpc). However, 26 non-redshift measurements give a much closer distance of 37.17 ± 1.83 Mly (11.395 ± 0.56 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akib) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.51075%20-0.590561&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 97. [AT2026akic](https://www.wis-tns.org/object/2026akic) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.77839° (46.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 19 days · 21.72 r |
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
| Subject | **NGC3640** · `NGC3640` |
| Catalog display name | NGC3640 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 10.4 · 4.33′ × 3.81′ |
| Distance | — |
| Separation | 0.77839° · 46.70′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akic) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.640917%203.922233&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 98. [AT2026akjt](https://www.wis-tns.org/object/2026akjt) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 0.59759° (35.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T22:43:40Z · 16 days · 22.87 g |
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
| Subject | **IC 632** · `IC 632` |
| Catalog display name | NGC 5334 |
| Type / constellation | Galaxy · Sex |
| Catalog magnitude / angular size | — · 0.98′ × 0.57′ |
| Distance | — |
| Separation | 0.59759° · 35.86′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.653375%200.170075&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 99. [AT2026akko](https://www.wis-tns.org/object/2026akko) near IC2446

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2446 as this object's host. The 0.75145° (45.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:59:02Z · 14 days · 22.14 g |
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
| Subject | **IC2446** · `IC2446` |
| Catalog display name | IC2446 |
| Type / constellation | Galaxy · Cancer |
| Catalog magnitude / angular size | 13.6 · 1.49′ × 0.61′ |
| Distance | 119,500 kpc |
| Separation | 0.75145° · 45.09′ |
| Catalog description | faint, small in angular size, extended 130deg , brighter middle, or in the middle nucleus, or to a nucleus, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akko) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=139.162375%2029.262258&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 100. [AT2026akkr](https://www.wis-tns.org/object/2026akkr) near NGC3310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3310 as this object's host. The 0.66200° (39.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T18:41:45Z · 12 days · 20.74 g |
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
| Subject | **NGC3310** · `NGC3310` |
| Catalog display name | NGC3310 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 1.8′ × 1.73′ |
| Distance | — |
| Separation | 0.66200° · 39.72′ |
| Catalog description | NGC 3310 is a grand design spiral galaxy in the constellation Ursa Major. It is a starburst galaxy and it is likely that NGC 3310 collided with one of its satellite galaxies about 100 million years ago, triggering widespread star formation. It is thought to be located approximately 46 million light-years away from the Earth, and is thought to be about 22,000 light-years wide. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.037458%2052.875469&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 101. [AT2026akkw](https://www.wis-tns.org/object/2026akkw) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 0.73584° (44.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:30:14Z · 12 days · 20.93 g |
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
| Subject | **NGC3319** · `NGC3319` |
| Catalog display name | NGC3319 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.4 · 3.63′ × 1.77′ |
| Distance | — |
| Separation | 0.73584° · 44.15′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.486292%2042.387678&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 102. [AT2026akkz](https://www.wis-tns.org/object/2026akkz) near IC 1540

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1540 as this object's host. The 0.38069° (22.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T12:00:00Z · 9 days · 21.29 g |
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
| Subject | **IC 1540** · `IC 1540` |
| Catalog display name | NGC 2685 |
| Type / constellation | Galaxy · And |
| Catalog magnitude / angular size | — · 0.97′ × 0.41′ |
| Distance | — |
| Separation | 0.38069° · 22.84′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1540 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.081292%2023.410489&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 103. [AT2026aklt](https://www.wis-tns.org/object/2026aklt) near IC5338

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5338 as this object's host. The 0.28524° (17.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:15:40Z · 8 days · 19.87 g |
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
| Subject | **IC5338** · `IC5338` |
| Catalog display name | IC5338 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 13.7 · 1.26′ × 0.91′ |
| Distance | — |
| Separation | 0.28524° · 17.11′ |
| Catalog description | IC 5337 or JW100, is a spiral galaxy located 800 million light-years away from the Solar System in the constellation of Pegasus. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.3979166%2021.0174987&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 104. [AT2026akmy](https://www.wis-tns.org/object/2026akmy) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 0.90933° (54.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T06:57:40Z · 18 days · 21.1 w |
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
| Subject | **IC1495** · `IC1495` |
| Catalog display name | IC1495 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13 · 1.33′ × 0.83′ |
| Distance | 80,650 kpc |
| Separation | 0.90933° · 54.56′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.5333437%20-12.5899947&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 105. [AT2026akot](https://www.wis-tns.org/object/2026akot) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 0.83806° (50.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T22:43:40Z · 8 days · 21.69 r |
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
| Separation | 0.83806° · 50.28′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akot) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.9705%20-0.842139&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 106. [AT2026akpe](https://www.wis-tns.org/object/2026akpe) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.43964° (26.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:07:40Z · 17 days · 21.67 r |
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
| Subject | **NGC2549** · `NGC2549` |
| Catalog display name | NGC2549 |
| Type / constellation | Galaxy · Lynx |
| Catalog magnitude / angular size | 11.1 · 3.63′ × 0.92′ |
| Distance | — |
| Separation | 0.43964° · 26.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=125.11825%2057.412439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 107. [AT2026aksb](https://www.wis-tns.org/object/2026aksb) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.44777° (26.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:32:00Z · 8 days · 19.75 g |
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
| Subject | **NGC 2207 / IC 2163** · `IC 207` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 1.81′ × 0.45′ |
| Distance | 81 ly |
| Separation | 0.44777° · 26.87′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.1141094%20-6.5877796&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 108. [AT2026aksr](https://www.wis-tns.org/object/2026aksr) near IC 186 A

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 186 A as this object's host. The 0.90589° (54.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:35:02Z · 19 days · 22.42 g |
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
| Separation | 0.90589° · 54.35′ |
| Catalog description | NGC 5746 is a barred spiral galaxy located in the eastern part of the constellation of Virgo. It was discovered on 24 February 1786 by German-British astronomer William Herschel. It is the lead member of the NGC 5746 Group of galaxies, itself one of the Virgo III Groups strung out to the east of the Virgo Supercluster of galaxies. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 186 A has the different designation NGC 5746 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.329208%20-0.676433&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 109. [AT2026akte](https://www.wis-tns.org/object/2026akte) near Mirach's Ghost

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Mirach's Ghost as this object's host. The 0.94077° (56.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T19:06:14Z · 29 days · 20.29 g |
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
| Separation | 0.94077° · 56.45′ |
| Catalog description | NGC 404 is a field galaxy located about 10 million light years away in the constellation Andromeda. It was discovered by William Herschel in 1784, and is visible through small telescopes. NGC 404 lies just beyond the Local Group and does not appear gravitationally bound to it. It is located within 7 arc-minutes of second magnitude star Mirach, making it a difficult target to observe or photograph and granting it the nickname "Mirach's Ghost". |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akte) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.501542%2035.091558&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 110. [SN2026aisi](https://www.wis-tns.org/object/2026aisi) near Collinder 133 (CR133)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 133 (CR133) as this object's host. The 1.35375° (81.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.029 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T10:33:14Z · 19 days · 20.26 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4513....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4513....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 133 (CR133)** · `CR133` |
| Catalog display name | Collinder 133 (CR133) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 9.7 · 6′ × 6′ |
| Distance | 2.2 kpc |
| Separation | 1.35375° · 81.22′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=108.4571614%2012.4870812&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 111. [SN2026aiys](https://www.wis-tns.org/object/2026aiys) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.74753° (104.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.04 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:48:30Z · 17 days · 19.55 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4526....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4526....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5251** · `IC5251` |
| Catalog display name | IC5251 |
| Type / constellation | Nebula · Pegasus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.74753° · 104.85′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiys) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=339.5791041%2011.6438661&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 112. [AT2026airi](https://www.wis-tns.org/object/2026airi) near NGC636

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.79681° (107.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T11:07:26Z · 19 days · 20.14 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4507....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4507....1O/abstract) |
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
| Separation | 1.79681° · 107.81′ |
| Catalog description | NGC 636 is an elliptical galaxy in the Cetus constellation. It is located about 96 million light-years from the Milky Way. It was discovered by the German–British astronomer William Herschel in 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.8348191%20-5.7167882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 113. [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) near IC1657

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.48817° (89.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T10:46:37Z · 14 days · 19.98 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4660....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4660....1O/abstract) |
| Classification references | — |
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
| Separation | 1.48817° · 89.29′ |
| Catalog description | extremely, excessively faint, small in angular size, very much / magnitude extended |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.5299367%20-31.4281733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 114. [AT2026akcc](https://www.wis-tns.org/object/2026akcc) near IC2143

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2143 as this object's host. The 1.17278° (70.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T13:27:30Z · 9 days · 19.55 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4672....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4672....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2143** · `IC2143` |
| Catalog display name | IC2143 |
| Type / constellation | Galaxy · Lepus |
| Catalog magnitude / angular size | 13.4 · 1.9′ × 0.92′ |
| Distance | 39,300 kpc |
| Separation | 1.17278° · 70.37′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, very much / magnitude extended 45deg , 3 stars (pl.) south following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=87.3781541%20-19.54558&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 115. [AT2026akcy](https://www.wis-tns.org/object/2026akcy) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.31632° (78.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T11:33:08Z · 8 days · 19.55 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4695....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4695....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Caldwell 48 (C48)** · `C48` |
| Catalog display name | Caldwell 48 (C48) |
| Type / constellation | Galaxy · Cancer |
| Catalog magnitude / angular size | 10.3 · 4.5′ × 3′ |
| Distance | 26,400 kpc |
| Separation | 1.31632° · 78.98′ |
| Catalog description | NGC 2775, also known as Caldwell 48, is a spiral galaxy in the constellation Cancer. It is 67 million light-years away from the Milky Way. It was discovered by German-British astronomer William Herschel on 19 December 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.5117799%206.0988&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 116. [AT2026akgw](https://www.wis-tns.org/object/2026akgw) near NGC7457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7457 as this object's host. The 1.57742° (94.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T19:41:38Z · 11 days · 19.98 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4700....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4700....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7457** · `NGC7457` |
| Catalog display name | NGC7457 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 11 · 3.95′ × 2.25′ |
| Distance | — |
| Separation | 1.57742° · 94.65′ |
| Catalog description | NGC 7457 is an unbarred lenticular galaxy in the constellation Pegasus. NGC 7457 is its New General Catalogue designation. It was discovered by the astronomer William Herschel on 12 September 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.5460385%2029.5833122&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 117. [AT2026akho](https://www.wis-tns.org/object/2026akho) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.12255° (67.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 12 days · 23.08 r |
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
| Separation | 1.12255° · 67.35′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akho) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.971611%20-49.0135335&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 118. [AT2026akif](https://www.wis-tns.org/object/2026akif) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.04947° (62.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T16:35:02Z · 12 days · 22.46 r |
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
| Separation | 1.04947° · 62.97′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akif) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.876958%203.826464&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 119. [AT2026akix](https://www.wis-tns.org/object/2026akix) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.42748° (85.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:21:55Z · 20 days · 23.81 r |
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
| Separation | 1.42748° · 85.65′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akix) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.625375%20-49.985583&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 120. [AT2026akjp](https://www.wis-tns.org/object/2026akjp) near Caldwell 3 (C3)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 3 (C3) as this object's host. The 1.24289° (74.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T11:54:19Z · 18 days · 19.82 r |
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
| Subject | **Caldwell 3 (C3)** · `C3` |
| Catalog display name | Caldwell 3 (C3) |
| Type / constellation | Galaxy · Draco |
| Catalog magnitude / angular size | 9.7 · 21′ × 7′ |
| Distance | — |
| Separation | 1.24289° · 74.57′ |
| Catalog description | NGC 4236 is a barred Magellanic spiral galaxy located in the constellation Draco. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.052576%2068.9023678&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 121. [AT2026akjs](https://www.wis-tns.org/object/2026akjs) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.50636° (90.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:29:16Z · 18 days · 22.16 r |
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
| Separation | 1.50636° · 90.38′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.31775%204.249436&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 122. [AT2026akke](https://www.wis-tns.org/object/2026akke) near NGC3310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3310 as this object's host. The 1.50843° (90.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:27:50Z · 20 days · 20.8 g |
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
| Subject | **NGC3310** · `NGC3310` |
| Catalog display name | NGC3310 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 1.8′ × 1.73′ |
| Distance | — |
| Separation | 1.50843° · 90.51′ |
| Catalog description | NGC 3310 is a grand design spiral galaxy in the constellation Ursa Major. It is a starburst galaxy and it is likely that NGC 3310 collided with one of its satellite galaxies about 100 million years ago, triggering widespread star formation. It is thought to be located approximately 46 million light-years away from the Earth, and is thought to be about 22,000 light-years wide. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akke) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.086083%2054.683889&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 123. [AT2026akkh](https://www.wis-tns.org/object/2026akkh) near NGC2841

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2841 as this object's host. The 1.69532° (101.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T21:28:48Z · 17 days · 21.56 r |
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
| Subject | **NGC2841** · `NGC2841` |
| Catalog display name | NGC2841 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.2 · 6.9′ × 3.31′ |
| Distance | — |
| Separation | 1.69532° · 101.72′ |
| Catalog description | NGC 2841 is an unbarred spiral galaxy in the northern circumpolar constellation of Ursa Major. It was discovered on 9 March, 1788 by German-born astronomer William Herschel. J. L. E. Dreyer, the author of the New General Catalogue, described it as, "very bright, large, very much extended 151°, very suddenly much brighter middle equal to 10th magnitude star". Initially thought to be about 30 million light-years distant, a 2001 Hubble Space Telescope survey of the galaxy's Cepheid variables determined its distance to be approximately 14.1 megaparsecs, or 46 million light-years. The optical size of the galaxy is 8.1′ × 3.5′. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.659667%2049.758347&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 124. [AT2026akkm](https://www.wis-tns.org/object/2026akkm) near NGC3198

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3198 as this object's host. The 1.12242° (67.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T22:33:36Z · 15 days · 21.22 g |
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
| Subject | **NGC3198** · `NGC3198` |
| Catalog display name | NGC3198 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.4 · 6.46′ × 1.84′ |
| Distance | — |
| Separation | 1.12242° · 67.35′ |
| Catalog description | NGC 3198, also known as Herschel 146 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by German-British astronomer William Herschel on 15 January 1788. NGC 3198 is located in the Leo Spur, which is part of the Virgo Supercluster, and is approximately 47 million light years away. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.096083%2044.614344&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 125. [AT2026akkq](https://www.wis-tns.org/object/2026akkq) near NGC 2782

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2782 as this object's host. The 1.48763° (89.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:06:14Z · 14 days · 21.92 g |
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
| Subject | **NGC 2782** · `NGC 2782` |
| Catalog display name | NGC 2782 |
| Type / constellation | Galaxy · Lyn |
| Catalog magnitude / angular size | 12.36 · 3.25′ × 2.41′ |
| Distance | — |
| Separation | 1.48763° · 89.26′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=139.682917%2038.926181&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 126. [AT2026akks](https://www.wis-tns.org/object/2026akks) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.31211° (78.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:17:45Z · 12 days · 20.65 g |
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
| Subject | **NGC3319** · `NGC3319` |
| Catalog display name | NGC3319 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.4 · 3.63′ × 1.77′ |
| Distance | — |
| Separation | 1.31211° · 78.73′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akks) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.085125%2041.374264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 127. [AT2026akkx](https://www.wis-tns.org/object/2026akkx) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.95134° (117.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:30:14Z · 12 days · 21.4 g |
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
| Subject | **NGC3319** · `NGC3319` |
| Catalog display name | NGC3319 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.4 · 3.63′ × 1.77′ |
| Distance | — |
| Separation | 1.95134° · 117.08′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=162.068417%2042.661697&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 128. [AT2026aklk](https://www.wis-tns.org/object/2026aklk) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.18839° (71.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:05:35Z · 8 days · 20.13 g |
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
| Subject | **IC 5374** · `IC 5374` |
| Catalog display name | NGC5374 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 0.67′ × 0.57′ |
| Distance | — |
| Separation | 1.18839° · 71.30′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.1066794%203.6552999&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026akmd](https://www.wis-tns.org/object/2026akmd) near IC2389

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2389 as this object's host. The 1.32298° (79.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T09:55:47Z · 16 days · 21.03 g |
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
| Subject | **IC2389** · `IC2389` |
| Catalog display name | IC2389 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 13.3 · 1.3′ × 0.3′ |
| Distance | 22,500 kpc |
| Separation | 1.32298° · 79.38′ |
| Catalog description | very faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.3145007%2073.5685383&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026akni](https://www.wis-tns.org/object/2026akni) near IC2035

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2035 as this object's host. The 1.74091° (104.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:23:14Z · 27 days · 23.18 g |
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
| Separation | 1.74091° · 104.45′ |
| Catalog description | faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akni) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.380167%20-46.438556&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026aknn](https://www.wis-tns.org/object/2026aknn) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 1.46175° (87.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T21:33:07Z · 8 days · 21.42 g |
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
| Subject | **IC 632** · `IC 632` |
| Catalog display name | NGC 5334 |
| Type / constellation | Galaxy · Sex |
| Catalog magnitude / angular size | — · 0.98′ × 0.57′ |
| Distance | — |
| Separation | 1.46175° · 87.71′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.71075%20-1.385419&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026akon](https://www.wis-tns.org/object/2026akon) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 1.79903° (107.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T22:55:12Z · 16 days · 22.49 g |
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
| Separation | 1.79903° · 107.94′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akon) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=168.318208%20-1.617547&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 133. [AT2026akoo](https://www.wis-tns.org/object/2026akoo) near IC651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC651 as this object's host. The 1.90084° (114.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:49:26Z · 14 days · 21.27 g |
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
| Subject | **IC651** · `IC651` |
| Catalog display name | IC651 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.1 · 0.72′ × 0.71′ |
| Distance | — |
| Separation | 1.90084° · 114.05′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, gradually brighter middle, or in the middle, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akoo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.5995%20-2.231133&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 134. [AT2026akoz](https://www.wis-tns.org/object/2026akoz) near NGC2681

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2681 as this object's host. The 1.83591° (110.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T22:09:07Z · 30 days · 19.99 r |
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
| Subject | **NGC2681** · `NGC2681` |
| Catalog display name | NGC2681 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.9 · 3.97′ × 3.97′ |
| Distance | — |
| Separation | 1.83591° · 110.15′ |
| Catalog description | NGC 2681 is a lenticular galaxy in the constellation Ursa Major. The galaxy lies 50 million light years away from Earth, which means, given its apparent dimensions, that NGC 2681 is approximately 55,000 light years across. NGC 2681 has an active galactic nucleus and it is a type 3 Seyfert galaxy. Its nucleus is also a low-ionization nuclear emission-line region. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akoz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=136.255958%2050.963769&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 135. [AT2026akpa](https://www.wis-tns.org/object/2026akpa) near NGC3726

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3726 as this object's host. The 1.65954° (99.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:40:19Z · 12 days · 21.85 g |
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
| Subject | **NGC3726** · `NGC3726` |
| Catalog display name | NGC3726 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.5 · 5.27′ × 3.54′ |
| Distance | — |
| Separation | 1.65954° · 99.57′ |
| Catalog description | NGC 3726 is a barred spiral galaxy located in the constellation Ursa Major. It is located at a distance of circa 45 million light years from Earth, which, given its apparent dimensions, means that NGC 3726 is about 85,000 light years across. It was discovered by German-British astronomer William Herschel on February 5, 1788. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=172.239042%2045.553358&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 136. [AT2026akqn](https://www.wis-tns.org/object/2026akqn) near NGC 157

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 157 as this object's host. The 1.29573° (77.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T04:57:49Z · 8 days · 20.15 g |
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
| Subject | **NGC 157** · `NGC 157` |
| Catalog display name | NGC 157 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | 13.11 · 3.7′ × 1.9′ |
| Distance | — |
| Separation | 1.29573° · 77.74′ |
| Catalog description | Extended HIPASS source |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=7.5172312%20-8.9654456&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 137. [AT2026akqq](https://www.wis-tns.org/object/2026akqq) near Messier 81

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 81 as this object's host. The 1.34772° (80.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T07:47:01Z · 15 days · 20.51 r |
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
| Subject | **Messier 81** · `IC 1596` |
| Catalog display name | Messier 81 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.88′ × 0.75′ |
| Distance | — |
| Separation | 1.34772° · 80.86′ |
| Catalog description | Messier 81 (also known as NGC 3031 or Bode's Galaxy) is a grand design spiral galaxy about 12 million light-years away in the constellation Ursa Major. It has a D25 isophotal diameter of 29.44 kiloparsecs (96,000 light-years). Because of its relative proximity to the Milky Way galaxy, large size, and active galactic nucleus (which harbors a 70 million M☉ supermassive black hole), Messier 81 has been studied extensively by professional astronomers. The galaxy's large size and relatively high brightness also makes it a popular target for amateur astronomers. In late February 2022, astronomers reported that M81 may be the source of FRB 20200120E, a repeating fast radio burst. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=13.4081924%2022.8469262&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 138. [AT2026akra](https://www.wis-tns.org/object/2026akra) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.47772° (88.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T22:33:36Z · 8 days · 21.55 r |
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
| Separation | 1.47772° · 88.66′ |
| Catalog description | NGC 3521, also known as the Bubble Galaxy, is a flocculent intermediate spiral galaxy located in the constellation Leo. Its velocity with respect to the cosmic microwave background is 1167 ± 26 km/s, which corresponds to a Hubble distance of 56.1 ± 4.1 Mly (17.21 ± 1.26 Mpc). However, 26 non-redshift measurements give a much closer distance of 37.17 ± 1.83 Mly (11.395 ± 0.56 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akra) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.049333%20-1.497369&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 139. [AT2026akrg](https://www.wis-tns.org/object/2026akrg) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.03625° (62.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:34:33Z · 22 days · 21.7 r |
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
| Subject | **NGC 2207 / IC 2163** · `IC 2404` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Cnc |
| Catalog magnitude / angular size | — · 0.76′ × 0.55′ |
| Distance | 81 ly |
| Separation | 1.03625° · 62.17′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=133.226458%2029.613536&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 140. [AT2026akrm](https://www.wis-tns.org/object/2026akrm) near NGC3310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3310 as this object's host. The 1.52759° (91.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:16:19Z · 12 days · 20.79 g |
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
| Subject | **NGC3310** · `NGC3310` |
| Catalog display name | NGC3310 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 1.8′ × 1.73′ |
| Distance | — |
| Separation | 1.52759° · 91.66′ |
| Catalog description | NGC 3310 is a grand design spiral galaxy in the constellation Ursa Major. It is a starburst galaxy and it is likely that NGC 3310 collided with one of its satellite galaxies about 100 million years ago, triggering widespread star formation. It is thought to be located approximately 46 million light-years away from the Earth, and is thought to be about 22,000 light-years wide. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.426542%2055.023358&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 141. [AT2026akrx](https://www.wis-tns.org/object/2026akrx) near IC2035

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2035 as this object's host. The 1.42035° (85.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:26:49Z · 27 days · 22.79 i |
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
| Separation | 1.42035° · 85.22′ |
| Catalog description | faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.412208%20-46.689194&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 142. [AT2026aksk](https://www.wis-tns.org/object/2026aksk) near IC512

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC512 as this object's host. The 1.08444° (65.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T09:22:01Z · 8 days · 20.2 r |
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
| Subject | **IC512** · `IC512` |
| Catalog display name | IC512 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 13.1 · 1.72′ × 1.34′ |
| Distance | 22,100 kpc |
| Separation | 1.08444° · 65.07′ |
| Catalog description | faint, small in angular size, round, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=135.9685198%2084.417257&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 143. [SN2026aggp](https://www.wis-tns.org/object/2026aggp) near IC532

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC532 as this object's host. The 1.14385° (68.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.055 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-21T14:26:49Z · 36 days · 17.63 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4242....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4242....1T/abstract) |
| Classification references | [2026TNSCR4294....1W](https://ui.adsabs.harvard.edu/abs/2026TNSCR4294....1W/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC532** · `IC532` |
| Catalog display name | IC532 |
| Type / constellation | Nebula · Hydra |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.14385° · 68.63′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) large, extended preceding-following, brighter middle, or in the middle |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude ≤18.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aggp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=139.0558536%20-17.6784167&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026akoh](https://www.wis-tns.org/object/2026akoh) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.15574° (69.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T02:27:57Z · 4 days · 19.74 r |
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
| Subject | **IC5248** · `IC5248` |
| Catalog display name | IC5248 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.15574° · 69.34′ |
| Catalog description | suspected (13.5 mag) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akoh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=340.5043772%20-1.2808324&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026akrz](https://www.wis-tns.org/object/2026akrz) near IC1547

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1547 as this object's host. The 1.08700° (65.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T02:38:17Z · 4 days · 19.65 r |
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
| Subject | **IC1547** · `IC1547` |
| Catalog display name | IC1547 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.08700° · 65.22′ |
| Catalog description | eF.pS, suddenly (abruptly) / south brighter middle, or in the middle a single star |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.2405526%2022.3044186&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026aksx](https://www.wis-tns.org/object/2026aksx) near NGC3387

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3387 as this object's host. The 1.06791° (64.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T22:33:36Z · 7 days · 22.18 r |
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
| Subject | **NGC3387** · `NGC3387` |
| Catalog display name | NGC3387 |
| Type / constellation | Nebula · Sextans |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.06791° · 64.07′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.516125%204.050519&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 147. [AT2026akug](https://www.wis-tns.org/object/2026akug) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.90789° (114.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-24T15:38:22Z · 2 days · 27.37 F200W |
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
| Subject | **Robin's Egg Nebula** · `NGC 1360` |
| Catalog display name | Robin's Egg Nebula |
| Type / constellation | Planetary nebula · For |
| Catalog magnitude / angular size | — · 6′ × 4.5′ |
| Distance | — |
| Separation | 1.90789° · 114.47′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akug) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.213333%20-27.773494&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026akie](https://www.wis-tns.org/object/2026akie) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 0.80143° (48.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:48:00Z · 14 days · 21.89 g |
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
| Subject | **NGC3229** · `NGC3229` |
| Catalog display name | NGC3229 |
| Type / constellation | Nebula · Sextans |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.80143° · 48.09′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akie) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.94125%20-0.731408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026akiy](https://www.wis-tns.org/object/2026akiy) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 0.48687° (29.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:23:48Z · 27 days · 23.45 r |
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
| Subject | **NGC7453** · `NGC7453` |
| Catalog display name | NGC7453 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · 0.3′ × 0.3′ |
| Distance | — |
| Separation | 0.48687° · 29.21′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akiy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.812542%20-6.5285&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 150. [AT2026akkb](https://www.wis-tns.org/object/2026akkb) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 0.94983° (56.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:37:26Z · 20 days · 21.01 g |
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
| Subject | **Gemini nebula** · `NGC 2371` |
| Catalog display name | Gemini nebula |
| Type / constellation | Planetary nebula · Gem |
| Catalog magnitude / angular size | — · 1.23′ × 0.9′ |
| Distance | — |
| Separation | 0.94983° · 56.99′ |
| Catalog description | NGC 2371-2 is a dual lobed planetary nebula located in the constellation Gemini. Visually, it appears like it could be two separate objects; therefore, two entries were given to the planetary nebula by John Louis Emil Dreyer in the New General Catalogue, so it may be referred to as NGC 2371, NGC 2372, or variations on this name. It has also been called the double bubble nebula. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=110.736292%2028.734108&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 151. [AT2026akkc](https://www.wis-tns.org/object/2026akkc) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 0.26232° (15.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:37:26Z · 20 days · 21.65 g |
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
| Subject | **Gemini nebula** · `NGC 2371` |
| Catalog display name | Gemini nebula |
| Type / constellation | Planetary nebula · Gem |
| Catalog magnitude / angular size | — · 1.23′ × 0.9′ |
| Distance | — |
| Separation | 0.26232° · 15.74′ |
| Catalog description | NGC 2371-2 is a dual lobed planetary nebula located in the constellation Gemini. Visually, it appears like it could be two separate objects; therefore, two entries were given to the planetary nebula by John Louis Emil Dreyer in the New General Catalogue, so it may be referred to as NGC 2371, NGC 2372, or variations on this name. It has also been called the double bubble nebula. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.701833%2029.438133&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 152. [AT2026akls](https://www.wis-tns.org/object/2026akls) near Collinder 444 (CR444)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 444 (CR444) as this object's host. The 0.80752° (48.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T04:25:52Z · 23 days · 20.82 g |
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
| Subject | **Collinder 444 (CR444)** · `CR444` |
| Catalog display name | Collinder 444 (CR444) |
| Type / constellation | Open cluster · Lacerta |
| Catalog magnitude / angular size | 7.7 · 6′ × 6′ |
| Distance | 1.168 kpc |
| Separation | 0.80752° · 48.45′ |
| Catalog description | NGC 7209 is an open cluster in the constellation Lacerta. It was discovered by William Herschel on 19 October 1787. The cluster lies 3,810 light years away from Earth. It has been suggested that there is another cluster at a distance of 2,100 light years projected in front of a cluster lying at 3,800 light years away, based on the reddening of the cluster, however, further photometric studies of the cluster did not support that claim. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akls) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.4518258%2046.5021232&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026aklx](https://www.wis-tns.org/object/2026aklx) near Caldwell 1 (C1)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 1 (C1) as this object's host. The 0.94306° (56.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T06:49:29Z · 17 days · 20.47 r |
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
| Separation | 0.94306° · 56.58′ |
| Catalog description | NGC 188 is an open cluster in the constellation Cepheus. It was discovered by John Herschel in 1825. Unlike most open clusters that drift apart after a few million years because of the gravitational interaction of our Milky Way galaxy, NGC 188 lies far above the plane of the galaxy and is one of the most ancient of open clusters known, at approximately 6.8 billion years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aklx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.4027933%2084.3274901&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 154. [AT2026akmh](https://www.wis-tns.org/object/2026akmh) near IC 489

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 489 as this object's host. The 0.60193° (36.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T12:06:01Z · 8 days · 20.83 r |
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
| Subject | **IC 489** · `IC 489` |
| Catalog display name | IC 348 |
| Type / constellation | Star · Cnc |
| Catalog magnitude / angular size | — · 20′ × 20′ |
| Distance | — |
| Separation | 0.60193° · 36.12′ |
| Catalog description | IC 348 is a star-forming region in the constellation Perseus located about 1,000 light years from the Sun. Together with NGC 1333 it is part of the Perseus molecular cloud. It consists of nebulosity and an associated 2-million-year-old cluster of roughly 400 stars within an angular diameter of 20″. A later work found an older age of about 5 Million years. The most massive stars in the cluster are the binary star system HD 281159 (BD+31°643), which has a combined spectral class of B5, and is surrounded by an accretion disk. This binary is surrounded by an incomplete spherical shell open to the northwest, 50,000 AU in diameter, seen in infrared images of Spitzer and JWST. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 489 has the different designation IC 348 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=120.751728%2025.4806027&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 155. [AT2026akmt](https://www.wis-tns.org/object/2026akmt) near Collinder 179 (CR179)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 179 (CR179) as this object's host. The 0.40651° (24.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T11:21:13Z · 8 days · 20.26 g |
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
| Subject | **Collinder 179 (CR179)** · `CR179` |
| Catalog display name | Collinder 179 (CR179) |
| Type / constellation | Open cluster · Hydra |
| Catalog magnitude / angular size | 5.8 · 28.2′ × 28.2′ |
| Distance | 0.77 kpc |
| Separation | 0.40651° · 24.39′ |
| Catalog description | Messier 48 or M48, also known as NGC 2548, is an open cluster of stars in the equatorial constellation of Hydra. It sits near Hydra's westernmost limit with Monoceros, about 18° 34′ to the east and slightly south of Hydra's brightest star, Alphard. This grouping was discovered by Charles Messier in 1771, but there is no cluster precisely where Messier indicated; he made an error, as he did with M47. The value that he gave for the right ascension matches, however, his declination is off by five degrees. Credit for discovery is sometimes given instead to Caroline Herschel in 1783. Her nephew John Herschel described it as, "a superb cluster which fills the whole field; stars of 9th and 10th to the 13th magnitude – and none below, but the whole ground of the sky on which it stands is singularly dotted over with infinitely minute points". |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akmt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=122.8929425%20-5.9477056&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 156. [AT2026akng](https://www.wis-tns.org/object/2026akng) near NGC2875

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2875 as this object's host. The 0.31508° (18.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T11:25:58Z · 8 days · 20.51 g |
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
| Subject | **NGC2875** · `NGC2875` |
| Catalog display name | NGC2875 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.31508° · 18.90′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akng) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.7699587%2011.4014711&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 157. [AT2026akrn](https://www.wis-tns.org/object/2026akrn) near IC2278

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2278 as this object's host. The 0.69641° (41.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:41:45Z · 14 days · 21.32 g |
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
| Subject | **IC2278** · `IC2278` |
| Catalog display name | IC2278 |
| Type / constellation | Nebula · Cancer |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.69641° · 41.78′ |
| Catalog description | irregular figure, connected with IC 2276, 80 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=125.323792%2018.20515&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 158. [AT2026aksa](https://www.wis-tns.org/object/2026aksa) near Alpha Persei Cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Alpha Persei Cluster as this object's host. The 0.60304° (36.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T07:07:24Z · 4 days · 19.75 r |
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
| Subject | **Alpha Persei Cluster** · `MEL20` |
| Catalog display name | Alpha Persei Cluster |
| Type / constellation | Open cluster · Perseus |
| Catalog magnitude / angular size | 1.2 · — |
| Distance | — |
| Separation | 0.60304° · 36.18′ |
| Catalog description | The Alpha Persei Cluster, also known as Melotte 20 or Collinder 39, is an open cluster of stars in the northern constellation of Perseus. To the naked eye, the cluster consists of several blue-hued spectral type B stars. The most luminous member is the ~2nd magnitude yellow supergiant Mirfak, also known as Alpha Persei. Bright members also include Delta, Sigma, Psi, 29, 30, 34, and 48 Persei. The Hipparcos satellite and infrared color-magnitude diagram fitting have been used to establish a distance to the cluster of ~560 light-years (172 pc). The distance established via the independent analyses agree, thereby making the cluster an important rung on the cosmic distance ladder. As seen from the Earth, the extinction of the cluster due to interstellar dust is around 0.30. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aksa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.186185%2047.9067542&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 159. [AT2026akss](https://www.wis-tns.org/object/2026akss) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 0.92286° (55.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:40:48Z · 14 days · 22.26 g |
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
| Subject | **NGC3229** · `NGC3229` |
| Catalog display name | NGC3229 |
| Type / constellation | Nebula · Sextans |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.92286° · 55.37′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akss) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.681542%200.972158&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 160. [AT2026aktf](https://www.wis-tns.org/object/2026aktf) near NGC737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC737 as this object's host. The 0.32108° (19.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T20:45:36Z · 21 days · 21.36 g |
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
| Subject | **NGC737** · `NGC737` |
| Catalog display name | NGC737 |
| Type / constellation | Nebula · Triangulum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.32108° · 19.26′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.902667%2032.816542&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 161. [AT2026agvn](https://www.wis-tns.org/object/2026agvn) near NGC3486

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 38/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3486 as this object's host. The 1.16840° (70.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T12:50:15Z · 32 days · 18.12 r |
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
| Separation | 1.16840° · 70.10′ |
| Catalog description | NGC 3486 is an intermediate barred spiral galaxy located about 27.4 million light years away in the constellation of Leo Minor. It has a morphological classification of SAB(r)c, which indicates it is a weakly barred spiral with an inner ring and loosely wound arms. This is a borderline, low-luminosity Seyfert galaxy with an active nucleus. However, no radio or X-ray emission has been detected from the core, and it may only have a small supermassive black hole with less than a million times the mass of the Sun. |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agvn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.4182933%2029.1451089&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 162. [AT2026aijr](https://www.wis-tns.org/object/2026aijr) near NGC7447

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7447 as this object's host. The 1.89138° (113.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:48:34Z · 22 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4473....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4473....1R/abstract) |
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
| Separation | 1.89138° · 113.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.702808%20-12.3273961&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 163. [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.09787° (65.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:01:26Z · 20 days · 20.91 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4625....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4625....1X/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Intergalactic Wanderer** · `C25` |
| Catalog display name | Intergalactic Wanderer |
| Type / constellation | Globular cluster · Lynx |
| Catalog magnitude / angular size | 10.4 · 4.1′ × 4.1′ |
| Distance | 84.2 kpc |
| Separation | 1.09787° · 65.87′ |
| Catalog description | NGC 2419 is a globular cluster in the constellation Lynx. It was discovered by William Herschel on December 31, 1788. NGC 2419 is at a distance of about 300,000 light years from the Solar System and at the same distance from the Galactic Center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.1675378%2038.6017523&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 164. [AT2026akcq](https://www.wis-tns.org/object/2026akcq) near IC2189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2189 as this object's host. The 1.26362° (75.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T02:35:57Z · 11 days · 19.76 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4687....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4687....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2189** · `IC2189` |
| Catalog display name | IC2189 |
| Type / constellation | Nebula · Canis Minor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.26362° · 75.82′ |
| Catalog description | planetary nebula stellar, pointlike |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.6370499%2010.0129703&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 165. [AT2026akhj](https://www.wis-tns.org/object/2026akhj) near IC2328

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2328 as this object's host. The 1.00650° (60.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T03:36:43Z · 9 days · 19.63 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4716....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4716....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2328** · `IC2328` |
| Catalog display name | IC2328 |
| Type / constellation | Nebula · Cancer |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.00650° · 60.39′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, much / magnitude extended 65deg |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=124.8309665%2020.3441485&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 166. [AT2026akhw](https://www.wis-tns.org/object/2026akhw) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 1.62985° (97.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:37:55Z · 14 days · 21.25 g |
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
| Subject | **NGC3229** · `NGC3229` |
| Catalog display name | NGC3229 |
| Type / constellation | Nebula · Sextans |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.62985° · 97.79′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.224292%200.181&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 167. [AT2026akil](https://www.wis-tns.org/object/2026akil) near NGC3097

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3097 as this object's host. The 1.78512° (107.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:29:16Z · 20 days · 21.05 g |
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
| Subject | **NGC3097** · `NGC3097` |
| Catalog display name | NGC3097 |
| Type / constellation | Nebula · Ursa Major |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.78512° · 107.11′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akil) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.580042%2058.876639&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 168. [AT2026akio](https://www.wis-tns.org/object/2026akio) near Collinder 113 (CR113)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 113 (CR113) as this object's host. The 1.46002° (87.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:00:00Z · 15 days · 21.46 g |
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
| Subject | **Collinder 113 (CR113)** · `CR113` |
| Catalog display name | Collinder 113 (CR113) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 9.5 · 4.2′ × 4.2′ |
| Distance | 3.4 kpc |
| Separation | 1.46002° · 87.60′ |
| Catalog description | NGC 2266 is an open cluster of stars in the constellation of Gemini. It was discovered by German-British astronomer William Herschel on 7 December 1785. This is a relatively dim cluster with an integrated visual magnitude of 9.5 and an angular size of 5.0′. The stellar members can be readily resolved with an amateur telescope. NGC 2266 is located at a distance of 10,603 ly (3,251.0 pc) from the Sun. It is located close to the opposite part of the sky from the Galactic Center, or the anti-center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akio) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=102.465625%2026.911208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 169. [AT2026akjm](https://www.wis-tns.org/object/2026akjm) near IC240

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC240 as this object's host. The 1.07528° (64.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T08:10:54Z · 17 days · 20.64 g |
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
| Subject | **IC240** · `IC240` |
| Catalog display name | IC240 |
| Type / constellation | Nebula · Perseus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.07528° · 64.52′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=38.4271201%2042.1668956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 170. [AT2026akkg](https://www.wis-tns.org/object/2026akkg) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 1.07214° (64.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:16:48Z · 17 days · 21.86 r |
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
| Subject | **Gemini nebula** · `NGC 2371` |
| Catalog display name | Gemini nebula |
| Type / constellation | Planetary nebula · Gem |
| Catalog magnitude / angular size | — · 1.23′ × 0.9′ |
| Distance | — |
| Separation | 1.07214° · 64.33′ |
| Catalog description | NGC 2371-2 is a dual lobed planetary nebula located in the constellation Gemini. Visually, it appears like it could be two separate objects; therefore, two entries were given to the planetary nebula by John Louis Emil Dreyer in the New General Catalogue, so it may be referred to as NGC 2371, NGC 2372, or variations on this name. It has also been called the double bubble nebula. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.390958%2028.410931&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026akkl](https://www.wis-tns.org/object/2026akkl) near Eskimo or Clown Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Eskimo or Clown Nebula as this object's host. The 1.67199° (100.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:34:33Z · 15 days · 21.16 g |
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
| Subject | **Eskimo or Clown Nebula** · `C39` |
| Catalog display name | Eskimo or Clown Nebula |
| Type / constellation | Planetary nebula · Gemini |
| Catalog magnitude / angular size | 9.9 · 0.7′ × 0.2′ |
| Distance | 1.6 kpc |
| Separation | 1.67199° · 100.32′ |
| Catalog description | The Eskimo Nebula, also known as the Clown Face Nebula, Lion Nebula, or Caldwell 39, is a bipolar double-shell planetary nebula (PN). It was discovered by astronomer William Herschel in 1787. The formation resembles a person's head surrounded by a parka hood. It is surrounded by gas that composed the outer layers of a Sun-like star. The visible inner filaments are ejected by a strong wind of particles from the central star. The outer disk contains unusual, light-year-long filaments. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.010167%2022.083983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 172. [AT2026akkp](https://www.wis-tns.org/object/2026akkp) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.15866° (69.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:00:28Z · 14 days · 21.28 g |
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
| Subject | **NGC2901** · `NGC2901` |
| Catalog display name | NGC2901 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.15866° · 69.52′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.93175%2031.6365&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 173. [AT2026akkt](https://www.wis-tns.org/object/2026akkt) near NGC3180

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3180 as this object's host. The 1.53716° (92.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:17:45Z · 12 days · 20.11 g |
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
| Subject | **NGC3180** · `NGC3180` |
| Catalog display name | NGC3180 |
| Type / constellation | HII · Ursa Major |
| Catalog magnitude / angular size | — · 0.2′ × 0.2′ |
| Distance | — |
| Separation | 1.53716° · 92.23′ |
| Catalog description | NGC 3184, also known as The Little Pinwheel Galaxy, is an unbarred spiral galaxy approximately 40 million light-years away in the constellation Ursa Major. Its name comes from its resemblance to the Pinwheel Galaxy. It was discovered by German-British astronomer William Herschel on 18 March 1787. It has two HII regions named NGC 3180 and NGC 3181. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.89175%2042.60735&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 174. [AT2026akkv](https://www.wis-tns.org/object/2026akkv) near IC2610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2610 as this object's host. The 1.26969° (76.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:23:02Z · 12 days · 20.93 g |
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
| Subject | **IC2610** · `IC2610` |
| Catalog display name | IC2610 |
| Type / constellation | Nebula · Leo Minor |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.26969° · 76.18′ |
| Catalog description | very faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle, a single star 25" preceding (westward) / pretty (adv., before F. B. L, S) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.290708%2033.798217&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 175. [AT2026aknk](https://www.wis-tns.org/object/2026aknk) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.37344° (82.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-22T02:27:57Z · 4 days · 19.86 r |
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
| Separation | 1.37344° · 82.41′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aknk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.3172603%20-0.5982082&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 176. [AT2026aknl](https://www.wis-tns.org/object/2026aknl) near Messier 15 (M15)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 15 (M15) as this object's host. The 1.65930° (99.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:36:42Z · 23 days · 20.39 r |
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
| Subject | **Messier 15 (M15)** · `M15` |
| Catalog display name | Messier 15 (M15) |
| Type / constellation | Globular cluster · Pegasus |
| Catalog magnitude / angular size | 6.2 · 12.3′ × 12.3′ |
| Distance | 10.302 kpc |
| Separation | 1.65930° · 99.56′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=323.1201518%2010.743281&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 177. [AT2026aknm](https://www.wis-tns.org/object/2026aknm) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.68883° (101.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:10:04Z · 15 days · 23.05 g |
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
| Subject | **IC5248** · `IC5248` |
| Catalog display name | IC5248 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.68883° · 101.33′ |
| Catalog description | suspected (13.5 mag) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.664958%200.455619&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 178. [AT2026aknp](https://www.wis-tns.org/object/2026aknp) near NGC370

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC370 as this object's host. The 1.60098° (96.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:40:48Z · 12 days · 21.21 g |
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
| Subject | **NGC370** · `NGC370` |
| Catalog display name | NGC370 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.60098° · 96.06′ |
| Catalog description | NGC 370 is a triple star located in the constellation Pisces. It was recorded on October 7, 1861, by Heinrich d'Arrest. It was described by Dreyer as "very faint, 13th magnitude star 15 arcsec to south, diffuse." However, there is nothing there. It is now presumed to be either a lost or "non-existent" object, although it is possible it could be a duplication of NGC 372. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aknp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.457417%2033.656364&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 179. [AT2026akog](https://www.wis-tns.org/object/2026akog) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.58533° (95.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T05:45:39Z · 17 days · 23.18 i |
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
| Subject | **Robin's Egg Nebula** · `NGC 1360` |
| Catalog display name | Robin's Egg Nebula |
| Type / constellation | Planetary nebula · For |
| Catalog magnitude / angular size | — · 6′ × 4.5′ |
| Distance | — |
| Separation | 1.58533° · 95.12′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akog) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.792875%20-26.703333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 180. [AT2026akom](https://www.wis-tns.org/object/2026akom) near NGC3387

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3387 as this object's host. The 1.99594° (119.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T22:46:33Z · 16 days · 22.33 g |
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
| Subject | **NGC3387** · `NGC3387` |
| Catalog display name | NGC3387 |
| Type / constellation | Nebula · Sextans |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.99594° · 119.76′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akom) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.063333%204.992472&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 181. [AT2026akph](https://www.wis-tns.org/object/2026akph) near NGC2386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2386 as this object's host. The 1.92748° (115.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:27:21Z · 15 days · 21.04 g |
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
| Subject | **NGC2386** · `NGC2386` |
| Catalog display name | NGC2386 |
| Type / constellation | Nebula · Gemini |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.92748° · 115.65′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akph) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.269958%2035.558856&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 182. [AT2026akpk](https://www.wis-tns.org/object/2026akpk) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.87997° (112.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T18:14:24Z · 12 days · 21.74 g |
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
| Subject | **NGC2464** · `NGC2464` |
| Catalog display name | NGC2464 |
| Type / constellation | Nebula · Lynx |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.87997° · 112.80′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.804917%2058.368853&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 183. [AT2026akpo](https://www.wis-tns.org/object/2026akpo) near IC2170

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2170 as this object's host. The 1.35210° (81.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T21:31:40Z · 9 days · 20.77 g |
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
| Subject | **IC2170** · `IC2170` |
| Catalog display name | IC2170 |
| Type / constellation | Nebula · Auriga |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.35210° · 81.13′ |
| Catalog description | extremely, excessively faint, small in angular size, resolvable (mottled, not resolved), a star of 13th magnitude south preceding preceding (westward) / pretty (adv., before F. B. L, S) 0'.8 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akpo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.45375%2043.515667&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 184. [AT2026akqs](https://www.wis-tns.org/object/2026akqs) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.67892° (100.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T03:07:05Z · 16 days · 20.41 r |
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
| Subject | **IC5251** · `IC5251` |
| Catalog display name | IC5251 |
| Type / constellation | Nebula · Pegasus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.67892° · 100.74′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akqs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=340.4452106%209.7004615&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 185. [AT2026akrh](https://www.wis-tns.org/object/2026akrh) near NGC3097

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3097 as this object's host. The 1.61855° (97.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:29:16Z · 20 days · 21.05 g |
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
| Subject | **NGC3097** · `NGC3097` |
| Catalog display name | NGC3097 |
| Type / constellation | Nebula · Ursa Major |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.61855° · 97.11′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.689292%2058.7333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 186. [AT2026akrl](https://www.wis-tns.org/object/2026akrl) near Collinder 154 (CR154)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 154 (CR154) as this object's host. The 1.12325° (67.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:40:19Z · 15 days · 21.54 g |
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
| Separation | 1.12325° · 67.40′ |
| Catalog description | NGC 2420 is an open cluster in the constellation Gemini. It was discovered by German-British astronomer William Herschel on 19 November 1783. The cluster is about two billion years old and it is located 10,000 light years away. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akrl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=115.061083%2020.538139&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 187. [AT2026akro](https://www.wis-tns.org/object/2026akro) near IC 2237

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2237 as this object's host. The 1.50919° (90.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:11:31Z · 14 days · 22.27 g |
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
| Subject | **IC 2237** · `IC 2237` |
| Catalog display name | IC 2391 |
| Type / constellation | Star · Cnc |
| Catalog magnitude / angular size | — · 50′ × 50′ |
| Distance | 574 ly |
| Separation | 1.50919° · 90.55′ |
| Catalog description | IC 2391 is an open cluster in the constellation Vela consisting of hot, young, blueish stars, some of which are binaries and one of which is a quadruple. Persian astronomer A. a.-R. al-Sufi first described it as "a nebulous star" in c. 964. It was re-found by Abbe Lacaille and cataloged as Lac II 5. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2237 has the different designation IC 2391 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akro) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=122.755833%2026.014786&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 188. [AT2026aksv](https://www.wis-tns.org/object/2026aksv) near NGC3708

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3708 as this object's host. The 1.64139° (98.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T22:55:12Z · 8 days · 20.51 r |
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
| Subject | **NGC3708** · `NGC3708` |
| Catalog display name | NGC3708 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.64139° · 98.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aksv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=172.765583%20-1.584425&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 189. [AT2026aktb](https://www.wis-tns.org/object/2026aktb) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.25733° (75.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-23T14:51:21Z · 3 days · 21.39 r |
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
| Separation | 1.25733° · 75.44′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aktb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.297333%20-0.266722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 190. [AT2026aktm](https://www.wis-tns.org/object/2026aktm) near Collinder 113 (CR113)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 113 (CR113) as this object's host. The 1.01419° (60.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T19:39:21Z · 9 days · 21.38 g |
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
| Subject | **Collinder 113 (CR113)** · `CR113` |
| Catalog display name | Collinder 113 (CR113) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 9.5 · 4.2′ × 4.2′ |
| Distance | 3.4 kpc |
| Separation | 1.01419° · 60.85′ |
| Catalog description | NGC 2266 is an open cluster of stars in the constellation of Gemini. It was discovered by German-British astronomer William Herschel on 7 December 1785. This is a relatively dim cluster with an integrated visual magnitude of 9.5 and an angular size of 5.0′. The stellar members can be readily resolved with an amateur telescope. NGC 2266 is located at a distance of 10,603 ly (3,251.0 pc) from the Sun. It is located close to the opposite part of the sky from the Galactic Center, or the anti-center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.790208%2026.559603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 191. [AT2026akty](https://www.wis-tns.org/object/2026akty) near Collinder 144 (CR144)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 144 (CR144) as this object's host. The 1.33609° (80.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T10:19:40Z · 8 days · 19.79 i |
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
| Subject | **Collinder 144 (CR144)** · `CR144` |
| Catalog display name | Collinder 144 (CR144) |
| Type / constellation | Open cluster · Gemini |
| Catalog magnitude / angular size | 8 · 4.62′ × 4.62′ |
| Distance | 0.512 kpc |
| Separation | 1.33609° · 80.17′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akty) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.9316171%2014.93818&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 192. [AT2026akcp](https://www.wis-tns.org/object/2026akcp) near Lynds Bright Nebula 980 (LBN980)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 980 (LBN980) as this object's host. The 0.73350° (44.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T01:45:31Z · 9 days · 20.01 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4688....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4688....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 980 (LBN980)** · `LBN980` |
| Catalog display name | Lynds Bright Nebula 980 (LBN980) |
| Type / constellation | HII · Lepus |
| Catalog magnitude / angular size | — · 50′ × 12′ |
| Distance | — |
| Separation | 0.73350° · 44.01′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026akcp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.7544708%20-10.9811762&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 193. [SN2026agyr](https://www.wis-tns.org/object/2026agyr) near IC5061

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 33/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5061 as this object's host. The 1.57959° (94.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.055 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T04:34:07Z · 31 days · 18.99 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4321....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4321....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5061** · `IC5061` |
| Catalog display name | IC5061 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.57959° · 94.78′ |
| Catalog description | extremely, excessively faint, very small in angular size cluster; neb? |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=313.4837469%200.3459967&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 194. [SN2026adfc](https://www.wis-tns.org/object/2026adfc) near Lynds Bright Nebula 429 (LBN429)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 32/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 429 (LBN429) as this object's host. The 0.65958° (39.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.057903 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T06:55:47Z · 58 days · 18.97 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3917....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR3917....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 429 (LBN429)** · `LBN429` |
| Catalog display name | Lynds Bright Nebula 429 (LBN429) |
| Type / constellation | HII · Lacerta |
| Catalog magnitude / angular size | — · 100′ × 20′ |
| Distance | — |
| Separation | 0.65958° · 39.57′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026adfc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=336.8624514%2039.5211274&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 195. [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) near Lynds Bright Nebula 856 (LBN856)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 856 (LBN856) as this object's host. The 1.86938° (112.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T11:55:40Z · 14 days · 19.74 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4649....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4649....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 856 (LBN856)** · `LBN856` |
| Catalog display name | Lynds Bright Nebula 856 (LBN856) |
| Type / constellation | HII · Eridanus |
| Catalog magnitude / angular size | — · 15′ × 15′ |
| Distance | — |
| Separation | 1.86938° · 112.16′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajsa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.8570355%20-9.5882192&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026akjb](https://www.wis-tns.org/object/2026akjb) near Lynds Bright Nebula 896 (LBN896)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 896 (LBN896) as this object's host. The 1.22063° (73.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T10:13:26Z · 8 days · 21.26 w |
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
| Subject | **Lynds Bright Nebula 896 (LBN896)** · `LBN896` |
| Catalog display name | Lynds Bright Nebula 896 (LBN896) |
| Type / constellation | HII · Eridanus |
| Catalog magnitude / angular size | — · 40′ × 10′ |
| Distance | — |
| Separation | 1.22063° · 73.24′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akjb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.303419%20-7.3539019&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 197. [AT2026akme](https://www.wis-tns.org/object/2026akme) near Lynds Bright Nebula 693 (LBN693)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 693 (LBN693) as this object's host. The 1.56718° (94.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T10:19:56Z · 15 days · 20.72 r |
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
| Subject | **Lynds Bright Nebula 693 (LBN693)** · `LBN693` |
| Catalog display name | Lynds Bright Nebula 693 (LBN693) |
| Type / constellation | HII · Camelopardalis |
| Catalog magnitude / angular size | — · 90′ × 35′ |
| Distance | — |
| Separation | 1.56718° · 94.03′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akme) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=80.3466279%2064.782295&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 198. [AT2026akrp](https://www.wis-tns.org/object/2026akrp) near Lynds Bright Nebula 418 (LBN418)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 418 (LBN418) as this object's host. The 1.28863° (77.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T13:06:14Z · 8 days · 20.93 g |
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
| Subject | **Lynds Bright Nebula 418 (LBN418)** · `LBN418` |
| Catalog display name | Lynds Bright Nebula 418 (LBN418) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 200′ × 120′ |
| Distance | — |
| Separation | 1.28863° · 77.32′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akrp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.909458%2023.86375&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 199. [SN2026ahxw](https://www.wis-tns.org/object/2026ahxw) near Collinder 154 (CR154)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 20/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 154 (CR154) as this object's host. The 0.75676° (45.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.147 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T10:50:01Z · 37 days · 20.84 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4416....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4416....1S/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=115.2644247%2022.0068357&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 200. [SN2026aedz](https://www.wis-tns.org/object/2026aedz) near NGC1480

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1480 as this object's host. The 1.10868° (66.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIn |
| Redshift | 0.1222 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-03T09:32:37Z · 54 days · 19.78 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3981....1H](https://ui.adsabs.harvard.edu/abs/2026TNSTR3981....1H/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1480** · `NGC1480` |
| Catalog display name | NGC1480 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.10868° · 66.52′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aedz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.5876615%20-9.6708635&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 201. [SN2026agok](https://www.wis-tns.org/object/2026agok) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.64277° (98.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.13 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T22:23:31Z · 40 days · 19.99 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4256....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4256....1X/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Beehive cluster** · `CR189` |
| Catalog display name | Beehive cluster |
| Type / constellation | Open cluster · Cancer |
| Catalog magnitude / angular size | 3.1 · 108.6′ × 108.6′ |
| Distance | 0.187 kpc |
| Separation | 1.64277° · 98.57′ |
| Catalog description | (See Praesepe) |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agok) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=129.082042%2021.066014&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026aepc](https://www.wis-tns.org/object/2026aepc) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.76492° (105.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T12:36:55Z · 52 days · 19.7 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4017....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4017....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3319** · `NGC3319` |
| Catalog display name | NGC3319 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.4 · 3.63′ × 1.77′ |
| Distance | — |
| Separation | 1.76492° · 105.90′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aepc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.4886929%2042.120079&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 203. [AT2026akoy](https://www.wis-tns.org/object/2026akoy) near NGC2279

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 5/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2279 as this object's host. The 0.28704° (17.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-22T21:14:24Z · 35 days · 21.27 r |
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
| Subject | **NGC2279** · `NGC2279` |
| Catalog display name | NGC2279 |
| Type / constellation | Nebula · Gemini |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.28704° · 17.22′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akoy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=102.437875%2033.469147&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 204. [AT2026akjx](https://www.wis-tns.org/object/2026akjx) near IC132

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC132 as this object's host. The 1.66808° (100.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-21T21:07:12Z · 36 days · 21.13 r |
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
| Subject | **IC132** · `IC132` |
| Catalog display name | IC132 |
| Type / constellation | HII · Triangulum |
| Catalog magnitude / angular size | 14.8 · 0.67′ × 0.55′ |
| Distance | — |
| Separation | 1.66808° · 100.08′ |
| Catalog description | very faint, double a single star (13, 13) close |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.444042%2031.422531&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 205. [AT2026aktc](https://www.wis-tns.org/object/2026aktc) near NGC2284

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2284 as this object's host. The 1.82461° (109.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T21:37:26Z · 45 days · 21.16 r |
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
| Subject | **NGC2284** · `NGC2284` |
| Catalog display name | NGC2284 |
| Type / constellation | Nebula · Gemini |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.82461° · 109.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aktc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=104.432292%2033.541364&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
