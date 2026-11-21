# TNS transient opportunity review — 2026-11-15

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `5900d95b3deee825`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 385 review opportunities: 14 urgent, 371 watch, 0 expired
- Recommendations: 11 approve, 374 hold, 0 reject
- 385 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 870 staged rows collapsed to 841 unique TNS objects (29 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) | SN Ia | 13 | 16.1 | NGC4216 (Galaxy) | 0.39321° | near-field match | 100 | approve |
| urgent | [AT2026aina](https://www.wis-tns.org/object/2026aina) | Nova | 9 | 13.8 | NGC2052 (Nebula) | 0.15398° | near-field match | 100 | approve |
| urgent | [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) | SN | 12 | 18.49 | IC 2405 (Galaxy) | 0.45056° | near-field match | 97 | hold |
| urgent | [SN2026aicq](https://www.wis-tns.org/object/2026aicq) | SN II | 11 | 18.48 | IC 369 (Galaxy) | 0.91868° | near-field match | 97 | hold |
| urgent | [SN2026ainb](https://www.wis-tns.org/object/2026ainb) | SN Ia | 11 | 18.12 | IC 450 (Galaxy) | 1.07438° | near-field match | 90 | hold |
| urgent | [AT2026aizp](https://www.wis-tns.org/object/2026aizp) | transient_candidate | 6 | 18.1 | Atoms For Peace Galaxy (Galaxy) | 0.49861° | near-field match | 90 | approve |
| urgent | [AT2026ajcp](https://www.wis-tns.org/object/2026ajcp) | transient_candidate | 5 | 17.76 | NGC 4517 (Galaxy) | 0.80621° | near-field match | 90 | approve |
| urgent | [AT2026ajpr](https://www.wis-tns.org/object/2026ajpr) | transient_candidate | 5 | 18.03 | NGC3945 (Galaxy) | 0.86986° | near-field match | 90 | approve |
| urgent | [AT2026ajrb](https://www.wis-tns.org/object/2026ajrb) | transient_candidate | 2 | 18.48 | IC5270 (Galaxy) | 1.73389° | near-field match | 83 | approve |
| urgent | [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) | transient_candidate | 7 | 18.38 | IC656 (Nebula) | 0.87225° | near-field match | 80 | approve |
| urgent | [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) | transient_candidate | 1 | 18.22 | IC765 (Nebula) | 0.75222° | near-field match | 80 | approve |
| urgent | [SN2026aied](https://www.wis-tns.org/object/2026aied) | SN Ia | 12 | 18.33 | Lynds Bright Nebula 465 (LBN465) (HII) | 0.57960° | near-field match | 79 | approve |
| urgent | [AT2026aiuw](https://www.wis-tns.org/object/2026aiuw) | transient_candidate | 7 | 14.89 | Lynds Dark Nebula 637 (LDN637) (Dark nebula) | 1.17864° | near-field match | 75 | approve |
| urgent | [AT2026aiux](https://www.wis-tns.org/object/2026aiux) | transient_candidate | 7 | 17.29 | Lynds Dark Nebula 705 (LDN705) (Dark nebula) | 0.57543° | near-field match | 72 | approve |
| watch | [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) | transient_candidate | 2 | 19.32 | NGC2276 (Galaxy) | 0.19202° | near-field match | 93 | hold |
| watch | [SN2026agwk](https://www.wis-tns.org/object/2026agwk) | SN Ia-91T-like | 20 | 19.32 | IC391 (Galaxy) | 0.40294° | near-field match | 87 | hold |
| watch | [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) | SN II | 14 | 18.71 | IC 3 (Spiral galaxy) | 0.47363° | near-field match | 87 | hold |
| watch | [SN2026ahze](https://www.wis-tns.org/object/2026ahze) | SN Ia | 12 | 18.71 | NGC797 (Galaxy) | 1.92287° | near-field match | 80 | hold |
| watch | [AT2026aiuv](https://www.wis-tns.org/object/2026aiuv) | transient_candidate | 7 | 18.64 | IC 897 (Galaxy) | 0.45434° | near-field match | 80 | hold |
| watch | [AT2026ajcv](https://www.wis-tns.org/object/2026ajcv) | transient_candidate | 6 | 19.32 | IC 4297 (Galaxy) | 0.36926° | near-field match | 80 | hold |
| watch | [AT2026ajdx](https://www.wis-tns.org/object/2026ajdx) | transient_candidate | 7 | 19.5 | IC2160 (Galaxy) | 0.65192° | near-field match | 80 | hold |
| watch | [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) | transient_candidate | 2 | 19.37 | NGC2549 (Galaxy) | 0.59331° | near-field match | 80 | hold |
| watch | [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) | transient_candidate | 2 | 19.35 | NGC2768 (Galaxy) | 0.41880° | near-field match | 80 | hold |
| watch | [AT2026aive](https://www.wis-tns.org/object/2026aive) | transient_candidate | 7 | 18.74 | NGC2835 (Galaxy) | 1.04795° | near-field match | 73 | hold |
| watch | [AT2026aivf](https://www.wis-tns.org/object/2026aivf) | transient_candidate | 7 | 19.03 | NGC2835 (Galaxy) | 1.02455° | near-field match | 73 | hold |
| watch | [AT2026ajbn](https://www.wis-tns.org/object/2026ajbn) | transient_candidate | 5 | 19.45 | NGC3189 (Galaxy) | 1.65719° | near-field match | 73 | hold |
| watch | [AT2026ajdq](https://www.wis-tns.org/object/2026ajdq) | transient_candidate | 5 | 19.19 | IC 1600 (Galaxy) | 1.96019° | near-field match | 73 | hold |
| watch | [AT2026ajig](https://www.wis-tns.org/object/2026ajig) | transient_candidate | 3 | 19.78 | IC 38 (Galaxy) | 0.00569° | near-field match | 73 | hold |
| watch | [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) | transient_candidate | 3 | 19.46 | NGC1169 (Galaxy) | 1.01800° | near-field match | 73 | hold |
| watch | [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) | transient_candidate | 3 | 18.82 | NGC 3294 (Galaxy) | 1.51592° | near-field match | 73 | hold |
| watch | [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) | transient_candidate | 3 | 19 | IC486 (Galaxy) | 1.22917° | near-field match | 73 | hold |
| watch | [AT2026ajoo](https://www.wis-tns.org/object/2026ajoo) | transient_candidate | 2 | 22.76 | IC2058 (Galaxy) | 0.00834° | near-field match | 73 | hold |
| watch | [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) | transient_candidate | 1 | 19.45 | IC1733 (Galaxy) | 1.11166° | near-field match | 73 | hold |
| watch | [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) | transient_candidate | 2 | 19.27 | IC5261 (Galaxy) | 1.21834° | near-field match | 73 | hold |
| watch | [AT2026ajva](https://www.wis-tns.org/object/2026ajva) | transient_candidate | 0 | 21.81 | NGC 3561 (Galaxy) | 0.19660° | near-field match | 73 | hold |
| watch | [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) | transient_candidate | 0 | 22.15 | NGC 3561 (Galaxy) | 0.19359° | near-field match | 73 | hold |
| watch | [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) | transient_candidate | 16 | 19.31 | IC 2017 (Galaxy) | 0.36964° | near-field match | 72 | hold |
| watch | [AT2026aiyr](https://www.wis-tns.org/object/2026aiyr) | transient_candidate | 8 | 19.34 | NGC2566 (Galaxy) | 0.87981° | near-field match | 72 | hold |
| watch | [AT2026ajmb](https://www.wis-tns.org/object/2026ajmb) | transient_candidate | 4 | 19.13 | IC 1623 (CiG) | 0.67085° | near-field match | 70 | hold |
| watch | [SN2026agyk](https://www.wis-tns.org/object/2026agyk) | SN Ia | 20 | 18.8 | Barnard 152 (B152) (Dark nebula) | 0.73509° | near-field match | 69 | hold |
| watch | [SN2026aitx](https://www.wis-tns.org/object/2026aitx) | SN Ia | 7 | 19.57 | IC 2083 (Galaxy) | 1.14340° | near-field match | 68 | hold |
| watch | [AT2026aivh](https://www.wis-tns.org/object/2026aivh) | transient_candidate | 12 | 18.75 | Lynds Bright Nebula 749 (LBN749) (HII) | 0.23181° | near-field match | 67 | hold |
| watch | [AT2026agye](https://www.wis-tns.org/object/2026agye) | transient_candidate | 19 | 19.16 | IC 5124 (Galaxy) | 1.51433° | near-field match | 65 | hold |
| watch | [AT2026ahcr](https://www.wis-tns.org/object/2026ahcr) | transient_candidate | 18 | 19.43 | NGC7626 (Galaxy) | 1.62993° | near-field match | 65 | hold |
| watch | [AT2026aizi](https://www.wis-tns.org/object/2026aizi) | transient_candidate | 10 | 18.92 | IC 4660 (Galaxy) | 1.33546° | near-field match | 65 | hold |
| watch | [AT2026ajko](https://www.wis-tns.org/object/2026ajko) | transient_candidate | 14 | 22.23 | NGC864 (Galaxy) | 0.13264° | near-field match | 65 | hold |
| watch | [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) | transient_candidate | 3 | 18.5 | Lynds Bright Nebula 1043 (LBN1043) (HII) | 1.49482° | near-field match | 65 | hold |
| watch | [AT2026ajcg](https://www.wis-tns.org/object/2026ajcg) | transient_candidate | 8 | 16.87 | Collinder 394 (CR394) (Open cluster) | 0.65272° | near-field match | 64 | hold |
| watch | [AT2026aixw](https://www.wis-tns.org/object/2026aixw) | transient_candidate | 6 | 18.85 | IC877 (Nebula) | 1.87815° | near-field match | 63 | hold |
| watch | [AT2026aiyx](https://www.wis-tns.org/object/2026aiyx) | transient_candidate | 6 | 19.09 | IC5251 (Nebula) | 1.73252° | near-field match | 63 | hold |
| watch | [AT2026ajcc](https://www.wis-tns.org/object/2026ajcc) | transient_candidate | 6 | 18.82 | IC435 (reflection nebula) | 1.32248° | near-field match | 63 | hold |
| watch | [AT2026ajkf](https://www.wis-tns.org/object/2026ajkf) | transient_candidate | 3 | 19.07 | Collinder 409 (CR409) (Globular cluster) | 1.82025° | near-field match | 63 | hold |
| watch | [AT2026ajpu](https://www.wis-tns.org/object/2026ajpu) | transient_candidate | 3 | 19.22 | Blue Snowball (Planetary nebula) | 1.82980° | near-field match | 63 | hold |
| watch | [AT2026ajru](https://www.wis-tns.org/object/2026ajru) | transient_candidate | 1 | 18.7 | Collinder 176 (CR176) (Open cluster) | 1.06889° | near-field match | 63 | hold |
| watch | [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) | transient_candidate | 0 | 22.79 | IC5194 (Nebula) | 0.13206° | near-field match | 63 | hold |
| watch | [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) | transient_candidate | 0 | 21.79 | NGC894 (Nebula) | 0.00471° | near-field match | 63 | hold |
| watch | [SN2026agua](https://www.wis-tns.org/object/2026agua) | SN Ia | 22 | 19.33 | Lynds Dark Nebula 1571 (LDN1571) (Dark nebula) | 1.07129° | near-field match | 62 | hold |
| watch | [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) | transient_candidate | 1 | 19.17 | van den Bergh 12 (VDB12) (Nebula) | 0.51247° | near-field match | 62 | hold |
| watch | [SN2026ahhp](https://www.wis-tns.org/object/2026ahhp) | SN Ic | 16 | 21.98 | NGC1398 (Galaxy) | 1.54372° | near-field match | 60 | hold |
| watch | [AT2026aisx](https://www.wis-tns.org/object/2026aisx) | transient_candidate | 7 | 21.65 | Fornax B (Galaxy) | 0.65992° | near-field match | 60 | hold |
| watch | [AT2026aiyg](https://www.wis-tns.org/object/2026aiyg) | transient_candidate | 6 | 20.21 | IC2135 (Galaxy) | 0.98727° | near-field match | 60 | hold |
| watch | [AT2026ajbh](https://www.wis-tns.org/object/2026ajbh) | transient_candidate | 6 | 19.94 | IC302 (Galaxy) | 0.86924° | near-field match | 60 | hold |
| watch | [AT2026ajen](https://www.wis-tns.org/object/2026ajen) | transient_candidate | 7 | 23.05 | IC 1639 (Galaxy) | 0.27076° | near-field match | 60 | hold |
| watch | [AT2026ajfg](https://www.wis-tns.org/object/2026ajfg) | transient_candidate | 4 | 22.52 | NGC1340 (Galaxy) | 0.35306° | near-field match | 60 | hold |
| watch | [AT2026ajfh](https://www.wis-tns.org/object/2026ajfh) | transient_candidate | 5 | 19.55 | NGC1433 (Galaxy) | 0.67734° | near-field match | 60 | hold |
| watch | [AT2026ajfj](https://www.wis-tns.org/object/2026ajfj) | transient_candidate | 4 | 20.45 | IC 2039 (Galaxy) | 0.31321° | near-field match | 60 | hold |
| watch | [AT2026ajfk](https://www.wis-tns.org/object/2026ajfk) | transient_candidate | 4 | 21.23 | IC1993 (Galaxy) | 0.44583° | near-field match | 60 | hold |
| watch | [AT2026ajfl](https://www.wis-tns.org/object/2026ajfl) | transient_candidate | 4 | 22.63 | NGC1543 (Galaxy) | 0.58240° | near-field match | 60 | hold |
| watch | [AT2026ajiz](https://www.wis-tns.org/object/2026ajiz) | transient_candidate | 5 | 19.64 | NGC 2207 / IC 2163 (Galaxy) | 0.62701° | near-field match | 60 | hold |
| watch | [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) | transient_candidate | 5 | 20.16 | NGC779 (Galaxy) | 0.37574° | near-field match | 60 | hold |
| watch | [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) | transient_candidate | 3 | 19.72 | NGC3239 (Galaxy) | 0.74036° | near-field match | 60 | hold |
| watch | [AT2026ajkp](https://www.wis-tns.org/object/2026ajkp) | transient_candidate | 7 | 22.96 | Darth Vader's Galaxy (Galaxy) | 0.53744° | near-field match | 60 | hold |
| watch | [AT2026ajks](https://www.wis-tns.org/object/2026ajks) | transient_candidate | 5 | 22.25 | IC 5374 (Galaxy) | 0.92554° | near-field match | 60 | hold |
| watch | [AT2026ajkt](https://www.wis-tns.org/object/2026ajkt) | transient_candidate | 7 | 23.15 | IC 234 (Galaxy) | 0.57827° | near-field match | 60 | hold |
| watch | [AT2026ajlj](https://www.wis-tns.org/object/2026ajlj) | transient_candidate | 7 | 22.54 | IC 1749 (Galaxy) | 0.61175° | near-field match | 60 | hold |
| watch | [AT2026ajlk](https://www.wis-tns.org/object/2026ajlk) | transient_candidate | 7 | 22.61 | IC 1481 (Galaxy) | 0.75962° | near-field match | 60 | hold |
| watch | [AT2026ajlz](https://www.wis-tns.org/object/2026ajlz) | transient_candidate | 4 | 22.45 | IC 1481 (Galaxy) | 0.87422° | near-field match | 60 | hold |
| watch | [AT2026ajog](https://www.wis-tns.org/object/2026ajog) | transient_candidate | 7 | 20.22 | IC 21 (Galaxy) | 0.76970° | near-field match | 60 | hold |
| watch | [AT2026ajoh](https://www.wis-tns.org/object/2026ajoh) | transient_candidate | 2 | 22.19 | IC2006 (Galaxy) | 0.63770° | near-field match | 60 | hold |
| watch | [AT2026ajoq](https://www.wis-tns.org/object/2026ajoq) | transient_candidate | 2 | 22.27 | NGC1596 (Galaxy) | 0.89838° | near-field match | 60 | hold |
| watch | [AT2026ajor](https://www.wis-tns.org/object/2026ajor) | transient_candidate | 2 | 23.32 | NGC1672 (Galaxy) | 0.66270° | near-field match | 60 | hold |
| watch | [AT2026ajos](https://www.wis-tns.org/object/2026ajos) | transient_candidate | 2 | 22.1 | NGC1549 (Galaxy) | 0.50705° | near-field match | 60 | hold |
| watch | [AT2026ajpf](https://www.wis-tns.org/object/2026ajpf) | transient_candidate | 4 | 24.04 | NGC1527 (Galaxy) | 0.95803° | near-field match | 60 | hold |
| watch | [AT2026ajqp](https://www.wis-tns.org/object/2026ajqp) | transient_candidate | 1 | 23.6 | NGC1527 (Galaxy) | 0.92885° | near-field match | 60 | hold |
| watch | [AT2026ajqu](https://www.wis-tns.org/object/2026ajqu) | transient_candidate | 1 | 22.3 | Fornax B (Galaxy) | 0.90734° | near-field match | 60 | hold |
| watch | [AT2026ajqv](https://www.wis-tns.org/object/2026ajqv) | transient_candidate | 1 | 22.77 | NGC1374 (Galaxy) | 0.29655° | near-field match | 60 | hold |
| watch | [AT2026ajqw](https://www.wis-tns.org/object/2026ajqw) | transient_candidate | 1 | 23.09 | Fornax B (Galaxy) | 0.90002° | near-field match | 60 | hold |
| watch | [AT2026ajqx](https://www.wis-tns.org/object/2026ajqx) | transient_candidate | 1 | 22.19 | NGC1365 (Galaxy) | 0.95992° | near-field match | 60 | hold |
| watch | [AT2026ajqy](https://www.wis-tns.org/object/2026ajqy) | transient_candidate | 1 | 22.68 | NGC1332 (Galaxy) | 0.63270° | near-field match | 60 | hold |
| watch | [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) | transient_candidate | 1 | 20.85 | Messier 81 (Galaxy) | 0.68539° | near-field match | 60 | hold |
| watch | [AT2026ajri](https://www.wis-tns.org/object/2026ajri) | transient_candidate | 1 | 21.44 | IC 1540 (Galaxy) | 0.82912° | near-field match | 60 | hold |
| watch | [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) | transient_candidate | 2 | 19.61 | NGC2985 (Galaxy) | 0.55170° | near-field match | 60 | hold |
| watch | [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) | transient_candidate | 7 | 22.82 | IC 74 (Galaxy) | 0.60041° | near-field match | 60 | hold |
| watch | [AT2026ajta](https://www.wis-tns.org/object/2026ajta) | transient_candidate | 7 | 22.45 | IC1696 (Galaxy) | 0.88977° | near-field match | 60 | hold |
| watch | [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) | transient_candidate | 7 | 21.43 | NGC3521 (Galaxy) | 0.82591° | near-field match | 60 | hold |
| watch | [AT2026ajut](https://www.wis-tns.org/object/2026ajut) | transient_candidate | 0 | 22.82 | NGC 3561 (Galaxy) | 0.37521° | near-field match | 60 | hold |
| watch | [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) | transient_candidate | 0 | 22.02 | NGC 3561 (Galaxy) | 0.41178° | near-field match | 60 | hold |
| watch | [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) | transient_candidate | 0 | 22.11 | IC 1417 (Galaxy) | 0.66407° | near-field match | 60 | hold |
| watch | [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) | transient_candidate | 0 | 22.2 | IC 1417 (Galaxy) | 0.99563° | near-field match | 60 | hold |
| watch | [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) | transient_candidate | 0 | 21.89 | IC 1417 (Galaxy) | 0.95089° | near-field match | 60 | hold |
| watch | [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) | transient_candidate | 0 | 22.91 | IC 1419 (Galaxy) | 0.31675° | near-field match | 60 | hold |
| watch | [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) | transient_candidate | 0 | 21.59 | IC 1417 (Galaxy) | 0.46768° | near-field match | 60 | hold |
| watch | [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) | transient_candidate | 0 | 19.72 | IC2560 (Galaxy) | 0.97287° | near-field match | 60 | hold |
| watch | [AT2026aiep](https://www.wis-tns.org/object/2026aiep) | transient_candidate | 11 | 19.17 | IC5194 (Nebula) | 1.65297° | near-field match | 55 | hold |
| watch | [AT2026aizq](https://www.wis-tns.org/object/2026aizq) | transient_candidate | 6 | 18.67 | Lynds Bright Nebula 54 (LBN54) (HII) | 1.56600° | near-field match | 55 | hold |
| watch | [AT2026ajds](https://www.wis-tns.org/object/2026ajds) | transient_candidate | 5 | 19.01 | Boomerang nebula (Planetary nebula) | 1.53259° | near-field match | 55 | hold |
| watch | [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) | transient_candidate | 0 | 19.27 | Lynds Dark Nebula 1473 (LDN1473) (Dark nebula) | 1.48136° | near-field match | 55 | hold |
| watch | [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) | transient_candidate | 12 | 19.39 | Lynds Bright Nebula 718 (LBN718) (HII) | 0.53252° | near-field match | 54 | hold |
| watch | [AT2026aivb](https://www.wis-tns.org/object/2026aivb) | transient_candidate | 8 | 19.04 | Lynds Dark Nebula 387 (LDN387) (Dark nebula) | 0.97429° | near-field match | 54 | hold |
| watch | [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) | transient_candidate | 9 | 18.9 | The opal nebula (Planetary nebula) | 0.75975° | near-field match | 54 | hold |
| watch | [SN2026aela](https://www.wis-tns.org/object/2026aela) | SN Ia | 41 | 18.14 | NGC797 (Galaxy) | 1.46981° | near-field match | 53 | hold |
| watch | [AT2026aixb](https://www.wis-tns.org/object/2026aixb) | transient_candidate | 6 | 20.2 | IC1508 (Galaxy) | 1.64877° | near-field match | 53 | hold |
| watch | [AT2026aizb](https://www.wis-tns.org/object/2026aizb) | transient_candidate | 7 | 20.76 | IC 1776 (Galaxy) | 1.97947° | near-field match | 53 | hold |
| watch | [AT2026ajbj](https://www.wis-tns.org/object/2026ajbj) | transient_candidate | 6 | 20.17 | IC2007 (Galaxy) | 1.79494° | near-field match | 53 | hold |
| watch | [AT2026ajbo](https://www.wis-tns.org/object/2026ajbo) | transient_candidate | 5 | 19.95 | NGC 4346 (Galaxy) | 1.29956° | near-field match | 53 | hold |
| watch | [AT2026ajbw](https://www.wis-tns.org/object/2026ajbw) | transient_candidate | 6 | 20.02 | IC 632 (Galaxy) | 1.68563° | near-field match | 53 | hold |
| watch | [AT2026ajby](https://www.wis-tns.org/object/2026ajby) | transient_candidate | 6 | 20.2 | IC48 (Galaxy) | 1.83966° | near-field match | 53 | hold |
| watch | [AT2026ajek](https://www.wis-tns.org/object/2026ajek) | transient_candidate | 7 | 22.65 | IC 5241 (Galaxy) | 1.64483° | near-field match | 53 | hold |
| watch | [AT2026ajeo](https://www.wis-tns.org/object/2026ajeo) | transient_candidate | 7 | 22.9 | IC 1639 (Galaxy) | 1.33383° | near-field match | 53 | hold |
| watch | [AT2026ajff](https://www.wis-tns.org/object/2026ajff) | transient_candidate | 7 | 20.17 | NGC289 (Galaxy) | 1.00140° | near-field match | 53 | hold |
| watch | [AT2026ajji](https://www.wis-tns.org/object/2026ajji) | transient_candidate | 3 | 19.77 | NGC 3294 (Galaxy) | 1.46840° | near-field match | 53 | hold |
| watch | [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) | transient_candidate | 2 | 19.73 | NGC3198 (Galaxy) | 1.44295° | near-field match | 53 | hold |
| watch | [AT2026ajju](https://www.wis-tns.org/object/2026ajju) | transient_candidate | 3 | 19.62 | NGC3239 (Galaxy) | 1.03532° | near-field match | 53 | hold |
| watch | [AT2026ajlv](https://www.wis-tns.org/object/2026ajlv) | transient_candidate | 5 | 22.55 | IC 74 (Galaxy) | 1.59885° | near-field match | 53 | hold |
| watch | [AT2026ajlw](https://www.wis-tns.org/object/2026ajlw) | transient_candidate | 5 | 22.67 | NGC488 (Galaxy) | 1.28359° | near-field match | 53 | hold |
| watch | [AT2026ajlx](https://www.wis-tns.org/object/2026ajlx) | transient_candidate | 5 | 22.55 | IC 70 (Galaxy) | 1.02713° | near-field match | 53 | hold |
| watch | [AT2026ajmf](https://www.wis-tns.org/object/2026ajmf) | transient_candidate | 7 | 22.59 | IC 5241 (Galaxy) | 1.90571° | near-field match | 53 | hold |
| watch | [AT2026ajok](https://www.wis-tns.org/object/2026ajok) | transient_candidate | 2 | 19.77 | IC1993 (Galaxy) | 1.08961° | near-field match | 53 | hold |
| watch | [AT2026ajol](https://www.wis-tns.org/object/2026ajol) | transient_candidate | 2 | 22.52 | NGC1340 (Galaxy) | 1.17282° | near-field match | 53 | hold |
| watch | [AT2026ajqe](https://www.wis-tns.org/object/2026ajqe) | transient_candidate | 1 | 21.46 | IC1386 (Galaxy) | 1.97158° | near-field match | 53 | hold |
| watch | [AT2026ajqf](https://www.wis-tns.org/object/2026ajqf) | transient_candidate | 1 | 23.7 | IC2000 (Galaxy) | 1.19498° | near-field match | 53 | hold |
| watch | [AT2026ajqg](https://www.wis-tns.org/object/2026ajqg) | transient_candidate | 1 | 22.41 | NGC1527 (Galaxy) | 1.43634° | near-field match | 53 | hold |
| watch | [AT2026ajqm](https://www.wis-tns.org/object/2026ajqm) | transient_candidate | 1 | 21.44 | IC1386 (Galaxy) | 1.42198° | near-field match | 53 | hold |
| watch | [AT2026ajqz](https://www.wis-tns.org/object/2026ajqz) | transient_candidate | 1 | 22.81 | NGC1350 (Galaxy) | 1.39326° | near-field match | 53 | hold |
| watch | [AT2026ajra](https://www.wis-tns.org/object/2026ajra) | transient_candidate | 1 | 21.72 | IC1993 (Galaxy) | 1.92768° | near-field match | 53 | hold |
| watch | [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) | transient_candidate | 7 | 19.83 | IC1386 (Galaxy) | 1.28167° | near-field match | 53 | hold |
| watch | [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) | transient_candidate | 2 | 20.87 | IC 2016 (Galaxy) | 1.84241° | near-field match | 53 | hold |
| watch | [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) | transient_candidate | 1 | 19.52 | IC5338 (Galaxy) | 1.79914° | near-field match | 53 | hold |
| watch | [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) | transient_candidate | 2 | 19.68 | IC 17 (Galaxy) | 1.57726° | near-field match | 53 | hold |
| watch | [AT2026ajss](https://www.wis-tns.org/object/2026ajss) | transient_candidate | 4 | 22.86 | NGC 2207 / IC 2163 (Galaxy) | 1.55710° | near-field match | 53 | hold |
| watch | [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) | transient_candidate | 6 | 22.02 | NGC3521 (Galaxy) | 1.08432° | near-field match | 53 | hold |
| watch | [AT2026ajti](https://www.wis-tns.org/object/2026ajti) | transient_candidate | 5 | 22.44 | IC 1757 (Galaxy) | 1.42421° | near-field match | 53 | hold |
| watch | [AT2026ajum](https://www.wis-tns.org/object/2026ajum) | transient_candidate | 4 | 22.35 | IC 1540 (Galaxy) | 1.37052° | near-field match | 53 | hold |
| watch | [AT2026ajux](https://www.wis-tns.org/object/2026ajux) | transient_candidate | 0 | 22.92 | NGC 3561 (Galaxy) | 1.74911° | near-field match | 53 | hold |
| watch | [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) | transient_candidate | 0 | 22.32 | IC 1419 (Galaxy) | 1.06627° | near-field match | 53 | hold |
| watch | [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) | transient_candidate | 0 | 22.34 | IC 1417 (Galaxy) | 1.37982° | near-field match | 53 | hold |
| watch | [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) | transient_candidate | 0 | 21.97 | IC 1419 (Galaxy) | 1.70955° | near-field match | 53 | hold |
| watch | [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) | transient_candidate | 0 | 22.71 | IC 1419 (Galaxy) | 1.38932° | near-field match | 53 | hold |
| watch | [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) | transient_candidate | 0 | 20.46 | IC 1417 (Galaxy) | 1.85790° | near-field match | 53 | hold |
| watch | [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) | transient_candidate | 0 | 22.31 | IC 1419 (Galaxy) | 1.29911° | near-field match | 53 | hold |
| watch | [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) | transient_candidate | 0 | 22.48 | IC 1417 (Galaxy) | 1.26051° | near-field match | 53 | hold |
| watch | [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) | transient_candidate | 0 | 21.14 | IC 1417 (Galaxy) | 1.52083° | near-field match | 53 | hold |
| watch | [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) | transient_candidate | 0 | 22.74 | NGC 3561 (Galaxy) | 1.67055° | near-field match | 53 | hold |
| watch | [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) | transient_candidate | 0 | 22.77 | IC 1419 (Galaxy) | 1.64042° | near-field match | 53 | hold |
| watch | [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) | transient_candidate | 0 | 22.7 | IC 1417 (Galaxy) | 1.79224° | near-field match | 53 | hold |
| watch | [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) | transient_candidate | 0 | 22.99 | IC 1417 (Galaxy) | 1.40126° | near-field match | 53 | hold |
| watch | [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) | transient_candidate | 0 | 22.77 | NGC 3561 (Galaxy) | 1.85355° | near-field match | 53 | hold |
| watch | [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) | transient_candidate | 0 | 22.84 | IC 1417 (Galaxy) | 1.52748° | near-field match | 53 | hold |
| watch | [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) | transient_candidate | 0 | 22.67 | NGC 3561 (Galaxy) | 1.03799° | near-field match | 53 | hold |
| watch | [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) | transient_candidate | 0 | 21.31 | IC 1417 (Galaxy) | 1.38720° | near-field match | 53 | hold |
| watch | [AT2026ajws](https://www.wis-tns.org/object/2026ajws) | transient_candidate | 0 | 22.61 | IC 1417 (Galaxy) | 1.64454° | near-field match | 53 | hold |
| watch | [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) | transient_candidate | 0 | 19.73 | IC 1419 (Galaxy) | 1.89146° | near-field match | 53 | hold |
| watch | [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) | transient_candidate | 0 | 22.68 | IC 1417 (Galaxy) | 1.86530° | near-field match | 53 | hold |
| watch | [AT2026ajww](https://www.wis-tns.org/object/2026ajww) | transient_candidate | 0 | 22.29 | IC 1417 (Galaxy) | 1.35306° | near-field match | 53 | hold |
| watch | [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) | transient_candidate | 0 | 23.14 | IC 1417 (Galaxy) | 1.79292° | near-field match | 53 | hold |
| watch | [AT2026aiki](https://www.wis-tns.org/object/2026aiki) | transient_candidate | 9 | 20.27 | IC 230 (Galaxy) | 0.98313° | near-field match | 52 | hold |
| watch | [AT2026aiup](https://www.wis-tns.org/object/2026aiup) | transient_candidate | 12 | 20.72 | IC148 (Galaxy) | 0.32866° | near-field match | 52 | hold |
| watch | [AT2026aivo](https://www.wis-tns.org/object/2026aivo) | transient_candidate | 14 | 22.3 | NGC864 (Galaxy) | 0.76363° | near-field match | 52 | hold |
| watch | [AT2026aivt](https://www.wis-tns.org/object/2026aivt) | transient_candidate | 12 | 22.44 | NGC864 (Galaxy) | 0.37622° | near-field match | 52 | hold |
| watch | [AT2026aivv](https://www.wis-tns.org/object/2026aivv) | transient_candidate | 10 | 22.66 | IC 173 (Galaxy) | 0.25518° | near-field match | 52 | hold |
| watch | [AT2026aiwb](https://www.wis-tns.org/object/2026aiwb) | transient_candidate | 8 | 22.88 | Darth Vader's Galaxy (Galaxy) | 0.88875° | near-field match | 52 | hold |
| watch | [AT2026aiwc](https://www.wis-tns.org/object/2026aiwc) | transient_candidate | 8 | 22.4 | Darth Vader's Galaxy (Galaxy) | 0.41006° | near-field match | 52 | hold |
| watch | [AT2026aixe](https://www.wis-tns.org/object/2026aixe) | transient_candidate | 17 | 20.05 | IC1860 (Galaxy) | 0.49089° | near-field match | 52 | hold |
| watch | [AT2026aixg](https://www.wis-tns.org/object/2026aixg) | transient_candidate | 10 | 20.63 | IC1895 (Galaxy) | 0.41742° | near-field match | 52 | hold |
| watch | [AT2026aiyi](https://www.wis-tns.org/object/2026aiyi) | transient_candidate | 17 | 20.5 | IC1628 (Galaxy) | 0.47290° | near-field match | 52 | hold |
| watch | [AT2026aiyy](https://www.wis-tns.org/object/2026aiyy) | transient_candidate | 9 | 19.87 | NGC7457 (Galaxy) | 0.53496° | near-field match | 52 | hold |
| watch | [AT2026ajai](https://www.wis-tns.org/object/2026ajai) | transient_candidate | 16 | 22.25 | NGC741 (Galaxy) | 0.59906° | near-field match | 52 | hold |
| watch | [AT2026ajaj](https://www.wis-tns.org/object/2026ajaj) | transient_candidate | 16 | 22.02 | IC 1757 (Galaxy) | 0.93441° | near-field match | 52 | hold |
| watch | [AT2026ajar](https://www.wis-tns.org/object/2026ajar) | transient_candidate | 8 | 19.82 | NGC3169 (Galaxy) | 0.74868° | near-field match | 52 | hold |
| watch | [AT2026ajbz](https://www.wis-tns.org/object/2026ajbz) | transient_candidate | 12 | 20.81 | IC163 (Galaxy) | 0.66373° | near-field match | 52 | hold |
| watch | [AT2026ajdn](https://www.wis-tns.org/object/2026ajdn) | transient_candidate | 16 | 22.14 | NGC7585 (Galaxy) | 0.84567° | near-field match | 52 | hold |
| watch | [AT2026ajec](https://www.wis-tns.org/object/2026ajec) | transient_candidate | 10 | 23.01 | NGC488 (Galaxy) | 0.68536° | near-field match | 52 | hold |
| watch | [AT2026ajed](https://www.wis-tns.org/object/2026ajed) | transient_candidate | 10 | 22.77 | IC 173 (Galaxy) | 0.78871° | near-field match | 52 | hold |
| watch | [AT2026ajee](https://www.wis-tns.org/object/2026ajee) | transient_candidate | 10 | 22.59 | IC 1776 (Galaxy) | 0.75879° | near-field match | 52 | hold |
| watch | [AT2026ajei](https://www.wis-tns.org/object/2026ajei) | transient_candidate | 8 | 21.94 | NGC3640 (Galaxy) | 0.37997° | near-field match | 52 | hold |
| watch | [AT2026ajlh](https://www.wis-tns.org/object/2026ajlh) | transient_candidate | 8 | 21.69 | NGC3640 (Galaxy) | 0.60624° | near-field match | 52 | hold |
| watch | [AT2026ajmu](https://www.wis-tns.org/object/2026ajmu) | transient_candidate | 10 | 21.64 | IC2421 (Galaxy) | 0.41790° | near-field match | 52 | hold |
| watch | [AT2026ajmx](https://www.wis-tns.org/object/2026ajmx) | transient_candidate | 9 | 22.35 | NGC2549 (Galaxy) | 0.72858° | near-field match | 52 | hold |
| watch | [AT2026ajnl](https://www.wis-tns.org/object/2026ajnl) | transient_candidate | 17 | 21.1 | NGC1058 (Galaxy) | 0.90832° | near-field match | 52 | hold |
| watch | [AT2026ajsm](https://www.wis-tns.org/object/2026ajsm) | transient_candidate | 17 | 20.24 | IC1919 (Galaxy) | 0.30868° | near-field match | 52 | hold |
| watch | [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) | transient_candidate | 17 | 21.33 | IC178 (Galaxy) | 0.93972° | near-field match | 52 | hold |
| watch | [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) | transient_candidate | 12 | 20.75 | NGC 2964 (Galaxy) | 0.25419° | near-field match | 52 | hold |
| watch | [SN2026ahyd](https://www.wis-tns.org/object/2026ahyd) | SN Ia | 12 | 19.53 | IC5366 (Nebula) | 1.01813° | near-field match | 50 | hold |
| watch | [AT2026ajlm](https://www.wis-tns.org/object/2026ajlm) | transient_candidate | 7 | 22.24 | NGC7613 (Nebula) | 0.70355° | near-field match | 50 | hold |
| watch | [AT2026ajnx](https://www.wis-tns.org/object/2026ajnx) | transient_candidate | 2 | 21.82 | NGC894 (Nebula) | 0.40162° | near-field match | 50 | hold |
| watch | [AT2026ajqr](https://www.wis-tns.org/object/2026ajqr) | transient_candidate | 1 | 22.14 | Messier 72 (M72) (Globular cluster) | 0.84769° | near-field match | 50 | hold |
| watch | [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) | transient_candidate | 0 | 21.93 | NGC7158 (Nebula) | 0.76418° | near-field match | 50 | hold |
| watch | [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) | transient_candidate | 0 | 22.2 | NGC7158 (Nebula) | 0.83221° | near-field match | 50 | hold |
| watch | [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) | transient_candidate | 0 | 21.24 | NGC7158 (Nebula) | 0.38606° | near-field match | 50 | hold |
| watch | [AT2026aifu](https://www.wis-tns.org/object/2026aifu) | transient_candidate | 11 | 19.01 | Lynds Bright Nebula 1025 (LBN1025) (HII) | 1.13184° | near-field match | 47 | hold |
| watch | [AT2026aimn](https://www.wis-tns.org/object/2026aimn) | transient_candidate | 9 | 19.23 | van den Bergh 29 (VDB29) (Nebula) | 1.12187° | near-field match | 47 | hold |
| watch | [AT2026aizl](https://www.wis-tns.org/object/2026aizl) | transient_candidate | 8 | 18.61 | Lynds Dark Nebula 1563 (LDN1563) (Dark nebula) | 1.36769° | near-field match | 47 | hold |
| watch | [AT2026ahdm](https://www.wis-tns.org/object/2026ahdm) | transient_candidate | 18 | 21.64 | IC 1507 (Galaxy) | 1.56833° | near-field match | 45 | hold |
| watch | [AT2026ahhy](https://www.wis-tns.org/object/2026ahhy) | transient_candidate | 16 | 21.58 | NGC7606 (Galaxy) | 1.55641° | near-field match | 45 | hold |
| watch | [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) | transient_candidate | 15 | 19.8 | IC1401 (Galaxy) | 1.09401° | near-field match | 45 | hold |
| watch | [AT2026aicw](https://www.wis-tns.org/object/2026aicw) | transient_candidate | 17 | 19.96 | IC1574 (Galaxy) | 1.16063° | near-field match | 45 | hold |
| watch | [AT2026aidv](https://www.wis-tns.org/object/2026aidv) | transient_candidate | 10 | 19.73 | IC 5298 (Galaxy) | 1.04272° | near-field match | 45 | hold |
| watch | [AT2026aigp](https://www.wis-tns.org/object/2026aigp) | transient_candidate | 14 | 19.83 | IC2007 (Galaxy) | 1.25561° | near-field match | 45 | hold |
| watch | [AT2026aihe](https://www.wis-tns.org/object/2026aihe) | transient_candidate | 14 | 19.64 | NGC2855 (Galaxy) | 1.17126° | near-field match | 45 | hold |
| watch | [AT2026aiit](https://www.wis-tns.org/object/2026aiit) | transient_candidate | 20 | 20.1 | IC 536 (Galaxy) | 1.35004° | near-field match | 45 | hold |
| watch | [AT2026ainu](https://www.wis-tns.org/object/2026ainu) | transient_candidate | 13 | 19.94 | NGC1637 (Galaxy) | 1.60141° | near-field match | 45 | hold |
| watch | [AT2026airi](https://www.wis-tns.org/object/2026airi) | transient_candidate | 8 | 20.14 | NGC636 (Galaxy) | 1.79687° | near-field match | 45 | hold |
| watch | [AT2026aiul](https://www.wis-tns.org/object/2026aiul) | transient_candidate | 14 | 21.17 | Caldwell 44 (C44) (Galaxy) | 1.56654° | near-field match | 45 | hold |
| watch | [AT2026aiun](https://www.wis-tns.org/object/2026aiun) | transient_candidate | 12 | 20.54 | IC 1757 (Galaxy) | 1.41669° | near-field match | 45 | hold |
| watch | [AT2026aius](https://www.wis-tns.org/object/2026aius) | transient_candidate | 9 | 19.94 | NGC797 (Galaxy) | 1.88178° | near-field match | 45 | hold |
| watch | [AT2026aivi](https://www.wis-tns.org/object/2026aivi) | transient_candidate | 12 | 19.82 | IC 1797 (Galaxy) | 1.40546° | near-field match | 45 | hold |
| watch | [AT2026aivw](https://www.wis-tns.org/object/2026aivw) | transient_candidate | 10 | 21.91 | IC 1757 (Galaxy) | 1.24572° | near-field match | 45 | hold |
| watch | [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) | transient_candidate | 14 | 21.09 | NGC2681 (Galaxy) | 1.89726° | near-field match | 45 | hold |
| watch | [AT2026aiwk](https://www.wis-tns.org/object/2026aiwk) | transient_candidate | 26 | 19.72 | Caldwell 48 (C48) (Galaxy) | 1.74454° | near-field match | 45 | hold |
| watch | [AT2026aiwu](https://www.wis-tns.org/object/2026aiwu) | transient_candidate | 9 | 20.14 | IC 1568 (Galaxy) | 1.34453° | near-field match | 45 | hold |
| watch | [AT2026aixs](https://www.wis-tns.org/object/2026aixs) | transient_candidate | 13 | 19.97 | NGC3610 (Galaxy) | 1.63021° | near-field match | 45 | hold |
| watch | [AT2026aiyb](https://www.wis-tns.org/object/2026aiyb) | transient_candidate | 14 | 20.39 | IC392 (Galaxy) | 1.52492° | near-field match | 45 | hold |
| watch | [AT2026aiyd](https://www.wis-tns.org/object/2026aiyd) | transient_candidate | 16 | 20 | IC 1481 (Galaxy) | 1.26208° | near-field match | 45 | hold |
| watch | [AT2026aiye](https://www.wis-tns.org/object/2026aiye) | transient_candidate | 8 | 19.93 | IC1616 (Galaxy) | 1.28647° | near-field match | 45 | hold |
| watch | [AT2026aiyh](https://www.wis-tns.org/object/2026aiyh) | transient_candidate | 10 | 20.26 | IC2152 (Galaxy) | 1.16508° | near-field match | 45 | hold |
| watch | [AT2026aizu](https://www.wis-tns.org/object/2026aizu) | transient_candidate | 17 | 22.25 | IC 1507 (Galaxy) | 1.65578° | near-field match | 45 | hold |
| watch | [AT2026aizw](https://www.wis-tns.org/object/2026aizw) | transient_candidate | 16 | 22.11 | IC 5374 (Galaxy) | 1.76396° | near-field match | 45 | hold |
| watch | [AT2026aizx](https://www.wis-tns.org/object/2026aizx) | transient_candidate | 14 | 22.3 | IC1696 (Galaxy) | 1.77435° | near-field match | 45 | hold |
| watch | [AT2026ajae](https://www.wis-tns.org/object/2026ajae) | transient_candidate | 29 | 22.56 | NGC488 (Galaxy) | 1.54038° | near-field match | 45 | hold |
| watch | [AT2026ajaf](https://www.wis-tns.org/object/2026ajaf) | transient_candidate | 16 | 22.36 | IC 1481 (Galaxy) | 1.97393° | near-field match | 45 | hold |
| watch | [AT2026ajah](https://www.wis-tns.org/object/2026ajah) | transient_candidate | 16 | 21.96 | IC1696 (Galaxy) | 1.73881° | near-field match | 45 | hold |
| watch | [AT2026ajay](https://www.wis-tns.org/object/2026ajay) | transient_candidate | 27 | 21.83 | Andromeda Galaxy (Galaxy) | 1.60207° | near-field match | 45 | hold |
| watch | [AT2026ajbe](https://www.wis-tns.org/object/2026ajbe) | transient_candidate | 15 | 21.27 | IC 180 (Galaxy) | 1.55678° | near-field match | 45 | hold |
| watch | [AT2026ajbr](https://www.wis-tns.org/object/2026ajbr) | transient_candidate | 12 | 20.52 | NGC2841 (Galaxy) | 1.54687° | near-field match | 45 | hold |
| watch | [AT2026ajcl](https://www.wis-tns.org/object/2026ajcl) | transient_candidate | 10 | 20.82 | IC 1873 (Galaxy) | 1.66353° | near-field match | 45 | hold |
| watch | [AT2026ajcz](https://www.wis-tns.org/object/2026ajcz) | transient_candidate | 11 | 19.92 | NGC3319 (Galaxy) | 1.96765° | near-field match | 45 | hold |
| watch | [AT2026ajdj](https://www.wis-tns.org/object/2026ajdj) | transient_candidate | 16 | 21.21 | NGC7727 (Galaxy) | 1.24258° | near-field match | 45 | hold |
| watch | [AT2026ajdo](https://www.wis-tns.org/object/2026ajdo) | transient_candidate | 16 | 21.42 | NGC7606 (Galaxy) | 1.40071° | near-field match | 45 | hold |
| watch | [AT2026ajea](https://www.wis-tns.org/object/2026ajea) | transient_candidate | 14 | 22.17 | IC 197 (Galaxy) | 1.52695° | near-field match | 45 | hold |
| watch | [AT2026ajef](https://www.wis-tns.org/object/2026ajef) | transient_candidate | 8 | 22.5 | IC1696 (Galaxy) | 1.28974° | near-field match | 45 | hold |
| watch | [AT2026ajla](https://www.wis-tns.org/object/2026ajla) | transient_candidate | 16 | 21.76 | IC 197 (Galaxy) | 1.37876° | near-field match | 45 | hold |
| watch | [AT2026ajlb](https://www.wis-tns.org/object/2026ajlb) | transient_candidate | 11 | 22.99 | IC 1507 (Galaxy) | 1.75832° | near-field match | 45 | hold |
| watch | [AT2026ajld](https://www.wis-tns.org/object/2026ajld) | transient_candidate | 10 | 23.02 | IC 3 (Spiral galaxy) | 1.91032° | near-field match | 45 | hold |
| watch | [AT2026ajle](https://www.wis-tns.org/object/2026ajle) | transient_candidate | 10 | 23.03 | IC1696 (Galaxy) | 1.84067° | near-field match | 45 | hold |
| watch | [AT2026ajlf](https://www.wis-tns.org/object/2026ajlf) | transient_candidate | 10 | 22.81 | IC 173 (Galaxy) | 1.30826° | near-field match | 45 | hold |
| watch | [AT2026ajlg](https://www.wis-tns.org/object/2026ajlg) | transient_candidate | 8 | 22.56 | IC 1757 (Galaxy) | 1.52105° | near-field match | 45 | hold |
| watch | [AT2026ajli](https://www.wis-tns.org/object/2026ajli) | transient_candidate | 8 | 21.42 | NGC3640 (Galaxy) | 1.32202° | near-field match | 45 | hold |
| watch | [AT2026ajnc](https://www.wis-tns.org/object/2026ajnc) | transient_candidate | 8 | 21.47 | NGC205 (Galaxy) | 1.21009° | near-field match | 45 | hold |
| watch | [AT2026ajnt](https://www.wis-tns.org/object/2026ajnt) | transient_candidate | 12 | 20.27 | NGC2859 (Galaxy) | 1.90673° | near-field match | 45 | hold |
| watch | [AT2026ajnu](https://www.wis-tns.org/object/2026ajnu) | transient_candidate | 11 | 21.73 | IC 189 (Galaxy) | 1.32564° | near-field match | 45 | hold |
| watch | [AT2026ajpc](https://www.wis-tns.org/object/2026ajpc) | transient_candidate | 16 | 20.3 | NGC 1954 (Galaxy) | 1.01085° | near-field match | 45 | hold |
| watch | [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) | transient_candidate | 14 | 21.43 | NGC925 (Galaxy) | 1.68238° | near-field match | 45 | hold |
| watch | [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) | transient_candidate | 11 | 21.33 | IC509 (Galaxy) | 1.28504° | near-field match | 45 | hold |
| watch | [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) | transient_candidate | 11 | 21.32 | UFO Galaxy (Galaxy) | 1.99519° | near-field match | 45 | hold |
| watch | [AT2026ajty](https://www.wis-tns.org/object/2026ajty) | transient_candidate | 11 | 21.65 | IC2378 (Galaxy) | 1.21289° | near-field match | 45 | hold |
| watch | [AT2026ajug](https://www.wis-tns.org/object/2026ajug) | transient_candidate | 8 | 21.26 | IC1525 (Galaxy) | 1.31062° | near-field match | 45 | hold |
| watch | [SN2026aaee](https://www.wis-tns.org/object/2026aaee) | SN II | 77 | 17.12 | IC 2360 (Star) | 1.01344° | near-field match | 43 | hold |
| watch | [AT2026aiwn](https://www.wis-tns.org/object/2026aiwn) | transient_candidate | 7 | 20.08 | NGC56 (Nebula) | 1.79121° | near-field match | 43 | hold |
| watch | [AT2026aixc](https://www.wis-tns.org/object/2026aixc) | transient_candidate | 6 | 20.38 | IC5383 (Nebula) | 1.16692° | near-field match | 43 | hold |
| watch | [AT2026aixy](https://www.wis-tns.org/object/2026aixy) | transient_candidate | 7 | 20.58 | IC333 (Nebula) | 1.08009° | near-field match | 43 | hold |
| watch | [AT2026aiys](https://www.wis-tns.org/object/2026aiys) | transient_candidate | 6 | 19.55 | IC5251 (Nebula) | 1.74747° | near-field match | 43 | hold |
| watch | [AT2026aiyz](https://www.wis-tns.org/object/2026aiyz) | transient_candidate | 7 | 20.43 | IC229 (Nebula) | 1.20798° | near-field match | 43 | hold |
| watch | [AT2026ajlo](https://www.wis-tns.org/object/2026ajlo) | transient_candidate | 7 | 22.65 | NGC7565 (Nebula) | 1.97938° | near-field match | 43 | hold |
| watch | [AT2026ajlt](https://www.wis-tns.org/object/2026ajlt) | transient_candidate | 5 | 22.76 | IC1651 (Nebula) | 1.25864° | near-field match | 43 | hold |
| watch | [AT2026ajma](https://www.wis-tns.org/object/2026ajma) | transient_candidate | 4 | 22.33 | NGC7668 (Nebula) | 1.52330° | near-field match | 43 | hold |
| watch | [AT2026ajne](https://www.wis-tns.org/object/2026ajne) | transient_candidate | 6 | 21.45 | Collinder 116 (CR116) (Open cluster) | 1.30710° | near-field match | 43 | hold |
| watch | [AT2026ajng](https://www.wis-tns.org/object/2026ajng) | transient_candidate | 6 | 20.81 | IC2350 (Nebula) | 1.54892° | near-field match | 43 | hold |
| watch | [AT2026ajob](https://www.wis-tns.org/object/2026ajob) | transient_candidate | 2 | 22.59 | NGC894 (Nebula) | 1.67540° | near-field match | 43 | hold |
| watch | [AT2026ajou](https://www.wis-tns.org/object/2026ajou) | transient_candidate | 3 | 19.83 | IC5251 (Nebula) | 1.43468° | near-field match | 43 | hold |
| watch | [AT2026ajpi](https://www.wis-tns.org/object/2026ajpi) | transient_candidate | 3 | 22.62 | NGC7526 (Nebula) | 1.96789° | near-field match | 43 | hold |
| watch | [AT2026ajpy](https://www.wis-tns.org/object/2026ajpy) | transient_candidate | 4 | 21.42 | Messier 30 (M30) (Globular cluster) | 1.04427° | near-field match | 43 | hold |
| watch | [AT2026ajqb](https://www.wis-tns.org/object/2026ajqb) | transient_candidate | 1 | 21.61 | Messier 72 (M72) (Globular cluster) | 1.44459° | near-field match | 43 | hold |
| watch | [AT2026ajqn](https://www.wis-tns.org/object/2026ajqn) | transient_candidate | 1 | 22.45 | NGC894 (Nebula) | 1.39431° | near-field match | 43 | hold |
| watch | [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) | transient_candidate | 0 | 19.77 | NGC3578 (Nebula) | 1.46782° | near-field match | 43 | hold |
| watch | [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) | transient_candidate | 7 | 22.88 | NGC728 (Nebula) | 1.25970° | near-field match | 43 | hold |
| watch | [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) | transient_candidate | 7 | 21.48 | NGC3387 (Nebula) | 1.71033° | near-field match | 43 | hold |
| watch | [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) | transient_candidate | 5 | 21.8 | NGC7453 (Nebula) | 1.30353° | near-field match | 43 | hold |
| watch | [AT2026ajur](https://www.wis-tns.org/object/2026ajur) | transient_candidate | 0 | 23.23 | NGC7158 (Nebula) | 1.05093° | near-field match | 43 | hold |
| watch | [AT2026ajve](https://www.wis-tns.org/object/2026ajve) | transient_candidate | 0 | 22.03 | IC5194 (Nebula) | 1.56732° | near-field match | 43 | hold |
| watch | [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) | transient_candidate | 0 | 21.75 | IC5194 (Nebula) | 1.82559° | near-field match | 43 | hold |
| watch | [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) | transient_candidate | 0 | 22.52 | IC1457 (Nebula) | 1.62885° | near-field match | 43 | hold |
| watch | [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) | transient_candidate | 0 | 21.84 | IC5194 (Nebula) | 1.34031° | near-field match | 43 | hold |
| watch | [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) | transient_candidate | 0 | 20.66 | IC1457 (Nebula) | 1.88540° | near-field match | 43 | hold |
| watch | [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) | transient_candidate | 0 | 21.83 | NGC894 (Nebula) | 1.21470° | near-field match | 43 | hold |
| watch | [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) | transient_candidate | 0 | 21.12 | NGC7158 (Nebula) | 1.66580° | near-field match | 43 | hold |
| watch | [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) | transient_candidate | 0 | 21.76 | NGC7158 (Nebula) | 1.17313° | near-field match | 43 | hold |
| watch | [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) | transient_candidate | 6 | 22.61 | NGC894 (Nebula) | 1.74562° | near-field match | 43 | hold |
| watch | [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) | transient_candidate | 6 | 20.08 | NGC1498 (Open cluster) | 1.41273° | near-field match | 43 | hold |
| watch | [AT2026aias](https://www.wis-tns.org/object/2026aias) | transient_candidate | 16 | 20.04 | IC333 (Nebula) | 0.69484° | near-field match | 42 | hold |
| watch | [AT2026aiat](https://www.wis-tns.org/object/2026aiat) | transient_candidate | 14 | 19.61 | Collinder 163 (CR163) (Open cluster) | 0.39277° | near-field match | 42 | hold |
| watch | [AT2026aihc](https://www.wis-tns.org/object/2026aihc) | transient_candidate | 17 | 20.27 | NGC7666 (Nebula) | 0.34612° | near-field match | 42 | hold |
| watch | [AT2026aiko](https://www.wis-tns.org/object/2026aiko) | transient_candidate | 9 | 19.85 | NGC7158 (Nebula) | 0.38092° | near-field match | 42 | hold |
| watch | [SN2026airg](https://www.wis-tns.org/object/2026airg) | SN II | 8 | 19.93 | Sharpless 260 (SH2-260) (HII) | 1.20103° | near-field match | 42 | hold |
| watch | [AT2026aivj](https://www.wis-tns.org/object/2026aivj) | transient_candidate | 10 | 20.47 | IC1547 (Nebula) | 0.56558° | near-field match | 42 | hold |
| watch | [AT2026aiwl](https://www.wis-tns.org/object/2026aiwl) | transient_candidate | 9 | 20.35 | IC5344 (Nebula) | 0.90611° | near-field match | 42 | hold |
| watch | [AT2026aiws](https://www.wis-tns.org/object/2026aiws) | transient_candidate | 10 | 20.91 | Collinder 59 (CR59) (Open cluster) | 0.80866° | near-field match | 42 | hold |
| watch | [AT2026aixd](https://www.wis-tns.org/object/2026aixd) | transient_candidate | 10 | 20 | NGC7826 (Nebula) | 0.88575° | near-field match | 42 | hold |
| watch | [AT2026aixn](https://www.wis-tns.org/object/2026aixn) | transient_candidate | 28 | 20.95 | NGC2531 (Nebula) | 0.88316° | near-field match | 42 | hold |
| watch | [AT2026aixq](https://www.wis-tns.org/object/2026aixq) | transient_candidate | 27 | 20.62 | Hind's variable nebula (reflection nebula) | 0.75249° | near-field match | 42 | hold |
| watch | [AT2026ajan](https://www.wis-tns.org/object/2026ajan) | transient_candidate | 11 | 22.15 | NGC7668 (Nebula) | 0.77578° | near-field match | 42 | hold |
| watch | [AT2026ajbi](https://www.wis-tns.org/object/2026ajbi) | transient_candidate | 6 | 20.84 | Barnard 215 (B215) (Dark nebula) | 0.54619° | near-field match | 42 | hold |
| watch | [AT2026ajdc](https://www.wis-tns.org/object/2026ajdc) | transient_candidate | 12 | 19.73 | IC240 (Nebula) | 0.55882° | near-field match | 42 | hold |
| watch | [AT2026ajdy](https://www.wis-tns.org/object/2026ajdy) | transient_candidate | 8 | 20.06 | NGC272 (Open cluster) | 0.82818° | near-field match | 42 | hold |
| watch | [AT2026ajmh](https://www.wis-tns.org/object/2026ajmh) | transient_candidate | 27 | 21.78 | IC1665 (Nebula) | 0.81988° | near-field match | 42 | hold |
| watch | [AT2026ajmi](https://www.wis-tns.org/object/2026ajmi) | transient_candidate | 27 | 21.94 | NGC843 (Nebula) | 0.79289° | near-field match | 42 | hold |
| watch | [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) | transient_candidate | 3 | 19.72 | Lynds Bright Nebula 439 (LBN439) (HII) | 0.79678° | near-field match | 42 | hold |
| watch | [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) | transient_candidate | 8 | 22.16 | IC111 (Nebula) | 0.80147° | near-field match | 42 | hold |
| watch | [AT2026ajup](https://www.wis-tns.org/object/2026ajup) | transient_candidate | 12 | 21.25 | Collinder 116 (CR116) (Open cluster) | 0.84314° | near-field match | 42 | hold |
| watch | [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) | transient_candidate | 15 | 23.8 | NGC894 (Nebula) | 0.53340° | near-field match | 42 | hold |
| watch | [AT2026ahhj](https://www.wis-tns.org/object/2026ahhj) | transient_candidate | 16 | 22.31 | NGC7453 (Nebula) | 1.72039° | near-field match | 35 | hold |
| watch | [AT2026aies](https://www.wis-tns.org/object/2026aies) | transient_candidate | 10 | 21.09 | Robin's Egg Nebula (Planetary nebula) | 1.74650° | near-field match | 35 | hold |
| watch | [AT2026aijr](https://www.wis-tns.org/object/2026aijr) | transient_candidate | 11 | 20.08 | NGC7447 (Nebula) | 1.89133° | near-field match | 35 | hold |
| watch | [AT2026aila](https://www.wis-tns.org/object/2026aila) | transient_candidate | 10 | 19.91 | NGC2586 (Nebula) | 1.95903° | near-field match | 35 | hold |
| watch | [AT2026airk](https://www.wis-tns.org/object/2026airk) | transient_candidate | 8 | 20.12 | IC 71 (Star) | 1.00378° | near-field match | 35 | hold |
| watch | [AT2026aivl](https://www.wis-tns.org/object/2026aivl) | transient_candidate | 14 | 22.36 | IC1651 (Nebula) | 1.27407° | near-field match | 35 | hold |
| watch | [AT2026aivm](https://www.wis-tns.org/object/2026aivm) | transient_candidate | 16 | 21.89 | NGC728 (Nebula) | 1.63081° | near-field match | 35 | hold |
| watch | [AT2026aiwa](https://www.wis-tns.org/object/2026aiwa) | transient_candidate | 8 | 22.37 | IC 1623 (CiG) | 1.45584° | near-field match | 35 | hold |
| watch | [AT2026aiwg](https://www.wis-tns.org/object/2026aiwg) | transient_candidate | 10 | 20.6 | IC323 (Nebula) | 1.25852° | near-field match | 35 | hold |
| watch | [AT2026aiwh](https://www.wis-tns.org/object/2026aiwh) | transient_candidate | 6 | 19.85 | Lynds Bright Nebula 434 (LBN434) (HII) | 1.66663° | near-field match | 35 | hold |
| watch | [AT2026aiwm](https://www.wis-tns.org/object/2026aiwm) | transient_candidate | 9 | 20.09 | IC2940 (Nebula) | 1.28946° | near-field match | 35 | hold |
| watch | [AT2026aixk](https://www.wis-tns.org/object/2026aixk) | transient_candidate | 26 | 20.78 | NGC1037 (Nebula) | 1.03553° | near-field match | 35 | hold |
| watch | [AT2026aixt](https://www.wis-tns.org/object/2026aixt) | transient_candidate | 11 | 19.6 | IC640 (Nebula) | 1.79762° | near-field match | 35 | hold |
| watch | [AT2026aiym](https://www.wis-tns.org/object/2026aiym) | transient_candidate | 16 | 20.49 | Robin's Egg Nebula (Planetary nebula) | 1.48879° | near-field match | 35 | hold |
| watch | [AT2026aiyn](https://www.wis-tns.org/object/2026aiyn) | transient_candidate | 16 | 22.14 | NGC894 (Nebula) | 1.63394° | near-field match | 35 | hold |
| watch | [AT2026aiyq](https://www.wis-tns.org/object/2026aiyq) | transient_candidate | 9 | 20.08 | Melotte 53 (MEL53) (Globular cluster) | 1.83617° | near-field match | 35 | hold |
| watch | [AT2026aize](https://www.wis-tns.org/object/2026aize) | transient_candidate | 16 | 20.61 | IC5248 (Nebula) | 1.94668° | near-field match | 35 | hold |
| watch | [AT2026ajbc](https://www.wis-tns.org/object/2026ajbc) | transient_candidate | 17 | 21.19 | IC1707 (Nebula) | 1.73198° | near-field match | 35 | hold |
| watch | [AT2026ajcx](https://www.wis-tns.org/object/2026ajcx) | transient_candidate | 12 | 20.12 | IC337 (Nebula) | 1.86545° | near-field match | 35 | hold |
| watch | [AT2026ajde](https://www.wis-tns.org/object/2026ajde) | transient_candidate | 10 | 19.71 | NGC2875 (Nebula) | 1.32058° | near-field match | 35 | hold |
| watch | [AT2026ajdm](https://www.wis-tns.org/object/2026ajdm) | transient_candidate | 16 | 22.14 | NGC7668 (Nebula) | 1.32204° | near-field match | 35 | hold |
| watch | [AT2026ajeq](https://www.wis-tns.org/object/2026ajeq) | transient_candidate | 24 | 21.42 | NGC2284 (Nebula) | 1.44095° | near-field match | 35 | hold |
| watch | [AT2026ajet](https://www.wis-tns.org/object/2026ajet) | transient_candidate | 20 | 20.96 | Collinder 116 (CR116) (Open cluster) | 1.97492° | near-field match | 35 | hold |
| watch | [AT2026ajev](https://www.wis-tns.org/object/2026ajev) | transient_candidate | 14 | 21.31 | Collinder 116 (CR116) (Open cluster) | 1.73662° | near-field match | 35 | hold |
| watch | [AT2026ajfn](https://www.wis-tns.org/object/2026ajfn) | transient_candidate | 16 | 23.14 | NGC894 (Nebula) | 1.16150° | near-field match | 35 | hold |
| watch | [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) | transient_candidate | 9 | 20.91 | Intergalactic Wanderer (Globular cluster) | 1.09787° | near-field match | 35 | hold |
| watch | [AT2026ajkm](https://www.wis-tns.org/object/2026ajkm) | transient_candidate | 5 | 21.9 | Lynds Bright Nebula 418 (LBN418) (HII) | 1.03018° | near-field match | 35 | hold |
| watch | [AT2026ajkq](https://www.wis-tns.org/object/2026ajkq) | transient_candidate | 19 | 20.77 | IC1651 (Nebula) | 1.80188° | near-field match | 35 | hold |
| watch | [AT2026ajlq](https://www.wis-tns.org/object/2026ajlq) | transient_candidate | 5 | 22.86 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.81927° | near-field match | 35 | hold |
| watch | [AT2026ajmr](https://www.wis-tns.org/object/2026ajmr) | transient_candidate | 12 | 21.98 | NGC2464 (Nebula) | 1.15457° | near-field match | 35 | hold |
| watch | [AT2026ajmw](https://www.wis-tns.org/object/2026ajmw) | transient_candidate | 9 | 21.36 | NGC2464 (Nebula) | 1.42390° | near-field match | 35 | hold |
| watch | [AT2026ajnh](https://www.wis-tns.org/object/2026ajnh) | transient_candidate | 5 | 20.62 | Goblet of Fire nebula (Planetary nebula) | 1.85337° | near-field match | 35 | hold |
| watch | [AT2026ajnw](https://www.wis-tns.org/object/2026ajnw) | transient_candidate | 9 | 20.74 | Collinder 116 (CR116) (Open cluster) | 1.48474° | near-field match | 35 | hold |
| watch | [AT2026ajom](https://www.wis-tns.org/object/2026ajom) | transient_candidate | 4 | 20.3 | Lynds Bright Nebula 968 (LBN968) (HII) | 1.64919° | near-field match | 35 | hold |
| watch | [AT2026ajpe](https://www.wis-tns.org/object/2026ajpe) | transient_candidate | 10 | 23.13 | IC2069 (Nebula) | 1.57505° | near-field match | 35 | hold |
| watch | [AT2026ajpl](https://www.wis-tns.org/object/2026ajpl) | transient_candidate | 8 | 21.06 | IC5344 (Nebula) | 1.63978° | near-field match | 35 | hold |
| watch | [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) | transient_candidate | 1 | 19.58 | Lynds Bright Nebula 484 (LBN484) (HII) | 1.74355° | near-field match | 35 | hold |
| watch | [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) | transient_candidate | 3 | 19.74 | Lynds Bright Nebula 856 (LBN856) (HII) | 1.86922° | near-field match | 35 | hold |
| watch | [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) | transient_candidate | 9 | 23.61 | IC5248 (Nebula) | 1.48459° | near-field match | 35 | hold |
| watch | [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) | transient_candidate | 12 | 21.87 | NGC737 (Nebula) | 1.51249° | near-field match | 35 | hold |
| watch | [AT2026ajub](https://www.wis-tns.org/object/2026ajub) | transient_candidate | 10 | 21.61 | NGC2901 (Nebula) | 1.29090° | near-field match | 35 | hold |
| watch | [AT2026aigg](https://www.wis-tns.org/object/2026aigg) | transient_candidate | 13 | 20.26 | Lynds Bright Nebula 910 (LBN910) (HII) | 0.77477° | near-field match | 34 | hold |
| watch | [AT2026ajts](https://www.wis-tns.org/object/2026ajts) | transient_candidate | 12 | 20.91 | Lynds Bright Nebula 891 (LBN891) (HII) | 0.64768° | near-field match | 34 | hold |
| watch | [SN2026aeff](https://www.wis-tns.org/object/2026aeff) | SN II | 45 | 19.25 | NGC 2207 / IC 2163 (CiG) | 1.95543° | near-field match | 33 | hold |
| watch | [AT2026absv](https://www.wis-tns.org/object/2026absv) | transient_candidate | 62 | 19.48 | NGC 3561 (Galaxy) | 1.10562° | near-field match | 28 | hold |
| watch | [AT2026aeka](https://www.wis-tns.org/object/2026aeka) | transient_candidate | 58 | 20.21 | IC 1876 (Galaxy) | 0.09948° | near-field match | 28 | hold |
| watch | [AT2026aiem](https://www.wis-tns.org/object/2026aiem) | transient_candidate | 10 | 19.89 | Lynds Bright Nebula 556 (LBN556) (HII) | 1.55459° | near-field match | 27 | hold |
| watch | [AT2026aimd](https://www.wis-tns.org/object/2026aimd) | transient_candidate | 9 | 20.38 | Collinder 65 (CR65) (Open cluster) | 1.83171° | near-field match | 27 | hold |
| watch | [AT2026aivx](https://www.wis-tns.org/object/2026aivx) | transient_candidate | 8 | 22.48 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.67357° | near-field match | 27 | hold |
| watch | [AT2026aiwq](https://www.wis-tns.org/object/2026aiwq) | transient_candidate | 10 | 20.72 | van den Bergh 61 (VDB61) (Nebula) | 1.44782° | near-field match | 27 | hold |
| watch | [AT2026aixl](https://www.wis-tns.org/object/2026aixl) | transient_candidate | 12 | 20.49 | Lynds Bright Nebula 763 (LBN763) (HII) | 1.50403° | near-field match | 27 | hold |
| watch | [AT2026aixm](https://www.wis-tns.org/object/2026aixm) | transient_candidate | 12 | 20.73 | Lynds Bright Nebula 828 (LBN828) (HII) | 1.46269° | near-field match | 27 | hold |
| watch | [AT2026aizy](https://www.wis-tns.org/object/2026aizy) | transient_candidate | 10 | 22.68 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.97258° | near-field match | 27 | hold |
| watch | [AT2026ajkk](https://www.wis-tns.org/object/2026ajkk) | transient_candidate | 8 | 21.78 | Lynds Bright Nebula 688 (LBN688) (HII) | 1.01865° | near-field match | 27 | hold |
| watch | [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) | SN Ia | 41 | 19.82 | NGC7158 (Nebula) | 0.70237° | near-field match | 20 | hold |
| watch | [AT2026abyt](https://www.wis-tns.org/object/2026abyt) | transient_candidate | 59 | 19.14 | IC2170 (Nebula) | 1.73601° | near-field match | 18 | hold |
| watch | [AT2026adsv](https://www.wis-tns.org/object/2026adsv) | transient_candidate | 45 | 20.83 | IC1386 (Galaxy) | 0.88938° | near-field match | 15 | hold |
| watch | [AT2026ajax](https://www.wis-tns.org/object/2026ajax) | transient_candidate | 34 | 21.28 | IC509 (Galaxy) | 0.40100° | near-field match | 15 | hold |
| watch | [AT2026ajku](https://www.wis-tns.org/object/2026ajku) | transient_candidate | 68 | 22.1 | NGC488 (Galaxy) | 0.71371° | near-field match | 15 | hold |
| watch | [AT2026ajky](https://www.wis-tns.org/object/2026ajky) | transient_candidate | 37 | 22.61 | IC 197 (Galaxy) | 0.99165° | near-field match | 15 | hold |
| watch | [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) | transient_candidate | 63 | 20.79 | NGC925 (Galaxy) | 0.76155° | near-field match | 15 | hold |
| watch | [SN2026afgl](https://www.wis-tns.org/object/2026afgl) | SN IIn | 35 | 19.63 | Beehive cluster (Open cluster) | 1.83228° | near-field match | 13 | hold |
| watch | [AT2026aawo](https://www.wis-tns.org/object/2026aawo) | transient_candidate | 73 | 20.08 | IC 1341 (Galaxy) | 1.50242° | near-field match | 8 | hold |
| watch | [AT2026adsx](https://www.wis-tns.org/object/2026adsx) | transient_candidate | 45 | 20.67 | IC1386 (Galaxy) | 1.56536° | near-field match | 8 | hold |
| watch | [AT2026agac](https://www.wis-tns.org/object/2026agac) | transient_candidate | 36 | 20.92 | IC 1417 (Galaxy) | 1.74979° | near-field match | 8 | hold |
| watch | [AT2026aiyu](https://www.wis-tns.org/object/2026aiyu) | transient_candidate | 72 | 21.98 | NGC1425 (Galaxy) | 1.69335° | near-field match | 8 | hold |
| watch | [AT2026aiyw](https://www.wis-tns.org/object/2026aiyw) | transient_candidate | 78 | 20.41 | NGC1340 (Galaxy) | 1.91424° | near-field match | 8 | hold |
| watch | [AT2026ajkn](https://www.wis-tns.org/object/2026ajkn) | transient_candidate | 33 | 22.34 | IC 1639 (Galaxy) | 1.07935° | near-field match | 8 | hold |
| watch | [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) | transient_candidate | 63 | 22.85 | IC 1507 (Galaxy) | 1.97219° | near-field match | 8 | hold |
| watch | [SN2026acjc](https://www.wis-tns.org/object/2026acjc) | SN Ib | 57 | 19.85 | Lynds Dark Nebula 1648 (LDN1648) (Dark nebula) | 1.97714° | near-field match | 5 | hold |
| watch | [AT2026aflb](https://www.wis-tns.org/object/2026aflb) | transient_candidate | 37 | 22.4 | NGC7668 (Nebula) | 0.94348° | near-field match | 5 | hold |
| watch | [AT2026agwt](https://www.wis-tns.org/object/2026agwt) | transient_candidate | 34 | 20.95 | Intergalactic Wanderer (Globular cluster) | 1.72330° | near-field match | 0 | hold |
| watch | [AT2026aixp](https://www.wis-tns.org/object/2026aixp) | transient_candidate | 32 | 20.76 | Collinder 204 (CR204) (Open cluster) | 1.53361° | near-field match | 0 | hold |
| watch | [AT2026ajau](https://www.wis-tns.org/object/2026ajau) | transient_candidate | 34 | 21.1 | Collinder 116 (CR116) (Open cluster) | 1.33313° | near-field match | 0 | hold |
| watch | [AT2026ajaw](https://www.wis-tns.org/object/2026ajaw) | transient_candidate | 34 | 20.69 | Beehive cluster (Open cluster) | 1.31677° | near-field match | 0 | hold |
| watch | [AT2026ajmg](https://www.wis-tns.org/object/2026ajmg) | transient_candidate | 42 | 20.17 | NGC2464 (Nebula) | 1.82991° | near-field match | 0 | hold |

## Candidate dossiers

### 1. [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) near NGC4216

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4216 as this object's host. The 0.39321° (23.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.006997 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T19:55:53Z · 13 days · 16.1 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4401....1I](https://ui.adsabs.harvard.edu/abs/2026TNSTR4401....1I/abstract) |
| Classification references | [2026TNSCR4483....1B](https://ui.adsabs.harvard.edu/abs/2026TNSCR4483....1B/abstract) |
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
| Separation | 0.39321° · 23.59′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤16.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahvi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.4601771%2013.4239557&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 2. [AT2026aina](https://www.wis-tns.org/object/2026aina) near NGC2052

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2052 as this object's host. The 0.15398° (9.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | Nova |
| Redshift | 0.0011 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T03:50:24Z · 9 days · 13.8 g |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤16.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aina) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=84.47673%20-69.915&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) near IC 2405

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 97/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2405 as this object's host. The 0.45056° (27.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN |
| Redshift | 0.0257 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:36Z · 12 days · 18.49 g |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=132.0534498%2036.7792244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [SN2026aicq](https://www.wis-tns.org/object/2026aicq) near IC 369

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 97/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 369 as this object's host. The 0.91868° (55.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.02 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T13:00:09Z · 11 days · 18.48 L |
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
| Subject | **IC 369** · `IC 369` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Eri |
| Catalog magnitude / angular size | — · 0.76′ × 0.76′ |
| Distance | — |
| Separation | 0.91868° · 55.12′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 369 has the different designation IC 1101 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aicq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.2543158%20-12.6274032&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [SN2026ainb](https://www.wis-tns.org/object/2026ainb) near IC 450

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 450 as this object's host. The 1.07438° (64.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.017792 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T02:25:45Z · 11 days · 18.12 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4490....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4490....1T/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=99.0704236%2074.3446308&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 6. [AT2026aizp](https://www.wis-tns.org/object/2026aizp) near Atoms For Peace Galaxy

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Atoms For Peace Galaxy as this object's host. The 0.49861° (29.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T08:20:41Z · 6 days · 18.1 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 7. [AT2026ajcp](https://www.wis-tns.org/object/2026ajcp) near NGC 4517

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4517 as this object's host. The 0.80621° (48.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:16Z · 5 days · 17.76 r |
| Latest public photometry | Not available in the staged feed |
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

### 8. [AT2026ajpr](https://www.wis-tns.org/object/2026ajpr) near NGC3945

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3945 as this object's host. The 0.86986° (52.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:18:43Z · 5 days · 18.03 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3945** · `NGC3945` |
| Catalog display name | NGC3945 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.8 · 5.55′ × 3.29′ |
| Distance | — |
| Separation | 0.86986° · 52.19′ |
| Catalog description | NGC 3945 is a barred lenticular galaxy in the constellation Ursa Major. It was discovered by German-British astronomer William Herschel on March 19, 1790. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=179.6848206%2060.1353844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 9. [AT2026ajrb](https://www.wis-tns.org/object/2026ajrb) near IC5270

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5270 as this object's host. The 1.73389° (104.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T06:17:03Z · 2 days · 18.48 orange |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.73389° · 104.03′ |
| Catalog description | The Telescopium−Grus Cloud is a galaxy filament in the constellations of Pavo, Indus, and Telescopium. It was first defined by astronomer Brent Tully in his book The Nearby Galaxies Atlas and its companion book The Nearby Galaxies Catalog. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.6133678%20-35.9343111&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 10. [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) near IC656

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC656 as this object's host. The 0.87225° (52.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:02:11Z · 7 days · 18.38 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.87225° · 52.34′ |
| Catalog description | very small in angular size, cluster, neb? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.5999869%2017.2209044&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 11. [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) near IC765

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC765 as this object's host. The 0.75222° (45.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:56:47Z · 1 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.75222° · 45.13′ |
| Catalog description | very faint, suspected 6'north of 4152 |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.4079733%2016.1252067&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 12. [SN2026aied](https://www.wis-tns.org/object/2026aied) near Lynds Bright Nebula 465 (LBN465)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 79/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 465 (LBN465) as this object's host. The 0.57960° (34.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.018596 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T03:44:06Z · 12 days · 18.33 g |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aied) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=289.2104416%2070.5122062&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 13. [AT2026aiuw](https://www.wis-tns.org/object/2026aiuw) near Lynds Dark Nebula 637 (LDN637)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 637 (LDN637) as this object's host. The 1.17864° (70.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:51:28Z · 7 days · 14.89 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 14. [AT2026aiux](https://www.wis-tns.org/object/2026aiux) near Lynds Dark Nebula 705 (LDN705)

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 705 (LDN705) as this object's host. The 0.57543° (34.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:57:16Z · 7 days · 17.29 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 15. [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) near NGC2276

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2276 as this object's host. The 0.19202° (11.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T02:46:53Z · 2 days · 19.32 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2276** · `NGC2276` |
| Catalog display name | NGC2276 |
| Type / constellation | Galaxy · Cepheus |
| Catalog magnitude / angular size | 11.4 · 2.23′ × 1.73′ |
| Distance | — |
| Separation | 0.19202° · 11.52′ |
| Catalog description | NGC 2276 is an intermediate spiral galaxy in the constellation Cepheus. The galaxy lies 120 million light-years away from Earth. NGC 2276 has an asymmetrical appearance, most likely caused by gravitational interactions with its neighbor, elliptical galaxy NGC 2300. NGC 2276 is traveling with an orbital velocity of about 968 km/s relative to the NGC 2300 group of galaxies. Trailing NGC 2276 is a long tail of interstellar medium about 300,000 light-years long, formed by ram pressure stripping. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.27614%2085.597616&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 16. [SN2026agwk](https://www.wis-tns.org/object/2026agwk) near IC391

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 87/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC391 as this object's host. The 0.40294° (24.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia-91T-like |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T07:48:13Z · 20 days · 19.32 g |
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

### 17. [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) near IC 3

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
| Discovery | 2026-11-01T10:53:54Z · 14 days · 18.71 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4390....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4390....1O/abstract) |
| Classification references | [2026TNSCR4440....1W](https://ui.adsabs.harvard.edu/abs/2026TNSCR4440....1W/abstract) |
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

[TNS object](https://www.wis-tns.org/object/2026ahsn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=3.1673709%20-0.0368758&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 18. [SN2026ahze](https://www.wis-tns.org/object/2026ahze) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.92287° (115.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.092 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:33:40Z · 12 days · 18.71 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4419....1W](https://ui.adsabs.harvard.edu/abs/2026TNSTR4419....1W/abstract) |
| Classification references | [2026TNSCR4518....1F](https://ui.adsabs.harvard.edu/abs/2026TNSCR4518....1F/abstract) |
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
| Separation | 1.92287° · 115.37′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahze) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.1393832%20-1.8788253&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 19. [AT2026aiuv](https://www.wis-tns.org/object/2026aiuv) near IC 897

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
| Discovery | 2026-11-08T13:04:34Z · 7 days · 18.64 r |
| Latest public photometry | Not available in the staged feed |
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

### 20. [AT2026ajcv](https://www.wis-tns.org/object/2026ajcv) near IC 4297

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
| Discovery | 2026-11-09T13:07:08Z · 6 days · 19.32 r |
| Latest public photometry | Not available in the staged feed |
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

### 21. [AT2026ajdx](https://www.wis-tns.org/object/2026ajdx) near IC2160

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2160 as this object's host. The 0.65192° (39.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T06:16:49Z · 7 days · 19.5 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2160** · `IC2160` |
| Catalog display name | IC2160 |
| Type / constellation | Galaxy · Mensa |
| Catalog magnitude / angular size | 13.1 · 1.8′ × 0.89′ |
| Distance | — |
| Separation | 0.65192° · 39.12′ |
| Catalog description | very faint, very small in angular size, stellar, pointlike nucleus, or to a nucleus |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=86.17722%20-77.1682775&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 22. [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.59331° (35.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:02Z · 2 days · 19.37 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4631....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4631....1T/abstract) |
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
| Separation | 0.59331° · 35.60′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=125.788333%2057.604842&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 23. [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) near NGC2768

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2768 as this object's host. The 0.41880° (25.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T04:23:39Z · 2 days · 19.35 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC2768** · `NGC2768` |
| Catalog display name | NGC2768 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 9.9 · 5.64′ × 2.24′ |
| Distance | — |
| Separation | 0.41880° · 25.13′ |
| Catalog description | NGC 2768 is a lenticular galaxy located in the constellation of Ursa Major. It is at a distance of 65 million light years from Earth. NGC 2768 is an example of a Seyfert galaxy, an object with a supermassive black hole at its centre. A dusty structure is encircling the centre of the galaxy, forming a knotted ring around the galaxy's brightly glowing middle. This ring lies perpendicular to the plane of NGC 2768 itself, stretching up and out of the galaxy. The dust in NGC 2768 forms an intricate network of knots and filaments. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.5544312%2060.303245&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 24. [AT2026aive](https://www.wis-tns.org/object/2026aive) near NGC2835

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2835 as this object's host. The 1.04795° (62.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:06:23Z · 7 days · 18.74 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 25. [AT2026aivf](https://www.wis-tns.org/object/2026aivf) near NGC2835

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2835 as this object's host. The 1.02455° (61.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:06:23Z · 7 days · 19.03 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 26. [AT2026ajbn](https://www.wis-tns.org/object/2026ajbn) near NGC3189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3189 as this object's host. The 1.65719° (99.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:53:05Z · 5 days · 19.45 r |
| Latest public photometry | Not available in the staged feed |
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

### 27. [AT2026ajdq](https://www.wis-tns.org/object/2026ajdq) near IC 1600

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1600 as this object's host. The 1.96019° (117.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T06:02:28Z · 5 days · 19.19 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.96019° · 117.61′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1600 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=14.7520682%20-21.7878802&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 28. [AT2026ajig](https://www.wis-tns.org/object/2026ajig) near IC 38

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 38 as this object's host. The 0.00569° (0.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T10:08:29Z · 3 days · 19.78 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4597....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4597....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 38** · `IC 38` |
| Catalog display name | IC 10 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.77′ × 0.57′ |
| Distance | 2.5 ly |
| Separation | 0.00569° · 0.34′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 38 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajig) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.6670318%20-15.4178427&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) near NGC1169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1169 as this object's host. The 1.01800° (61.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T23:39:27Z · 3 days · 19.46 L |
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
| Separation | 1.01800° · 61.08′ |
| Catalog description | NGC 1169 is an intermediate barred spiral galaxy in the constellation of Perseus. NGC 1169 has a reddish center, indicating the region is dominated by older stars. In contrast, the outer ring contains larger blue-white stars, a sign of recent star formation. The entire galaxy is rotating at approximately 265 km/s. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=45.7965046%2045.3705223&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 30. [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.51592° (90.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:19:10Z · 3 days · 18.82 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.51592° · 90.96′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.78624%2036.2092171&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 31. [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) near IC486

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC486 as this object's host. The 1.22917° (73.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T12:37:47Z · 3 days · 19 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4613....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4613....1T/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC486** · `IC486` |
| Catalog display name | IC486 |
| Type / constellation | Galaxy · Gemini |
| Catalog magnitude / angular size | 13.2 · 0.87′ × 0.66′ |
| Distance | 119,000 kpc |
| Separation | 1.22917° · 73.75′ |
| Catalog description | faint, small in angular size, diffused, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.181083%2027.543858&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 32. [AT2026ajoo](https://www.wis-tns.org/object/2026ajoo) near IC2058

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2058 as this object's host. The 0.00834° (0.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 22.76 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2058** · `IC2058` |
| Catalog display name | IC2058 |
| Type / constellation | Galaxy · Dorado |
| Catalog magnitude / angular size | 13.8 · 3.4′ × 0.48′ |
| Distance | 19,900 kpc |
| Separation | 0.00834° · 0.50′ |
| Catalog description | considerably bright, considerably large, extremely, excessively extended 10deg |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajoo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.482181%20-55.925588&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 33. [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) near IC1733

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1733 as this object's host. The 1.11166° (66.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T06:40:30Z · 1 days · 19.45 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.11166° · 66.70′ |
| Catalog description | faint, very small in angular size, preceding (westward) / pretty (adv., before F. B. L, S) round, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.3115111%2034.1516816&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) near IC5261

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5261 as this object's host. The 1.21834° (73.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T20:50:16Z · 2 days · 19.27 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC5261** · `IC5261` |
| Catalog display name | IC5261 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 13.9 · 1.44′ × 1.28′ |
| Distance | 54,100 kpc |
| Separation | 1.21834° · 73.10′ |
| Catalog description | most extremely faint, preceding (westward) / pretty (adv., before F. B. L, S) large, round, very difficult, a star of 9th magnitude preceding (westward) / pretty (adv., before F. B. L, S) 22s |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.6960475%20-19.4936975&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 35. [AT2026ajva](https://www.wis-tns.org/object/2026ajva) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19660° (11.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 21.81 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.19660° · 11.80′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajva) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.2374258%20-12.7213112&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 36. [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19359° (11.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.15 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.19359° · 11.62′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.9945911%20-12.9538304&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 37. [AT2026ahpf](https://www.wis-tns.org/object/2026ahpf) near IC 2017

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
| Discovery | 2026-10-30T14:43:45Z · 16 days · 19.31 L |
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

### 38. [AT2026aiyr](https://www.wis-tns.org/object/2026aiyr) near NGC2566

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2566 as this object's host. The 0.87981° (52.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T17:37:26Z · 8 days · 19.34 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=123.79501%20-25.85603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 39. [AT2026ajmb](https://www.wis-tns.org/object/2026ajmb) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 0.67085° (40.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:38:52Z · 4 days · 19.13 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.67085° · 40.25′ |
| Catalog description | IC 1623 is a galaxy merger in the constellation Cetus. The galaxy lies about 250 million light years away from Earth, which means, given its apparent dimensions, that IC 1623 is approximately 115,000 light years across. It was discovered by Lewis Swift on November 19, 1897. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.382833%20-0.262964&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [SN2026agyk](https://www.wis-tns.org/object/2026agyk) near Barnard 152 (B152)

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
| Discovery | 2026-10-26T03:50:53Z · 20 days · 18.8 r |
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

### 41. [SN2026aitx](https://www.wis-tns.org/object/2026aitx) near IC 2083

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
| Discovery | 2026-11-08T04:24:30Z · 7 days · 19.57 cyan |
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

### 42. [AT2026aivh](https://www.wis-tns.org/object/2026aivh) near Lynds Bright Nebula 749 (LBN749)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 67/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 749 (LBN749) as this object's host. The 0.23181° (13.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:09:31Z · 12 days · 18.75 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°.

[TNS object](https://www.wis-tns.org/object/2026aivh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.4915023%2032.0738749&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 43. [AT2026agye](https://www.wis-tns.org/object/2026agye) near IC 5124

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5124 as this object's host. The 1.51433° (90.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T10:07:35Z · 19 days · 19.16 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4299....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4299....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 5124** · `IC 5124` |
| Catalog display name | NGC 5135 |
| Type / constellation | Galaxy · Cap |
| Catalog magnitude / angular size | — · 0.51′ × 0.23′ |
| Distance | 194 ly |
| Separation | 1.51433° · 90.86′ |
| Catalog description | NGC 5135 is a barred spiral galaxy located in the constellation Hydra. It is located at a distance of about 200 million light years from Earth. It was discovered by John Herschel on May 8, 1834. It is a Seyfert galaxy. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5124 has the different designation NGC 5135 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agye) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=323.3702254%20-22.7163771&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 44. [AT2026ahcr](https://www.wis-tns.org/object/2026ahcr) near NGC7626

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7626 as this object's host. The 1.62993° (97.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-28T21:16:18Z · 18 days · 19.43 L |
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

### 45. [AT2026aizi](https://www.wis-tns.org/object/2026aizi) near IC 4660

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4660 as this object's host. The 1.33546° (80.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T02:25:08Z · 10 days · 18.92 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aizi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=257.6433885%2074.7170731&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 46. [AT2026ajko](https://www.wis-tns.org/object/2026ajko) near NGC864

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC864 as this object's host. The 0.13264° (7.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:10:04Z · 14 days · 22.23 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.13264° · 7.96′ |
| Catalog description | NGC 864 is a star-forming intermediate spiral galaxy located in the Cetus constellation. It's also classified as an isolated galaxy on the AMIGA catalogue as CIG 96. Its discovery and first description was realized by William Herschel in October 25th, 1785 and the findings made public through his Catalogue of Nebulae and Clusters of Stars, published in 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajko) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.897083%205.874514&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 47. [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) near Lynds Bright Nebula 1043 (LBN1043)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1043 (LBN1043) as this object's host. The 1.49482° (89.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T18:56:34Z · 3 days · 18.5 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 1043 (LBN1043)** · `LBN1043` |
| Catalog display name | Lynds Bright Nebula 1043 (LBN1043) |
| Type / constellation | HII · Canis Major |
| Catalog magnitude / angular size | — · 20′ × 10′ |
| Distance | — |
| Separation | 1.49482° · 89.69′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajsc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=105.725333%20-18.029806&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 48. [AT2026ajcg](https://www.wis-tns.org/object/2026ajcg) near Collinder 394 (CR394)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 64/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 394 (CR394) as this object's host. The 0.65272° (39.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:00:30Z · 8 days · 16.87 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajcg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=282.8768301%20-20.3408695&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 49. [AT2026aixw](https://www.wis-tns.org/object/2026aixw) near IC877

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC877 as this object's host. The 1.87815° (112.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T13:09:19Z · 6 days · 18.85 r |
| Latest public photometry | Not available in the staged feed |
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

### 50. [AT2026aiyx](https://www.wis-tns.org/object/2026aiyx) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.73252° (103.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:58:05Z · 6 days · 19.09 L |
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

### 51. [AT2026ajcc](https://www.wis-tns.org/object/2026ajcc) near IC435

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC435 as this object's host. The 1.32248° (79.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:47:15Z · 6 days · 18.82 i |
| Latest public photometry | Not available in the staged feed |
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

### 52. [AT2026ajkf](https://www.wis-tns.org/object/2026ajkf) near Collinder 409 (CR409)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 409 (CR409) as this object's host. The 1.82025° (109.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:55:20Z · 3 days · 19.07 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 409 (CR409)** · `CR409` |
| Catalog display name | Collinder 409 (CR409) |
| Type / constellation | Globular cluster · Sagitta |
| Catalog magnitude / angular size | 8.4 · 6.9′ × 6.9′ |
| Distance | 4 kpc |
| Separation | 1.82025° · 109.21′ |
| Catalog description | Messier 71 is a globular cluster in the small northern constellation Sagitta. It was discovered by Philippe Loys de Chéseaux in 1745 and included by Charles Messier in his catalog of non-comet-like objects in 1780. It was also noted by Koehler at Dresden around 1775. Messier 71 is also known as NGC 6839, though this identification is very uncertain. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=300.0597633%2019.7857967&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 53. [AT2026ajpu](https://www.wis-tns.org/object/2026ajpu) near Blue Snowball

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Blue Snowball as this object's host. The 1.82980° (109.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T08:10:22Z · 3 days · 19.22 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Blue Snowball** · `NGC 7662` |
| Catalog display name | Blue Snowball |
| Type / constellation | Planetary nebula · And |
| Catalog magnitude / angular size | — · 0.28′ × 0.23′ |
| Distance | 5,600 ly |
| Separation | 1.82980° · 109.79′ |
| Catalog description | NGC 7662 is a planetary nebula located in the northern constellation Andromeda. It is known as the Blue Snowball Nebula, Snowball Nebula, and Caldwell 22. This nebula was discovered October 6, 1784 by the German-born English astronomer William Herschel. In the New General Catalogue it is described as a "magnificent planetary or annular nebula, very bright, pretty small in angular size, round, blue, variable nucleus". The object has an apparent visual magnitude of 8.3 and spans an angular size of 32″ × 28″. Parallax measurements give a distance estimate of 5,730 ± 340 ly (1,757 ± 103 pc). |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=353.9556364%2042.4141143&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 54. [AT2026ajru](https://www.wis-tns.org/object/2026ajru) near Collinder 176 (CR176)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 176 (CR176) as this object's host. The 1.06889° (64.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T02:16:35Z · 1 days · 18.7 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 176 (CR176)** · `CR176` |
| Catalog display name | Collinder 176 (CR176) |
| Type / constellation | Open cluster · Puppis |
| Catalog magnitude / angular size | 6.5 · 12.3′ × 12.3′ |
| Distance | 1.363 kpc |
| Separation | 1.06889° · 64.13′ |
| Catalog description | NGC 2539 is an open cluster in the constellation Puppis, located at the north edge of the constellation. It was discovered by William Herschel on January 31, 1785. It is a moderately rich cluster and with little central concentration, with Trumpler class II1m. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajru) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=122.2152986%20-13.8022929&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 55. [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 0.13206° (7.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:31:35Z · 0 days · 22.79 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.13206° · 7.92′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.1748122%20-16.0266701&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 56. [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.00471° (0.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 0 days · 21.79 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.00471° · 0.28′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.3940372%20-5.5061496&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 57. [SN2026agua](https://www.wis-tns.org/object/2026agua) near Lynds Dark Nebula 1571 (LDN1571)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1571 (LDN1571) as this object's host. The 1.07129° (64.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.05 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T11:03:46Z · 22 days · 19.33 g |
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

### 58. [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) near van den Bergh 12 (VDB12)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 12 (VDB12) as this object's host. The 0.51247° (30.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T10:32:37Z · 1 days · 19.17 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **van den Bergh 12 (VDB12)** · `VDB12` |
| Catalog display name | van den Bergh 12 (VDB12) |
| Type / constellation | Nebula · Perseus |
| Catalog magnitude / angular size | 7 · — |
| Distance | — |
| Separation | 0.51247° · 30.75′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajxc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.7275167%2031.4626067&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 59. [SN2026ahhp](https://www.wis-tns.org/object/2026ahhp) near NGC1398

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1398 as this object's host. The 1.54372° (92.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ic |
| Redshift | 0.11 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:15:38Z · 16 days · 21.98 i |
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
| Subject | **NGC1398** · `NGC1398` |
| Catalog display name | NGC1398 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 9.6 · 6.95′ × 4.91′ |
| Distance | — |
| Separation | 1.54372° · 92.62′ |
| Catalog description | NGC 1398 is an isolated barred spiral galaxy exhibiting a double ring structure. It is located 65 million light years from the Earth, in the constellation of Fornax. The galaxy, with a diameter of approximately 292,000 light years, is bigger than the Milky Way. Over 100 billion stars are in the galaxy. The discovery credit for NGC 1398 is often given to Friedrich Winnecke of Karlsruhe, Germany, who observed it on 17 December 1868, while he was searching for comets. German astronomer Wilhelm Tempel had first observed it on 9 October 1861, but he did not publish his observation until 1882. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahhp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.2735782%20-27.8302977&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 60. [AT2026aisx](https://www.wis-tns.org/object/2026aisx) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.65992° (39.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T07:24:51Z · 7 days · 21.65 g |
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

### 61. [AT2026aiyg](https://www.wis-tns.org/object/2026aiyg) near IC2135

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2135 as this object's host. The 0.98727° (59.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T15:06:42Z · 6 days · 20.21 L |
| Latest public photometry | Not available in the staged feed |
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

### 62. [AT2026ajbh](https://www.wis-tns.org/object/2026ajbh) near IC302

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC302 as this object's host. The 0.86924° (52.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T14:39:14Z · 6 days · 19.94 L |
| Latest public photometry | Not available in the staged feed |
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

### 63. [AT2026ajen](https://www.wis-tns.org/object/2026ajen) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 0.27076° (16.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:10:33Z · 7 days · 23.05 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1639** · `IC 1639` |
| Catalog display name | NGC5042 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.76′ × 0.7′ |
| Distance | — |
| Separation | 0.27076° · 16.25′ |
| Catalog description | NGC 5042 is an intermediate spiral galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background for is 1,697±22 km/s, which corresponds to a Hubble distance of 81.6 ± 5.8 Mly (25.03 ± 1.78 Mpc). However, 15 non redshift measurements give a much closer distance of 47.88 ± 2.37 Mly (14.680 ± 0.726 Mpc). It was discovered by British astronomer John Herschel on 25 March 1836. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1639 has the different designation NGC5042 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajen) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=17.896792%20-0.930986&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 64. [AT2026ajfg](https://www.wis-tns.org/object/2026ajfg) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 0.35306° (21.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 4 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.35306° · 21.18′ |
| Catalog description | NGC 1340 is an elliptical galaxy located in the constellation Fornax. Its speed relative to the cosmic microwave background is 1,126 ± 17 km/s, which corresponds to a Hubble Distance of 16.6 ± 1.2 Mpc. It was discovered by the German-British astronomer William Herschel in 1790, but it was added to the New General Catalog under the designation NGC 1344 later. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.277819%20-30.758965&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 65. [AT2026ajfh](https://www.wis-tns.org/object/2026ajfh) near NGC1433

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1433 as this object's host. The 0.67734° (40.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:46:44Z · 5 days · 19.55 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4581....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4581....1R/abstract) |
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
| Separation | 0.67734° · 40.64′ |
| Catalog description | NGC 1433 is a barred spiral galaxy with a double ring structure located in the constellation of Horologium. It was discovered by James Dunlop on 28 September 1826, and lies a distance of 46 million light-years from Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.0808614%20-46.6709071&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 66. [AT2026ajfj](https://www.wis-tns.org/object/2026ajfj) near IC 2039

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2039 as this object's host. The 0.31321° (18.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 4 days · 20.45 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.31321° · 18.79′ |
| Catalog description | NGC 1533 is a barred lenticular galaxy with faint spiral structure in the constellation Dorado. The seventh-brightest member of the Dorado Group and 1° off the group's center, it is surrounded by a vast arc or ring of H I which is connected to IC 2038 and IC 2039. The ring orbits around 32 kpc from the center.[b] As is typical of lenticular galaxies, star formation is weak in NGC 1533. Using both the surface brightness fluctuation (SBF) and globular cluster luminosity function (GCLF) methods, its distance was estimated in 2007 to be 19.4 ± 1.1 Mpc and 18.6 ± 2.0 Mpc respectively. Averaging these together gives a distance of around 19 million parsecs or 62 million light-years from earth.[a] In 1970, a supernova was detected in NGC 1533. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2039 has the different designation NGC 1533 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.349206%20-55.702521&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 67. [AT2026ajfk](https://www.wis-tns.org/object/2026ajfk) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 0.44583° (26.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 4 days · 21.23 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1993** · `IC1993` |
| Catalog display name | IC1993 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 11.9 · 2.81′ × 2.48′ |
| Distance | — |
| Separation | 0.44583° · 26.75′ |
| Catalog description | IC 1993 is an unbarred spiral galaxy in the constellation Fornax. It was discovered by Lewis Swift on November 19, 1897. At a distance of about 50 million light-years, and redshift of 1057 km/s, it is one of the closest to us of the 200 galaxies in the Fornax Cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.298366%20-33.927552&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 68. [AT2026ajfl](https://www.wis-tns.org/object/2026ajfl) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.58240° (34.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 4 days · 22.63 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.58240° · 34.94′ |
| Catalog description | NGC 1543 is a barred lenticular galaxy in the constellation Reticulum. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 1543 is approximately 100,000 light years across. It was discovered by James Dunlop on November 5, 1826. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.262228%20-57.813157&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 69. [AT2026ajiz](https://www.wis-tns.org/object/2026ajiz) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.62701° (37.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:40:32Z · 5 days · 19.64 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4599....1K](https://ui.adsabs.harvard.edu/abs/2026TNSTR4599....1K/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2207 / IC 2163** · `IC 2060` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Ret |
| Catalog magnitude / angular size | — · 1.25′ × 0.82′ |
| Distance | 81 ly |
| Separation | 0.62701° · 37.62′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajiz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=65.4956267%20-56.344525&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 70. [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) near NGC779

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC779 as this object's host. The 0.37574° (22.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:18:57Z · 5 days · 20.16 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC779** · `NGC779` |
| Catalog display name | NGC779 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.2 · 1.35′ × 0.58′ |
| Distance | — |
| Separation | 0.37574° · 22.54′ |
| Catalog description | NGC 779 is a spiral galaxy seen edge-on, located in the constellation Cetus. It is located at a distance of circa 60 million light years from Earth, which, given its apparent dimensions, means that NGC 779 is about 70,000 light years across. It was discovered by William Herschel on September 10, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.591866%20-6.140491&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 71. [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.74036° (44.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 3 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.74036° · 44.42′ |
| Catalog description | NGC 3239 is an irregular galaxy in the constellation of Leo. The galaxy was discovered in 1784 by William Herschel and is part of the New General Catalogue. It harbors a large and relatively bright H II region in its southeastern section that was first cataloged by Russian astronomer Boris Vorontsov-Velyaminov as VV95b. It's believed that NGC 3239 is the result of a galactic merger with a low-mass galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.074315%2017.880864&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 72. [AT2026ajkp](https://www.wis-tns.org/object/2026ajkp) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.53744° (32.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:46:33Z · 7 days · 22.96 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.53744° · 32.25′ |
| Catalog description | NGC 936 is a barred lenticular galaxy in the constellation Cetus. It is at a distance of about 60 million light-years away from Earth. Its nucleus and prominent bar have high surface brightness. Because of the shape of the prominent bar, the nucleus and the ring of stars at the end of the barrel, the galaxy has been compared with the shape of a TIE fighter, from the Star Wars universe, and thus NGC 936 has been named Darth Vader's Galaxy or Darth Vader's Starfighter. By measuring the radial velocity of the disc, Kormendy found in 1986 that the disc is stable, which is the reason why it is so smooth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.365667%20-0.880722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 73. [AT2026ajks](https://www.wis-tns.org/object/2026ajks) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 0.92554° (55.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:37:55Z · 5 days · 22.25 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.92554° · 55.53′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajks) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.475083%204.020544&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 74. [AT2026ajkt](https://www.wis-tns.org/object/2026ajkt) near IC 234

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 234 as this object's host. The 0.57827° (34.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:46:33Z · 7 days · 23.15 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 234** · `IC 234` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.69′ × 0.35′ |
| Distance | — |
| Separation | 0.57827° · 34.70′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 234 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.710208%20-0.683942&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 75. [AT2026ajlj](https://www.wis-tns.org/object/2026ajlj) near IC 1749

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1749 as this object's host. The 0.61175° (36.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:53:45Z · 7 days · 22.54 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.61175° · 36.70′ |
| Catalog description | NGC 1701, also known as the Trekkie Galaxy, is a large unbarred spiral galaxy located in the constellation Caelum. Its speed relative to the cosmic microwave background is 5,836 ± 24 km/s, which corresponds to a Hubble distance of 86.1 ± 6.0 Mpc. It was discovered by the British astronomer John Herschel in 1834. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1749 has the different designation NGC 1701 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.506542%206.338597&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026ajlk](https://www.wis-tns.org/object/2026ajlk) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.75962° (45.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:34:04Z · 7 days · 22.61 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.75962° · 45.58′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.523208%205.221917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 77. [AT2026ajlz](https://www.wis-tns.org/object/2026ajlz) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.87422° (52.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:30:14Z · 4 days · 22.45 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.87422° · 52.45′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.244958%205.276839&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 78. [AT2026ajog](https://www.wis-tns.org/object/2026ajog) near IC 21

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 21 as this object's host. The 0.76970° (46.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:56:32Z · 7 days · 20.22 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.76970° · 46.18′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 21 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajog) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=6.540778%20-0.324788&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 79. [AT2026ajoh](https://www.wis-tns.org/object/2026ajoh) near IC2006

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2006 as this object's host. The 0.63770° (38.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 22.19 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2006** · `IC2006` |
| Catalog display name | IC2006 |
| Type / constellation | Galaxy · Eridanus |
| Catalog magnitude / angular size | 11.3 · 2.36′ × 1.98′ |
| Distance | 19,900 kpc |
| Separation | 0.63770° · 38.26′ |
| Catalog description | IC 2006 is an elliptical galaxy in the constellation Eridanus. The galaxy was discovered on 3 October 1897 by the American astronomer Lewis A. Swift. It is estimated to be around 60 to 70 million light years away, in the Fornax Cluster. The galaxy is one of the smaller in the Fornax cluster, with a diameter of only 35 000 light-years. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajoh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.496088%20-35.337009&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 80. [AT2026ajoq](https://www.wis-tns.org/object/2026ajoq) near NGC1596

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1596 as this object's host. The 0.89838° (53.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 22.27 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1596** · `NGC1596` |
| Catalog display name | NGC1596 |
| Type / constellation | Galaxy · Dorado |
| Catalog magnitude / angular size | 11.1 · 3.87′ × 1.02′ |
| Distance | 15,950 kpc |
| Separation | 0.89838° · 53.90′ |
| Catalog description | NGC 1596 is a lenticular galaxy in the constellation Dorado. The galaxy lies about 55 million light years away from Earth, which means, given its apparent dimensions, that NGC 1596 is approximately 55,000 light years across. It was discovered by John Herschel on December 5, 1834. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajoq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=67.551399%20-55.848793&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 81. [AT2026ajor](https://www.wis-tns.org/object/2026ajor) near NGC1672

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1672 as this object's host. The 0.66270° (39.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 23.32 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1672** · `NGC1672` |
| Catalog display name | NGC1672 |
| Type / constellation | Galaxy · Dorado |
| Catalog magnitude / angular size | 10.2 · 6.14′ × 5.46′ |
| Distance | — |
| Separation | 0.66270° · 39.76′ |
| Catalog description | NGC 1672 is a barred spiral galaxy located in the constellation Dorado. It was discovered by Scottish astronomer James Dunlop on 5 November 1826. It was originally unclear whether it was a member of the Dorado Group, with some sources finding it to be a member and other sources rejecting its membership. However, recent tip of the red-giant branch (TRGB) measurements indicate that NGC 1672 is located at the same distance as other members, suggesting it is indeed a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajor) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=70.394339%20-58.849454&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 82. [AT2026ajos](https://www.wis-tns.org/object/2026ajos) near NGC1549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1549 as this object's host. The 0.50705° (30.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 22.1 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1549** · `NGC1549` |
| Catalog display name | NGC1549 |
| Type / constellation | Galaxy · Dorado |
| Catalog magnitude / angular size | 9.8 · 5.09′ × 4.35′ |
| Distance | — |
| Separation | 0.50705° · 30.42′ |
| Catalog description | NGC 1549 is an elliptical galaxy located in the constellation Dorado. It is located at a distance of about 50 million light years from Earth, which, given its apparent dimensions, means that NGC 1549 is about 75,000 light years across. NGC 1549 was discovered by John Herschel on 6 December 1835 and may have been observed by James Dunlop in 1826. It is a member of the Dorado Group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajos) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.041515%20-55.567801&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 83. [AT2026ajpf](https://www.wis-tns.org/object/2026ajpf) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.95803° (57.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T05:47:42Z · 4 days · 24.04 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.95803° · 57.48′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.671205%20-47.921664&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 84. [AT2026ajqp](https://www.wis-tns.org/object/2026ajqp) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.92885° (55.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 1 days · 23.6 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.92885° · 55.73′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=61.273532%20-48.6454728&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 85. [AT2026ajqu](https://www.wis-tns.org/object/2026ajqu) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.90734° (54.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T09:37:27Z · 1 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.90734° · 54.44′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.104361%20-37.947365&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 86. [AT2026ajqv](https://www.wis-tns.org/object/2026ajqv) near NGC1374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1374 as this object's host. The 0.29655° (17.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T09:37:27Z · 1 days · 22.77 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1374** · `NGC1374` |
| Catalog display name | NGC1374 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 11.1 · 2.86′ × 2.65′ |
| Distance | 19,200 kpc |
| Separation | 0.29655° · 17.79′ |
| Catalog description | NGC 1374 is a low-luminosity elliptical galaxy in the southern constellation Fornax. It was discovered by John Herschel on November 29, 1837. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.583987%20-34.998844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 87. [AT2026ajqw](https://www.wis-tns.org/object/2026ajqw) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.90002° (54.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 1 days · 23.09 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.90002° · 54.00′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.240649%20-36.276628&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 88. [AT2026ajqx](https://www.wis-tns.org/object/2026ajqx) near NGC1365

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1365 as this object's host. The 0.95992° (57.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 1 days · 22.19 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1365** · `NGC1365` |
| Catalog display name | NGC1365 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 10.1 · 12.02′ × 6.14′ |
| Distance | — |
| Separation | 0.95992° · 57.60′ |
| Catalog description | NGC 1365, also known as the Fornax Propeller Galaxy or the Great Barred Spiral Galaxy, is a double-barred spiral galaxy about 56 million light-years away in the constellation Fornax. It was discovered by Scottish astronomer James Dunlop on 2 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.112329%20-36.910974&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 89. [AT2026ajqy](https://www.wis-tns.org/object/2026ajqy) near NGC1332

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1332 as this object's host. The 0.63270° (37.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 1 days · 22.68 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.63270° · 37.96′ |
| Catalog description | NGC 1332 is an almost edge-on elliptical galaxy located in constellation of Eridanus. Situated about 70 million light years away, it is a member of the Eridanus Cluster of galaxies, a cluster of about 200 galaxies. It is also the brightest member of the NGC 1332 Group. It was discovered by William Herschel on 9 December 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.230475%20-21.883109&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 90. [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) near Messier 81

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 81 as this object's host. The 0.68539° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:28:39Z · 1 days · 20.85 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.68539° · 41.12′ |
| Catalog description | Messier 81 (also known as NGC 3031 or Bode's Galaxy) is a grand design spiral galaxy about 12 million light-years away in the constellation Ursa Major. It has a D25 isophotal diameter of 29.44 kiloparsecs (96,000 light-years). Because of its relative proximity to the Milky Way galaxy, large size, and active galactic nucleus (which harbors a 70 million M☉ supermassive black hole), Messier 81 has been studied extensively by professional astronomers. The galaxy's large size and relatively high brightness also makes it a popular target for amateur astronomers. In late February 2022, astronomers reported that M81 may be the source of FRB 20200120E, a repeating fast radio burst. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=13.9852945%2022.146041&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 91. [AT2026ajri](https://www.wis-tns.org/object/2026ajri) near IC 1540

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1540 as this object's host. The 0.82912° (49.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:21:13Z · 1 days · 21.44 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.82912° · 49.75′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1540 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajri) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.738124%2024.1885576&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 92. [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) near NGC2985

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2985 as this object's host. The 0.55170° (33.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T05:10:07Z · 2 days · 19.61 wide |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.55170° · 33.10′ |
| Catalog description | NGC 2985 is a spiral galaxy located in the constellation Ursa Major. It is located at a distance of circa 70 million light years from Earth, which, given its apparent dimensions, means that NGC 2985 is about 95,000 light years across. It was discovered by William Herschel on April 3, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=145.886332%2072.473064&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 93. [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) near IC 74

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 74 as this object's host. The 0.60041° (36.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:04:48Z · 7 days · 22.82 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.60041° · 36.02′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 74 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.904917%203.923525&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 94. [AT2026ajta](https://www.wis-tns.org/object/2026ajta) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 0.88977° (53.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:12:00Z · 7 days · 22.45 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.88977° · 53.39′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajta) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.029833%20-0.7274&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 95. [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 0.82591° (49.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:45:07Z · 7 days · 21.43 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.82591° · 49.55′ |
| Catalog description | NGC 3521, also known as the Bubble Galaxy, is a flocculent intermediate spiral galaxy located in the constellation Leo. Its velocity with respect to the cosmic microwave background is 1167 ± 26 km/s, which corresponds to a Hubble distance of 56.1 ± 4.1 Mly (17.21 ± 1.26 Mpc). However, 26 non-redshift measurements give a much closer distance of 37.17 ± 1.83 Mly (11.395 ± 0.56 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.480833%20-0.826333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 96. [AT2026ajut](https://www.wis-tns.org/object/2026ajut) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.37521° (22.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.82 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.37521° · 22.51′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajut) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.406097%20-12.8842788&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 97. [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.41178° (24.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.02 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.41178° · 24.71′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.6740286%20-12.9694323&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 98. [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 0.66407° (39.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.11 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.66407° · 39.84′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.6718945%20-13.6722882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 99. [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 0.99563° (59.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.99563° · 59.74′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.1011659%20-13.0016366&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 100. [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 0.95089° (57.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 21.89 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.95089° · 57.05′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.1565123%20-13.4279807&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 101. [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 0.31675° (19.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:26:43Z · 0 days · 22.91 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.31675° · 19.00′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.0642743%20-9.9601916&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 102. [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 0.46768° (28.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 21.59 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.46768° · 28.06′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.5602051%20-13.2432007&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 103. [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) near IC2560

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2560 as this object's host. The 0.97287° (58.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T17:23:09Z · 0 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2560** · `IC2560` |
| Catalog display name | IC2560 |
| Type / constellation | Galaxy · Antlia |
| Catalog magnitude / angular size | 12.1 · 3.55′ × 1.67′ |
| Distance | — |
| Separation | 0.97287° · 58.37′ |
| Catalog description | IC 2560 is a spiral galaxy lying over 110 million light-years away from Earth in the constellation of Antlia. It was discovered by Lewis Swift on 28 December 1897. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.134422%20-32.990954&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 104. [AT2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65297° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 11 days · 19.17 wide |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiep) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=335.3713756%20-14.6685694&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 105. [AT2026aizq](https://www.wis-tns.org/object/2026aizq) near Lynds Bright Nebula 54 (LBN54)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 54 (LBN54) as this object's host. The 1.56600° (93.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:47:24Z · 6 days · 18.67 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 106. [AT2026ajds](https://www.wis-tns.org/object/2026ajds) near Boomerang nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Boomerang nebula as this object's host. The 1.53259° (91.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:30:35Z · 5 days · 19.01 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Boomerang nebula** · `eso172-07` |
| Catalog display name | Boomerang nebula |
| Type / constellation | Planetary nebula · Cen |
| Catalog magnitude / angular size | — · 1.45′ × 0.72′ |
| Distance | 5,000 ly |
| Separation | 1.53259° · 91.96′ |
| Catalog description | The Boomerang Nebula is a bipolar reflection young planetary nebula located approximately 5,000 light-years from Earth in the constellation Centaurus. The Boomerang Nebula (canonical name ) is a bipolar reflection young planetary nebula located approximately 5,000 light-years from Earth in the constellation Centaurus. Holmberg & Lauberts (Uppsala Observatory) and Schuster & West (European Southern Observatory (ESO))  in their survey of 1976 or earlier discovered the existence of an object at the location. Before or during 1978 I.S. Glass  discovered the object as a nebula  with G. Wegner, both of South African Astronomical Observatory, from data of the ESO Quick Blue Survey. Wegner and Glass in their paper of 1979 mentioned a "butterfly" or "bow-tie" like shape. K. N. R. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajds) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=189.799902%2053.3257763&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 107. [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) near Lynds Dark Nebula 1473 (LDN1473)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1473 (LDN1473) as this object's host. The 1.48136° (88.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:51:51Z · 0 days · 19.27 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Dark Nebula 1473 (LDN1473)** · `LDN1473` |
| Catalog display name | Lynds Dark Nebula 1473 (LDN1473) |
| Type / constellation | Dark nebula · Perseus |
| Catalog magnitude / angular size | — · 26.05′ × 26.05′ |
| Distance | — |
| Separation | 1.48136° · 88.88′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajxa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.741255%2036.63532&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 108. [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) near Lynds Bright Nebula 718 (LBN718)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 718 (LBN718) as this object's host. The 0.53252° (31.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:11:33Z · 12 days · 19.39 r |
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
| Subject | **Lynds Bright Nebula 718 (LBN718)** · `LBN718` |
| Catalog display name | Lynds Bright Nebula 718 (LBN718) |
| Type / constellation | HII · Perseus |
| Catalog magnitude / angular size | — · 210′ × 30′ |
| Distance | — |
| Separation | 0.53252° · 31.95′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ahxz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.3073554%2038.0684979&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 109. [AT2026aivb](https://www.wis-tns.org/object/2026aivb) near Lynds Dark Nebula 387 (LDN387)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 387 (LDN387) as this object's host. The 0.97429° (58.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T01:50:01Z · 8 days · 19.04 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aivb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=260.3900108%20-3.6491243&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 110. [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) near The opal nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify The opal nebula as this object's host. The 0.75975° (45.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:11:11Z · 9 days · 18.9 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **The opal nebula** · `stdr98` |
| Catalog display name | The opal nebula |
| Type / constellation | Planetary nebula · Cas |
| Catalog magnitude / angular size | — · 1.5′ × 1′ |
| Distance | 965 ly |
| Separation | 0.75975° · 45.59′ |
| Catalog description | Gyulbudaghian's Nebula (gyool-boo-DAH-ghee-an) is a reflection nebula in the northern constellation Cepheus, located about 1.5 degrees west of the much brighter reflection nebula NGC 7023. The light illuminating it comes from the T Tauri star PV Cephei. It is known for changing its shape dramatically on a timescale of months to years, as the brightness of PV Cephei changes. The nebula, whose magnitude ranges from 13.4 to 18.5, is far too faint to be seen with the naked eye, or even a small telescope. However, because of its changing morphology, it has become a target for observations by advanced amateur astronomers. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajrf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.8508175%2055.1728892&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 111. [SN2026aela](https://www.wis-tns.org/object/2026aela) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.46981° (88.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0503 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T20:31:24Z · 41 days · 18.14 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4020....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4020....1M/abstract) |
| Classification references | [2026TNSCR4217....1S](https://ui.adsabs.harvard.edu/abs/2026TNSCR4217....1S/abstract) |
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
| Separation | 1.46981° · 88.19′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aela) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=129.4775734%20-1.8406933&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 112. [AT2026aixb](https://www.wis-tns.org/object/2026aixb) near IC1508

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1508 as this object's host. The 1.64877° (98.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:25:41Z · 6 days · 20.2 L |
| Latest public photometry | Not available in the staged feed |
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

### 113. [AT2026aizb](https://www.wis-tns.org/object/2026aizb) near IC 1776

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
| Discovery | 2026-11-08T08:40:18Z · 7 days · 20.76 w |
| Latest public photometry | Not available in the staged feed |
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

### 114. [AT2026ajbj](https://www.wis-tns.org/object/2026ajbj) near IC2007

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2007 as this object's host. The 1.79494° (107.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T13:58:26Z · 6 days · 20.17 L |
| Latest public photometry | Not available in the staged feed |
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

### 115. [AT2026ajbo](https://www.wis-tns.org/object/2026ajbo) near NGC 4346

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 4346 as this object's host. The 1.29956° (77.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:48:55Z · 5 days · 19.95 r |
| Latest public photometry | Not available in the staged feed |
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

### 116. [AT2026ajbw](https://www.wis-tns.org/object/2026ajbw) near IC 632

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
| Discovery | 2026-11-09T12:58:39Z · 6 days · 20.02 r |
| Latest public photometry | Not available in the staged feed |
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

### 117. [AT2026ajby](https://www.wis-tns.org/object/2026ajby) near IC48

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC48 as this object's host. The 1.83966° (110.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T03:31:31Z · 6 days · 20.2 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4564....1W](https://ui.adsabs.harvard.edu/abs/2026TNSTR4564....1W/abstract) |
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
| Separation | 1.83966° · 110.38′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, small in angular size (var brightness?) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajby) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.8589676%20-6.3471302&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 118. [AT2026ajek](https://www.wis-tns.org/object/2026ajek) near IC 5241

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5241 as this object's host. The 1.64483° (98.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:19:40Z · 7 days · 22.65 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.64483° · 98.69′ |
| Catalog description | NGC 804 is a lenticular galaxy located in the Triangulum constellation about 231 million light-years from the Milky Way. It was discovered by the American astronomer Lewis Swift in 1885. This galaxy was also observed by the French astronomer Guillaume Bigourdan on December 24, 1897, and it has been added to the Index Catalogue under the symbol IC 1773. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5241 has the different designation NGC 804 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajek) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=341.855167%201.851428&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 119. [AT2026ajeo](https://www.wis-tns.org/object/2026ajeo) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 1.33383° (80.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:10:33Z · 7 days · 22.9 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1639** · `IC 1639` |
| Catalog display name | NGC5042 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.76′ × 0.7′ |
| Distance | — |
| Separation | 1.33383° · 80.03′ |
| Catalog description | NGC 5042 is an intermediate spiral galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background for is 1,697±22 km/s, which corresponds to a Hubble distance of 81.6 ± 5.8 Mly (25.03 ± 1.78 Mpc). However, 15 non redshift measurements give a much closer distance of 47.88 ± 2.37 Mly (14.680 ± 0.726 Mpc). It was discovered by British astronomer John Herschel on 25 March 1836. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1639 has the different designation NGC5042 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajeo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.160292%20-0.116889&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 120. [AT2026ajff](https://www.wis-tns.org/object/2026ajff) near NGC289

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC289 as this object's host. The 1.00140° (60.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:29:48Z · 7 days · 20.17 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4582....1M](https://ui.adsabs.harvard.edu/abs/2026TNSTR4582....1M/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC289** · `NGC289` |
| Catalog display name | NGC289 |
| Type / constellation | Galaxy · Sculptor |
| Catalog magnitude / angular size | 11.2 · 3.36′ × 2.51′ |
| Distance | 18,200 kpc |
| Separation | 1.00140° · 60.08′ |
| Catalog description | NGC 289 is a spiral galaxy in the southern constellation of Sculptor, located at a distance of 76 megalight-years from the Milky Way. It was discovered on September 27, 1834, by John Herschel. The compiler of the New General Catalogue, John Louis Emil Dreyer, noted that NGC 289 was "pretty bright, large, extended, between 2 considerably bright stars". The plane of the galaxy is inclined by an angle of 45° to the line of sight from the Earth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajff) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=12.0076788%20-31.2884437&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 121. [AT2026ajji](https://www.wis-tns.org/object/2026ajji) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.46840° (88.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:15:17Z · 3 days · 19.77 L |
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
| Separation | 1.46840° · 88.10′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajji) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.86421%2038.7843267&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 122. [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) near NGC3198

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3198 as this object's host. The 1.44295° (86.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T06:12:54Z · 2 days · 19.73 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.44295° · 86.58′ |
| Catalog description | NGC 3198, also known as Herschel 146 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by German-British astronomer William Herschel on 15 January 1788. NGC 3198 is located in the Leo Spur, which is part of the Virgo Supercluster, and is approximately 47 million light years away. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.149026%2044.369745&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 123. [AT2026ajju](https://www.wis-tns.org/object/2026ajju) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 1.03532° (62.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 3 days · 19.62 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.03532° · 62.12′ |
| Catalog description | NGC 3239 is an irregular galaxy in the constellation of Leo. The galaxy was discovered in 1784 by William Herschel and is part of the New General Catalogue. It harbors a large and relatively bright H II region in its southeastern section that was first cataloged by Russian astronomer Boris Vorontsov-Velyaminov as VV95b. It's believed that NGC 3239 is the result of a galactic merger with a low-mass galaxy. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajju) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.294987%2016.839768&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 124. [AT2026ajlv](https://www.wis-tns.org/object/2026ajlv) near IC 74

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 74 as this object's host. The 1.59885° (95.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T17:26:52Z · 5 days · 22.55 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.59885° · 95.93′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 74 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.062458%204.365214&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 125. [AT2026ajlw](https://www.wis-tns.org/object/2026ajlw) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.28359° (77.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T17:26:52Z · 5 days · 22.67 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.28359° · 77.02′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.175458%205.498386&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 126. [AT2026ajlx](https://www.wis-tns.org/object/2026ajlx) near IC 70

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 70 as this object's host. The 1.02713° (61.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T17:32:38Z · 5 days · 22.55 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 70** · `IC 70` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.42′ × 0.24′ |
| Distance | — |
| Separation | 1.02713° · 61.63′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 70 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.115458%200.628875&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 127. [AT2026ajmf](https://www.wis-tns.org/object/2026ajmf) near IC 5241

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5241 as this object's host. The 1.90571° (114.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:19:40Z · 7 days · 22.59 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.90571° · 114.34′ |
| Catalog description | NGC 804 is a lenticular galaxy located in the Triangulum constellation about 231 million light-years from the Milky Way. It was discovered by the American astronomer Lewis Swift in 1885. This galaxy was also observed by the French astronomer Guillaume Bigourdan on December 24, 1897, and it has been added to the Index Catalogue under the symbol IC 1773. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5241 has the different designation NGC 804 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.312958%202.499219&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 128. [AT2026ajok](https://www.wis-tns.org/object/2026ajok) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 1.08961° (65.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 19.77 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1993** · `IC1993` |
| Catalog display name | IC1993 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 11.9 · 2.81′ × 2.48′ |
| Distance | — |
| Separation | 1.08961° · 65.38′ |
| Catalog description | IC 1993 is an unbarred spiral galaxy in the constellation Fornax. It was discovered by Lewis Swift on November 19, 1897. At a distance of about 50 million light-years, and redshift of 1057 km/s, it is one of the closest to us of the 200 galaxies in the Fornax Cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajok) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.752789%20-34.799411&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026ajol](https://www.wis-tns.org/object/2026ajol) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 1.17282° (70.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 2 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.17282° · 70.37′ |
| Catalog description | NGC 1340 is an elliptical galaxy located in the constellation Fornax. Its speed relative to the cosmic microwave background is 1,126 ± 17 km/s, which corresponds to a Hubble Distance of 16.6 ± 1.2 Mpc. It was discovered by the German-British astronomer William Herschel in 1790, but it was added to the New General Catalog under the designation NGC 1344 later. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajol) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.387019%20-30.727459&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026ajqe](https://www.wis-tns.org/object/2026ajqe) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.97158° (118.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:28:56Z · 1 days · 21.46 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.97158° · 118.29′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=321.2297667%20-19.5600719&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026ajqf](https://www.wis-tns.org/object/2026ajqf) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.19498° (71.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 1 days · 23.7 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.19498° · 71.70′ |
| Catalog description | considerably bright, large, extremely, excessively extended 80deg , very much / magnitude brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=57.8148197%20-50.0012778&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026ajqg](https://www.wis-tns.org/object/2026ajqg) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.43634° (86.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:04:44Z · 1 days · 22.41 z |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.43634° · 86.18′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.1243031%20-47.3582426&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 133. [AT2026ajqm](https://www.wis-tns.org/object/2026ajqm) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.42198° (85.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:14:05Z · 1 days · 21.44 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.42198° · 85.32′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=323.0632874%20-22.479333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 134. [AT2026ajqz](https://www.wis-tns.org/object/2026ajqz) near NGC1350

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1350 as this object's host. The 1.39326° (83.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 1 days · 22.81 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.39326° · 83.60′ |
| Catalog description | NGC 1350 is a spiral galaxy located 87 million light years away in the southern constellation Fornax. It was discovered by Scottish astronomer James Dunlop on 24 November 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=53.968429%20-32.650615&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 135. [AT2026ajra](https://www.wis-tns.org/object/2026ajra) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 1.92768° (115.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 1 days · 21.72 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1993** · `IC1993` |
| Catalog display name | IC1993 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 11.9 · 2.81′ × 2.48′ |
| Distance | — |
| Separation | 1.92768° · 115.66′ |
| Catalog description | IC 1993 is an unbarred spiral galaxy in the constellation Fornax. It was discovered by Lewis Swift on November 19, 1897. At a distance of about 50 million light-years, and redshift of 1057 km/s, it is one of the closest to us of the 200 galaxies in the Fornax Cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajra) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=55.75498%20-31.979645&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 136. [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.28167° (76.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T00:21:13Z · 7 days · 19.83 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.28167° · 76.90′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=321.5223436%20-22.181237&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 137. [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) near IC 2016

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2016 as this object's host. The 1.84241° (110.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T12:03:19Z · 2 days · 20.87 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 2016** · `IC 2016` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Tau |
| Catalog magnitude / angular size | — · 0.51′ × 0.25′ |
| Distance | — |
| Separation | 1.84241° · 110.54′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2016 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.5366584%2020.30768&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 138. [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) near IC5338

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5338 as this object's host. The 1.79914° (107.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:12:20Z · 1 days · 19.52 cyan |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79914° · 107.95′ |
| Catalog description | IC 5337 or JW100, is a spiral galaxy located 800 million light-years away from the Solar System in the constellation of Pegasus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.6032467%2022.2586267&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 139. [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) near IC 17

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 17 as this object's host. The 1.57726° (94.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T21:33:37Z · 2 days · 19.68 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.57726° · 94.64′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 17 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=8.170507%203.830257&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 140. [AT2026ajss](https://www.wis-tns.org/object/2026ajss) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.55710° (93.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T17:22:33Z · 4 days · 22.86 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.55710° · 93.43′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajss) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.212%203.7757&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 141. [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.08432° (65.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:49:26Z · 6 days · 22.02 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.08432° · 65.06′ |
| Catalog description | NGC 3521, also known as the Bubble Galaxy, is a flocculent intermediate spiral galaxy located in the constellation Leo. Its velocity with respect to the cosmic microwave background is 1167 ± 26 km/s, which corresponds to a Hubble distance of 56.1 ± 4.1 Mly (17.21 ± 1.26 Mpc). However, 26 non-redshift measurements give a much closer distance of 37.17 ± 1.83 Mly (11.395 ± 0.56 Mpc). It was discovered by German-British astronomer William Herschel on 22 February 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.515792%20-1.084572&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 142. [AT2026ajti](https://www.wis-tns.org/object/2026ajti) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.42421° (85.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T16:56:38Z · 5 days · 22.44 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.42421° · 85.45′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajti) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.272125%200.564381&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 143. [AT2026ajum](https://www.wis-tns.org/object/2026ajum) near IC 1540

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1540 as this object's host. The 1.37052° (82.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:56:09Z · 4 days · 22.35 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.37052° · 82.23′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1540 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajum) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.395125%2025.045464&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026ajux](https://www.wis-tns.org/object/2026ajux) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.74911° (104.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:17:24Z · 0 days · 22.92 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.74911° · 104.95′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajux) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=334.3138047%20-14.0010557&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.06627° (63.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:26:43Z · 0 days · 22.32 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.06627° · 63.98′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajuz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.0263489%20-8.8914218&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.37982° (82.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 22.34 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.37982° · 82.79′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.782114%20-11.9442127&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 147. [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.70955° (102.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:27:24Z · 0 days · 21.97 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.70955° · 102.57′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.0850478%20-9.426595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.38932° (83.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:26:43Z · 0 days · 22.71 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.38932° · 83.36′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.0639558%20-8.5677499&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.85790° (111.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 20.46 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.85790° · 111.47′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.43098%20-14.8917716&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 150. [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.29911° (77.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:26:43Z · 0 days · 22.31 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.29911° · 77.95′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.0611332%20-9.8378349&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 151. [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.26051° (75.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.48 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.26051° · 75.63′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.832431%20-12.8518522&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 152. [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.52083° (91.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 21.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52083° · 91.25′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.9063741%20-14.4452269&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.67055° (100.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.74 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.67055° · 100.23′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.0316888%20-14.4361332&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 154. [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.64042° (98.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.64042° · 98.43′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.7272263%20-11.2472883&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 155. [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.79224° (107.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.7 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79224° · 107.53′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.8665365%20-14.7734937&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 156. [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.40126° (84.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.99 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.40126° · 84.08′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.2140028%20-14.0248453&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 157. [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.85355° (111.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.85355° · 111.21′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.4441614%20-14.5260801&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 158. [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.52748° (91.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.84 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52748° · 91.65′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.4041525%20-14.5220132&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 159. [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.03799° (62.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.67 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.03799° · 62.28′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.9253205%20-13.7974722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 160. [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.38720° (83.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 21.31 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.38720° · 83.23′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=331.0665497%20-14.1592539&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 161. [AT2026ajws](https://www.wis-tns.org/object/2026ajws) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.64454° (98.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.64454° · 98.67′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajws) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.9160446%20-14.7832118&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 162. [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.89146° (113.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:27:24Z · 0 days · 19.73 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.89146° · 113.49′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.8754911%20-9.495113&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 163. [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.86530° (111.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.68 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.86530° · 111.92′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.8122079%20-14.5402267&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 164. [AT2026ajww](https://www.wis-tns.org/object/2026ajww) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.35306° (81.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 22.29 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.35306° · 81.18′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajww) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.7042094%20-13.2491686&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 165. [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.79292° (107.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:29:36Z · 0 days · 23.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79292° · 107.58′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.5577412%20-14.1460601&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 166. [AT2026aiki](https://www.wis-tns.org/object/2026aiki) near IC 230

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 230 as this object's host. The 0.98313° (58.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T11:50:45Z · 9 days · 20.27 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiki) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.8446171%20-9.9113799&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 167. [AT2026aiup](https://www.wis-tns.org/object/2026aiup) near IC148

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC148 as this object's host. The 0.32866° (19.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:07:31Z · 12 days · 20.72 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiup) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=25.5245754%2014.2954958&fov=0.5&survey=P%2FDSS2%2Fcolor)

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
| Discovery | 2026-11-01T18:10:04Z · 14 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
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

### 169. [AT2026aivt](https://www.wis-tns.org/object/2026aivt) near NGC864

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC864 as this object's host. The 0.37622° (22.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T16:50:52Z · 12 days · 22.44 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.057833%205.680458&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 170. [AT2026aivv](https://www.wis-tns.org/object/2026aivv) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 0.25518° (15.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:56:09Z · 10 days · 22.66 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.212542%201.163614&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026aiwb](https://www.wis-tns.org/object/2026aiwb) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.88875° (53.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:45:07Z · 8 days · 22.88 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.369125%20-0.446586&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 172. [AT2026aiwc](https://www.wis-tns.org/object/2026aiwc) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.41006° (24.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:45:07Z · 8 days · 22.4 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.147208%20-0.825983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 173. [AT2026aixe](https://www.wis-tns.org/object/2026aixe) near IC1860

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1860 as this object's host. The 0.49089° (29.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:04:26Z · 17 days · 20.05 L |
| Latest public photometry | Not available in the staged feed |
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

### 174. [AT2026aixg](https://www.wis-tns.org/object/2026aixg) near IC1895

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1895 as this object's host. The 0.41742° (25.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T12:34:32Z · 10 days · 20.63 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.997138%20-25.457798&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 175. [AT2026aiyi](https://www.wis-tns.org/object/2026aiyi) near IC1628

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1628 as this object's host. The 0.47290° (28.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:33:11Z · 17 days · 20.5 L |
| Latest public photometry | Not available in the staged feed |
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

### 176. [AT2026aiyy](https://www.wis-tns.org/object/2026aiyy) near NGC7457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7457 as this object's host. The 0.53496° (32.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:22:18Z · 9 days · 19.87 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.861474%2030.198849&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 177. [AT2026ajai](https://www.wis-tns.org/object/2026ajai) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.59906° (35.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:05:16Z · 16 days · 22.25 r |
| Latest public photometry | Not available in the staged feed |
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

### 178. [AT2026ajaj](https://www.wis-tns.org/object/2026ajaj) near IC 1757

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
| Discovery | 2026-10-30T14:08:09Z · 16 days · 22.02 r |
| Latest public photometry | Not available in the staged feed |
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

### 179. [AT2026ajar](https://www.wis-tns.org/object/2026ajar) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 0.74868° (44.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 8 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajar) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.291333%203.643194&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 180. [AT2026ajbz](https://www.wis-tns.org/object/2026ajbz) near IC163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC163 as this object's host. The 0.66373° (39.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:08:52Z · 12 days · 20.81 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=26.8778367%2021.2394728&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 181. [AT2026ajdn](https://www.wis-tns.org/object/2026ajdn) near NGC7585

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7585 as this object's host. The 0.84567° (50.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:53:56Z · 16 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.84567° · 50.74′ |
| Catalog description | NGC 7585 is a lenticular galaxy with a peculiar shape resulting from an interaction between two galaxies. It is located 145 million light years away in the constellation Aquarius which, given its apparent dimensions, means that NGC 7585 is about 100,000 light years across. It was discovered by William Herschel on September 20, 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.5633394%20-5.4939212&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 182. [AT2026ajec](https://www.wis-tns.org/object/2026ajec) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.68536° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:37:26Z · 10 days · 23.01 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.68536° · 41.12′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajec) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.770292%205.106233&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 183. [AT2026ajed](https://www.wis-tns.org/object/2026ajed) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 0.78871° (47.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:56:09Z · 10 days · 22.77 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.78871° · 47.32′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajed) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.233417%201.055569&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 184. [AT2026ajee](https://www.wis-tns.org/object/2026ajee) near IC 1776

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1776 as this object's host. The 0.75879° (45.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T18:04:19Z · 10 days · 22.59 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.75879° · 45.53′ |
| Catalog description | IC 2574, also known as Coddington's Nebula, is a dwarf spiral galaxy discovered by American astronomer Edwin Foster Coddington in 1898. Located in Ursa Major, a constellation in the northern sky, it is an outlying member of the M81 Group. It is believed that 90% of its mass is in the form of dark matter. IC 2574 does not show evidence of interaction with other galaxies. It is currently forming stars; a UV analysis showed clumps of star formation 85 to 500 light-years in size. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1776 has the different designation IC 2574 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajee) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.171667%205.361264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 185. [AT2026ajei](https://www.wis-tns.org/object/2026ajei) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.37997° (22.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:46:33Z · 8 days · 21.94 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.37997° · 22.80′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajei) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.239792%202.856492&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 186. [AT2026ajlh](https://www.wis-tns.org/object/2026ajlh) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.60624° (36.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 8 days · 21.69 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.60624° · 36.37′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.675292%203.14005&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 187. [AT2026ajmu](https://www.wis-tns.org/object/2026ajmu) near IC2421

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2421 as this object's host. The 0.41790° (25.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T21:30:14Z · 10 days · 21.64 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.41790° · 25.07′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, diffused, difficult |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=133.267333%2032.361864&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 188. [AT2026ajmx](https://www.wis-tns.org/object/2026ajmx) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.72858° (43.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:28:19Z · 9 days · 22.35 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.72858° · 43.71′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=124.403625%2057.097536&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 189. [AT2026ajnl](https://www.wis-tns.org/object/2026ajnl) near NGC1058

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1058 as this object's host. The 0.90832° (54.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:27:50Z · 17 days · 21.1 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1058** · `NGC1058` |
| Catalog display name | NGC1058 |
| Type / constellation | Galaxy · Perseus |
| Catalog magnitude / angular size | 11.2 · 2.47′ × 1.36′ |
| Distance | — |
| Separation | 0.90832° · 54.50′ |
| Catalog description | NGC 1058 is a Seyfert Type 2 galaxy in the NGC 1023 Group, located in the Perseus constellation. It is approximately 27.4 million light years from Earth and has an apparent magnitude of 11.82. It is receding from Earth at 518 kilometers per second (322 mi/s), and at 629 kilometers per second (391 mi/s) relative to the Milky Way. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=41.818875%2036.833258&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 190. [AT2026ajsm](https://www.wis-tns.org/object/2026ajsm) near IC1919

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1919 as this object's host. The 0.30868° (18.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T20:39:03Z · 17 days · 20.24 BG-q |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1919** · `IC1919` |
| Catalog display name | IC1919 |
| Type / constellation | Galaxy · Fornax |
| Catalog magnitude / angular size | 13.8 · 1.73′ × 1.08′ |
| Distance | 20,000 kpc |
| Separation | 0.30868° · 18.52′ |
| Catalog description | IC 1919 is an elliptical galaxy in the constellation of Fornax. It is 61 million light years distant from Earth and it is a member of Fornax Cluster, a cluster of approximately 200 galaxies. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.225567%20-33.092131&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 191. [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) near IC178

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC178 as this object's host. The 0.93972° (56.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:24:57Z · 17 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC178** · `IC178` |
| Catalog display name | IC178 |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 13.3 · 0.94′ × 0.79′ |
| Distance | — |
| Separation | 0.93972° · 56.38′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) faint, nucleus, or to a nucleus = 13m |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.643708%2036.094978&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 192. [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) near NGC 2964

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2964 as this object's host. The 0.25419° (15.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T21:54:43Z · 12 days · 20.75 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2964** · `NGC 2964` |
| Catalog display name | NGC 2964 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11.37 · 2.92′ × 2.18′ |
| Distance | — |
| Separation | 0.25419° · 15.25′ |
| Catalog description | One of two 6cm sources associated with [WB92] 0940+3206 |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=146.01975%2031.799456&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 193. [SN2026ahyd](https://www.wis-tns.org/object/2026ahyd) near IC5366

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5366 as this object's host. The 1.01813° (61.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.041 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:20:44Z · 12 days · 19.53 r |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=359.7728239%2051.7970796&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 194. [AT2026ajlm](https://www.wis-tns.org/object/2026ajlm) near NGC7613

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7613 as this object's host. The 0.70355° (42.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:38:24Z · 7 days · 22.24 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7613** · `NGC7613` |
| Catalog display name | NGC7613 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.70355° · 42.21′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.558917%200.860436&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 195. [AT2026ajnx](https://www.wis-tns.org/object/2026ajnx) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.40162° (24.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:16Z · 2 days · 21.82 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.40162° · 24.10′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.7909627%20-5.5680801&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026ajqr](https://www.wis-tns.org/object/2026ajqr) near Messier 72 (M72)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 72 (M72) as this object's host. The 0.84769° (50.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:25:56Z · 1 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Messier 72 (M72)** · `M72` |
| Catalog display name | Messier 72 (M72) |
| Type / constellation | Globular cluster · Aquarius |
| Catalog magnitude / angular size | 9.3 · 5.9′ × 5.9′ |
| Distance | 16.986 kpc |
| Separation | 0.84769° · 50.86′ |
| Catalog description | Messier 72 is a globular cluster in the south west of the very mildly southern constellation of Aquarius. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=313.4293144%20-13.3793404&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 197. [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.76418° (45.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 21.93 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.76418° · 45.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.6378634%20-11.3209028&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 198. [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.83221° (49.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.83221° · 49.93′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.1939786%20-11.7828268&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 199. [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38606° (23.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 21.24 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.38606° · 23.16′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.9728463%20-11.5782794&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 200. [AT2026aifu](https://www.wis-tns.org/object/2026aifu) near Lynds Bright Nebula 1025 (LBN1025)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1025 (LBN1025) as this object's host. The 1.13184° (67.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T10:32:52Z · 11 days · 19.01 g |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aifu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=90.08462%20-16.1648627&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 201. [AT2026aimn](https://www.wis-tns.org/object/2026aimn) near van den Bergh 29 (VDB29)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 29 (VDB29) as this object's host. The 1.12187° (67.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:56:00Z · 9 days · 19.23 Clear |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aimn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=73.300604%2029.507051&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026aizl](https://www.wis-tns.org/object/2026aizl) near Lynds Dark Nebula 1563 (LDN1563)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1563 (LDN1563) as this object's host. The 1.36769° (82.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T09:35:04Z · 8 days · 18.61 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aizl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=74.6590599%2012.575872&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 203. [AT2026ahdm](https://www.wis-tns.org/object/2026ahdm) near IC 1507

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
| Discovery | 2026-10-28T13:52:19Z · 18 days · 21.64 g |
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

### 204. [AT2026ahhy](https://www.wis-tns.org/object/2026ahhy) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.55641° (93.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:57:54Z · 16 days · 21.58 r |
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

### 205. [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) near IC1401

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1401 as this object's host. The 1.09401° (65.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:14:32Z · 15 days · 19.8 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4403....1J](https://ui.adsabs.harvard.edu/abs/2026TNSTR4403....1J/abstract) |
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
| Separation | 1.09401° · 65.64′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=325.7642553%202.5101047&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 206. [AT2026aicw](https://www.wis-tns.org/object/2026aicw) near IC1574

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1574 as this object's host. The 1.16063° (69.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T11:16:36Z · 17 days · 19.96 L |
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

### 207. [AT2026aidv](https://www.wis-tns.org/object/2026aidv) near IC 5298

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5298 as this object's host. The 1.04272° (62.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T04:07:55Z · 10 days · 19.73 r |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aidv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.5201053%2024.6100872&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 208. [AT2026aigp](https://www.wis-tns.org/object/2026aigp) near IC2007

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2007 as this object's host. The 1.25561° (75.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:17:49Z · 14 days · 19.83 L |
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

### 209. [AT2026aihe](https://www.wis-tns.org/object/2026aihe) near NGC2855

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2855 as this object's host. The 1.17126° (70.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:32Z · 14 days · 19.64 L |
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

### 210. [AT2026aiit](https://www.wis-tns.org/object/2026aiit) near IC 536

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 536 as this object's host. The 1.35004° (81.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T12:16:17Z · 20 days · 20.1 g |
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
| Subject | **IC 536** · `IC 536` |
| Catalog display name | IC 10 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | — · 1.09′ × 0.22′ |
| Distance | 2.5 ly |
| Separation | 1.35004° · 81.00′ |
| Catalog description | IC 10 is an irregular galaxy in the constellation Cassiopeia. It was discovered by American astronomer Lewis Swift on 8 October 1887. In 1935 Nicholas Mayall became the first to suggest that the object is extragalactic. Edwin Hubble suspected it might belong to the Local Group of galaxies, but its status remained uncertain for decades. The radial velocity of IC 10 was measured in 1962, and it was found to be approaching the Milky Way at approximately 350 km/s, strengthening the evidence for its membership in the Local Group. Its membership in the group was finally confirmed in 1996 by direct measurements of its distance based on observations of Cepheids; most estimates place the galaxy 2–3 million light years from Earth, with some estimates ranging from 1.5–4.5 million light years. Despite its closeness, the galaxy is rather difficult to study because it lies near the plane of the Milky Way and is therefore  heavily obscured by interstellar matter. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 536 has the different designation IC 10 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiit) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.6408058%2026.3742758&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 211. [AT2026ainu](https://www.wis-tns.org/object/2026ainu) near NGC1637

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1637 as this object's host. The 1.60141° (96.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T15:16:16Z · 13 days · 19.94 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4493....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4493....1O/abstract) |
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
| Separation | 1.60141° · 96.08′ |
| Catalog description | NGC 1637 is an isolated, non-interacting intermediate spiral galaxy in the constellation Eridanus, about a degree to the WNW of the star Mu Eridani. It was discovered by German-British astronomer William Herschel on 1 February 1786. It is located at a distance of about 9.77 ± 1.82 Mpc (31.9 ± 5.9 Mly) from the Milky Way. The galaxy is inclined at an angle of 31.1° to the line of sight from the Earth and the long axis is oriented along a position angle of 16.3°. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ainu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.7867233%20-2.5861044&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 212. [AT2026airi](https://www.wis-tns.org/object/2026airi) near NGC636

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC636 as this object's host. The 1.79687° (107.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T11:07:26Z · 8 days · 20.14 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=24.8348337%20-5.7167276&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 213. [AT2026aiul](https://www.wis-tns.org/object/2026aiul) near Caldwell 44 (C44)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 44 (C44) as this object's host. The 1.56654° (93.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T08:43:14Z · 14 days · 21.17 w |
| Latest public photometry | Not available in the staged feed |
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

### 214. [AT2026aiun](https://www.wis-tns.org/object/2026aiun) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.41669° (85.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T09:47:31Z · 12 days · 20.54 w |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiun) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.5662017%200.1561255&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 215. [AT2026aius](https://www.wis-tns.org/object/2026aius) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.88178° (112.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T06:19:17Z · 9 days · 19.94 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aius) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.1790365%20-13.7731417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 216. [AT2026aivi](https://www.wis-tns.org/object/2026aivi) near IC 1797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1797 as this object's host. The 1.40546° (84.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:53:01Z · 12 days · 19.82 r |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.8618328%2021.7196375&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 217. [AT2026aivw](https://www.wis-tns.org/object/2026aivw) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.24572° (74.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T18:01:26Z · 10 days · 21.91 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.258542%200.318439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 218. [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) near NGC2681

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2681 as this object's host. The 1.89726° (113.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:43:40Z · 14 days · 21.09 g |
| Latest public photometry | Not available in the staged feed |
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

### 219. [AT2026aiwk](https://www.wis-tns.org/object/2026aiwk) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.74454° (104.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T12:34:03Z · 26 days · 19.72 i |
| Latest public photometry | Not available in the staged feed |
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

### 220. [AT2026aiwu](https://www.wis-tns.org/object/2026aiwu) near IC 1568

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1568 as this object's host. The 1.34453° (80.67′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:22:30Z · 9 days · 20.14 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.6938485%205.5351742&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 221. [AT2026aixs](https://www.wis-tns.org/object/2026aixs) near NGC3610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3610 as this object's host. The 1.63021° (97.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:36:44Z · 13 days · 19.97 r |
| Latest public photometry | Not available in the staged feed |
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

### 222. [AT2026aiyb](https://www.wis-tns.org/object/2026aiyb) near IC392

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC392 as this object's host. The 1.52492° (91.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T14:18:04Z · 14 days · 20.39 L |
| Latest public photometry | Not available in the staged feed |
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

### 223. [AT2026aiyd](https://www.wis-tns.org/object/2026aiyd) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.26208° (75.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T20:04:33Z · 16 days · 20 L |
| Latest public photometry | Not available in the staged feed |
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

### 224. [AT2026aiye](https://www.wis-tns.org/object/2026aiye) near IC1616

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1616 as this object's host. The 1.28647° (77.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T11:05:38Z · 8 days · 19.93 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiye) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.063801%20-26.437733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 225. [AT2026aiyh](https://www.wis-tns.org/object/2026aiyh) near IC2152

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2152 as this object's host. The 1.16508° (69.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T14:57:38Z · 10 days · 20.26 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.686947%20-24.211454&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 226. [AT2026aizu](https://www.wis-tns.org/object/2026aizu) near IC 1507

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
| Discovery | 2026-10-29T15:01:26Z · 17 days · 22.25 r |
| Latest public photometry | Not available in the staged feed |
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

### 227. [AT2026aizw](https://www.wis-tns.org/object/2026aizw) near IC 5374

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
| Discovery | 2026-10-30T13:22:04Z · 16 days · 22.11 r |
| Latest public photometry | Not available in the staged feed |
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

### 228. [AT2026aizx](https://www.wis-tns.org/object/2026aizx) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.77435° (106.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:52:48Z · 14 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
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

### 229. [AT2026ajae](https://www.wis-tns.org/object/2026ajae) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.54038° (92.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T14:41:16Z · 29 days · 22.56 g |
| Latest public photometry | Not available in the staged feed |
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

### 230. [AT2026ajaf](https://www.wis-tns.org/object/2026ajaf) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 1.97393° (118.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:04:48Z · 16 days · 22.36 r |
| Latest public photometry | Not available in the staged feed |
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

### 231. [AT2026ajah](https://www.wis-tns.org/object/2026ajah) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.73881° (104.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:56:38Z · 16 days · 21.96 r |
| Latest public photometry | Not available in the staged feed |
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

### 232. [AT2026ajay](https://www.wis-tns.org/object/2026ajay) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 1.60207° (96.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T19:23:31Z · 27 days · 21.83 g |
| Latest public photometry | Not available in the staged feed |
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

### 233. [AT2026ajbe](https://www.wis-tns.org/object/2026ajbe) near IC 180

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
| Discovery | 2026-10-31T20:45:36Z · 15 days · 21.27 r |
| Latest public photometry | Not available in the staged feed |
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

### 234. [AT2026ajbr](https://www.wis-tns.org/object/2026ajbr) near NGC2841

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2841 as this object's host. The 1.54687° (92.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:55:42Z · 12 days · 20.52 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajbr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.1064581%2050.6747332&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 235. [AT2026ajcl](https://www.wis-tns.org/object/2026ajcl) near IC 1873

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1873 as this object's host. The 1.66353° (99.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:29:12Z · 10 days · 20.82 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=45.85227%2011.2727208&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 236. [AT2026ajcz](https://www.wis-tns.org/object/2026ajcz) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.96765° (118.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:24:52Z · 11 days · 19.92 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.351529%2039.7659917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 237. [AT2026ajdj](https://www.wis-tns.org/object/2026ajdj) near NGC7727

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7727 as this object's host. The 1.24258° (74.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:59:51Z · 16 days · 21.21 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7727** · `NGC7727` |
| Catalog display name | NGC7727 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 10.6 · 3.61′ × 2.75′ |
| Distance | — |
| Separation | 1.24258° · 74.55′ |
| Catalog description | NGC 7727 is a peculiar galaxy in the constellation Aquarius. It harbors two galactic nuclei, each containing a supermassive black hole, separated 1,600 light years apart. It was discovered by German-British astronomer William Herschel on 27 November 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.9696872%20-11.9342694&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 238. [AT2026ajdo](https://www.wis-tns.org/object/2026ajdo) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.40071° (84.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:15:54Z · 16 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.40071° · 84.04′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.9943041%20-7.7885912&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 239. [AT2026ajea](https://www.wis-tns.org/object/2026ajea) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.52695° (91.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:08:38Z · 14 days · 22.17 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52695° · 91.62′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajea) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.113458%203.855081&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 240. [AT2026ajef](https://www.wis-tns.org/object/2026ajef) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.28974° (77.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:12:00Z · 8 days · 22.5 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.28974° · 77.38′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajef) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.887542%20-0.331836&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 241. [AT2026ajla](https://www.wis-tns.org/object/2026ajla) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.37876° (82.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:12:28Z · 16 days · 21.76 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.37876° · 82.73′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajla) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.124667%201.959794&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 242. [AT2026ajlb](https://www.wis-tns.org/object/2026ajlb) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.75832° (105.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T17:21:07Z · 11 days · 22.99 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.75832° · 105.50′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.145083%201.777697&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 243. [AT2026ajld](https://www.wis-tns.org/object/2026ajld) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.91032° (114.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:12:57Z · 10 days · 23.02 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.91032° · 114.62′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajld) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=2.412667%202.224444&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 244. [AT2026ajle](https://www.wis-tns.org/object/2026ajle) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.84067° (110.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:43:12Z · 10 days · 23.03 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.84067° · 110.44′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajle) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=22.73875%20-1.011339&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 245. [AT2026ajlf](https://www.wis-tns.org/object/2026ajlf) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 1.30826° (78.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:53:16Z · 10 days · 22.81 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.30826° · 78.50′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.818%201.871161&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 246. [AT2026ajlg](https://www.wis-tns.org/object/2026ajlg) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.52105° (91.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:33:36Z · 8 days · 22.56 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52105° · 91.26′ |
| Catalog description | IC 5152 is an irregular galaxy 5.8 million light-years from Earth in the constellation Indus. It was discovered by DeLisle Stewart in 1908. It is an open question as to whether it is an outlying member of the Local Group. It is one of the easiest galaxies to resolve into stars, but there is a bright foreground star right in front of it that makes deep observations difficult. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1757 has the different designation IC 5152 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.776333%20-0.491842&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 247. [AT2026ajli](https://www.wis-tns.org/object/2026ajli) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.32202° (79.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 8 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.32202° · 79.32′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajli) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.584625%204.363206&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 248. [AT2026ajnc](https://www.wis-tns.org/object/2026ajnc) near NGC205

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC205 as this object's host. The 1.21009° (72.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:20:38Z · 8 days · 21.47 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.21009° · 72.61′ |
| Catalog description | Messier 110, or M110, also known as NGC 205, is a dwarf elliptical galaxy that is a satellite of the Andromeda Galaxy in the Local Group. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.001917%2042.893572&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 249. [AT2026ajnt](https://www.wis-tns.org/object/2026ajnt) near NGC2859

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2859 as this object's host. The 1.90673° (114.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T21:51:50Z · 12 days · 20.27 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.90673° · 114.40′ |
| Catalog description | NGC 2859 is a barred lenticular galaxy located some 83 million light years away in the constellation Leo Minor. The morphological classification is (R)SB(r)0+, where the S0+ notation indicates a well-defined physical structure that is lacking in visible spiral arms. It has a strong bar (B) of the "ansae" type, which means it grows brighter or wider toward the tips. A faint, secondary bar is positioned at nearly a right angle to the main bar. These features are surrounded by a weak inner ring (r) that appears diffuse. The outer region of the galaxy hosts a prominent, detached ring (R) that includes a series of blue-hued knots along the eastern side. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=143.157917%2033.700206&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 250. [AT2026ajnu](https://www.wis-tns.org/object/2026ajnu) near IC 189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 189 as this object's host. The 1.32564° (79.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:32:38Z · 11 days · 21.73 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.32564° · 79.54′ |
| Catalog description | NGC 2685 is a lenticular and polar ring Seyfert Type 2 galaxy in the constellation Ursa Major. Its velocity with respect to the cosmic microwave background is 1003 ± 9 km/s, which corresponds to a Hubble distance of 48.2 ± 3.4 Mly (14.79 ± 1.05 Mpc). Additionally, eight non-redshift measurements give a distance of 42.56 ± 3.01 Mly (13.050 ± 0.924 Mpc). It was discovered by German astronomer Wilhelm Tempel on 18 August 1882. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 189 has the different designation NGC 2685 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.8415%2023.135903&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 251. [AT2026ajpc](https://www.wis-tns.org/object/2026ajpc) near NGC 1954

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 1954 as this object's host. The 1.01085° (60.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T22:23:40Z · 16 days · 20.3 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.01085° · 60.65′ |
| Catalog description | NGC 1954 is a large spiral galaxy in the constellation of Lepus. Its velocity with respect to the cosmic microwave background is 3,172 ± 4 km/s, which corresponds to a Hubble distance of 46.8 ± 3.3 Mpc Mpc. It was discovered by German-British astronomer William Herschel on 14 December 1786. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.602768%2017.102647&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 252. [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 1.68238° (100.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:03:21Z · 14 days · 21.43 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC925** · `NGC925` |
| Catalog display name | NGC925 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 10.1 · 10.72′ × 5.75′ |
| Distance | — |
| Separation | 1.68238° · 100.94′ |
| Catalog description | NGC 925 is a barred spiral galaxy located about 30 million light-years away in the constellation Triangulum. German-British astronomer William Herschel discovered this galaxy on 13 September 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=38.730667%2034.130586&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 253. [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) near IC509

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC509 as this object's host. The 1.28504° (77.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:23:02Z · 11 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.28504° · 77.10′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) large, diffused, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.391208%2022.859219&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 254. [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) near UFO Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify UFO Galaxy as this object's host. The 1.99519° (119.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:34:33Z · 11 days · 21.32 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **UFO Galaxy** · `NGC2683` |
| Catalog display name | UFO Galaxy |
| Type / constellation | Galaxy · Lynx |
| Catalog magnitude / angular size | 9.7 · 9.48′ × 2.7′ |
| Distance | — |
| Separation | 1.99519° · 119.71′ |
| Catalog description | NGC 2683 is a field spiral galaxy in the northern constellation of Lynx. It was nicknamed the "UFO Galaxy" by the Astronaut Memorial Planetarium and Observatory. It was discovered by the astronomer William Herschel on February 5, 1788. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=130.999375%2032.60595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 255. [AT2026ajty](https://www.wis-tns.org/object/2026ajty) near IC2378

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2378 as this object's host. The 1.21289° (72.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:37:26Z · 11 days · 21.65 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.21289° · 72.77′ |
| Catalog description | faint, small in angular size, round, gradually little (adv.); long (adj.) brighter middle, or in the middle, resolvable (mottled, not resolved) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajty) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=128.187417%2031.234717&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 256. [AT2026ajug](https://www.wis-tns.org/object/2026ajug) near IC1525

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1525 as this object's host. The 1.31062° (78.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:17:45Z · 8 days · 21.26 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1525** · `IC1525` |
| Catalog display name | IC1525 |
| Type / constellation | Galaxy · Andromeda |
| Catalog magnitude / angular size | 13.2 · 1.79′ × 1.24′ |
| Distance | — |
| Separation | 1.31062° · 78.64′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajug) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.614083%2046.454214&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 257. [SN2026aaee](https://www.wis-tns.org/object/2026aaee) near IC 2360

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
| Discovery | 2026-08-30T12:21:48Z · 77 days · 17.12 r |
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

### 258. [AT2026aiwn](https://www.wis-tns.org/object/2026aiwn) near NGC56

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC56 as this object's host. The 1.79121° (107.47′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T03:57:19Z · 7 days · 20.08 r |
| Latest public photometry | Not available in the staged feed |
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

### 259. [AT2026aixc](https://www.wis-tns.org/object/2026aixc) near IC5383

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5383 as this object's host. The 1.16692° (70.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:18:42Z · 6 days · 20.38 L |
| Latest public photometry | Not available in the staged feed |
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

### 260. [AT2026aixy](https://www.wis-tns.org/object/2026aixy) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 1.08009° (64.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:19:01Z · 7 days · 20.58 r |
| Latest public photometry | Not available in the staged feed |
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

### 261. [AT2026aiys](https://www.wis-tns.org/object/2026aiys) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.74747° (104.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:48:30Z · 6 days · 19.55 L |
| Latest public photometry | Not available in the staged feed |
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

### 262. [AT2026aiyz](https://www.wis-tns.org/object/2026aiyz) near IC229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC229 as this object's host. The 1.20798° (72.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T09:13:20Z · 7 days · 20.43 w |
| Latest public photometry | Not available in the staged feed |
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

### 263. [AT2026ajlo](https://www.wis-tns.org/object/2026ajlo) near NGC7565

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7565 as this object's host. The 1.97938° (118.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:24:28Z · 7 days · 22.65 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97938° · 118.76′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.671625%201.333197&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 264. [AT2026ajlt](https://www.wis-tns.org/object/2026ajlt) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.25864° (75.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:19:40Z · 5 days · 22.76 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.25864° · 75.52′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=17.935917%203.253481&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 265. [AT2026ajma](https://www.wis-tns.org/object/2026ajma) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 1.52330° (91.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:36:00Z · 4 days · 22.33 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52330° · 91.40′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajma) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.601167%20-1.081336&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 266. [AT2026ajne](https://www.wis-tns.org/object/2026ajne) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.30710° (78.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:52:19Z · 6 days · 21.45 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.30710° · 78.43′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajne) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.3475%2041.237222&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 267. [AT2026ajng](https://www.wis-tns.org/object/2026ajng) near IC2350

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2350 as this object's host. The 1.54892° (92.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:41:16Z · 6 days · 20.81 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2350** · `IC2350` |
| Catalog display name | IC2350 |
| Type / constellation | Nebula · Cancer |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.54892° · 92.94′ |
| Catalog description | very faint, small in angular size, gradually brighter middle, or in the middle nucleus, or to a nucleus, bright a single star suddenly (abruptly) / south |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajng) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.268375%2021.094431&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 268. [AT2026ajob](https://www.wis-tns.org/object/2026ajob) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.67540° (100.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:16Z · 2 days · 22.59 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.67540° · 100.52′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajob) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.5068697%20-4.2562921&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 269. [AT2026ajou](https://www.wis-tns.org/object/2026ajou) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.43468° (86.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T20:16:00Z · 3 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.43468° · 86.08′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajou) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=341.166179%209.729107&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 270. [AT2026ajpi](https://www.wis-tns.org/object/2026ajpi) near NGC7526

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7526 as this object's host. The 1.96789° (118.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T00:22:48Z · 3 days · 22.62 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7526** · `NGC7526` |
| Catalog display name | NGC7526 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.96789° · 118.07′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.587677%20-11.187977&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 271. [AT2026ajpy](https://www.wis-tns.org/object/2026ajpy) near Messier 30 (M30)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 30 (M30) as this object's host. The 1.04427° (62.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T02:12:03Z · 4 days · 21.42 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Messier 30 (M30)** · `M30` |
| Catalog display name | Messier 30 (M30) |
| Type / constellation | Globular cluster · Capricornus |
| Catalog magnitude / angular size | 7.2 · 11′ × 11′ |
| Distance | 8.002 kpc |
| Separation | 1.04427° · 62.66′ |
| Catalog description | Messier 30 is a globular cluster of stars in the southeast of the southern constellation of Capricornus, at about the declination of the Sun when the latter is at December solstice. It was discovered by the French astronomer Charles Messier in 1764, who described it as a circular nebula without a star. In the New General Catalogue, compiled during the 1880s, it was described as a "remarkable globular, bright, large, slightly oval." It can be easily viewed with a pair of 10×50 binoculars, forming a patch of hazy light some 4 arcminutes wide that is slightly elongated along the east–west axis. With a larger instrument, individual stars can be resolved and the cluster will cover an angle of up to 12 arcminutes across graduating into a compressed core about one arcminute wide that has further star density within. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=324.0626086%20-23.61251&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 272. [AT2026ajqb](https://www.wis-tns.org/object/2026ajqb) near Messier 72 (M72)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 72 (M72) as this object's host. The 1.44459° (86.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:25:56Z · 1 days · 21.61 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Messier 72 (M72)** · `M72` |
| Catalog display name | Messier 72 (M72) |
| Type / constellation | Globular cluster · Aquarius |
| Catalog magnitude / angular size | 9.3 · 5.9′ × 5.9′ |
| Distance | 16.986 kpc |
| Separation | 1.44459° · 86.68′ |
| Catalog description | Messier 72 is a globular cluster in the south west of the very mildly southern constellation of Aquarius. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=312.9253756%20-13.9099563&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 273. [AT2026ajqn](https://www.wis-tns.org/object/2026ajqn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.39431° (83.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T03:20:11Z · 1 days · 22.45 z |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.39431° · 83.66′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajqn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.782396%20-5.67858&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 274. [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) near NGC3578

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3578 as this object's host. The 1.46782° (88.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T05:54:36Z · 0 days · 19.77 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.46782° · 88.07′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=167.991129%20-14.482202&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 275. [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) near NGC728

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC728 as this object's host. The 1.25970° (75.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:32:09Z · 7 days · 22.88 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.25970° · 75.58′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.1305%203.020175&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 276. [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) near NGC3387

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3387 as this object's host. The 1.71033° (102.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:37:55Z · 7 days · 21.48 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.71033° · 102.62′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.638125%204.019469&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 277. [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.30353° (78.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T00:31:47Z · 5 days · 21.8 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.30353° · 78.21′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajuq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.621221%20-6.694867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 278. [AT2026ajur](https://www.wis-tns.org/object/2026ajur) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.05093° (63.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 23.23 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.05093° · 63.06′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajur) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.0758218%20-10.8047935&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 279. [AT2026ajve](https://www.wis-tns.org/object/2026ajve) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.56732° (94.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 22.03 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.56732° · 94.04′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajve) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.1549298%20-14.8175025&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 280. [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.82559° (109.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 21.75 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.82559° · 109.54′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=332.432013%20-15.5483599&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 281. [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.62885° (97.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 0 days · 22.52 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.62885° · 97.73′ |
| Catalog description | extremely, excessively faint, a star of 10th magnitude south following 1' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.2593456%20-5.9647412&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 282. [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.34031° (80.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 0 days · 21.84 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.34031° · 80.42′ |
| Catalog description | extremely, excessively faint (not found again) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.2771689%20-15.020363&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 283. [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.88540° (113.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 0 days · 20.66 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.88540° · 113.12′ |
| Catalog description | extremely, excessively faint, a star of 10th magnitude south following 1' |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.010207%20-6.0313848&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 284. [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.21470° (72.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 0 days · 21.83 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.21470° · 72.88′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajvz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.0094775%20-4.3567437&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 285. [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.66580° (99.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:27:24Z · 0 days · 21.12 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.66580° · 99.95′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.552342%20-10.1312445&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 286. [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.17313° (70.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 0 days · 21.76 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.17313° · 70.39′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=330.4845008%20-12.0155785&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 287. [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.74562° (104.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:07:47Z · 6 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.74562° · 104.74′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.096358%20-3.912106&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 288. [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) near NGC1498

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1498 as this object's host. The 1.41273° (84.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T17:26:25Z · 6 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.41273° · 84.76′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.852439%20-12.76826&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 289. [AT2026aias](https://www.wis-tns.org/object/2026aias) near IC333

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC333 as this object's host. The 0.69484° (41.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:13:26Z · 16 days · 20.04 L |
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

### 290. [AT2026aiat](https://www.wis-tns.org/object/2026aiat) near Collinder 163 (CR163)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 163 (CR163) as this object's host. The 0.39277° (23.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:14Z · 14 days · 19.61 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4427....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4427....1O/abstract) |
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
| Separation | 0.39277° · 23.57′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiat) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=116.8247933%20-21.6406533&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 291. [AT2026aihc](https://www.wis-tns.org/object/2026aihc) near NGC7666

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7666 as this object's host. The 0.34612° (20.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T10:42:55Z · 17 days · 20.27 L |
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

### 292. [AT2026aiko](https://www.wis-tns.org/object/2026aiko) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38092° (22.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:02:26Z · 9 days · 19.85 r |
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
| Subject | **NGC7158** · `NGC7158` |
| Catalog display name | NGC7158 |
| Type / constellation | Nebula · Capricornus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.38092° · 22.86′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiko) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.403672%20-11.2133422&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 293. [SN2026airg](https://www.wis-tns.org/object/2026airg) near Sharpless 260 (SH2-260)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 260 (SH2-260) as this object's host. The 1.20103° (72.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.029 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T09:34:22Z · 8 days · 19.93 r |
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
| Subject | **Sharpless 260 (SH2-260)** · `SH2-260` |
| Catalog display name | Sharpless 260 (SH2-260) |
| Type / constellation | HII · Orion |
| Catalog magnitude / angular size | — · 22′ × 22′ |
| Distance | — |
| Separation | 1.20103° · 72.06′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026airg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=72.9951006%206.5875963&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 294. [AT2026aivj](https://www.wis-tns.org/object/2026aivj) near IC1547

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1547 as this object's host. The 0.56558° (33.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T08:18:10Z · 10 days · 20.47 g |
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
| Subject | **IC1547** · `IC1547` |
| Catalog display name | IC1547 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.56558° · 33.93′ |
| Catalog description | eF.pS, suddenly (abruptly) / south brighter middle, or in the middle a single star |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aivj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.9513462%2022.7451069&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 295. [AT2026aiwl](https://www.wis-tns.org/object/2026aiwl) near IC5344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5344 as this object's host. The 0.90611° (54.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T10:43:03Z · 9 days · 20.35 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.60002%20-4.513882&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 296. [AT2026aiws](https://www.wis-tns.org/object/2026aiws) near Collinder 59 (CR59)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 59 (CR59) as this object's host. The 0.80866° (48.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T09:40:03Z · 10 days · 20.91 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiws) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.9234498%2016.1716185&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 297. [AT2026aixd](https://www.wis-tns.org/object/2026aixd) near NGC7826

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7826 as this object's host. The 0.88575° (53.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T09:57:26Z · 10 days · 20 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.463425%20-21.049051&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 298. [AT2026aixn](https://www.wis-tns.org/object/2026aixn) near NGC2531

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2531 as this object's host. The 0.88316° (52.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T12:09:20Z · 28 days · 20.95 g |
| Latest public photometry | Not available in the staged feed |
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

### 299. [AT2026aixq](https://www.wis-tns.org/object/2026aixq) near Hind's variable nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Hind's variable nebula as this object's host. The 0.75249° (45.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T09:11:25Z · 27 days · 20.62 r |
| Latest public photometry | Not available in the staged feed |
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

### 300. [AT2026ajan](https://www.wis-tns.org/object/2026ajan) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.77578° (46.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T17:03:50Z · 11 days · 22.15 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajan) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.079042%20-0.028278&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 301. [AT2026ajbi](https://www.wis-tns.org/object/2026ajbi) near Barnard 215 (B215)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Barnard 215 (B215) as this object's host. The 0.54619° (32.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T07:26:44Z · 6 days · 20.84 r |
| Latest public photometry | Not available in the staged feed |
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

### 302. [AT2026ajdc](https://www.wis-tns.org/object/2026ajdc) near IC240

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC240 as this object's host. The 0.55882° (33.53′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T05:13:05Z · 12 days · 19.73 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=39.4326826%2042.228844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 303. [AT2026ajdy](https://www.wis-tns.org/object/2026ajdy) near NGC272

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC272 as this object's host. The 0.82818° (49.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T06:13:04Z · 8 days · 20.06 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.82818° · 49.69′ |
| Catalog description | NGC 272 is an open cluster located in the constellation Andromeda. It was discovered on August 2, 1864, by Heinrich d'Arrest. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=13.4080957%2036.5188342&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 304. [AT2026ajmh](https://www.wis-tns.org/object/2026ajmh) near IC1665

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1665 as this object's host. The 0.81988° (49.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T19:20:38Z · 27 days · 21.78 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1665** · `IC1665` |
| Catalog display name | IC1665 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.81988° · 49.19′ |
| Catalog description | faint, very small in angular size, round, like 2 or 3 faint stars (pl.) irregular north nebula |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.946417%2033.999694&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 305. [AT2026ajmi](https://www.wis-tns.org/object/2026ajmi) near NGC843

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC843 as this object's host. The 0.79289° (47.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T21:30:14Z · 27 days · 21.94 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.79289° · 47.57′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.892958%2031.856081&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 306. [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) near Lynds Bright Nebula 439 (LBN439)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 439 (LBN439) as this object's host. The 0.79678° (47.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T19:43:55Z · 3 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 439 (LBN439)** · `LBN439` |
| Catalog display name | Lynds Bright Nebula 439 (LBN439) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 28′ × 6′ |
| Distance | — |
| Separation | 0.79678° · 47.81′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajsh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.351332%2028.491949&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 307. [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) near IC111

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC111 as this object's host. The 0.80147° (48.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:48:00Z · 8 days · 22.16 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC111** · `IC111` |
| Catalog display name | IC111 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.80147° · 48.09′ |
| Catalog description | IC 349, also known as Barnard's Merope Nebula, is a nebula which lies 3500 AUs from the star Merope in the Pleiades cluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajuh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.962083%2034.200733&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 308. [AT2026ajup](https://www.wis-tns.org/object/2026ajup) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 0.84314° (50.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:27:50Z · 12 days · 21.25 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.84314° · 50.59′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajup) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=101.017167%2041.366625&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 309. [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.53340° (32.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 15 days · 23.8 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.53340° · 32.00′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.525804%20-6.026658&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 310. [AT2026ahhj](https://www.wis-tns.org/object/2026ahhj) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.72039° (103.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:23:06Z · 16 days · 22.31 r |
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
| Subject | **NGC7453** · `NGC7453` |
| Catalog display name | NGC7453 |
| Type / constellation | Nebula · Aquarius |
| Catalog magnitude / angular size | — · 0.3′ × 0.3′ |
| Distance | — |
| Separation | 1.72039° · 103.22′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahhj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.0734215%20-6.5597035&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 311. [AT2026aies](https://www.wis-tns.org/object/2026aies) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.74650° (104.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T06:01:28Z · 10 days · 21.09 i |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aies) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=52.7613763%20-27.5471983&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 312. [AT2026aijr](https://www.wis-tns.org/object/2026aijr) near NGC7447

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7447 as this object's host. The 1.89133° (113.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:48:34Z · 11 days · 20.08 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aijr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.7027508%20-12.3273564&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 313. [AT2026aila](https://www.wis-tns.org/object/2026aila) near NGC2586

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2586 as this object's host. The 1.95903° (117.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T17:46:45Z · 10 days · 19.91 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aila) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.800004%20-4.535484&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 314. [AT2026airk](https://www.wis-tns.org/object/2026airk) near IC 71

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 71 as this object's host. The 1.00378° (60.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T10:51:34Z · 8 days · 20.12 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026airk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.266447%20-7.1465927&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 315. [AT2026aivl](https://www.wis-tns.org/object/2026aivl) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.27407° (76.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:42:43Z · 14 days · 22.36 r |
| Latest public photometry | Not available in the staged feed |
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

### 316. [AT2026aivm](https://www.wis-tns.org/object/2026aivm) near NGC728

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC728 as this object's host. The 1.63081° (97.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T14:06:43Z · 16 days · 21.89 r |
| Latest public photometry | Not available in the staged feed |
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

### 317. [AT2026aiwa](https://www.wis-tns.org/object/2026aiwa) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 1.45584° (87.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T15:44:38Z · 8 days · 22.37 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.994292%20-1.052686&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 318. [AT2026aiwg](https://www.wis-tns.org/object/2026aiwg) near IC323

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC323 as this object's host. The 1.25852° (75.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:53:59Z · 10 days · 20.6 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.0483718%2042.0988238&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 319. [AT2026aiwh](https://www.wis-tns.org/object/2026aiwh) near Lynds Bright Nebula 434 (LBN434)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 434 (LBN434) as this object's host. The 1.66663° (100.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T10:04:55Z · 6 days · 19.85 L |
| Latest public photometry | Not available in the staged feed |
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

### 320. [AT2026aiwm](https://www.wis-tns.org/object/2026aiwm) near IC2940

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2940 as this object's host. The 1.28946° (77.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T12:59:13Z · 9 days · 20.09 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=173.7547524%2023.2296939&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 321. [AT2026aixk](https://www.wis-tns.org/object/2026aixk) near NGC1037

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1037 as this object's host. The 1.03553° (62.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T09:28:57Z · 26 days · 20.78 g |
| Latest public photometry | Not available in the staged feed |
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

### 322. [AT2026aixt](https://www.wis-tns.org/object/2026aixt) near IC640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC640 as this object's host. The 1.79762° (107.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:27:34Z · 11 days · 19.6 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.5238562%2034.6786725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 323. [AT2026aiym](https://www.wis-tns.org/object/2026aiym) near Robin's Egg Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Robin's Egg Nebula as this object's host. The 1.48879° (89.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T07:11:26Z · 16 days · 20.49 i |
| Latest public photometry | Not available in the staged feed |
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

### 324. [AT2026aiyn](https://www.wis-tns.org/object/2026aiyn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.63394° (98.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:13:22Z · 16 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 325. [AT2026aiyq](https://www.wis-tns.org/object/2026aiyq) near Melotte 53 (MEL53)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Melotte 53 (MEL53) as this object's host. The 1.83617° (110.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T15:30:53Z · 9 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiyq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.50063%20-34.481664&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 326. [AT2026aize](https://www.wis-tns.org/object/2026aize) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.94668° (116.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:22:29Z · 16 days · 20.61 i |
| Latest public photometry | Not available in the staged feed |
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

### 327. [AT2026ajbc](https://www.wis-tns.org/object/2026ajbc) near IC1707

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1707 as this object's host. The 1.73198° (103.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T20:55:40Z · 17 days · 21.19 g |
| Latest public photometry | Not available in the staged feed |
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

### 328. [AT2026ajcx](https://www.wis-tns.org/object/2026ajcx) near IC337

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC337 as this object's host. The 1.86545° (111.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:11:24Z · 12 days · 20.12 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajcx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.7424687%20-8.5260573&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 329. [AT2026ajde](https://www.wis-tns.org/object/2026ajde) near NGC2875

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2875 as this object's host. The 1.32058° (79.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T11:29:06Z · 10 days · 19.71 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajde) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=140.1027718%2011.449902&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 330. [AT2026ajdm](https://www.wis-tns.org/object/2026ajdm) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 1.32204° (79.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:54:36Z · 16 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.32204° · 79.32′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.5231317%20-1.4754369&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 331. [AT2026ajeq](https://www.wis-tns.org/object/2026ajeq) near NGC2284

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2284 as this object's host. The 1.44095° (86.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-22T21:14:24Z · 24 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.44095° · 86.46′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajeq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.703167%2034.022239&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 332. [AT2026ajet](https://www.wis-tns.org/object/2026ajet) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.97492° (118.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T20:41:16Z · 20 days · 20.96 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97492° · 118.50′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajet) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=102.315167%2039.1128&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 333. [AT2026ajev](https://www.wis-tns.org/object/2026ajev) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.73662° (104.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T20:21:07Z · 14 days · 21.31 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.73662° · 104.20′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajev) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.32475%2042.225144&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 334. [AT2026ajfn](https://www.wis-tns.org/object/2026ajfn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.16150° (69.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:13:02Z · 16 days · 23.14 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.16150° · 69.69′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajfn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.2979196%20-5.1064445&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 335. [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.09787° (65.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:01:26Z · 9 days · 20.91 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.09787° · 65.87′ |
| Catalog description | NGC 2419 is a globular cluster in the constellation Lynx. It was discovered by William Herschel on December 31, 1788. NGC 2419 is at a distance of about 300,000 light years from the Solar System and at the same distance from the Galactic Center. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.167542%2038.601739&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 336. [AT2026ajkm](https://www.wis-tns.org/object/2026ajkm) near Lynds Bright Nebula 418 (LBN418)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 418 (LBN418) as this object's host. The 1.03018° (61.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:42:43Z · 5 days · 21.9 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.03018° · 61.81′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajkm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.185833%2024.616978&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 337. [AT2026ajkq](https://www.wis-tns.org/object/2026ajkq) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.80188° (108.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T17:25:26Z · 19 days · 20.77 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.80188° · 108.11′ |
| Catalog description | a star of 13th magnitude with nebula, chiefly north north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.098375%202.557453&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 338. [AT2026ajlq](https://www.wis-tns.org/object/2026ajlq) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.81927° (109.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:07Z · 5 days · 22.86 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.81927° · 109.16′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajlq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.234208%201.764594&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 339. [AT2026ajmr](https://www.wis-tns.org/object/2026ajmr) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.15457° (69.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:10:33Z · 12 days · 21.98 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.15457° · 69.27′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.111917%2055.545942&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 340. [AT2026ajmw](https://www.wis-tns.org/object/2026ajmw) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.42390° (85.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:26:52Z · 9 days · 21.36 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.42390° · 85.43′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.907333%2055.297133&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 341. [AT2026ajnh](https://www.wis-tns.org/object/2026ajnh) near Goblet of Fire nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Goblet of Fire nebula as this object's host. The 1.85337° (111.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:45:36Z · 5 days · 20.62 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Goblet of Fire nebula** · `StDr56` |
| Catalog display name | Goblet of Fire nebula |
| Type / constellation | Planetary nebula · Tri |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.85337° · 111.20′ |
| Catalog description | Constance Elaine Trimmer "Connie" Willis is an American science fiction and fantasy writer. She has won more major genre awards than any other writer, including eleven Hugo Awards and seven Nebula Awards. Most recently, she won the "Best Novel" Hugo and Nebula Awards for Blackout/All Clear (2010). She was inducted by the Science Fiction Hall of Fame in 2009 and the Science Fiction Writers of America named her its 28th SFWA Grand Master in 2011. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajnh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.086167%2028.604156&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 342. [AT2026ajnw](https://www.wis-tns.org/object/2026ajnw) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.48474° (89.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:25:26Z · 9 days · 20.74 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.48474° · 89.08′ |
| Catalog description | NGC 2281, also known as the Broken Heart Cluster, is an open cluster of stars in the northern constellation of Auriga. It was discovered by English astronomer William Herschel on March 4, 1788, and described as a, "cluster of coarsely scattered pretty [bright] stars, pretty rich". The Trumpler class for NGC 2281 is I3p, indicating a poor (p) but compact (I) grouping with a wide range of brightness (3). It is located at a distance of approximately 1,720 ly from the Sun and is 630–661 million years old. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajnw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=101.705875%2039.620406&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 343. [AT2026ajom](https://www.wis-tns.org/object/2026ajom) near Lynds Bright Nebula 968 (LBN968)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 968 (LBN968) as this object's host. The 1.64919° (98.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T09:01:19Z · 4 days · 20.3 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 968 (LBN968)** · `LBN968` |
| Catalog display name | Lynds Bright Nebula 968 (LBN968) |
| Type / constellation | HII · Eridanus |
| Catalog magnitude / angular size | — · 20′ × 12′ |
| Distance | — |
| Separation | 1.64919° · 98.95′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajom) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=73.6800879%20-8.3591447&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 344. [AT2026ajpe](https://www.wis-tns.org/object/2026ajpe) near IC2069

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2069 as this object's host. The 1.57505° (94.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T06:43:05Z · 10 days · 23.13 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2069** · `IC2069` |
| Catalog display name | IC2069 |
| Type / constellation | Nebula · Caelum |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.57505° · 94.50′ |
| Catalog description | most extremely faint, small in angular size, round, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpe) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=64.844135%20-47.084908&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 345. [AT2026ajpl](https://www.wis-tns.org/object/2026ajpl) near IC5344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5344 as this object's host. The 1.63978° (98.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:05:52Z · 8 days · 21.06 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.63978° · 98.39′ |
| Catalog description | very faint, large, others near |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.32232%20-6.532331&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 346. [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) near Lynds Bright Nebula 484 (LBN484)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 484 (LBN484) as this object's host. The 1.74355° (104.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:18:12Z · 1 days · 19.58 cyan |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.74355° · 104.61′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajrp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.9083033%2030.683525&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 347. [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) near Lynds Bright Nebula 856 (LBN856)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 856 (LBN856) as this object's host. The 1.86922° (112.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T11:55:40Z · 3 days · 19.74 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.86922° · 112.15′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajsa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.856869%20-9.588252&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 348. [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.48459° (89.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T14:25:26Z · 9 days · 23.61 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.48459° · 89.08′ |
| Catalog description | suspected (13.5 mag) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.657708%20-0.414844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 349. [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) near NGC737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC737 as this object's host. The 1.51249° (90.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T19:37:55Z · 12 days · 21.87 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.51249° · 90.75′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.431083%2034.134442&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 350. [AT2026ajub](https://www.wis-tns.org/object/2026ajub) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.29090° (77.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T21:28:48Z · 10 days · 21.61 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.29090° · 77.45′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajub) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.972167%2031.931817&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 351. [AT2026aigg](https://www.wis-tns.org/object/2026aigg) near Lynds Bright Nebula 910 (LBN910)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 910 (LBN910) as this object's host. The 0.77477° (46.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:05:05Z · 13 days · 20.26 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4451....1P](https://ui.adsabs.harvard.edu/abs/2026TNSTR4451....1P/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 910 (LBN910)** · `LBN910` |
| Catalog display name | Lynds Bright Nebula 910 (LBN910) |
| Type / constellation | HII · Orion |
| Catalog magnitude / angular size | — · 45′ × 10′ |
| Distance | — |
| Separation | 0.77477° · 46.49′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aigg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=76.7938003%20-2.4198909&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 352. [AT2026ajts](https://www.wis-tns.org/object/2026ajts) near Lynds Bright Nebula 891 (LBN891)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 891 (LBN891) as this object's host. The 0.64768° (38.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:48:00Z · 12 days · 20.91 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 891 (LBN891)** · `LBN891` |
| Catalog display name | Lynds Bright Nebula 891 (LBN891) |
| Type / constellation | HII · Gemini |
| Catalog magnitude / angular size | — · 120′ × 120′ |
| Distance | — |
| Separation | 0.64768° · 38.86′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajts) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=107.303542%2016.247308&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 353. [SN2026aeff](https://www.wis-tns.org/object/2026aeff) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 33/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.95543° (117.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.082674911233642 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T12:30:18Z · 45 days · 19.25 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4002....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4002....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2207 / IC 2163** · `IC 2441` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | CiG · Cnc |
| Catalog magnitude / angular size | — · 0.9′ × 87.65′ |
| Distance | 81 ly |
| Separation | 1.95543° · 117.33′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeff) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=136.3534311%2021.2177022&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 354. [AT2026absv](https://www.wis-tns.org/object/2026absv) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 28/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.10562° (66.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-14T10:32:09Z · 62 days · 19.48 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3717....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3717....1O/abstract) |
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
| Separation | 1.10562° · 66.34′ |
| Catalog description | NGC 3561, also known as Arp 105, is a pair of interacting galaxies NGC 3561A and NGC 3561B within the galaxy cluster Abell 1185 in Ursa Major. It was discovered by British astronomer John Herschel on 30 March 1827. Its common name is "the Guitar" and contains a small tidal dwarf galaxy known as Ambartsumian's Knot that is believed to be the remnant of the extensive tidal tail pulled out of one of the galaxies. |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026absv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=333.6636107%20-13.6903278&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 355. [AT2026aeka](https://www.wis-tns.org/object/2026aeka) near IC 1876

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 28/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1876 as this object's host. The 0.09948° (5.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-18T18:53:26Z · 58 days · 20.21 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4009....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4009....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1876** · `IC 1876` |
| Catalog display name | NGC 575 |
| Type / constellation | Galaxy · For |
| Catalog magnitude / angular size | — · 1.16′ × 1.12′ |
| Distance | — |
| Separation | 0.09948° · 5.97′ |
| Catalog description | NGC 575  is a barred spiral galaxy of Hubble type SB(rs)c in the constellation Pisces. It is approximately 145 million light years from the Milky Way and has a diameter of about 70,000 light years. NGC 575  is a barred spiral galaxy of Hubble type SB(rs)c in the constellation Pisces. It is approximately 145 million light years from the Milky Way and has a diameter of about 70,000 light years. The object was discovered on October 17, 1876, by Édouard Stephan (listed as NGC 575) and on January 18, 1896, by Stéphane Javelle (listed as IC 1710). |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1876 has the different designation NGC 575 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeka) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=46.2357573%20-27.5033239&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 356. [AT2026aiem](https://www.wis-tns.org/object/2026aiem) near Lynds Bright Nebula 556 (LBN556)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 556 (LBN556) as this object's host. The 1.55459° (93.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T04:28:06Z · 10 days · 19.89 r |
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
| Subject | **Lynds Bright Nebula 556 (LBN556)** · `LBN556` |
| Catalog display name | Lynds Bright Nebula 556 (LBN556) |
| Type / constellation | HII · Pisces |
| Catalog magnitude / angular size | — · 60′ × 10′ |
| Distance | — |
| Separation | 1.55459° · 93.28′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiem) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.7505229%2018.4520326&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 357. [AT2026aimd](https://www.wis-tns.org/object/2026aimd) near Collinder 65 (CR65)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 65 (CR65) as this object's host. The 1.83171° (109.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:37:25Z · 9 days · 20.38 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4499....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4499....1S/abstract) |
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
| Separation | 1.83171° · 109.90′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aimd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=81.7363092%2017.4547477&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 358. [AT2026aivx](https://www.wis-tns.org/object/2026aivx) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.67357° (100.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T14:28:19Z · 8 days · 22.48 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aivx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.745625%20-1.017767&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 359. [AT2026aiwq](https://www.wis-tns.org/object/2026aiwq) near van den Bergh 61 (VDB61)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 61 (VDB61) as this object's host. The 1.44782° (86.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T11:38:15Z · 10 days · 20.72 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aiwq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=88.9949799%206.2063749&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 360. [AT2026aixl](https://www.wis-tns.org/object/2026aixl) near Lynds Bright Nebula 763 (LBN763)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 763 (LBN763) as this object's host. The 1.50403° (90.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T06:55:12Z · 12 days · 20.49 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aixl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.5135966%2020.3415483&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 361. [AT2026aixm](https://www.wis-tns.org/object/2026aixm) near Lynds Bright Nebula 828 (LBN828)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 828 (LBN828) as this object's host. The 1.46269° (87.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T07:18:54Z · 12 days · 20.73 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aixm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.1182102%209.2539029&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 362. [AT2026aizy](https://www.wis-tns.org/object/2026aizy) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.97258° (118.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T13:42:14Z · 10 days · 22.68 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026aizy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.402542%200.621142&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 363. [AT2026ajkk](https://www.wis-tns.org/object/2026ajkk) near Lynds Bright Nebula 688 (LBN688)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 688 (LBN688) as this object's host. The 1.01865° (61.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:58:04Z · 8 days · 21.78 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 688 (LBN688)** · `LBN688` |
| Catalog display name | Lynds Bright Nebula 688 (LBN688) |
| Type / constellation | HII · Aries |
| Catalog magnitude / angular size | — · 60′ × 30′ |
| Distance | — |
| Separation | 1.01865° · 61.12′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajkk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.985125%2020.598033&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 364. [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 20/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.70237° (42.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.087 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T05:00:26Z · 41 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4014....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4014....1S/abstract) |
| Classification references | [2026TNSCR4212....1G](https://ui.adsabs.harvard.edu/abs/2026TNSCR4212....1G/abstract) |
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
| Separation | 0.70237° · 42.14′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aeiu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=328.9342847%20-12.153135&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 365. [AT2026abyt](https://www.wis-tns.org/object/2026abyt) near IC2170

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 18/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2170 as this object's host. The 1.73601° (104.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T05:48:58Z · 59 days · 19.14 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3759....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3759....1O/abstract) |
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
| Separation | 1.73601° · 104.16′ |
| Catalog description | extremely, excessively faint, small in angular size, resolvable (mottled, not resolved), a star of 13th magnitude south preceding preceding (westward) / pretty (adv., before F. B. L, S) 0'.8 |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026abyt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.820667%2044.135881&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 366. [AT2026adsv](https://www.wis-tns.org/object/2026adsv) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 0.88938° (53.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T07:01:55Z · 45 days · 20.83 w |
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
| Separation | 0.88938° · 53.36′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adsv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=321.7936512%20-20.5134163&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 367. [AT2026ajax](https://www.wis-tns.org/object/2026ajax) near IC509

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC509 as this object's host. The 0.40100° (24.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T22:19:12Z · 34 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajax) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=127.619125%2024.189408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 368. [AT2026ajku](https://www.wis-tns.org/object/2026ajku) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.71371° (42.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-08T19:58:04Z · 68 days · 22.1 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.71371° · 42.82′ |
| Catalog description | NGC 488 is a face-on spiral galaxy in the constellation Pisces. It was discovered by German-British astronomer William Herschel on 13 December 1784. It is at a distance of about 90 million light-years away from Earth. Its diameter is estimated to be ~185,800 Light Years. The galaxy has a large central bulge, and is considered a prototype galaxy with multiple spiral arms. Its arms are tightly wound. Star forming activity has been traced within the arms. The nucleus of NGC 488 has been found to be chemically decoupled, being twice as metal rich as the central bulge of the galaxy. NGC 488, with the exception of its smaller companions, form the NGC 488 group; a relatively isolated galaxy group. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajku) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=20.590625%205.954869&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 369. [AT2026ajky](https://www.wis-tns.org/object/2026ajky) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 0.99165° (59.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T16:06:14Z · 37 days · 22.61 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.99165° · 59.50′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 197 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajky) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.001042%202.942992&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 370. [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 0.76155° (45.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-13T16:59:31Z · 63 days · 20.79 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC925** · `NGC925` |
| Catalog display name | NGC925 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 10.1 · 10.72′ × 5.75′ |
| Distance | — |
| Separation | 0.76155° · 45.69′ |
| Catalog description | NGC 925 is a barred spiral galaxy located about 30 million light-years away in the constellation Triangulum. German-British astronomer William Herschel discovered this galaxy on 13 September 1784. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajuo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.12775%2034.081633&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 371. [SN2026afgl](https://www.wis-tns.org/object/2026afgl) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.83228° (109.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIn |
| Redshift | 0.105 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-11T05:50:16Z · 35 days · 19.63 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4107....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4107....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Beehive cluster** · `NGC2632` |
| Catalog display name | Beehive cluster |
| Type / constellation | Open cluster · Cancer |
| Catalog magnitude / angular size | 3.1 · 108.6′ × 108.6′ |
| Distance | 0.187 kpc |
| Separation | 1.83228° · 109.94′ |
| Catalog description | (See Praesepe) |

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afgl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.9670669%2020.1705514&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 372. [AT2026aawo](https://www.wis-tns.org/object/2026aawo) near IC 1341

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1341 as this object's host. The 1.50242° (90.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-03T10:40:30Z · 73 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR3619....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR3619....1O/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1341** · `IC 1341` |
| Catalog display name | IC 342 |
| Type / constellation | Galaxy · Aqr |
| Catalog magnitude / angular size | — · 0.95′ × 0.53′ |
| Distance | 10.7 ly |
| Separation | 1.50242° · 90.15′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1341 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aawo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=313.5431497%20-14.233021&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 373. [AT2026adsx](https://www.wis-tns.org/object/2026adsx) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.56536° (93.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T07:04:43Z · 45 days · 20.67 w |
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
| Separation | 1.56536° · 93.92′ |
| Catalog description | faint, binuclear, or nebula double a single star |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026adsx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=322.4321434%20-19.6305548&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 374. [AT2026agac](https://www.wis-tns.org/object/2026agac) near IC 1417

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1417 as this object's host. The 1.74979° (104.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-10T07:53:22Z · 36 days · 20.92 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4226....1C](https://ui.adsabs.harvard.edu/abs/2026TNSTR4226....1C/abstract) |
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
| Separation | 1.74979° · 104.99′ |
| Catalog description | IC 1459 is an elliptical galaxy located in the constellation Grus. It is located at a distance of circa 85 million light-years from Earth, which, given its apparent dimensions, means that IC 1459 is about 130,000 light-years across. It was discovered by Edward Emerson Barnard in 1892. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1417 has the different designation IC 1459 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agac) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.1692309%20-14.651636&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 375. [AT2026aiyu](https://www.wis-tns.org/object/2026aiyu) near NGC1425

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1425 as this object's host. The 1.69335° (101.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-04T09:11:22Z · 72 days · 21.98 r |
| Latest public photometry | Not available in the staged feed |
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

### 376. [AT2026aiyw](https://www.wis-tns.org/object/2026aiyw) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 1.91424° (114.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-08-29T06:05:16Z · 78 days · 20.41 i |
| Latest public photometry | Not available in the staged feed |
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

### 377. [AT2026ajkn](https://www.wis-tns.org/object/2026ajkn) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 1.07935° (64.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-13T15:11:31Z · 33 days · 22.34 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1639** · `IC 1639` |
| Catalog display name | NGC5042 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.76′ × 0.7′ |
| Distance | — |
| Separation | 1.07935° · 64.76′ |
| Catalog description | NGC 5042 is an intermediate spiral galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background for is 1,697±22 km/s, which corresponds to a Hubble distance of 81.6 ± 5.8 Mly (25.03 ± 1.78 Mpc). However, 15 non redshift measurements give a much closer distance of 47.88 ± 2.37 Mly (14.680 ± 0.726 Mpc). It was discovered by British astronomer John Herschel on 25 March 1836. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1639 has the different designation NGC5042 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.93175%20-1.039408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 378. [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 1.97219° (118.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-13T02:53:11Z · 63 days · 22.85 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.97219° · 118.33′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=356.4049427%20-0.2833666&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 379. [SN2026acjc](https://www.wis-tns.org/object/2026acjc) near Lynds Dark Nebula 1648 (LDN1648)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 5/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1648 (LDN1648) as this object's host. The 1.97714° (118.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ib |
| Redshift | 0.003012 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-19T18:54:31Z · 57 days · 19.85 L |
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

### 380. [AT2026aflb](https://www.wis-tns.org/object/2026aflb) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 5/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.94348° (56.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T15:02:52Z · 37 days · 22.4 r |
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
| Subject | **NGC7668** · `NGC7668` |
| Catalog display name | NGC7668 |
| Type / constellation | Nebula · Pisces |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.94348° · 56.61′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aflb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.7755591%20-1.132748&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 381. [AT2026agwt](https://www.wis-tns.org/object/2026agwt) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.72330° (103.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T21:46:04Z · 34 days · 20.95 r |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agwt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.7860959%2040.5056762&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 382. [AT2026aixp](https://www.wis-tns.org/object/2026aixp) near Collinder 204 (CR204)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 204 (CR204) as this object's host. The 1.53361° (92.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-14T10:49:06Z · 32 days · 20.76 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aixp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.8808033%2010.4550659&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 383. [AT2026ajau](https://www.wis-tns.org/object/2026ajau) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.33313° (79.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T21:18:43Z · 34 days · 21.1 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajau) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=103.351458%2040.166439&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 384. [AT2026ajaw](https://www.wis-tns.org/object/2026ajaw) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.31677° (79.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-12T22:16:19Z · 34 days · 20.69 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajaw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=128.772208%2019.040575&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 385. [AT2026ajmg](https://www.wis-tns.org/object/2026ajmg) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.82991° (109.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T22:20:38Z · 42 days · 20.17 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.82991° · 109.79′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=116.649875%2055.67325&fov=0.5&survey=P%2FDSS2%2Fcolor)

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
