# TNS transient opportunity review — 2026-11-10

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `c056e395d75f279b`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 339 review opportunities: 17 urgent, 322 watch, 0 expired
- Recommendations: 14 approve, 325 hold, 0 reject
- 339 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 840 staged rows collapsed to 784 unique TNS objects (56 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026agzo](https://www.wis-tns.org/object/2026agzo) | SN Ia | 17 | 18.14 | NGC3239 (Galaxy) | 0.15481° | near-field match | 100 | approve |
| urgent | [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) | SN Ia | 8 | 16.1 | NGC4216 (Galaxy) | 0.39324° | near-field match | 100 | approve |
| urgent | [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) | SN | 7 | 18.49 | IC 2405 (Galaxy) | 0.45056° | near-field match | 100 | hold |
| urgent | [AT2026aina](https://www.wis-tns.org/object/2026aina) | Nova | 4 | 13.8 | NGC2052 (Nebula) | 0.15398° | near-field match | 100 | approve |
| urgent | [SN2026agst](https://www.wis-tns.org/object/2026agst) | SN Ic-BL | 18 | 18.36 | NGC636 (Galaxy) | 1.79813° | near-field match | 90 | approve |
| urgent | [AT2026aicq](https://www.wis-tns.org/object/2026aicq) | transient_candidate | 6 | 18.48 | IC 369 (Galaxy) | 0.91864° | near-field match | 90 | hold |
| urgent | [AT2026aikg](https://www.wis-tns.org/object/2026aikg) | transient_candidate | 7 | 17.95 | NGC4414 (Galaxy) | 0.85966° | near-field match | 90 | approve |
| urgent | [AT2026aimo](https://www.wis-tns.org/object/2026aimo) | transient_candidate | 4 | 16.71 | NGC4691 (Galaxy) | 0.52514° | near-field match | 90 | approve |
| urgent | [AT2026aizp](https://www.wis-tns.org/object/2026aizp) | transient_candidate | 1 | 18.1 | Atoms For Peace Galaxy (Galaxy) | 0.49861° | near-field match | 90 | approve |
| urgent | [AT2026ajcp](https://www.wis-tns.org/object/2026ajcp) | transient_candidate | 0 | 17.76 | NGC 4517 (Galaxy) | 0.80621° | near-field match | 90 | approve |
| urgent | [SN2026aied](https://www.wis-tns.org/object/2026aied) | SN Ia | 7 | 18.33 | Lynds Bright Nebula 465 (LBN465) (HII) | 0.57960° | near-field match | 87 | approve |
| urgent | [AT2026ainb](https://www.wis-tns.org/object/2026ainb) | transient_candidate | 6 | 18.12 | IC 450 (Galaxy) | 1.07438° | near-field match | 83 | hold |
| urgent | [AT2026aisw](https://www.wis-tns.org/object/2026aisw) | transient_candidate | 4 | 18.02 | IC4946 (Galaxy) | 1.25863° | near-field match | 83 | approve |
| urgent | [AT2026aict](https://www.wis-tns.org/object/2026aict) | transient_candidate | 6 | 18.31 | Dumbbell Nebula (Planetary nebula) | 0.76955° | near-field match | 80 | approve |
| urgent | [AT2026aiuw](https://www.wis-tns.org/object/2026aiuw) | transient_candidate | 2 | 14.89 | Lynds Dark Nebula 637 (LDN637) (Dark nebula) | 1.17864° | near-field match | 75 | approve |
| urgent | [AT2026aiux](https://www.wis-tns.org/object/2026aiux) | transient_candidate | 2 | 17.29 | Lynds Dark Nebula 705 (LDN705) (Dark nebula) | 0.57543° | near-field match | 72 | approve |
| urgent | [AT2026ajcg](https://www.wis-tns.org/object/2026ajcg) | transient_candidate | 3 | 16.87 | Collinder 394 (CR394) (Open cluster) | 0.65272° | near-field match | 72 | approve |
| watch | [AT2026aikp](https://www.wis-tns.org/object/2026aikp) | transient_candidate | 6 | 19.14 | Great Nebula in Andromeda (Galaxy) | 0.10297° | near-field match | 93 | hold |
| watch | [AT2026aiol](https://www.wis-tns.org/object/2026aiol) | transient_candidate | 5 | 19.29 | IC1231 (Galaxy) | 0.00433° | near-field match | 93 | hold |
| watch | [SN2026ahze](https://www.wis-tns.org/object/2026ahze) | SN Ia | 7 | 18.71 | NGC797 (Galaxy) | 1.92283° | near-field match | 88 | hold |
| watch | [SN2026agwk](https://www.wis-tns.org/object/2026agwk) | SN Ia-91T-like | 15 | 19.32 | IC391 (Galaxy) | 0.40294° | near-field match | 87 | hold |
| watch | [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) | SN II | 9 | 18.71 | IC 3 (Spiral galaxy) | 0.47363° | near-field match | 87 | hold |
| watch | [AT2026aile](https://www.wis-tns.org/object/2026aile) | transient_candidate | 4 | 19.36 | NGC7471 (Nebula) | 0.21732° | near-field match | 83 | hold |
| watch | [SN2026aguc](https://www.wis-tns.org/object/2026aguc) | SN Ia-91T-like | 16 | 19.18 | IC382 (Galaxy) | 1.38071° | near-field match | 80 | hold |
| watch | [AT2026aijt](https://www.wis-tns.org/object/2026aijt) | transient_candidate | 7 | 19.16 | IC 673 (Galaxy) | 0.58117° | near-field match | 80 | hold |
| watch | [AT2026ainc](https://www.wis-tns.org/object/2026ainc) | transient_candidate | 6 | 19.14 | NGC 2742 (Galaxy) | 0.83545° | near-field match | 80 | hold |
| watch | [AT2026aitl](https://www.wis-tns.org/object/2026aitl) | transient_candidate | 6 | 19.38 | NGC3938 (Galaxy) | 0.67438° | near-field match | 80 | hold |
| watch | [AT2026aitv](https://www.wis-tns.org/object/2026aitv) | transient_candidate | 2 | 19.16 | NGC3887 (Galaxy) | 0.26253° | near-field match | 80 | hold |
| watch | [AT2026aiuv](https://www.wis-tns.org/object/2026aiuv) | transient_candidate | 2 | 18.64 | IC 897 (Galaxy) | 0.45434° | near-field match | 80 | hold |
| watch | [AT2026aiyr](https://www.wis-tns.org/object/2026aiyr) | transient_candidate | 3 | 19.34 | NGC2566 (Galaxy) | 0.87981° | near-field match | 80 | hold |
| watch | [AT2026ajcv](https://www.wis-tns.org/object/2026ajcv) | transient_candidate | 1 | 19.32 | IC 4297 (Galaxy) | 0.36926° | near-field match | 80 | hold |
| watch | [AT2026aivh](https://www.wis-tns.org/object/2026aivh) | transient_candidate | 7 | 18.75 | Lynds Bright Nebula 749 (LBN749) (HII) | 0.23181° | near-field match | 75 | hold |
| watch | [AT2026ahzg](https://www.wis-tns.org/object/2026ahzg) | transient_candidate | 7 | 18.77 | IC2152 (Galaxy) | 1.50611° | near-field match | 73 | hold |
| watch | [AT2026aijg](https://www.wis-tns.org/object/2026aijg) | transient_candidate | 4 | 19.19 | IC 5016 (Galaxy) | 1.00177° | near-field match | 73 | hold |
| watch | [AT2026aijv](https://www.wis-tns.org/object/2026aijv) | transient_candidate | 7 | 18.99 | NGC3521 (Galaxy) | 1.27193° | near-field match | 73 | hold |
| watch | [AT2026aioe](https://www.wis-tns.org/object/2026aioe) | transient_candidate | 3 | 18.57 | IC 1331 (Galaxy) | 1.19750° | near-field match | 73 | hold |
| watch | [AT2026aisl](https://www.wis-tns.org/object/2026aisl) | transient_candidate | 3 | 18.61 | IC575 (Galaxy) | 1.57115° | near-field match | 73 | hold |
| watch | [AT2026aiso](https://www.wis-tns.org/object/2026aiso) | transient_candidate | 4 | 19.36 | IC4951 (Galaxy) | 1.51398° | near-field match | 73 | hold |
| watch | [AT2026aita](https://www.wis-tns.org/object/2026aita) | transient_candidate | 2 | 21.27 | NGC1404 (Galaxy) | 0.21838° | near-field match | 73 | hold |
| watch | [AT2026aite](https://www.wis-tns.org/object/2026aite) | transient_candidate | 4 | 19.2 | IC 659 (Galaxy) | 1.35166° | near-field match | 73 | hold |
| watch | [AT2026aitn](https://www.wis-tns.org/object/2026aitn) | transient_candidate | 6 | 19.38 | NGC3414 (Galaxy) | 1.29435° | near-field match | 73 | hold |
| watch | [AT2026aive](https://www.wis-tns.org/object/2026aive) | transient_candidate | 2 | 18.74 | NGC2835 (Galaxy) | 1.04795° | near-field match | 73 | hold |
| watch | [AT2026aivf](https://www.wis-tns.org/object/2026aivf) | transient_candidate | 2 | 19.03 | NGC2835 (Galaxy) | 1.02455° | near-field match | 73 | hold |
| watch | [AT2026aizi](https://www.wis-tns.org/object/2026aizi) | transient_candidate | 5 | 18.92 | IC 4660 (Galaxy) | 1.33546° | near-field match | 73 | hold |
| watch | [AT2026ajbn](https://www.wis-tns.org/object/2026ajbn) | transient_candidate | 0 | 19.45 | NGC3189 (Galaxy) | 1.65719° | near-field match | 73 | hold |
| watch | [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) | transient_candidate | 11 | 19.31 | IC 2017 (Galaxy) | 0.36964° | near-field match | 72 | hold |
| watch | [AT2026aica](https://www.wis-tns.org/object/2026aica) | transient_candidate | 13 | 18.78 | IC1914 (Galaxy) | 0.56142° | near-field match | 72 | hold |
| watch | [SN2026agpk](https://www.wis-tns.org/object/2026agpk) | SN II | 18 | 18.85 | NGC2399 (Nebula) | 1.83747° | near-field match | 70 | hold |
| watch | [SN2026ahmz](https://www.wis-tns.org/object/2026ahmz) | SN II | 13 | 19.33 | IC2084 (Nebula) | 1.11286° | near-field match | 70 | hold |
| watch | [SN2026ahxo](https://www.wis-tns.org/object/2026ahxo) | SN Ia | 7 | 18.88 | Lynds Bright Nebula 484 (LBN484) (HII) | 1.59750° | near-field match | 70 | hold |
| watch | [AT2026aisv](https://www.wis-tns.org/object/2026aisv) | transient_candidate | 2 | 19.05 | Caldwell 87 (C87) (Globular cluster) | 0.51533° | near-field match | 70 | hold |
| watch | [SN2026agyk](https://www.wis-tns.org/object/2026agyk) | SN Ia | 15 | 18.8 | Barnard 152 (B152) (Dark nebula) | 0.73509° | near-field match | 69 | hold |
| watch | [SN2026aitx](https://www.wis-tns.org/object/2026aitx) | SN Ia | 2 | 19.57 | IC 2083 (Galaxy) | 1.14340° | near-field match | 68 | hold |
| watch | [AT2026ahab](https://www.wis-tns.org/object/2026ahab) | transient_candidate | 13 | 19.2 | IC 530 (Galaxy) | 1.84652° | near-field match | 65 | hold |
| watch | [AT2026ahch](https://www.wis-tns.org/object/2026ahch) | transient_candidate | 12 | 19.49 | NGC1792 (Galaxy) | 1.51662° | near-field match | 65 | hold |
| watch | [AT2026ahcr](https://www.wis-tns.org/object/2026ahcr) | transient_candidate | 13 | 19.43 | NGC7626 (Galaxy) | 1.62993° | near-field match | 65 | hold |
| watch | [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) | transient_candidate | 12 | 19.41 | IC1933 (Galaxy) | 1.58832° | near-field match | 65 | hold |
| watch | [AT2026aiaz](https://www.wis-tns.org/object/2026aiaz) | transient_candidate | 8 | 19.46 | NGC2655 (Galaxy) | 1.67391° | near-field match | 65 | hold |
| watch | [AT2026aiju](https://www.wis-tns.org/object/2026aiju) | transient_candidate | 12 | 19.02 | IC630 (Galaxy) | 1.80723° | near-field match | 65 | hold |
| watch | [AT2026aiql](https://www.wis-tns.org/object/2026aiql) | transient_candidate | 9 | 21.91 | IC1727 (Galaxy) | 0.16652° | near-field match | 65 | hold |
| watch | [AT2026aibq](https://www.wis-tns.org/object/2026aibq) | transient_candidate | 6 | 19.07 | NGC6669 (Nebula) | 1.81749° | near-field match | 63 | hold |
| watch | [AT2026aiep](https://www.wis-tns.org/object/2026aiep) | transient_candidate | 6 | 19.17 | IC5194 (Nebula) | 1.65298° | near-field match | 63 | hold |
| watch | [AT2026aihy](https://www.wis-tns.org/object/2026aihy) | transient_candidate | 5 | 19.5 | NGC56 (Nebula) | 1.97482° | near-field match | 63 | hold |
| watch | [AT2026aija](https://www.wis-tns.org/object/2026aija) | transient_candidate | 4 | 19.1 | NGC796 (Open cluster) | 1.18846° | near-field match | 63 | hold |
| watch | [AT2026aism](https://www.wis-tns.org/object/2026aism) | transient_candidate | 2 | 19.39 | IC1988 (Nebula) | 1.79403° | near-field match | 63 | hold |
| watch | [AT2026aitz](https://www.wis-tns.org/object/2026aitz) | transient_candidate | 4 | 19.86 | IC3009 (Nebula) | 0.16327° | near-field match | 63 | hold |
| watch | [AT2026aixw](https://www.wis-tns.org/object/2026aixw) | transient_candidate | 1 | 18.85 | IC877 (Nebula) | 1.87815° | near-field match | 63 | hold |
| watch | [AT2026aiyx](https://www.wis-tns.org/object/2026aiyx) | transient_candidate | 1 | 19.09 | IC5251 (Nebula) | 1.73252° | near-field match | 63 | hold |
| watch | [AT2026ajcc](https://www.wis-tns.org/object/2026ajcc) | transient_candidate | 1 | 18.82 | IC435 (reflection nebula) | 1.32248° | near-field match | 63 | hold |
| watch | [SN2026agua](https://www.wis-tns.org/object/2026agua) | SN Ia | 17 | 19.33 | Lynds Dark Nebula 1571 (LDN1571) (Dark nebula) | 1.07129° | near-field match | 62 | hold |
| watch | [SN2026agyt](https://www.wis-tns.org/object/2026agyt) | SN Ia | 13 | 18.99 | Lynds Bright Nebula 564 (LBN564) (HII) | 1.14138° | near-field match | 62 | hold |
| watch | [AT2026aiap](https://www.wis-tns.org/object/2026aiap) | transient_candidate | 7 | 18.98 | Lynds Bright Nebula 437 (LBN437) (HII) | 0.83711° | near-field match | 62 | hold |
| watch | [AT2026aimb](https://www.wis-tns.org/object/2026aimb) | transient_candidate | 4 | 19.3 | Lynds Bright Nebula 703 (LBN703) (HII) | 0.99979° | near-field match | 62 | hold |
| watch | [AT2026aivb](https://www.wis-tns.org/object/2026aivb) | transient_candidate | 3 | 19.04 | Lynds Dark Nebula 387 (LDN387) (Dark nebula) | 0.97429° | near-field match | 62 | hold |
| watch | [SN2026afvg](https://www.wis-tns.org/object/2026afvg) | SN Ia | 23 | 20.34 | IC 1931 (Galaxy) | 1.30858° | near-field match | 60 | hold |
| watch | [AT2026aicj](https://www.wis-tns.org/object/2026aicj) | transient_candidate | 6 | 20.1 | IC1531 (Galaxy) | 0.49233° | near-field match | 60 | hold |
| watch | [AT2026aiij](https://www.wis-tns.org/object/2026aiij) | transient_candidate | 4 | 23.51 | IC2000 (Galaxy) | 0.81942° | near-field match | 60 | hold |
| watch | [AT2026aike](https://www.wis-tns.org/object/2026aike) | transient_candidate | 4 | 22.75 | NGC1543 (Galaxy) | 0.28536° | near-field match | 60 | hold |
| watch | [AT2026aikf](https://www.wis-tns.org/object/2026aikf) | transient_candidate | 4 | 21.83 | NGC1543 (Galaxy) | 0.39139° | near-field match | 60 | hold |
| watch | [AT2026aiki](https://www.wis-tns.org/object/2026aiki) | transient_candidate | 4 | 20.27 | IC 230 (Galaxy) | 0.98313° | near-field match | 60 | hold |
| watch | [AT2026ainz](https://www.wis-tns.org/object/2026ainz) | transient_candidate | 6 | 20.23 | NGC7418 (Galaxy) | 0.82463° | near-field match | 60 | hold |
| watch | [AT2026aiob](https://www.wis-tns.org/object/2026aiob) | transient_candidate | 7 | 19.57 | NGC4036 (Galaxy) | 0.77482° | near-field match | 60 | hold |
| watch | [AT2026airb](https://www.wis-tns.org/object/2026airb) | transient_candidate | 7 | 21.04 | NGC7741 (Galaxy) | 0.69274° | near-field match | 60 | hold |
| watch | [AT2026airq](https://www.wis-tns.org/object/2026airq) | transient_candidate | 4 | 23.72 | NGC1527 (Galaxy) | 0.66655° | near-field match | 60 | hold |
| watch | [AT2026aisu](https://www.wis-tns.org/object/2026aisu) | transient_candidate | 2 | 19.52 | IC5181 (Galaxy) | 0.85860° | near-field match | 60 | hold |
| watch | [AT2026aisx](https://www.wis-tns.org/object/2026aisx) | transient_candidate | 2 | 21.65 | Fornax B (Galaxy) | 0.65992° | near-field match | 60 | hold |
| watch | [AT2026aisy](https://www.wis-tns.org/object/2026aisy) | transient_candidate | 2 | 22.37 | Fornax A (Galaxy) | 0.92416° | near-field match | 60 | hold |
| watch | [AT2026aitc](https://www.wis-tns.org/object/2026aitc) | transient_candidate | 2 | 22.01 | NGC1427 (Galaxy) | 0.53248° | near-field match | 60 | hold |
| watch | [AT2026aitj](https://www.wis-tns.org/object/2026aitj) | transient_candidate | 7 | 20.29 | NGC4062 (Galaxy) | 0.40955° | near-field match | 60 | hold |
| watch | [AT2026aitm](https://www.wis-tns.org/object/2026aitm) | transient_candidate | 6 | 19.81 | NGC3675 (Galaxy) | 0.94795° | near-field match | 60 | hold |
| watch | [AT2026aito](https://www.wis-tns.org/object/2026aito) | transient_candidate | 6 | 20.21 | NGC 3294 (Galaxy) | 0.37031° | near-field match | 60 | hold |
| watch | [AT2026aitt](https://www.wis-tns.org/object/2026aitt) | transient_candidate | 4 | 19.93 | IC 739 (Galaxy) | 0.95329° | near-field match | 60 | hold |
| watch | [AT2026aiup](https://www.wis-tns.org/object/2026aiup) | transient_candidate | 7 | 20.72 | IC148 (Galaxy) | 0.32866° | near-field match | 60 | hold |
| watch | [AT2026aivt](https://www.wis-tns.org/object/2026aivt) | transient_candidate | 7 | 22.44 | NGC864 (Galaxy) | 0.37622° | near-field match | 60 | hold |
| watch | [AT2026aivv](https://www.wis-tns.org/object/2026aivv) | transient_candidate | 5 | 22.66 | IC 173 (Galaxy) | 0.25518° | near-field match | 60 | hold |
| watch | [AT2026aiwb](https://www.wis-tns.org/object/2026aiwb) | transient_candidate | 3 | 22.88 | Darth Vader's Galaxy (Galaxy) | 0.88875° | near-field match | 60 | hold |
| watch | [AT2026aiwc](https://www.wis-tns.org/object/2026aiwc) | transient_candidate | 3 | 22.4 | Darth Vader's Galaxy (Galaxy) | 0.41006° | near-field match | 60 | hold |
| watch | [AT2026aixg](https://www.wis-tns.org/object/2026aixg) | transient_candidate | 5 | 20.63 | IC1895 (Galaxy) | 0.41742° | near-field match | 60 | hold |
| watch | [AT2026aiyg](https://www.wis-tns.org/object/2026aiyg) | transient_candidate | 1 | 20.21 | IC2135 (Galaxy) | 0.98727° | near-field match | 60 | hold |
| watch | [AT2026aiyy](https://www.wis-tns.org/object/2026aiyy) | transient_candidate | 4 | 19.87 | NGC7457 (Galaxy) | 0.53496° | near-field match | 60 | hold |
| watch | [AT2026ajar](https://www.wis-tns.org/object/2026ajar) | transient_candidate | 3 | 19.82 | NGC3169 (Galaxy) | 0.74868° | near-field match | 60 | hold |
| watch | [AT2026ajbh](https://www.wis-tns.org/object/2026ajbh) | transient_candidate | 1 | 19.94 | IC302 (Galaxy) | 0.86924° | near-field match | 60 | hold |
| watch | [AT2026ajbz](https://www.wis-tns.org/object/2026ajbz) | transient_candidate | 7 | 20.81 | IC163 (Galaxy) | 0.66373° | near-field match | 60 | hold |
| watch | [SN2026ahyd](https://www.wis-tns.org/object/2026ahyd) | SN Ia | 7 | 19.53 | IC5366 (Nebula) | 1.01813° | near-field match | 58 | hold |
| watch | [SN2026agpt](https://www.wis-tns.org/object/2026agpt) | SN Ia | 21 | 20.26 | IC353 (Nebula) | 0.25824° | near-field match | 57 | hold |
| watch | [SN2026ahru](https://www.wis-tns.org/object/2026ahru) | SN Ia | 10 | 20.33 | IC1376 (Nebula) | 0.31912° | near-field match | 57 | hold |
| watch | [AT2026aiba](https://www.wis-tns.org/object/2026aiba) | transient_candidate | 8 | 19 | NGC2404 (HII) | 1.36391° | near-field match | 55 | hold |
| watch | [AT2026aibu](https://www.wis-tns.org/object/2026aibu) | transient_candidate | 17 | 19.47 | IC640 (Nebula) | 1.43879° | near-field match | 55 | hold |
| watch | [AT2026ailu](https://www.wis-tns.org/object/2026ailu) | transient_candidate | 15 | 18.89 | IC1140 (Nebula) | 1.65700° | near-field match | 55 | hold |
| watch | [AT2026aimn](https://www.wis-tns.org/object/2026aimn) | transient_candidate | 4 | 19.23 | van den Bergh 29 (VDB29) (Nebula) | 1.12187° | near-field match | 55 | hold |
| watch | [AT2026airn](https://www.wis-tns.org/object/2026airn) | transient_candidate | 3 | 18.52 | Barnard 224 (B224) (Dark nebula) | 1.10477° | near-field match | 55 | hold |
| watch | [AT2026aizl](https://www.wis-tns.org/object/2026aizl) | transient_candidate | 3 | 18.61 | Lynds Dark Nebula 1563 (LDN1563) (Dark nebula) | 1.36769° | near-field match | 55 | hold |
| watch | [AT2026aizq](https://www.wis-tns.org/object/2026aizq) | transient_candidate | 1 | 18.67 | Lynds Bright Nebula 54 (LBN54) (HII) | 1.56600° | near-field match | 55 | hold |
| watch | [AT2026aiar](https://www.wis-tns.org/object/2026aiar) | transient_candidate | 7 | 20.11 | NGC 2207 / IC 2163 (Galaxy) | 1.27730° | near-field match | 53 | hold |
| watch | [AT2026aibw](https://www.wis-tns.org/object/2026aibw) | transient_candidate | 6 | 19.69 | NGC 2207 / IC 2163 (Galaxy) | 1.77222° | near-field match | 53 | hold |
| watch | [AT2026aick](https://www.wis-tns.org/object/2026aick) | transient_candidate | 6 | 19.75 | NGC7410 (Galaxy) | 1.11442° | near-field match | 53 | hold |
| watch | [AT2026aicx](https://www.wis-tns.org/object/2026aicx) | transient_candidate | 7 | 20.09 | IC 21 (Galaxy) | 1.65583° | near-field match | 53 | hold |
| watch | [AT2026aidv](https://www.wis-tns.org/object/2026aidv) | transient_candidate | 5 | 19.73 | IC 5298 (Galaxy) | 1.04272° | near-field match | 53 | hold |
| watch | [AT2026aiin](https://www.wis-tns.org/object/2026aiin) | transient_candidate | 7 | 20.59 | NGC1084 (Galaxy) | 1.58124° | near-field match | 53 | hold |
| watch | [AT2026aijo](https://www.wis-tns.org/object/2026aijo) | transient_candidate | 5 | 20.25 | NGC1055 (Galaxy) | 1.04248° | near-field match | 53 | hold |
| watch | [AT2026aijx](https://www.wis-tns.org/object/2026aijx) | transient_candidate | 4 | 21.8 | NGC1527 (Galaxy) | 1.48110° | near-field match | 53 | hold |
| watch | [AT2026aika](https://www.wis-tns.org/object/2026aika) | transient_candidate | 7 | 20.36 | IC 1776 (Galaxy) | 1.83590° | near-field match | 53 | hold |
| watch | [AT2026aikq](https://www.wis-tns.org/object/2026aikq) | transient_candidate | 7 | 20.18 | NGC 4150 (Galaxy) | 1.54182° | near-field match | 53 | hold |
| watch | [AT2026aikv](https://www.wis-tns.org/object/2026aikv) | transient_candidate | 7 | 20.5 | NGC628 (Galaxy) | 1.77250° | near-field match | 53 | hold |
| watch | [AT2026aikw](https://www.wis-tns.org/object/2026aikw) | transient_candidate | 7 | 20.06 | IC 186 A (Galaxy) | 1.01615° | near-field match | 53 | hold |
| watch | [AT2026aikx](https://www.wis-tns.org/object/2026aikx) | transient_candidate | 5 | 20.65 | IC 1730 (Galaxy) | 1.43755° | near-field match | 53 | hold |
| watch | [AT2026aikz](https://www.wis-tns.org/object/2026aikz) | transient_candidate | 6 | 19.88 | Arp 147 (Galaxy) | 1.07092° | near-field match | 53 | hold |
| watch | [AT2026ailf](https://www.wis-tns.org/object/2026ailf) | transient_candidate | 4 | 20.95 | IC5338 (Galaxy) | 1.89253° | near-field match | 53 | hold |
| watch | [AT2026ailh](https://www.wis-tns.org/object/2026ailh) | transient_candidate | 4 | 21.27 | IC 16 (Galaxy) | 1.81588° | near-field match | 53 | hold |
| watch | [AT2026ainl](https://www.wis-tns.org/object/2026ainl) | transient_candidate | 7 | 19.67 | IC 2973 (Galaxy) | 1.85833° | near-field match | 53 | hold |
| watch | [AT2026aiod](https://www.wis-tns.org/object/2026aiod) | transient_candidate | 5 | 20.35 | IC 17 (Galaxy) | 1.30850° | near-field match | 53 | hold |
| watch | [AT2026aion](https://www.wis-tns.org/object/2026aion) | transient_candidate | 7 | 20.12 | Silver Sliver Galaxy (Galaxy) | 1.67303° | near-field match | 53 | hold |
| watch | [AT2026aior](https://www.wis-tns.org/object/2026aior) | transient_candidate | 7 | 22.61 | NGC488 (Galaxy) | 1.68195° | near-field match | 53 | hold |
| watch | [AT2026airi](https://www.wis-tns.org/object/2026airi) | transient_candidate | 3 | 20.14 | NGC636 (Galaxy) | 1.79687° | near-field match | 53 | hold |
| watch | [AT2026airp](https://www.wis-tns.org/object/2026airp) | transient_candidate | 5 | 20 | IC1734 (Galaxy) | 1.46402° | near-field match | 53 | hold |
| watch | [AT2026airu](https://www.wis-tns.org/object/2026airu) | transient_candidate | 2 | 21.49 | IC5065 (Galaxy) | 1.63610° | near-field match | 53 | hold |
| watch | [AT2026aisb](https://www.wis-tns.org/object/2026aisb) | transient_candidate | 2 | 23.29 | IC2000 (Galaxy) | 1.38375° | near-field match | 53 | hold |
| watch | [AT2026aisz](https://www.wis-tns.org/object/2026aisz) | transient_candidate | 2 | 21.06 | IC 1906 (Galaxy) | 1.46114° | near-field match | 53 | hold |
| watch | [AT2026aitb](https://www.wis-tns.org/object/2026aitb) | transient_candidate | 2 | 21.49 | NGC1350 (Galaxy) | 1.28617° | near-field match | 53 | hold |
| watch | [AT2026aiua](https://www.wis-tns.org/object/2026aiua) | transient_candidate | 5 | 20.14 | Caldwell 48 (C48) (Galaxy) | 1.07394° | near-field match | 53 | hold |
| watch | [AT2026aiue](https://www.wis-tns.org/object/2026aiue) | transient_candidate | 5 | 20.32 | IC 1417 (Galaxy) | 1.53875° | near-field match | 53 | hold |
| watch | [AT2026aiun](https://www.wis-tns.org/object/2026aiun) | transient_candidate | 7 | 20.54 | IC 1757 (Galaxy) | 1.41669° | near-field match | 53 | hold |
| watch | [AT2026aius](https://www.wis-tns.org/object/2026aius) | transient_candidate | 4 | 19.94 | NGC797 (Galaxy) | 1.88178° | near-field match | 53 | hold |
| watch | [AT2026aivi](https://www.wis-tns.org/object/2026aivi) | transient_candidate | 7 | 19.82 | IC 1797 (Galaxy) | 1.40546° | near-field match | 53 | hold |
| watch | [AT2026aivw](https://www.wis-tns.org/object/2026aivw) | transient_candidate | 5 | 21.91 | IC 1757 (Galaxy) | 1.24572° | near-field match | 53 | hold |
| watch | [AT2026aiwu](https://www.wis-tns.org/object/2026aiwu) | transient_candidate | 4 | 20.14 | IC 1568 (Galaxy) | 1.34453° | near-field match | 53 | hold |
| watch | [AT2026aixb](https://www.wis-tns.org/object/2026aixb) | transient_candidate | 1 | 20.2 | IC1508 (Galaxy) | 1.64877° | near-field match | 53 | hold |
| watch | [AT2026aiye](https://www.wis-tns.org/object/2026aiye) | transient_candidate | 3 | 19.93 | IC1616 (Galaxy) | 1.28647° | near-field match | 53 | hold |
| watch | [AT2026aiyh](https://www.wis-tns.org/object/2026aiyh) | transient_candidate | 5 | 20.26 | IC2152 (Galaxy) | 1.16508° | near-field match | 53 | hold |
| watch | [AT2026aizb](https://www.wis-tns.org/object/2026aizb) | transient_candidate | 2 | 20.76 | IC 1776 (Galaxy) | 1.97947° | near-field match | 53 | hold |
| watch | [AT2026ajbj](https://www.wis-tns.org/object/2026ajbj) | transient_candidate | 1 | 20.17 | IC2007 (Galaxy) | 1.79494° | near-field match | 53 | hold |
| watch | [AT2026ajbo](https://www.wis-tns.org/object/2026ajbo) | transient_candidate | 0 | 19.95 | NGC 4346 (Galaxy) | 1.29956° | near-field match | 53 | hold |
| watch | [AT2026ajbr](https://www.wis-tns.org/object/2026ajbr) | transient_candidate | 7 | 20.52 | NGC2841 (Galaxy) | 1.54687° | near-field match | 53 | hold |
| watch | [AT2026ajbw](https://www.wis-tns.org/object/2026ajbw) | transient_candidate | 1 | 20.02 | IC 632 (Galaxy) | 1.68563° | near-field match | 53 | hold |
| watch | [AT2026ajby](https://www.wis-tns.org/object/2026ajby) | transient_candidate | 1 | 20.2 | IC48 (Galaxy) | 1.83970° | near-field match | 53 | hold |
| watch | [AT2026ajcl](https://www.wis-tns.org/object/2026ajcl) | transient_candidate | 5 | 20.82 | IC 1873 (Galaxy) | 1.66353° | near-field match | 53 | hold |
| watch | [AT2026ajcz](https://www.wis-tns.org/object/2026ajcz) | transient_candidate | 6 | 19.92 | NGC3319 (Galaxy) | 1.96765° | near-field match | 53 | hold |
| watch | [AT2026ahsf](https://www.wis-tns.org/object/2026ahsf) | transient_candidate | 11 | 20.36 | IC1892 (Galaxy) | 0.43473° | near-field match | 52 | hold |
| watch | [AT2026ahsm](https://www.wis-tns.org/object/2026ahsm) | transient_candidate | 13 | 19.9 | IC1796 (Galaxy) | 0.47424° | near-field match | 52 | hold |
| watch | [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) | transient_candidate | 9 | 19.59 | IC1933 (Galaxy) | 0.59209° | near-field match | 52 | hold |
| watch | [AT2026aiax](https://www.wis-tns.org/object/2026aiax) | transient_candidate | 11 | 22.27 | NGC1527 (Galaxy) | 0.49618° | near-field match | 52 | hold |
| watch | [AT2026aibf](https://www.wis-tns.org/object/2026aibf) | transient_candidate | 24 | 21.48 | IC1784 (Galaxy) | 0.51346° | near-field match | 52 | hold |
| watch | [AT2026aimu](https://www.wis-tns.org/object/2026aimu) | transient_candidate | 11 | 20.91 | NGC7585 (Galaxy) | 0.67498° | near-field match | 52 | hold |
| watch | [AT2026aimv](https://www.wis-tns.org/object/2026aimv) | transient_candidate | 11 | 21.54 | IC1495 (Galaxy) | 0.99831° | near-field match | 52 | hold |
| watch | [AT2026ains](https://www.wis-tns.org/object/2026ains) | transient_candidate | 17 | 19.94 | NGC1961 (Galaxy) | 0.68080° | near-field match | 52 | hold |
| watch | [AT2026aipd](https://www.wis-tns.org/object/2026aipd) | transient_candidate | 13 | 21.22 | IC 1746 (Galaxy) | 0.30858° | near-field match | 52 | hold |
| watch | [AT2026aiph](https://www.wis-tns.org/object/2026aiph) | transient_candidate | 9 | 22.48 | Caldwell 51 (C51) (Galaxy) | 0.47650° | near-field match | 52 | hold |
| watch | [AT2026aivo](https://www.wis-tns.org/object/2026aivo) | transient_candidate | 9 | 22.3 | NGC864 (Galaxy) | 0.76363° | near-field match | 52 | hold |
| watch | [AT2026aixe](https://www.wis-tns.org/object/2026aixe) | transient_candidate | 12 | 20.05 | IC1860 (Galaxy) | 0.49089° | near-field match | 52 | hold |
| watch | [AT2026aiyi](https://www.wis-tns.org/object/2026aiyi) | transient_candidate | 12 | 20.5 | IC1628 (Galaxy) | 0.47290° | near-field match | 52 | hold |
| watch | [AT2026ajai](https://www.wis-tns.org/object/2026ajai) | transient_candidate | 11 | 22.25 | NGC741 (Galaxy) | 0.59906° | near-field match | 52 | hold |
| watch | [AT2026ajaj](https://www.wis-tns.org/object/2026ajaj) | transient_candidate | 11 | 22.02 | IC 1757 (Galaxy) | 0.93441° | near-field match | 52 | hold |
| watch | [AT2026ajax](https://www.wis-tns.org/object/2026ajax) | transient_candidate | 29 | 21.28 | IC509 (Galaxy) | 0.40100° | near-field match | 52 | hold |
| watch | [AT2026aiko](https://www.wis-tns.org/object/2026aiko) | transient_candidate | 4 | 19.85 | NGC7158 (Nebula) | 0.38099° | near-field match | 50 | hold |
| watch | [AT2026aimh](https://www.wis-tns.org/object/2026aimh) | transient_candidate | 4 | 20.12 | IC488 (Nebula) | 0.45906° | near-field match | 50 | hold |
| watch | [AT2026aiog](https://www.wis-tns.org/object/2026aiog) | transient_candidate | 7 | 20.42 | Cleopatra's eye (Planetary nebula) | 0.80675° | near-field match | 50 | hold |
| watch | [AT2026aisd](https://www.wis-tns.org/object/2026aisd) | transient_candidate | 2 | 23.49 | IC2055 (Nebula) | 0.36810° | near-field match | 50 | hold |
| watch | [AT2026aisr](https://www.wis-tns.org/object/2026aisr) | transient_candidate | 4 | 19.69 | NGC1900 (Open cluster) | 0.38063° | near-field match | 50 | hold |
| watch | [AT2026aivj](https://www.wis-tns.org/object/2026aivj) | transient_candidate | 5 | 20.47 | IC1547 (Nebula) | 0.56565° | near-field match | 50 | hold |
| watch | [AT2026aiwl](https://www.wis-tns.org/object/2026aiwl) | transient_candidate | 4 | 20.35 | IC5344 (Nebula) | 0.90611° | near-field match | 50 | hold |
| watch | [AT2026aiws](https://www.wis-tns.org/object/2026aiws) | transient_candidate | 5 | 20.91 | Collinder 59 (CR59) (Open cluster) | 0.80866° | near-field match | 50 | hold |
| watch | [AT2026aixd](https://www.wis-tns.org/object/2026aixd) | transient_candidate | 5 | 20 | NGC7826 (Nebula) | 0.88575° | near-field match | 50 | hold |
| watch | [AT2026ajan](https://www.wis-tns.org/object/2026ajan) | transient_candidate | 6 | 22.15 | NGC7668 (Nebula) | 0.77578° | near-field match | 50 | hold |
| watch | [AT2026ajdc](https://www.wis-tns.org/object/2026ajdc) | transient_candidate | 7 | 19.73 | IC240 (Nebula) | 0.55882° | near-field match | 50 | hold |
| watch | [AT2026ahnp](https://www.wis-tns.org/object/2026ahnp) | transient_candidate | 12 | 18.54 | Sharpless 122 (SH2-122) (HII) | 1.14210° | near-field match | 47 | hold |
| watch | [AT2026afve](https://www.wis-tns.org/object/2026afve) | transient_candidate | 23 | 20.21 | IC 1931 (Galaxy) | 1.91599° | near-field match | 45 | hold |
| watch | [AT2026agyb](https://www.wis-tns.org/object/2026agyb) | transient_candidate | 14 | 19.63 | IC5201 (Galaxy) | 1.07201° | near-field match | 45 | hold |
| watch | [AT2026ahbv](https://www.wis-tns.org/object/2026ahbv) | transient_candidate | 13 | 19.86 | IC1495 (Galaxy) | 1.53637° | near-field match | 45 | hold |
| watch | [AT2026ahdm](https://www.wis-tns.org/object/2026ahdm) | transient_candidate | 13 | 21.64 | IC 1507 (Galaxy) | 1.56833° | near-field match | 45 | hold |
| watch | [AT2026ahho](https://www.wis-tns.org/object/2026ahho) | transient_candidate | 11 | 21.9 | IC1495 (Galaxy) | 1.70871° | near-field match | 45 | hold |
| watch | [AT2026ahhy](https://www.wis-tns.org/object/2026ahhy) | transient_candidate | 11 | 21.58 | NGC7606 (Galaxy) | 1.55641° | near-field match | 45 | hold |
| watch | [AT2026ahiv](https://www.wis-tns.org/object/2026ahiv) | transient_candidate | 11 | 22.17 | IC1495 (Galaxy) | 1.93793° | near-field match | 45 | hold |
| watch | [AT2026aibd](https://www.wis-tns.org/object/2026aibd) | transient_candidate | 13 | 21.48 | NGC741 (Galaxy) | 1.35024° | near-field match | 45 | hold |
| watch | [AT2026aibz](https://www.wis-tns.org/object/2026aibz) | transient_candidate | 15 | 19.66 | IC334 (Galaxy) | 1.51904° | near-field match | 45 | hold |
| watch | [AT2026aicm](https://www.wis-tns.org/object/2026aicm) | transient_candidate | 9 | 19.97 | IC 2039 (Galaxy) | 1.00001° | near-field match | 45 | hold |
| watch | [AT2026aico](https://www.wis-tns.org/object/2026aico) | transient_candidate | 13 | 19.65 | IC 33 (Galaxy) | 1.03221° | near-field match | 45 | hold |
| watch | [AT2026aicp](https://www.wis-tns.org/object/2026aicp) | transient_candidate | 13 | 20.02 | IC5270 (Galaxy) | 1.45156° | near-field match | 45 | hold |
| watch | [AT2026aicw](https://www.wis-tns.org/object/2026aicw) | transient_candidate | 12 | 19.96 | IC1574 (Galaxy) | 1.16063° | near-field match | 45 | hold |
| watch | [AT2026aieg](https://www.wis-tns.org/object/2026aieg) | transient_candidate | 11 | 21.47 | IC1495 (Galaxy) | 1.01519° | near-field match | 45 | hold |
| watch | [AT2026aigp](https://www.wis-tns.org/object/2026aigp) | transient_candidate | 9 | 19.83 | IC2007 (Galaxy) | 1.25561° | near-field match | 45 | hold |
| watch | [AT2026aihe](https://www.wis-tns.org/object/2026aihe) | transient_candidate | 9 | 19.64 | NGC2855 (Galaxy) | 1.17126° | near-field match | 45 | hold |
| watch | [AT2026aiit](https://www.wis-tns.org/object/2026aiit) | transient_candidate | 15 | 20.1 | IC 536 (Galaxy) | 1.35010° | near-field match | 45 | hold |
| watch | [AT2026aiiu](https://www.wis-tns.org/object/2026aiiu) | transient_candidate | 12 | 20.2 | IC1729 (Galaxy) | 1.95901° | near-field match | 45 | hold |
| watch | [AT2026aiiw](https://www.wis-tns.org/object/2026aiiw) | transient_candidate | 9 | 19.98 | IC5325 (Galaxy) | 1.36152° | near-field match | 45 | hold |
| watch | [AT2026aijz](https://www.wis-tns.org/object/2026aijz) | transient_candidate | 8 | 19.8 | IC522 (Galaxy) | 1.16708° | near-field match | 45 | hold |
| watch | [AT2026aikd](https://www.wis-tns.org/object/2026aikd) | transient_candidate | 11 | 20.95 | NGC7606 (Galaxy) | 1.84563° | near-field match | 45 | hold |
| watch | [AT2026aimy](https://www.wis-tns.org/object/2026aimy) | transient_candidate | 11 | 21.54 | IC 1507 (Galaxy) | 1.81739° | near-field match | 45 | hold |
| watch | [AT2026aine](https://www.wis-tns.org/object/2026aine) | transient_candidate | 14 | 19.68 | Caldwell 48 (C48) (Galaxy) | 1.77858° | near-field match | 45 | hold |
| watch | [AT2026aint](https://www.wis-tns.org/object/2026aint) | transient_candidate | 15 | 19.89 | NGC3631 (Galaxy) | 1.58810° | near-field match | 45 | hold |
| watch | [AT2026ainu](https://www.wis-tns.org/object/2026ainu) | transient_candidate | 8 | 19.94 | NGC1637 (Galaxy) | 1.60149° | near-field match | 45 | hold |
| watch | [AT2026aioc](https://www.wis-tns.org/object/2026aioc) | transient_candidate | 14 | 19.92 | NGC205 (Galaxy) | 1.85287° | near-field match | 45 | hold |
| watch | [AT2026aios](https://www.wis-tns.org/object/2026aios) | transient_candidate | 12 | 22.19 | IC 5374 (Galaxy) | 1.32538° | near-field match | 45 | hold |
| watch | [AT2026aipc](https://www.wis-tns.org/object/2026aipc) | transient_candidate | 9 | 21.55 | IC 1757 (Galaxy) | 1.38724° | near-field match | 45 | hold |
| watch | [AT2026aipi](https://www.wis-tns.org/object/2026aipi) | transient_candidate | 9 | 21.97 | IC 74 (Galaxy) | 1.59561° | near-field match | 45 | hold |
| watch | [AT2026aipl](https://www.wis-tns.org/object/2026aipl) | transient_candidate | 9 | 22.31 | IC 1746 (Galaxy) | 1.98515° | near-field match | 45 | hold |
| watch | [AT2026aipm](https://www.wis-tns.org/object/2026aipm) | transient_candidate | 8 | 22.66 | IC 1481 (Galaxy) | 1.50924° | near-field match | 45 | hold |
| watch | [AT2026aipu](https://www.wis-tns.org/object/2026aipu) | transient_candidate | 24 | 21.76 | NGC 2782 (Galaxy) | 1.33199° | near-field match | 45 | hold |
| watch | [AT2026aiqc](https://www.wis-tns.org/object/2026aiqc) | transient_candidate | 14 | 20.5 | NGC2859 (Galaxy) | 1.88260° | near-field match | 45 | hold |
| watch | [AT2026aiqd](https://www.wis-tns.org/object/2026aiqd) | transient_candidate | 14 | 21.04 | NGC 2782 (Galaxy) | 1.42815° | near-field match | 45 | hold |
| watch | [AT2026aiqe](https://www.wis-tns.org/object/2026aiqe) | transient_candidate | 13 | 20.53 | Andromeda Galaxy (Galaxy) | 1.66342° | near-field match | 45 | hold |
| watch | [AT2026aiqm](https://www.wis-tns.org/object/2026aiqm) | transient_candidate | 10 | 21 | IC187 (Galaxy) | 1.72540° | near-field match | 45 | hold |
| watch | [AT2026aiqs](https://www.wis-tns.org/object/2026aiqs) | transient_candidate | 9 | 21.44 | IC 189 (Galaxy) | 1.98630° | near-field match | 45 | hold |
| watch | [AT2026aiqv](https://www.wis-tns.org/object/2026aiqv) | transient_candidate | 9 | 21.94 | NGC672 (Galaxy) | 1.71851° | near-field match | 45 | hold |
| watch | [AT2026aira](https://www.wis-tns.org/object/2026aira) | transient_candidate | 8 | 21.61 | NGC7177 (Galaxy) | 1.64805° | near-field match | 45 | hold |
| watch | [AT2026airm](https://www.wis-tns.org/object/2026airm) | transient_candidate | 13 | 19.98 | IC1562 (Galaxy) | 1.43858° | near-field match | 45 | hold |
| watch | [AT2026aiti](https://www.wis-tns.org/object/2026aiti) | transient_candidate | 12 | 19.56 | IC719 (Galaxy) | 1.52988° | near-field match | 45 | hold |
| watch | [AT2026aiul](https://www.wis-tns.org/object/2026aiul) | transient_candidate | 9 | 21.17 | Caldwell 44 (C44) (Galaxy) | 1.56654° | near-field match | 45 | hold |
| watch | [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) | transient_candidate | 9 | 21.09 | NGC2681 (Galaxy) | 1.89726° | near-field match | 45 | hold |
| watch | [AT2026aiwk](https://www.wis-tns.org/object/2026aiwk) | transient_candidate | 21 | 19.72 | Caldwell 48 (C48) (Galaxy) | 1.74454° | near-field match | 45 | hold |
| watch | [AT2026aixs](https://www.wis-tns.org/object/2026aixs) | transient_candidate | 8 | 19.97 | NGC3610 (Galaxy) | 1.63021° | near-field match | 45 | hold |
| watch | [AT2026aiyb](https://www.wis-tns.org/object/2026aiyb) | transient_candidate | 9 | 20.39 | IC392 (Galaxy) | 1.52492° | near-field match | 45 | hold |
| watch | [AT2026aiyd](https://www.wis-tns.org/object/2026aiyd) | transient_candidate | 11 | 20 | IC 1481 (Galaxy) | 1.26208° | near-field match | 45 | hold |
| watch | [AT2026aizu](https://www.wis-tns.org/object/2026aizu) | transient_candidate | 12 | 22.25 | IC 1507 (Galaxy) | 1.65578° | near-field match | 45 | hold |
| watch | [AT2026aizw](https://www.wis-tns.org/object/2026aizw) | transient_candidate | 11 | 22.11 | IC 5374 (Galaxy) | 1.76396° | near-field match | 45 | hold |
| watch | [AT2026aizx](https://www.wis-tns.org/object/2026aizx) | transient_candidate | 9 | 22.3 | IC1696 (Galaxy) | 1.77435° | near-field match | 45 | hold |
| watch | [AT2026ajae](https://www.wis-tns.org/object/2026ajae) | transient_candidate | 24 | 22.56 | NGC488 (Galaxy) | 1.54038° | near-field match | 45 | hold |
| watch | [AT2026ajaf](https://www.wis-tns.org/object/2026ajaf) | transient_candidate | 11 | 22.36 | IC 1481 (Galaxy) | 1.97393° | near-field match | 45 | hold |
| watch | [AT2026ajah](https://www.wis-tns.org/object/2026ajah) | transient_candidate | 11 | 21.96 | IC1696 (Galaxy) | 1.73881° | near-field match | 45 | hold |
| watch | [AT2026ajay](https://www.wis-tns.org/object/2026ajay) | transient_candidate | 22 | 21.83 | Andromeda Galaxy (Galaxy) | 1.60207° | near-field match | 45 | hold |
| watch | [AT2026ajbe](https://www.wis-tns.org/object/2026ajbe) | transient_candidate | 10 | 21.27 | IC 180 (Galaxy) | 1.55678° | near-field match | 45 | hold |
| watch | [SN2026aaee](https://www.wis-tns.org/object/2026aaee) | SN II | 72 | 17.12 | IC 2360 (Star) | 1.01344° | near-field match | 43 | hold |
| watch | [AT2026aiay](https://www.wis-tns.org/object/2026aiay) | transient_candidate | 7 | 20 | Messier 40 (M40) (Double star) | 1.14193° | near-field match | 43 | hold |
| watch | [AT2026aies](https://www.wis-tns.org/object/2026aies) | transient_candidate | 5 | 21.09 | Robin's Egg Nebula (Planetary nebula) | 1.74650° | near-field match | 43 | hold |
| watch | [AT2026aiid](https://www.wis-tns.org/object/2026aiid) | transient_candidate | 7 | 19.8 | IC1415 (Nebula) | 1.79155° | near-field match | 43 | hold |
| watch | [AT2026aiif](https://www.wis-tns.org/object/2026aiif) | transient_candidate | 7 | 20.25 | IC2013 (Nebula) | 1.67634° | near-field match | 43 | hold |
| watch | [AT2026aiih](https://www.wis-tns.org/object/2026aiih) | transient_candidate | 4 | 23.45 | IC2055 (Nebula) | 1.30155° | near-field match | 43 | hold |
| watch | [AT2026aiik](https://www.wis-tns.org/object/2026aiik) | transient_candidate | 4 | 23.13 | IC1992 (Nebula) | 1.50046° | near-field match | 43 | hold |
| watch | [AT2026aijr](https://www.wis-tns.org/object/2026aijr) | transient_candidate | 6 | 20.08 | NGC7447 (Nebula) | 1.89133° | near-field match | 43 | hold |
| watch | [AT2026aila](https://www.wis-tns.org/object/2026aila) | transient_candidate | 5 | 19.91 | NGC2586 (Nebula) | 1.95903° | near-field match | 43 | hold |
| watch | [AT2026ailb](https://www.wis-tns.org/object/2026ailb) | transient_candidate | 5 | 19.83 | IC518 (Nebula) | 1.97027° | near-field match | 43 | hold |
| watch | [AT2026ailw](https://www.wis-tns.org/object/2026ailw) | transient_candidate | 7 | 20.38 | IC286 (Nebula) | 1.73940° | near-field match | 43 | hold |
| watch | [AT2026aimq](https://www.wis-tns.org/object/2026aimq) | transient_candidate | 7 | 20.11 | NGC4317 (Nebula) | 1.22316° | near-field match | 43 | hold |
| watch | [AT2026aiof](https://www.wis-tns.org/object/2026aiof) | transient_candidate | 7 | 20.59 | Collinder 120 (CR120) (Open cluster) | 1.65707° | near-field match | 43 | hold |
| watch | [AT2026aipr](https://www.wis-tns.org/object/2026aipr) | transient_candidate | 6 | 22.3 | IC5385 (Nebula) | 1.58832° | near-field match | 43 | hold |
| watch | [AT2026airk](https://www.wis-tns.org/object/2026airk) | transient_candidate | 3 | 20.12 | IC 71 (Star) | 1.00378° | near-field match | 43 | hold |
| watch | [AT2026aisi](https://www.wis-tns.org/object/2026aisi) | transient_candidate | 3 | 20.26 | Collinder 133 (CR133) (Open cluster) | 1.35377° | near-field match | 43 | hold |
| watch | [AT2026aitf](https://www.wis-tns.org/object/2026aitf) | transient_candidate | 4 | 19.56 | NGC3578 (Nebula) | 1.94090° | near-field match | 43 | hold |
| watch | [AT2026aitp](https://www.wis-tns.org/object/2026aitp) | transient_candidate | 6 | 19.76 | NGC3181 (HII) | 1.80905° | near-field match | 43 | hold |
| watch | [AT2026aiui](https://www.wis-tns.org/object/2026aiui) | transient_candidate | 4 | 21.25 | Intergalactic Wanderer (Globular cluster) | 1.22722° | near-field match | 43 | hold |
| watch | [AT2026aiwa](https://www.wis-tns.org/object/2026aiwa) | transient_candidate | 3 | 22.37 | IC 1623 (CiG) | 1.45584° | near-field match | 43 | hold |
| watch | [AT2026aiwg](https://www.wis-tns.org/object/2026aiwg) | transient_candidate | 5 | 20.6 | IC323 (Nebula) | 1.25852° | near-field match | 43 | hold |
| watch | [AT2026aiwm](https://www.wis-tns.org/object/2026aiwm) | transient_candidate | 4 | 20.09 | IC2940 (Nebula) | 1.28946° | near-field match | 43 | hold |
| watch | [AT2026aiwn](https://www.wis-tns.org/object/2026aiwn) | transient_candidate | 2 | 20.08 | NGC56 (Nebula) | 1.79121° | near-field match | 43 | hold |
| watch | [AT2026aixc](https://www.wis-tns.org/object/2026aixc) | transient_candidate | 1 | 20.38 | IC5383 (Nebula) | 1.16692° | near-field match | 43 | hold |
| watch | [AT2026aixt](https://www.wis-tns.org/object/2026aixt) | transient_candidate | 6 | 19.6 | IC640 (Nebula) | 1.79762° | near-field match | 43 | hold |
| watch | [AT2026aixy](https://www.wis-tns.org/object/2026aixy) | transient_candidate | 2 | 20.58 | IC333 (Nebula) | 1.08009° | near-field match | 43 | hold |
| watch | [AT2026aiyq](https://www.wis-tns.org/object/2026aiyq) | transient_candidate | 4 | 20.08 | Melotte 53 (MEL53) (Globular cluster) | 1.83617° | near-field match | 43 | hold |
| watch | [AT2026aiys](https://www.wis-tns.org/object/2026aiys) | transient_candidate | 1 | 19.55 | IC5251 (Nebula) | 1.74747° | near-field match | 43 | hold |
| watch | [AT2026aiyz](https://www.wis-tns.org/object/2026aiyz) | transient_candidate | 2 | 20.43 | IC229 (Nebula) | 1.20798° | near-field match | 43 | hold |
| watch | [AT2026ajcx](https://www.wis-tns.org/object/2026ajcx) | transient_candidate | 7 | 20.12 | IC337 (Nebula) | 1.86545° | near-field match | 43 | hold |
| watch | [AT2026ajde](https://www.wis-tns.org/object/2026ajde) | transient_candidate | 5 | 19.71 | NGC2875 (Nebula) | 1.32058° | near-field match | 43 | hold |
| watch | [SN2026afke](https://www.wis-tns.org/object/2026afke) | SN II | 27 | 19.75 | Lynds Bright Nebula 157 (LBN157) (HII) | 1.95410° | near-field match | 42 | hold |
| watch | [AT2026afxf](https://www.wis-tns.org/object/2026afxf) | transient_candidate | 21 | 19.58 | IC5340 (Nebula) | 0.52787° | near-field match | 42 | hold |
| watch | [AT2026ahkb](https://www.wis-tns.org/object/2026ahkb) | transient_candidate | 11 | 20.8 | NGC7666 (Nebula) | 0.90553° | near-field match | 42 | hold |
| watch | [AT2026aias](https://www.wis-tns.org/object/2026aias) | transient_candidate | 11 | 20.04 | IC333 (Nebula) | 0.69484° | near-field match | 42 | hold |
| watch | [AT2026aiat](https://www.wis-tns.org/object/2026aiat) | transient_candidate | 9 | 19.61 | Collinder 163 (CR163) (Open cluster) | 0.39314° | near-field match | 42 | hold |
| watch | [AT2026aibk](https://www.wis-tns.org/object/2026aibk) | transient_candidate | 12 | 21.26 | NGC843 (Nebula) | 0.80016° | near-field match | 42 | hold |
| watch | [AT2026aihc](https://www.wis-tns.org/object/2026aihc) | transient_candidate | 12 | 20.27 | NGC7666 (Nebula) | 0.34612° | near-field match | 42 | hold |
| watch | [AT2026aiic](https://www.wis-tns.org/object/2026aiic) | transient_candidate | 7 | 20.55 | Lynds Bright Nebula 220 (LBN220) (HII) | 0.80240° | near-field match | 42 | hold |
| watch | [AT2026aiio](https://www.wis-tns.org/object/2026aiio) | transient_candidate | 21 | 20.63 | NGC930 (Nebula) | 0.95799° | near-field match | 42 | hold |
| watch | [AT2026aiop](https://www.wis-tns.org/object/2026aiop) | transient_candidate | 5 | 20.23 | Lynds Bright Nebula 773 (LBN773) (HII) | 0.84759° | near-field match | 42 | hold |
| watch | [AT2026aipj](https://www.wis-tns.org/object/2026aipj) | transient_candidate | 9 | 21.98 | IC1651 (Nebula) | 0.77284° | near-field match | 42 | hold |
| watch | [AT2026aipy](https://www.wis-tns.org/object/2026aipy) | transient_candidate | 20 | 21.81 | NGC2464 (Nebula) | 0.68824° | near-field match | 42 | hold |
| watch | [AT2026aiqq](https://www.wis-tns.org/object/2026aiqq) | transient_candidate | 9 | 21.76 | IC1707 (Nebula) | 0.77210° | near-field match | 42 | hold |
| watch | [AT2026aiqr](https://www.wis-tns.org/object/2026aiqr) | transient_candidate | 9 | 21.78 | NGC737 (Nebula) | 0.33866° | near-field match | 42 | hold |
| watch | [AT2026aiuf](https://www.wis-tns.org/object/2026aiuf) | transient_candidate | 7 | 20.72 | Lynds Bright Nebula 556 (LBN556) (HII) | 0.70503° | near-field match | 42 | hold |
| watch | [AT2026aixn](https://www.wis-tns.org/object/2026aixn) | transient_candidate | 23 | 20.95 | NGC2531 (Nebula) | 0.88316° | near-field match | 42 | hold |
| watch | [AT2026aixq](https://www.wis-tns.org/object/2026aixq) | transient_candidate | 22 | 20.62 | Hind's variable nebula (reflection nebula) | 0.75249° | near-field match | 42 | hold |
| watch | [AT2026ajbi](https://www.wis-tns.org/object/2026ajbi) | transient_candidate | 1 | 20.84 | Barnard 215 (B215) (Dark nebula) | 0.54619° | near-field match | 42 | hold |
| watch | [AT2026agnk](https://www.wis-tns.org/object/2026agnk) | transient_candidate | 23 | 20.06 | Intergalactic Wanderer (Globular cluster) | 1.83335° | near-field match | 35 | hold |
| watch | [AT2026agwt](https://www.wis-tns.org/object/2026agwt) | transient_candidate | 29 | 20.95 | Intergalactic Wanderer (Globular cluster) | 1.72330° | near-field match | 35 | hold |
| watch | [AT2026ahux](https://www.wis-tns.org/object/2026ahux) | transient_candidate | 12 | 20.27 | NGC611 (Nebula) | 1.75898° | near-field match | 35 | hold |
| watch | [AT2026aidb](https://www.wis-tns.org/object/2026aidb) | transient_candidate | 6 | 20.12 | Sharpless 246 (SH2-246) (HII) | 1.22301° | near-field match | 35 | hold |
| watch | [AT2026aiip](https://www.wis-tns.org/object/2026aiip) | transient_candidate | 21 | 20.62 | NGC1639 (Nebula) | 1.39017° | near-field match | 35 | hold |
| watch | [AT2026aikj](https://www.wis-tns.org/object/2026aikj) | transient_candidate | 5 | 20.02 | Lynds Bright Nebula 1010 (LBN1010) (HII) | 1.53192° | near-field match | 35 | hold |
| watch | [AT2026ailo](https://www.wis-tns.org/object/2026ailo) | transient_candidate | 7 | 19.91 | Lynds Bright Nebula 141 (LBN141) (HII) | 1.55411° | near-field match | 35 | hold |
| watch | [AT2026ails](https://www.wis-tns.org/object/2026ails) | transient_candidate | 7 | 20.29 | Lynds Bright Nebula 481 (LBN481) (HII) | 1.74690° | near-field match | 35 | hold |
| watch | [AT2026aimc](https://www.wis-tns.org/object/2026aimc) | transient_candidate | 7 | 20.71 | Sharpless 250 (SH2-250) (HII) | 1.29797° | near-field match | 35 | hold |
| watch | [AT2026aimd](https://www.wis-tns.org/object/2026aimd) | transient_candidate | 4 | 20.38 | Collinder 65 (CR65) (Open cluster) | 1.83173° | near-field match | 35 | hold |
| watch | [AT2026aimw](https://www.wis-tns.org/object/2026aimw) | transient_candidate | 11 | 21.43 | IC5340 (Nebula) | 1.86813° | near-field match | 35 | hold |
| watch | [AT2026aimx](https://www.wis-tns.org/object/2026aimx) | transient_candidate | 11 | 21.18 | NGC7666 (Nebula) | 1.26208° | near-field match | 35 | hold |
| watch | [AT2026aiou](https://www.wis-tns.org/object/2026aiou) | transient_candidate | 12 | 22 | IC1651 (Nebula) | 1.99649° | near-field match | 35 | hold |
| watch | [AT2026aiow](https://www.wis-tns.org/object/2026aiow) | transient_candidate | 9 | 21.68 | NGC7668 (Nebula) | 1.02900° | near-field match | 35 | hold |
| watch | [AT2026aipf](https://www.wis-tns.org/object/2026aipf) | transient_candidate | 11 | 21.81 | IC1651 (Nebula) | 1.78743° | near-field match | 35 | hold |
| watch | [AT2026aipz](https://www.wis-tns.org/object/2026aipz) | transient_candidate | 16 | 20.69 | IC 2275 (Star) | 1.79427° | near-field match | 35 | hold |
| watch | [AT2026aiqf](https://www.wis-tns.org/object/2026aiqf) | transient_candidate | 13 | 21.23 | IC1707 (Nebula) | 1.23023° | near-field match | 35 | hold |
| watch | [AT2026aiqp](https://www.wis-tns.org/object/2026aiqp) | transient_candidate | 9 | 22.1 | IC1737 (Nebula) | 1.48777° | near-field match | 35 | hold |
| watch | [AT2026airg](https://www.wis-tns.org/object/2026airg) | transient_candidate | 3 | 19.93 | Sharpless 260 (SH2-260) (HII) | 1.20103° | near-field match | 35 | hold |
| watch | [AT2026aivl](https://www.wis-tns.org/object/2026aivl) | transient_candidate | 9 | 22.36 | IC1651 (Nebula) | 1.27407° | near-field match | 35 | hold |
| watch | [AT2026aivm](https://www.wis-tns.org/object/2026aivm) | transient_candidate | 11 | 21.89 | NGC728 (Nebula) | 1.63081° | near-field match | 35 | hold |
| watch | [AT2026aivx](https://www.wis-tns.org/object/2026aivx) | transient_candidate | 3 | 22.48 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.67357° | near-field match | 35 | hold |
| watch | [AT2026aiwh](https://www.wis-tns.org/object/2026aiwh) | transient_candidate | 1 | 19.85 | Lynds Bright Nebula 434 (LBN434) (HII) | 1.66663° | near-field match | 35 | hold |
| watch | [AT2026aiwq](https://www.wis-tns.org/object/2026aiwq) | transient_candidate | 5 | 20.72 | van den Bergh 61 (VDB61) (Nebula) | 1.44782° | near-field match | 35 | hold |
| watch | [AT2026aixk](https://www.wis-tns.org/object/2026aixk) | transient_candidate | 21 | 20.78 | NGC1037 (Nebula) | 1.03553° | near-field match | 35 | hold |
| watch | [AT2026aixl](https://www.wis-tns.org/object/2026aixl) | transient_candidate | 7 | 20.49 | Lynds Bright Nebula 763 (LBN763) (HII) | 1.50403° | near-field match | 35 | hold |
| watch | [AT2026aixm](https://www.wis-tns.org/object/2026aixm) | transient_candidate | 7 | 20.73 | Lynds Bright Nebula 828 (LBN828) (HII) | 1.46269° | near-field match | 35 | hold |
| watch | [AT2026aixp](https://www.wis-tns.org/object/2026aixp) | transient_candidate | 27 | 20.76 | Collinder 204 (CR204) (Open cluster) | 1.53361° | near-field match | 35 | hold |
| watch | [AT2026aiym](https://www.wis-tns.org/object/2026aiym) | transient_candidate | 11 | 20.49 | Robin's Egg Nebula (Planetary nebula) | 1.48879° | near-field match | 35 | hold |
| watch | [AT2026aiyn](https://www.wis-tns.org/object/2026aiyn) | transient_candidate | 11 | 22.14 | NGC894 (Nebula) | 1.63394° | near-field match | 35 | hold |
| watch | [AT2026aize](https://www.wis-tns.org/object/2026aize) | transient_candidate | 11 | 20.61 | IC5248 (Nebula) | 1.94668° | near-field match | 35 | hold |
| watch | [AT2026aizy](https://www.wis-tns.org/object/2026aizy) | transient_candidate | 5 | 22.68 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.97258° | near-field match | 35 | hold |
| watch | [AT2026ajau](https://www.wis-tns.org/object/2026ajau) | transient_candidate | 29 | 21.1 | Collinder 116 (CR116) (Open cluster) | 1.33313° | near-field match | 35 | hold |
| watch | [AT2026ajaw](https://www.wis-tns.org/object/2026ajaw) | transient_candidate | 29 | 20.69 | Beehive cluster (Open cluster) | 1.31677° | near-field match | 35 | hold |
| watch | [AT2026ajbc](https://www.wis-tns.org/object/2026ajbc) | transient_candidate | 12 | 21.19 | IC1707 (Nebula) | 1.73198° | near-field match | 35 | hold |
| watch | [AT2026aiqu](https://www.wis-tns.org/object/2026aiqu) | transient_candidate | 9 | 21.88 | Collinder 21 (CR21) (Open cluster) | 0.34357° | near-field match | 34 | hold |
| watch | [AT2026ahbl](https://www.wis-tns.org/object/2026ahbl) | transient_candidate | 13 | 19.99 | Lynds Bright Nebula 157 (LBN157) (HII) | 1.08937° | near-field match | 27 | hold |
| watch | [AT2026aipg](https://www.wis-tns.org/object/2026aipg) | transient_candidate | 9 | 22.37 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.21442° | near-field match | 27 | hold |
| watch | [AT2026aiiq](https://www.wis-tns.org/object/2026aiiq) | transient_candidate | 35 | 19.77 | IC 1962 (Galaxy) | 0.89936° | near-field match | 15 | hold |
| watch | [AT2026aioy](https://www.wis-tns.org/object/2026aioy) | transient_candidate | 41 | 21.42 | IC 3 (Spiral galaxy) | 0.87334° | near-field match | 15 | hold |
| watch | [AT2026aavs](https://www.wis-tns.org/object/2026aavs) | transient_candidate | 67 | 19.29 | Lynds Bright Nebula 811 (LBN811) (HII) | 1.33240° | near-field match | 10 | hold |
| watch | [AT2026adsw](https://www.wis-tns.org/object/2026adsw) | transient_candidate | 40 | 21.73 | IC1386 (Galaxy) | 1.35743° | near-field match | 8 | hold |
| watch | [AT2026aibe](https://www.wis-tns.org/object/2026aibe) | transient_candidate | 37 | 21.74 | Silver Sliver Galaxy (Galaxy) | 1.67355° | near-field match | 8 | hold |
| watch | [AT2026aiov](https://www.wis-tns.org/object/2026aiov) | transient_candidate | 32 | 22.32 | IC 5374 (Galaxy) | 1.17482° | near-field match | 8 | hold |
| watch | [AT2026aiox](https://www.wis-tns.org/object/2026aiox) | transient_candidate | 32 | 21.82 | IC 3 (Spiral galaxy) | 1.75237° | near-field match | 8 | hold |
| watch | [AT2026aipt](https://www.wis-tns.org/object/2026aipt) | transient_candidate | 39 | 20.84 | IC 1775 (Galaxy) | 1.50389° | near-field match | 8 | hold |
| watch | [AT2026aiyu](https://www.wis-tns.org/object/2026aiyu) | transient_candidate | 67 | 21.98 | NGC1425 (Galaxy) | 1.69335° | near-field match | 8 | hold |
| watch | [AT2026aiyw](https://www.wis-tns.org/object/2026aiyw) | transient_candidate | 73 | 20.41 | NGC1340 (Galaxy) | 1.91424° | near-field match | 8 | hold |
| watch | [SN2026acjc](https://www.wis-tns.org/object/2026acjc) | SN Ib | 52 | 19.85 | Lynds Dark Nebula 1648 (LDN1648) (Dark nebula) | 1.97714° | near-field match | 5 | hold |
| watch | [AT2026aiir](https://www.wis-tns.org/object/2026aiir) | transient_candidate | 34 | 20.1 | Lynds Bright Nebula 790 (LBN790) (HII) | 0.58443° | near-field match | 0 | hold |

## Candidate dossiers

### 1. [SN2026agzo](https://www.wis-tns.org/object/2026agzo) near NGC3239

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.15481° (9.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.04449 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:49:08Z · 17 days · 18.14 r |
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
| Subject | **NGC3239** · `NGC3239` |
| Catalog display name | NGC3239 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.4 · 3.61′ × 2.71′ |
| Distance | — |
| Separation | 0.15481° · 9.29′ |
| Catalog description | NGC 3239 is an irregular galaxy in the constellation of Leo. The galaxy was discovered in 1784 by William Herschel and is part of the New General Catalogue. It harbors a large and relatively bright H II region in its southeastern section that was first cataloged by Russian astronomer Boris Vorontsov-Velyaminov as VV95b. It's believed that NGC 3239 is the result of a galactic merger with a low-mass galaxy. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agzo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.4034933%2017.0807088&fov=0.5&survey=P%2FDSS2%2Fcolor)

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
| Discovery | 2026-11-02T19:55:53Z · 8 days · 16.1 Clear |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.460208%2013.424028&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) near IC 2405

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 100/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2405 as this object's host. The 0.45056° (27.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN |
| Redshift | 0.0257 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:36Z · 7 days · 18.49 g |
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
| Subject | **IC 2405** · `IC 2405` |
| Catalog display name | NGC 4329 |
| Type / constellation | Galaxy · Lyn |
| Catalog magnitude / angular size | — · 0.76′ × 0.57′ |
| Distance | — |
| Separation | 0.45056° · 27.03′ |
| Catalog description | NGC 4329 is an elliptical galaxy located 144 million light-years away in the constellation Corvus. The galaxy was discovered by astronomer John Herschel on March 9, 1828. NGC 4329 is host a supermassive black hole with an estimated mass of 3.1×108 solar masses. NGC 4329 is a member of a group of 5 galaxies known as [T2015] nest 100478. NGC 4329 is the brightest member of this group and the group includes the galaxies IC 785, IC 786, MCG-02-32-006, and LEDA 170189. The redshift of NGC 4329 places it in the within the bounds of the Hydra-Centaurus supercluster. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2405 has the different designation NGC 4329 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=132.0534498%2036.7792244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026aina](https://www.wis-tns.org/object/2026aina) near NGC2052

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2052 as this object's host. The 0.15398° (9.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | Nova |
| Redshift | 0.0011 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T03:50:24Z · 4 days · 13.8 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4489....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4489....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2052** · `NGC2052` |
| Catalog display name | NGC2052 |
| Type / constellation | Nebula · Dorado |
| Catalog magnitude / angular size | — · 18′ × 12′ |
| Distance | — |
| Separation | 0.15398° · 9.24′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤16.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aina) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=84.47673%20-69.915&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [SN2026agst](https://www.wis-tns.org/object/2026agst) near NGC636

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.79813° (107.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ic-BL |
| Redshift | 0.059 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-23T22:28:43Z · 18 days · 18.36 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4260....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4260....1T/abstract) |
| Classification references | [2026TNSCR4322....1N](https://ui.adsabs.harvard.edu/abs/2026TNSCR4322....1N/abstract) |
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
| Separation | 1.79813° · 107.89′ |
| Catalog description | NGC 636 is an elliptical galaxy in the Cetus constellation. It is located about 96 million light-years from the Milky Way. It was discovered by the German–British astronomer William Herschel in 1785. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agst) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.5457722%20-7.9051303&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 6. [AT2026aicq](https://www.wis-tns.org/object/2026aicq) near IC 369

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
| Discovery | 2026-11-04T13:00:09Z · 6 days · 18.48 L |
| Latest public photometry | Not available in the staged feed |
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

### 7. [AT2026aikg](https://www.wis-tns.org/object/2026aikg) near NGC4414

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4414 as this object's host. The 0.85966° (51.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:55:21Z · 7 days · 17.95 r |
| Latest public photometry | Not available in the staged feed |
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

### 8. [AT2026aimo](https://www.wis-tns.org/object/2026aimo) near NGC4691

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4691 as this object's host. The 0.52514° (31.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T13:17:44Z · 4 days · 16.71 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC4691** · `NGC4691` |
| Catalog display name | NGC4691 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 11 · 3.03′ × 2.46′ |
| Distance | — |
| Separation | 0.52514° · 31.51′ |
| Catalog description | NGC 4691 is a barred spiral galaxy in the constellation Virgo. The galaxy lies about 70 million light years away from Earth, which means, given its apparent dimensions, that NGC 4691 is approximately 60,000 light years across. It was discovered by German-British astronomer William Herschel on 17 April 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=192.4356316%20-2.9712045&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 9. [AT2026aizp](https://www.wis-tns.org/object/2026aizp) near Atoms For Peace Galaxy

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Atoms For Peace Galaxy as this object's host. The 0.49861° (29.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T08:20:41Z · 1 days · 18.1 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
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
| Separation | 0.49861° · 29.92′ |
| Catalog description | NGC 7252 is a peculiar galaxy resulting from an interaction between two galaxies that started a billion years ago. It is located 220 million light years away in the constellation Aquarius. It is also called Atoms for Peace Galaxy, a nickname which comes from its loop-like structure, made of stars, that resembles a classic diagram of an electron orbiting an atomic nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.941229%20-25.125931&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 10. [AT2026ajcp](https://www.wis-tns.org/object/2026ajcp) near NGC 4517

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4517 as this object's host. The 0.80621° (48.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:16Z · 0 days · 17.76 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 4517** · `NGC4517` |
| Catalog display name | NGC 4517 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | — · 10.73′ × 1.72′ |
| Distance | — |
| Separation | 0.80621° · 48.37′ |
| Catalog description | NGC 4517 is a spiral galaxy located approximately 40 million light-years away in the constellation of Virgo. It was discovered in 1784 by William Herschel. It is a member of the Virgo II Groups, a series of galaxies and galaxy clusters strung out from the southern edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=188.9257748%20-0.2144061&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 11. [SN2026aied](https://www.wis-tns.org/object/2026aied) near Lynds Bright Nebula 465 (LBN465)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 465 (LBN465) as this object's host. The 0.57960° (34.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.018596 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T03:44:06Z · 7 days · 18.33 g |
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
| Subject | **Lynds Bright Nebula 465 (LBN465)** · `LBN465` |
| Catalog display name | Lynds Bright Nebula 465 (LBN465) |
| Type / constellation | HII · Draco |
| Catalog magnitude / angular size | — · 90′ × 10′ |
| Distance | — |
| Separation | 0.57960° · 34.78′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aied) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=289.2104416%2070.5122062&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 12. [AT2026ainb](https://www.wis-tns.org/object/2026ainb) near IC 450

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 83/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 450 as this object's host. The 1.07438° (64.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T02:25:45Z · 6 days · 18.12 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 450** · `IC 450` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cam |
| Catalog magnitude / angular size | — · 1.38′ × 0.8′ |
| Distance | — |
| Separation | 1.07438° · 64.46′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 450 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.0704236%2074.3446308&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 13. [AT2026aisw](https://www.wis-tns.org/object/2026aisw) near IC4946

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4946 as this object's host. The 1.25863° (75.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T00:30:48Z · 4 days · 18.02 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC4946** · `IC4946` |
| Catalog display name | IC4946 |
| Type / constellation | Galaxy · Sagittarius |
| Catalog magnitude / angular size | 11.9 · 2.5′ × 0.9′ |
| Distance | 37,900 kpc |
| Separation | 1.25863° · 75.52′ |
| Catalog description | extremely, excessively faint, small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=306.969195%20-42.955565&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 14. [AT2026aict](https://www.wis-tns.org/object/2026aict) near Dumbbell Nebula

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Dumbbell Nebula as this object's host. The 0.76955° (46.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T05:43:56Z · 6 days · 18.31 orange |
| Latest public photometry | Not available in the staged feed |
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

### 15. [AT2026aiuw](https://www.wis-tns.org/object/2026aiuw) near Lynds Dark Nebula 637 (LDN637)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 637 (LDN637) as this object's host. The 1.17864° (70.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:51:28Z · 2 days · 14.89 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 637 (LDN637)** · `LDN637` |
| Catalog display name | Lynds Dark Nebula 637 (LDN637) |
| Type / constellation | Dark nebula · Ophiuchus |
| Catalog magnitude / angular size | — · 11.73′ × 11.73′ |
| Distance | — |
| Separation | 1.17864° · 70.72′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤16.5; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiuw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=281.376833%208.58275&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 16. [AT2026aiux](https://www.wis-tns.org/object/2026aiux) near Lynds Dark Nebula 705 (LDN705)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 705 (LDN705) as this object's host. The 0.57543° (34.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:57:16Z · 2 days · 17.29 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 705 (LDN705)** · `LDN705` |
| Catalog display name | Lynds Dark Nebula 705 (LDN705) |
| Type / constellation | Dark nebula · Aquila |
| Catalog magnitude / angular size | — · 19.85′ × 19.85′ |
| Distance | — |
| Separation | 0.57543° · 34.53′ |
| Catalog description | Dark; diam. 3', with narrow extension for 17'to NW. This small spot, with its narrow extension, is in a relatively darker space in the star cloud. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiux) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=294.331792%2012.953528&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 17. [AT2026ajcg](https://www.wis-tns.org/object/2026ajcg) near Collinder 394 (CR394)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 394 (CR394) as this object's host. The 0.65272° (39.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:00:30Z · 3 days · 16.87 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 394 (CR394)** · `CR394` |
| Catalog display name | Collinder 394 (CR394) |
| Type / constellation | Open cluster · Sagittarius |
| Catalog magnitude / angular size | 6.3 · — |
| Distance | — |
| Separation | 0.65272° · 39.16′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajcg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=282.8768301%20-20.3408695&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 18. [AT2026aikp](https://www.wis-tns.org/object/2026aikp) near Great Nebula in Andromeda

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Great Nebula in Andromeda as this object's host. The 0.10297° (6.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T13:24:24Z · 6 days · 19.14 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 19. [AT2026aiol](https://www.wis-tns.org/object/2026aiol) near IC1231

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1231 as this object's host. The 0.00433° (0.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T02:23:06Z · 5 days · 19.29 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1231** · `IC1231` |
| Catalog display name | IC1231 |
| Type / constellation | Galaxy · Draco |
| Catalog magnitude / angular size | 13.2 · 1.88′ × 0.86′ |
| Distance | 71,400 kpc |
| Separation | 0.00433° · 0.26′ |
| Catalog description | most extremely faint, large, round, preceding (westward) / pretty (adv., before F. B. L, S) bright a single star south preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiol) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=251.7473241%2058.4274252&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 20. [SN2026ahze](https://www.wis-tns.org/object/2026ahze) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 88/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.92283° (115.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.092 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:33:40Z · 7 days · 18.71 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4419....1W](https://ui.adsabs.harvard.edu/abs/2026TNSTR4419....1W/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahze) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.1394246%20-1.8788168&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 21. [SN2026agwk](https://www.wis-tns.org/object/2026agwk) near IC391

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC391 as this object's host. The 0.40294° (24.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T07:48:13Z · 15 days · 19.32 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4304....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4304....1S/abstract) |
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
| Separation | 0.40294° · 24.18′ |
| Catalog description | faint, small in angular size, round |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=72.5297696%2078.3542167&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 22. [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 87/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 0.47363° (28.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.039 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:53:54Z · 9 days · 18.71 L |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=3.1673559%20-0.0368725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 23. [AT2026aile](https://www.wis-tns.org/object/2026aile) near NGC7471

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7471 as this object's host. The 0.21732° (13.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T06:25:03Z · 4 days · 19.36 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7471** · `NGC7471` |
| Catalog display name | NGC7471 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.21732° · 13.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aile) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.5157203%20-22.8746702&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 24. [SN2026aguc](https://www.wis-tns.org/object/2026aguc) near IC382

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC382 as this object's host. The 1.38071° (82.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.035 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T09:42:27Z · 16 days · 19.18 r |
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

### 25. [AT2026aijt](https://www.wis-tns.org/object/2026aijt) near IC 673

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
| Discovery | 2026-11-03T12:53:54Z · 7 days · 19.16 r |
| Latest public photometry | Not available in the staged feed |
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

### 26. [AT2026ainc](https://www.wis-tns.org/object/2026ainc) near NGC 2742

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2742 as this object's host. The 0.83545° (50.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T03:44:02Z · 6 days · 19.14 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2742** · `NGC 2742` |
| Catalog display name | NGC 2742 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | 11.49 · 2.86′ × 1.49′ |
| Distance | — |
| Separation | 0.83545° · 50.13′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=137.2210583%2061.2990817&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 27. [AT2026aitl](https://www.wis-tns.org/object/2026aitl) near NGC3938

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3938 as this object's host. The 0.67438° (40.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:18:04Z · 6 days · 19.38 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3938** · `NGC3938` |
| Catalog display name | NGC3938 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.4 · 3.55′ × 3.44′ |
| Distance | — |
| Separation | 0.67438° · 40.46′ |
| Catalog description | NGC 3938 is an unbarred spiral galaxy in the Ursa Major constellation. It was discovered by German-British astronomer William Herschel on 6 February 1788. It is one of the brightest spiral galaxies in the Ursa Major South galaxy group and is roughly 76,000 light years in diameter. It is approximately 41.4 million light years away from Earth. NGC 3938 is classified as type Sc under the Hubble sequence, a loosely wound spiral galaxy with a smaller and dimmer bulge. The spiral arms of the galaxy contain many areas of ionized atomic hydrogen gas, more so towards the center. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=178.41791%2043.464231&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 28. [AT2026aitv](https://www.wis-tns.org/object/2026aitv) near NGC3887

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3887 as this object's host. The 0.26253° (15.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:05:27Z · 2 days · 19.16 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.26253° · 15.75′ |
| Catalog description | NGC 3887 is a barred spiral galaxy in the constellation Crater. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 3887 is approximately 60,000 light years across. It was discovered by William Herschel on December 31, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=176.8187009%20-16.5968583&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [AT2026aiuv](https://www.wis-tns.org/object/2026aiuv) near IC 897

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 897 as this object's host. The 0.45434° (27.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:04:34Z · 2 days · 18.64 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 897** · `IC 897` |
| Catalog display name | IC 5325 |
| Type / constellation | Galaxy · Com |
| Catalog magnitude / angular size | — · 0.75′ × 0.32′ |
| Distance | 68.2 ly |
| Separation | 0.45434° · 27.26′ |
| Catalog description | IC 5325 is a spiral galaxy in the constellation Phoenix. The galaxy lies about 70 million light years away from Earth, which means, given its apparent dimensions, that IC 5325 is approximately 75,000 light years across. It was discovered by Lewis Swift in 1897. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 897 has the different designation IC 5325 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiuv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=203.1490435%2018.0417474&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 30. [AT2026aiyr](https://www.wis-tns.org/object/2026aiyr) near NGC2566

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2566 as this object's host. The 0.87981° (52.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T17:37:26Z · 3 days · 19.34 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2566** · `NGC2566` |
| Catalog display name | NGC2566 |
| Type / constellation | Galaxy · Puppis |
| Catalog magnitude / angular size | 10.8 · 3.98′ × 2.75′ |
| Distance | 8,770 kpc |
| Separation | 0.87981° · 52.79′ |
| Catalog description | NGC 2566 is a barred spiral galaxy in the constellation of Puppis. Its velocity with respect to the cosmic microwave background is 1898 ± 19 km/s, which corresponds to a Hubble distance of 91.3 ± 6.5 Mly (28.00 ± 1.98 Mpc). However, five non-redshift measurements give a much closer distance of 35.39 ± 8.42 Mly (10.852 ± 2.583 Mpc). It was discovered by German-British astronomer William Herschel on 6 March 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=123.79501%20-25.85603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 31. [AT2026ajcv](https://www.wis-tns.org/object/2026ajcv) near IC 4297

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4297 as this object's host. The 0.36926° (22.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T13:07:08Z · 1 days · 19.32 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 4297** · `IC 4297` |
| Catalog display name | NGC4273 |
| Type / constellation | Galaxy · Com |
| Catalog magnitude / angular size | — · 0.88′ × 0.4′ |
| Distance | — |
| Separation | 0.36926° · 22.16′ |
| Catalog description | NGC 4273 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 2727 ± 24 km/s, which corresponds to a Hubble distance of 131.2 ± 9.3 Mly (40.23 ± 2.84 Mpc). However, 20 non-redshift measurements give a much closer distance of 94.72 ± 4.68 Mly (29.040 ± 1.435 Mpc). It was discovered by German-British astronomer William Herschel on 17 April 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4297 has the different designation NGC4273 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=204.1177926%2026.1604328&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 32. [AT2026aivh](https://www.wis-tns.org/object/2026aivh) near Lynds Bright Nebula 749 (LBN749)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 749 (LBN749) as this object's host. The 0.23181° (13.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:09:31Z · 7 days · 18.75 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 749 (LBN749)** · `LBN749` |
| Catalog display name | Lynds Bright Nebula 749 (LBN749) |
| Type / constellation | HII · Perseus |
| Catalog magnitude / angular size | — · 150′ × 60′ |
| Distance | — |
| Separation | 0.23181° · 13.91′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°.

[TNS object](https://www.wis-tns.org/object/2026aivh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.4915023%2032.0738749&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 33. [AT2026ahzg](https://www.wis-tns.org/object/2026ahzg) near IC2152

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2152 as this object's host. The 1.50611° (90.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:43:26Z · 7 days · 18.77 orange |
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
| Subject | **IC2152** · `IC2152` |
| Catalog display name | IC2152 |
| Type / constellation | Galaxy · Lepus |
| Catalog magnitude / angular size | 13.5 · 1.65′ × 1.15′ |
| Distance | 29,000 kpc |
| Separation | 1.50611° · 90.37′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, several bright stars (pl.) following (eastward) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahzg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.5738941%20-21.7962206&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026aijg](https://www.wis-tns.org/object/2026aijg) near IC 5016

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
| Discovery | 2026-11-06T01:37:49Z · 4 days · 19.19 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 35. [AT2026aijv](https://www.wis-tns.org/object/2026aijv) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.27193° (76.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:53:54Z · 7 days · 18.99 r |
| Latest public photometry | Not available in the staged feed |
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

### 36. [AT2026aioe](https://www.wis-tns.org/object/2026aioe) near IC 1331

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1331 as this object's host. The 1.19750° (71.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:11:14Z · 3 days · 18.57 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1331** · `IC 1331` |
| Catalog display name | NGC 1415 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 1.75′ × 0.49′ |
| Distance | — |
| Separation | 1.19750° · 71.85′ |
| Catalog description | NGC 1415 is a Lenticular Galaxy in the constellation Eridanus. it was Discovered on Dec 9, 1784 by William Herschel  also observed on a unknown date by John Herschel and Discovered on Oct 8, 1896 by Lewis Swift NGC 1415 (also known as IC 1983) is a Lenticular Galaxy in the constellation Eridanus. it was Discovered on Dec 9, 1784 by William Herschel (listed as NGC 1415) also observed on a unknown date by John Herschel and Discovered on Oct 8, 1896 by Lewis Swift (and listed as IC 1983) |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1331 has the different designation NGC 1415 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aioe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=310.8738136%20-9.4462796&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 37. [AT2026aisl](https://www.wis-tns.org/object/2026aisl) near IC575

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC575 as this object's host. The 1.57115° (94.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T08:07:46Z · 3 days · 18.61 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC575** · `IC575` |
| Catalog display name | IC575 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 13.2 · 1.52′ × 1.17′ |
| Distance | — |
| Separation | 1.57115° · 94.27′ |
| Catalog description | faint, small in angular size, round, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=149.0785514%20-5.3500586&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 38. [AT2026aiso](https://www.wis-tns.org/object/2026aiso) near IC4951

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4951 as this object's host. The 1.51398° (90.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T01:31:48Z · 4 days · 19.36 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC4951** · `IC4951` |
| Catalog display name | IC4951 |
| Type / constellation | Galaxy · Pavo |
| Catalog magnitude / angular size | 13.8 · 3.07′ × 0.71′ |
| Distance | 9,010 kpc |
| Separation | 1.51398° · 90.84′ |
| Catalog description | very faint, very small in angular size, extremely, excessively extended 170deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiso) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=305.46338%20-61.464788&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 39. [AT2026aita](https://www.wis-tns.org/object/2026aita) near NGC1404

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1404 as this object's host. The 0.21838° (13.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 21.27 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1404** · `NGC1404` |
| Catalog display name | NGC1404 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 9.9 · 5.01′ × 4.38′ |
| Distance | — |
| Separation | 0.21838° · 13.10′ |
| Catalog description | NGC 1404 is an elliptical galaxy in the Southern constellation Eridanus. It was discovered on November 28, 1837, by the astronomer John Herschel. Based on the tip of the red-giant branch distance indicator, it lies at a distance of approximately 60 million light-years from the Milky Way. It is one of the brightest members of the Fornax Cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aita) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.527674%20-35.752971&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [AT2026aite](https://www.wis-tns.org/object/2026aite) near IC 659

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 659 as this object's host. The 1.35166° (81.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T12:55:42Z · 4 days · 19.2 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 659** · `IC 659` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 1.24′ × 0.86′ |
| Distance | — |
| Separation | 1.35166° · 81.10′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 659 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aite) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=163.8194246%20-7.4218059&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 41. [AT2026aitn](https://www.wis-tns.org/object/2026aitn) near NGC3414

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3414 as this object's host. The 1.29435° (77.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:26:13Z · 6 days · 19.38 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3414** · `NGC3414` |
| Catalog display name | NGC3414 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10.8 · 2.67′ × 1.37′ |
| Distance | — |
| Separation | 1.29435° · 77.66′ |
| Catalog description | NGC 3414 is a lenticular galaxy in the constellation Leo Minor. It was discovered by William Herschel on April 11, 1785. It is the central galaxy of a rich galaxy group. Two galaxies, NGC 3418 and UGC 5958, have similar redshifts and are within 800,000 light-years of NGC 3414. It is a member of the NGC 3504 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=163.6336815%2026.9029181&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 42. [AT2026aive](https://www.wis-tns.org/object/2026aive) near NGC2835

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2835 as this object's host. The 1.04795° (62.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:06:23Z · 2 days · 18.74 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2835** · `NGC2835` |
| Catalog display name | NGC2835 |
| Type / constellation | Galaxy · Hydra |
| Catalog magnitude / angular size | 10.6 · 6.43′ × 3.72′ |
| Distance | — |
| Separation | 1.04795° · 62.88′ |
| Catalog description | NGC 2835 is an intermediate spiral galaxy located in the constellation Hydra. It is located at a distance of circa 35 million light years from Earth, which, given its apparent dimensions, means that NGC 2835 is about 65,000 light years across. It was discovered by German astronomer Wilhelm Tempel on April 13, 1884. NGC 2835 is located only 18.5 degrees from the galactic plane. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aive) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.3284%20-22.67521&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 43. [AT2026aivf](https://www.wis-tns.org/object/2026aivf) near NGC2835

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2835 as this object's host. The 1.02455° (61.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:06:23Z · 2 days · 19.03 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2835** · `NGC2835` |
| Catalog display name | NGC2835 |
| Type / constellation | Galaxy · Hydra |
| Catalog magnitude / angular size | 10.6 · 6.43′ × 3.72′ |
| Distance | — |
| Separation | 1.02455° · 61.47′ |
| Catalog description | NGC 2835 is an intermediate spiral galaxy located in the constellation Hydra. It is located at a distance of circa 35 million light years from Earth, which, given its apparent dimensions, means that NGC 2835 is about 65,000 light years across. It was discovered by German astronomer Wilhelm Tempel on April 13, 1884. NGC 2835 is located only 18.5 degrees from the galactic plane. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.325836%20-22.1093&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 44. [AT2026aizi](https://www.wis-tns.org/object/2026aizi) near IC 4660

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4660 as this object's host. The 1.33546° (80.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T02:25:08Z · 5 days · 18.92 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 4660** · `IC 4660` |
| Catalog display name | NGC 4660 |
| Type / constellation | Galaxy · UMi |
| Catalog magnitude / angular size | — · 1.28′ × 0.33′ |
| Distance | — |
| Separation | 1.33546° · 80.13′ |
| Catalog description | NGC 4660 is an elliptical galaxy located about 63 million light-years away in the constellation Virgo. The galaxy was discovered by astronomer William Herschel on March 15, 1784 and is a member of the Virgo Cluster. NGC 4660 is an elliptical galaxy located about 63 million light-years away in the constellation Virgo. The galaxy was discovered by astronomer William Herschel on March 15, 1784 and is a member of the Virgo Cluster. NGC 4660 forms a tight pair with Messier 59. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4660 has the different designation NGC 4660 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=257.6433885%2074.7170731&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 45. [AT2026ajbn](https://www.wis-tns.org/object/2026ajbn) near NGC3189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3189 as this object's host. The 1.65719° (99.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:53:05Z · 0 days · 19.45 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3189** · `NGC3189` |
| Catalog display name | NGC3189 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.1 · 3.64′ × 1.22′ |
| Distance | 24,100 kpc |
| Separation | 1.65719° · 99.43′ |
| Catalog description | NGC 3190 is a spiral galaxy with tightly wound arms and lying in the constellation Leo. It was discovered by William Herschel in 1784. NGC 3190 is member of Hickson 44 galaxy group, estimated at around 80 million light years away, and consisting of four galaxies in a tight group - NGC 3193 is fairly featureless, NGC 3187 is a dim but striking spiral galaxy and NGC 3185 has a barred spiral structure with an outer ring. It is also a member of the NGC 3190 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.7381405%2021.9310431&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 46. [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) near IC 2017

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2017 as this object's host. The 0.36964° (22.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:43:45Z · 11 days · 19.31 L |
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
| Subject | **IC 2017** · `IC 2017` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Ret |
| Catalog magnitude / angular size | — · 1.11′ × 0.74′ |
| Distance | — |
| Separation | 0.36964° · 22.18′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2017 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahpf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.4170832%20-59.7414537&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 47. [AT2026aica](https://www.wis-tns.org/object/2026aica) near IC1914

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1914 as this object's host. The 0.56142° (33.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:03:29Z · 13 days · 18.78 L |
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

### 48. [SN2026agpk](https://www.wis-tns.org/object/2026agpk) near NGC2399

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2399 as this object's host. The 1.83747° (110.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.039 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-23T01:36:00Z · 18 days · 18.85 orange |
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

### 49. [SN2026ahmz](https://www.wis-tns.org/object/2026ahmz) near IC2084

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2084 as this object's host. The 1.11286° (66.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.04 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T14:16:05Z · 13 days · 19.33 L |
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

### 50. [SN2026ahxo](https://www.wis-tns.org/object/2026ahxo) near Lynds Bright Nebula 484 (LBN484)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 484 (LBN484) as this object's host. The 1.59750° (95.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.085 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T00:17:28Z · 7 days · 18.88 wide |
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
| Subject | **Lynds Bright Nebula 484 (LBN484)** · `LBN484` |
| Catalog display name | Lynds Bright Nebula 484 (LBN484) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 60′ × 40′ |
| Distance | — |
| Separation | 1.59750° · 95.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahxo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.472256%2028.5747&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 51. [AT2026aisv](https://www.wis-tns.org/object/2026aisv) near Caldwell 87 (C87)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 87 (C87) as this object's host. The 0.51533° (30.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T04:07:25Z · 2 days · 19.05 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.51533° · 30.92′ |
| Catalog description | NGC 1261 is a globular cluster of stars in the southern constellation of Horologium, first discovered by Scottish astronomer James Dunlop in 1826. The cluster is located at a distance of 53 kilolight-years from the Sun, and 59 kilolight-years from the Galactic Center. It is about 10.24 billion years old with 341,000 times the mass of the Sun. The cluster does not display the normal indications of core collapse, but evidence suggests it may have instead passed through a post core-collapse bounce state within the past two billion years. The central luminosity density is 2.22 L☉·pc−3, which is low for a globular cluster. Despite this, it has a Shapley–Sawyer Concentration Class of II, indicating a dense central concentration. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.237478%20-55.00969&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 52. [SN2026agyk](https://www.wis-tns.org/object/2026agyk) near Barnard 152 (B152)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 69/100

![AstroGuide catalog thumbnail for Barnard 152 (B152)](https://metadata.astroguide.space/v1/assets/target-images/LDN935/71961707339b-primary-exact/thumbnail-160.jpg)

Catalog image: AstroGuide Capture Harvest approved target image asset · [open hosted image](https://metadata.astroguide.space/v1/assets/target-images/LDN935/71961707339b-primary-exact/thumbnail-160.jpg)

> **Near-field only:** TNS does not identify Barnard 152 (B152) as this object's host. The 0.73509° (44.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.03 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T03:50:53Z · 15 days · 18.8 r |
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
| Subject | **Barnard 152 (B152)** · `B152` |
| Catalog display name | Barnard 152 (B152) |
| Type / constellation | Dark nebula · Cepheus |
| Catalog magnitude / angular size | — · 9′ × 9′ |
| Distance | — |
| Separation | 0.73509° · 44.11′ |
| Catalog description | Small; 15'x3'SE and NW |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026agyk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=319.6036762%2061.1807524&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 53. [SN2026aitx](https://www.wis-tns.org/object/2026aitx) near IC 2083

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 68/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2083 as this object's host. The 1.14340° (68.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.03 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T04:24:30Z · 2 days · 19.57 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4505....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4505....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 2083** · `IC 2083` |
| Catalog display name | NGC 320 |
| Type / constellation | Galaxy · Dor |
| Catalog magnitude / angular size | — · 0.95′ × 0.51′ |
| Distance | — |
| Separation | 1.14340° · 68.60′ |
| Catalog description | NGC 320 is a spiral galaxy in the constellation Cetus. It was first discovered in 1886 by Francis Leavenworth. NGC 320 is a spiral galaxy in the constellation Cetus. It was first discovered in 1886 by Francis Leavenworth. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2083 has the different designation NGC 320 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=69.1626575%20-53.2470075&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 54. [AT2026ahab](https://www.wis-tns.org/object/2026ahab) near IC 530

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
| Discovery | 2026-10-28T11:45:47Z · 13 days · 19.2 V-crts |
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

### 55. [AT2026ahch](https://www.wis-tns.org/object/2026ahch) near NGC1792

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1792 as this object's host. The 1.51662° (91.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T14:57:59Z · 12 days · 19.49 L |
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

### 56. [AT2026ahcr](https://www.wis-tns.org/object/2026ahcr) near NGC7626

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7626 as this object's host. The 1.62993° (97.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T21:16:18Z · 13 days · 19.43 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4341....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4341....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7626** · `NGC7626` |
| Catalog display name | NGC7626 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 11.1 · 2.5′ × 2.1′ |
| Distance | — |
| Separation | 1.62993° · 97.80′ |
| Catalog description | NGC 7626 is an elliptical galaxy located in the constellation Pegasus. It was discovered on September 26, 1785, by the German-British astronomer William Herschel. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahcr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.2512992%209.4521324&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 57. [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 1.58832° (95.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:59:41Z · 12 days · 19.41 L |
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

### 58. [AT2026aiaz](https://www.wis-tns.org/object/2026aiaz) near NGC2655

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2655 as this object's host. The 1.67391° (100.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:42:07Z · 8 days · 19.46 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiaz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.9111933%2077.9501758&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 59. [AT2026aiju](https://www.wis-tns.org/object/2026aiju) near IC630

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC630 as this object's host. The 1.80723° (108.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:05:29Z · 12 days · 19.02 r |
| Latest public photometry | Not available in the staged feed |
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

### 60. [AT2026aiql](https://www.wis-tns.org/object/2026aiql) near IC1727

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1727 as this object's host. The 0.16652° (9.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:46:33Z · 9 days · 21.91 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1727** · `IC1727` |
| Catalog display name | IC1727 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 11.6 · 6.52′ × 2.44′ |
| Distance | — |
| Separation | 0.16652° · 9.99′ |
| Catalog description | NGC 672 is a spiral galaxy in the northern constellation of Triangulum, positioned around 2° to the southwest of the star Alpha Trianguli. The original object designated NGC 672 was discovered by the German-born astronomer William Herschel on 26 October 1786, but this was later cataloged as NGC 614. The object now identified as NGC 672 was discovered by John Herschel on 11 November 1827. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiql) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.027667%2027.424658&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 61. [AT2026aibq](https://www.wis-tns.org/object/2026aibq) near NGC6669

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC6669 as this object's host. The 1.81749° (109.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T05:22:11Z · 6 days · 19.07 orange |
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

### 62. [AT2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65298° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 6 days · 19.17 wide |
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

### 63. [AT2026aihy](https://www.wis-tns.org/object/2026aihy) near NGC56

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC56 as this object's host. The 1.97482° (118.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T14:28:11Z · 5 days · 19.5 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 64. [AT2026aija](https://www.wis-tns.org/object/2026aija) near NGC796

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC796 as this object's host. The 1.18846° (71.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T02:00:00Z · 4 days · 19.1 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 65. [AT2026aism](https://www.wis-tns.org/object/2026aism) near IC1988

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1988 as this object's host. The 1.79403° (107.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T03:56:19Z · 2 days · 19.39 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1988** · `IC1988` |
| Catalog display name | IC1988 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.79403° · 107.64′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) large, round, 2 stars (pl.) near following (eastward), 2 stars (pl.) north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aism) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.3653125%20-39.6997213&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 66. [AT2026aitz](https://www.wis-tns.org/object/2026aitz) near IC3009

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC3009 as this object's host. The 0.16327° (9.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T13:02:11Z · 4 days · 19.86 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC3009** · `IC3009` |
| Catalog display name | IC3009 |
| Type / constellation | Nebula · Virgo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.16327° · 9.80′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, considerably small in angular size |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.8414683%2012.5942788&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 67. [AT2026aixw](https://www.wis-tns.org/object/2026aixw) near IC877

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC877 as this object's host. The 1.87815° (112.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T13:09:19Z · 1 days · 18.85 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC877** · `IC877` |
| Catalog display name | IC877 |
| Type / constellation | Nebula · Virgo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.87815° · 112.69′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, preceding (westward) / pretty (adv., before F. B. L, S) bright a single star following (eastward) 13s |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=198.0387641%207.5092143&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 68. [AT2026aiyx](https://www.wis-tns.org/object/2026aiyx) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.73252° (103.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:58:05Z · 1 days · 19.09 L |
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
| Separation | 1.73252° · 103.95′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=340.5478229%2012.7307529&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 69. [AT2026ajcc](https://www.wis-tns.org/object/2026ajcc) near IC435

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC435 as this object's host. The 1.32248° (79.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:47:15Z · 1 days · 18.82 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC435** · `IC435` |
| Catalog display name | IC435 |
| Type / constellation | reflection nebula · Orion |
| Catalog magnitude / angular size | — · 3.98′ × 3.02′ |
| Distance | — |
| Separation | 1.32248° · 79.35′ |
| Catalog description | nebula, a single star 8.5 |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=86.8368515%20-1.5582478&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 70. [SN2026agua](https://www.wis-tns.org/object/2026agua) near Lynds Dark Nebula 1571 (LDN1571)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1571 (LDN1571) as this object's host. The 1.07129° (64.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.05 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T11:03:46Z · 17 days · 19.33 g |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026agua) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.4774615%2010.1813155&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 71. [SN2026agyt](https://www.wis-tns.org/object/2026agyt) near Lynds Bright Nebula 564 (LBN564)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 564 (LBN564) as this object's host. The 1.14138° (68.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.054 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T04:20:39Z · 13 days · 18.99 r |
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
| Subject | **Lynds Bright Nebula 564 (LBN564)** · `LBN564` |
| Catalog display name | Lynds Bright Nebula 564 (LBN564) |
| Type / constellation | HII · Andromeda |
| Catalog magnitude / angular size | — · 70′ × 15′ |
| Distance | — |
| Separation | 1.14138° · 68.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026agyt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.9747814%2048.6572299&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 72. [AT2026aiap](https://www.wis-tns.org/object/2026aiap) near Lynds Bright Nebula 437 (LBN437)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 437 (LBN437) as this object's host. The 0.83711° (50.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T00:08:34Z · 7 days · 18.98 wide |
| Latest public photometry | Not available in the staged feed |
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

### 73. [AT2026aimb](https://www.wis-tns.org/object/2026aimb) near Lynds Bright Nebula 703 (LBN703)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 703 (LBN703) as this object's host. The 0.99979° (59.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:24:53Z · 4 days · 19.3 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 703 (LBN703)** · `LBN703` |
| Catalog display name | Lynds Bright Nebula 703 (LBN703) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 420′ × 120′ |
| Distance | — |
| Separation | 0.99979° · 59.99′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aimb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.6671054%2018.2981873&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 74. [AT2026aivb](https://www.wis-tns.org/object/2026aivb) near Lynds Dark Nebula 387 (LDN387)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 387 (LDN387) as this object's host. The 0.97429° (58.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T01:50:01Z · 3 days · 19.04 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 387 (LDN387)** · `LDN387` |
| Catalog display name | Lynds Dark Nebula 387 (LDN387) |
| Type / constellation | Dark nebula · Ophiuchus |
| Catalog magnitude / angular size | — · 50.12′ × 50.12′ |
| Distance | — |
| Separation | 0.97429° · 58.46′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aivb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=260.3900108%20-3.6491243&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 75. [SN2026afvg](https://www.wis-tns.org/object/2026afvg) near IC 1931

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1931 as this object's host. The 1.30858° (78.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.081 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T08:10:04Z · 23 days · 20.34 g |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afvg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.4652846%202.2134044&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026aicj](https://www.wis-tns.org/object/2026aicj) near IC1531

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1531 as this object's host. The 0.49233° (29.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T10:12:50Z · 6 days · 20.1 L |
| Latest public photometry | Not available in the staged feed |
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

### 77. [AT2026aiij](https://www.wis-tns.org/object/2026aiij) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 0.81942° (49.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 4 days · 23.51 r |
| Latest public photometry | Not available in the staged feed |
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

### 78. [AT2026aike](https://www.wis-tns.org/object/2026aike) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.28536° (17.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T07:22:35Z · 4 days · 22.75 r |
| Latest public photometry | Not available in the staged feed |
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

### 79. [AT2026aikf](https://www.wis-tns.org/object/2026aikf) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.39139° (23.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T07:22:35Z · 4 days · 21.83 r |
| Latest public photometry | Not available in the staged feed |
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

### 80. [AT2026aiki](https://www.wis-tns.org/object/2026aiki) near IC 230

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 230 as this object's host. The 0.98313° (58.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T11:50:45Z · 4 days · 20.27 L |
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
| Subject | **IC 230** · `IC 230` |
| Catalog display name | NGC 945 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.64′ × 0.42′ |
| Distance | — |
| Separation | 0.98313° · 58.99′ |
| Catalog description | NGC 945 is a barred spiral galaxy in the constellation Cetus, located south of the celestial equator. It is estimated to be 200 million light-years from the Milky Way, and about 135,000 light-years in diameter. The object was discovered by astronomer William Herschel on November 28, 1785. It is near NGC 948, with which it forms a gravitationally bound pair of galaxies. In the same area of the sky there are the galaxies NGC 942, NGC 943, NGC 950, and IC 230. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 230 has the different designation NGC 945 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiki) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.8446171%20-9.9113799&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 81. [AT2026ainz](https://www.wis-tns.org/object/2026ainz) near NGC7418

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7418 as this object's host. The 0.82463° (49.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:52:52Z · 6 days · 20.23 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7418** · `NGC7418` |
| Catalog display name | NGC7418 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 11 · 3.66′ × 2.83′ |
| Distance | — |
| Separation | 0.82463° · 49.48′ |
| Catalog description | NGC 7418 is an intermediate spiral galaxy located in the constellation Grus. It is located at a distance of circa 60 million light-years from Earth, which, given its apparent dimensions, means that NGC 7418 is about 60,000 light-years across. It was discovered by John Herschel on August 30, 1834. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.055248%20-37.097899&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 82. [AT2026aiob](https://www.wis-tns.org/object/2026aiob) near NGC4036

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4036 as this object's host. The 0.77482° (46.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:46:27Z · 7 days · 19.57 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC4036** · `NGC4036` |
| Catalog display name | NGC4036 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 4.85′ × 2.08′ |
| Distance | — |
| Separation | 0.77482° · 46.49′ |
| Catalog description | NGC 4036 is the New General Catalogue identifier for a lenticular galaxy in the northern circumpolar constellation of Ursa Major. It was discovered by German-British astronomer William Herschel on 19 March 1790. In the Carnegie Atlas of Galaxies, it is described as being "characterized by an irregular pattern of dust lanes threaded through the disc in an'embryonic'spiral pattern indicating a mixed S0/Sa form." It is located near the Big Dipper, a little to the north of the mid-way point between the stars Alpha Ursae Majoris and Delta Ursae Majoris. With a visual magnitude of 10.7, it can be dimly viewed using a 4 in (10 cm) aperture telescope. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiob) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.3890309%2061.2957827&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 83. [AT2026airb](https://www.wis-tns.org/object/2026airb) near NGC7741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7741 as this object's host. The 0.69274° (41.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T15:15:50Z · 7 days · 21.04 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.69274° · 41.56′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.523%2026.7289&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 84. [AT2026airq](https://www.wis-tns.org/object/2026airq) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.66655° (39.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:23:12Z · 4 days · 23.72 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.66655° · 39.99′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.8700482%20-48.3211964&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 85. [AT2026aisu](https://www.wis-tns.org/object/2026aisu) near IC5181

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5181 as this object's host. The 0.85860° (51.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T01:12:07Z · 2 days · 19.52 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5181** · `IC5181` |
| Catalog display name | IC5181 |
| Type / constellation | Galaxy · Grus |
| Catalog magnitude / angular size | 11.5 · 2.65′ × 0.86′ |
| Distance | 24,800 kpc |
| Separation | 0.85860° · 51.52′ |
| Catalog description | The Telescopium−Grus Cloud is a galaxy filament in the constellations of Pavo, Indus, and Telescopium. It was first defined by astronomer Brent Tully in his book The Nearby Galaxies Atlas and its companion book The Nearby Galaxies Catalog. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.0733333%20-45.3299733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 86. [AT2026aisx](https://www.wis-tns.org/object/2026aisx) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.65992° (39.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 21.65 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4510....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4510....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Fornax B** · `NGC1317` |
| Catalog display name | Fornax B |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.9 · 3.1′ × 2.58′ |
| Distance | — |
| Separation | 0.65992° · 39.60′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.097246%20-37.570975&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 87. [AT2026aisy](https://www.wis-tns.org/object/2026aisy) near Fornax A

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax A as this object's host. The 0.92416° (55.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 22.37 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Fornax A** · `NGC1316` |
| Catalog display name | Fornax A |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 8.2 · 13.46′ × 7.71′ |
| Distance | — |
| Separation | 0.92416° · 55.45′ |
| Catalog description | NGC 1316 is a lenticular galaxy about 60 million light-years away in the constellation Fornax. It is a radio galaxy and at 1400 MHz the fourth-brightest radio source in the sky. It was discovered by Scottish astronomer James Dunlop on 2 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.237539%20-36.095757&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 88. [AT2026aitc](https://www.wis-tns.org/object/2026aitc) near NGC1427

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1427 as this object's host. The 0.53248° (31.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 22.01 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1427** · `NGC1427` |
| Catalog display name | NGC1427 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 10.9 · 4.33′ × 2.87′ |
| Distance | — |
| Separation | 0.53248° · 31.95′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=55.180194%20-36.128741&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 89. [AT2026aitj](https://www.wis-tns.org/object/2026aitj) near NGC4062

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4062 as this object's host. The 0.40955° (24.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:55:21Z · 7 days · 20.29 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC4062** · `NGC4062` |
| Catalog display name | NGC4062 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 11.2 · 4.14′ × 1.61′ |
| Distance | 14,550 kpc |
| Separation | 0.40955° · 24.57′ |
| Catalog description | NGC 4062 is a spiral galaxy in the constellation Ursa Major. The galaxy lies about 50 million light years away from Earth, which means, given its apparent dimensions, that NGC 4062 is approximately 50,000 light years across. It was discovered by William Herschel on March 20, 1787. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=181.2154989%2031.5244405&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 90. [AT2026aitm](https://www.wis-tns.org/object/2026aitm) near NGC3675

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3675 as this object's host. The 0.94795° (56.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:18:04Z · 6 days · 19.81 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3675** · `NGC3675` |
| Catalog display name | NGC3675 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.1 · 5.9′ × 3.27′ |
| Distance | — |
| Separation | 0.94795° · 56.88′ |
| Catalog description | NGC 3675 is a spiral galaxy located in the constellation Ursa Major. It is located at a distance of about 50 million light years from Earth, which, given its apparent dimensions, means that NGC 3675 is about 100,000 light years across. It was discovered by German-British astronomer William Herschel on 14 January 1788. NGC 3675 belongs to the Ursa Major Cluster, part of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=171.50148%2042.6382537&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 91. [AT2026aito](https://www.wis-tns.org/object/2026aito) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 0.37031° (22.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:24:52Z · 6 days · 20.21 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.37031° · 22.22′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aito) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.3222872%2037.0148923&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 92. [AT2026aitt](https://www.wis-tns.org/object/2026aitt) near IC 739

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 739 as this object's host. The 0.95329° (57.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T12:42:08Z · 4 days · 19.93 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 739** · `IC 739` |
| Catalog display name | NGC 3951 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 1.09′ × 0.76′ |
| Distance | — |
| Separation | 0.95329° · 57.20′ |
| Catalog description | NGC 3951 is a spiral galaxy located 300 million light-years away in the constellation Leo. It was discovered on April 10, 1785, by astronomer William Herschel. NGC 3951 is a member of a group of 5 galaxies known as [T2015] nest 100412 or the UGC 6846 Group, which is part of the Coma Supercluster. Other members of the group are UGC 6846, UGC 6855, IC 739, and 2MASX J11543515+2352505. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 739 has the different designation NGC 3951 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=178.4335688%2024.6718301&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 93. [AT2026aiup](https://www.wis-tns.org/object/2026aiup) near IC148

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC148 as this object's host. The 0.32866° (19.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:07:31Z · 7 days · 20.72 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC148** · `IC148` |
| Catalog display name | IC148 |
| Type / constellation | Galaxy · Pisces |
| Catalog magnitude / angular size | 13.8 · 1.82′ × 0.57′ |
| Distance | 9,245 kpc |
| Separation | 0.32866° · 19.72′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, very difficult, 660 south following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiup) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.5245754%2014.2954958&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 94. [AT2026aivt](https://www.wis-tns.org/object/2026aivt) near NGC864

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC864 as this object's host. The 0.37622° (22.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T16:50:52Z · 7 days · 22.44 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC864** · `NGC864` |
| Catalog display name | NGC864 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.1 · 3.72′ × 2.57′ |
| Distance | — |
| Separation | 0.37622° · 22.57′ |
| Catalog description | NGC 864 is a star-forming intermediate spiral galaxy located in the Cetus constellation. It's also classified as an isolated galaxy on the AMIGA catalogue as CIG 96. Its discovery and first description was realized by William Herschel in October 25th, 1785 and the findings made public through his Catalogue of Nebulae and Clusters of Stars, published in 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.057833%205.680458&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 95. [AT2026aivv](https://www.wis-tns.org/object/2026aivv) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 0.25518° (15.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:56:09Z · 5 days · 22.66 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.25518° · 15.31′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.212542%201.163614&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 96. [AT2026aiwb](https://www.wis-tns.org/object/2026aiwb) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.88875° (53.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:45:07Z · 3 days · 22.88 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Darth Vader's Galaxy** · `NGC936` |
| Catalog display name | Darth Vader's Galaxy |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 10.2 · 4.44′ × 3.18′ |
| Distance | 18,650 kpc |
| Separation | 0.88875° · 53.33′ |
| Catalog description | NGC 936 is a barred lenticular galaxy in the constellation Cetus. It is at a distance of about 60 million light-years away from Earth. Its nucleus and prominent bar have high surface brightness. Because of the shape of the prominent bar, the nucleus and the ring of stars at the end of the barrel, the galaxy has been compared with the shape of a TIE fighter, from the Star Wars universe, and thus NGC 936 has been named Darth Vader's Galaxy or Darth Vader's Starfighter. By measuring the radial velocity of the disc, Kormendy found in 1986 that the disc is stable, which is the reason why it is so smooth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.369125%20-0.446586&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 97. [AT2026aiwc](https://www.wis-tns.org/object/2026aiwc) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.41006° (24.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:45:07Z · 3 days · 22.4 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Darth Vader's Galaxy** · `NGC936` |
| Catalog display name | Darth Vader's Galaxy |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 10.2 · 4.44′ × 3.18′ |
| Distance | 18,650 kpc |
| Separation | 0.41006° · 24.60′ |
| Catalog description | NGC 936 is a barred lenticular galaxy in the constellation Cetus. It is at a distance of about 60 million light-years away from Earth. Its nucleus and prominent bar have high surface brightness. Because of the shape of the prominent bar, the nucleus and the ring of stars at the end of the barrel, the galaxy has been compared with the shape of a TIE fighter, from the Star Wars universe, and thus NGC 936 has been named Darth Vader's Galaxy or Darth Vader's Starfighter. By measuring the radial velocity of the disc, Kormendy found in 1986 that the disc is stable, which is the reason why it is so smooth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.147208%20-0.825983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 98. [AT2026aixg](https://www.wis-tns.org/object/2026aixg) near IC1895

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1895 as this object's host. The 0.41742° (25.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T12:34:32Z · 5 days · 20.63 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.41742° · 25.05′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, 2 stars (pl.) close preceding (westward) / pretty (adv., before F. B. L, S) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.997138%20-25.457798&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 99. [AT2026aiyg](https://www.wis-tns.org/object/2026aiyg) near IC2135

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2135 as this object's host. The 0.98727° (59.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T15:06:42Z · 1 days · 20.21 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2135** · `IC2135` |
| Catalog display name | IC2135 |
| Type / constellation | Galaxy · Columba |
| Catalog magnitude / angular size | 13.3 · 3.24′ × 0.66′ |
| Distance | 18,250 kpc |
| Separation | 0.98727° · 59.24′ |
| Catalog description | most extremely faint, extremely, excessively small in angular size, extremely, excessively extended, very difficult |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=83.400741%20-37.382812&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 100. [AT2026aiyy](https://www.wis-tns.org/object/2026aiyy) near NGC7457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7457 as this object's host. The 0.53496° (32.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:22:18Z · 4 days · 19.87 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.53496° · 32.10′ |
| Catalog description | NGC 7457 is an unbarred lenticular galaxy in the constellation Pegasus. NGC 7457 is its New General Catalogue designation. It was discovered by the astronomer William Herschel on 12 September 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.861474%2030.198849&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 101. [AT2026ajar](https://www.wis-tns.org/object/2026ajar) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 0.74868° (44.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 3 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3169** · `NGC3169` |
| Catalog display name | NGC3169 |
| Type / constellation | Galaxy · Sextans |
| Catalog magnitude / angular size | 10.9 · 4.34′ × 2.65′ |
| Distance | — |
| Separation | 0.74868° · 44.92′ |
| Catalog description | NGC 3169 is a spiral galaxy about 75 million light years away in the constellation Sextans. It has the morphological classification SA(s)a pec, which indicates this is a pure, unbarred spiral galaxy with tightly-wound arms and peculiar features. There is an asymmetrical spiral arm and an extended halo around the galaxy. It is a member of the NGC 3166 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajar) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.291333%203.643194&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 102. [AT2026ajbh](https://www.wis-tns.org/object/2026ajbh) near IC302

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC302 as this object's host. The 0.86924° (52.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T14:39:14Z · 1 days · 19.94 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC302** · `IC302` |
| Catalog display name | IC302 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 12.9 · 1.84′ × 1.2′ |
| Distance | 55,600 kpc |
| Separation | 0.86924° · 52.15′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, very small in angular size nucleus, or to a nucleus |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.243724%204.267417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 103. [AT2026ajbz](https://www.wis-tns.org/object/2026ajbz) near IC163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC163 as this object's host. The 0.66373° (39.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:08:52Z · 7 days · 20.81 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.66373° · 39.82′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.8778367%2021.2394728&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 104. [SN2026ahyd](https://www.wis-tns.org/object/2026ahyd) near IC5366

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 58/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5366 as this object's host. The 1.01813° (61.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.041 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:20:44Z · 7 days · 19.53 r |
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
| Subject | **IC5366** · `IC5366` |
| Catalog display name | IC5366 |
| Type / constellation | Nebula · Cassiopeia |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.01813° · 61.09′ |
| Catalog description | extremely, excessively large, much / magnitude extended (30'by 10') |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.7728239%2051.7970796&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 105. [SN2026agpt](https://www.wis-tns.org/object/2026agpt) near IC353

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 57/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC353 as this object's host. The 0.25824° (15.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.068 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T07:25:21Z · 21 days · 20.26 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4268....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4268....1S/abstract) |
| Classification references | [2026TNSCR4485....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4485....1S/abstract) |
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

[TNS object](https://www.wis-tns.org/object/2026agpt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.5280048%2025.9254261&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 106. [SN2026ahru](https://www.wis-tns.org/object/2026ahru) near IC1376

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 57/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1376 as this object's host. The 0.31912° (19.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.029 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:13:56Z · 10 days · 20.33 w |
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
| Subject | **IC1376** · `IC1376` |
| Catalog display name | IC1376 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.31912° · 19.15′ |
| Catalog description | no descr |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=320.9078844%20-5.9252208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 107. [AT2026aiba](https://www.wis-tns.org/object/2026aiba) near NGC2404

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2404 as this object's host. The 1.36391° (81.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T11:08:40Z · 8 days · 19 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiba) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.5782174%2065.6846644&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 108. [AT2026aibu](https://www.wis-tns.org/object/2026aibu) near IC640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC640 as this object's host. The 1.43879° (86.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:42:26Z · 17 days · 19.47 r |
| Latest public photometry | Not available in the staged feed |
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

### 109. [AT2026ailu](https://www.wis-tns.org/object/2026ailu) near IC1140

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1140 as this object's host. The 1.65700° (99.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T02:01:20Z · 15 days · 18.89 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1140** · `IC1140` |
| Catalog display name | IC1140 |
| Type / constellation | Nebula · Serpens Caput |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.65700° · 99.42′ |
| Catalog description | very faint (S Cl?), a single star 9.5 close |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ailu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=236.2136767%2017.8581501&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 110. [AT2026aimn](https://www.wis-tns.org/object/2026aimn) near van den Bergh 29 (VDB29)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 29 (VDB29) as this object's host. The 1.12187° (67.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:56:00Z · 4 days · 19.23 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4497....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4497....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **van den Bergh 29 (VDB29)** · `VDB29` |
| Catalog display name | van den Bergh 29 (VDB29) |
| Type / constellation | Nebula · Taurus |
| Catalog magnitude / angular size | 6.5 · — |
| Distance | — |
| Separation | 1.12187° · 67.31′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aimn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=73.300604%2029.507051&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 111. [AT2026airn](https://www.wis-tns.org/object/2026airn) near Barnard 224 (B224)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Barnard 224 (B224) as this object's host. The 1.10477° (66.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:11:58Z · 3 days · 18.52 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Barnard 224 (B224)** · `B224` |
| Catalog display name | Barnard 224 (B224) |
| Type / constellation | Dark nebula · Orion |
| Catalog magnitude / angular size | — · 20′ × 20′ |
| Distance | — |
| Separation | 1.10477° · 66.29′ |
| Catalog description | Indefinite; diam. 20' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026airn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=81.398796%209.715167&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 112. [AT2026aizl](https://www.wis-tns.org/object/2026aizl) near Lynds Dark Nebula 1563 (LDN1563)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1563 (LDN1563) as this object's host. The 1.36769° (82.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T09:35:04Z · 3 days · 18.61 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 1563 (LDN1563)** · `LDN1563` |
| Catalog display name | Lynds Dark Nebula 1563 (LDN1563) |
| Type / constellation | Dark nebula · Orion |
| Catalog magnitude / angular size | — · 15.44′ × 15.44′ |
| Distance | — |
| Separation | 1.36769° · 82.06′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aizl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=74.6590599%2012.575872&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 113. [AT2026aizq](https://www.wis-tns.org/object/2026aizq) near Lynds Bright Nebula 54 (LBN54)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 54 (LBN54) as this object's host. The 1.56600° (93.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:47:24Z · 1 days · 18.67 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 54 (LBN54)** · `LBN54` |
| Catalog display name | Lynds Bright Nebula 54 (LBN54) |
| Type / constellation | HII · Sagittarius |
| Catalog magnitude / angular size | — · 260′ × 40′ |
| Distance | — |
| Separation | 1.56600° · 93.96′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aizq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=301.381108%20-29.314672&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 114. [AT2026aiar](https://www.wis-tns.org/object/2026aiar) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.27730° (76.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:41:48Z · 7 days · 20.11 w |
| Latest public photometry | Not available in the staged feed |
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

### 115. [AT2026aibw](https://www.wis-tns.org/object/2026aibw) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.77222° (106.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:27:34Z · 6 days · 19.69 g |
| Latest public photometry | Not available in the staged feed |
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

### 116. [AT2026aick](https://www.wis-tns.org/object/2026aick) near NGC7410

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7410 as this object's host. The 1.11442° (66.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:52:52Z · 6 days · 19.75 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4429....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4429....1R/abstract) |
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
| Separation | 1.11442° · 66.87′ |
| Catalog description | NGC 7410 is a barred spiral galaxy located in the constellation Grus. It is about 122 million light-years away. It was discovered on 15 July 1826, by James Dunlop. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aick) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.576785%20-39.0143325&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 117. [AT2026aicx](https://www.wis-tns.org/object/2026aicx) near IC 21

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 21 as this object's host. The 1.65583° (99.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:38Z · 7 days · 20.09 L |
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
| Subject | **IC 21** · `IC 21` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.49′ × 0.45′ |
| Distance | — |
| Separation | 1.65583° · 99.35′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 21 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=8.8010075%200.521135&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 118. [AT2026aidv](https://www.wis-tns.org/object/2026aidv) near IC 5298

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5298 as this object's host. The 1.04272° (62.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T04:07:55Z · 5 days · 19.73 r |
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
| Subject | **IC 5298** · `IC 5298` |
| Catalog display name | NGC4632 |
| Type / constellation | Galaxy · Peg |
| Catalog magnitude / angular size | — · 0.79′ × 0.7′ |
| Distance | — |
| Separation | 1.04272° · 62.56′ |
| Catalog description | NGC 4632 is a spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background for is 2,061±24 km/s, which corresponds to a Hubble distance of 99.2 ± 7.0 Mly (30.40 ± 2.16 Mpc). However, 15 non-redshift measurements give a much closer distance of 54.12 ± 3.04 Mly (16.593 ± 0.931 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5298 has the different designation NGC4632 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aidv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.5201053%2024.6100872&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 119. [AT2026aiin](https://www.wis-tns.org/object/2026aiin) near NGC1084

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1084 as this object's host. The 1.58124° (94.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:02:50Z · 7 days · 20.59 g |
| Latest public photometry | Not available in the staged feed |
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

### 120. [AT2026aijo](https://www.wis-tns.org/object/2026aijo) near NGC1055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1055 as this object's host. The 1.04248° (62.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T12:08:33Z · 5 days · 20.25 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4472....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4472....1O/abstract) |
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
| Separation | 1.04248° · 62.55′ |
| Catalog description | NGC 1055 is an edge-on spiral galaxy located in the constellation Cetus. The galaxy has a prominent nuclear bulge crossed by a wide, knotty, dark lane of dust and gas. The spiral arm structure appears to be elevated above the galaxy's plane and obscures the upper half of the bulge. It was discovered by German-British astronomer William Herschel on December 18, 1783, from his home in Slough, England. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=39.6064088%20-0.1861723&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 121. [AT2026aijx](https://www.wis-tns.org/object/2026aijx) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.48110° (88.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:31Z · 4 days · 21.8 r |
| Latest public photometry | Not available in the staged feed |
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

### 122. [AT2026aika](https://www.wis-tns.org/object/2026aika) near IC 1776

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
| Discovery | 2026-11-03T05:55:04Z · 7 days · 20.36 r |
| Latest public photometry | Not available in the staged feed |
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

### 123. [AT2026aikq](https://www.wis-tns.org/object/2026aikq) near NGC 4150

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4150 as this object's host. The 1.54182° (92.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:55:21Z · 7 days · 20.18 r |
| Latest public photometry | Not available in the staged feed |
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

### 124. [AT2026aikv](https://www.wis-tns.org/object/2026aikv) near NGC628

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC628 as this object's host. The 1.77250° (106.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:08:13Z · 7 days · 20.5 r |
| Latest public photometry | Not available in the staged feed |
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

### 125. [AT2026aikw](https://www.wis-tns.org/object/2026aikw) near IC 186 A

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
| Discovery | 2026-11-03T05:59:53Z · 7 days · 20.06 r |
| Latest public photometry | Not available in the staged feed |
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

### 126. [AT2026aikx](https://www.wis-tns.org/object/2026aikx) near IC 1730

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
| Discovery | 2026-11-05T08:41:41Z · 5 days · 20.65 g |
| Latest public photometry | Not available in the staged feed |
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

### 127. [AT2026aikz](https://www.wis-tns.org/object/2026aikz) near Arp 147

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Arp 147 as this object's host. The 1.07092° (64.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:35:00Z · 6 days · 19.88 L |
| Latest public photometry | Not available in the staged feed |
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

### 128. [AT2026ailf](https://www.wis-tns.org/object/2026ailf) near IC5338

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5338 as this object's host. The 1.89253° (113.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:02:04Z · 4 days · 20.95 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.89253° · 113.55′ |
| Catalog description | IC 5337 or JW100, is a spiral galaxy located 800 million light-years away from the Solar System in the constellation of Pegasus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ailf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.1568055%2021.6180683&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026ailh](https://www.wis-tns.org/object/2026ailh) near IC 16

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 16 as this object's host. The 1.81588° (108.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T07:45:44Z · 4 days · 21.27 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 16** · `IC 16` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.58′ × 0.32′ |
| Distance | — |
| Separation | 1.81588° · 108.95′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 16 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ailh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.1791624%20-12.8977769&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026ainl](https://www.wis-tns.org/object/2026ainl) near IC 2973

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2973 as this object's host. The 1.85833° (111.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:46:04Z · 7 days · 19.67 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 2973** · `IC 2973` |
| Catalog display name | NGC 623 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | — · 1.42′ × 0.82′ |
| Distance | — |
| Separation | 1.85833° · 111.50′ |
| Catalog description | NGC 623 is a large elliptical galaxy located in the Sculptor constellation at a distance of about 400 million light-years away from the Milky Way. It was discovered by British astronomer John Herschel on 30 November 1837. NGC 623 is a large elliptical galaxy located in the Sculptor constellation at a distance of about 400 million light-years away from the Milky Way. It was discovered by British astronomer John Herschel on 30 November 1837. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2973 has the different designation NGC 623 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=177.9516113%2031.5576422&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026aiod](https://www.wis-tns.org/object/2026aiod) near IC 17

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 17 as this object's host. The 1.30850° (78.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T05:00:05Z · 5 days · 20.35 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 17** · `IC 17` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.67′ × 0.54′ |
| Distance | — |
| Separation | 1.30850° · 78.51′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 17 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiod) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.8283251%202.4575066&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026aion](https://www.wis-tns.org/object/2026aion) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.67303° (100.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:13:05Z · 7 days · 20.12 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.67303° · 100.38′ |
| Catalog description | NGC 891 is an edge-on unbarred spiral galaxy about 30 million light-years away in the constellation Andromeda. It was discovered by William Herschel on October 6, 1784. The galaxy is a member of the NGC 1023 group of galaxies in the Local Supercluster. It has an H II nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aion) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.3259593%2044.0066728&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 133. [AT2026aior](https://www.wis-tns.org/object/2026aior) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.68195° (100.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T16:24:57Z · 7 days · 22.61 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.68195° · 100.92′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aior) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.372458%203.853833&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 134. [AT2026airi](https://www.wis-tns.org/object/2026airi) near NGC636

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.79687° (107.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T11:07:26Z · 3 days · 20.14 L |
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
| Separation | 1.79687° · 107.81′ |
| Catalog description | NGC 636 is an elliptical galaxy in the Cetus constellation. It is located about 96 million light-years from the Milky Way. It was discovered by the German–British astronomer William Herschel in 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.8348337%20-5.7167276&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 135. [AT2026airp](https://www.wis-tns.org/object/2026airp) near IC1734

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1734 as this object's host. The 1.46402° (87.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T11:22:08Z · 5 days · 20 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1734** · `IC1734` |
| Catalog display name | IC1734 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 12.9 · 1.63′ × 1.52′ |
| Distance | — |
| Separation | 1.46402° · 87.84′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, little (adv.); long (adj.) extended 100deg , brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.594283%20-31.29706&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 136. [AT2026airu](https://www.wis-tns.org/object/2026airu) near IC5065

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5065 as this object's host. The 1.63610° (98.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T00:26:24Z · 2 days · 21.49 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.63610° · 98.17′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=313.3809487%20-28.2577609&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 137. [AT2026aisb](https://www.wis-tns.org/object/2026aisb) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.38375° (83.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T08:17:34Z · 2 days · 23.29 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.38375° · 83.03′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.5605461%20-49.9626432&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 138. [AT2026aisz](https://www.wis-tns.org/object/2026aisz) near IC 1906

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1906 as this object's host. The 1.46114° (87.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 21.06 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1906** · `IC 1906` |
| Catalog display name | IC 1613 |
| Type / constellation | Galaxy · For |
| Catalog magnitude / angular size | — · 1.21′ × 0.51′ |
| Distance | — |
| Separation | 1.46114° · 87.67′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1906 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.802783%20-35.675059&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 139. [AT2026aitb](https://www.wis-tns.org/object/2026aitb) near NGC1350

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1350 as this object's host. The 1.28617° (77.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 2 days · 21.49 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1350** · `NGC1350` |
| Catalog display name | NGC1350 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.3 · 5.18′ × 2.6′ |
| Distance | 18,500 kpc |
| Separation | 1.28617° · 77.17′ |
| Catalog description | NGC 1350 is a spiral galaxy located 87 million light years away in the southern constellation Fornax. It was discovered by Scottish astronomer James Dunlop on 24 November 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.317254%20-32.422879&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 140. [AT2026aiua](https://www.wis-tns.org/object/2026aiua) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.07394° (64.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T12:35:00Z · 5 days · 20.14 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.07394° · 64.44′ |
| Catalog description | NGC 2775, also known as Caldwell 48, is a spiral galaxy in the constellation Cancer. It is 67 million light-years away from the Milky Way. It was discovered by German-British astronomer William Herschel on 19 December 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiua) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=137.9573703%208.0458396&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 141. [AT2026aiue](https://www.wis-tns.org/object/2026aiue) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.53875° (92.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T03:27:21Z · 5 days · 20.32 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1417** · `IC 1417` |
| Catalog display name | IC 1459 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 1.65′ × 0.54′ |
| Distance | 85 ly |
| Separation | 1.53875° · 92.33′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiue) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.4834476%20-12.4253573&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 142. [AT2026aiun](https://www.wis-tns.org/object/2026aiun) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.41669° (85.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T09:47:31Z · 7 days · 20.54 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.41669° · 85.00′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiun) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.5662017%200.1561255&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 143. [AT2026aius](https://www.wis-tns.org/object/2026aius) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.88178° (112.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T06:19:17Z · 4 days · 19.94 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC797** · `IC 80 NED02` |
| Catalog display name | NGC797 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 1.5′ × 1.06′ |
| Distance | — |
| Separation | 1.88178° · 112.91′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aius) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.1790365%20-13.7731417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026aivi](https://www.wis-tns.org/object/2026aivi) near IC 1797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1797 as this object's host. The 1.40546° (84.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:53:01Z · 7 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4538....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4538....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1797** · `IC 1797` |
| Catalog display name | NGC 932 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.97′ × 0.37′ |
| Distance | — |
| Separation | 1.40546° · 84.33′ |
| Catalog description | NGC 932 is a spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 3,837±17 km/s, which corresponds to a Hubble distance of 184.6 ± 12.9 Mly (56.59 ± 3.97 Mpc). It was discovered by German-British astronomer William Herschel on 29 November 1785. There has been a longstanding confusion between this galaxy and NGC 930, which is a nonexistent object. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1797 has the different designation NGC 932 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.8618328%2021.7196375&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026aivw](https://www.wis-tns.org/object/2026aivw) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.24572° (74.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T18:01:26Z · 5 days · 21.91 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.24572° · 74.74′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.258542%200.318439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026aiwu](https://www.wis-tns.org/object/2026aiwu) near IC 1568

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1568 as this object's host. The 1.34453° (80.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:22:30Z · 4 days · 20.14 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1568** · `IC 1568` |
| Catalog display name | NGC4378 |
| Type / constellation | Galaxy · Psc |
| Catalog magnitude / angular size | — · 1.15′ × 0.87′ |
| Distance | — |
| Separation | 1.34453° · 80.67′ |
| Catalog description | NGC 4378 is a spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 2,903±24 km/s, which corresponds to a Hubble distance of 139.7 ± 9.8 Mly (42.82 ± 3.02 Mpc). Also, six non-redshift measurements give a similar distance of 136.50 ± 16.23 Mly (41.850 ± 4.975 Mpc). It was discovered by German-British astronomer William Herschel on 2 February 1786. It is a member of the Virgo Cluster, listed as VCC 785. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1568 has the different designation NGC4378 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.6938485%205.5351742&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 147. [AT2026aixb](https://www.wis-tns.org/object/2026aixb) near IC1508

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1508 as this object's host. The 1.64877° (98.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:25:41Z · 1 days · 20.2 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1508** · `IC1508` |
| Catalog display name | IC1508 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 13.4 · 0.76′ × 0.37′ |
| Distance | — |
| Separation | 1.64877° · 98.93′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) large, extended north-south |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.718773%2011.364164&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026aiye](https://www.wis-tns.org/object/2026aiye) near IC1616

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1616 as this object's host. The 1.28647° (77.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T11:05:38Z · 3 days · 19.93 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.28647° · 77.19′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, 3 stars (pl.) irregular north little (adv.); long (adj.) irregular north extremely, excessively near |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiye) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.063801%20-26.437733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026aiyh](https://www.wis-tns.org/object/2026aiyh) near IC2152

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2152 as this object's host. The 1.16508° (69.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T14:57:38Z · 5 days · 20.26 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.16508° · 69.90′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, several bright stars (pl.) following (eastward) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.686947%20-24.211454&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 150. [AT2026aizb](https://www.wis-tns.org/object/2026aizb) near IC 1776

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1776 as this object's host. The 1.97947° (118.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T08:40:18Z · 2 days · 20.76 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97947° · 118.77′ |
| Catalog description | IC 2574, also known as Coddington's Nebula, is a dwarf spiral galaxy discovered by American astronomer Edwin Foster Coddington in 1898. Located in Ursa Major, a constellation in the northern sky, it is an outlying member of the M81 Group. It is believed that 90% of its mass is in the form of dark matter. IC 2574 does not show evidence of interaction with other galaxies. It is currently forming stars; a UV analysis showed clumps of star formation 85 to 500 light-years in size. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1776 has the different designation IC 2574 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.9392465%208.0511641&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 151. [AT2026ajbj](https://www.wis-tns.org/object/2026ajbj) near IC2007

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2007 as this object's host. The 1.79494° (107.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T13:58:26Z · 1 days · 20.17 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2007** · `IC2007` |
| Catalog display name | IC2007 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 13.7 · 1.29′ × 0.6′ |
| Distance | 22,300 kpc |
| Separation | 1.79494° · 107.70′ |
| Catalog description | extremely, excessively faint, small in angular size, round, faint a single star attached north following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=57.765057%20-29.686055&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 152. [AT2026ajbo](https://www.wis-tns.org/object/2026ajbo) near NGC 4346

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4346 as this object's host. The 1.29956° (77.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:48:55Z · 0 days · 19.95 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 4346** · `NGC 4346` |
| Catalog display name | NGC 4346 |
| Type / constellation | Galaxy · CVn |
| Catalog magnitude / angular size | 12.14 · 3.13′ × 1.13′ |
| Distance | — |
| Separation | 1.29956° · 77.97′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=187.7603579%2046.8666574&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026ajbr](https://www.wis-tns.org/object/2026ajbr) near NGC2841

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2841 as this object's host. The 1.54687° (92.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:55:42Z · 7 days · 20.52 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.54687° · 92.81′ |
| Catalog description | NGC 2841 is an unbarred spiral galaxy in the northern circumpolar constellation of Ursa Major. It was discovered on 9 March, 1788 by German-born astronomer William Herschel. J. L. E. Dreyer, the author of the New General Catalogue, described it as, "very bright, large, very much extended 151°, very suddenly much brighter middle equal to 10th magnitude star". Initially thought to be about 30 million light-years distant, a 2001 Hubble Space Telescope survey of the galaxy's Cepheid variables determined its distance to be approximately 14.1 megaparsecs, or 46 million light-years. The optical size of the galaxy is 8.1′ × 3.5′. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.1064581%2050.6747332&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 154. [AT2026ajbw](https://www.wis-tns.org/object/2026ajbw) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 1.68563° (101.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T12:58:39Z · 1 days · 20.02 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.68563° · 101.14′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.5287691%20-1.9290868&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 155. [AT2026ajby](https://www.wis-tns.org/object/2026ajby) near IC48

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC48 as this object's host. The 1.83970° (110.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T03:31:31Z · 1 days · 20.2 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC48** · `IC48` |
| Catalog display name | IC48 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.2 · 1.12′ × 0.92′ |
| Distance | 88,600 kpc |
| Separation | 1.83970° · 110.38′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, small in angular size (var brightness?) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajby) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.8589474%20-6.3470906&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 156. [AT2026ajcl](https://www.wis-tns.org/object/2026ajcl) near IC 1873

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1873 as this object's host. The 1.66353° (99.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:29:12Z · 5 days · 20.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1873** · `IC 1873` |
| Catalog display name | NGC 7466 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 1.17′ × 0.46′ |
| Distance | — |
| Separation | 1.66353° · 99.81′ |
| Catalog description | NGC 7466 is a spiral galaxy in the constellation of Pegasus. Its velocity with respect to the cosmic microwave background is 7160 ± 25 km/s, which corresponds to a Hubble distance of 105.60 ± 7.40 Mpc. It was discovered by French astronomer Édouard Stephan on 20 September 1873. It was independently rediscovered by the French astronomer Guillaume Bigourdan on 19 November 1895 and listed as IC 5281 in the Index Catalogue. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1873 has the different designation NGC 7466 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=45.85227%2011.2727208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 157. [AT2026ajcz](https://www.wis-tns.org/object/2026ajcz) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.96765° (118.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:24:52Z · 6 days · 19.92 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.96765° · 118.06′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.351529%2039.7659917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 158. [AT2026ahsf](https://www.wis-tns.org/object/2026ahsf) near IC1892

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1892 as this object's host. The 0.43473° (26.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:03:20Z · 11 days · 20.36 L |
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
| Subject | **IC1892** · `IC1892` |
| Catalog display name | IC1892 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 13.8 · 1.78′ × 0.98′ |
| Distance | — |
| Separation | 0.43473° · 26.08′ |
| Catalog description | very faint, large, near 1230 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahsf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.0403446%20-23.4854218&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 159. [AT2026ahsm](https://www.wis-tns.org/object/2026ahsm) near IC1796

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1796 as this object's host. The 0.47424° (28.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T12:27:19Z · 13 days · 19.9 L |
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

### 160. [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 0.59209° (35.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:45:50Z · 9 days · 19.59 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.618572%20-52.441701&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 161. [AT2026aiax](https://www.wis-tns.org/object/2026aiax) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.49618° (29.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:23:51Z · 11 days · 22.27 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiax) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=61.4588819%20-47.6509559&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 162. [AT2026aibf](https://www.wis-tns.org/object/2026aibf) near IC1784

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1784 as this object's host. The 0.51346° (30.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T19:14:52Z · 24 days · 21.48 r |
| Latest public photometry | Not available in the staged feed |
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

### 163. [AT2026aimu](https://www.wis-tns.org/object/2026aimu) near NGC7585

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7585 as this object's host. The 0.67498° (40.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:53:56Z · 11 days · 20.91 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7585** · `NGC7585` |
| Catalog display name | NGC7585 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 11.4 · 2.55′ × 1.92′ |
| Distance | — |
| Separation | 0.67498° · 40.50′ |
| Catalog description | NGC 7585 is a lenticular galaxy with a peculiar shape resulting from an interaction between two galaxies. It is located 145 million light years away in the constellation Aquarius which, given its apparent dimensions, means that NGC 7585 is about 100,000 light years across. It was discovered by William Herschel on September 20, 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.6032792%20-5.3180287&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 164. [AT2026aimv](https://www.wis-tns.org/object/2026aimv) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 0.99831° (59.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:58:33Z · 11 days · 21.54 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.99831° · 59.90′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.0118617%20-12.741879&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 165. [AT2026ains](https://www.wis-tns.org/object/2026ains) near NGC1961

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1961 as this object's host. The 0.68080° (40.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T12:25:44Z · 17 days · 19.94 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1961** · `NGC1961` |
| Catalog display name | NGC1961 |
| Type / constellation | Galaxy · Camelopardalis |
| Catalog magnitude / angular size | 11 · 4.42′ × 3.1′ |
| Distance | — |
| Separation | 0.68080° · 40.85′ |
| Catalog description | NGC 1961 is a spiral galaxy in the constellation Camelopardalis. It was discovered by German-British astronomer William Herschel on 3 December 1788. It was also observed by Guillaume Bigourdan on 22 December 1891, causing it to be listed in the Index Catalogue as IC 2133. Its velocity with respect to the cosmic microwave background for is 3,909±2 km/s, which corresponds to a Hubble distance of 188.0 ± 13.2 Mly (57.65 ± 4.04 Mpc). However, seven non redshift measurements give a much closer distance of 145.42 ± 27.36 Mly (44.586 ± 8.390 Mpc). |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ains) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=84.9448526%2070.0297196&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 166. [AT2026aipd](https://www.wis-tns.org/object/2026aipd) near IC 1746

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1746 as this object's host. The 0.30858° (18.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:09:36Z · 13 days · 21.22 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.30858° · 18.51′ |
| Catalog description | NGC 502, also occasionally referred to as PGC 5034 or UGC 922, is a lenticular galaxy in the constellation Pisces. It is located approximately 113 million light-years from the Solar System and was discovered on 25 September 1862 by German astronomer Heinrich Louis d'Arrest. When the Morphological Catalogue of Galaxies was published between 1962 and 1974, the identifications of NGC 502 and NGC 505 were reversed. In reality, NGC 502 is equal to MGC +01-04-041 and not MCG +01-04-043 as noted in the catalogue. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1746 has the different designation NGC 502 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.909917%204.829272&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 167. [AT2026aiph](https://www.wis-tns.org/object/2026aiph) near Caldwell 51 (C51)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 51 (C51) as this object's host. The 0.47650° (28.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:36:57Z · 9 days · 22.48 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.47650° · 28.59′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiph) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.4925%202.490856&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 168. [AT2026aivo](https://www.wis-tns.org/object/2026aivo) near NGC864

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC864 as this object's host. The 0.76363° (45.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:10:04Z · 9 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC864** · `NGC864` |
| Catalog display name | NGC864 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.1 · 3.72′ × 2.57′ |
| Distance | — |
| Separation | 0.76363° · 45.82′ |
| Catalog description | NGC 864 is a star-forming intermediate spiral galaxy located in the Cetus constellation. It's also classified as an isolated galaxy on the AMIGA catalogue as CIG 96. Its discovery and first description was realized by William Herschel in October 25th, 1785 and the findings made public through his Catalogue of Nebulae and Clusters of Stars, published in 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.562833%206.316167&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 169. [AT2026aixe](https://www.wis-tns.org/object/2026aixe) near IC1860

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1860 as this object's host. The 0.49089° (29.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:04:26Z · 12 days · 20.05 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1860** · `IC1860` |
| Catalog display name | IC1860 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 12.6 · 2.64′ × 1.8′ |
| Distance | 95,750 kpc |
| Separation | 0.49089° · 29.45′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, little (adv.); long (adj.) extended, 3rd of 3 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=42.155425%20-30.740371&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 170. [AT2026aiyi](https://www.wis-tns.org/object/2026aiyi) near IC1628

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1628 as this object's host. The 0.47290° (28.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:33:11Z · 12 days · 20.5 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1628** · `IC1628` |
| Catalog display name | IC1628 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 12.5 · 1.65′ × 1.53′ |
| Distance | — |
| Separation | 0.47290° · 28.37′ |
| Catalog description | considerably bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, 3 stars (pl.) 8 near |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.750115%20-28.317645&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026ajai](https://www.wis-tns.org/object/2026ajai) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.59906° (35.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:05:16Z · 11 days · 22.25 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.59906° · 35.94′ |
| Catalog description | NGC 741, also known as PGC 7252, is a formerly active radio galaxy in the constellation of Pisces. Located 74.13 Mpc away, NGC 741 is part of a group of galaxies including NGC 742 and PGC 7250. NGC 741 and NGC 742 recently collided, although the disruption was minor. Radio filaments have been found connecting NGC 741 to NGC 742, and due to the bent structure of the radio filaments, NGC 741 is estimated to be moving at 1400 km/s with respect to its local group, suggesting that ram-pressure stripping was created as a product of the former merger. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajai) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.661167%205.810744&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 172. [AT2026ajaj](https://www.wis-tns.org/object/2026ajaj) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 0.93441° (56.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:08:09Z · 11 days · 22.02 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.93441° · 56.06′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajaj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.751583%200.342597&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 173. [AT2026ajax](https://www.wis-tns.org/object/2026ajax) near IC509

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC509 as this object's host. The 0.40100° (24.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T22:19:12Z · 29 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC509** · `IC509` |
| Catalog display name | IC509 |
| Type / constellation | Galaxy · Cancer |
| Catalog magnitude / angular size | 13.2 · 1.02′ × 0.92′ |
| Distance | 12,600 kpc |
| Separation | 0.40100° · 24.06′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) large, diffused, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajax) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.619125%2024.189408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 174. [AT2026aiko](https://www.wis-tns.org/object/2026aiko) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38099° (22.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:02:26Z · 4 days · 19.85 r |
| Latest public photometry | Not available in the staged feed |
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

### 175. [AT2026aimh](https://www.wis-tns.org/object/2026aimh) near IC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC488 as this object's host. The 0.45906° (27.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T11:11:03Z · 4 days · 20.12 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.45906° · 27.54′ |
| Catalog description | very faint, small in angular size, diffused, a star of 13th magnitude south preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.7469738%2025.6986102&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 176. [AT2026aiog](https://www.wis-tns.org/object/2026aiog) near Cleopatra's eye

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Cleopatra's eye as this object's host. The 0.80675° (48.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:14:48Z · 7 days · 20.42 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Cleopatra's eye** · `NGC 1535` |
| Catalog display name | Cleopatra's eye |
| Type / constellation | Planetary nebula · Eri |
| Catalog magnitude / angular size | — · 0.33′ × 0.28′ |
| Distance | — |
| Separation | 0.80675° · 48.41′ |
| Catalog description | NGC 1535, also known as Cleopatra's Eye, is a planetary nebula in the constellation of Eridanus, discovered by William Herschel on February 1, 1785. It is very similar to the Eskimo Nebula in both color and structure but the central star can be quite difficult to observe visually. The object is included in the Astronomical League's Herschel 400 Observing Program. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiog) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.8583911%20-11.9770369&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 177. [AT2026aisd](https://www.wis-tns.org/object/2026aisd) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 0.36810° (22.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:50:41Z · 2 days · 23.49 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.36810° · 22.09′ |
| Catalog description | faint, small in angular size, considerably extended north-south, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.7838498%20-48.628987&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 178. [AT2026aisr](https://www.wis-tns.org/object/2026aisr) near NGC1900

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1900 as this object's host. The 0.38063° (22.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:54Z · 4 days · 19.69 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1900** · `NGC1900` |
| Catalog display name | NGC1900 |
| Type / constellation | Open cluster · Dorado |
| Catalog magnitude / angular size | 13.6 · 1.8′ × 1.6′ |
| Distance | 47 kpc |
| Separation | 0.38063° · 22.84′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=79.0857557%20-63.2341286&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 179. [AT2026aivj](https://www.wis-tns.org/object/2026aivj) near IC1547

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1547 as this object's host. The 0.56565° (33.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T08:18:10Z · 5 days · 20.47 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.56565° · 33.94′ |
| Catalog description | eF.pS, suddenly (abruptly) / south brighter middle, or in the middle a single star |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.9514231%2022.7451279&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 180. [AT2026aiwl](https://www.wis-tns.org/object/2026aiwl) near IC5344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5344 as this object's host. The 0.90611° (54.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T10:43:03Z · 4 days · 20.35 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5344** · `IC5344` |
| Catalog display name | IC5344 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.90611° · 54.37′ |
| Catalog description | very faint, large, others near |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.60002%20-4.513882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 181. [AT2026aiws](https://www.wis-tns.org/object/2026aiws) near Collinder 59 (CR59)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 59 (CR59) as this object's host. The 0.80866° (48.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T09:40:03Z · 5 days · 20.91 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 59 (CR59)** · `CR59` |
| Catalog display name | Collinder 59 (CR59) |
| Type / constellation | Open cluster · Taurus |
| Catalog magnitude / angular size | 7 · 5.4′ × 5.4′ |
| Distance | — |
| Separation | 0.80866° · 48.52′ |
| Catalog description | NGC 1807 is an asterism at the border of the constellations Orion and Taurus near the open cluster NGC 1817. NGC 1807 has an apparent size of 5.4'and an apparent magnitude of 7.0. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiws) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.9234498%2016.1716185&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 182. [AT2026aixd](https://www.wis-tns.org/object/2026aixd) near NGC7826

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7826 as this object's host. The 0.88575° (53.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T09:57:26Z · 5 days · 20 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7826** · `NGC7826` |
| Catalog display name | NGC7826 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · 12′ × 12′ |
| Distance | — |
| Separation | 0.88575° · 53.15′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.463425%20-21.049051&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 183. [AT2026ajan](https://www.wis-tns.org/object/2026ajan) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.77578° (46.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T17:03:50Z · 6 days · 22.15 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7668** · `NGC7668` |
| Catalog display name | NGC7668 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.77578° · 46.55′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajan) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.079042%20-0.028278&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 184. [AT2026ajdc](https://www.wis-tns.org/object/2026ajdc) near IC240

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC240 as this object's host. The 0.55882° (33.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:13:05Z · 7 days · 19.73 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.55882° · 33.53′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=39.4326826%2042.228844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 185. [AT2026ahnp](https://www.wis-tns.org/object/2026ahnp) near Sharpless 122 (SH2-122)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 122 (SH2-122) as this object's host. The 1.14210° (68.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T21:24:40Z · 12 days · 18.54 L |
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
| Subject | **Sharpless 122 (SH2-122)** · `SH2-122` |
| Catalog display name | Sharpless 122 (SH2-122) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 40′ × 40′ |
| Distance | — |
| Separation | 1.14210° · 68.53′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ahnp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.1296236%2014.5834124&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 186. [AT2026afve](https://www.wis-tns.org/object/2026afve) near IC 1931

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1931 as this object's host. The 1.91599° (114.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T09:53:06Z · 23 days · 20.21 r |
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
| Separation | 1.91599° · 114.96′ |
| Catalog description | NGC 5162 is a very large spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 7125 ± 20 km/s, which corresponds to a Hubble distance of 342.8 ± 24.0 Mly (105.09 ± 7.36 Mpc). In addition, 11 non redshift measurements give a distance of 303.71 ± 12.41 Mly (93.118 ± 3.806 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 15 March 1784. It was also observed by Lewis Swift on 19 April 1887, resulting in the galaxy being included twice in the New General Catalogue, as both NGC 5162 and NGC 5174. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1931 has the different designation NGC5162 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afve) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.419504%203.2619141&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 187. [AT2026agyb](https://www.wis-tns.org/object/2026agyb) near IC5201

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5201 as this object's host. The 1.07201° (64.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T10:28:36Z · 14 days · 19.63 L |
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

### 188. [AT2026ahbv](https://www.wis-tns.org/object/2026ahbv) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.53637° (92.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T10:02:19Z · 13 days · 19.86 L |
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

### 189. [AT2026ahdm](https://www.wis-tns.org/object/2026ahdm) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.56833° (94.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T13:52:19Z · 13 days · 21.64 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4371....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4371....1X/abstract) |
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
| Separation | 1.56833° · 94.10′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahdm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.7667355%200.2487603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 190. [AT2026ahho](https://www.wis-tns.org/object/2026ahho) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.70871° (102.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:59:10Z · 11 days · 21.9 r |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahho) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.8608986%20-11.9832835&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 191. [AT2026ahhy](https://www.wis-tns.org/object/2026ahhy) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.55641° (93.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:57:54Z · 11 days · 21.58 r |
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
| Subject | **NGC7606** · `NGC7606` |
| Catalog display name | NGC7606 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 11 · 5.26′ × 4.47′ |
| Distance | — |
| Separation | 1.55641° · 93.38′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahhy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.335184%20-8.3627722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 192. [AT2026ahiv](https://www.wis-tns.org/object/2026ahiv) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.93793° (116.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:33:32Z · 11 days · 22.17 i |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahiv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.4642577%20-15.4103602&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 193. [AT2026aibd](https://www.wis-tns.org/object/2026aibd) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 1.35024° (81.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:19:40Z · 13 days · 21.48 r |
| Latest public photometry | Not available in the staged feed |
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

### 194. [AT2026aibz](https://www.wis-tns.org/object/2026aibz) near IC334

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC334 as this object's host. The 1.51904° (91.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T09:21:30Z · 15 days · 19.66 r |
| Latest public photometry | Not available in the staged feed |
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

### 195. [AT2026aicm](https://www.wis-tns.org/object/2026aicm) near IC 2039

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2039 as this object's host. The 1.00001° (60.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:09:56Z · 9 days · 19.97 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.531499%20-56.281986&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026aico](https://www.wis-tns.org/object/2026aico) near IC 33

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
| Discovery | 2026-10-28T11:14:08Z · 13 days · 19.65 L |
| Latest public photometry | Not available in the staged feed |
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

### 197. [AT2026aicp](https://www.wis-tns.org/object/2026aicp) near IC5270

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5270 as this object's host. The 1.45156° (87.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T09:54:42Z · 13 days · 20.02 L |
| Latest public photometry | Not available in the staged feed |
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

### 198. [AT2026aicw](https://www.wis-tns.org/object/2026aicw) near IC1574

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1574 as this object's host. The 1.16063° (69.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:16:36Z · 12 days · 19.96 L |
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
| Subject | **IC1574** · `IC1574` |
| Catalog display name | IC1574 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.9 · 1.83′ × 0.7′ |
| Distance | 4,910 kpc |
| Separation | 1.16063° · 69.64′ |
| Catalog description | IC 1574 is an irregular galaxy 17 million light-years from Earth. It is a member of the Sculptor Group, a group of galaxies near the Local Group. It was discovered by DeLisle Stewart on 3 November 1898. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.5216496%20-22.0840133&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 199. [AT2026aieg](https://www.wis-tns.org/object/2026aieg) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.01519° (60.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:59:10Z · 11 days · 21.47 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4448....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4448....1M/abstract) |
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
| Separation | 1.01519° · 60.91′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aieg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.6847157%20-13.2347762&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 200. [AT2026aigp](https://www.wis-tns.org/object/2026aigp) near IC2007

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2007 as this object's host. The 1.25561° (75.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:17:49Z · 9 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4452....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4452....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2007** · `IC2007` |
| Catalog display name | IC2007 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 13.7 · 1.29′ × 0.6′ |
| Distance | 22,300 kpc |
| Separation | 1.25561° · 75.34′ |
| Catalog description | extremely, excessively faint, small in angular size, round, faint a single star attached north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aigp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.4436153%20-27.0216875&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 201. [AT2026aihe](https://www.wis-tns.org/object/2026aihe) near NGC2855

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2855 as this object's host. The 1.17126° (70.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:32Z · 9 days · 19.64 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4452....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4452....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2855** · `NGC2855` |
| Catalog display name | NGC2855 |
| Type / constellation | Galaxy · Hydra |
| Catalog magnitude / angular size | 11.1 · 3.45′ × 1.85′ |
| Distance | 24,250 kpc |
| Separation | 1.17126° · 70.28′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aihe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=139.1940827%20-12.1664773&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026aiit](https://www.wis-tns.org/object/2026aiit) near IC 536

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
| Discovery | 2026-10-26T12:16:17Z · 15 days · 20.1 g |
| Latest public photometry | Not available in the staged feed |
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

### 203. [AT2026aiiu](https://www.wis-tns.org/object/2026aiiu) near IC1729

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1729 as this object's host. The 1.95901° (117.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:03:28Z · 12 days · 20.2 L |
| Latest public photometry | Not available in the staged feed |
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

### 204. [AT2026aiiw](https://www.wis-tns.org/object/2026aiiw) near IC5325

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5325 as this object's host. The 1.36152° (81.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T10:09:22Z · 9 days · 19.98 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiiw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.764581%20-40.490264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 205. [AT2026aijz](https://www.wis-tns.org/object/2026aijz) near IC522

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC522 as this object's host. The 1.16708° (70.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T11:06:29Z · 8 days · 19.8 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.5650403%2057.4916495&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 206. [AT2026aikd](https://www.wis-tns.org/object/2026aikd) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.84563° (110.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:34:20Z · 11 days · 20.95 i |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aikd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.3976846%20-9.385282&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 207. [AT2026aimy](https://www.wis-tns.org/object/2026aimy) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.81739° (109.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:12:08Z · 11 days · 21.54 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.81739° · 109.04′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=357.1989177%200.0621411&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 208. [AT2026aine](https://www.wis-tns.org/object/2026aine) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.77858° (106.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T12:34:56Z · 14 days · 19.68 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.77858° · 106.71′ |
| Catalog description | NGC 2775, also known as Caldwell 48, is a spiral galaxy in the constellation Cancer. It is 67 million light-years away from the Milky Way. It was discovered by German-British astronomer William Herschel on 19 December 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aine) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=135.80344%207.2484421&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 209. [AT2026aint](https://www.wis-tns.org/object/2026aint) near NGC3631

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3631 as this object's host. The 1.58810° (95.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T11:26:44Z · 15 days · 19.89 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3631** · `NGC3631` |
| Catalog display name | NGC3631 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.4 · 3.72′ × 3.08′ |
| Distance | — |
| Separation | 1.58810° · 95.29′ |
| Catalog description | NGC 3631 is a spiral galaxy located in the constellation Ursa Major. It is located at a distance of about 35 million light years from Earth, which, given its apparent dimensions, means that NGC 3631 is about 60,000 light years across. It was discovered by William Herschel on April 14, 1789. It is a grand design spiral galaxy seen face on. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aint) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.7822873%2051.6082456&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 210. [AT2026ainu](https://www.wis-tns.org/object/2026ainu) near NGC1637

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1637 as this object's host. The 1.60149° (96.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T15:16:16Z · 8 days · 19.94 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
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
| Separation | 1.60149° · 96.09′ |
| Catalog description | NGC 1637 is an isolated, non-interacting intermediate spiral galaxy in the constellation Eridanus, about a degree to the WNW of the star Mu Eridani. It was discovered by German-British astronomer William Herschel on 1 February 1786. It is located at a distance of about 9.77 ± 1.82 Mpc (31.9 ± 5.9 Mly) from the Milky Way. The galaxy is inclined at an angle of 31.1° to the line of sight from the Earth and the long axis is oriented along a position angle of 16.3°. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.786624%20-2.586168&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 211. [AT2026aioc](https://www.wis-tns.org/object/2026aioc) near NGC205

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC205 as this object's host. The 1.85287° (111.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T06:20:12Z · 14 days · 19.92 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC205** · `NGC205` |
| Catalog display name | NGC205 |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 8.2 · 16.22′ × 9.59′ |
| Distance | 674.509 kpc |
| Separation | 1.85287° · 111.17′ |
| Catalog description | Messier 110, or M110, also known as NGC 205, is a dwarf elliptical galaxy that is a satellite of the Andromeda Galaxy in the Local Group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aioc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=7.6701356%2041.3061804&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 212. [AT2026aios](https://www.wis-tns.org/object/2026aios) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.32538° (79.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T15:10:04Z · 12 days · 22.19 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.32538° · 79.52′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aios) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.50025%205.000853&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 213. [AT2026aipc](https://www.wis-tns.org/object/2026aipc) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.38724° (83.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:05:45Z · 9 days · 21.55 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.38724° · 83.23′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.539958%200.142742&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 214. [AT2026aipi](https://www.wis-tns.org/object/2026aipi) near IC 74

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 74 as this object's host. The 1.59561° (95.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:38:24Z · 9 days · 21.97 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.59561° · 95.74′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 74 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.726583%205.667311&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 215. [AT2026aipl](https://www.wis-tns.org/object/2026aipl) near IC 1746

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1746 as this object's host. The 1.98515° (119.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:58:33Z · 9 days · 22.31 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.98515° · 119.11′ |
| Catalog description | NGC 502, also occasionally referred to as PGC 5034 or UGC 922, is a lenticular galaxy in the constellation Pisces. It is located approximately 113 million light-years from the Solar System and was discovered on 25 September 1862 by German astronomer Heinrich Louis d'Arrest. When the Morphological Catalogue of Galaxies was published between 1962 and 1974, the identifications of NGC 502 and NGC 505 were reversed. In reality, NGC 502 is equal to MGC +01-04-041 and not MCG +01-04-043 as noted in the catalogue. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1746 has the different designation NGC 502 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.613%204.930244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 216. [AT2026aipm](https://www.wis-tns.org/object/2026aipm) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.50924° (90.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T13:30:43Z · 8 days · 22.66 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.50924° · 90.55′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.35825%206.157722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 217. [AT2026aipu](https://www.wis-tns.org/object/2026aipu) near NGC 2782

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2782 as this object's host. The 1.33199° (79.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T22:36:28Z · 24 days · 21.76 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.33199° · 79.92′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.868458%2038.80895&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 218. [AT2026aiqc](https://www.wis-tns.org/object/2026aiqc) near NGC2859

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2859 as this object's host. The 1.88260° (112.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T21:51:50Z · 14 days · 20.5 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2859** · `NGC2859` |
| Catalog display name | NGC2859 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10.9 · 3.19′ × 2.78′ |
| Distance | — |
| Separation | 1.88260° · 112.96′ |
| Catalog description | NGC 2859 is a barred lenticular galaxy located some 83 million light years away in the constellation Leo Minor. The morphological classification is (R)SB(r)0+, where the S0+ notation indicates a well-defined physical structure that is lacking in visible spiral arms. It has a strong bar (B) of the "ansae" type, which means it grows brighter or wider toward the tips. A faint, secondary bar is positioned at nearly a right angle to the main bar. These features are surrounded by a weak inner ring (r) that appears diffuse. The outer region of the galaxy hosts a prominent, detached ring (R) that includes a series of blue-hued knots along the eastern side. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.531%2036.343183&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 219. [AT2026aiqd](https://www.wis-tns.org/object/2026aiqd) near NGC 2782

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2782 as this object's host. The 1.42815° (85.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T22:00:28Z · 14 days · 21.04 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.42815° · 85.69′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.25225%2041.527264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 220. [AT2026aiqe](https://www.wis-tns.org/object/2026aiqe) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 1.66342° (99.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T17:41:16Z · 13 days · 20.53 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
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
| Separation | 1.66342° · 99.81′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=12.895083%2041.375958&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 221. [AT2026aiqm](https://www.wis-tns.org/object/2026aiqm) near IC187

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC187 as this object's host. The 1.72540° (103.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T21:17:16Z · 10 days · 21 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC187** · `IC187` |
| Catalog display name | IC187 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 13.8 · 2.23′ × 0.73′ |
| Distance | 76,700 kpc |
| Separation | 1.72540° · 103.52′ |
| Catalog description | most extremely faint, round |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.294958%2026.339119&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 222. [AT2026aiqs](https://www.wis-tns.org/object/2026aiqs) near IC 189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 189 as this object's host. The 1.98630° (119.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:39:21Z · 9 days · 21.44 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 189** · `IC 189` |
| Catalog display name | NGC 2685 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.78′ × 0.67′ |
| Distance | — |
| Separation | 1.98630° · 119.18′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 189 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.133333%2024.834003&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 223. [AT2026aiqv](https://www.wis-tns.org/object/2026aiqv) near NGC672

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC672 as this object's host. The 1.71851° (103.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:50:52Z · 9 days · 21.94 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC672** · `NGC672` |
| Catalog display name | NGC672 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 10.9 · 7.01′ × 2.71′ |
| Distance | — |
| Separation | 1.71851° · 103.11′ |
| Catalog description | NGC 672 is a spiral galaxy in the northern constellation of Triangulum, positioned around 2° to the southwest of the star Alpha Trianguli. The original object designated NGC 672 was discovered by the German-born astronomer William Herschel on 26 October 1786, but this was later cataloged as NGC 614. The object now identified as NGC 672 was discovered by John Herschel on 11 November 1827. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.741958%2028.887517&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 224. [AT2026aira](https://www.wis-tns.org/object/2026aira) near NGC7177

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7177 as this object's host. The 1.64805° (98.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T15:10:04Z · 8 days · 21.61 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7177** · `NGC7177` |
| Catalog display name | NGC7177 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 11.1 · 2.85′ × 1.93′ |
| Distance | 17,200 kpc |
| Separation | 1.64805° · 98.88′ |
| Catalog description | NGC 7177 is a barred spiral galaxy in the constellation of Pegasus. Its velocity with respect to the cosmic microwave background is 801±24 km/s, which corresponds to a Hubble distance of 38.6 ± 2.9 Mly (11.82 ± 0.90 Mpc). However, 12 non-redshift measurements give a much farther distance of 86.49 ± 10.33 Mly (26.517 ± 3.166 Mpc). It was discovered by German-British astronomer William Herschel on 15 October 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aira) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.839875%2018.179903&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 225. [AT2026airm](https://www.wis-tns.org/object/2026airm) near IC1562

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1562 as this object's host. The 1.43858° (86.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T11:07:03Z · 13 days · 19.98 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1562** · `IC1562` |
| Catalog display name | IC1562 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.6 · 1.5′ × 1.41′ |
| Distance | — |
| Separation | 1.43858° · 86.31′ |
| Catalog description | small in angular size, round, pretty suddenly brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=8.835642%20-23.037086&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 226. [AT2026aiti](https://www.wis-tns.org/object/2026aiti) near IC719

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC719 as this object's host. The 1.52988° (91.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:06:13Z · 12 days · 19.56 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC719** · `IC719` |
| Catalog display name | IC719 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 13.8 · 1.22′ × 0.39′ |
| Distance | 26,600 kpc |
| Separation | 1.52988° · 91.79′ |
| Catalog description | IC 719 is a lenticular galaxy located in the constellation of Virgo. The redshift of the galaxy is estimated to be (z) 0.0061 and it was first discovered in March 1892 by the Austrian astronomer named Rudolph Spitaler who described it as a 13th magnitude galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiti) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=174.213558%207.7393715&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 227. [AT2026aiul](https://www.wis-tns.org/object/2026aiul) near Caldwell 44 (C44)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 44 (C44) as this object's host. The 1.56654° (93.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T08:43:14Z · 9 days · 21.17 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Caldwell 44 (C44)** · `C44` |
| Catalog display name | Caldwell 44 (C44) |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 11 · 4′ × 3′ |
| Distance | — |
| Separation | 1.56654° · 93.99′ |
| Catalog description | NGC 7479 is a barred spiral galaxy about 105 million light-years away in the constellation Pegasus. William Herschel discovered it in 1784. NGC 7479 is also recognized as a Seyfert galaxy and a LINER undergoing starburst activity not only on the nucleus and the outer arms, but also across the bar of the galaxy, where most of the stars were formed in the last 100 million years. Polarization studies of this galaxy indicate that it recently underwent a minor merger and that it is unique in the radio continuum, with arms opening in a direction opposite to the optical arms. This feature, along with the asymmetrical arms of the galaxy and the intense star formation activity are attributed to a merger with a smaller galaxy. This galaxy is similar in both size and morphology to the barred spiral NGC 1300. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiul) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.22843%2013.3263041&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 228. [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) near NGC2681

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2681 as this object's host. The 1.89726° (113.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:43:40Z · 9 days · 21.09 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.89726° · 113.84′ |
| Catalog description | NGC 2681 is a lenticular galaxy in the constellation Ursa Major. The galaxy lies 50 million light years away from Earth, which means, given its apparent dimensions, that NGC 2681 is approximately 55,000 light years across. NGC 2681 has an active galactic nucleus and it is a type 3 Seyfert galaxy. Its nucleus is also a low-ionization nuclear emission-line region. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.253583%2049.980844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 229. [AT2026aiwk](https://www.wis-tns.org/object/2026aiwk) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.74454° (104.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T12:34:03Z · 21 days · 19.72 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.74454° · 104.67′ |
| Catalog description | NGC 2775, also known as Caldwell 48, is a spiral galaxy in the constellation Cancer. It is 67 million light-years away from the Milky Way. It was discovered by German-British astronomer William Herschel on 19 December 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.9505931%208.1364268&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 230. [AT2026aixs](https://www.wis-tns.org/object/2026aixs) near NGC3610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3610 as this object's host. The 1.63021° (97.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:36:44Z · 8 days · 19.97 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.63021° · 97.81′ |
| Catalog description | NGC 3610 is an elliptical galaxy in the constellation Ursa Major. It was discovered on 8 April 1793 by German-British astronomer William Herschel. This galaxy is located at a distance of 106 million light-years (32.5 Mpc) from the Milky Way, and is receding with a galacto-centric radial velocity of 1,819 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.608116%2058.3224663&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 231. [AT2026aiyb](https://www.wis-tns.org/object/2026aiyb) near IC392

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC392 as this object's host. The 1.52492° (91.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:18:04Z · 9 days · 20.39 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC392** · `IC392` |
| Catalog display name | IC392 |
| Type / constellation | Galaxy · Orion |
| Catalog magnitude / angular size | 13.5 · 1.45′ × 1′ |
| Distance | — |
| Separation | 1.52492° · 91.50′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, small in angular size, round, nucleus, or to a nucleus = 12.5 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=71.487159%201.985122&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 232. [AT2026aiyd](https://www.wis-tns.org/object/2026aiyd) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.26208° (75.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T20:04:33Z · 11 days · 20 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.26208° · 75.72′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.910009%206.749575&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 233. [AT2026aizu](https://www.wis-tns.org/object/2026aizu) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.65578° (99.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T15:01:26Z · 12 days · 22.25 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.65578° · 99.35′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.241833%202.8844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 234. [AT2026aizw](https://www.wis-tns.org/object/2026aizw) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.76396° (105.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:22:04Z · 11 days · 22.11 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.76396° · 105.84′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.799458%203.518825&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 235. [AT2026aizx](https://www.wis-tns.org/object/2026aizx) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.77435° (106.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:52:48Z · 9 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1696** · `IC1696` |
| Catalog display name | IC1696 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.6 · 0.83′ × 0.75′ |
| Distance | 72,050 kpc |
| Separation | 1.77435° · 106.46′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=22.37675%20-0.497033&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 236. [AT2026ajae](https://www.wis-tns.org/object/2026ajae) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.54038° (92.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T14:41:16Z · 24 days · 22.56 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.54038° · 92.42′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajae) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.91625%204.792956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 237. [AT2026ajaf](https://www.wis-tns.org/object/2026ajaf) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.97393° (118.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:04:48Z · 11 days · 22.36 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97393° · 118.44′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajaf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.27775%204.532092&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 238. [AT2026ajah](https://www.wis-tns.org/object/2026ajah) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.73881° (104.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:56:38Z · 11 days · 21.96 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1696** · `IC1696` |
| Catalog display name | IC1696 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 13.6 · 0.83′ × 0.75′ |
| Distance | 72,050 kpc |
| Separation | 1.73881° · 104.33′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajah) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=22.639792%20-1.037003&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 239. [AT2026ajay](https://www.wis-tns.org/object/2026ajay) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 1.60207° (96.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T19:23:31Z · 22 days · 21.83 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Andromeda Galaxy** · `IC 1732` |
| Catalog display name | Andromeda Galaxy |
| Type / constellation | Galaxy · And |
| Catalog magnitude / angular size | — · 1.32′ × 0.38′ |
| Distance | — |
| Separation | 1.60207° · 96.12′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajay) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.778792%2036.332881&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 240. [AT2026ajbe](https://www.wis-tns.org/object/2026ajbe) near IC 180

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 180 as this object's host. The 1.55678° (93.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T20:45:36Z · 10 days · 21.27 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 180** · `IC 180` |
| Catalog display name | NGC664 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.83′ × 0.34′ |
| Distance | — |
| Separation | 1.55678° · 93.41′ |
| Catalog description | NGC 664 is a spiral galaxy in the constellation of Pisces. Its velocity with respect to the cosmic microwave background is 5137 ± 21 km/s, which corresponds to a Hubble distance of 247.1 ± 17.3 Mly (75.77 ± 5.31 Mpc). In addition, six non redshift measurements give a closer distance of 218.91 ± 3.66 Mly (67.117 ± 1.123 Mpc). It was discovered by British astronomer John Herschel on 24 September 1830. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 180 has the different designation NGC664 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.68875%2022.074497&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 241. [SN2026aaee](https://www.wis-tns.org/object/2026aaee) near IC 2360

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2360 as this object's host. The 1.01344° (60.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.014804 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-08-30T12:21:48Z · 72 days · 17.12 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3532....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR3532....1S/abstract) |
| Classification references | [2026TNSCR3840....1B](https://ui.adsabs.harvard.edu/abs/2026TNSCR3840....1B/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 2360** · `IC 2360` |
| Catalog display name | NGC 2360 |
| Type / constellation | Star · Cnc |
| Catalog magnitude / angular size | — · 13′ × 13′ |
| Distance | — |
| Separation | 1.01344° · 60.81′ |
| Catalog description | NGC 2360 is an open cluster in the constellation Canis Major. It was discovered on 26 February 1783 by Caroline Herschel, who described it as a "beautiful cluster of pretty compressed stars near 1/2 degree in diameter". Her notes were overlooked until her brother William included the cluster in his 1786 catalogue of 1000 clusters and nebulae and acknowledged her as the discoverer. The cluster lies 3.5 degrees east of Gamma Canis Majoris and less than one degree northwest of the eclipsing binary star R Canis Majoris; it has a combined apparent magnitude of 7.2. It is 13 arc minutes in diameter. By the western edge of the cluster is the unrelated star, 5.5-magnitude HD 56405. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2360 has the different designation NGC 2360 as its display name.

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude ≤18.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aaee) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.0300443%2020.2729487&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 242. [AT2026aiay](https://www.wis-tns.org/object/2026aiay) near Messier 40 (M40)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 40 (M40) as this object's host. The 1.14193° (68.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:47:29Z · 7 days · 20 g |
| Latest public photometry | Not available in the staged feed |
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

### 243. [AT2026aies](https://www.wis-tns.org/object/2026aies) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.74650° (104.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T06:01:28Z · 5 days · 21.09 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4446....1F](https://ui.adsabs.harvard.edu/abs/2026TNSTR4446....1F/abstract) |
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
| Separation | 1.74650° · 104.79′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aies) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.7613763%20-27.5471983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 244. [AT2026aiid](https://www.wis-tns.org/object/2026aiid) near IC1415

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1415 as this object's host. The 1.79155° (107.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:32:38Z · 7 days · 19.8 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4480....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4480....1S/abstract) |
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
| Separation | 1.79155° · 107.49′ |
| Catalog description | extremely, excessively faint, a single star 9.5 south following 8' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiid) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.9471753%200.0888023&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 245. [AT2026aiif](https://www.wis-tns.org/object/2026aiif) near IC2013

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2013 as this object's host. The 1.67634° (100.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:10:44Z · 7 days · 20.25 g |
| Latest public photometry | Not available in the staged feed |
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

### 246. [AT2026aiih](https://www.wis-tns.org/object/2026aiih) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 1.30155° (78.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 4 days · 23.45 r |
| Latest public photometry | Not available in the staged feed |
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

### 247. [AT2026aiik](https://www.wis-tns.org/object/2026aiik) near IC1992

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1992 as this object's host. The 1.50046° (90.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:22:32Z · 4 days · 23.13 r |
| Latest public photometry | Not available in the staged feed |
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

### 248. [AT2026aijr](https://www.wis-tns.org/object/2026aijr) near NGC7447

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7447 as this object's host. The 1.89133° (113.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:48:34Z · 6 days · 20.08 L |
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
| Separation | 1.89133° · 113.48′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.7027508%20-12.3273564&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 249. [AT2026aila](https://www.wis-tns.org/object/2026aila) near NGC2586

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2586 as this object's host. The 1.95903° (117.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T17:46:45Z · 5 days · 19.91 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4471....1G](https://ui.adsabs.harvard.edu/abs/2026TNSTR4471....1G/abstract) |
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
| Separation | 1.95903° · 117.54′ |
| Catalog description | A galaxy is a system of stars, stellar remnants, interstellar gas, dust, and dark matter bound together by gravity. The word is derived from the Greek galaxias (γαλαξίας), literally'milky', a reference to the Milky Way galaxy that contains the Solar System. Galaxies, averaging an estimated 100 million stars, range in size from dwarfs with less than a thousand stars, to the largest galaxies known – supergiants with one hundred trillion stars, each orbiting its galaxy's centre of mass. Most of the mass in a typical galaxy is in the form of dark matter, with only a few percent of that mass visible in the form of stars and nebulae. Supermassive black holes are a common feature at the centres of galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aila) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.800004%20-4.535484&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 250. [AT2026ailb](https://www.wis-tns.org/object/2026ailb) near IC518

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC518 as this object's host. The 1.97027° (118.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T17:46:45Z · 5 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
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

### 251. [AT2026ailw](https://www.wis-tns.org/object/2026ailw) near IC286

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC286 as this object's host. The 1.73940° (104.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:04:11Z · 7 days · 20.38 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC286** · `IC286` |
| Catalog display name | IC286 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.73940° · 104.36′ |
| Catalog description | very faint |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ailw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=44.4839222%20-6.8511357&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 252. [AT2026aimq](https://www.wis-tns.org/object/2026aimq) near NGC4317

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4317 as this object's host. The 1.22316° (73.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:46:04Z · 7 days · 20.11 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC4317** · `NGC4317` |
| Catalog display name | NGC4317 |
| Type / constellation | Nebula · Coma Berenices |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.22316° · 73.39′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=184.4967696%2031.7390522&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 253. [AT2026aiof](https://www.wis-tns.org/object/2026aiof) near Collinder 120 (CR120)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 120 (CR120) as this object's host. The 1.65707° (99.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:22:07Z · 7 days · 20.59 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.65707° · 99.42′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiof) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=105.0652583%2016.8618278&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 254. [AT2026aipr](https://www.wis-tns.org/object/2026aipr) near IC5385

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5385 as this object's host. The 1.58832° (95.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T17:26:52Z · 6 days · 22.3 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.58832° · 95.30′ |
| Catalog description | extremely, excessively faint (not verified) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.795958%201.499003&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 255. [AT2026airk](https://www.wis-tns.org/object/2026airk) near IC 71

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 71 as this object's host. The 1.00378° (60.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T10:51:34Z · 3 days · 20.12 L |
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
| Subject | **IC 71** · `IC 71` |
| Catalog display name | IC 2944 |
| Type / constellation | Star · Cet |
| Catalog magnitude / angular size | — · 75′ × 75′ |
| Distance | — |
| Separation | 1.00378° · 60.23′ |
| Catalog description | IC 2944, also known as the Running Chicken Nebula, the Lambda Centauri Nebula or the λ Centauri Nebula, is an open cluster with an associated emission nebula found in the constellation Centaurus, near the star λ Centauri. It features Bok globules, which are frequently a site of active star formation. However, no evidence for star formation has been found in any of the globules in IC 2944. Other designations for IC 2944 include RCW 62, G40 and G42. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 71 has the different designation IC 2944 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.266447%20-7.1465927&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 256. [AT2026aisi](https://www.wis-tns.org/object/2026aisi) near Collinder 133 (CR133)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 133 (CR133) as this object's host. The 1.35377° (81.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T10:33:14Z · 3 days · 20.26 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.35377° · 81.23′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=108.457168%2012.487059&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 257. [AT2026aitf](https://www.wis-tns.org/object/2026aitf) near NGC3578

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3578 as this object's host. The 1.94090° (116.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T13:00:03Z · 4 days · 19.56 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3578** · `NGC3578` |
| Catalog display name | NGC3578 |
| Type / constellation | Nebula · Crater |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.94090° · 116.45′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.2753616%20-14.9480713&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 258. [AT2026aitp](https://www.wis-tns.org/object/2026aitp) near NGC3181

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3181 as this object's host. The 1.80905° (108.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:24:52Z · 6 days · 19.76 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3181** · `NGC3181` |
| Catalog display name | NGC3181 |
| Type / constellation | HII · Ursa Major |
| Catalog magnitude / angular size | 15.8 · 2.84′ × 0.83′ |
| Distance | — |
| Separation | 1.80905° · 108.54′ |
| Catalog description | NGC 3184, also known as The Little Pinwheel Galaxy, is an unbarred spiral galaxy approximately 40 million light-years away in the constellation Ursa Major. Its name comes from its resemblance to the Pinwheel Galaxy. It was discovered by German-British astronomer William Herschel on 18 March 1787. It has two HII regions named NGC 3180 and NGC 3181. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.6085564%2039.7934982&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 259. [AT2026aiui](https://www.wis-tns.org/object/2026aiui) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.22722° (73.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T13:04:07Z · 4 days · 21.25 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.22722° · 73.63′ |
| Catalog description | NGC 2419 is a globular cluster in the constellation Lynx. It was discovered by William Herschel on December 31, 1788. NGC 2419 is at a distance of about 300,000 light years from the Solar System and at the same distance from the Galactic Center. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiui) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.0930428%2039.3950908&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 260. [AT2026aiwa](https://www.wis-tns.org/object/2026aiwa) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 1.45584° (87.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T15:44:38Z · 3 days · 22.37 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.45584° · 87.35′ |
| Catalog description | IC 1623 is a galaxy merger in the constellation Cetus. The galaxy lies about 250 million light years away from Earth, which means, given its apparent dimensions, that IC 1623 is approximately 115,000 light years across. It was discovered by Lewis Swift on November 19, 1897. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.994292%20-1.052686&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 261. [AT2026aiwg](https://www.wis-tns.org/object/2026aiwg) near IC323

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC323 as this object's host. The 1.25852° (75.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:53:59Z · 5 days · 20.6 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC323** · `IC323` |
| Catalog display name | IC323 |
| Type / constellation | Nebula · Perseus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.25852° · 75.51′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, preceding (westward) / pretty (adv., before F. B. L, S) of 2 |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.0483718%2042.0988238&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 262. [AT2026aiwm](https://www.wis-tns.org/object/2026aiwm) near IC2940

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2940 as this object's host. The 1.28946° (77.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T12:59:13Z · 4 days · 20.09 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2940** · `IC2940` |
| Catalog display name | IC2940 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.28946° · 77.37′ |
| Catalog description | extremely, excessively faint, suspected (not suddenly (abruptly) / south most extremely north at Birr) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=173.7547524%2023.2296939&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 263. [AT2026aiwn](https://www.wis-tns.org/object/2026aiwn) near NGC56

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC56 as this object's host. The 1.79121° (107.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T03:57:19Z · 2 days · 20.08 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79121° · 107.47′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=3.0868602%2010.8093252&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 264. [AT2026aixc](https://www.wis-tns.org/object/2026aixc) near IC5383

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5383 as this object's host. The 1.16692° (70.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:18:42Z · 1 days · 20.38 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5383** · `IC5383` |
| Catalog display name | IC5383 |
| Type / constellation | Nebula · Pegasus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.16692° · 70.02′ |
| Catalog description | faint, small in angular size, round, brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.116803%2014.858375&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 265. [AT2026aixt](https://www.wis-tns.org/object/2026aixt) near IC640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC640 as this object's host. The 1.79762° (107.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:27:34Z · 6 days · 19.6 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79762° · 107.86′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, extended, double ? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.5238562%2034.6786725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 266. [AT2026aixy](https://www.wis-tns.org/object/2026aixy) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 1.08009° (64.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:19:01Z · 2 days · 20.58 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.08009° · 64.81′ |
| Catalog description | extremely, excessively faint, a single star 8.8 north following 4' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.7923609%20-3.7781902&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 267. [AT2026aiyq](https://www.wis-tns.org/object/2026aiyq) near Melotte 53 (MEL53)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Melotte 53 (MEL53) as this object's host. The 1.83617° (110.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T15:30:53Z · 4 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.83617° · 110.17′ |
| Catalog description | NGC 2298 is a globular cluster in the southern constellation of Puppis. Discovered by James Dunlop on May 30, 1826, it is probably a former member of the disputed Canis Major Dwarf galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.50063%20-34.481664&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 268. [AT2026aiys](https://www.wis-tns.org/object/2026aiys) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.74747° (104.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:48:30Z · 1 days · 19.55 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.74747° · 104.85′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiys) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=339.579172%2011.643886&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 269. [AT2026aiyz](https://www.wis-tns.org/object/2026aiyz) near IC229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC229 as this object's host. The 1.20798° (72.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T09:13:20Z · 2 days · 20.43 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC229** · `IC229` |
| Catalog display name | IC229 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.20798° · 72.48′ |
| Catalog description | nebula, 10m |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.0369861%20-22.8573169&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 270. [AT2026ajcx](https://www.wis-tns.org/object/2026ajcx) near IC337

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC337 as this object's host. The 1.86545° (111.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:11:24Z · 7 days · 20.12 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC337** · `IC337` |
| Catalog display name | IC337 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · 1.6′ × 1.6′ |
| Distance | — |
| Separation | 1.86545° · 111.93′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) large, 3 stars (pl.) near |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.7424687%20-8.5260573&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 271. [AT2026ajde](https://www.wis-tns.org/object/2026ajde) near NGC2875

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2875 as this object's host. The 1.32058° (79.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T11:29:06Z · 5 days · 19.71 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.32058° · 79.23′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajde) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.1027718%2011.449902&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 272. [SN2026afke](https://www.wis-tns.org/object/2026afke) near Lynds Bright Nebula 157 (LBN157)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 157 (LBN157) as this object's host. The 1.95410° (117.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.044 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T04:04:08Z · 27 days · 19.75 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4138....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4138....1S/abstract) |
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
| Separation | 1.95410° · 117.25′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026afke) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=326.2600816%2014.7732179&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 273. [AT2026afxf](https://www.wis-tns.org/object/2026afxf) near IC5340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5340 as this object's host. The 0.52787° (31.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T03:58:07Z · 21 days · 19.58 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4227....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4227....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5340** · `IC5340` |
| Catalog display name | IC5340 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.52787° · 31.67′ |
| Catalog description | extremely, excessively faint, a star of 13th magnitude north 1'.5 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afxf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.1060958%20-4.9064084&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 274. [AT2026ahkb](https://www.wis-tns.org/object/2026ahkb) near NGC7666

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7666 as this object's host. The 0.90553° (54.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:15:54Z · 11 days · 20.8 r |
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
| Subject | **NGC7666** · `NGC7666` |
| Catalog display name | NGC7666 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.90553° · 54.33′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahkb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.8126967%20-5.0910715&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 275. [AT2026aias](https://www.wis-tns.org/object/2026aias) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 0.69484° (41.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:13:26Z · 11 days · 20.04 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4430....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4430....1R/abstract) |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aias) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.9722541%20-4.0627528&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 276. [AT2026aiat](https://www.wis-tns.org/object/2026aiat) near Collinder 163 (CR163)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 163 (CR163) as this object's host. The 0.39314° (23.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:14Z · 9 days · 19.61 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiat) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=116.824398%20-21.640891&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 277. [AT2026aibk](https://www.wis-tns.org/object/2026aibk) near NGC843

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC843 as this object's host. The 0.80016° (48.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:32:09Z · 12 days · 21.26 r |
| Latest public photometry | Not available in the staged feed |
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

### 278. [AT2026aihc](https://www.wis-tns.org/object/2026aihc) near NGC7666

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7666 as this object's host. The 0.34612° (20.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T10:42:55Z · 12 days · 20.27 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4452....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4452....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7666** · `NGC7666` |
| Catalog display name | NGC7666 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.34612° · 20.77′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aihc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.6092934%20-3.9370077&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 279. [AT2026aiic](https://www.wis-tns.org/object/2026aiic) near Lynds Bright Nebula 220 (LBN220)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 220 (LBN220) as this object's host. The 0.80240° (48.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T04:23:06Z · 7 days · 20.55 g |
| Latest public photometry | Not available in the staged feed |
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

### 280. [AT2026aiio](https://www.wis-tns.org/object/2026aiio) near NGC930

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC930 as this object's host. The 0.95799° (57.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T06:44:12Z · 21 days · 20.63 r |
| Latest public photometry | Not available in the staged feed |
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

### 281. [AT2026aiop](https://www.wis-tns.org/object/2026aiop) near Lynds Bright Nebula 773 (LBN773)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 773 (LBN773) as this object's host. The 0.84759° (50.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:58:48Z · 5 days · 20.23 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 773 (LBN773)** · `LBN773` |
| Catalog display name | Lynds Bright Nebula 773 (LBN773) |
| Type / constellation | HII · Taurus |
| Catalog magnitude / angular size | — · 150′ × 120′ |
| Distance | — |
| Separation | 0.84759° · 50.86′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiop) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.4124213%2022.749387&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 282. [AT2026aipj](https://www.wis-tns.org/object/2026aipj) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 0.77284° (46.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:42:43Z · 9 days · 21.98 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1651** · `IC1651` |
| Catalog display name | IC1651 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.77284° · 46.37′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.836875%202.679611&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 283. [AT2026aipy](https://www.wis-tns.org/object/2026aipy) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 0.68824° (41.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-21T21:21:36Z · 20 days · 21.81 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.68824° · 41.29′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.94275%2057.307686&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 284. [AT2026aiqq](https://www.wis-tns.org/object/2026aiqq) near IC1707

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1707 as this object's host. The 0.77210° (46.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:29:16Z · 9 days · 21.76 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1707** · `IC1707` |
| Catalog display name | IC1707 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.77210° · 46.33′ |
| Catalog description | extremely, excessively faint, diffused, a single star 13.3 close |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.048125%2037.2624&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 285. [AT2026aiqr](https://www.wis-tns.org/object/2026aiqr) near NGC737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC737 as this object's host. The 0.33866° (20.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:35:02Z · 9 days · 21.78 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.33866° · 20.32′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.377875%2032.760394&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 286. [AT2026aiuf](https://www.wis-tns.org/object/2026aiuf) near Lynds Bright Nebula 556 (LBN556)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 556 (LBN556) as this object's host. The 0.70503° (42.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:05:30Z · 7 days · 20.72 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
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
| Separation | 0.70503° · 42.30′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiuf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.9349304%2019.6474786&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 287. [AT2026aixn](https://www.wis-tns.org/object/2026aixn) near NGC2531

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2531 as this object's host. The 0.88316° (52.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T12:09:20Z · 23 days · 20.95 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2531** · `NGC2531` |
| Catalog display name | NGC2531 |
| Type / constellation | Nebula · Cancer |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.88316° · 52.99′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=122.4678581%2018.5860889&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 288. [AT2026aixq](https://www.wis-tns.org/object/2026aixq) near Hind's variable nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Hind's variable nebula as this object's host. The 0.75249° (45.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T09:11:25Z · 22 days · 20.62 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Hind's variable nebula** · `NGC1555` |
| Catalog display name | Hind's variable nebula |
| Type / constellation | reflection nebula · Taurus |
| Catalog magnitude / angular size | 10 · 1.82′ × 1.35′ |
| Distance | — |
| Separation | 0.75249° · 45.15′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.4668312%2019.6815135&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 289. [AT2026ajbi](https://www.wis-tns.org/object/2026ajbi) near Barnard 215 (B215)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Barnard 215 (B215) as this object's host. The 0.54619° (32.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T07:26:44Z · 1 days · 20.84 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Barnard 215 (B215)** · `B215` |
| Catalog display name | Barnard 215 (B215) |
| Type / constellation | Dark nebula · Taurus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.54619° · 32.77′ |
| Catalog description | Darker spot in dark lane |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajbi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.3239822%2025.4146032&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 290. [AT2026agnk](https://www.wis-tns.org/object/2026agnk) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.83335° (110.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T22:19:12Z · 23 days · 20.06 r |
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
| Subject | **Intergalactic Wanderer** · `C25` |
| Catalog display name | Intergalactic Wanderer |
| Type / constellation | Globular cluster · Lynx |
| Catalog magnitude / angular size | 10.4 · 4.1′ × 4.1′ |
| Distance | 84.2 kpc |
| Separation | 1.83335° · 110.00′ |
| Catalog description | NGC 2419 is a globular cluster in the constellation Lynx. It was discovered by William Herschel on December 31, 1788. NGC 2419 is at a distance of about 300,000 light years from the Solar System and at the same distance from the Galactic Center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agnk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=116.5210613%2039.8753573&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 291. [AT2026agwt](https://www.wis-tns.org/object/2026agwt) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.72330° (103.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T21:46:04Z · 29 days · 20.95 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4301....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4301....1X/abstract) |
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
| Separation | 1.72330° · 103.40′ |
| Catalog description | NGC 2419 is a globular cluster in the constellation Lynx. It was discovered by William Herschel on December 31, 1788. NGC 2419 is at a distance of about 300,000 light years from the Solar System and at the same distance from the Galactic Center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.7860959%2040.5056762&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 292. [AT2026ahux](https://www.wis-tns.org/object/2026ahux) near NGC611

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC611 as this object's host. The 1.75898° (105.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:02:54Z · 12 days · 20.27 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4398....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4398....1O/abstract) |
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
| Separation | 1.75898° · 105.54′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahux) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=23.338665%20-18.3827864&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 293. [AT2026aidb](https://www.wis-tns.org/object/2026aidb) near Sharpless 246 (SH2-246)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 246 (SH2-246) as this object's host. The 1.22301° (73.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T12:14:40Z · 6 days · 20.12 r |
| Latest public photometry | Not available in the staged feed |
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

### 294. [AT2026aiip](https://www.wis-tns.org/object/2026aiip) near NGC1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1639 as this object's host. The 1.39017° (83.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T09:31:11Z · 21 days · 20.62 g |
| Latest public photometry | Not available in the staged feed |
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

### 295. [AT2026aikj](https://www.wis-tns.org/object/2026aikj) near Lynds Bright Nebula 1010 (LBN1010)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1010 (LBN1010) as this object's host. The 1.53192° (91.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:17:28Z · 5 days · 20.02 L |
| Latest public photometry | Not available in the staged feed |
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

### 296. [AT2026ailo](https://www.wis-tns.org/object/2026ailo) near Lynds Bright Nebula 141 (LBN141)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 141 (LBN141) as this object's host. The 1.55411° (93.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T02:17:27Z · 7 days · 19.91 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.55411° · 93.25′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ailo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=308.2389762%2019.3133284&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 297. [AT2026ails](https://www.wis-tns.org/object/2026ails) near Lynds Bright Nebula 481 (LBN481)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 481 (LBN481) as this object's host. The 1.74690° (104.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T03:44:46Z · 7 days · 20.29 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 481 (LBN481)** · `LBN481` |
| Catalog display name | Lynds Bright Nebula 481 (LBN481) |
| Type / constellation | HII · Draco |
| Catalog magnitude / angular size | — · 80′ × 8′ |
| Distance | — |
| Separation | 1.74690° · 104.81′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ails) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=296.2591872%2072.8473083&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 298. [AT2026aimc](https://www.wis-tns.org/object/2026aimc) near Sharpless 250 (SH2-250)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 250 (SH2-250) as this object's host. The 1.29797° (77.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:05:16Z · 7 days · 20.71 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Sharpless 250 (SH2-250)** · `SH2-250` |
| Catalog display name | Sharpless 250 (SH2-250) |
| Type / constellation | HII · Taurus |
| Catalog magnitude / angular size | — · 10′ × 10′ |
| Distance | — |
| Separation | 1.29797° · 77.88′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aimc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=70.5224583%206.1602357&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 299. [AT2026aimd](https://www.wis-tns.org/object/2026aimd) near Collinder 65 (CR65)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 65 (CR65) as this object's host. The 1.83173° (109.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:37:25Z · 4 days · 20.38 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 65 (CR65)** · `CR65` |
| Catalog display name | Collinder 65 (CR65) |
| Type / constellation | Open cluster · Orion |
| Catalog magnitude / angular size | 3 · — |
| Distance | — |
| Separation | 1.83173° · 109.90′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aimd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=81.7364047%2017.454751&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 300. [AT2026aimw](https://www.wis-tns.org/object/2026aimw) near IC5340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5340 as this object's host. The 1.86813° (112.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:15:17Z · 11 days · 21.43 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5340** · `IC5340` |
| Catalog display name | IC5340 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.86813° · 112.09′ |
| Catalog description | extremely, excessively faint, a star of 13th magnitude north 1'.5 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=353.2379353%20-6.1038577&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 301. [AT2026aimx](https://www.wis-tns.org/object/2026aimx) near NGC7666

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7666 as this object's host. The 1.26208° (75.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:15:17Z · 11 days · 21.18 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7666** · `NGC7666` |
| Catalog display name | NGC7666 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.26208° · 75.72′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aimx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.5047827%20-5.2666019&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 302. [AT2026aiou](https://www.wis-tns.org/object/2026aiou) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.99649° (119.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T17:26:52Z · 12 days · 22 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1651** · `IC1651` |
| Catalog display name | IC1651 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.99649° · 119.79′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiou) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.050417%203.138211&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 303. [AT2026aiow](https://www.wis-tns.org/object/2026aiow) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 1.02900° (61.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:17:16Z · 9 days · 21.68 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7668** · `NGC7668` |
| Catalog display name | NGC7668 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.02900° · 61.74′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiow) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.8085%20-0.193222&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 304. [AT2026aipf](https://www.wis-tns.org/object/2026aipf) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.78743° (107.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:49:26Z · 11 days · 21.81 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1651** · `IC1651` |
| Catalog display name | IC1651 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.78743° · 107.25′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.998583%202.792356&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 305. [AT2026aipz](https://www.wis-tns.org/object/2026aipz) near IC 2275

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2275 as this object's host. The 1.79427° (107.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T20:49:55Z · 16 days · 20.69 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79427° · 107.66′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2275 has the different designation NGC 1360 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=125.441458%2016.827419&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 306. [AT2026aiqf](https://www.wis-tns.org/object/2026aiqf) near IC1707

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1707 as this object's host. The 1.23023° (73.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T19:37:55Z · 13 days · 21.23 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1707** · `IC1707` |
| Catalog display name | IC1707 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.23023° · 73.81′ |
| Catalog description | extremely, excessively faint, diffused, a single star 13.3 close |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.540917%2038.292447&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 307. [AT2026aiqp](https://www.wis-tns.org/object/2026aiqp) near IC1737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1737 as this object's host. The 1.48777° (89.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:27:50Z · 9 days · 22.1 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1737** · `IC1737` |
| Catalog display name | IC1737 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.48777° · 89.27′ |
| Catalog description | extremely, excessively faint, 3 or 4 very faint stars (pl.) irregular north nebula |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiqp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.828208%2037.452569&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 308. [AT2026airg](https://www.wis-tns.org/object/2026airg) near Sharpless 260 (SH2-260)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 260 (SH2-260) as this object's host. The 1.20103° (72.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T09:34:22Z · 3 days · 19.93 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Sharpless 260 (SH2-260)** · `SH2-260` |
| Catalog display name | Sharpless 260 (SH2-260) |
| Type / constellation | HII · Orion |
| Catalog magnitude / angular size | — · 22′ × 22′ |
| Distance | — |
| Separation | 1.20103° · 72.06′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026airg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=72.9951006%206.5875963&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 309. [AT2026aivl](https://www.wis-tns.org/object/2026aivl) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.27407° (76.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:42:43Z · 9 days · 22.36 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1651** · `IC1651` |
| Catalog display name | IC1651 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.27407° · 76.44′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=17.492292%203.000553&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 310. [AT2026aivm](https://www.wis-tns.org/object/2026aivm) near NGC728

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC728 as this object's host. The 1.63081° (97.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:06:43Z · 11 days · 21.89 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC728** · `NGC728` |
| Catalog display name | NGC728 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.63081° · 97.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.407375%203.298717&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 311. [AT2026aivx](https://www.wis-tns.org/object/2026aivx) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.67357° (100.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T14:28:19Z · 3 days · 22.48 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.67357° · 100.41′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aivx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.745625%20-1.017767&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 312. [AT2026aiwh](https://www.wis-tns.org/object/2026aiwh) near Lynds Bright Nebula 434 (LBN434)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 434 (LBN434) as this object's host. The 1.66663° (100.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:04:55Z · 1 days · 19.85 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 434 (LBN434)** · `LBN434` |
| Catalog display name | Lynds Bright Nebula 434 (LBN434) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 80′ × 30′ |
| Distance | — |
| Separation | 1.66663° · 100.00′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiwh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=353.838738%208.971353&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 313. [AT2026aiwq](https://www.wis-tns.org/object/2026aiwq) near van den Bergh 61 (VDB61)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 61 (VDB61) as this object's host. The 1.44782° (86.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T11:38:15Z · 5 days · 20.72 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **van den Bergh 61 (VDB61)** · `VDB61` |
| Catalog display name | van den Bergh 61 (VDB61) |
| Type / constellation | Nebula · Orion |
| Catalog magnitude / angular size | 8.6 · — |
| Distance | — |
| Separation | 1.44782° · 86.87′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiwq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.9949799%206.2063749&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 314. [AT2026aixk](https://www.wis-tns.org/object/2026aixk) near NGC1037

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1037 as this object's host. The 1.03553° (62.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T09:28:57Z · 21 days · 20.78 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1037** · `NGC1037` |
| Catalog display name | NGC1037 |
| Type / constellation | Nebula · Cetus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.03553° · 62.13′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=40.6960589%20-1.3115142&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 315. [AT2026aixl](https://www.wis-tns.org/object/2026aixl) near Lynds Bright Nebula 763 (LBN763)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 763 (LBN763) as this object's host. The 1.50403° (90.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T06:55:12Z · 7 days · 20.49 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 763 (LBN763)** · `LBN763` |
| Catalog display name | Lynds Bright Nebula 763 (LBN763) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 25′ × 12′ |
| Distance | — |
| Separation | 1.50403° · 90.24′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aixl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.5135966%2020.3415483&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 316. [AT2026aixm](https://www.wis-tns.org/object/2026aixm) near Lynds Bright Nebula 828 (LBN828)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 828 (LBN828) as this object's host. The 1.46269° (87.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:18:54Z · 7 days · 20.73 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 828 (LBN828)** · `LBN828` |
| Catalog display name | Lynds Bright Nebula 828 (LBN828) |
| Type / constellation | HII · Taurus |
| Catalog magnitude / angular size | — · 5′ × 5′ |
| Distance | — |
| Separation | 1.46269° · 87.76′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aixm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.1182102%209.2539029&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 317. [AT2026aixp](https://www.wis-tns.org/object/2026aixp) near Collinder 204 (CR204)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 204 (CR204) as this object's host. The 1.53361° (92.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T10:49:06Z · 27 days · 20.76 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 204 (CR204)** · `CR204` |
| Catalog display name | Collinder 204 (CR204) |
| Type / constellation | Open cluster · Cancer |
| Catalog magnitude / angular size | 6.9 · 33′ × 33′ |
| Distance | 0.908 kpc |
| Separation | 1.53361° · 92.02′ |
| Catalog description | Messier 67 and sometimes called the King Cobra Cluster or the Golden Eye Cluster is an open cluster in the southern, equatorial half of Cancer. It was discovered by Johann Gottfried Koehler in 1779. Estimates of its age range between 3.2 and 5 billion years. Distance estimates are likewise varied, but typically are 800–900 parsecs (2,600–2,900 ly). Estimates of 855, 840, and 815 pc were established via binary star modelling and infrared color-magnitude diagram fitting. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.8808033%2010.4550659&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 318. [AT2026aiym](https://www.wis-tns.org/object/2026aiym) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.48879° (89.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T07:11:26Z · 11 days · 20.49 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.48879° · 89.33′ |
| Catalog description | NGC 1360, also known as the Robin's Egg Nebula, is a planetary nebula in the constellation of Fornax. It was identified as a planetary nebula due to its strong radiation in the OIII (oxygen) bands. Reddish matter, believed to have been ejected from the original star before its final collapse, is visible in images. It is slightly fainter than IC 2003. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiym) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.8636527%20-26.6209312&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 319. [AT2026aiyn](https://www.wis-tns.org/object/2026aiyn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.63394° (98.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:13:22Z · 11 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.63394° · 98.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.0256232%20-4.6056668&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 320. [AT2026aize](https://www.wis-tns.org/object/2026aize) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.94668° (116.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:22:29Z · 11 days · 20.61 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.94668° · 116.80′ |
| Catalog description | suspected (13.5 mag) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aize) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=341.3494959%20-2.2783453&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 321. [AT2026aizy](https://www.wis-tns.org/object/2026aizy) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.97258° (118.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T13:42:14Z · 5 days · 22.68 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97258° · 118.35′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aizy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.402542%200.621142&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 322. [AT2026ajau](https://www.wis-tns.org/object/2026ajau) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.33313° (79.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T21:18:43Z · 29 days · 21.1 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 116 (CR116)** · `CR116` |
| Catalog display name | Collinder 116 (CR116) |
| Type / constellation | Open cluster · Auriga |
| Catalog magnitude / angular size | 5.4 · 10.8′ × 10.8′ |
| Distance | 0.558 kpc |
| Separation | 1.33313° · 79.99′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajau) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.351458%2040.166439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 323. [AT2026ajaw](https://www.wis-tns.org/object/2026ajaw) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.31677° (79.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T22:16:19Z · 29 days · 20.69 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.31677° · 79.01′ |
| Catalog description | (See Praesepe) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajaw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=128.772208%2019.040575&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 324. [AT2026ajbc](https://www.wis-tns.org/object/2026ajbc) near IC1707

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1707 as this object's host. The 1.73198° (103.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T20:55:40Z · 12 days · 21.19 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1707** · `IC1707` |
| Catalog display name | IC1707 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.73198° · 103.92′ |
| Catalog description | extremely, excessively faint, diffused, a single star 13.3 close |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.172208%2037.139411&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 325. [AT2026aiqu](https://www.wis-tns.org/object/2026aiqu) near Collinder 21 (CR21)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 21 (CR21) as this object's host. The 0.34357° (20.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T19:46:33Z · 9 days · 21.88 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 21 (CR21)** · `CR21` |
| Catalog display name | Collinder 21 (CR21) |
| Type / constellation | Open cluster · Triangulum |
| Catalog magnitude / angular size | 7.3 · — |
| Distance | — |
| Separation | 0.34357° · 20.61′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiqu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.392458%2026.760397&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 326. [AT2026ahbl](https://www.wis-tns.org/object/2026ahbl) near Lynds Bright Nebula 157 (LBN157)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 157 (LBN157) as this object's host. The 1.08937° (65.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T20:02:06Z · 13 days · 19.99 L |
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

### 327. [AT2026aipg](https://www.wis-tns.org/object/2026aipg) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.21442° (72.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:17:45Z · 9 days · 22.37 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.21442° · 72.87′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aipg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.396458%200.607014&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 328. [AT2026aiiq](https://www.wis-tns.org/object/2026aiiq) near IC 1962

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
| Discovery | 2026-10-06T08:56:10Z · 35 days · 19.77 i |
| Latest public photometry | Not available in the staged feed |
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

### 329. [AT2026aioy](https://www.wis-tns.org/object/2026aioy) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 0.87334° (52.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-30T15:37:26Z · 41 days · 21.42 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.87334° · 52.40′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aioy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=3.72375%200.938131&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 330. [AT2026aavs](https://www.wis-tns.org/object/2026aavs) near Lynds Bright Nebula 811 (LBN811)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 10/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 811 (LBN811) as this object's host. The 1.33240° (79.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-04T12:14:15Z · 67 days · 19.29 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3610....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR3610....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 811 (LBN811)** · `LBN811` |
| Catalog display name | Lynds Bright Nebula 811 (LBN811) |
| Type / constellation | HII · Lynx |
| Catalog magnitude / angular size | — · 60′ × 10′ |
| Distance | — |
| Separation | 1.33240° · 79.94′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aavs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=118.3950777%2044.4375714&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 331. [AT2026adsw](https://www.wis-tns.org/object/2026adsw) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.35743° (81.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T07:03:46Z · 40 days · 21.73 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3941....1C](https://ui.adsabs.harvard.edu/abs/2026TNSTR3941....1C/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1386** · `IC1386` |
| Catalog display name | IC1386 |
| Type / constellation | Galaxy · Capricornus |
| Catalog magnitude / angular size | 13.1 · 0.97′ × 0.77′ |
| Distance | 120,000 kpc |
| Separation | 1.35743° · 81.45′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adsw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=321.0803102%20-21.7658412&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 332. [AT2026aibe](https://www.wis-tns.org/object/2026aibe) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.67355° (100.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T21:50:24Z · 37 days · 21.74 r |
| Latest public photometry | Not available in the staged feed |
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

### 333. [AT2026aiov](https://www.wis-tns.org/object/2026aiov) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.17482° (70.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T15:21:36Z · 32 days · 22.32 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.17482° · 70.49′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiov) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.188125%205.672261&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 334. [AT2026aiox](https://www.wis-tns.org/object/2026aiox) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.75237° (105.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T15:28:48Z · 32 days · 21.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.75237° · 105.14′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiox) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.582125%201.218092&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 335. [AT2026aipt](https://www.wis-tns.org/object/2026aipt) near IC 1775

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1775 as this object's host. The 1.50389° (90.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-02T20:54:14Z · 39 days · 20.84 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1775** · `IC 1775` |
| Catalog display name | NGC 809 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.75′ × 0.67′ |
| Distance | — |
| Separation | 1.50389° · 90.23′ |
| Catalog description | NGC 809 is a lenticular galaxy located in the constellation Cetus about 249 million light-years away from the Milky Way. The redshift of the galaxy is (z) 0.017 and it was first discovered by the American astronomer named Lewis Swift in November 1886. NGC 809 is a lenticular galaxy located in the constellation Cetus about 249 million light-years away from the Milky Way. The redshift of the galaxy is (z) 0.017 and it was first discovered by the American astronomer named Lewis Swift in November 1886. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1775 has the different designation NGC 809 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aipt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.836667%2013.819681&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 336. [AT2026aiyu](https://www.wis-tns.org/object/2026aiyu) near NGC1425

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1425 as this object's host. The 1.69335° (101.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-04T09:11:22Z · 67 days · 21.98 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1425** · `NGC1425` |
| Catalog display name | NGC1425 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.7 · 4.91′ × 2.15′ |
| Distance | — |
| Separation | 1.69335° · 101.60′ |
| Catalog description | NGC 1425, also known as IC 1988, is a spiral galaxy around 71 million light-years away in the constellation Fornax. It was discovered by William Herschel on Oct 9, 1790, and it belongs to the Fornax cluster. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=55.0302572%20-28.2610232&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 337. [AT2026aiyw](https://www.wis-tns.org/object/2026aiyw) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 1.91424° (114.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-08-29T06:05:16Z · 73 days · 20.41 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1340** · `NGC1340` |
| Catalog display name | NGC1340 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.4 · 5.12′ × 3.12′ |
| Distance | 18,600 kpc |
| Separation | 1.91424° · 114.85′ |
| Catalog description | NGC 1340 is an elliptical galaxy located in the constellation Fornax. Its speed relative to the cosmic microwave background is 1,126 ± 17 km/s, which corresponds to a Hubble Distance of 16.6 ± 1.2 Mpc. It was discovered by the German-British astronomer William Herschel in 1790, but it was added to the New General Catalog under the designation NGC 1344 later. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.8220395%20-29.1668897&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 338. [SN2026acjc](https://www.wis-tns.org/object/2026acjc) near Lynds Dark Nebula 1648 (LDN1648)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 5/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1648 (LDN1648) as this object's host. The 1.97714° (118.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ib |
| Redshift | 0.003012 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-19T18:54:31Z · 52 days · 19.85 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3788....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3788....1O/abstract) |
| Classification references | [2026TNSCR4119....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4119....1S/abstract) |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 1648 (LDN1648)** · `LDN1648` |
| Catalog display name | Lynds Dark Nebula 1648 (LDN1648) |
| Type / constellation | Dark nebula · Orion |
| Catalog magnitude / angular size | — · 92.09′ × 92.09′ |
| Distance | — |
| Separation | 1.97714° · 118.63′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026acjc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.0427969%20-11.1266929&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 339. [AT2026aiir](https://www.wis-tns.org/object/2026aiir) near Lynds Bright Nebula 790 (LBN790)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 790 (LBN790) as this object's host. The 0.58443° (35.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T11:44:01Z · 34 days · 20.1 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiir) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=118.8242602%2046.6763504&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
