# TNS transient opportunity review — 2026-11-17

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `d77d7c2cf52bd135`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 300 review opportunities: 8 urgent, 292 watch, 0 expired
- Recommendations: 6 approve, 294 hold, 0 reject
- 300 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 669 staged rows collapsed to 645 unique TNS objects (24 duplicate/change rows)
- 0 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) | SN Ia | 15 | 16.1 | NGC4216 (Galaxy) | 0.39321° | near-field match | 100 | approve |
| urgent | [AT2026ajxw](https://www.wis-tns.org/object/2026ajxw) | transient_candidate | 2 | 18.22 | IC750 (Galaxy) | 0.12317° | near-field match | 100 | approve |
| urgent | [SN2026aicq](https://www.wis-tns.org/object/2026aicq) | SN II | 13 | 18.48 | IC 369 (Galaxy) | 0.91868° | near-field match | 97 | hold |
| urgent | [SN2026ainb](https://www.wis-tns.org/object/2026ainb) | SN Ia | 13 | 18.12 | IC 450 (Galaxy) | 1.07438° | near-field match | 90 | hold |
| urgent | [AT2026ajpr](https://www.wis-tns.org/object/2026ajpr) | transient_candidate | 7 | 18.03 | NGC3945 (Galaxy) | 0.86986° | near-field match | 90 | approve |
| urgent | [AT2026ajrb](https://www.wis-tns.org/object/2026ajrb) | transient_candidate | 4 | 18.48 | IC5270 (Galaxy) | 1.73389° | near-field match | 83 | approve |
| urgent | [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) | transient_candidate | 3 | 18.22 | IC765 (Nebula) | 0.75222° | near-field match | 80 | approve |
| urgent | [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) | transient_candidate | 9 | 18.38 | IC656 (Nebula) | 0.87219° | near-field match | 72 | approve |
| watch | [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) | transient_candidate | 4 | 19.32 | NGC2276 (Galaxy) | 0.19202° | near-field match | 93 | hold |
| watch | [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) | SN II | 16 | 18.71 | IC 3 (Spiral galaxy) | 0.47363° | near-field match | 87 | hold |
| watch | [SN2026ahze](https://www.wis-tns.org/object/2026ahze) | SN Ia | 14 | 18.71 | NGC797 (Galaxy) | 1.92287° | near-field match | 80 | hold |
| watch | [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) | transient_candidate | 4 | 19.37 | NGC2549 (Galaxy) | 0.59331° | near-field match | 80 | hold |
| watch | [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) | transient_candidate | 4 | 19.35 | NGC2768 (Galaxy) | 0.41880° | near-field match | 80 | hold |
| watch | [AT2026ajxv](https://www.wis-tns.org/object/2026ajxv) | transient_candidate | 3 | 19.13 | NGC 3277 (Galaxy) | 0.80128° | near-field match | 80 | hold |
| watch | [AT2026ajdq](https://www.wis-tns.org/object/2026ajdq) | transient_candidate | 7 | 19.19 | IC 1600 (Galaxy) | 1.96019° | near-field match | 73 | hold |
| watch | [AT2026ajig](https://www.wis-tns.org/object/2026ajig) | transient_candidate | 5 | 19.78 | IC 38 (Galaxy) | 0.00569° | near-field match | 73 | hold |
| watch | [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) | transient_candidate | 5 | 19.46 | NGC1169 (Galaxy) | 1.01800° | near-field match | 73 | hold |
| watch | [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) | transient_candidate | 5 | 18.82 | NGC 3294 (Galaxy) | 1.51592° | near-field match | 73 | hold |
| watch | [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) | transient_candidate | 5 | 19 | IC486 (Galaxy) | 1.22917° | near-field match | 73 | hold |
| watch | [AT2026ajoo](https://www.wis-tns.org/object/2026ajoo) | transient_candidate | 4 | 22.76 | IC2058 (Galaxy) | 0.00834° | near-field match | 73 | hold |
| watch | [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) | transient_candidate | 3 | 19.45 | IC1733 (Galaxy) | 1.11166° | near-field match | 73 | hold |
| watch | [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) | transient_candidate | 4 | 19.27 | IC5261 (Galaxy) | 1.21834° | near-field match | 73 | hold |
| watch | [AT2026ajva](https://www.wis-tns.org/object/2026ajva) | transient_candidate | 2 | 21.81 | NGC 3561 (Galaxy) | 0.19660° | near-field match | 73 | hold |
| watch | [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) | transient_candidate | 2 | 22.15 | NGC 3561 (Galaxy) | 0.19359° | near-field match | 73 | hold |
| watch | [AT2026ajyd](https://www.wis-tns.org/object/2026ajyd) | transient_candidate | 1 | 19.16 | IC600 (Galaxy) | 1.36887° | near-field match | 73 | hold |
| watch | [AT2026akaz](https://www.wis-tns.org/object/2026akaz) | transient_candidate | 1 | 19.3 | Caldwell 3 (C3) (Galaxy) | 1.12593° | near-field match | 73 | hold |
| watch | [AT2026agub](https://www.wis-tns.org/object/2026agub) | transient_candidate | 23 | 19.46 | Andromeda Galaxy (Galaxy) | 0.34859° | near-field match | 72 | hold |
| watch | [AT2026ajdx](https://www.wis-tns.org/object/2026ajdx) | transient_candidate | 9 | 19.5 | IC2160 (Galaxy) | 0.65192° | near-field match | 72 | hold |
| watch | [AT2026ajmb](https://www.wis-tns.org/object/2026ajmb) | transient_candidate | 6 | 19.13 | IC 1623 (CiG) | 0.67085° | near-field match | 70 | hold |
| watch | [AT2026agye](https://www.wis-tns.org/object/2026agye) | transient_candidate | 21 | 19.16 | IC 5124 (Galaxy) | 1.51433° | near-field match | 65 | hold |
| watch | [AT2026ajko](https://www.wis-tns.org/object/2026ajko) | transient_candidate | 16 | 22.23 | NGC864 (Galaxy) | 0.13264° | near-field match | 65 | hold |
| watch | [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) | transient_candidate | 5 | 18.5 | Lynds Bright Nebula 1043 (LBN1043) (HII) | 1.49482° | near-field match | 65 | hold |
| watch | [AT2026ajxy](https://www.wis-tns.org/object/2026ajxy) | transient_candidate | 8 | 19.88 | IC 1894 (Galaxy) | 0.17650° | near-field match | 65 | hold |
| watch | [AT2026ajkf](https://www.wis-tns.org/object/2026ajkf) | transient_candidate | 5 | 19.07 | Collinder 409 (CR409) (Globular cluster) | 1.82025° | near-field match | 63 | hold |
| watch | [AT2026ajpu](https://www.wis-tns.org/object/2026ajpu) | transient_candidate | 5 | 19.22 | Blue Snowball (Planetary nebula) | 1.82980° | near-field match | 63 | hold |
| watch | [AT2026ajru](https://www.wis-tns.org/object/2026ajru) | transient_candidate | 3 | 18.7 | Collinder 176 (CR176) (Open cluster) | 1.06889° | near-field match | 63 | hold |
| watch | [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) | transient_candidate | 2 | 22.79 | IC5194 (Nebula) | 0.13206° | near-field match | 63 | hold |
| watch | [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) | transient_candidate | 2 | 21.79 | NGC894 (Nebula) | 0.00471° | near-field match | 63 | hold |
| watch | [AT2026ajxu](https://www.wis-tns.org/object/2026ajxu) | transient_candidate | 2 | 19.22 | Collinder 27 (CR27) (Open cluster) | 1.69906° | near-field match | 63 | hold |
| watch | [AT2026akap](https://www.wis-tns.org/object/2026akap) | transient_candidate | 1 | 19.32 | Ghost of Jupiter (Planetary nebula) | 1.78164° | near-field match | 63 | hold |
| watch | [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) | transient_candidate | 3 | 19.17 | van den Bergh 12 (VDB12) (Nebula) | 0.51247° | near-field match | 62 | hold |
| watch | [SN2026ahhp](https://www.wis-tns.org/object/2026ahhp) | SN Ic | 18 | 21.98 | NGC1398 (Galaxy) | 1.54372° | near-field match | 60 | hold |
| watch | [AT2026ajfg](https://www.wis-tns.org/object/2026ajfg) | transient_candidate | 6 | 22.52 | NGC1340 (Galaxy) | 0.35306° | near-field match | 60 | hold |
| watch | [AT2026ajfh](https://www.wis-tns.org/object/2026ajfh) | transient_candidate | 7 | 19.55 | NGC1433 (Galaxy) | 0.67734° | near-field match | 60 | hold |
| watch | [AT2026ajfj](https://www.wis-tns.org/object/2026ajfj) | transient_candidate | 6 | 20.45 | IC 2039 (Galaxy) | 0.31321° | near-field match | 60 | hold |
| watch | [AT2026ajfk](https://www.wis-tns.org/object/2026ajfk) | transient_candidate | 6 | 21.23 | IC1993 (Galaxy) | 0.44583° | near-field match | 60 | hold |
| watch | [AT2026ajfl](https://www.wis-tns.org/object/2026ajfl) | transient_candidate | 6 | 22.63 | NGC1543 (Galaxy) | 0.58240° | near-field match | 60 | hold |
| watch | [AT2026ajiz](https://www.wis-tns.org/object/2026ajiz) | transient_candidate | 7 | 19.64 | NGC 2207 / IC 2163 (Galaxy) | 0.62701° | near-field match | 60 | hold |
| watch | [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) | transient_candidate | 7 | 20.16 | NGC779 (Galaxy) | 0.37577° | near-field match | 60 | hold |
| watch | [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) | transient_candidate | 5 | 19.72 | NGC3239 (Galaxy) | 0.74061° | near-field match | 60 | hold |
| watch | [AT2026ajks](https://www.wis-tns.org/object/2026ajks) | transient_candidate | 7 | 22.25 | IC 5374 (Galaxy) | 0.92554° | near-field match | 60 | hold |
| watch | [AT2026ajlz](https://www.wis-tns.org/object/2026ajlz) | transient_candidate | 6 | 22.45 | IC 1481 (Galaxy) | 0.87422° | near-field match | 60 | hold |
| watch | [AT2026ajoh](https://www.wis-tns.org/object/2026ajoh) | transient_candidate | 4 | 22.19 | IC2006 (Galaxy) | 0.63770° | near-field match | 60 | hold |
| watch | [AT2026ajoq](https://www.wis-tns.org/object/2026ajoq) | transient_candidate | 4 | 22.27 | NGC1596 (Galaxy) | 0.89838° | near-field match | 60 | hold |
| watch | [AT2026ajor](https://www.wis-tns.org/object/2026ajor) | transient_candidate | 4 | 23.32 | NGC1672 (Galaxy) | 0.66270° | near-field match | 60 | hold |
| watch | [AT2026ajos](https://www.wis-tns.org/object/2026ajos) | transient_candidate | 4 | 22.1 | NGC1549 (Galaxy) | 0.50705° | near-field match | 60 | hold |
| watch | [AT2026ajpf](https://www.wis-tns.org/object/2026ajpf) | transient_candidate | 6 | 24.04 | NGC1527 (Galaxy) | 0.95803° | near-field match | 60 | hold |
| watch | [AT2026ajqp](https://www.wis-tns.org/object/2026ajqp) | transient_candidate | 3 | 23.6 | NGC1527 (Galaxy) | 0.92885° | near-field match | 60 | hold |
| watch | [AT2026ajqu](https://www.wis-tns.org/object/2026ajqu) | transient_candidate | 3 | 22.3 | Fornax B (Galaxy) | 0.90734° | near-field match | 60 | hold |
| watch | [AT2026ajqv](https://www.wis-tns.org/object/2026ajqv) | transient_candidate | 3 | 22.77 | NGC1374 (Galaxy) | 0.29655° | near-field match | 60 | hold |
| watch | [AT2026ajqw](https://www.wis-tns.org/object/2026ajqw) | transient_candidate | 3 | 23.09 | Fornax B (Galaxy) | 0.90002° | near-field match | 60 | hold |
| watch | [AT2026ajqx](https://www.wis-tns.org/object/2026ajqx) | transient_candidate | 3 | 22.19 | NGC1365 (Galaxy) | 0.95992° | near-field match | 60 | hold |
| watch | [AT2026ajqy](https://www.wis-tns.org/object/2026ajqy) | transient_candidate | 3 | 22.68 | NGC1332 (Galaxy) | 0.63270° | near-field match | 60 | hold |
| watch | [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) | transient_candidate | 3 | 20.85 | Messier 81 (Galaxy) | 0.68539° | near-field match | 60 | hold |
| watch | [AT2026ajri](https://www.wis-tns.org/object/2026ajri) | transient_candidate | 3 | 21.44 | IC 1540 (Galaxy) | 0.82912° | near-field match | 60 | hold |
| watch | [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) | transient_candidate | 4 | 19.61 | NGC2985 (Galaxy) | 0.55170° | near-field match | 60 | hold |
| watch | [AT2026ajut](https://www.wis-tns.org/object/2026ajut) | transient_candidate | 2 | 22.82 | NGC 3561 (Galaxy) | 0.37521° | near-field match | 60 | hold |
| watch | [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) | transient_candidate | 2 | 22.02 | NGC 3561 (Galaxy) | 0.41178° | near-field match | 60 | hold |
| watch | [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) | transient_candidate | 2 | 22.11 | IC 1417 (Galaxy) | 0.66407° | near-field match | 60 | hold |
| watch | [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) | transient_candidate | 2 | 22.2 | IC 1417 (Galaxy) | 0.99563° | near-field match | 60 | hold |
| watch | [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) | transient_candidate | 2 | 21.89 | IC 1417 (Galaxy) | 0.95089° | near-field match | 60 | hold |
| watch | [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) | transient_candidate | 2 | 22.91 | IC 1419 (Galaxy) | 0.31675° | near-field match | 60 | hold |
| watch | [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) | transient_candidate | 2 | 21.59 | IC 1417 (Galaxy) | 0.46768° | near-field match | 60 | hold |
| watch | [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) | transient_candidate | 2 | 19.72 | IC2560 (Galaxy) | 0.97287° | near-field match | 60 | hold |
| watch | [AT2026ajyh](https://www.wis-tns.org/object/2026ajyh) | transient_candidate | 7 | 21.89 | IC 173 (Galaxy) | 0.72506° | near-field match | 60 | hold |
| watch | [AT2026ajzp](https://www.wis-tns.org/object/2026ajzp) | transient_candidate | 6 | 23.34 | IC 1481 (Galaxy) | 0.91299° | near-field match | 60 | hold |
| watch | [AT2026akaf](https://www.wis-tns.org/object/2026akaf) | transient_candidate | 6 | 20.79 | NGC7723 (Galaxy) | 0.30146° | near-field match | 60 | hold |
| watch | [AT2026akau](https://www.wis-tns.org/object/2026akau) | transient_candidate | 1 | 21.29 | NGC1532 (Galaxy) | 0.51650° | near-field match | 60 | hold |
| watch | [AT2026akbd](https://www.wis-tns.org/object/2026akbd) | transient_candidate | 3 | 20.38 | NGC3193 (Galaxy) | 0.42737° | near-field match | 60 | hold |
| watch | [AT2026aiep](https://www.wis-tns.org/object/2026aiep) | transient_candidate | 13 | 19.17 | IC5194 (Nebula) | 1.65297° | near-field match | 55 | hold |
| watch | [AT2026ajds](https://www.wis-tns.org/object/2026ajds) | transient_candidate | 7 | 19.01 | Boomerang nebula (Planetary nebula) | 1.53259° | near-field match | 55 | hold |
| watch | [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) | transient_candidate | 2 | 19.27 | Lynds Dark Nebula 1473 (LDN1473) (Dark nebula) | 1.48136° | near-field match | 55 | hold |
| watch | [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) | transient_candidate | 14 | 19.39 | Lynds Bright Nebula 718 (LBN718) (HII) | 0.53252° | near-field match | 54 | hold |
| watch | [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) | transient_candidate | 11 | 18.9 | The opal nebula (Planetary nebula) | 0.75975° | near-field match | 54 | hold |
| watch | [SN2026aela](https://www.wis-tns.org/object/2026aela) | SN Ia | 43 | 18.14 | NGC797 (Galaxy) | 1.46981° | near-field match | 53 | hold |
| watch | [AT2026ajji](https://www.wis-tns.org/object/2026ajji) | transient_candidate | 5 | 19.77 | NGC 3294 (Galaxy) | 1.46840° | near-field match | 53 | hold |
| watch | [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) | transient_candidate | 4 | 19.73 | NGC3198 (Galaxy) | 1.44295° | near-field match | 53 | hold |
| watch | [AT2026ajju](https://www.wis-tns.org/object/2026ajju) | transient_candidate | 5 | 19.62 | NGC3239 (Galaxy) | 1.03532° | near-field match | 53 | hold |
| watch | [AT2026ajlv](https://www.wis-tns.org/object/2026ajlv) | transient_candidate | 7 | 22.55 | IC 74 (Galaxy) | 1.59885° | near-field match | 53 | hold |
| watch | [AT2026ajlw](https://www.wis-tns.org/object/2026ajlw) | transient_candidate | 7 | 22.67 | NGC488 (Galaxy) | 1.28359° | near-field match | 53 | hold |
| watch | [AT2026ajlx](https://www.wis-tns.org/object/2026ajlx) | transient_candidate | 7 | 22.55 | IC 70 (Galaxy) | 1.02713° | near-field match | 53 | hold |
| watch | [AT2026ajok](https://www.wis-tns.org/object/2026ajok) | transient_candidate | 4 | 19.77 | IC1993 (Galaxy) | 1.08961° | near-field match | 53 | hold |
| watch | [AT2026ajol](https://www.wis-tns.org/object/2026ajol) | transient_candidate | 4 | 22.52 | NGC1340 (Galaxy) | 1.17282° | near-field match | 53 | hold |
| watch | [AT2026ajqe](https://www.wis-tns.org/object/2026ajqe) | transient_candidate | 3 | 21.46 | IC1386 (Galaxy) | 1.97158° | near-field match | 53 | hold |
| watch | [AT2026ajqf](https://www.wis-tns.org/object/2026ajqf) | transient_candidate | 3 | 23.7 | IC2000 (Galaxy) | 1.19498° | near-field match | 53 | hold |
| watch | [AT2026ajqg](https://www.wis-tns.org/object/2026ajqg) | transient_candidate | 3 | 22.41 | NGC1527 (Galaxy) | 1.43634° | near-field match | 53 | hold |
| watch | [AT2026ajqm](https://www.wis-tns.org/object/2026ajqm) | transient_candidate | 3 | 21.44 | IC1386 (Galaxy) | 1.42198° | near-field match | 53 | hold |
| watch | [AT2026ajqz](https://www.wis-tns.org/object/2026ajqz) | transient_candidate | 3 | 22.81 | NGC1350 (Galaxy) | 1.39326° | near-field match | 53 | hold |
| watch | [AT2026ajra](https://www.wis-tns.org/object/2026ajra) | transient_candidate | 3 | 21.72 | IC1993 (Galaxy) | 1.92768° | near-field match | 53 | hold |
| watch | [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) | transient_candidate | 4 | 20.87 | IC 2016 (Galaxy) | 1.84241° | near-field match | 53 | hold |
| watch | [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) | transient_candidate | 3 | 19.52 | IC5338 (Galaxy) | 1.79914° | near-field match | 53 | hold |
| watch | [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) | transient_candidate | 4 | 19.68 | IC 17 (Galaxy) | 1.57726° | near-field match | 53 | hold |
| watch | [AT2026ajss](https://www.wis-tns.org/object/2026ajss) | transient_candidate | 6 | 22.86 | NGC 2207 / IC 2163 (Galaxy) | 1.55710° | near-field match | 53 | hold |
| watch | [AT2026ajti](https://www.wis-tns.org/object/2026ajti) | transient_candidate | 7 | 22.44 | IC 1757 (Galaxy) | 1.42421° | near-field match | 53 | hold |
| watch | [AT2026ajum](https://www.wis-tns.org/object/2026ajum) | transient_candidate | 6 | 22.35 | IC 1540 (Galaxy) | 1.37052° | near-field match | 53 | hold |
| watch | [AT2026ajux](https://www.wis-tns.org/object/2026ajux) | transient_candidate | 2 | 22.92 | NGC 3561 (Galaxy) | 1.74911° | near-field match | 53 | hold |
| watch | [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) | transient_candidate | 2 | 22.32 | IC 1419 (Galaxy) | 1.06627° | near-field match | 53 | hold |
| watch | [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) | transient_candidate | 2 | 22.34 | IC 1417 (Galaxy) | 1.37982° | near-field match | 53 | hold |
| watch | [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) | transient_candidate | 2 | 21.97 | IC 1419 (Galaxy) | 1.70955° | near-field match | 53 | hold |
| watch | [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) | transient_candidate | 2 | 22.71 | IC 1419 (Galaxy) | 1.38932° | near-field match | 53 | hold |
| watch | [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) | transient_candidate | 2 | 20.46 | IC 1417 (Galaxy) | 1.85790° | near-field match | 53 | hold |
| watch | [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) | transient_candidate | 2 | 22.31 | IC 1419 (Galaxy) | 1.29911° | near-field match | 53 | hold |
| watch | [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) | transient_candidate | 2 | 22.48 | IC 1417 (Galaxy) | 1.26051° | near-field match | 53 | hold |
| watch | [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) | transient_candidate | 2 | 21.14 | IC 1417 (Galaxy) | 1.52083° | near-field match | 53 | hold |
| watch | [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) | transient_candidate | 2 | 22.74 | NGC 3561 (Galaxy) | 1.67055° | near-field match | 53 | hold |
| watch | [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) | transient_candidate | 2 | 22.77 | IC 1419 (Galaxy) | 1.64042° | near-field match | 53 | hold |
| watch | [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) | transient_candidate | 2 | 22.7 | IC 1417 (Galaxy) | 1.79224° | near-field match | 53 | hold |
| watch | [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) | transient_candidate | 2 | 22.99 | IC 1417 (Galaxy) | 1.40126° | near-field match | 53 | hold |
| watch | [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) | transient_candidate | 2 | 22.77 | NGC 3561 (Galaxy) | 1.85355° | near-field match | 53 | hold |
| watch | [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) | transient_candidate | 2 | 22.84 | IC 1417 (Galaxy) | 1.52748° | near-field match | 53 | hold |
| watch | [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) | transient_candidate | 2 | 22.67 | NGC 3561 (Galaxy) | 1.03799° | near-field match | 53 | hold |
| watch | [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) | transient_candidate | 2 | 21.31 | IC 1417 (Galaxy) | 1.38720° | near-field match | 53 | hold |
| watch | [AT2026ajws](https://www.wis-tns.org/object/2026ajws) | transient_candidate | 2 | 22.61 | IC 1417 (Galaxy) | 1.64454° | near-field match | 53 | hold |
| watch | [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) | transient_candidate | 2 | 19.73 | IC 1419 (Galaxy) | 1.89146° | near-field match | 53 | hold |
| watch | [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) | transient_candidate | 2 | 22.68 | IC 1417 (Galaxy) | 1.86530° | near-field match | 53 | hold |
| watch | [AT2026ajww](https://www.wis-tns.org/object/2026ajww) | transient_candidate | 2 | 22.29 | IC 1417 (Galaxy) | 1.35306° | near-field match | 53 | hold |
| watch | [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) | transient_candidate | 2 | 23.14 | IC 1417 (Galaxy) | 1.79292° | near-field match | 53 | hold |
| watch | [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) | transient_candidate | 5 | 19.98 | IC1657 (Galaxy) | 1.48817° | near-field match | 53 | hold |
| watch | [AT2026ajyl](https://www.wis-tns.org/object/2026ajyl) | transient_candidate | 6 | 22.53 | IC 1639 (Galaxy) | 1.77291° | near-field match | 53 | hold |
| watch | [AT2026ajzi](https://www.wis-tns.org/object/2026ajzi) | transient_candidate | 7 | 22.58 | IC 3 (Spiral galaxy) | 1.77766° | near-field match | 53 | hold |
| watch | [AT2026ajzj](https://www.wis-tns.org/object/2026ajzj) | transient_candidate | 7 | 22.67 | IC 173 (Galaxy) | 1.13242° | near-field match | 53 | hold |
| watch | [AT2026akae](https://www.wis-tns.org/object/2026akae) | transient_candidate | 5 | 21.79 | Andromeda Galaxy (Galaxy) | 1.02507° | near-field match | 53 | hold |
| watch | [AT2026akah](https://www.wis-tns.org/object/2026akah) | transient_candidate | 4 | 21.07 | NGC7606 (Galaxy) | 1.33761° | near-field match | 53 | hold |
| watch | [AT2026akam](https://www.wis-tns.org/object/2026akam) | transient_candidate | 1 | 19.7 | IC1657 (Galaxy) | 1.69463° | near-field match | 53 | hold |
| watch | [AT2026akao](https://www.wis-tns.org/object/2026akao) | transient_candidate | 2 | 21.28 | IC 1419 (Galaxy) | 1.62610° | near-field match | 53 | hold |
| watch | [AT2026akaq](https://www.wis-tns.org/object/2026akaq) | transient_candidate | 1 | 19.73 | IC 2031 (Galaxy) | 1.69253° | near-field match | 53 | hold |
| watch | [AT2026akat](https://www.wis-tns.org/object/2026akat) | transient_candidate | 3 | 21.55 | NGC1527 (Galaxy) | 1.52157° | near-field match | 53 | hold |
| watch | [AT2026ajdn](https://www.wis-tns.org/object/2026ajdn) | transient_candidate | 18 | 22.14 | NGC7585 (Galaxy) | 0.84567° | near-field match | 52 | hold |
| watch | [AT2026ajec](https://www.wis-tns.org/object/2026ajec) | transient_candidate | 12 | 23.01 | NGC488 (Galaxy) | 0.68536° | near-field match | 52 | hold |
| watch | [AT2026ajed](https://www.wis-tns.org/object/2026ajed) | transient_candidate | 12 | 22.77 | IC 173 (Galaxy) | 0.78871° | near-field match | 52 | hold |
| watch | [AT2026ajee](https://www.wis-tns.org/object/2026ajee) | transient_candidate | 12 | 22.59 | IC 1776 (Galaxy) | 0.75879° | near-field match | 52 | hold |
| watch | [AT2026ajei](https://www.wis-tns.org/object/2026ajei) | transient_candidate | 10 | 21.94 | NGC3640 (Galaxy) | 0.37997° | near-field match | 52 | hold |
| watch | [AT2026ajen](https://www.wis-tns.org/object/2026ajen) | transient_candidate | 9 | 23.05 | IC 1639 (Galaxy) | 0.27076° | near-field match | 52 | hold |
| watch | [AT2026ajkp](https://www.wis-tns.org/object/2026ajkp) | transient_candidate | 9 | 22.96 | Darth Vader's Galaxy (Galaxy) | 0.53744° | near-field match | 52 | hold |
| watch | [AT2026ajkt](https://www.wis-tns.org/object/2026ajkt) | transient_candidate | 9 | 23.15 | IC 234 (Galaxy) | 0.57827° | near-field match | 52 | hold |
| watch | [AT2026ajlh](https://www.wis-tns.org/object/2026ajlh) | transient_candidate | 10 | 21.69 | NGC3640 (Galaxy) | 0.60624° | near-field match | 52 | hold |
| watch | [AT2026ajlj](https://www.wis-tns.org/object/2026ajlj) | transient_candidate | 9 | 22.54 | IC 1749 (Galaxy) | 0.61175° | near-field match | 52 | hold |
| watch | [AT2026ajlk](https://www.wis-tns.org/object/2026ajlk) | transient_candidate | 9 | 22.61 | IC 1481 (Galaxy) | 0.75962° | near-field match | 52 | hold |
| watch | [AT2026ajmu](https://www.wis-tns.org/object/2026ajmu) | transient_candidate | 12 | 21.64 | IC2421 (Galaxy) | 0.41790° | near-field match | 52 | hold |
| watch | [AT2026ajmx](https://www.wis-tns.org/object/2026ajmx) | transient_candidate | 11 | 22.35 | NGC2549 (Galaxy) | 0.72858° | near-field match | 52 | hold |
| watch | [AT2026ajnl](https://www.wis-tns.org/object/2026ajnl) | transient_candidate | 19 | 21.1 | NGC1058 (Galaxy) | 0.90832° | near-field match | 52 | hold |
| watch | [AT2026ajog](https://www.wis-tns.org/object/2026ajog) | transient_candidate | 9 | 20.22 | IC 21 (Galaxy) | 0.76970° | near-field match | 52 | hold |
| watch | [AT2026ajsm](https://www.wis-tns.org/object/2026ajsm) | transient_candidate | 19 | 20.24 | IC1919 (Galaxy) | 0.30868° | near-field match | 52 | hold |
| watch | [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) | transient_candidate | 9 | 22.82 | IC 74 (Galaxy) | 0.60041° | near-field match | 52 | hold |
| watch | [AT2026ajta](https://www.wis-tns.org/object/2026ajta) | transient_candidate | 9 | 22.45 | IC1696 (Galaxy) | 0.88977° | near-field match | 52 | hold |
| watch | [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) | transient_candidate | 9 | 21.43 | NGC3521 (Galaxy) | 0.82591° | near-field match | 52 | hold |
| watch | [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) | transient_candidate | 19 | 21.33 | IC178 (Galaxy) | 0.93972° | near-field match | 52 | hold |
| watch | [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) | transient_candidate | 14 | 20.75 | NGC 2964 (Galaxy) | 0.25419° | near-field match | 52 | hold |
| watch | [AT2026ajyc](https://www.wis-tns.org/object/2026ajyc) | transient_candidate | 8 | 19.72 | NGC 2207 / IC 2163 (Galaxy) | 0.74711° | near-field match | 52 | hold |
| watch | [AT2026ajyr](https://www.wis-tns.org/object/2026ajyr) | transient_candidate | 18 | 22.47 | IC 1507 (Galaxy) | 0.87774° | near-field match | 52 | hold |
| watch | [AT2026ajzb](https://www.wis-tns.org/object/2026ajzb) | transient_candidate | 10 | 21.83 | NGC3640 (Galaxy) | 0.57000° | near-field match | 52 | hold |
| watch | [AT2026ajzh](https://www.wis-tns.org/object/2026ajzh) | transient_candidate | 8 | 22.48 | Local Group (Galaxy) | 0.56395° | near-field match | 52 | hold |
| watch | [AT2026ajnx](https://www.wis-tns.org/object/2026ajnx) | transient_candidate | 4 | 21.82 | NGC894 (Nebula) | 0.40162° | near-field match | 50 | hold |
| watch | [AT2026ajqr](https://www.wis-tns.org/object/2026ajqr) | transient_candidate | 3 | 22.14 | Messier 72 (M72) (Globular cluster) | 0.84769° | near-field match | 50 | hold |
| watch | [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) | transient_candidate | 2 | 21.93 | NGC7158 (Nebula) | 0.76418° | near-field match | 50 | hold |
| watch | [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) | transient_candidate | 2 | 22.2 | NGC7158 (Nebula) | 0.83221° | near-field match | 50 | hold |
| watch | [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) | transient_candidate | 2 | 21.24 | NGC7158 (Nebula) | 0.38606° | near-field match | 50 | hold |
| watch | [AT2026akbc](https://www.wis-tns.org/object/2026akbc) | transient_candidate | 2 | 20.89 | IC2030 (Nebula) | 0.58630° | near-field match | 50 | hold |
| watch | [AT2026aifu](https://www.wis-tns.org/object/2026aifu) | transient_candidate | 13 | 19.01 | Lynds Bright Nebula 1025 (LBN1025) (HII) | 1.13184° | near-field match | 47 | hold |
| watch | [AT2026ajye](https://www.wis-tns.org/object/2026ajye) | transient_candidate | 9 | 18.67 | Lynds Bright Nebula 878 (LBN878) (HII) | 1.00364° | near-field match | 47 | hold |
| watch | [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) | transient_candidate | 17 | 19.8 | IC1401 (Galaxy) | 1.09401° | near-field match | 45 | hold |
| watch | [AT2026aiit](https://www.wis-tns.org/object/2026aiit) | transient_candidate | 22 | 20.1 | IC 536 (Galaxy) | 1.35004° | near-field match | 45 | hold |
| watch | [AT2026ainu](https://www.wis-tns.org/object/2026ainu) | transient_candidate | 15 | 19.94 | NGC1637 (Galaxy) | 1.60141° | near-field match | 45 | hold |
| watch | [AT2026ajby](https://www.wis-tns.org/object/2026ajby) | transient_candidate | 8 | 20.2 | IC48 (Galaxy) | 1.83966° | near-field match | 45 | hold |
| watch | [AT2026ajdj](https://www.wis-tns.org/object/2026ajdj) | transient_candidate | 18 | 21.21 | NGC7727 (Galaxy) | 1.24258° | near-field match | 45 | hold |
| watch | [AT2026ajdo](https://www.wis-tns.org/object/2026ajdo) | transient_candidate | 18 | 21.42 | NGC7606 (Galaxy) | 1.40071° | near-field match | 45 | hold |
| watch | [AT2026ajea](https://www.wis-tns.org/object/2026ajea) | transient_candidate | 16 | 22.17 | IC 197 (Galaxy) | 1.52695° | near-field match | 45 | hold |
| watch | [AT2026ajef](https://www.wis-tns.org/object/2026ajef) | transient_candidate | 10 | 22.5 | IC1696 (Galaxy) | 1.28974° | near-field match | 45 | hold |
| watch | [AT2026ajek](https://www.wis-tns.org/object/2026ajek) | transient_candidate | 9 | 22.65 | IC 5241 (Galaxy) | 1.64483° | near-field match | 45 | hold |
| watch | [AT2026ajeo](https://www.wis-tns.org/object/2026ajeo) | transient_candidate | 9 | 22.9 | IC 1639 (Galaxy) | 1.33383° | near-field match | 45 | hold |
| watch | [AT2026ajff](https://www.wis-tns.org/object/2026ajff) | transient_candidate | 9 | 20.17 | NGC289 (Galaxy) | 1.00140° | near-field match | 45 | hold |
| watch | [AT2026ajla](https://www.wis-tns.org/object/2026ajla) | transient_candidate | 18 | 21.76 | IC 197 (Galaxy) | 1.37876° | near-field match | 45 | hold |
| watch | [AT2026ajlb](https://www.wis-tns.org/object/2026ajlb) | transient_candidate | 13 | 22.99 | IC 1507 (Galaxy) | 1.75832° | near-field match | 45 | hold |
| watch | [AT2026ajld](https://www.wis-tns.org/object/2026ajld) | transient_candidate | 12 | 23.02 | IC 3 (Spiral galaxy) | 1.91032° | near-field match | 45 | hold |
| watch | [AT2026ajle](https://www.wis-tns.org/object/2026ajle) | transient_candidate | 12 | 23.03 | IC1696 (Galaxy) | 1.84067° | near-field match | 45 | hold |
| watch | [AT2026ajlf](https://www.wis-tns.org/object/2026ajlf) | transient_candidate | 12 | 22.81 | IC 173 (Galaxy) | 1.30826° | near-field match | 45 | hold |
| watch | [AT2026ajlg](https://www.wis-tns.org/object/2026ajlg) | transient_candidate | 10 | 22.56 | IC 1757 (Galaxy) | 1.52105° | near-field match | 45 | hold |
| watch | [AT2026ajli](https://www.wis-tns.org/object/2026ajli) | transient_candidate | 10 | 21.42 | NGC3640 (Galaxy) | 1.32202° | near-field match | 45 | hold |
| watch | [AT2026ajmf](https://www.wis-tns.org/object/2026ajmf) | transient_candidate | 9 | 22.59 | IC 5241 (Galaxy) | 1.90571° | near-field match | 45 | hold |
| watch | [AT2026ajnc](https://www.wis-tns.org/object/2026ajnc) | transient_candidate | 10 | 21.47 | NGC205 (Galaxy) | 1.21009° | near-field match | 45 | hold |
| watch | [AT2026ajnt](https://www.wis-tns.org/object/2026ajnt) | transient_candidate | 14 | 20.27 | NGC2859 (Galaxy) | 1.90673° | near-field match | 45 | hold |
| watch | [AT2026ajnu](https://www.wis-tns.org/object/2026ajnu) | transient_candidate | 13 | 21.73 | IC 189 (Galaxy) | 1.32564° | near-field match | 45 | hold |
| watch | [AT2026ajpc](https://www.wis-tns.org/object/2026ajpc) | transient_candidate | 18 | 20.3 | NGC 1954 (Galaxy) | 1.01085° | near-field match | 45 | hold |
| watch | [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) | transient_candidate | 9 | 19.83 | IC1386 (Galaxy) | 1.28167° | near-field match | 45 | hold |
| watch | [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) | transient_candidate | 8 | 22.02 | NGC3521 (Galaxy) | 1.08432° | near-field match | 45 | hold |
| watch | [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) | transient_candidate | 16 | 21.43 | NGC925 (Galaxy) | 1.68238° | near-field match | 45 | hold |
| watch | [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) | transient_candidate | 13 | 21.33 | IC509 (Galaxy) | 1.28504° | near-field match | 45 | hold |
| watch | [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) | transient_candidate | 13 | 21.32 | UFO Galaxy (Galaxy) | 1.99519° | near-field match | 45 | hold |
| watch | [AT2026ajty](https://www.wis-tns.org/object/2026ajty) | transient_candidate | 13 | 21.65 | IC2378 (Galaxy) | 1.21289° | near-field match | 45 | hold |
| watch | [AT2026ajug](https://www.wis-tns.org/object/2026ajug) | transient_candidate | 10 | 21.26 | IC1525 (Galaxy) | 1.31062° | near-field match | 45 | hold |
| watch | [AT2026ajyi](https://www.wis-tns.org/object/2026ajyi) | transient_candidate | 10 | 22.68 | IC 1776 (Galaxy) | 1.14126° | near-field match | 45 | hold |
| watch | [AT2026ajyt](https://www.wis-tns.org/object/2026ajyt) | transient_candidate | 18 | 22.05 | IC1696 (Galaxy) | 1.53398° | near-field match | 45 | hold |
| watch | [AT2026ajyx](https://www.wis-tns.org/object/2026ajyx) | transient_candidate | 12 | 23 | IC1696 (Galaxy) | 1.66353° | near-field match | 45 | hold |
| watch | [AT2026ajyy](https://www.wis-tns.org/object/2026ajyy) | transient_candidate | 10 | 20.1 | NGC3169 (Galaxy) | 1.85756° | near-field match | 45 | hold |
| watch | [AT2026ajyz](https://www.wis-tns.org/object/2026ajyz) | transient_candidate | 10 | 21.28 | IC 632 (Galaxy) | 1.27527° | near-field match | 45 | hold |
| watch | [AT2026ajzc](https://www.wis-tns.org/object/2026ajzc) | transient_candidate | 10 | 21.7 | Local Group (Galaxy) | 1.45136° | near-field match | 45 | hold |
| watch | [AT2026ajzf](https://www.wis-tns.org/object/2026ajzf) | transient_candidate | 9 | 21.83 | NGC3640 (Galaxy) | 1.39275° | near-field match | 45 | hold |
| watch | [AT2026ajzg](https://www.wis-tns.org/object/2026ajzg) | transient_candidate | 8 | 22.3 | NGC3169 (Galaxy) | 1.35429° | near-field match | 45 | hold |
| watch | [AT2026ajzu](https://www.wis-tns.org/object/2026ajzu) | transient_candidate | 30 | 22.52 | IC 3 (Spiral galaxy) | 1.04710° | near-field match | 45 | hold |
| watch | [AT2026ajzy](https://www.wis-tns.org/object/2026ajzy) | transient_candidate | 10 | 22.9 | NGC 2207 / IC 2163 (Galaxy) | 1.30641° | near-field match | 45 | hold |
| watch | [AT2026akaa](https://www.wis-tns.org/object/2026akaa) | transient_candidate | 8 | 21.91 | NGC3640 (Galaxy) | 1.98192° | near-field match | 45 | hold |
| watch | [AT2026akac](https://www.wis-tns.org/object/2026akac) | transient_candidate | 9 | 21.88 | IC187 (Galaxy) | 1.14616° | near-field match | 45 | hold |
| watch | [AT2026ajlt](https://www.wis-tns.org/object/2026ajlt) | transient_candidate | 7 | 22.76 | IC1651 (Nebula) | 1.25864° | near-field match | 43 | hold |
| watch | [AT2026ajma](https://www.wis-tns.org/object/2026ajma) | transient_candidate | 6 | 22.33 | NGC7668 (Nebula) | 1.52330° | near-field match | 43 | hold |
| watch | [AT2026ajob](https://www.wis-tns.org/object/2026ajob) | transient_candidate | 4 | 22.59 | NGC894 (Nebula) | 1.67540° | near-field match | 43 | hold |
| watch | [AT2026ajou](https://www.wis-tns.org/object/2026ajou) | transient_candidate | 5 | 19.83 | IC5251 (Nebula) | 1.43468° | near-field match | 43 | hold |
| watch | [AT2026ajpi](https://www.wis-tns.org/object/2026ajpi) | transient_candidate | 5 | 22.62 | NGC7526 (Nebula) | 1.96789° | near-field match | 43 | hold |
| watch | [AT2026ajpy](https://www.wis-tns.org/object/2026ajpy) | transient_candidate | 6 | 21.42 | Messier 30 (M30) (Globular cluster) | 1.04427° | near-field match | 43 | hold |
| watch | [AT2026ajqb](https://www.wis-tns.org/object/2026ajqb) | transient_candidate | 3 | 21.61 | Messier 72 (M72) (Globular cluster) | 1.44459° | near-field match | 43 | hold |
| watch | [AT2026ajqn](https://www.wis-tns.org/object/2026ajqn) | transient_candidate | 3 | 22.45 | NGC894 (Nebula) | 1.39431° | near-field match | 43 | hold |
| watch | [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) | transient_candidate | 2 | 19.77 | NGC3578 (Nebula) | 1.46782° | near-field match | 43 | hold |
| watch | [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) | transient_candidate | 7 | 21.8 | NGC7453 (Nebula) | 1.30353° | near-field match | 43 | hold |
| watch | [AT2026ajur](https://www.wis-tns.org/object/2026ajur) | transient_candidate | 2 | 23.23 | NGC7158 (Nebula) | 1.05093° | near-field match | 43 | hold |
| watch | [AT2026ajve](https://www.wis-tns.org/object/2026ajve) | transient_candidate | 2 | 22.03 | IC5194 (Nebula) | 1.56732° | near-field match | 43 | hold |
| watch | [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) | transient_candidate | 2 | 21.75 | IC5194 (Nebula) | 1.82559° | near-field match | 43 | hold |
| watch | [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) | transient_candidate | 2 | 22.52 | IC1457 (Nebula) | 1.62885° | near-field match | 43 | hold |
| watch | [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) | transient_candidate | 2 | 21.84 | IC5194 (Nebula) | 1.34031° | near-field match | 43 | hold |
| watch | [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) | transient_candidate | 2 | 20.66 | IC1457 (Nebula) | 1.88540° | near-field match | 43 | hold |
| watch | [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) | transient_candidate | 2 | 21.83 | NGC894 (Nebula) | 1.21470° | near-field match | 43 | hold |
| watch | [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) | transient_candidate | 2 | 21.12 | NGC7158 (Nebula) | 1.66580° | near-field match | 43 | hold |
| watch | [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) | transient_candidate | 2 | 21.76 | NGC7158 (Nebula) | 1.17313° | near-field match | 43 | hold |
| watch | [AT2026aiat](https://www.wis-tns.org/object/2026aiat) | transient_candidate | 16 | 19.61 | Collinder 163 (CR163) (Open cluster) | 0.39277° | near-field match | 42 | hold |
| watch | [AT2026aiko](https://www.wis-tns.org/object/2026aiko) | transient_candidate | 11 | 19.85 | NGC7158 (Nebula) | 0.38092° | near-field match | 42 | hold |
| watch | [SN2026airg](https://www.wis-tns.org/object/2026airg) | SN II | 10 | 19.93 | Sharpless 260 (SH2-260) (HII) | 1.20103° | near-field match | 42 | hold |
| watch | [AT2026aivj](https://www.wis-tns.org/object/2026aivj) | transient_candidate | 12 | 20.47 | IC1547 (Nebula) | 0.56558° | near-field match | 42 | hold |
| watch | [AT2026ajdy](https://www.wis-tns.org/object/2026ajdy) | transient_candidate | 10 | 20.06 | NGC272 (Open cluster) | 0.82818° | near-field match | 42 | hold |
| watch | [AT2026ajlm](https://www.wis-tns.org/object/2026ajlm) | transient_candidate | 9 | 22.24 | NGC7613 (Nebula) | 0.70355° | near-field match | 42 | hold |
| watch | [AT2026ajmh](https://www.wis-tns.org/object/2026ajmh) | transient_candidate | 29 | 21.78 | IC1665 (Nebula) | 0.81988° | near-field match | 42 | hold |
| watch | [AT2026ajmi](https://www.wis-tns.org/object/2026ajmi) | transient_candidate | 29 | 21.94 | NGC843 (Nebula) | 0.79289° | near-field match | 42 | hold |
| watch | [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) | transient_candidate | 5 | 19.72 | Lynds Bright Nebula 439 (LBN439) (HII) | 0.79678° | near-field match | 42 | hold |
| watch | [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) | transient_candidate | 10 | 22.16 | IC111 (Nebula) | 0.80147° | near-field match | 42 | hold |
| watch | [AT2026ajup](https://www.wis-tns.org/object/2026ajup) | transient_candidate | 14 | 21.25 | Collinder 116 (CR116) (Open cluster) | 0.84314° | near-field match | 42 | hold |
| watch | [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) | transient_candidate | 17 | 23.8 | NGC894 (Nebula) | 0.53340° | near-field match | 42 | hold |
| watch | [AT2026ajym](https://www.wis-tns.org/object/2026ajym) | transient_candidate | 19 | 22.1 | NGC7613 (Nebula) | 0.51096° | near-field match | 42 | hold |
| watch | [AT2026ajzw](https://www.wis-tns.org/object/2026ajzw) | transient_candidate | 16 | 22.42 | NGC7668 (Nebula) | 0.85066° | near-field match | 42 | hold |
| watch | [AT2026ahhj](https://www.wis-tns.org/object/2026ahhj) | transient_candidate | 18 | 22.31 | NGC7453 (Nebula) | 1.72039° | near-field match | 35 | hold |
| watch | [AT2026ajdm](https://www.wis-tns.org/object/2026ajdm) | transient_candidate | 18 | 22.14 | NGC7668 (Nebula) | 1.32204° | near-field match | 35 | hold |
| watch | [AT2026ajeq](https://www.wis-tns.org/object/2026ajeq) | transient_candidate | 26 | 21.42 | NGC2284 (Nebula) | 1.44095° | near-field match | 35 | hold |
| watch | [AT2026ajet](https://www.wis-tns.org/object/2026ajet) | transient_candidate | 22 | 20.96 | Collinder 116 (CR116) (Open cluster) | 1.97492° | near-field match | 35 | hold |
| watch | [AT2026ajev](https://www.wis-tns.org/object/2026ajev) | transient_candidate | 16 | 21.31 | Collinder 116 (CR116) (Open cluster) | 1.73662° | near-field match | 35 | hold |
| watch | [AT2026ajfn](https://www.wis-tns.org/object/2026ajfn) | transient_candidate | 18 | 23.14 | NGC894 (Nebula) | 1.16150° | near-field match | 35 | hold |
| watch | [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) | transient_candidate | 11 | 20.91 | Intergalactic Wanderer (Globular cluster) | 1.09787° | near-field match | 35 | hold |
| watch | [AT2026ajkm](https://www.wis-tns.org/object/2026ajkm) | transient_candidate | 7 | 21.9 | Lynds Bright Nebula 418 (LBN418) (HII) | 1.03018° | near-field match | 35 | hold |
| watch | [AT2026ajkq](https://www.wis-tns.org/object/2026ajkq) | transient_candidate | 21 | 20.77 | IC1651 (Nebula) | 1.80188° | near-field match | 35 | hold |
| watch | [AT2026ajlo](https://www.wis-tns.org/object/2026ajlo) | transient_candidate | 9 | 22.65 | NGC7565 (Nebula) | 1.97938° | near-field match | 35 | hold |
| watch | [AT2026ajlq](https://www.wis-tns.org/object/2026ajlq) | transient_candidate | 7 | 22.86 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.81927° | near-field match | 35 | hold |
| watch | [AT2026ajmr](https://www.wis-tns.org/object/2026ajmr) | transient_candidate | 14 | 21.98 | NGC2464 (Nebula) | 1.15457° | near-field match | 35 | hold |
| watch | [AT2026ajmw](https://www.wis-tns.org/object/2026ajmw) | transient_candidate | 11 | 21.36 | NGC2464 (Nebula) | 1.42390° | near-field match | 35 | hold |
| watch | [AT2026ajne](https://www.wis-tns.org/object/2026ajne) | transient_candidate | 8 | 21.45 | Collinder 116 (CR116) (Open cluster) | 1.30710° | near-field match | 35 | hold |
| watch | [AT2026ajng](https://www.wis-tns.org/object/2026ajng) | transient_candidate | 8 | 20.81 | IC2350 (Nebula) | 1.54892° | near-field match | 35 | hold |
| watch | [AT2026ajnh](https://www.wis-tns.org/object/2026ajnh) | transient_candidate | 7 | 20.62 | Goblet of Fire nebula (Planetary nebula) | 1.85337° | near-field match | 35 | hold |
| watch | [AT2026ajnw](https://www.wis-tns.org/object/2026ajnw) | transient_candidate | 11 | 20.74 | Collinder 116 (CR116) (Open cluster) | 1.48474° | near-field match | 35 | hold |
| watch | [AT2026ajom](https://www.wis-tns.org/object/2026ajom) | transient_candidate | 6 | 20.3 | Lynds Bright Nebula 968 (LBN968) (HII) | 1.64919° | near-field match | 35 | hold |
| watch | [AT2026ajpe](https://www.wis-tns.org/object/2026ajpe) | transient_candidate | 12 | 23.13 | IC2069 (Nebula) | 1.57505° | near-field match | 35 | hold |
| watch | [AT2026ajpl](https://www.wis-tns.org/object/2026ajpl) | transient_candidate | 10 | 21.06 | IC5344 (Nebula) | 1.63978° | near-field match | 35 | hold |
| watch | [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) | transient_candidate | 3 | 19.58 | Lynds Bright Nebula 484 (LBN484) (HII) | 1.74355° | near-field match | 35 | hold |
| watch | [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) | transient_candidate | 5 | 19.74 | Lynds Bright Nebula 856 (LBN856) (HII) | 1.86922° | near-field match | 35 | hold |
| watch | [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) | transient_candidate | 9 | 22.88 | NGC728 (Nebula) | 1.25970° | near-field match | 35 | hold |
| watch | [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) | transient_candidate | 11 | 23.61 | IC5248 (Nebula) | 1.48459° | near-field match | 35 | hold |
| watch | [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) | transient_candidate | 9 | 21.48 | NGC3387 (Nebula) | 1.71033° | near-field match | 35 | hold |
| watch | [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) | transient_candidate | 14 | 21.87 | NGC737 (Nebula) | 1.51249° | near-field match | 35 | hold |
| watch | [AT2026ajub](https://www.wis-tns.org/object/2026ajub) | transient_candidate | 12 | 21.61 | NGC2901 (Nebula) | 1.29090° | near-field match | 35 | hold |
| watch | [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) | transient_candidate | 8 | 22.61 | NGC894 (Nebula) | 1.74562° | near-field match | 35 | hold |
| watch | [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) | transient_candidate | 8 | 20.08 | NGC1498 (Open cluster) | 1.41273° | near-field match | 35 | hold |
| watch | [AT2026ajxz](https://www.wis-tns.org/object/2026ajxz) | transient_candidate | 5 | 20.27 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.08910° | near-field match | 35 | hold |
| watch | [AT2026ajyk](https://www.wis-tns.org/object/2026ajyk) | transient_candidate | 7 | 22.81 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.88407° | near-field match | 35 | hold |
| watch | [AT2026akak](https://www.wis-tns.org/object/2026akak) | transient_candidate | 11 | 20.3 | IC 5364 (CiG) | 1.64295° | near-field match | 35 | hold |
| watch | [AT2026aigg](https://www.wis-tns.org/object/2026aigg) | transient_candidate | 15 | 20.26 | Lynds Bright Nebula 910 (LBN910) (HII) | 0.77477° | near-field match | 34 | hold |
| watch | [AT2026ajts](https://www.wis-tns.org/object/2026ajts) | transient_candidate | 14 | 20.91 | Lynds Bright Nebula 891 (LBN891) (HII) | 0.64768° | near-field match | 34 | hold |
| watch | [SN2026aeff](https://www.wis-tns.org/object/2026aeff) | SN II | 47 | 19.25 | NGC 2207 / IC 2163 (CiG) | 1.95543° | near-field match | 33 | hold |
| watch | [AT2026absv](https://www.wis-tns.org/object/2026absv) | transient_candidate | 64 | 19.48 | NGC 3561 (Galaxy) | 1.10562° | near-field match | 28 | hold |
| watch | [AT2026aeka](https://www.wis-tns.org/object/2026aeka) | transient_candidate | 60 | 20.21 | IC 1876 (Galaxy) | 0.09948° | near-field match | 28 | hold |
| watch | [AT2026aiem](https://www.wis-tns.org/object/2026aiem) | transient_candidate | 12 | 19.89 | Lynds Bright Nebula 556 (LBN556) (HII) | 1.55459° | near-field match | 27 | hold |
| watch | [AT2026aimd](https://www.wis-tns.org/object/2026aimd) | transient_candidate | 11 | 20.38 | Collinder 65 (CR65) (Open cluster) | 1.83171° | near-field match | 27 | hold |
| watch | [AT2026ajkk](https://www.wis-tns.org/object/2026ajkk) | transient_candidate | 10 | 21.78 | Lynds Bright Nebula 688 (LBN688) (HII) | 1.01865° | near-field match | 27 | hold |
| watch | [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) | SN Ia | 43 | 19.82 | NGC7158 (Nebula) | 0.70237° | near-field match | 20 | hold |
| watch | [AT2026abyt](https://www.wis-tns.org/object/2026abyt) | transient_candidate | 61 | 19.14 | IC2170 (Nebula) | 1.73601° | near-field match | 18 | hold |
| watch | [AT2026adsv](https://www.wis-tns.org/object/2026adsv) | transient_candidate | 47 | 20.83 | IC1386 (Galaxy) | 0.88938° | near-field match | 15 | hold |
| watch | [AT2026ajku](https://www.wis-tns.org/object/2026ajku) | transient_candidate | 70 | 22.1 | NGC488 (Galaxy) | 0.71371° | near-field match | 15 | hold |
| watch | [AT2026ajky](https://www.wis-tns.org/object/2026ajky) | transient_candidate | 39 | 22.61 | IC 197 (Galaxy) | 0.99165° | near-field match | 15 | hold |
| watch | [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) | transient_candidate | 65 | 20.79 | NGC925 (Galaxy) | 0.76155° | near-field match | 15 | hold |
| watch | [SN2026afgl](https://www.wis-tns.org/object/2026afgl) | SN IIn | 37 | 19.63 | Beehive cluster (Open cluster) | 1.83228° | near-field match | 13 | hold |
| watch | [AT2026aawo](https://www.wis-tns.org/object/2026aawo) | transient_candidate | 75 | 20.08 | IC 1341 (Galaxy) | 1.50242° | near-field match | 8 | hold |
| watch | [AT2026adsx](https://www.wis-tns.org/object/2026adsx) | transient_candidate | 47 | 20.67 | IC1386 (Galaxy) | 1.56536° | near-field match | 8 | hold |
| watch | [AT2026agac](https://www.wis-tns.org/object/2026agac) | transient_candidate | 38 | 20.92 | IC 1417 (Galaxy) | 1.74979° | near-field match | 8 | hold |
| watch | [AT2026ajkn](https://www.wis-tns.org/object/2026ajkn) | transient_candidate | 35 | 22.34 | IC 1639 (Galaxy) | 1.07935° | near-field match | 8 | hold |
| watch | [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) | transient_candidate | 65 | 22.85 | IC 1507 (Galaxy) | 1.97219° | near-field match | 8 | hold |
| watch | [AT2026ajyo](https://www.wis-tns.org/object/2026ajyo) | transient_candidate | 31 | 22.17 | IC 173 (Galaxy) | 1.29924° | near-field match | 8 | hold |
| watch | [AT2026aflb](https://www.wis-tns.org/object/2026aflb) | transient_candidate | 39 | 22.4 | NGC7668 (Nebula) | 0.94348° | near-field match | 5 | hold |
| watch | [AT2026ajmg](https://www.wis-tns.org/object/2026ajmg) | transient_candidate | 44 | 20.17 | NGC2464 (Nebula) | 1.82991° | near-field match | 0 | hold |

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
| Discovery | 2026-11-02T19:55:53Z · 15 days · 16.1 Clear |
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

### 2. [AT2026ajxw](https://www.wis-tns.org/object/2026ajxw) near IC750

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 100/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC750 as this object's host. The 0.12317° (7.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T15:10:28Z · 2 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.12317° · 7.39′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, large, little (adv.); long (adj.) extended 35deg , brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=179.6954282%2042.6002982&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 3. [SN2026aicq](https://www.wis-tns.org/object/2026aicq) near IC 369

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
| Discovery | 2026-11-04T13:00:09Z · 13 days · 18.48 L |
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

### 4. [SN2026ainb](https://www.wis-tns.org/object/2026ainb) near IC 450

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
| Discovery | 2026-11-04T02:25:45Z · 13 days · 18.12 wide |
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

### 5. [AT2026ajpr](https://www.wis-tns.org/object/2026ajpr) near NGC3945

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 90/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3945 as this object's host. The 0.86986° (52.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:18:43Z · 7 days · 18.03 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 6. [AT2026ajrb](https://www.wis-tns.org/object/2026ajrb) near IC5270

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5270 as this object's host. The 1.73389° (104.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T06:17:03Z · 4 days · 18.48 orange |
| Latest public photometry | Not available in the staged feed |
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

### 7. [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) near IC765

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC765 as this object's host. The 0.75222° (45.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:56:47Z · 3 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 8. [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) near IC656

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC656 as this object's host. The 0.87219° (52.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:02:11Z · 9 days · 18.38 orange |
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
| Subject | **IC656** · `IC656` |
| Catalog display name | IC656 |
| Type / constellation | Nebula · Leo |
| Catalog magnitude / angular size | — · 0.2′ × 0.2′ |
| Distance | — |
| Separation | 0.87219° · 52.33′ |
| Catalog description | very small in angular size, cluster, neb? |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.5998779%2017.2208246&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 9. [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) near NGC2276

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2276 as this object's host. The 0.19202° (11.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T02:46:53Z · 4 days · 19.32 wide |
| Latest public photometry | Not available in the staged feed |
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

### 10. [SN2026ahsn](https://www.wis-tns.org/object/2026ahsn) near IC 3

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
| Discovery | 2026-11-01T10:53:54Z · 16 days · 18.71 L |
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

### 11. [SN2026ahze](https://www.wis-tns.org/object/2026ahze) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.92287° (115.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.092 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:33:40Z · 14 days · 18.71 g |
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

### 12. [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.59331° (35.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:02Z · 4 days · 19.37 wide |
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

### 13. [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) near NGC2768

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2768 as this object's host. The 0.41880° (25.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T04:23:39Z · 4 days · 19.35 wide |
| Latest public photometry | Not available in the staged feed |
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

### 14. [AT2026ajxv](https://www.wis-tns.org/object/2026ajxv) near NGC 3277

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3277 as this object's host. The 0.80128° (48.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:06:01Z · 3 days · 19.13 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 3277** · `NGC 3277` |
| Catalog display name | NGC 3277 |
| Type / constellation | Galaxy · LMi |
| Catalog magnitude / angular size | 11.65 · 2.11′ × 1.59′ |
| Distance | — |
| Separation | 0.80128° · 48.08′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.9248246%2027.9934838&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 15. [AT2026ajdq](https://www.wis-tns.org/object/2026ajdq) near IC 1600

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
| Discovery | 2026-11-10T06:02:28Z · 7 days · 19.19 i |
| Latest public photometry | Not available in the staged feed |
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

### 16. [AT2026ajig](https://www.wis-tns.org/object/2026ajig) near IC 38

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
| Discovery | 2026-11-12T10:08:29Z · 5 days · 19.78 L |
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

### 17. [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) near NGC1169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1169 as this object's host. The 1.01800° (61.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T23:39:27Z · 5 days · 19.46 L |
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

### 18. [AT2026ajjn](https://www.wis-tns.org/object/2026ajjn) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.51592° (90.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:19:10Z · 5 days · 18.82 L |
| Latest public photometry | Not available in the staged feed |
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

### 19. [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) near IC486

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC486 as this object's host. The 1.22917° (73.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T12:37:47Z · 5 days · 19 cyan |
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

### 20. [AT2026ajoo](https://www.wis-tns.org/object/2026ajoo) near IC2058

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2058 as this object's host. The 0.00834° (0.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 22.76 r |
| Latest public photometry | Not available in the staged feed |
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

### 21. [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) near IC1733

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1733 as this object's host. The 1.11166° (66.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T06:40:30Z · 3 days · 19.45 w |
| Latest public photometry | Not available in the staged feed |
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

### 22. [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) near IC5261

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5261 as this object's host. The 1.21834° (73.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T20:50:16Z · 4 days · 19.27 wide |
| Latest public photometry | Not available in the staged feed |
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

### 23. [AT2026ajva](https://www.wis-tns.org/object/2026ajva) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19660° (11.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 21.81 i |
| Latest public photometry | Not available in the staged feed |
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

### 24. [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19359° (11.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.15 i |
| Latest public photometry | Not available in the staged feed |
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

### 25. [AT2026ajyd](https://www.wis-tns.org/object/2026ajyd) near IC600

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC600 as this object's host. The 1.36887° (82.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T06:07:10Z · 1 days · 19.16 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.36887° · 82.13′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.319783%20-2.532441&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 26. [AT2026akaz](https://www.wis-tns.org/object/2026akaz) near Caldwell 3 (C3)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 3 (C3) as this object's host. The 1.12593° (67.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T14:52:08Z · 1 days · 19.3 cyan |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.12593° · 67.56′ |
| Catalog description | NGC 4236 is a barred Magellanic spiral galaxy located in the constellation Draco. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akaz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=186.70665%2070.17334&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 27. [AT2026agub](https://www.wis-tns.org/object/2026agub) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 0.34859° (20.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T09:54:09Z · 23 days · 19.46 r |
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
| Subject | **Andromeda Galaxy** · `IC 1732` |
| Catalog display name | Andromeda Galaxy |
| Type / constellation | Galaxy · And |
| Catalog magnitude / angular size | — · 1.32′ × 0.38′ |
| Distance | — |
| Separation | 0.34859° · 20.92′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agub) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=28.0919572%2035.7899313&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 28. [AT2026ajdx](https://www.wis-tns.org/object/2026ajdx) near IC2160

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2160 as this object's host. The 0.65192° (39.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T06:16:49Z · 9 days · 19.5 cyan |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajdx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=86.17722%20-77.1682775&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [AT2026ajmb](https://www.wis-tns.org/object/2026ajmb) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 0.67085° (40.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:38:52Z · 6 days · 19.13 r |
| Latest public photometry | Not available in the staged feed |
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

### 30. [AT2026agye](https://www.wis-tns.org/object/2026agye) near IC 5124

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
| Discovery | 2026-10-27T10:07:35Z · 21 days · 19.16 L |
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

### 31. [AT2026ajko](https://www.wis-tns.org/object/2026ajko) near NGC864

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC864 as this object's host. The 0.13264° (7.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T18:10:04Z · 16 days · 22.23 r |
| Latest public photometry | Not available in the staged feed |
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

### 32. [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) near Lynds Bright Nebula 1043 (LBN1043)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1043 (LBN1043) as this object's host. The 1.49482° (89.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T18:56:34Z · 5 days · 18.5 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 33. [AT2026ajxy](https://www.wis-tns.org/object/2026ajxy) near IC 1894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1894 as this object's host. The 0.17650° (10.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T23:00:52Z · 8 days · 19.88 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1894** · `IC 1894` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Ari |
| Catalog magnitude / angular size | — · 0.78′ × 0.52′ |
| Distance | — |
| Separation | 0.17650° · 10.59′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1894 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=47.793493%2019.606402&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026ajkf](https://www.wis-tns.org/object/2026ajkf) near Collinder 409 (CR409)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 409 (CR409) as this object's host. The 1.82025° (109.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:55:20Z · 5 days · 19.07 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 35. [AT2026ajpu](https://www.wis-tns.org/object/2026ajpu) near Blue Snowball

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Blue Snowball as this object's host. The 1.82980° (109.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T08:10:22Z · 5 days · 19.22 orange |
| Latest public photometry | Not available in the staged feed |
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

### 36. [AT2026ajru](https://www.wis-tns.org/object/2026ajru) near Collinder 176 (CR176)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 176 (CR176) as this object's host. The 1.06889° (64.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T02:16:35Z · 3 days · 18.7 orange |
| Latest public photometry | Not available in the staged feed |
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

### 37. [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 0.13206° (7.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:31:35Z · 2 days · 22.79 i |
| Latest public photometry | Not available in the staged feed |
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

### 38. [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.00471° (0.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 2 days · 21.79 i |
| Latest public photometry | Not available in the staged feed |
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

### 39. [AT2026ajxu](https://www.wis-tns.org/object/2026ajxu) near Collinder 27 (CR27)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 27 (CR27) as this object's host. The 1.69906° (101.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T09:38:01Z · 2 days · 19.22 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
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
| Separation | 1.69906° · 101.94′ |
| Catalog description | NGC 956 is an asterism in the constellation Andromeda. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=40.153305%2045.506525&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [AT2026akap](https://www.wis-tns.org/object/2026akap) near Ghost of Jupiter

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Ghost of Jupiter as this object's host. The 1.78164° (106.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T05:23:23Z · 1 days · 19.32 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Ghost of Jupiter** · `NGC 3242` |
| Catalog display name | Ghost of Jupiter |
| Type / constellation | Planetary nebula · Hya |
| Catalog magnitude / angular size | — · 0.67′ × 0.58′ |
| Distance | 2,000 ly |
| Separation | 1.78164° · 106.90′ |
| Catalog description | NGC 3242 is a planetary nebula located in the constellation Hydra. NGC 3242 (also known as the Ghost of Jupiter, Eye Nebula or Caldwell 59) is a planetary nebula located  in the constellation Hydra. William Herschel discovered the nebula on February 7, 1785, and catalogued it as H IV.27. John Herschel observed it from the Cape of Good Hope, South Africa, in the 1830s, and numbered it as h 3248, and included it in the 1864 General Catalogue as GC 2102; this became NGC 3242 in J. L. E. Dreyer's New General Catalogue of 1888. This planetary nebula is most frequently called the Ghost of Jupiter, or Jupiter's Ghost due to its similar shape to the planet, but it is also sometimes referred to as the Eye Nebula. The nebula measures around two light years long from end to end, and contains a central white dwarf with an apparent magnitude of 11. The inner layers of the nebula were formed some 1,500 years ago. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akap) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.3589925%20-20.2477725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 41. [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) near van den Bergh 12 (VDB12)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 12 (VDB12) as this object's host. The 0.51247° (30.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T10:32:37Z · 3 days · 19.17 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 42. [SN2026ahhp](https://www.wis-tns.org/object/2026ahhp) near NGC1398

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1398 as this object's host. The 1.54372° (92.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ic |
| Redshift | 0.11 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:15:38Z · 18 days · 21.98 i |
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

### 43. [AT2026ajfg](https://www.wis-tns.org/object/2026ajfg) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 0.35306° (21.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 6 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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

### 44. [AT2026ajfh](https://www.wis-tns.org/object/2026ajfh) near NGC1433

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1433 as this object's host. The 0.67734° (40.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:46:44Z · 7 days · 19.55 L |
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

### 45. [AT2026ajfj](https://www.wis-tns.org/object/2026ajfj) near IC 2039

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
| Discovery | 2026-11-11T13:58:21Z · 6 days · 20.45 r |
| Latest public photometry | Not available in the staged feed |
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

### 46. [AT2026ajfk](https://www.wis-tns.org/object/2026ajfk) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 0.44583° (26.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 6 days · 21.23 g |
| Latest public photometry | Not available in the staged feed |
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

### 47. [AT2026ajfl](https://www.wis-tns.org/object/2026ajfl) near NGC1543

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1543 as this object's host. The 0.58240° (34.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T13:58:21Z · 6 days · 22.63 g |
| Latest public photometry | Not available in the staged feed |
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

### 48. [AT2026ajiz](https://www.wis-tns.org/object/2026ajiz) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.62701° (37.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:40:32Z · 7 days · 19.64 L |
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

### 49. [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) near NGC779

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC779 as this object's host. The 0.37577° (22.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:18:57Z · 7 days · 20.16 L |
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
| Subject | **NGC779** · `NGC779` |
| Catalog display name | NGC779 |
| Type / constellation | Galaxy · Cetus |
| Catalog magnitude / angular size | 11.2 · 1.35′ × 0.58′ |
| Distance | — |
| Separation | 0.37577° · 22.55′ |
| Catalog description | NGC 779 is a spiral galaxy seen edge-on, located in the constellation Cetus. It is located at a distance of circa 60 million light years from Earth, which, given its apparent dimensions, means that NGC 779 is about 70,000 light years across. It was discovered by William Herschel on September 10, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.5917983%20-6.14044&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 50. [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.74061° (44.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 5 days · 19.72 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.07439%2017.88114&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 51. [AT2026ajks](https://www.wis-tns.org/object/2026ajks) near IC 5374

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
| Discovery | 2026-11-10T13:37:55Z · 7 days · 22.25 g |
| Latest public photometry | Not available in the staged feed |
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

### 52. [AT2026ajlz](https://www.wis-tns.org/object/2026ajlz) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.87422° (52.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:30:14Z · 6 days · 22.45 r |
| Latest public photometry | Not available in the staged feed |
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

### 53. [AT2026ajoh](https://www.wis-tns.org/object/2026ajoh) near IC2006

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2006 as this object's host. The 0.63770° (38.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 22.19 r |
| Latest public photometry | Not available in the staged feed |
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

### 54. [AT2026ajoq](https://www.wis-tns.org/object/2026ajoq) near NGC1596

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1596 as this object's host. The 0.89838° (53.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 22.27 r |
| Latest public photometry | Not available in the staged feed |
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

### 55. [AT2026ajor](https://www.wis-tns.org/object/2026ajor) near NGC1672

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1672 as this object's host. The 0.66270° (39.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 23.32 g |
| Latest public photometry | Not available in the staged feed |
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

### 56. [AT2026ajos](https://www.wis-tns.org/object/2026ajos) near NGC1549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1549 as this object's host. The 0.50705° (30.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 22.1 r |
| Latest public photometry | Not available in the staged feed |
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

### 57. [AT2026ajpf](https://www.wis-tns.org/object/2026ajpf) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.95803° (57.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T05:47:42Z · 6 days · 24.04 g |
| Latest public photometry | Not available in the staged feed |
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

### 58. [AT2026ajqp](https://www.wis-tns.org/object/2026ajqp) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 0.92885° (55.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 3 days · 23.6 r |
| Latest public photometry | Not available in the staged feed |
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

### 59. [AT2026ajqu](https://www.wis-tns.org/object/2026ajqu) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.90734° (54.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T09:37:27Z · 3 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
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

### 60. [AT2026ajqv](https://www.wis-tns.org/object/2026ajqv) near NGC1374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1374 as this object's host. The 0.29655° (17.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T09:37:27Z · 3 days · 22.77 g |
| Latest public photometry | Not available in the staged feed |
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

### 61. [AT2026ajqw](https://www.wis-tns.org/object/2026ajqw) near Fornax B

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Fornax B as this object's host. The 0.90002° (54.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 3 days · 23.09 g |
| Latest public photometry | Not available in the staged feed |
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

### 62. [AT2026ajqx](https://www.wis-tns.org/object/2026ajqx) near NGC1365

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1365 as this object's host. The 0.95992° (57.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 3 days · 22.19 g |
| Latest public photometry | Not available in the staged feed |
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

### 63. [AT2026ajqy](https://www.wis-tns.org/object/2026ajqy) near NGC1332

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1332 as this object's host. The 0.63270° (37.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 3 days · 22.68 g |
| Latest public photometry | Not available in the staged feed |
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

### 64. [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) near Messier 81

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 81 as this object's host. The 0.68539° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:28:39Z · 3 days · 20.85 w |
| Latest public photometry | Not available in the staged feed |
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

### 65. [AT2026ajri](https://www.wis-tns.org/object/2026ajri) near IC 1540

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
| Discovery | 2026-11-14T05:21:13Z · 3 days · 21.44 w |
| Latest public photometry | Not available in the staged feed |
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

### 66. [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) near NGC2985

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2985 as this object's host. The 0.55170° (33.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T05:10:07Z · 4 days · 19.61 wide |
| Latest public photometry | Not available in the staged feed |
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

### 67. [AT2026ajut](https://www.wis-tns.org/object/2026ajut) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.37521° (22.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.82 i |
| Latest public photometry | Not available in the staged feed |
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

### 68. [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.41178° (24.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.02 i |
| Latest public photometry | Not available in the staged feed |
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

### 69. [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.11 i |
| Latest public photometry | Not available in the staged feed |
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

### 70. [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 2 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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

### 71. [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 21.89 i |
| Latest public photometry | Not available in the staged feed |
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

### 72. [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 2 days · 22.91 i |
| Latest public photometry | Not available in the staged feed |
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

### 73. [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 2 days · 21.59 i |
| Latest public photometry | Not available in the staged feed |
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

### 74. [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) near IC2560

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2560 as this object's host. The 0.97287° (58.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T17:23:09Z · 2 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
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

### 75. [AT2026ajyh](https://www.wis-tns.org/object/2026ajyh) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 0.72506° (43.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T16:59:31Z · 7 days · 21.89 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.72506° · 43.50′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.678917%201.064447&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026ajzp](https://www.wis-tns.org/object/2026ajzp) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.91299° (54.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:25:55Z · 6 days · 23.34 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.91299° · 54.78′ |
| Catalog description | IC 1481 is a spiral galaxy located in the Pisces constellation. It is located 289 million light years from Earth and was discovered by Austrian astronomer, Rudolf Spitaler on October 6, 1891. The galaxy has an approximate diameter of 65,000 light years with a surface brightness of 12.8 square arcmin. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.772458%205.895517&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 77. [AT2026akaf](https://www.wis-tns.org/object/2026akaf) near NGC7723

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7723 as this object's host. The 0.30146° (18.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T03:02:55Z · 6 days · 20.79 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7723** · `NGC7723` |
| Catalog display name | NGC7723 |
| Type / constellation | Galaxy · Aquarius |
| Catalog magnitude / angular size | 11.2 · 3.29′ × 2.32′ |
| Distance | 26,550 kpc |
| Separation | 0.30146° · 18.09′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akaf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.611558%20-12.6688512&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 78. [AT2026akau](https://www.wis-tns.org/object/2026akau) near NGC1532

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1532 as this object's host. The 0.51650° (30.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T07:15:40Z · 1 days · 21.29 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.51650° · 30.99′ |
| Catalog description | NGC 1532, also known as Haley's Coronet, is an edge-on barred spiral galaxy located approximately 58 million light-years from the Solar System in the constellation Eridanus. The galaxy was discovered by James Dunlop on 29 October 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akau) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.470687%20-33.22343&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 79. [AT2026akbd](https://www.wis-tns.org/object/2026akbd) near NGC3193

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3193 as this object's host. The 0.42737° (25.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:20:55Z · 3 days · 20.38 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3193** · `NGC3193` |
| Catalog display name | NGC3193 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 11 · 2.36′ × 2.16′ |
| Distance | — |
| Separation | 0.42737° · 25.64′ |
| Catalog description | NGC 3193 is an elliptical galaxy in the constellation Leo. The galaxy lies about 90 million light years away from Earth, which means, given its apparent dimensions, that NGC 3193 is approximately 80,000 light years across. It was discovered by William Herschel on March 12, 1784. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.5081395%2022.3127864&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 80. [AT2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65297° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 13 days · 19.17 wide |
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

### 81. [AT2026ajds](https://www.wis-tns.org/object/2026ajds) near Boomerang nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Boomerang nebula as this object's host. The 1.53259° (91.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:30:35Z · 7 days · 19.01 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 82. [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) near Lynds Dark Nebula 1473 (LDN1473)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1473 (LDN1473) as this object's host. The 1.48136° (88.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:51:51Z · 2 days · 19.27 wide |
| Latest public photometry | Not available in the staged feed |
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

### 83. [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) near Lynds Bright Nebula 718 (LBN718)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 718 (LBN718) as this object's host. The 0.53252° (31.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:11:33Z · 14 days · 19.39 r |
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

### 84. [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) near The opal nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify The opal nebula as this object's host. The 0.75975° (45.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:11:11Z · 11 days · 18.9 orange |
| Latest public photometry | Not available in the staged feed |
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

### 85. [SN2026aela](https://www.wis-tns.org/object/2026aela) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.46981° (88.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0503 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T20:31:24Z · 43 days · 18.14 L |
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

### 86. [AT2026ajji](https://www.wis-tns.org/object/2026ajji) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.46840° (88.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:15:17Z · 5 days · 19.77 L |
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

### 87. [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) near NGC3198

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3198 as this object's host. The 1.44295° (86.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T06:12:54Z · 4 days · 19.73 L |
| Latest public photometry | Not available in the staged feed |
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

### 88. [AT2026ajju](https://www.wis-tns.org/object/2026ajju) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 1.03532° (62.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 5 days · 19.62 L |
| Latest public photometry | Not available in the staged feed |
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

### 89. [AT2026ajlv](https://www.wis-tns.org/object/2026ajlv) near IC 74

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
| Discovery | 2026-11-10T17:26:52Z · 7 days · 22.55 r |
| Latest public photometry | Not available in the staged feed |
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

### 90. [AT2026ajlw](https://www.wis-tns.org/object/2026ajlw) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.28359° (77.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T17:26:52Z · 7 days · 22.67 r |
| Latest public photometry | Not available in the staged feed |
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

### 91. [AT2026ajlx](https://www.wis-tns.org/object/2026ajlx) near IC 70

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
| Discovery | 2026-11-10T17:32:38Z · 7 days · 22.55 r |
| Latest public photometry | Not available in the staged feed |
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

### 92. [AT2026ajok](https://www.wis-tns.org/object/2026ajok) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 1.08961° (65.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 19.77 g |
| Latest public photometry | Not available in the staged feed |
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

### 93. [AT2026ajol](https://www.wis-tns.org/object/2026ajol) near NGC1340

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1340 as this object's host. The 1.17282° (70.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T07:00:58Z · 4 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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

### 94. [AT2026ajqe](https://www.wis-tns.org/object/2026ajqe) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.97158° (118.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:28:56Z · 3 days · 21.46 i |
| Latest public photometry | Not available in the staged feed |
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

### 95. [AT2026ajqf](https://www.wis-tns.org/object/2026ajqf) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.19498° (71.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 3 days · 23.7 r |
| Latest public photometry | Not available in the staged feed |
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

### 96. [AT2026ajqg](https://www.wis-tns.org/object/2026ajqg) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.43634° (86.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:04:44Z · 3 days · 22.41 z |
| Latest public photometry | Not available in the staged feed |
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

### 97. [AT2026ajqm](https://www.wis-tns.org/object/2026ajqm) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.42198° (85.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:14:05Z · 3 days · 21.44 i |
| Latest public photometry | Not available in the staged feed |
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

### 98. [AT2026ajqz](https://www.wis-tns.org/object/2026ajqz) near NGC1350

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1350 as this object's host. The 1.39326° (83.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 3 days · 22.81 r |
| Latest public photometry | Not available in the staged feed |
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

### 99. [AT2026ajra](https://www.wis-tns.org/object/2026ajra) near IC1993

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1993 as this object's host. The 1.92768° (115.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T13:22:42Z · 3 days · 21.72 r |
| Latest public photometry | Not available in the staged feed |
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

### 100. [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) near IC 2016

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
| Discovery | 2026-11-13T12:03:19Z · 4 days · 20.87 w |
| Latest public photometry | Not available in the staged feed |
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

### 101. [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) near IC5338

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5338 as this object's host. The 1.79914° (107.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:12:20Z · 3 days · 19.52 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 102. [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) near IC 17

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
| Discovery | 2026-11-13T21:33:37Z · 4 days · 19.68 L |
| Latest public photometry | Not available in the staged feed |
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

### 103. [AT2026ajss](https://www.wis-tns.org/object/2026ajss) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.55710° (93.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T17:22:33Z · 6 days · 22.86 g |
| Latest public photometry | Not available in the staged feed |
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

### 104. [AT2026ajti](https://www.wis-tns.org/object/2026ajti) near IC 1757

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
| Discovery | 2026-11-10T16:56:38Z · 7 days · 22.44 r |
| Latest public photometry | Not available in the staged feed |
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

### 105. [AT2026ajum](https://www.wis-tns.org/object/2026ajum) near IC 1540

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
| Discovery | 2026-11-11T12:56:09Z · 6 days · 22.35 g |
| Latest public photometry | Not available in the staged feed |
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

### 106. [AT2026ajux](https://www.wis-tns.org/object/2026ajux) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.74911° (104.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:17:24Z · 2 days · 22.92 i |
| Latest public photometry | Not available in the staged feed |
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

### 107. [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 2 days · 22.32 i |
| Latest public photometry | Not available in the staged feed |
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

### 108. [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 2 days · 22.34 i |
| Latest public photometry | Not available in the staged feed |
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

### 109. [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) near IC 1419

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
| Discovery | 2026-11-15T00:27:24Z · 2 days · 21.97 i |
| Latest public photometry | Not available in the staged feed |
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

### 110. [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 2 days · 22.71 i |
| Latest public photometry | Not available in the staged feed |
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

### 111. [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 20.46 i |
| Latest public photometry | Not available in the staged feed |
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

### 112. [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 2 days · 22.31 i |
| Latest public photometry | Not available in the staged feed |
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

### 113. [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.48 i |
| Latest public photometry | Not available in the staged feed |
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

### 114. [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 2 days · 21.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 115. [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.67055° (100.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.74 i |
| Latest public photometry | Not available in the staged feed |
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

### 116. [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) near IC 1419

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
| Discovery | 2026-11-15T00:28:09Z · 2 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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

### 117. [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.7 i |
| Latest public photometry | Not available in the staged feed |
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

### 118. [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.99 i |
| Latest public photometry | Not available in the staged feed |
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

### 119. [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.85355° (111.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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

### 120. [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.84 i |
| Latest public photometry | Not available in the staged feed |
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

### 121. [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.03799° (62.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.67 i |
| Latest public photometry | Not available in the staged feed |
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

### 122. [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 2 days · 21.31 i |
| Latest public photometry | Not available in the staged feed |
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

### 123. [AT2026ajws](https://www.wis-tns.org/object/2026ajws) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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

### 124. [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) near IC 1419

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
| Discovery | 2026-11-15T00:27:24Z · 2 days · 19.73 i |
| Latest public photometry | Not available in the staged feed |
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

### 125. [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.68 i |
| Latest public photometry | Not available in the staged feed |
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

### 126. [AT2026ajww](https://www.wis-tns.org/object/2026ajww) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 22.29 i |
| Latest public photometry | Not available in the staged feed |
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

### 127. [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 2 days · 23.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 128. [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) near IC1657

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.48817° (89.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T10:46:37Z · 5 days · 19.98 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.529929%20-31.428161&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026ajyl](https://www.wis-tns.org/object/2026ajyl) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 1.77291° (106.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T16:42:14Z · 6 days · 22.53 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.77291° · 106.37′ |
| Catalog description | NGC 5042 is an intermediate spiral galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background for is 1,697±22 km/s, which corresponds to a Hubble distance of 81.6 ± 5.8 Mly (25.03 ± 1.78 Mpc). However, 15 non redshift measurements give a much closer distance of 47.88 ± 2.37 Mly (14.680 ± 0.726 Mpc). It was discovered by British astronomer John Herschel on 25 March 1836. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1639 has the different designation NGC5042 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.413542%200.327408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026ajzi](https://www.wis-tns.org/object/2026ajzi) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.77766° (106.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:42:14Z · 7 days · 22.58 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.77766° · 106.66′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.795875%201.699603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026ajzj](https://www.wis-tns.org/object/2026ajzj) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 1.13242° (67.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:56:38Z · 7 days · 22.67 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.13242° · 67.95′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.857042%201.345936&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026akae](https://www.wis-tns.org/object/2026akae) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 1.02507° (61.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T18:30:14Z · 5 days · 21.79 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.02507° · 61.50′ |
| Catalog description | The Andromeda Galaxy is a barred spiral galaxy and is the nearest major galaxy to the Milky Way. It was originally named the Andromeda Nebula and is cataloged as Messier 31, M31, and NGC 224. Andromeda has a D25 isophotal diameter of about 46.56 kiloparsecs (152,000 light-years) and is approximately 765 kpc (2.5 million light-years) from Earth. The galaxy's name stems from the area of Earth's sky in which it appears, the constellation of Andromeda, which itself is named after the princess who was the wife of Perseus in Greek mythology. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akae) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.957125%2041.644789&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 133. [AT2026akah](https://www.wis-tns.org/object/2026akah) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.33761° (80.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T00:38:14Z · 4 days · 21.07 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.33761° · 80.26′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akah) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.105899%20-8.6737289&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 134. [AT2026akam](https://www.wis-tns.org/object/2026akam) near IC1657

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.69463° (101.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T10:12:24Z · 1 days · 19.7 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.69463° · 101.68′ |
| Catalog description | extremely, excessively faint, small in angular size, very much / magnitude extended |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akam) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.532685%20-32.882141&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 135. [AT2026akao](https://www.wis-tns.org/object/2026akao) near IC 1419

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1419 as this object's host. The 1.62610° (97.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:45:25Z · 2 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.62610° · 97.57′ |
| Catalog description | NGC 1198 is an elliptical galaxy in the constellation of Perseus. Its velocity with respect to the cosmic microwave background is 1419 ± 14 km/s, which corresponds to a Hubble distance of 20.92 ± 1.48 Mpc. It was discovered by French astronomer Édouard Stephan on 6 December 1880. This galaxy was also observed by the American astronomer Lewis Swift on 27 October 1888, and was later added to the Index Catalogue as IC 282. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1419 has the different designation NGC 1198 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akao) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.1023986%20-9.7648485&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 136. [AT2026akaq](https://www.wis-tns.org/object/2026akaq) near IC 2031

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2031 as this object's host. The 1.69253° (101.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T00:10:48Z · 1 days · 19.73 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 2031** · `IC 2031` |
| Catalog display name | IC 342 |
| Type / constellation | Galaxy · Eri |
| Catalog magnitude / angular size | — · 0.56′ × 0.48′ |
| Distance | 10.7 ly |
| Separation | 1.69253° · 101.55′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2031 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akaq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.86084%20-5.6863883&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 137. [AT2026akat](https://www.wis-tns.org/object/2026akat) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.52157° (91.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:04:03Z · 3 days · 21.55 z |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.52157° · 91.29′ |
| Catalog description | NGC 1527 is a lenticular galaxy in the constellation of Horologium. Its velocity with respect to the cosmic microwave background is 1,178±17 km/s, which corresponds to a Hubble distance of 56.7 ± 4.1 Mly (17.37 ± 1.27 Mpc). Additionally, 10 non-redshift measurements give a mean distance of 55.87 ± 3.62 Mly (17.130 ± 1.111 Mpc). It was discovered by Scottish astronomer James Dunlop on 28 September 1826. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akat) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=59.8342547%20-48.009595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 138. [AT2026ajdn](https://www.wis-tns.org/object/2026ajdn) near NGC7585

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7585 as this object's host. The 0.84567° (50.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:53:56Z · 18 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 139. [AT2026ajec](https://www.wis-tns.org/object/2026ajec) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.68536° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:37:26Z · 12 days · 23.01 g |
| Latest public photometry | Not available in the staged feed |
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

### 140. [AT2026ajed](https://www.wis-tns.org/object/2026ajed) near IC 173

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
| Discovery | 2026-11-05T15:56:09Z · 12 days · 22.77 g |
| Latest public photometry | Not available in the staged feed |
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

### 141. [AT2026ajee](https://www.wis-tns.org/object/2026ajee) near IC 1776

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
| Discovery | 2026-11-05T18:04:19Z · 12 days · 22.59 r |
| Latest public photometry | Not available in the staged feed |
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

### 142. [AT2026ajei](https://www.wis-tns.org/object/2026ajei) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.37997° (22.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:46:33Z · 10 days · 21.94 r |
| Latest public photometry | Not available in the staged feed |
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

### 143. [AT2026ajen](https://www.wis-tns.org/object/2026ajen) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 0.27076° (16.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:10:33Z · 9 days · 23.05 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajen) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=17.896792%20-0.930986&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026ajkp](https://www.wis-tns.org/object/2026ajkp) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 0.53744° (32.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:46:33Z · 9 days · 22.96 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.365667%20-0.880722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026ajkt](https://www.wis-tns.org/object/2026ajkt) near IC 234

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 234 as this object's host. The 0.57827° (34.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:46:33Z · 9 days · 23.15 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=37.710208%20-0.683942&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026ajlh](https://www.wis-tns.org/object/2026ajlh) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.60624° (36.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 10 days · 21.69 r |
| Latest public photometry | Not available in the staged feed |
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

### 147. [AT2026ajlj](https://www.wis-tns.org/object/2026ajlj) near IC 1749

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1749 as this object's host. The 0.61175° (36.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:53:45Z · 9 days · 22.54 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.506542%206.338597&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026ajlk](https://www.wis-tns.org/object/2026ajlk) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.75962° (45.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:34:04Z · 9 days · 22.61 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.523208%205.221917&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026ajmu](https://www.wis-tns.org/object/2026ajmu) near IC2421

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2421 as this object's host. The 0.41790° (25.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T21:30:14Z · 12 days · 21.64 g |
| Latest public photometry | Not available in the staged feed |
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

### 150. [AT2026ajmx](https://www.wis-tns.org/object/2026ajmx) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.72858° (43.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:28:19Z · 11 days · 22.35 g |
| Latest public photometry | Not available in the staged feed |
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

### 151. [AT2026ajnl](https://www.wis-tns.org/object/2026ajnl) near NGC1058

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1058 as this object's host. The 0.90832° (54.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:27:50Z · 19 days · 21.1 r |
| Latest public photometry | Not available in the staged feed |
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

### 152. [AT2026ajog](https://www.wis-tns.org/object/2026ajog) near IC 21

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 21 as this object's host. The 0.76970° (46.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:56:32Z · 9 days · 20.22 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajog) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=6.540778%20-0.324788&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026ajsm](https://www.wis-tns.org/object/2026ajsm) near IC1919

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1919 as this object's host. The 0.30868° (18.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T20:39:03Z · 19 days · 20.24 BG-q |
| Latest public photometry | Not available in the staged feed |
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

### 154. [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) near IC 74

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 74 as this object's host. The 0.60041° (36.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:04:48Z · 9 days · 22.82 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=15.904917%203.923525&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 155. [AT2026ajta](https://www.wis-tns.org/object/2026ajta) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 0.88977° (53.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:12:00Z · 9 days · 22.45 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajta) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.029833%20-0.7274&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 156. [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 0.82591° (49.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:45:07Z · 9 days · 21.43 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.480833%20-0.826333&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 157. [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) near IC178

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC178 as this object's host. The 0.93972° (56.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:24:57Z · 19 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
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

### 158. [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) near NGC 2964

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2964 as this object's host. The 0.25419° (15.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T21:54:43Z · 14 days · 20.75 r |
| Latest public photometry | Not available in the staged feed |
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

### 159. [AT2026ajyc](https://www.wis-tns.org/object/2026ajyc) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.74711° (44.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T17:46:50Z · 8 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2207 / IC 2163** · `IC 2548` |
| Catalog display name | NGC 2207 / IC 2163 |
| Type / constellation | Galaxy · Ant |
| Catalog magnitude / angular size | — · 2.17′ × 1.42′ |
| Distance | 81 ly |
| Separation | 0.74711° · 44.83′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.463753%20-35.864106&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 160. [AT2026ajyr](https://www.wis-tns.org/object/2026ajyr) near IC 1507

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1507 as this object's host. The 0.87774° (52.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:16:19Z · 18 days · 22.47 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.87774° · 52.66′ |
| Catalog description | IC 1613 is an irregular dwarf galaxy located on the outskirts of the Local group around 730 kiloparsecs from Earth in the constellation of Cetus near the star 26 Ceti. It has a low mass with its mass only being around 10^8 solar masses. It has played an important role in the calibration of the Cepheid variable period-luminosity relation for estimating distances. Other than the Magellanic Clouds, it is one of the few Local Group dwarf irregular galaxy where RR Lyrae-type variables have been observed; this factor, along with an unusually low abundance of interstellar dust both within IC 1613 and along the line of sight enable especially accurate distance estimates. IC 1613 was discovered in 1906 by Max Wolf, and is approaching Earth at 234 km/s. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1507 has the different designation IC 1613 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=355.83375%202.369481&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 161. [AT2026ajzb](https://www.wis-tns.org/object/2026ajzb) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.57000° (34.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 10 days · 21.83 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.57000° · 34.20′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.886958%203.653006&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 162. [AT2026ajzh](https://www.wis-tns.org/object/2026ajzh) near Local Group

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Local Group as this object's host. The 0.56395° (33.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:53:45Z · 8 days · 22.48 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.56395° · 33.84′ |
| Catalog description | The Local Group is the galaxy group that includes the Milky Way, where Earth is located. It consists of two collections of galaxies in a "dumbbell" shape; the Milky Way and its satellites form one lobe, and the Andromeda Galaxy and its satellites constitute the other. The two collections are separated by about 800 kiloparsecs (3×10^6 ly; 2×1019 km) and are moving toward one another with a velocity of 123 km/s. The center of the group is located at about 450 kpc (1.5 million ly) away from the Milky Way, placing it slightly closer to the Andromeda Galaxy by roughly 300 kpc (1 million ly), in which the latter may be more massive than the former in terms of mass. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=170.348375%205.270183&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 163. [AT2026ajnx](https://www.wis-tns.org/object/2026ajnx) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.40162° (24.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:16Z · 4 days · 21.82 i |
| Latest public photometry | Not available in the staged feed |
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

### 164. [AT2026ajqr](https://www.wis-tns.org/object/2026ajqr) near Messier 72 (M72)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 72 (M72) as this object's host. The 0.84769° (50.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:25:56Z · 3 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 165. [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.76418° (45.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 2 days · 21.93 i |
| Latest public photometry | Not available in the staged feed |
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

### 166. [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.83221° (49.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 2 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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

### 167. [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38606° (23.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 2 days · 21.24 i |
| Latest public photometry | Not available in the staged feed |
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

### 168. [AT2026akbc](https://www.wis-tns.org/object/2026akbc) near IC2030

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2030 as this object's host. The 0.58630° (35.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T10:56:11Z · 2 days · 20.89 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2030** · `IC2030` |
| Catalog display name | IC2030 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.58630° · 35.18′ |
| Catalog description | considerably faint, very small in angular size, extremely, excessively extended 135deg , suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=60.3800946%20-19.2508807&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 169. [AT2026aifu](https://www.wis-tns.org/object/2026aifu) near Lynds Bright Nebula 1025 (LBN1025)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1025 (LBN1025) as this object's host. The 1.13184° (67.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T10:32:52Z · 13 days · 19.01 g |
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

### 170. [AT2026ajye](https://www.wis-tns.org/object/2026ajye) near Lynds Bright Nebula 878 (LBN878)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 878 (LBN878) as this object's host. The 1.00364° (60.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:32:41Z · 9 days · 18.67 Clear |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Lynds Bright Nebula 878 (LBN878)** · `LBN878` |
| Catalog display name | Lynds Bright Nebula 878 (LBN878) |
| Type / constellation | HII · Orion |
| Catalog magnitude / angular size | — · 30′ × 5′ |
| Distance | — |
| Separation | 1.00364° · 60.22′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajye) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=84.983917%209.218778&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) near IC1401

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1401 as this object's host. The 1.09401° (65.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:14:32Z · 17 days · 19.8 i |
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

### 172. [AT2026aiit](https://www.wis-tns.org/object/2026aiit) near IC 536

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
| Discovery | 2026-10-26T12:16:17Z · 22 days · 20.1 g |
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

### 173. [AT2026ainu](https://www.wis-tns.org/object/2026ainu) near NGC1637

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1637 as this object's host. The 1.60141° (96.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T15:16:16Z · 15 days · 19.94 L |
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

### 174. [AT2026ajby](https://www.wis-tns.org/object/2026ajby) near IC48

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC48 as this object's host. The 1.83966° (110.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T03:31:31Z · 8 days · 20.2 g |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajby) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=10.8589676%20-6.3471302&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 175. [AT2026ajdj](https://www.wis-tns.org/object/2026ajdj) near NGC7727

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7727 as this object's host. The 1.24258° (74.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T00:59:51Z · 18 days · 21.21 r |
| Latest public photometry | Not available in the staged feed |
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

### 176. [AT2026ajdo](https://www.wis-tns.org/object/2026ajdo) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.40071° (84.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:15:54Z · 18 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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

### 177. [AT2026ajea](https://www.wis-tns.org/object/2026ajea) near IC 197

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
| Discovery | 2026-11-01T18:08:38Z · 16 days · 22.17 r |
| Latest public photometry | Not available in the staged feed |
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

### 178. [AT2026ajef](https://www.wis-tns.org/object/2026ajef) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.28974° (77.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:12:00Z · 10 days · 22.5 g |
| Latest public photometry | Not available in the staged feed |
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

### 179. [AT2026ajek](https://www.wis-tns.org/object/2026ajek) near IC 5241

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5241 as this object's host. The 1.64483° (98.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:19:40Z · 9 days · 22.65 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajek) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=341.855167%201.851428&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 180. [AT2026ajeo](https://www.wis-tns.org/object/2026ajeo) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 1.33383° (80.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:10:33Z · 9 days · 22.9 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajeo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.160292%20-0.116889&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 181. [AT2026ajff](https://www.wis-tns.org/object/2026ajff) near NGC289

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC289 as this object's host. The 1.00140° (60.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T10:29:48Z · 9 days · 20.17 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajff) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=12.0076788%20-31.2884437&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 182. [AT2026ajla](https://www.wis-tns.org/object/2026ajla) near IC 197

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
| Discovery | 2026-10-30T14:12:28Z · 18 days · 21.76 r |
| Latest public photometry | Not available in the staged feed |
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

### 183. [AT2026ajlb](https://www.wis-tns.org/object/2026ajlb) near IC 1507

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
| Discovery | 2026-11-04T17:21:07Z · 13 days · 22.99 g |
| Latest public photometry | Not available in the staged feed |
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

### 184. [AT2026ajld](https://www.wis-tns.org/object/2026ajld) near IC 3

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
| Discovery | 2026-11-05T15:12:57Z · 12 days · 23.02 g |
| Latest public photometry | Not available in the staged feed |
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

### 185. [AT2026ajle](https://www.wis-tns.org/object/2026ajle) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.84067° (110.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:43:12Z · 12 days · 23.03 g |
| Latest public photometry | Not available in the staged feed |
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

### 186. [AT2026ajlf](https://www.wis-tns.org/object/2026ajlf) near IC 173

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
| Discovery | 2026-11-05T15:53:16Z · 12 days · 22.81 g |
| Latest public photometry | Not available in the staged feed |
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

### 187. [AT2026ajlg](https://www.wis-tns.org/object/2026ajlg) near IC 1757

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
| Discovery | 2026-11-07T16:33:36Z · 10 days · 22.56 g |
| Latest public photometry | Not available in the staged feed |
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

### 188. [AT2026ajli](https://www.wis-tns.org/object/2026ajli) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.32202° (79.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 10 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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

### 189. [AT2026ajmf](https://www.wis-tns.org/object/2026ajmf) near IC 5241

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5241 as this object's host. The 1.90571° (114.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:19:40Z · 9 days · 22.59 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajmf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.312958%202.499219&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 190. [AT2026ajnc](https://www.wis-tns.org/object/2026ajnc) near NGC205

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC205 as this object's host. The 1.21009° (72.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:20:38Z · 10 days · 21.47 g |
| Latest public photometry | Not available in the staged feed |
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

### 191. [AT2026ajnt](https://www.wis-tns.org/object/2026ajnt) near NGC2859

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2859 as this object's host. The 1.90673° (114.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T21:51:50Z · 14 days · 20.27 r |
| Latest public photometry | Not available in the staged feed |
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

### 192. [AT2026ajnu](https://www.wis-tns.org/object/2026ajnu) near IC 189

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
| Discovery | 2026-11-04T20:32:38Z · 13 days · 21.73 r |
| Latest public photometry | Not available in the staged feed |
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

### 193. [AT2026ajpc](https://www.wis-tns.org/object/2026ajpc) near NGC 1954

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 1954 as this object's host. The 1.01085° (60.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T22:23:40Z · 18 days · 20.3 L |
| Latest public photometry | Not available in the staged feed |
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

### 194. [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.28167° (76.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T00:21:13Z · 9 days · 19.83 i |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=321.5223436%20-22.181237&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 195. [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.08432° (65.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:49:26Z · 8 days · 22.02 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=166.515792%20-1.084572&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 1.68238° (100.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:03:21Z · 16 days · 21.43 g |
| Latest public photometry | Not available in the staged feed |
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

### 197. [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) near IC509

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC509 as this object's host. The 1.28504° (77.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:23:02Z · 13 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
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

### 198. [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) near UFO Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify UFO Galaxy as this object's host. The 1.99519° (119.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:34:33Z · 13 days · 21.32 r |
| Latest public photometry | Not available in the staged feed |
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

### 199. [AT2026ajty](https://www.wis-tns.org/object/2026ajty) near IC2378

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2378 as this object's host. The 1.21289° (72.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:37:26Z · 13 days · 21.65 r |
| Latest public photometry | Not available in the staged feed |
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

### 200. [AT2026ajug](https://www.wis-tns.org/object/2026ajug) near IC1525

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1525 as this object's host. The 1.31062° (78.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:17:45Z · 10 days · 21.26 g |
| Latest public photometry | Not available in the staged feed |
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

### 201. [AT2026ajyi](https://www.wis-tns.org/object/2026ajyi) near IC 1776

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1776 as this object's host. The 1.14126° (68.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:37:55Z · 10 days · 22.68 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.14126° · 68.48′ |
| Catalog description | IC 2574, also known as Coddington's Nebula, is a dwarf spiral galaxy discovered by American astronomer Edwin Foster Coddington in 1898. Located in Ursa Major, a constellation in the northern sky, it is an outlying member of the M81 Group. It is believed that 90% of its mass is in the form of dark matter. IC 2574 does not show evidence of interaction with other galaxies. It is currently forming stars; a UV analysis showed clumps of star formation 85 to 500 light-years in size. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1776 has the different designation IC 2574 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.548375%205.256578&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026ajyt](https://www.wis-tns.org/object/2026ajyt) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.53398° (92.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:46:33Z · 18 days · 22.05 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.53398° · 92.04′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=21.122292%20-0.087567&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 203. [AT2026ajyx](https://www.wis-tns.org/object/2026ajyx) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.66353° (99.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:43:12Z · 12 days · 23 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.66353° · 99.81′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=22.195333%20-0.4595&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 204. [AT2026ajyy](https://www.wis-tns.org/object/2026ajyy) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 1.85756° (111.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 10 days · 20.1 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.85756° · 111.45′ |
| Catalog description | NGC 3169 is a spiral galaxy about 75 million light years away in the constellation Sextans. It has the morphological classification SA(s)a pec, which indicates this is a pure, unbarred spiral galaxy with tightly-wound arms and peculiar features. There is an asymmetrical spiral arm and an extended halo around the galaxy. It is a member of the NGC 3166 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.377875%203.059089&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 205. [AT2026ajyz](https://www.wis-tns.org/object/2026ajyz) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 1.27527° (76.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:35:02Z · 10 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.27527° · 76.52′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.547958%200.622792&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 206. [AT2026ajzc](https://www.wis-tns.org/object/2026ajzc) near Local Group

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Local Group as this object's host. The 1.45136° (87.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 10 days · 21.7 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.45136° · 87.08′ |
| Catalog description | The Local Group is the galaxy group that includes the Milky Way, where Earth is located. It consists of two collections of galaxies in a "dumbbell" shape; the Milky Way and its satellites form one lobe, and the Andromeda Galaxy and its satellites constitute the other. The two collections are separated by about 800 kiloparsecs (3×10^6 ly; 2×1019 km) and are moving toward one another with a velocity of 123 km/s. The center of the group is located at about 450 kpc (1.5 million ly) away from the Milky Way, placing it slightly closer to the Andromeda Galaxy by roughly 300 kpc (1 million ly), in which the latter may be more massive than the former in terms of mass. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.543208%204.864081&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 207. [AT2026ajzf](https://www.wis-tns.org/object/2026ajzf) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.39275° (83.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:46:33Z · 9 days · 21.83 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.39275° · 83.56′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=169.358292%202.185408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 208. [AT2026ajzg](https://www.wis-tns.org/object/2026ajzg) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 1.35429° (81.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:35:02Z · 8 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.35429° · 81.26′ |
| Catalog description | NGC 3169 is a spiral galaxy about 75 million light years away in the constellation Sextans. It has the morphological classification SA(s)a pec, which indicates this is a pure, unbarred spiral galaxy with tightly-wound arms and peculiar features. There is an asymmetrical spiral arm and an extended halo around the galaxy. It is a member of the NGC 3166 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.68425%204.814919&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 209. [AT2026ajzu](https://www.wis-tns.org/object/2026ajzu) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.04710° (62.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T15:10:04Z · 30 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.04710° · 62.83′ |
| Catalog description | IC 342 is an intermediate spiral galaxy in the constellation Camelopardalis, located relatively close to the Milky Way. Despite its size and actual brightness, its location behind dusty areas near the galactic equator makes it difficult to observe, leading to the nickname "The Hidden Galaxy", though it can readily be detected even with binoculars. If the galaxy were not obscured, it would be visible by naked eye. The dust makes it difficult to determine its precise distance; modern estimates range from about 7 million light-years (Mly) to about 11 Mly. The galaxy was discovered by William Frederick Denning in 1892. It is one of the brightest in the IC 342/Maffei Group, one of the closest galaxy groups to the Local Group. Edwin Hubble first thought it to be in the Local Group, but it was later determined not to be a member. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3 has the different designation IC 342 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.060708%200.566183&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 210. [AT2026ajzy](https://www.wis-tns.org/object/2026ajzy) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.30641° (78.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:40:48Z · 10 days · 22.9 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.30641° · 78.38′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.8095%204.917969&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 211. [AT2026akaa](https://www.wis-tns.org/object/2026akaa) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.98192° (118.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:56:38Z · 8 days · 21.91 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.98192° · 118.92′ |
| Catalog description | NGC 3640 is an elliptical galaxy located in the constellation Leo. It is located at a distance of circa 75 million light years from Earth, which, given its apparent dimensions, means that NGC 3640 is about 90,000 light years across. It was discovered by William Herschel on February 23, 1784. It is a member of the NGC 3640 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akaa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=172.149%202.582742&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 212. [AT2026akac](https://www.wis-tns.org/object/2026akac) near IC187

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC187 as this object's host. The 1.14616° (68.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T20:08:09Z · 9 days · 21.88 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.14616° · 68.77′ |
| Catalog description | most extremely faint, round |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akac) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.543667%2027.61725&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 213. [AT2026ajlt](https://www.wis-tns.org/object/2026ajlt) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.25864° (75.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:19:40Z · 7 days · 22.76 g |
| Latest public photometry | Not available in the staged feed |
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

### 214. [AT2026ajma](https://www.wis-tns.org/object/2026ajma) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 1.52330° (91.40′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T15:36:00Z · 6 days · 22.33 r |
| Latest public photometry | Not available in the staged feed |
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

### 215. [AT2026ajob](https://www.wis-tns.org/object/2026ajob) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.67540° (100.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:16Z · 4 days · 22.59 i |
| Latest public photometry | Not available in the staged feed |
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

### 216. [AT2026ajou](https://www.wis-tns.org/object/2026ajou) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.43468° (86.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T20:16:00Z · 5 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
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

### 217. [AT2026ajpi](https://www.wis-tns.org/object/2026ajpi) near NGC7526

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7526 as this object's host. The 1.96789° (118.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T00:22:48Z · 5 days · 22.62 i |
| Latest public photometry | Not available in the staged feed |
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

### 218. [AT2026ajpy](https://www.wis-tns.org/object/2026ajpy) near Messier 30 (M30)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 30 (M30) as this object's host. The 1.04427° (62.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T02:12:03Z · 6 days · 21.42 i |
| Latest public photometry | Not available in the staged feed |
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

### 219. [AT2026ajqb](https://www.wis-tns.org/object/2026ajqb) near Messier 72 (M72)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 72 (M72) as this object's host. The 1.44459° (86.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T00:25:56Z · 3 days · 21.61 i |
| Latest public photometry | Not available in the staged feed |
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

### 220. [AT2026ajqn](https://www.wis-tns.org/object/2026ajqn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.39431° (83.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T03:20:11Z · 3 days · 22.45 z |
| Latest public photometry | Not available in the staged feed |
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

### 221. [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) near NGC3578

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3578 as this object's host. The 1.46782° (88.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T05:54:36Z · 2 days · 19.77 L |
| Latest public photometry | Not available in the staged feed |
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

### 222. [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.30353° (78.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T00:31:47Z · 7 days · 21.8 i |
| Latest public photometry | Not available in the staged feed |
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

### 223. [AT2026ajur](https://www.wis-tns.org/object/2026ajur) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.05093° (63.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 2 days · 23.23 i |
| Latest public photometry | Not available in the staged feed |
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

### 224. [AT2026ajve](https://www.wis-tns.org/object/2026ajve) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.56732° (94.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 22.03 i |
| Latest public photometry | Not available in the staged feed |
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

### 225. [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.82559° (109.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 21.75 i |
| Latest public photometry | Not available in the staged feed |
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

### 226. [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.62885° (97.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 2 days · 22.52 i |
| Latest public photometry | Not available in the staged feed |
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

### 227. [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.34031° (80.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 2 days · 21.84 i |
| Latest public photometry | Not available in the staged feed |
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

### 228. [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.88540° (113.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 2 days · 20.66 i |
| Latest public photometry | Not available in the staged feed |
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

### 229. [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.21470° (72.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 2 days · 21.83 i |
| Latest public photometry | Not available in the staged feed |
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

### 230. [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.66580° (99.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:27:24Z · 2 days · 21.12 i |
| Latest public photometry | Not available in the staged feed |
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

### 231. [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.17313° (70.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 2 days · 21.76 i |
| Latest public photometry | Not available in the staged feed |
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

### 232. [AT2026aiat](https://www.wis-tns.org/object/2026aiat) near Collinder 163 (CR163)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 163 (CR163) as this object's host. The 0.39277° (23.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T17:13:14Z · 16 days · 19.61 L |
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

### 233. [AT2026aiko](https://www.wis-tns.org/object/2026aiko) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38092° (22.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:02:26Z · 11 days · 19.85 r |
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

### 234. [SN2026airg](https://www.wis-tns.org/object/2026airg) near Sharpless 260 (SH2-260)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Sharpless 260 (SH2-260) as this object's host. The 1.20103° (72.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.029 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T09:34:22Z · 10 days · 19.93 r |
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

### 235. [AT2026aivj](https://www.wis-tns.org/object/2026aivj) near IC1547

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1547 as this object's host. The 0.56558° (33.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T08:18:10Z · 12 days · 20.47 g |
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

### 236. [AT2026ajdy](https://www.wis-tns.org/object/2026ajdy) near NGC272

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC272 as this object's host. The 0.82818° (49.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T06:13:04Z · 10 days · 20.06 r |
| Latest public photometry | Not available in the staged feed |
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

### 237. [AT2026ajlm](https://www.wis-tns.org/object/2026ajlm) near NGC7613

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7613 as this object's host. The 0.70355° (42.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T14:38:24Z · 9 days · 22.24 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.558917%200.860436&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 238. [AT2026ajmh](https://www.wis-tns.org/object/2026ajmh) near IC1665

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1665 as this object's host. The 0.81988° (49.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T19:20:38Z · 29 days · 21.78 g |
| Latest public photometry | Not available in the staged feed |
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

### 239. [AT2026ajmi](https://www.wis-tns.org/object/2026ajmi) near NGC843

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC843 as this object's host. The 0.79289° (47.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-19T21:30:14Z · 29 days · 21.94 g |
| Latest public photometry | Not available in the staged feed |
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

### 240. [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) near Lynds Bright Nebula 439 (LBN439)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 439 (LBN439) as this object's host. The 0.79678° (47.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T19:43:55Z · 5 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
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

### 241. [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) near IC111

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC111 as this object's host. The 0.80147° (48.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:48:00Z · 10 days · 22.16 g |
| Latest public photometry | Not available in the staged feed |
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

### 242. [AT2026ajup](https://www.wis-tns.org/object/2026ajup) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 0.84314° (50.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:27:50Z · 14 days · 21.25 r |
| Latest public photometry | Not available in the staged feed |
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

### 243. [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.53340° (32.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 17 days · 23.8 i |
| Latest public photometry | Not available in the staged feed |
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

### 244. [AT2026ajym](https://www.wis-tns.org/object/2026ajym) near NGC7613

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7613 as this object's host. The 0.51096° (30.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:59:02Z · 19 days · 22.1 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.51096° · 30.66′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajym) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=349.875917%20-0.311867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 245. [AT2026ajzw](https://www.wis-tns.org/object/2026ajzw) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.85066° (51.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:32:09Z · 16 days · 22.42 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.85066° · 51.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.991917%20-0.098486&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 246. [AT2026ahhj](https://www.wis-tns.org/object/2026ahhj) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.72039° (103.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:23:06Z · 18 days · 22.31 r |
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

### 247. [AT2026ajdm](https://www.wis-tns.org/object/2026ajdm) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 1.32204° (79.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:54:36Z · 18 days · 22.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 248. [AT2026ajeq](https://www.wis-tns.org/object/2026ajeq) near NGC2284

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2284 as this object's host. The 1.44095° (86.46′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-22T21:14:24Z · 26 days · 21.42 r |
| Latest public photometry | Not available in the staged feed |
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

### 249. [AT2026ajet](https://www.wis-tns.org/object/2026ajet) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.97492° (118.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-26T20:41:16Z · 22 days · 20.96 r |
| Latest public photometry | Not available in the staged feed |
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

### 250. [AT2026ajev](https://www.wis-tns.org/object/2026ajev) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.73662° (104.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T20:21:07Z · 16 days · 21.31 g |
| Latest public photometry | Not available in the staged feed |
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

### 251. [AT2026ajfn](https://www.wis-tns.org/object/2026ajfn) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.16150° (69.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T03:13:02Z · 18 days · 23.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 252. [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.09787° (65.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:01:26Z · 11 days · 20.91 g |
| Latest public photometry | Not available in the staged feed |
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

### 253. [AT2026ajkm](https://www.wis-tns.org/object/2026ajkm) near Lynds Bright Nebula 418 (LBN418)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 418 (LBN418) as this object's host. The 1.03018° (61.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:42:43Z · 7 days · 21.9 g |
| Latest public photometry | Not available in the staged feed |
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

### 254. [AT2026ajkq](https://www.wis-tns.org/object/2026ajkq) near IC1651

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1651 as this object's host. The 1.80188° (108.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-27T17:25:26Z · 21 days · 20.77 r |
| Latest public photometry | Not available in the staged feed |
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

### 255. [AT2026ajlo](https://www.wis-tns.org/object/2026ajlo) near NGC7565

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7565 as this object's host. The 1.97938° (118.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:24:28Z · 9 days · 22.65 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajlo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=347.671625%201.333197&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 256. [AT2026ajlq](https://www.wis-tns.org/object/2026ajlq) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.81927° (109.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:07Z · 7 days · 22.86 g |
| Latest public photometry | Not available in the staged feed |
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

### 257. [AT2026ajmr](https://www.wis-tns.org/object/2026ajmr) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.15457° (69.27′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:10:33Z · 14 days · 21.98 r |
| Latest public photometry | Not available in the staged feed |
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

### 258. [AT2026ajmw](https://www.wis-tns.org/object/2026ajmw) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.42390° (85.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:26:52Z · 11 days · 21.36 g |
| Latest public photometry | Not available in the staged feed |
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

### 259. [AT2026ajne](https://www.wis-tns.org/object/2026ajne) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.30710° (78.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:52:19Z · 8 days · 21.45 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajne) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.3475%2041.237222&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 260. [AT2026ajng](https://www.wis-tns.org/object/2026ajng) near IC2350

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2350 as this object's host. The 1.54892° (92.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:41:16Z · 8 days · 20.81 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajng) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.268375%2021.094431&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 261. [AT2026ajnh](https://www.wis-tns.org/object/2026ajnh) near Goblet of Fire nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Goblet of Fire nebula as this object's host. The 1.85337° (111.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T14:45:36Z · 7 days · 20.62 g |
| Latest public photometry | Not available in the staged feed |
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

### 262. [AT2026ajnw](https://www.wis-tns.org/object/2026ajnw) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 1.48474° (89.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T20:25:26Z · 11 days · 20.74 g |
| Latest public photometry | Not available in the staged feed |
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

### 263. [AT2026ajom](https://www.wis-tns.org/object/2026ajom) near Lynds Bright Nebula 968 (LBN968)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 968 (LBN968) as this object's host. The 1.64919° (98.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T09:01:19Z · 6 days · 20.3 r |
| Latest public photometry | Not available in the staged feed |
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

### 264. [AT2026ajpe](https://www.wis-tns.org/object/2026ajpe) near IC2069

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2069 as this object's host. The 1.57505° (94.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T06:43:05Z · 12 days · 23.13 r |
| Latest public photometry | Not available in the staged feed |
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

### 265. [AT2026ajpl](https://www.wis-tns.org/object/2026ajpl) near IC5344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5344 as this object's host. The 1.63978° (98.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T02:05:52Z · 10 days · 21.06 r |
| Latest public photometry | Not available in the staged feed |
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

### 266. [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) near Lynds Bright Nebula 484 (LBN484)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 484 (LBN484) as this object's host. The 1.74355° (104.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:18:12Z · 3 days · 19.58 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 267. [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) near Lynds Bright Nebula 856 (LBN856)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 856 (LBN856) as this object's host. The 1.86922° (112.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T11:55:40Z · 5 days · 19.74 L |
| Latest public photometry | Not available in the staged feed |
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

### 268. [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) near NGC728

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC728 as this object's host. The 1.25970° (75.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:32:09Z · 9 days · 22.88 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.1305%203.020175&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 269. [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.48459° (89.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T14:25:26Z · 11 days · 23.61 g |
| Latest public photometry | Not available in the staged feed |
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

### 270. [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) near NGC3387

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3387 as this object's host. The 1.71033° (102.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:37:55Z · 9 days · 21.48 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajtd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.638125%204.019469&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 271. [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) near NGC737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC737 as this object's host. The 1.51249° (90.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T19:37:55Z · 14 days · 21.87 r |
| Latest public photometry | Not available in the staged feed |
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

### 272. [AT2026ajub](https://www.wis-tns.org/object/2026ajub) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.29090° (77.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T21:28:48Z · 12 days · 21.61 g |
| Latest public photometry | Not available in the staged feed |
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

### 273. [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.74562° (104.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:07:47Z · 8 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajwy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.096358%20-3.912106&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 274. [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) near NGC1498

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1498 as this object's host. The 1.41273° (84.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T17:26:25Z · 8 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.852439%20-12.76826&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 275. [AT2026ajxz](https://www.wis-tns.org/object/2026ajxz) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.08910° (65.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:25:02Z · 5 days · 20.27 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.08910° · 65.35′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajxz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.543772%201.188224&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 276. [AT2026ajyk](https://www.wis-tns.org/object/2026ajyk) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.88407° (113.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:07Z · 7 days · 22.81 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.88407° · 113.04′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajyk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.112417%201.943786&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 277. [AT2026akak](https://www.wis-tns.org/object/2026akak) near IC 5364

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5364 as this object's host. The 1.64295° (98.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T10:14:57Z · 11 days · 20.3 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 5364** · `IC 5364` |
| Catalog display name | NGC 5555 |
| Type / constellation | CiG · Scl |
| Catalog magnitude / angular size | — · 1.5′ |
| Distance | 538.83 ly |
| Separation | 1.64295° · 98.58′ |
| Catalog description | NGC 5555 is a spiral galaxy located in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 11200 ± 20 km/s, which corresponds to a Hubble distance of 165.20 ± 11.57 Mpc. It was originally discovered in 1886 by the American astronomer, Ormond Stone. NGC 5555 is situated close to the celestial equator and given its visual magnitude of 15.53, NGC 5555 is visible only through long exposure photography. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5364 has the different designation NGC 5555 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akak) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=0.854478%20-28.437118&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 278. [AT2026aigg](https://www.wis-tns.org/object/2026aigg) near Lynds Bright Nebula 910 (LBN910)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 910 (LBN910) as this object's host. The 0.77477° (46.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:05:05Z · 15 days · 20.26 g |
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

### 279. [AT2026ajts](https://www.wis-tns.org/object/2026ajts) near Lynds Bright Nebula 891 (LBN891)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 891 (LBN891) as this object's host. The 0.64768° (38.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:48:00Z · 14 days · 20.91 r |
| Latest public photometry | Not available in the staged feed |
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

### 280. [SN2026aeff](https://www.wis-tns.org/object/2026aeff) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 33/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.95543° (117.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN II |
| Redshift | 0.082674911233642 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T12:30:18Z · 47 days · 19.25 r |
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

### 281. [AT2026absv](https://www.wis-tns.org/object/2026absv) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 28/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.10562° (66.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-14T10:32:09Z · 64 days · 19.48 L |
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

### 282. [AT2026aeka](https://www.wis-tns.org/object/2026aeka) near IC 1876

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
| Discovery | 2026-09-18T18:53:26Z · 60 days · 20.21 L |
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

### 283. [AT2026aiem](https://www.wis-tns.org/object/2026aiem) near Lynds Bright Nebula 556 (LBN556)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 556 (LBN556) as this object's host. The 1.55459° (93.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T04:28:06Z · 12 days · 19.89 r |
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

### 284. [AT2026aimd](https://www.wis-tns.org/object/2026aimd) near Collinder 65 (CR65)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 65 (CR65) as this object's host. The 1.83171° (109.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:37:25Z · 11 days · 20.38 i |
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

### 285. [AT2026ajkk](https://www.wis-tns.org/object/2026ajkk) near Lynds Bright Nebula 688 (LBN688)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 688 (LBN688) as this object's host. The 1.01865° (61.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:58:04Z · 10 days · 21.78 g |
| Latest public photometry | Not available in the staged feed |
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

### 286. [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 20/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.70237° (42.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.087 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T05:00:26Z · 43 days · 19.82 r |
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

### 287. [AT2026abyt](https://www.wis-tns.org/object/2026abyt) near IC2170

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 18/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2170 as this object's host. The 1.73601° (104.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-17T05:48:58Z · 61 days · 19.14 L |
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

### 288. [AT2026adsv](https://www.wis-tns.org/object/2026adsv) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 0.88938° (53.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T07:01:55Z · 47 days · 20.83 w |
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

### 289. [AT2026ajku](https://www.wis-tns.org/object/2026ajku) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 0.71371° (42.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-08T19:58:04Z · 70 days · 22.1 r |
| Latest public photometry | Not available in the staged feed |
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

### 290. [AT2026ajky](https://www.wis-tns.org/object/2026ajky) near IC 197

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
| Discovery | 2026-10-09T16:06:14Z · 39 days · 22.61 r |
| Latest public photometry | Not available in the staged feed |
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

### 291. [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 0.76155° (45.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-13T16:59:31Z · 65 days · 20.79 r |
| Latest public photometry | Not available in the staged feed |
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

### 292. [SN2026afgl](https://www.wis-tns.org/object/2026afgl) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.83228° (109.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIn |
| Redshift | 0.105 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-11T05:50:16Z · 37 days · 19.63 L |
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

### 293. [AT2026aawo](https://www.wis-tns.org/object/2026aawo) near IC 1341

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
| Discovery | 2026-09-03T10:40:30Z · 75 days · 20.08 L |
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

### 294. [AT2026adsx](https://www.wis-tns.org/object/2026adsx) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.56536° (93.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-01T07:04:43Z · 47 days · 20.67 w |
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

### 295. [AT2026agac](https://www.wis-tns.org/object/2026agac) near IC 1417

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
| Discovery | 2026-10-10T07:53:22Z · 38 days · 20.92 w |
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

### 296. [AT2026ajkn](https://www.wis-tns.org/object/2026ajkn) near IC 1639

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
| Discovery | 2026-10-13T15:11:31Z · 35 days · 22.34 r |
| Latest public photometry | Not available in the staged feed |
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

### 297. [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) near IC 1507

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
| Discovery | 2026-09-13T02:53:11Z · 65 days · 22.85 i |
| Latest public photometry | Not available in the staged feed |
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

### 298. [AT2026ajyo](https://www.wis-tns.org/object/2026ajyo) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 1.29924° (77.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T17:24:00Z · 31 days · 22.17 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.29924° · 77.95′ |
| Catalog description | IC 3418 is a galaxy in the constellation Virgo. It is most well noted for its tidal tail, which formed after the galaxy collided with the Virgo Cluster some 54 million light years from Earth. The galaxy is home to many starburst regions. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 173 has the different designation IC 3418 as its display name.

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.101458%200.615192&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 299. [AT2026aflb](https://www.wis-tns.org/object/2026aflb) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 5/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.94348° (56.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-09T15:02:52Z · 39 days · 22.4 r |
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

### 300. [AT2026ajmg](https://www.wis-tns.org/object/2026ajmg) near NGC2464

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2464 as this object's host. The 1.82991° (109.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-04T22:20:38Z · 44 days · 20.17 r |
| Latest public photometry | Not available in the staged feed |
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
