# TNS transient opportunity review — 2026-11-21

> Review queue only. Nothing in this report is published as app-facing metadata or a notification.

AstroGuide catalog proximity is a smart-scope relevance filter. A **near-field match** is angular proximity only; it is not a host or physical association unless TNS explicitly supplies matching host evidence.

**Review evidence hash:** `cf877b556c589f4c`. This dated queue remains immutable evidence and keeps `reviewDecision` pending. Curated status lives in `transient-review-decisions-v1.json`; changed evidence resets an existing decision to pending. The generated runtime package includes only still-active approved decisions, so merging a synchronized review PR publishes that approved set through dynamic metadata.

## Summary

- 302 review opportunities: 11 urgent, 291 watch, 0 expired
- Recommendations: 8 approve, 294 hold, 0 reject
- 302 eligible opportunities retained; requested summary limit: all (no candidate truncation)
- 653 staged rows collapsed to 625 unique TNS objects (28 duplicate/change rows)
- 1 known contaminants rejected before cross-match

## Review queue

| Priority | Candidate | Type | Age | Disc. mag | AstroGuide subject | Separation | Relationship | Score | Action |
|---|---|---|---:|---:|---|---:|---|---:|---|
| urgent | [SN2026ahvi](https://www.wis-tns.org/object/2026ahvi) | SN Ia | 19 | 16.1 | NGC4216 (Galaxy) | 0.39321° | near-field match | 100 | approve |
| urgent | [AT2026ajxw](https://www.wis-tns.org/object/2026ajxw) | transient_candidate | 6 | 18.22 | IC750 (Galaxy) | 0.12317° | near-field match | 100 | approve |
| urgent | [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) | SN | 18 | 18.49 | IC 2405 (Galaxy) | 0.45058° | near-field match | 97 | hold |
| urgent | [AT2026akhh](https://www.wis-tns.org/object/2026akhh) | transient_candidate | 4 | 18.34 | IC2013 (Nebula) | 0.18157° | near-field match | 93 | approve |
| urgent | [AT2026akfo](https://www.wis-tns.org/object/2026akfo) | transient_candidate | 3 | 17.73 | IC 4415 (Galaxy) | 0.38149° | near-field match | 90 | hold |
| urgent | [AT2026akhc](https://www.wis-tns.org/object/2026akhc) | transient_candidate | 2 | 18.43 | IC 4168 (Galaxy) | 1.48969° | near-field match | 83 | hold |
| urgent | [AT2026akhs](https://www.wis-tns.org/object/2026akhs) | transient_candidate | 3 | 18.03 | NGC6958 (Galaxy) | 1.67482° | near-field match | 83 | approve |
| urgent | [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) | transient_candidate | 7 | 18.22 | IC765 (Nebula) | 0.75222° | near-field match | 80 | approve |
| urgent | [TDE2026akgn](https://www.wis-tns.org/object/2026akgn) | TDE-featureless | 28 | 17.86 | NGC1458 (Nebula) | 1.60630° | near-field match | 80 | approve |
| urgent | [AT2026aklg](https://www.wis-tns.org/object/2026aklg) | transient_candidate | 10 | 17.75 | NGC5204 (Galaxy) | 1.43417° | near-field match | 75 | approve |
| urgent | [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) | transient_candidate | 13 | 18.38 | IC656 (Nebula) | 0.87219° | near-field match | 72 | approve |
| watch | [SN2026akbo](https://www.wis-tns.org/object/2026akbo) | SN Ia | 4 | 18.76 | NGC3344 (Galaxy) | 0.96186° | near-field match | 95 | hold |
| watch | [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) | transient_candidate | 8 | 19.32 | NGC2276 (Galaxy) | 0.19202° | near-field match | 85 | hold |
| watch | [SN2026ahuu](https://www.wis-tns.org/object/2026ahuu) | SN Ia | 19 | 18.69 | IC449 (Galaxy) | 1.92939° | near-field match | 80 | hold |
| watch | [SN2026ahze](https://www.wis-tns.org/object/2026ahze) | SN Ia | 18 | 18.71 | NGC797 (Galaxy) | 1.92287° | near-field match | 80 | hold |
| watch | [AT2026ajxv](https://www.wis-tns.org/object/2026ajxv) | transient_candidate | 7 | 19.13 | NGC 3277 (Galaxy) | 0.80128° | near-field match | 80 | hold |
| watch | [AT2026akhu](https://www.wis-tns.org/object/2026akhu) | transient_candidate | 3 | 19.35 | NGC2325 (Galaxy) | 0.61029° | near-field match | 80 | hold |
| watch | [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) | transient_candidate | 7 | 19.45 | IC1733 (Galaxy) | 1.11166° | near-field match | 73 | hold |
| watch | [AT2026ajva](https://www.wis-tns.org/object/2026ajva) | transient_candidate | 6 | 21.81 | NGC 3561 (Galaxy) | 0.19660° | near-field match | 73 | hold |
| watch | [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) | transient_candidate | 6 | 22.15 | NGC 3561 (Galaxy) | 0.19359° | near-field match | 73 | hold |
| watch | [AT2026ajyd](https://www.wis-tns.org/object/2026ajyd) | transient_candidate | 5 | 19.16 | IC600 (Galaxy) | 1.36888° | near-field match | 73 | hold |
| watch | [AT2026akaz](https://www.wis-tns.org/object/2026akaz) | transient_candidate | 5 | 19.3 | Caldwell 3 (C3) (Galaxy) | 1.12593° | near-field match | 73 | hold |
| watch | [AT2026akgx](https://www.wis-tns.org/object/2026akgx) | transient_candidate | 2 | 19.28 | NGC1569 (Galaxy) | 1.05967° | near-field match | 73 | hold |
| watch | [AT2026akhd](https://www.wis-tns.org/object/2026akhd) | transient_candidate | 3 | 18.95 | IC625 (Galaxy) | 1.99202° | near-field match | 73 | hold |
| watch | [AT2026akhf](https://www.wis-tns.org/object/2026akhf) | transient_candidate | 2 | 19.45 | NGC3726 (Galaxy) | 1.78481° | near-field match | 73 | hold |
| watch | [AT2026akju](https://www.wis-tns.org/object/2026akju) | transient_candidate | 4 | 22.1 | NGC741 (Galaxy) | 0.15603° | near-field match | 73 | hold |
| watch | [AT2026agub](https://www.wis-tns.org/object/2026agub) | transient_candidate | 27 | 19.46 | Andromeda Galaxy (Galaxy) | 0.34859° | near-field match | 72 | hold |
| watch | [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) | transient_candidate | 8 | 19.37 | NGC2549 (Galaxy) | 0.59331° | near-field match | 72 | hold |
| watch | [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) | transient_candidate | 8 | 19.35 | NGC2768 (Galaxy) | 0.41880° | near-field match | 72 | hold |
| watch | [AT2026akit](https://www.wis-tns.org/object/2026akit) | transient_candidate | 3 | 19.03 | IC1560 (Nebula) | 0.48582° | near-field match | 70 | hold |
| watch | [SN2026ajsm](https://www.wis-tns.org/object/2026ajsm) | SN Ia | 23 | 20.24 | IC1919 (Galaxy) | 0.30868° | near-field match | 67 | hold |
| watch | [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) | transient_candidate | 23 | 19.41 | IC1933 (Galaxy) | 1.58832° | near-field match | 65 | hold |
| watch | [AT2026ahxx](https://www.wis-tns.org/object/2026ahxx) | transient_candidate | 27 | 19.86 | IC310 (Galaxy) | 0.17684° | near-field match | 65 | hold |
| watch | [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) | transient_candidate | 9 | 19.46 | NGC1169 (Galaxy) | 1.01795° | near-field match | 65 | hold |
| watch | [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) | transient_candidate | 9 | 19 | IC486 (Galaxy) | 1.22917° | near-field match | 65 | hold |
| watch | [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) | transient_candidate | 8 | 19.27 | IC5261 (Galaxy) | 1.21834° | near-field match | 65 | hold |
| watch | [AT2026ajxy](https://www.wis-tns.org/object/2026ajxy) | transient_candidate | 12 | 19.88 | IC 1894 (Galaxy) | 0.17650° | near-field match | 65 | hold |
| watch | [AT2026akeu](https://www.wis-tns.org/object/2026akeu) | transient_candidate | 9 | 19.38 | IC 3484 (Galaxy) | 1.32084° | near-field match | 65 | hold |
| watch | [AT2026akev](https://www.wis-tns.org/object/2026akev) | transient_candidate | 9 | 19.05 | IC 876 (Galaxy) | 1.55431° | near-field match | 65 | hold |
| watch | [AT2026akhx](https://www.wis-tns.org/object/2026akhx) | transient_candidate | 14 | 21.13 | NGC3640 (Galaxy) | 0.12692° | near-field match | 65 | hold |
| watch | [AT2026akir](https://www.wis-tns.org/object/2026akir) | transient_candidate | 10 | 20.71 | NGC4450 (Galaxy) | 0.23305° | near-field match | 65 | hold |
| watch | [AT2026akjq](https://www.wis-tns.org/object/2026akjq) | transient_candidate | 19 | 19.97 | NGC3348 (Galaxy) | 0.04326° | near-field match | 65 | hold |
| watch | [AT2026ajru](https://www.wis-tns.org/object/2026ajru) | transient_candidate | 7 | 18.7 | Collinder 176 (CR176) (Open cluster) | 1.06889° | near-field match | 63 | hold |
| watch | [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) | transient_candidate | 6 | 22.79 | IC5194 (Nebula) | 0.13206° | near-field match | 63 | hold |
| watch | [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) | transient_candidate | 6 | 21.79 | NGC894 (Nebula) | 0.00471° | near-field match | 63 | hold |
| watch | [AT2026ajxu](https://www.wis-tns.org/object/2026ajxu) | transient_candidate | 6 | 19.22 | Collinder 27 (CR27) (Open cluster) | 1.69919° | near-field match | 63 | hold |
| watch | [AT2026akap](https://www.wis-tns.org/object/2026akap) | transient_candidate | 5 | 19.32 | Ghost of Jupiter (Planetary nebula) | 1.78164° | near-field match | 63 | hold |
| watch | [AT2026akfn](https://www.wis-tns.org/object/2026akfn) | transient_candidate | 3 | 19.35 | IC 4287 (CiG) | 1.37018° | near-field match | 63 | hold |
| watch | [AT2026akgf](https://www.wis-tns.org/object/2026akgf) | transient_candidate | 4 | 19.4 | Butterfly nebula (reflection nebula) | 1.66856° | near-field match | 63 | hold |
| watch | [AT2026akhl](https://www.wis-tns.org/object/2026akhl) | transient_candidate | 2 | 18.85 | NGC2886 (Nebula) | 1.56605° | near-field match | 63 | hold |
| watch | [AT2026akhq](https://www.wis-tns.org/object/2026akhq) | transient_candidate | 2 | 19.21 | IC3668 (Nebula) | 1.11334° | near-field match | 63 | hold |
| watch | [AT2026akiv](https://www.wis-tns.org/object/2026akiv) | transient_candidate | 1 | 20 | IC488 (Nebula) | 0.01538° | near-field match | 63 | hold |
| watch | [AT2026akiw](https://www.wis-tns.org/object/2026akiw) | transient_candidate | 1 | 19.34 | IC656 (Nebula) | 1.14126° | near-field match | 63 | hold |
| watch | [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) | transient_candidate | 7 | 19.17 | van den Bergh 12 (VDB12) (Nebula) | 0.51247° | near-field match | 62 | hold |
| watch | [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) | transient_candidate | 7 | 20.85 | Messier 81 (Galaxy) | 0.68539° | near-field match | 60 | hold |
| watch | [AT2026ajri](https://www.wis-tns.org/object/2026ajri) | transient_candidate | 7 | 21.44 | IC 1540 (Galaxy) | 0.82912° | near-field match | 60 | hold |
| watch | [AT2026ajut](https://www.wis-tns.org/object/2026ajut) | transient_candidate | 6 | 22.82 | NGC 3561 (Galaxy) | 0.37521° | near-field match | 60 | hold |
| watch | [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) | transient_candidate | 6 | 22.02 | NGC 3561 (Galaxy) | 0.41178° | near-field match | 60 | hold |
| watch | [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) | transient_candidate | 6 | 22.11 | IC 1417 (Galaxy) | 0.66407° | near-field match | 60 | hold |
| watch | [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) | transient_candidate | 6 | 22.2 | IC 1417 (Galaxy) | 0.99563° | near-field match | 60 | hold |
| watch | [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) | transient_candidate | 6 | 21.89 | IC 1417 (Galaxy) | 0.95089° | near-field match | 60 | hold |
| watch | [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) | transient_candidate | 6 | 22.91 | IC 1419 (Galaxy) | 0.31675° | near-field match | 60 | hold |
| watch | [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) | transient_candidate | 6 | 21.59 | IC 1417 (Galaxy) | 0.46768° | near-field match | 60 | hold |
| watch | [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) | transient_candidate | 6 | 19.72 | IC2560 (Galaxy) | 0.97287° | near-field match | 60 | hold |
| watch | [AT2026akau](https://www.wis-tns.org/object/2026akau) | transient_candidate | 5 | 21.29 | NGC1532 (Galaxy) | 0.51650° | near-field match | 60 | hold |
| watch | [AT2026akbd](https://www.wis-tns.org/object/2026akbd) | transient_candidate | 7 | 20.38 | NGC3193 (Galaxy) | 0.42737° | near-field match | 60 | hold |
| watch | [AT2026akbp](https://www.wis-tns.org/object/2026akbp) | transient_candidate | 6 | 19.83 | UFO Galaxy (Galaxy) | 0.59348° | near-field match | 60 | hold |
| watch | [AT2026akcu](https://www.wis-tns.org/object/2026akcu) | transient_candidate | 5 | 19.83 | IC1609 (Galaxy) | 0.97202° | near-field match | 60 | hold |
| watch | [AT2026akfq](https://www.wis-tns.org/object/2026akfq) | transient_candidate | 5 | 20.65 | NGC 2207 / IC 2163 (Galaxy) | 0.70604° | near-field match | 60 | hold |
| watch | [AT2026akgi](https://www.wis-tns.org/object/2026akgi) | transient_candidate | 7 | 21.85 | NGC1398 (Galaxy) | 0.95139° | near-field match | 60 | hold |
| watch | [AT2026akgr](https://www.wis-tns.org/object/2026akgr) | transient_candidate | 5 | 20.36 | IC 1623 A (Galaxy) | 0.96916° | near-field match | 60 | hold |
| watch | [AT2026akjk](https://www.wis-tns.org/object/2026akjk) | transient_candidate | 0 | 19.66 | IC 1753 (Galaxy) | 0.98851° | near-field match | 60 | hold |
| watch | [AT2026akkr](https://www.wis-tns.org/object/2026akkr) | transient_candidate | 7 | 20.74 | NGC3310 (Galaxy) | 0.66200° | near-field match | 60 | hold |
| watch | [AT2026akkw](https://www.wis-tns.org/object/2026akkw) | transient_candidate | 7 | 20.93 | NGC3319 (Galaxy) | 0.73584° | near-field match | 60 | hold |
| watch | [AT2026akkz](https://www.wis-tns.org/object/2026akkz) | transient_candidate | 4 | 21.29 | IC 1540 (Galaxy) | 0.38069° | near-field match | 60 | hold |
| watch | [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) | transient_candidate | 9 | 18.5 | Lynds Bright Nebula 1043 (LBN1043) (HII) | 1.49482° | near-field match | 57 | hold |
| watch | [AT2026aiep](https://www.wis-tns.org/object/2026aiep) | transient_candidate | 17 | 19.17 | IC5194 (Nebula) | 1.65297° | near-field match | 55 | hold |
| watch | [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) | transient_candidate | 6 | 19.27 | Lynds Dark Nebula 1473 (LDN1473) (Dark nebula) | 1.48149° | near-field match | 55 | hold |
| watch | [AT2026akdi](https://www.wis-tns.org/object/2026akdi) | transient_candidate | 9 | 19.26 | NGC3229 (Nebula) | 1.67147° | near-field match | 55 | hold |
| watch | [AT2026akfr](https://www.wis-tns.org/object/2026akfr) | transient_candidate | 9 | 19.2 | IC4093 (Nebula) | 1.35385° | near-field match | 55 | hold |
| watch | [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) | transient_candidate | 18 | 19.39 | Lynds Bright Nebula 718 (LBN718) (HII) | 0.53252° | near-field match | 54 | hold |
| watch | [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) | transient_candidate | 15 | 18.9 | The opal nebula (Planetary nebula) | 0.75975° | near-field match | 54 | hold |
| watch | [SN2026aela](https://www.wis-tns.org/object/2026aela) | SN Ia | 47 | 18.14 | NGC797 (Galaxy) | 1.46981° | near-field match | 53 | hold |
| watch | [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) | transient_candidate | 7 | 19.52 | IC5338 (Galaxy) | 1.79914° | near-field match | 53 | hold |
| watch | [AT2026ajux](https://www.wis-tns.org/object/2026ajux) | transient_candidate | 6 | 22.92 | NGC 3561 (Galaxy) | 1.74911° | near-field match | 53 | hold |
| watch | [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) | transient_candidate | 6 | 22.32 | IC 1419 (Galaxy) | 1.06627° | near-field match | 53 | hold |
| watch | [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) | transient_candidate | 6 | 22.34 | IC 1417 (Galaxy) | 1.37982° | near-field match | 53 | hold |
| watch | [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) | transient_candidate | 6 | 21.97 | IC 1419 (Galaxy) | 1.70955° | near-field match | 53 | hold |
| watch | [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) | transient_candidate | 6 | 22.71 | IC 1419 (Galaxy) | 1.38932° | near-field match | 53 | hold |
| watch | [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) | transient_candidate | 6 | 20.46 | IC 1417 (Galaxy) | 1.85790° | near-field match | 53 | hold |
| watch | [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) | transient_candidate | 6 | 22.31 | IC 1419 (Galaxy) | 1.29911° | near-field match | 53 | hold |
| watch | [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) | transient_candidate | 6 | 22.48 | IC 1417 (Galaxy) | 1.26051° | near-field match | 53 | hold |
| watch | [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) | transient_candidate | 6 | 21.14 | IC 1417 (Galaxy) | 1.52083° | near-field match | 53 | hold |
| watch | [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) | transient_candidate | 6 | 22.74 | NGC 3561 (Galaxy) | 1.67055° | near-field match | 53 | hold |
| watch | [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) | transient_candidate | 6 | 22.77 | IC 1419 (Galaxy) | 1.64042° | near-field match | 53 | hold |
| watch | [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) | transient_candidate | 6 | 22.7 | IC 1417 (Galaxy) | 1.79224° | near-field match | 53 | hold |
| watch | [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) | transient_candidate | 6 | 22.99 | IC 1417 (Galaxy) | 1.40126° | near-field match | 53 | hold |
| watch | [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) | transient_candidate | 6 | 22.77 | NGC 3561 (Galaxy) | 1.85355° | near-field match | 53 | hold |
| watch | [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) | transient_candidate | 6 | 22.84 | IC 1417 (Galaxy) | 1.52748° | near-field match | 53 | hold |
| watch | [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) | transient_candidate | 6 | 22.67 | NGC 3561 (Galaxy) | 1.03799° | near-field match | 53 | hold |
| watch | [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) | transient_candidate | 6 | 21.31 | IC 1417 (Galaxy) | 1.38720° | near-field match | 53 | hold |
| watch | [AT2026ajws](https://www.wis-tns.org/object/2026ajws) | transient_candidate | 6 | 22.61 | IC 1417 (Galaxy) | 1.64454° | near-field match | 53 | hold |
| watch | [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) | transient_candidate | 6 | 19.73 | IC 1419 (Galaxy) | 1.89146° | near-field match | 53 | hold |
| watch | [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) | transient_candidate | 6 | 22.68 | IC 1417 (Galaxy) | 1.86530° | near-field match | 53 | hold |
| watch | [AT2026ajww](https://www.wis-tns.org/object/2026ajww) | transient_candidate | 6 | 22.29 | IC 1417 (Galaxy) | 1.35306° | near-field match | 53 | hold |
| watch | [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) | transient_candidate | 6 | 23.14 | IC 1417 (Galaxy) | 1.79292° | near-field match | 53 | hold |
| watch | [AT2026akam](https://www.wis-tns.org/object/2026akam) | transient_candidate | 5 | 19.7 | IC1657 (Galaxy) | 1.69463° | near-field match | 53 | hold |
| watch | [AT2026akao](https://www.wis-tns.org/object/2026akao) | transient_candidate | 6 | 21.28 | IC 1419 (Galaxy) | 1.62610° | near-field match | 53 | hold |
| watch | [AT2026akaq](https://www.wis-tns.org/object/2026akaq) | transient_candidate | 5 | 19.73 | IC 2031 (Galaxy) | 1.69253° | near-field match | 53 | hold |
| watch | [AT2026akat](https://www.wis-tns.org/object/2026akat) | transient_candidate | 7 | 21.55 | NGC1527 (Galaxy) | 1.52157° | near-field match | 53 | hold |
| watch | [AT2026akcc](https://www.wis-tns.org/object/2026akcc) | transient_candidate | 4 | 19.55 | IC2143 (Galaxy) | 1.17282° | near-field match | 53 | hold |
| watch | [AT2026akcy](https://www.wis-tns.org/object/2026akcy) | transient_candidate | 3 | 19.55 | Caldwell 48 (C48) (Galaxy) | 1.31632° | near-field match | 53 | hold |
| watch | [AT2026akdo](https://www.wis-tns.org/object/2026akdo) | transient_candidate | 6 | 22.19 | IC 5374 (Galaxy) | 1.26092° | near-field match | 53 | hold |
| watch | [AT2026aken](https://www.wis-tns.org/object/2026aken) | transient_candidate | 7 | 20.18 | NGC 2207 / IC 2163 (Galaxy) | 1.57182° | near-field match | 53 | hold |
| watch | [AT2026akfv](https://www.wis-tns.org/object/2026akfv) | transient_candidate | 7 | 22.35 | NGC1398 (Galaxy) | 1.49814° | near-field match | 53 | hold |
| watch | [AT2026akgo](https://www.wis-tns.org/object/2026akgo) | transient_candidate | 6 | 20.59 | NGC3319 (Galaxy) | 1.42736° | near-field match | 53 | hold |
| watch | [AT2026akgq](https://www.wis-tns.org/object/2026akgq) | transient_candidate | 5 | 19.67 | IC1696 (Galaxy) | 1.75554° | near-field match | 53 | hold |
| watch | [AT2026akgt](https://www.wis-tns.org/object/2026akgt) | transient_candidate | 3 | 20.41 | Darth Vader's Galaxy (Galaxy) | 1.96157° | near-field match | 53 | hold |
| watch | [AT2026akgw](https://www.wis-tns.org/object/2026akgw) | transient_candidate | 6 | 19.98 | NGC7457 (Galaxy) | 1.57742° | near-field match | 53 | hold |
| watch | [AT2026akho](https://www.wis-tns.org/object/2026akho) | transient_candidate | 7 | 23.08 | IC2000 (Galaxy) | 1.12255° | near-field match | 53 | hold |
| watch | [AT2026akif](https://www.wis-tns.org/object/2026akif) | transient_candidate | 7 | 22.46 | IC 197 (Galaxy) | 1.04947° | near-field match | 53 | hold |
| watch | [AT2026akjn](https://www.wis-tns.org/object/2026akjn) | transient_candidate | 0 | 19.97 | Silver Sliver Galaxy (Galaxy) | 1.99665° | near-field match | 53 | hold |
| watch | [AT2026akks](https://www.wis-tns.org/object/2026akks) | transient_candidate | 7 | 20.65 | NGC3319 (Galaxy) | 1.31211° | near-field match | 53 | hold |
| watch | [AT2026akkx](https://www.wis-tns.org/object/2026akkx) | transient_candidate | 7 | 21.4 | NGC3319 (Galaxy) | 1.95134° | near-field match | 53 | hold |
| watch | [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) | transient_candidate | 20 | 19.59 | IC1933 (Galaxy) | 0.59197° | near-field match | 52 | hold |
| watch | [AT2026aigt](https://www.wis-tns.org/object/2026aigt) | transient_candidate | 16 | 20.07 | IC2367 (Galaxy) | 0.90936° | near-field match | 52 | hold |
| watch | [AT2026aipd](https://www.wis-tns.org/object/2026aipd) | transient_candidate | 24 | 21.22 | IC 1746 (Galaxy) | 0.30860° | near-field match | 52 | hold |
| watch | [AT2026ajar](https://www.wis-tns.org/object/2026ajar) | transient_candidate | 14 | 19.82 | NGC3169 (Galaxy) | 0.74867° | near-field match | 52 | hold |
| watch | [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) | transient_candidate | 11 | 20.16 | NGC779 (Galaxy) | 0.37589° | near-field match | 52 | hold |
| watch | [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) | transient_candidate | 9 | 19.72 | NGC3239 (Galaxy) | 0.74061° | near-field match | 52 | hold |
| watch | [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) | transient_candidate | 8 | 19.61 | NGC2985 (Galaxy) | 0.55170° | near-field match | 52 | hold |
| watch | [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) | transient_candidate | 13 | 22.82 | IC 74 (Galaxy) | 0.60041° | near-field match | 52 | hold |
| watch | [AT2026ajta](https://www.wis-tns.org/object/2026ajta) | transient_candidate | 13 | 22.45 | IC1696 (Galaxy) | 0.88977° | near-field match | 52 | hold |
| watch | [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) | transient_candidate | 13 | 21.43 | NGC3521 (Galaxy) | 0.82591° | near-field match | 52 | hold |
| watch | [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) | transient_candidate | 23 | 21.33 | IC178 (Galaxy) | 0.93972° | near-field match | 52 | hold |
| watch | [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) | transient_candidate | 18 | 20.75 | NGC 2964 (Galaxy) | 0.25419° | near-field match | 52 | hold |
| watch | [AT2026ajyc](https://www.wis-tns.org/object/2026ajyc) | transient_candidate | 12 | 19.72 | NGC 2207 / IC 2163 (Galaxy) | 0.74711° | near-field match | 52 | hold |
| watch | [AT2026ajyh](https://www.wis-tns.org/object/2026ajyh) | transient_candidate | 11 | 21.89 | IC 173 (Galaxy) | 0.72506° | near-field match | 52 | hold |
| watch | [AT2026ajyr](https://www.wis-tns.org/object/2026ajyr) | transient_candidate | 22 | 22.47 | IC 1507 (Galaxy) | 0.87774° | near-field match | 52 | hold |
| watch | [AT2026ajzb](https://www.wis-tns.org/object/2026ajzb) | transient_candidate | 14 | 21.83 | NGC3640 (Galaxy) | 0.57000° | near-field match | 52 | hold |
| watch | [AT2026ajzh](https://www.wis-tns.org/object/2026ajzh) | transient_candidate | 12 | 22.48 | Local Group (Galaxy) | 0.56395° | near-field match | 52 | hold |
| watch | [AT2026ajzp](https://www.wis-tns.org/object/2026ajzp) | transient_candidate | 10 | 23.34 | IC 1481 (Galaxy) | 0.91299° | near-field match | 52 | hold |
| watch | [AT2026akaf](https://www.wis-tns.org/object/2026akaf) | transient_candidate | 10 | 20.79 | NGC7723 (Galaxy) | 0.30146° | near-field match | 52 | hold |
| watch | [AT2026akct](https://www.wis-tns.org/object/2026akct) | transient_candidate | 8 | 22.34 | NGC7606 (Galaxy) | 0.95998° | near-field match | 52 | hold |
| watch | [AT2026akdb](https://www.wis-tns.org/object/2026akdb) | transient_candidate | 14 | 21.57 | NGC3166 (Galaxy) | 0.47284° | near-field match | 52 | hold |
| watch | [AT2026akdd](https://www.wis-tns.org/object/2026akdd) | transient_candidate | 17 | 22.46 | IC 1639 (Galaxy) | 0.78978° | near-field match | 52 | hold |
| watch | [AT2026akdl](https://www.wis-tns.org/object/2026akdl) | transient_candidate | 9 | 21.48 | IC 632 (Galaxy) | 0.94676° | near-field match | 52 | hold |
| watch | [AT2026akdr](https://www.wis-tns.org/object/2026akdr) | transient_candidate | 20 | 20.11 | NGC 3619 (Galaxy) | 0.95077° | near-field match | 52 | hold |
| watch | [AT2026akea](https://www.wis-tns.org/object/2026akea) | transient_candidate | 9 | 20.51 | NGC3245 (Galaxy) | 0.39166° | near-field match | 52 | hold |
| watch | [AT2026akeh](https://www.wis-tns.org/object/2026akeh) | transient_candidate | 12 | 20.92 | NGC 2903 (Galaxy) | 0.83678° | near-field match | 52 | hold |
| watch | [AT2026akei](https://www.wis-tns.org/object/2026akei) | transient_candidate | 11 | 21.27 | IC200 (Galaxy) | 0.38584° | near-field match | 52 | hold |
| watch | [AT2026akfl](https://www.wis-tns.org/object/2026akfl) | transient_candidate | 9 | 19.76 | IC769 (Galaxy) | 0.41936° | near-field match | 52 | hold |
| watch | [AT2026akhy](https://www.wis-tns.org/object/2026akhy) | transient_candidate | 14 | 20.64 | NGC3640 (Galaxy) | 0.74894° | near-field match | 52 | hold |
| watch | [AT2026akhz](https://www.wis-tns.org/object/2026akhz) | transient_candidate | 11 | 22.82 | IC 673 (Galaxy) | 0.60410° | near-field match | 52 | hold |
| watch | [AT2026akia](https://www.wis-tns.org/object/2026akia) | transient_candidate | 9 | 20.98 | NGC3166 (Galaxy) | 0.95306° | near-field match | 52 | hold |
| watch | [AT2026akib](https://www.wis-tns.org/object/2026akib) | transient_candidate | 13 | 21.56 | NGC3521 (Galaxy) | 0.61522° | near-field match | 52 | hold |
| watch | [AT2026akic](https://www.wis-tns.org/object/2026akic) | transient_candidate | 14 | 21.72 | NGC3640 (Galaxy) | 0.77839° | near-field match | 52 | hold |
| watch | [AT2026akjt](https://www.wis-tns.org/object/2026akjt) | transient_candidate | 11 | 22.87 | IC 632 (Galaxy) | 0.59759° | near-field match | 52 | hold |
| watch | [AT2026akko](https://www.wis-tns.org/object/2026akko) | transient_candidate | 9 | 22.14 | IC2446 (Galaxy) | 0.75145° | near-field match | 52 | hold |
| watch | [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) | transient_candidate | 6 | 21.93 | NGC7158 (Nebula) | 0.76418° | near-field match | 50 | hold |
| watch | [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) | transient_candidate | 6 | 22.2 | NGC7158 (Nebula) | 0.83221° | near-field match | 50 | hold |
| watch | [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) | transient_candidate | 6 | 21.24 | NGC7158 (Nebula) | 0.38606° | near-field match | 50 | hold |
| watch | [AT2026akbc](https://www.wis-tns.org/object/2026akbc) | transient_candidate | 6 | 20.89 | IC2030 (Nebula) | 0.58630° | near-field match | 50 | hold |
| watch | [AT2026akfx](https://www.wis-tns.org/object/2026akfx) | transient_candidate | 7 | 22.85 | IC2055 (Nebula) | 0.92566° | near-field match | 50 | hold |
| watch | [AT2026akgs](https://www.wis-tns.org/object/2026akgs) | transient_candidate | 7 | 21.21 | NGC7161 (Nebula) | 0.86287° | near-field match | 50 | hold |
| watch | [SN2026aiop](https://www.wis-tns.org/object/2026aiop) | SN Ia | 16 | 20.23 | Lynds Bright Nebula 773 (LBN773) (HII) | 0.84759° | near-field match | 49 | hold |
| watch | [AT2026ajye](https://www.wis-tns.org/object/2026ajye) | transient_candidate | 13 | 18.67 | Lynds Bright Nebula 878 (LBN878) (HII) | 1.00364° | near-field match | 47 | hold |
| watch | [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) | transient_candidate | 21 | 19.8 | IC1401 (Galaxy) | 1.09401° | near-field match | 45 | hold |
| watch | [AT2026aiit](https://www.wis-tns.org/object/2026aiit) | transient_candidate | 26 | 20.1 | IC 536 (Galaxy) | 1.35004° | near-field match | 45 | hold |
| watch | [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) | transient_candidate | 20 | 21.09 | NGC2681 (Galaxy) | 1.89724° | near-field match | 45 | hold |
| watch | [AT2026ajji](https://www.wis-tns.org/object/2026ajji) | transient_candidate | 9 | 19.77 | NGC 3294 (Galaxy) | 1.46834° | near-field match | 45 | hold |
| watch | [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) | transient_candidate | 8 | 19.73 | NGC3198 (Galaxy) | 1.44291° | near-field match | 45 | hold |
| watch | [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) | transient_candidate | 13 | 19.83 | IC1386 (Galaxy) | 1.28167° | near-field match | 45 | hold |
| watch | [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) | transient_candidate | 8 | 20.87 | IC 2016 (Galaxy) | 1.84241° | near-field match | 45 | hold |
| watch | [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) | transient_candidate | 8 | 19.68 | IC 17 (Galaxy) | 1.57719° | near-field match | 45 | hold |
| watch | [AT2026ajss](https://www.wis-tns.org/object/2026ajss) | transient_candidate | 10 | 22.86 | NGC 2207 / IC 2163 (Galaxy) | 1.55710° | near-field match | 45 | hold |
| watch | [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) | transient_candidate | 12 | 22.02 | NGC3521 (Galaxy) | 1.08432° | near-field match | 45 | hold |
| watch | [AT2026ajti](https://www.wis-tns.org/object/2026ajti) | transient_candidate | 11 | 22.44 | IC 1757 (Galaxy) | 1.42421° | near-field match | 45 | hold |
| watch | [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) | transient_candidate | 20 | 21.43 | NGC925 (Galaxy) | 1.68238° | near-field match | 45 | hold |
| watch | [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) | transient_candidate | 17 | 21.33 | IC509 (Galaxy) | 1.28504° | near-field match | 45 | hold |
| watch | [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) | transient_candidate | 17 | 21.32 | UFO Galaxy (Galaxy) | 1.99519° | near-field match | 45 | hold |
| watch | [AT2026ajty](https://www.wis-tns.org/object/2026ajty) | transient_candidate | 17 | 21.65 | IC2378 (Galaxy) | 1.21289° | near-field match | 45 | hold |
| watch | [AT2026ajug](https://www.wis-tns.org/object/2026ajug) | transient_candidate | 14 | 21.26 | IC1525 (Galaxy) | 1.31062° | near-field match | 45 | hold |
| watch | [AT2026ajum](https://www.wis-tns.org/object/2026ajum) | transient_candidate | 10 | 22.35 | IC 1540 (Galaxy) | 1.37052° | near-field match | 45 | hold |
| watch | [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) | transient_candidate | 9 | 19.98 | IC1657 (Galaxy) | 1.48817° | near-field match | 45 | hold |
| watch | [AT2026ajyi](https://www.wis-tns.org/object/2026ajyi) | transient_candidate | 14 | 22.68 | IC 1776 (Galaxy) | 1.14126° | near-field match | 45 | hold |
| watch | [AT2026ajyl](https://www.wis-tns.org/object/2026ajyl) | transient_candidate | 10 | 22.53 | IC 1639 (Galaxy) | 1.77291° | near-field match | 45 | hold |
| watch | [AT2026ajyt](https://www.wis-tns.org/object/2026ajyt) | transient_candidate | 22 | 22.05 | IC1696 (Galaxy) | 1.53398° | near-field match | 45 | hold |
| watch | [AT2026ajyx](https://www.wis-tns.org/object/2026ajyx) | transient_candidate | 16 | 23 | IC1696 (Galaxy) | 1.66353° | near-field match | 45 | hold |
| watch | [AT2026ajyy](https://www.wis-tns.org/object/2026ajyy) | transient_candidate | 14 | 20.1 | NGC3169 (Galaxy) | 1.85756° | near-field match | 45 | hold |
| watch | [AT2026ajyz](https://www.wis-tns.org/object/2026ajyz) | transient_candidate | 14 | 21.28 | IC 632 (Galaxy) | 1.27527° | near-field match | 45 | hold |
| watch | [AT2026ajzc](https://www.wis-tns.org/object/2026ajzc) | transient_candidate | 14 | 21.7 | Local Group (Galaxy) | 1.45136° | near-field match | 45 | hold |
| watch | [AT2026ajzf](https://www.wis-tns.org/object/2026ajzf) | transient_candidate | 13 | 21.83 | NGC3640 (Galaxy) | 1.39275° | near-field match | 45 | hold |
| watch | [AT2026ajzg](https://www.wis-tns.org/object/2026ajzg) | transient_candidate | 12 | 22.3 | NGC3169 (Galaxy) | 1.35429° | near-field match | 45 | hold |
| watch | [AT2026ajzi](https://www.wis-tns.org/object/2026ajzi) | transient_candidate | 11 | 22.58 | IC 3 (Spiral galaxy) | 1.77766° | near-field match | 45 | hold |
| watch | [AT2026ajzj](https://www.wis-tns.org/object/2026ajzj) | transient_candidate | 11 | 22.67 | IC 173 (Galaxy) | 1.13242° | near-field match | 45 | hold |
| watch | [AT2026ajzy](https://www.wis-tns.org/object/2026ajzy) | transient_candidate | 14 | 22.9 | NGC 2207 / IC 2163 (Galaxy) | 1.30641° | near-field match | 45 | hold |
| watch | [AT2026akaa](https://www.wis-tns.org/object/2026akaa) | transient_candidate | 12 | 21.91 | NGC3640 (Galaxy) | 1.98192° | near-field match | 45 | hold |
| watch | [AT2026akac](https://www.wis-tns.org/object/2026akac) | transient_candidate | 13 | 21.88 | IC187 (Galaxy) | 1.14616° | near-field match | 45 | hold |
| watch | [AT2026akae](https://www.wis-tns.org/object/2026akae) | transient_candidate | 9 | 21.79 | Andromeda Galaxy (Galaxy) | 1.02507° | near-field match | 45 | hold |
| watch | [AT2026akah](https://www.wis-tns.org/object/2026akah) | transient_candidate | 8 | 21.07 | NGC7606 (Galaxy) | 1.33761° | near-field match | 45 | hold |
| watch | [AT2026akdf](https://www.wis-tns.org/object/2026akdf) | transient_candidate | 13 | 23.34 | Darth Vader's Galaxy (Galaxy) | 1.56640° | near-field match | 45 | hold |
| watch | [AT2026akdm](https://www.wis-tns.org/object/2026akdm) | transient_candidate | 9 | 21.93 | IC 632 (Galaxy) | 1.72914° | near-field match | 45 | hold |
| watch | [AT2026akdv](https://www.wis-tns.org/object/2026akdv) | transient_candidate | 15 | 20.79 | IC 478 (Galaxy) | 1.16737° | near-field match | 45 | hold |
| watch | [AT2026akek](https://www.wis-tns.org/object/2026akek) | transient_candidate | 11 | 21.27 | IC1784 (Galaxy) | 1.81247° | near-field match | 45 | hold |
| watch | [AT2026akfh](https://www.wis-tns.org/object/2026akfh) | transient_candidate | 18 | 20.14 | IC 673 (Galaxy) | 1.71606° | near-field match | 45 | hold |
| watch | [AT2026akfy](https://www.wis-tns.org/object/2026akfy) | transient_candidate | 9 | 22.41 | IC1495 (Galaxy) | 1.84137° | near-field match | 45 | hold |
| watch | [AT2026akge](https://www.wis-tns.org/object/2026akge) | transient_candidate | 9 | 19.94 | IC2081 (Galaxy) | 1.12136° | near-field match | 45 | hold |
| watch | [AT2026akgh](https://www.wis-tns.org/object/2026akgh) | transient_candidate | 8 | 22.43 | NGC7606 (Galaxy) | 1.05288° | near-field match | 45 | hold |
| watch | [AT2026akix](https://www.wis-tns.org/object/2026akix) | transient_candidate | 15 | 23.81 | IC2000 (Galaxy) | 1.42748° | near-field match | 45 | hold |
| watch | [AT2026akjp](https://www.wis-tns.org/object/2026akjp) | transient_candidate | 13 | 19.82 | Caldwell 3 (C3) (Galaxy) | 1.24289° | near-field match | 45 | hold |
| watch | [AT2026akjs](https://www.wis-tns.org/object/2026akjs) | transient_candidate | 13 | 22.16 | NGC488 (Galaxy) | 1.50636° | near-field match | 45 | hold |
| watch | [AT2026akke](https://www.wis-tns.org/object/2026akke) | transient_candidate | 15 | 20.8 | NGC3310 (Galaxy) | 1.50843° | near-field match | 45 | hold |
| watch | [AT2026akkh](https://www.wis-tns.org/object/2026akkh) | transient_candidate | 12 | 21.56 | NGC2841 (Galaxy) | 1.69532° | near-field match | 45 | hold |
| watch | [AT2026akkm](https://www.wis-tns.org/object/2026akkm) | transient_candidate | 10 | 21.22 | NGC3198 (Galaxy) | 1.12242° | near-field match | 45 | hold |
| watch | [AT2026akkq](https://www.wis-tns.org/object/2026akkq) | transient_candidate | 9 | 21.92 | NGC 2782 (Galaxy) | 1.48763° | near-field match | 45 | hold |
| watch | [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) | transient_candidate | 6 | 19.77 | NGC3578 (Nebula) | 1.46782° | near-field match | 43 | hold |
| watch | [AT2026ajur](https://www.wis-tns.org/object/2026ajur) | transient_candidate | 6 | 23.23 | NGC7158 (Nebula) | 1.05093° | near-field match | 43 | hold |
| watch | [AT2026ajve](https://www.wis-tns.org/object/2026ajve) | transient_candidate | 6 | 22.03 | IC5194 (Nebula) | 1.56732° | near-field match | 43 | hold |
| watch | [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) | transient_candidate | 6 | 21.75 | IC5194 (Nebula) | 1.82559° | near-field match | 43 | hold |
| watch | [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) | transient_candidate | 6 | 22.52 | IC1457 (Nebula) | 1.62885° | near-field match | 43 | hold |
| watch | [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) | transient_candidate | 6 | 21.84 | IC5194 (Nebula) | 1.34031° | near-field match | 43 | hold |
| watch | [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) | transient_candidate | 6 | 20.66 | IC1457 (Nebula) | 1.88540° | near-field match | 43 | hold |
| watch | [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) | transient_candidate | 6 | 21.83 | NGC894 (Nebula) | 1.21470° | near-field match | 43 | hold |
| watch | [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) | transient_candidate | 6 | 21.12 | NGC7158 (Nebula) | 1.66580° | near-field match | 43 | hold |
| watch | [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) | transient_candidate | 6 | 21.76 | NGC7158 (Nebula) | 1.17313° | near-field match | 43 | hold |
| watch | [AT2026akcq](https://www.wis-tns.org/object/2026akcq) | transient_candidate | 6 | 19.76 | IC2189 (Nebula) | 1.26363° | near-field match | 43 | hold |
| watch | [AT2026akdn](https://www.wis-tns.org/object/2026akdn) | transient_candidate | 7 | 22.2 | IC5248 (Nebula) | 1.11151° | near-field match | 43 | hold |
| watch | [AT2026akdp](https://www.wis-tns.org/object/2026akdp) | transient_candidate | 6 | 22.06 | IC 1623 (CiG) | 1.51486° | near-field match | 43 | hold |
| watch | [AT2026akgj](https://www.wis-tns.org/object/2026akgj) | transient_candidate | 6 | 22.45 | NGC894 (Nebula) | 1.41713° | near-field match | 43 | hold |
| watch | [AT2026akhj](https://www.wis-tns.org/object/2026akhj) | transient_candidate | 4 | 19.63 | IC2328 (Nebula) | 1.00646° | near-field match | 43 | hold |
| watch | [AT2026akkt](https://www.wis-tns.org/object/2026akkt) | transient_candidate | 7 | 20.11 | NGC3180 (HII) | 1.53716° | near-field match | 43 | hold |
| watch | [AT2026akkv](https://www.wis-tns.org/object/2026akkv) | transient_candidate | 7 | 20.93 | IC2610 (Nebula) | 1.26969° | near-field match | 43 | hold |
| watch | [AT2026aiko](https://www.wis-tns.org/object/2026aiko) | transient_candidate | 15 | 19.85 | NGC7158 (Nebula) | 0.38091° | near-field match | 42 | hold |
| watch | [AT2026aivj](https://www.wis-tns.org/object/2026aivj) | transient_candidate | 16 | 20.47 | IC1547 (Nebula) | 0.56558° | near-field match | 42 | hold |
| watch | [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) | transient_candidate | 14 | 22.16 | IC111 (Nebula) | 0.80147° | near-field match | 42 | hold |
| watch | [AT2026ajup](https://www.wis-tns.org/object/2026ajup) | transient_candidate | 18 | 21.25 | Collinder 116 (CR116) (Open cluster) | 0.84314° | near-field match | 42 | hold |
| watch | [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) | transient_candidate | 21 | 23.8 | NGC894 (Nebula) | 0.53340° | near-field match | 42 | hold |
| watch | [AT2026ajym](https://www.wis-tns.org/object/2026ajym) | transient_candidate | 23 | 22.1 | NGC7613 (Nebula) | 0.51096° | near-field match | 42 | hold |
| watch | [AT2026ajzw](https://www.wis-tns.org/object/2026ajzw) | transient_candidate | 20 | 22.42 | NGC7668 (Nebula) | 0.85066° | near-field match | 42 | hold |
| watch | [AT2026akbr](https://www.wis-tns.org/object/2026akbr) | transient_candidate | 9 | 19.51 | IC1538 (Nebula) | 0.81828° | near-field match | 42 | hold |
| watch | [AT2026akcp](https://www.wis-tns.org/object/2026akcp) | transient_candidate | 4 | 20.01 | Lynds Bright Nebula 980 (LBN980) (HII) | 0.73350° | near-field match | 42 | hold |
| watch | [AT2026akec](https://www.wis-tns.org/object/2026akec) | transient_candidate | 12 | 21.49 | Beehive cluster (Open cluster) | 0.95372° | near-field match | 42 | hold |
| watch | [AT2026akfs](https://www.wis-tns.org/object/2026akfs) | transient_candidate | 5 | 21.46 | van den Bergh 156 (VDB156) (Nebula) | 0.74673° | near-field match | 42 | hold |
| watch | [AT2026akgu](https://www.wis-tns.org/object/2026akgu) | transient_candidate | 2 | 20.6 | Lynds Bright Nebula 896 (LBN896) (HII) | 0.59978° | near-field match | 42 | hold |
| watch | [AT2026akie](https://www.wis-tns.org/object/2026akie) | transient_candidate | 9 | 21.89 | NGC3229 (Nebula) | 0.80143° | near-field match | 42 | hold |
| watch | [AT2026akiy](https://www.wis-tns.org/object/2026akiy) | transient_candidate | 22 | 23.45 | NGC7453 (Nebula) | 0.48687° | near-field match | 42 | hold |
| watch | [AT2026akkb](https://www.wis-tns.org/object/2026akkb) | transient_candidate | 15 | 21.01 | Gemini nebula (Planetary nebula) | 0.94983° | near-field match | 42 | hold |
| watch | [AT2026akkc](https://www.wis-tns.org/object/2026akkc) | transient_candidate | 15 | 21.65 | Gemini nebula (Planetary nebula) | 0.26232° | near-field match | 42 | hold |
| watch | [AT2026aetx](https://www.wis-tns.org/object/2026aetx) | transient_candidate | 45 | 19.1 | NGC3166 (Galaxy) | 0.65757° | near-field match | 35 | hold |
| watch | [AT2026aijr](https://www.wis-tns.org/object/2026aijr) | transient_candidate | 17 | 20.08 | NGC7447 (Nebula) | 1.89138° | near-field match | 35 | hold |
| watch | [AT2026aisi](https://www.wis-tns.org/object/2026aisi) | transient_candidate | 14 | 20.26 | Collinder 133 (CR133) (Open cluster) | 1.35375° | near-field match | 35 | hold |
| watch | [AT2026aitp](https://www.wis-tns.org/object/2026aitp) | transient_candidate | 17 | 19.76 | NGC3181 (HII) | 1.80903° | near-field match | 35 | hold |
| watch | [AT2026aiys](https://www.wis-tns.org/object/2026aiys) | transient_candidate | 12 | 19.55 | IC5251 (Nebula) | 1.74753° | near-field match | 35 | hold |
| watch | [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) | transient_candidate | 15 | 20.91 | Intergalactic Wanderer (Globular cluster) | 1.09787° | near-field match | 35 | hold |
| watch | [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) | transient_candidate | 7 | 19.58 | Lynds Bright Nebula 484 (LBN484) (HII) | 1.74348° | near-field match | 35 | hold |
| watch | [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) | transient_candidate | 13 | 22.88 | NGC728 (Nebula) | 1.25970° | near-field match | 35 | hold |
| watch | [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) | transient_candidate | 15 | 23.61 | IC5248 (Nebula) | 1.48459° | near-field match | 35 | hold |
| watch | [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) | transient_candidate | 13 | 21.48 | NGC3387 (Nebula) | 1.71033° | near-field match | 35 | hold |
| watch | [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) | transient_candidate | 18 | 21.87 | NGC737 (Nebula) | 1.51249° | near-field match | 35 | hold |
| watch | [AT2026ajub](https://www.wis-tns.org/object/2026ajub) | transient_candidate | 16 | 21.61 | NGC2901 (Nebula) | 1.29090° | near-field match | 35 | hold |
| watch | [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) | transient_candidate | 11 | 21.8 | NGC7453 (Nebula) | 1.30353° | near-field match | 35 | hold |
| watch | [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) | transient_candidate | 12 | 22.61 | NGC894 (Nebula) | 1.74562° | near-field match | 35 | hold |
| watch | [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) | transient_candidate | 12 | 20.08 | NGC1498 (Open cluster) | 1.41273° | near-field match | 35 | hold |
| watch | [AT2026akak](https://www.wis-tns.org/object/2026akak) | transient_candidate | 15 | 20.3 | IC 5364 (CiG) | 1.64295° | near-field match | 35 | hold |
| watch | [AT2026akcr](https://www.wis-tns.org/object/2026akcr) | transient_candidate | 8 | 21.46 | NGC7526 (Nebula) | 1.29193° | near-field match | 35 | hold |
| watch | [AT2026akdj](https://www.wis-tns.org/object/2026akdj) | transient_candidate | 9 | 21.1 | NGC3229 (Nebula) | 1.71319° | near-field match | 35 | hold |
| watch | [AT2026akeb](https://www.wis-tns.org/object/2026akeb) | transient_candidate | 12 | 21.51 | Beehive cluster (Open cluster) | 1.40035° | near-field match | 35 | hold |
| watch | [AT2026akeg](https://www.wis-tns.org/object/2026akeg) | transient_candidate | 12 | 21.24 | NGC 2207 / IC 2163 (CiG) | 1.81227° | near-field match | 35 | hold |
| watch | [AT2026akfj](https://www.wis-tns.org/object/2026akfj) | transient_candidate | 11 | 20.52 | NGC2901 (Nebula) | 1.79577° | near-field match | 35 | hold |
| watch | [AT2026akgv](https://www.wis-tns.org/object/2026akgv) | transient_candidate | 12 | 22.45 | NGC894 (Nebula) | 1.63959° | near-field match | 35 | hold |
| watch | [AT2026akhw](https://www.wis-tns.org/object/2026akhw) | transient_candidate | 9 | 21.25 | NGC3229 (Nebula) | 1.62985° | near-field match | 35 | hold |
| watch | [AT2026akil](https://www.wis-tns.org/object/2026akil) | transient_candidate | 15 | 21.05 | NGC3097 (Nebula) | 1.78512° | near-field match | 35 | hold |
| watch | [AT2026akio](https://www.wis-tns.org/object/2026akio) | transient_candidate | 10 | 21.46 | Collinder 113 (CR113) (Open cluster) | 1.46002° | near-field match | 35 | hold |
| watch | [AT2026akjb](https://www.wis-tns.org/object/2026akjb) | transient_candidate | 3 | 21.26 | Lynds Bright Nebula 896 (LBN896) (HII) | 1.22063° | near-field match | 35 | hold |
| watch | [AT2026akjm](https://www.wis-tns.org/object/2026akjm) | transient_candidate | 12 | 20.64 | IC240 (Nebula) | 1.07528° | near-field match | 35 | hold |
| watch | [AT2026akkg](https://www.wis-tns.org/object/2026akkg) | transient_candidate | 12 | 21.86 | Gemini nebula (Planetary nebula) | 1.07214° | near-field match | 35 | hold |
| watch | [AT2026akkl](https://www.wis-tns.org/object/2026akkl) | transient_candidate | 10 | 21.16 | Eskimo or Clown Nebula (Planetary nebula) | 1.67199° | near-field match | 35 | hold |
| watch | [AT2026akkp](https://www.wis-tns.org/object/2026akkp) | transient_candidate | 9 | 21.28 | NGC2901 (Nebula) | 1.15866° | near-field match | 35 | hold |
| watch | [AT2026aigg](https://www.wis-tns.org/object/2026aigg) | transient_candidate | 19 | 20.26 | Lynds Bright Nebula 910 (LBN910) (HII) | 0.77477° | near-field match | 34 | hold |
| watch | [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) | transient_candidate | 9 | 19.72 | Lynds Bright Nebula 439 (LBN439) (HII) | 0.79678° | near-field match | 34 | hold |
| watch | [AT2026ajts](https://www.wis-tns.org/object/2026ajts) | transient_candidate | 18 | 20.91 | Lynds Bright Nebula 891 (LBN891) (HII) | 0.64768° | near-field match | 34 | hold |
| watch | [SN2026adfc](https://www.wis-tns.org/object/2026adfc) | SN Ia | 53 | 18.97 | Lynds Bright Nebula 429 (LBN429) (HII) | 0.65958° | near-field match | 32 | hold |
| watch | [AT2026absv](https://www.wis-tns.org/object/2026absv) | transient_candidate | 68 | 19.48 | NGC 3561 (Galaxy) | 1.10562° | near-field match | 28 | hold |
| watch | [AT2026aimd](https://www.wis-tns.org/object/2026aimd) | transient_candidate | 15 | 20.38 | Collinder 65 (CR65) (Open cluster) | 1.83171° | near-field match | 27 | hold |
| watch | [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) | transient_candidate | 9 | 19.74 | Lynds Bright Nebula 856 (LBN856) (HII) | 1.86922° | near-field match | 27 | hold |
| watch | [AT2026ajxz](https://www.wis-tns.org/object/2026ajxz) | transient_candidate | 9 | 20.27 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.08910° | near-field match | 27 | hold |
| watch | [AT2026ajyk](https://www.wis-tns.org/object/2026ajyk) | transient_candidate | 11 | 22.81 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.88407° | near-field match | 27 | hold |
| watch | [AT2026akda](https://www.wis-tns.org/object/2026akda) | transient_candidate | 18 | 20.18 | Collinder 285 (CR285) (Open cluster) | 1.13740° | near-field match | 27 | hold |
| watch | [AT2026akde](https://www.wis-tns.org/object/2026akde) | transient_candidate | 14 | 22.36 | Lynds Bright Nebula 188 (LBN188) (HII) | 1.86673° | near-field match | 27 | hold |
| watch | [TDE2026afrm](https://www.wis-tns.org/object/2026afrm) | TDE | 34 | 19.69 | IC 478 (Galaxy) | 1.30982° | near-field match | 23 | hold |
| watch | [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) | SN Ia | 47 | 19.82 | NGC7158 (Nebula) | 0.70237° | near-field match | 20 | hold |
| watch | [SN2026ahxw](https://www.wis-tns.org/object/2026ahxw) | SN Ia | 32 | 20.84 | Collinder 154 (CR154) (Open cluster) | 0.75676° | near-field match | 20 | hold |
| watch | [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) | transient_candidate | 69 | 20.79 | NGC925 (Galaxy) | 0.76155° | near-field match | 15 | hold |
| watch | [SN2026aedz](https://www.wis-tns.org/object/2026aedz) | SN IIn | 49 | 19.78 | NGC1480 (Nebula) | 1.10868° | near-field match | 13 | hold |
| watch | [SN2026agok](https://www.wis-tns.org/object/2026agok) | SN Ia | 35 | 19.99 | Beehive cluster (Open cluster) | 1.64277° | near-field match | 13 | hold |
| watch | [AT2026agac](https://www.wis-tns.org/object/2026agac) | transient_candidate | 42 | 20.92 | IC 1417 (Galaxy) | 1.74979° | near-field match | 8 | hold |
| watch | [AT2026agzy](https://www.wis-tns.org/object/2026agzy) | transient_candidate | 39 | 20.21 | NGC797 (Galaxy) | 1.65183° | near-field match | 8 | hold |
| watch | [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) | transient_candidate | 69 | 22.85 | IC 1507 (Galaxy) | 1.97219° | near-field match | 8 | hold |
| watch | [AT2026ajyo](https://www.wis-tns.org/object/2026ajyo) | transient_candidate | 35 | 22.17 | IC 173 (Galaxy) | 1.29924° | near-field match | 8 | hold |
| watch | [AT2026ajzu](https://www.wis-tns.org/object/2026ajzu) | transient_candidate | 34 | 22.52 | IC 3 (Spiral galaxy) | 1.04710° | near-field match | 8 | hold |
| watch | [AT2026akjx](https://www.wis-tns.org/object/2026akjx) | transient_candidate | 31 | 21.13 | IC132 (HII) | 1.66808° | near-field match | 0 | hold |

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
| Discovery | 2026-11-02T19:55:53Z · 19 days · 16.1 Clear |
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
| Discovery | 2026-11-15T15:10:28Z · 6 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 3. [SN2026ahyf](https://www.wis-tns.org/object/2026ahyf) near IC 2405

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 97/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2405 as this object's host. The 0.45058° (27.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN |
| Redshift | 0.0257 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:42:36Z · 18 days · 18.49 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4416....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4416....1S/abstract) |
| Classification references | [2026TNSCR4543....1K](https://ui.adsabs.harvard.edu/abs/2026TNSCR4543....1K/abstract) |
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
| Separation | 0.45058° · 27.03′ |
| Catalog description | NGC 4329 is an elliptical galaxy located 144 million light-years away in the constellation Corvus. The galaxy was discovered by astronomer John Herschel on March 9, 1828. NGC 4329 is host a supermassive black hole with an estimated mass of 3.1×108 solar masses. NGC 4329 is a member of a group of 5 galaxies known as [T2015] nest 100478. NGC 4329 is the brightest member of this group and the group includes the galaxies IC 785, IC 786, MCG-02-32-006, and LEDA 170189. The redshift of NGC 4329 places it in the within the bounds of the Hydra-Centaurus supercluster. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 2405 has the different designation NGC 4329 as its display name.

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahyf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=132.053424%2036.7792155&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 4. [AT2026akhh](https://www.wis-tns.org/object/2026akhh) near IC2013

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 93/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2013 as this object's host. The 0.18157° (10.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T11:05:21Z · 4 days · 18.34 orange |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.18157° · 10.89′ |
| Catalog description | considerably bright, considerably large, much / magnitude extended 170deg , considerably brighter middle, or in the middle, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤0.25°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.9936895%20-17.0988243&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 5. [AT2026akfo](https://www.wis-tns.org/object/2026akfo) near IC 4415

**Recommendation:** `hold` · **Priority:** `urgent` · **Score:** 90/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4415 as this object's host. The 0.38149° (22.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T13:12:28Z · 3 days · 17.73 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 4415** · `IC 4415` |
| Catalog display name | NGC 5555 |
| Type / constellation | Galaxy · Boo |
| Catalog magnitude / angular size | — · 0.62′ × 0.3′ |
| Distance | 538.83 ly |
| Separation | 0.38149° · 22.89′ |
| Catalog description | NGC 5555 is a spiral galaxy located in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 11200 ± 20 km/s, which corresponds to a Hubble distance of 165.20 ± 11.57 Mpc. It was originally discovered in 1886 by the American astronomer, Ormond Stone. NGC 5555 is situated close to the celestial equator and given its visual magnitude of 15.53, NGC 5555 is visible only through long exposure photography. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4415 has the different designation NGC 5555 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=216.4644387%2016.4636257&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 6. [AT2026akhc](https://www.wis-tns.org/object/2026akhc) near IC 4168

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
| Discovery | 2026-11-19T15:05:42Z · 2 days · 18.43 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 7. [AT2026akhs](https://www.wis-tns.org/object/2026akhs) near NGC6958

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 83/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC6958 as this object's host. The 1.67482° (100.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T18:21:53Z · 3 days · 18.03 orange |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude ≤18.5; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=314.2312711%20-38.4392844&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 8. [AT2026ajsb](https://www.wis-tns.org/object/2026ajsb) near IC765

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC765 as this object's host. The 0.75222° (45.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:56:47Z · 7 days · 18.22 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 9. [TDE2026akgn](https://www.wis-tns.org/object/2026akgn) near NGC1458

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1458 as this object's host. The 1.60630° (96.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | TDE-featureless |
| Redshift | 0.105 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-24T11:29:30Z · 28 days · 17.86 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC1458** · `NGC1458` |
| Catalog display name | NGC1458 |
| Type / constellation | Nebula · Eridanus |
| Catalog magnitude / angular size | — · 2.2′ × 2.2′ |
| Distance | — |
| Separation | 1.60630° · 96.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.3962922%20-19.8366345&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 10. [AT2026aklg](https://www.wis-tns.org/object/2026aklg) near NGC5204

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 75/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC5204 as this object's host. The 1.43417° (86.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:51:54Z · 10 days · 17.75 g |
| Latest public photometry | Not available in the staged feed |
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

### 11. [AT2026ajjz](https://www.wis-tns.org/object/2026ajjz) near IC656

**Recommendation:** `approve` · **Priority:** `urgent` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC656 as this object's host. The 0.87219° (52.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T15:02:11Z · 13 days · 18.38 orange |
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

### 12. [SN2026akbo](https://www.wis-tns.org/object/2026akbo) near NGC3344

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 95/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3344 as this object's host. The 0.96186° (57.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0173 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T06:06:39Z · 4 days · 18.76 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4673....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4673....1R/abstract) |
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
| Separation | 0.96186° · 57.71′ |
| Catalog description | NGC 3344 is a relatively isolated barred spiral galaxy around half the size of the Milky Way located 22.5 million light years away in the constellation Leo Minor. It was discovered by German-British astronomer William Herschel on 6 April 1785. |

**Why it ranked:** confirmed high-interest transient class; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.912128%2025.320421&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 13. [AT2026ajxd](https://www.wis-tns.org/object/2026ajxd) near NGC2276

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 85/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2276 as this object's host. The 0.19202° (11.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T02:46:53Z · 8 days · 19.32 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=113.27614%2085.597616&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 14. [SN2026ahuu](https://www.wis-tns.org/object/2026ahuu) near IC449

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC449 as this object's host. The 1.92939° (115.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.07 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:07:43Z · 19 days · 18.69 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4404....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4404....1S/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahuu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=100.94736%2069.420988&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 15. [SN2026ahze](https://www.wis-tns.org/object/2026ahze) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.92287° (115.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.092 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:33:40Z · 18 days · 18.71 g |
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

### 16. [AT2026ajxv](https://www.wis-tns.org/object/2026ajxv) near NGC 3277

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3277 as this object's host. The 0.80128° (48.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:06:01Z · 7 days · 19.13 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 17. [AT2026akhu](https://www.wis-tns.org/object/2026akhu) near NGC2325

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 80/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2325 as this object's host. The 0.61029° (36.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T03:25:37Z · 3 days · 19.35 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=105.9784267%20-28.15199&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 18. [AT2026ajrk](https://www.wis-tns.org/object/2026ajrk) near IC1733

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1733 as this object's host. The 1.11166° (66.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T06:40:30Z · 7 days · 19.45 w |
| Latest public photometry | Not available in the staged feed |
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

### 19. [AT2026ajva](https://www.wis-tns.org/object/2026ajva) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19660° (11.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 21.81 i |
| Latest public photometry | Not available in the staged feed |
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

### 20. [AT2026ajwf](https://www.wis-tns.org/object/2026ajwf) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.19359° (11.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.15 i |
| Latest public photometry | Not available in the staged feed |
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

### 21. [AT2026ajyd](https://www.wis-tns.org/object/2026ajyd) near IC600

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC600 as this object's host. The 1.36888° (82.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T06:07:10Z · 5 days · 19.16 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4661....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4661....1R/abstract) |
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
| Separation | 1.36888° · 82.13′ |
| Catalog description | faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, round, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.3198425%20-2.53237&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 22. [AT2026akaz](https://www.wis-tns.org/object/2026akaz) near Caldwell 3 (C3)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 3 (C3) as this object's host. The 1.12593° (67.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T14:52:08Z · 5 days · 19.3 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 23. [AT2026akgx](https://www.wis-tns.org/object/2026akgx) near NGC1569

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1569 as this object's host. The 1.05967° (63.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T22:19:06Z · 2 days · 19.28 L |
| Latest public photometry | Not available in the staged feed |
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

### 24. [AT2026akhd](https://www.wis-tns.org/object/2026akhd) near IC625

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC625 as this object's host. The 1.99202° (119.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T06:03:30Z · 3 days · 18.95 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.6930392%20-21.9438442&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 25. [AT2026akhf](https://www.wis-tns.org/object/2026akhf) near NGC3726

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3726 as this object's host. The 1.78481° (107.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T14:18:10Z · 2 days · 19.45 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 26. [AT2026akju](https://www.wis-tns.org/object/2026akju) near NGC741

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 73/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC741 as this object's host. The 0.15603° (9.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T14:21:07Z · 4 days · 22.1 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akju) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.226542%205.556869&fov=0.5&survey=P%2FDSS2%2Fcolor)

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
| Discovery | 2026-10-25T09:54:09Z · 27 days · 19.46 r |
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

### 28. [AT2026ajpq](https://www.wis-tns.org/object/2026ajpq) near NGC2549

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2549 as this object's host. The 0.59331° (35.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T03:55:02Z · 8 days · 19.37 wide |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajpq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=125.788333%2057.604842&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 29. [AT2026ajrw](https://www.wis-tns.org/object/2026ajrw) near NGC2768

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 72/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2768 as this object's host. The 0.41880° (25.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T04:23:39Z · 8 days · 19.35 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.5544312%2060.303245&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 30. [AT2026akit](https://www.wis-tns.org/object/2026akit) near IC1560

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 70/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1560 as this object's host. The 0.48582° (29.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T05:18:14Z · 3 days · 19.03 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.48582° · 29.15′ |
| Catalog description | extremely, excessively faint; = 164? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akit) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=9.5745%203.129639&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 31. [SN2026ajsm](https://www.wis-tns.org/object/2026ajsm) near IC1919

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 67/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1919 as this object's host. The 0.30868° (18.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0664 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T20:39:03Z · 23 days · 20.24 BG-q |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4646....1T](https://ui.adsabs.harvard.edu/abs/2026TNSTR4646....1T/abstract) |
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

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=51.225567%20-33.092131&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 32. [AT2026ahqj](https://www.wis-tns.org/object/2026ahqj) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 1.58832° (95.30′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T13:59:41Z · 23 days · 19.41 L |
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

[TNS object](https://www.wis-tns.org/object/2026ahqj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=48.793062%20-52.695789&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 33. [AT2026ahxx](https://www.wis-tns.org/object/2026ahxx) near IC310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC310 as this object's host. The 0.17684° (10.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-25T09:56:10Z · 27 days · 19.86 r |
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
| Subject | **IC310** · `IC310` |
| Catalog display name | IC310 |
| Type / constellation | Galaxy · Perseus |
| Catalog magnitude / angular size | 12.7 · 1.5′ × 1.42′ |
| Distance | 76,300 kpc |
| Separation | 0.17684° · 10.61′ |
| Catalog description | IC 310 is a lenticular galaxy located in the constellation Perseus. It is located 265 million light-years from Earth, which means, given its apparent dimensions, it is about 117,000 light-years across. The galaxy was discovered by Edward D. Swift on November 3, 1888. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahxx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.1657768%2041.5016802&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 34. [AT2026ajjk](https://www.wis-tns.org/object/2026ajjk) near NGC1169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1169 as this object's host. The 1.01795° (61.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T23:39:27Z · 9 days · 19.46 L |
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

### 35. [AT2026ajkb](https://www.wis-tns.org/object/2026ajkb) near IC486

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC486 as this object's host. The 1.22917° (73.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T12:37:47Z · 9 days · 19 cyan |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajkb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=119.181083%2027.543858&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 36. [AT2026ajrs](https://www.wis-tns.org/object/2026ajrs) near IC5261

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5261 as this object's host. The 1.21834° (73.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T20:50:16Z · 8 days · 19.27 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.6960475%20-19.4936975&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 37. [AT2026ajxy](https://www.wis-tns.org/object/2026ajxy) near IC 1894

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
| Discovery | 2026-11-09T23:00:52Z · 12 days · 19.88 L |
| Latest public photometry | Not available in the staged feed |
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

### 38. [AT2026akeu](https://www.wis-tns.org/object/2026akeu) near IC 3484

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3484 as this object's host. The 1.32084° (79.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T13:07:04Z · 9 days · 19.38 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 3484** · `IC 3484` |
| Catalog display name | NGC 7611 |
| Type / constellation | Galaxy · Com |
| Catalog magnitude / angular size | — · 0.78′ × 0.63′ |
| Distance | 139 ly |
| Separation | 1.32084° · 79.25′ |
| Catalog description | NGC 7611 is a lenticular galaxy located in the constellation of Pisces. Its velocity relative to the cosmic microwave background is 2,881 ± 32 km/s, which corresponds to a Hubble distance of 42.5 ± 3.0 Mpc. NGC 7611 was discovered by the Prussian astronomer Heinrich Louis d'Arrest on September 21, 1862 |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 3484 has the different designation NGC 7611 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akeu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=188.6944211%2018.6613173&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 39. [AT2026akev](https://www.wis-tns.org/object/2026akev) near IC 876

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 876 as this object's host. The 1.55431° (93.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T13:16:52Z · 9 days · 19.05 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 876** · `IC 876` |
| Catalog display name | NGC 3914 |
| Type / constellation | Galaxy · Vir |
| Catalog magnitude / angular size | — · 0.9′ × 0.76′ |
| Distance | — |
| Separation | 1.55431° · 93.26′ |
| Catalog description | NGC 3914 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 6466 ± 25 km/s, which corresponds to a Hubble distance of 95.38 ± 6.69 Mpc. However, six non-redshift measurements give a distance of 81.2 ± 2.8 Mpc. The galaxy was discovered by German-British astronomer William Herschel on 13 April 1784. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 876 has the different designation NGC 3914 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akev) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=198.2385616%203.8149166&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 40. [AT2026akhx](https://www.wis-tns.org/object/2026akhx) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.12692° (7.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 14 days · 21.13 r |
| Latest public photometry | Not available in the staged feed |
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

### 41. [AT2026akir](https://www.wis-tns.org/object/2026akir) near NGC4450

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC4450 as this object's host. The 0.23305° (13.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T22:35:02Z · 10 days · 20.71 g |
| Latest public photometry | Not available in the staged feed |
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

### 42. [AT2026akjq](https://www.wis-tns.org/object/2026akjq) near NGC3348

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 65/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3348 as this object's host. The 0.04326° (2.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T12:08:19Z · 19 days · 19.97 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.04326° · 2.60′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤0.25°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akjq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.9245277%2072.8214201&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 43. [AT2026ajru](https://www.wis-tns.org/object/2026ajru) near Collinder 176 (CR176)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 176 (CR176) as this object's host. The 1.06889° (64.13′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T02:16:35Z · 7 days · 18.7 orange |
| Latest public photometry | Not available in the staged feed |
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

### 44. [AT2026ajwa](https://www.wis-tns.org/object/2026ajwa) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 0.13206° (7.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:31:35Z · 6 days · 22.79 i |
| Latest public photometry | Not available in the staged feed |
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

### 45. [AT2026ajwp](https://www.wis-tns.org/object/2026ajwp) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.00471° (0.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 6 days · 21.79 i |
| Latest public photometry | Not available in the staged feed |
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

### 46. [AT2026ajxu](https://www.wis-tns.org/object/2026ajxu) near Collinder 27 (CR27)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 27 (CR27) as this object's host. The 1.69919° (101.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T09:38:01Z · 6 days · 19.22 cyan |
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
| Subject | **Collinder 27 (CR27)** · `CR27` |
| Catalog display name | Collinder 27 (CR27) |
| Type / constellation | Open cluster · Andromeda |
| Catalog magnitude / angular size | 8.9 · 4.5′ × 4.5′ |
| Distance | — |
| Separation | 1.69919° · 101.95′ |
| Catalog description | NGC 956 is an asterism in the constellation Andromeda. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajxu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=40.1534822%2045.5065691&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 47. [AT2026akap](https://www.wis-tns.org/object/2026akap) near Ghost of Jupiter

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Ghost of Jupiter as this object's host. The 1.78164° (106.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T05:23:23Z · 5 days · 19.32 wide |
| Latest public photometry | Not available in the staged feed |
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

### 48. [AT2026akfn](https://www.wis-tns.org/object/2026akfn) near IC 4287

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 4287 as this object's host. The 1.37018° (82.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T13:10:56Z · 3 days · 19.35 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 4287** · `IC 4287` |
| Catalog display name | NGC 1667 |
| Type / constellation | CiG · Com |
| Catalog magnitude / angular size | — · 1′ × 1.4′ |
| Distance | 148 ly |
| Separation | 1.37018° · 82.21′ |
| Catalog description | NGC 1667, also catalogued as NGC 1689, is a spiral galaxy located in the constellation Eridanus. It is located at a distance of about 150 million light years from Earth based on redshift-independent methods, which, given its apparent dimensions, means that NGC 1667 is about 80,000 light years across. Based on its redshift, the galaxy sits roughly 200 million light years away from the Sun. It was discovered by Édouard Stephan on December 13, 1884, and independently by Lewis Swift on October 22, 1886. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 4287 has the different designation NGC 1667 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=201.8766188%2026.1741373&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 49. [AT2026akgf](https://www.wis-tns.org/object/2026akgf) near Butterfly nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Butterfly nebula as this object's host. The 1.66856° (100.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T16:56:09Z · 4 days · 19.4 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Butterfly nebula** · `IC2220` |
| Catalog display name | Butterfly nebula |
| Type / constellation | reflection nebula · Carina |
| Catalog magnitude / angular size | — · 5′ × 5′ |
| Distance | — |
| Separation | 1.66856° · 100.11′ |
| Catalog description | IC 2220, also known as the Toby Jug Nebula, is a reflection nebula located 1200 light years away in the southern constellation of Carina. The nebula was observed by the Gemini South telescope in 2023. It has an almost symmetrical bipolar structure, made up of gas and dust, reflecting light of the central red giant star HR 3126. This is rarely seen because the end-of-life phase of this type of star is relatively brief. Astronomers think that it is formed following the interaction between the dying red giant and a former companion star. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=121.138504%20-57.797153&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 50. [AT2026akhl](https://www.wis-tns.org/object/2026akhl) near NGC2886

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2886 as this object's host. The 1.56605° (93.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T14:05:33Z · 2 days · 18.85 orange |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=141.2788886%20-20.2123571&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 51. [AT2026akhq](https://www.wis-tns.org/object/2026akhq) near IC3668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC3668 as this object's host. The 1.11334° (66.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T15:07:39Z · 2 days · 19.21 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 52. [AT2026akiv](https://www.wis-tns.org/object/2026akiv) near IC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC488 as this object's host. The 0.01538° (0.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T03:31:49Z · 1 days · 20 L |
| Latest public photometry | Not available in the staged feed |
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

### 53. [AT2026akiw](https://www.wis-tns.org/object/2026akiw) near IC656

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 63/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC656 as this object's host. The 1.14126° (68.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-20T05:22:04Z · 1 days · 19.34 L |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.14126° · 68.48′ |
| Catalog description | very small in angular size, cluster, neb? |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akiw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.88632%2018.060149&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 54. [AT2026ajxc](https://www.wis-tns.org/object/2026ajxc) near van den Bergh 12 (VDB12)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 62/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 12 (VDB12) as this object's host. The 0.51247° (30.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T10:32:37Z · 7 days · 19.17 cyan |
| Latest public photometry | Not available in the staged feed |
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

### 55. [AT2026ajrh](https://www.wis-tns.org/object/2026ajrh) near Messier 81

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Messier 81 as this object's host. The 0.68539° (41.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:28:39Z · 7 days · 20.85 w |
| Latest public photometry | Not available in the staged feed |
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

### 56. [AT2026ajri](https://www.wis-tns.org/object/2026ajri) near IC 1540

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
| Discovery | 2026-11-14T05:21:13Z · 7 days · 21.44 w |
| Latest public photometry | Not available in the staged feed |
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

### 57. [AT2026ajut](https://www.wis-tns.org/object/2026ajut) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.37521° (22.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.82 i |
| Latest public photometry | Not available in the staged feed |
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

### 58. [AT2026ajvg](https://www.wis-tns.org/object/2026ajvg) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 0.41178° (24.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.02 i |
| Latest public photometry | Not available in the staged feed |
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

### 59. [AT2026ajvj](https://www.wis-tns.org/object/2026ajvj) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.11 i |
| Latest public photometry | Not available in the staged feed |
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

### 60. [AT2026ajvp](https://www.wis-tns.org/object/2026ajvp) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 6 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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

### 61. [AT2026ajwc](https://www.wis-tns.org/object/2026ajwc) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 21.89 i |
| Latest public photometry | Not available in the staged feed |
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

### 62. [AT2026ajwe](https://www.wis-tns.org/object/2026ajwe) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 6 days · 22.91 i |
| Latest public photometry | Not available in the staged feed |
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

### 63. [AT2026ajwl](https://www.wis-tns.org/object/2026ajwl) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 6 days · 21.59 i |
| Latest public photometry | Not available in the staged feed |
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

### 64. [AT2026ajxh](https://www.wis-tns.org/object/2026ajxh) near IC2560

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2560 as this object's host. The 0.97287° (58.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T17:23:09Z · 6 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
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

### 65. [AT2026akau](https://www.wis-tns.org/object/2026akau) near NGC1532

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1532 as this object's host. The 0.51650° (30.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T07:15:40Z · 5 days · 21.29 g |
| Latest public photometry | Not available in the staged feed |
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

### 66. [AT2026akbd](https://www.wis-tns.org/object/2026akbd) near NGC3193

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3193 as this object's host. The 0.42737° (25.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:20:55Z · 7 days · 20.38 w |
| Latest public photometry | Not available in the staged feed |
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

### 67. [AT2026akbp](https://www.wis-tns.org/object/2026akbp) near UFO Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify UFO Galaxy as this object's host. The 0.59348° (35.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:53:38Z · 6 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4673....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4673....1R/abstract) |
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
| Separation | 0.59348° · 35.61′ |
| Catalog description | NGC 2683 is a field spiral galaxy in the northern constellation of Lynx. It was nicknamed the "UFO Galaxy" by the Astronaut Memorial Planetarium and Observatory. It was discovered by the astronomer William Herschel on February 5, 1788. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=133.536487%2033.9312893&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 68. [AT2026akcu](https://www.wis-tns.org/object/2026akcu) near IC1609

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1609 as this object's host. The 0.97202° (58.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T10:05:26Z · 5 days · 19.83 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1609** · `IC1609` |
| Catalog display name | IC1609 |
| Type / constellation | Galaxy · Phoenix |
| Catalog magnitude / angular size | 13.7 · 1.13′ × 0.99′ |
| Distance | 82,500 kpc |
| Separation | 0.97202° · 58.32′ |
| Catalog description | very faint, very small in angular size, round |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=13.771904%20-40.726419&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 69. [AT2026akfq](https://www.wis-tns.org/object/2026akfq) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.70604° (42.36′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T09:02:43Z · 5 days · 20.65 w |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.70604° · 42.36′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=32.5081558%20-7.6220205&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 70. [AT2026akgi](https://www.wis-tns.org/object/2026akgi) near NGC1398

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1398 as this object's host. The 0.95139° (57.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T06:33:19Z · 7 days · 21.85 z |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 0.95139° · 57.08′ |
| Catalog description | NGC 1398 is an isolated barred spiral galaxy exhibiting a double ring structure. It is located 65 million light years from the Earth, in the constellation of Fornax. The galaxy, with a diameter of approximately 292,000 light years, is bigger than the Milky Way. Over 100 billion stars are in the galaxy. The discovery credit for NGC 1398 is often given to Friedrich Winnecke of Karlsruhe, Germany, who observed it on 17 December 1868, while he was searching for comets. German astronomer Wilhelm Tempel had first observed it on 9 October 1861, but he did not publish his observation until 1882. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.4931479%20-27.2680663&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 71. [AT2026akgr](https://www.wis-tns.org/object/2026akgr) near IC 1623 A

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 A as this object's host. The 0.96916° (58.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T08:52:23Z · 5 days · 20.36 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 1623 A** · `IC 1623 A` |
| Catalog display name | IC 1623 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 1.05′ × 0.87′ |
| Distance | 254 ly |
| Separation | 0.96916° · 58.15′ |
| Catalog description | IC 1623 is a galaxy merger in the constellation Cetus. The galaxy lies about 250 million light years away from Earth, which means, given its apparent dimensions, that IC 1623 is approximately 115,000 light years across. It was discovered by Lewis Swift on November 19, 1897. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1623 A has the different designation IC 1623 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=16.4861332%20-18.3726908&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 72. [AT2026akjk](https://www.wis-tns.org/object/2026akjk) near IC 1753

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
| Discovery | 2026-11-21T02:58:29Z · 0 days · 19.66 g |
| Latest public photometry | Not available in the staged feed |
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

### 73. [AT2026akkr](https://www.wis-tns.org/object/2026akkr) near NGC3310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3310 as this object's host. The 0.66200° (39.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T18:41:45Z · 7 days · 20.74 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.037458%2052.875469&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 74. [AT2026akkw](https://www.wis-tns.org/object/2026akkw) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 0.73584° (44.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:30:14Z · 7 days · 20.93 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.486292%2042.387678&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 75. [AT2026akkz](https://www.wis-tns.org/object/2026akkz) near IC 1540

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 60/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1540 as this object's host. The 0.38069° (22.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T12:00:00Z · 4 days · 21.29 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=5.081292%2023.410489&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 76. [AT2026ajsc](https://www.wis-tns.org/object/2026ajsc) near Lynds Bright Nebula 1043 (LBN1043)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 57/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 1043 (LBN1043) as this object's host. The 1.49482° (89.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T18:56:34Z · 9 days · 18.5 Clear |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude ≤18.5; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajsc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=105.725333%20-18.029806&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 77. [AT2026aiep](https://www.wis-tns.org/object/2026aiep) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.65297° (99.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T20:57:15Z · 17 days · 19.17 wide |
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

### 78. [AT2026ajxa](https://www.wis-tns.org/object/2026ajxa) near Lynds Dark Nebula 1473 (LDN1473)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Dark Nebula 1473 (LDN1473) as this object's host. The 1.48149° (88.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:51:51Z · 6 days · 19.27 wide |
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
| Subject | **Lynds Dark Nebula 1473 (LDN1473)** · `LDN1473` |
| Catalog display name | Lynds Dark Nebula 1473 (LDN1473) |
| Type / constellation | Dark nebula · Perseus |
| Catalog magnitude / angular size | — · 26.05′ × 26.05′ |
| Distance | — |
| Separation | 1.48149° · 88.89′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; discovery magnitude in watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajxa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=62.7415418%2036.6351906&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 79. [AT2026akdi](https://www.wis-tns.org/object/2026akdi) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 1.67147° (100.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:37:55Z · 9 days · 19.26 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.67147° · 100.29′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.409%20-0.782225&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 80. [AT2026akfr](https://www.wis-tns.org/object/2026akfr) near IC4093

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 55/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC4093 as this object's host. The 1.35385° (81.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T14:34:36Z · 9 days · 19.2 cyan |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC4093** · `IC4093` |
| Catalog display name | IC4093 |
| Type / constellation | Nebula · Coma Berenices |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.35385° · 81.23′ |
| Catalog description | suspected, close preceding (westward) / pretty (adv., before F. B. L, S) a star of 8th magnitude |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; discovery magnitude in watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=194.9172146%2030.2458065&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 81. [AT2026ahxz](https://www.wis-tns.org/object/2026ahxz) near Lynds Bright Nebula 718 (LBN718)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 718 (LBN718) as this object's host. The 0.53252° (31.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T10:11:33Z · 18 days · 19.39 r |
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

### 82. [AT2026ajrf](https://www.wis-tns.org/object/2026ajrf) near The opal nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 54/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify The opal nebula as this object's host. The 0.75975° (45.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:11:11Z · 15 days · 18.9 orange |
| Latest public photometry | Not available in the staged feed |
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

### 83. [SN2026aela](https://www.wis-tns.org/object/2026aela) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.46981° (88.19′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.0503 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T20:31:24Z · 47 days · 18.14 L |
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

### 84. [AT2026ajrm](https://www.wis-tns.org/object/2026ajrm) near IC5338

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5338 as this object's host. The 1.79914° (107.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:12:20Z · 7 days · 19.52 cyan |
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
| Subject | **IC5338** · `IC5338` |
| Catalog display name | IC5338 |
| Type / constellation | Galaxy · Pegasus |
| Catalog magnitude / angular size | 13.7 · 1.26′ × 0.91′ |
| Distance | — |
| Separation | 1.79914° · 107.95′ |
| Catalog description | IC 5337 or JW100, is a spiral galaxy located 800 million light-years away from the Solar System in the constellation of Pegasus. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.6032235%2022.2585979&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 85. [AT2026ajux](https://www.wis-tns.org/object/2026ajux) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.74911° (104.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:17:24Z · 6 days · 22.92 i |
| Latest public photometry | Not available in the staged feed |
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

### 86. [AT2026ajuz](https://www.wis-tns.org/object/2026ajuz) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 6 days · 22.32 i |
| Latest public photometry | Not available in the staged feed |
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

### 87. [AT2026ajvc](https://www.wis-tns.org/object/2026ajvc) near IC 1417

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
| Discovery | 2026-11-15T00:28:09Z · 6 days · 22.34 i |
| Latest public photometry | Not available in the staged feed |
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

### 88. [AT2026ajvd](https://www.wis-tns.org/object/2026ajvd) near IC 1419

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
| Discovery | 2026-11-15T00:27:24Z · 6 days · 21.97 i |
| Latest public photometry | Not available in the staged feed |
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

### 89. [AT2026ajvf](https://www.wis-tns.org/object/2026ajvf) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 6 days · 22.71 i |
| Latest public photometry | Not available in the staged feed |
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

### 90. [AT2026ajvh](https://www.wis-tns.org/object/2026ajvh) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 20.46 i |
| Latest public photometry | Not available in the staged feed |
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

### 91. [AT2026ajvm](https://www.wis-tns.org/object/2026ajvm) near IC 1419

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
| Discovery | 2026-11-15T00:26:43Z · 6 days · 22.31 i |
| Latest public photometry | Not available in the staged feed |
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

### 92. [AT2026ajvn](https://www.wis-tns.org/object/2026ajvn) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.48 i |
| Latest public photometry | Not available in the staged feed |
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

### 93. [AT2026ajvr](https://www.wis-tns.org/object/2026ajvr) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 6 days · 21.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 94. [AT2026ajvu](https://www.wis-tns.org/object/2026ajvu) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.67055° (100.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.74 i |
| Latest public photometry | Not available in the staged feed |
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

### 95. [AT2026ajvy](https://www.wis-tns.org/object/2026ajvy) near IC 1419

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
| Discovery | 2026-11-15T00:28:09Z · 6 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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

### 96. [AT2026ajwb](https://www.wis-tns.org/object/2026ajwb) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.7 i |
| Latest public photometry | Not available in the staged feed |
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

### 97. [AT2026ajwg](https://www.wis-tns.org/object/2026ajwg) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.99 i |
| Latest public photometry | Not available in the staged feed |
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

### 98. [AT2026ajwh](https://www.wis-tns.org/object/2026ajwh) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.85355° (111.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.77 i |
| Latest public photometry | Not available in the staged feed |
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

### 99. [AT2026ajwi](https://www.wis-tns.org/object/2026ajwi) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.84 i |
| Latest public photometry | Not available in the staged feed |
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

### 100. [AT2026ajwn](https://www.wis-tns.org/object/2026ajwn) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.03799° (62.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.67 i |
| Latest public photometry | Not available in the staged feed |
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

### 101. [AT2026ajwr](https://www.wis-tns.org/object/2026ajwr) near IC 1417

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
| Discovery | 2026-11-15T00:28:47Z · 6 days · 21.31 i |
| Latest public photometry | Not available in the staged feed |
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

### 102. [AT2026ajws](https://www.wis-tns.org/object/2026ajws) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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

### 103. [AT2026ajwt](https://www.wis-tns.org/object/2026ajwt) near IC 1419

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
| Discovery | 2026-11-15T00:27:24Z · 6 days · 19.73 i |
| Latest public photometry | Not available in the staged feed |
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

### 104. [AT2026ajwv](https://www.wis-tns.org/object/2026ajwv) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.68 i |
| Latest public photometry | Not available in the staged feed |
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

### 105. [AT2026ajww](https://www.wis-tns.org/object/2026ajww) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 22.29 i |
| Latest public photometry | Not available in the staged feed |
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

### 106. [AT2026ajwx](https://www.wis-tns.org/object/2026ajwx) near IC 1417

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
| Discovery | 2026-11-15T00:29:36Z · 6 days · 23.14 i |
| Latest public photometry | Not available in the staged feed |
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

### 107. [AT2026akam](https://www.wis-tns.org/object/2026akam) near IC1657

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.69463° (101.68′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T10:12:24Z · 5 days · 19.7 L |
| Latest public photometry | Not available in the staged feed |
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

### 108. [AT2026akao](https://www.wis-tns.org/object/2026akao) near IC 1419

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
| Discovery | 2026-11-15T00:45:25Z · 6 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
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

### 109. [AT2026akaq](https://www.wis-tns.org/object/2026akaq) near IC 2031

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
| Discovery | 2026-11-16T00:10:48Z · 5 days · 19.73 wide |
| Latest public photometry | Not available in the staged feed |
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

### 110. [AT2026akat](https://www.wis-tns.org/object/2026akat) near NGC1527

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1527 as this object's host. The 1.52157° (91.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T05:04:03Z · 7 days · 21.55 z |
| Latest public photometry | Not available in the staged feed |
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

### 111. [AT2026akcc](https://www.wis-tns.org/object/2026akcc) near IC2143

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2143 as this object's host. The 1.17282° (70.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T13:27:30Z · 4 days · 19.55 L |
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
| Separation | 1.17282° · 70.37′ |
| Catalog description | extremely, excessively faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, very much / magnitude extended 45deg , 3 stars (pl.) south following |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcc) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=87.3782312%20-19.54557&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 112. [AT2026akcy](https://www.wis-tns.org/object/2026akcy) near Caldwell 48 (C48)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 48 (C48) as this object's host. The 1.31632° (78.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T11:33:08Z · 3 days · 19.55 g |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=138.5117799%206.0988&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 113. [AT2026akdo](https://www.wis-tns.org/object/2026akdo) near IC 5374

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 5374 as this object's host. The 1.26092° (75.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T12:47:31Z · 6 days · 22.19 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.26092° · 75.66′ |
| Catalog description | NGC 5374 is a barred spiral galaxy in the constellation of Virgo. Its velocity with respect to the cosmic microwave background is 4,612±19 km/s, which corresponds to a Hubble distance of 221.9 ± 15.6 Mly (68.02 ± 4.77 Mpc). Additionally, seven non-redshift measurements give a similar mean distance of 224.16 ± 13.31 Mly (68.729 ± 4.081 Mpc). It was discovered by German-British astronomer William Herschel on 12 May 1793. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 5374 has the different designation NGC5374 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.352333%205.151561&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 114. [AT2026aken](https://www.wis-tns.org/object/2026aken) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.57182° (94.31′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T22:07:40Z · 7 days · 20.18 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.57182° · 94.31′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aken) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=151.778625%2031.801722&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 115. [AT2026akfv](https://www.wis-tns.org/object/2026akfv) near NGC1398

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1398 as this object's host. The 1.49814° (89.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T06:33:57Z · 7 days · 22.35 z |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.49814° · 89.89′ |
| Catalog description | NGC 1398 is an isolated barred spiral galaxy exhibiting a double ring structure. It is located 65 million light years from the Earth, in the constellation of Fornax. The galaxy, with a diameter of approximately 292,000 light years, is bigger than the Milky Way. Over 100 billion stars are in the galaxy. The discovery credit for NGC 1398 is often given to Friedrich Winnecke of Karlsruhe, Germany, who observed it on 17 December 1868, while he was searching for comets. German astronomer Wilhelm Tempel had first observed it on 9 October 1861, but he did not publish his observation until 1882. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=54.6678109%20-27.8353462&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 116. [AT2026akgo](https://www.wis-tns.org/object/2026akgo) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.42736° (85.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T15:19:07Z · 6 days · 20.59 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.42736° · 85.64′ |
| Catalog description | NGC 3319 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by William Herschel on Feb 3, 1788. It is rich in gas and lacks a galactic bulge. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgo) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=161.6955079%2041.6164957&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 117. [AT2026akgq](https://www.wis-tns.org/object/2026akgq) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.75554° (105.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T07:37:50Z · 5 days · 19.67 z |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.75554° · 105.33′ |
| Catalog description | extremely, excessively faint, extremely, excessively small in angular size, 530 north preceding |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.9458435%20-3.0211388&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 118. [AT2026akgt](https://www.wis-tns.org/object/2026akgt) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 1.96157° (117.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T08:36:16Z · 3 days · 20.41 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.96157° · 117.69′ |
| Catalog description | NGC 936 is a barred lenticular galaxy in the constellation Cetus. It is at a distance of about 60 million light-years away from Earth. Its nucleus and prominent bar have high surface brightness. Because of the shape of the prominent bar, the nucleus and the ring of stars at the end of the barrel, the galaxy has been compared with the shape of a TIE fighter, from the Star Wars universe, and thus NGC 936 has been named Darth Vader's Galaxy or Darth Vader's Starfighter. By measuring the radial velocity of the disc, Kormendy found in 1986 that the disc is stable, which is the reason why it is so smooth. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.8871952%20-2.8340357&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 119. [AT2026akgw](https://www.wis-tns.org/object/2026akgw) near NGC7457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7457 as this object's host. The 1.57742° (94.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T19:41:38Z · 6 days · 19.98 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgw) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=343.5460385%2029.5833122&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 120. [AT2026akho](https://www.wis-tns.org/object/2026akho) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.12255° (67.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:55:18Z · 7 days · 23.08 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akho) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.971611%20-49.0135335&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 121. [AT2026akif](https://www.wis-tns.org/object/2026akif) near IC 197

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 197 as this object's host. The 1.04947° (62.97′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T16:35:02Z · 7 days · 22.46 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akif) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.876958%203.826464&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 122. [AT2026akjn](https://www.wis-tns.org/object/2026akjn) near Silver Sliver Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Silver Sliver Galaxy as this object's host. The 1.99665° (119.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-21T04:12:52Z · 0 days · 19.97 g |
| Latest public photometry | Not available in the staged feed |
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

### 123. [AT2026akks](https://www.wis-tns.org/object/2026akks) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.31211° (78.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:17:45Z · 7 days · 20.65 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akks) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.085125%2041.374264&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 124. [AT2026akkx](https://www.wis-tns.org/object/2026akkx) near NGC3319

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 53/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3319 as this object's host. The 1.95134° (117.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:30:14Z · 7 days · 21.4 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=162.068417%2042.661697&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 125. [AT2026ahtx](https://www.wis-tns.org/object/2026ahtx) near IC1933

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1933 as this object's host. The 0.59197° (35.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T12:45:50Z · 20 days · 19.59 L |
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
| Separation | 0.59197° · 35.52′ |
| Catalog description | little (adv.); long (adj.) extended south preceding north following |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ahtx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=50.618679%20-52.441825&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 126. [AT2026aigt](https://www.wis-tns.org/object/2026aigt) near IC2367

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2367 as this object's host. The 0.90936° (54.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:49:26Z · 16 days · 20.07 L |
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
| Subject | **IC2367** · `IC2367` |
| Catalog display name | IC2367 |
| Type / constellation | Galaxy · Puppis |
| Catalog magnitude / angular size | 12.1 · 2.45′ × 1.3′ |
| Distance | 25,800 kpc |
| Separation | 0.90936° · 54.56′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, small in angular size |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aigt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=126.8460114%20-19.2742753&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 127. [AT2026aipd](https://www.wis-tns.org/object/2026aipd) near IC 1746

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
| Discovery | 2026-10-28T17:09:36Z · 24 days · 21.22 r |
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

### 128. [AT2026ajar](https://www.wis-tns.org/object/2026ajar) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 0.74867° (44.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 14 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4558....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4558....1X/abstract) |
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
| Separation | 0.74867° · 44.92′ |
| Catalog description | NGC 3169 is a spiral galaxy about 75 million light years away in the constellation Sextans. It has the morphological classification SA(s)a pec, which indicates this is a pure, unbarred spiral galaxy with tightly-wound arms and peculiar features. There is an asymmetrical spiral arm and an extended halo around the galaxy. It is a member of the NGC 3166 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajar) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=154.2913148%203.6432016&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 129. [AT2026ajjm](https://www.wis-tns.org/object/2026ajjm) near NGC779

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC779 as this object's host. The 0.37589° (22.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:18:57Z · 11 days · 20.16 L |
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
| Separation | 0.37589° · 22.55′ |
| Catalog description | NGC 779 is a spiral galaxy seen edge-on, located in the constellation Cetus. It is located at a distance of circa 60 million light years from Earth, which, given its apparent dimensions, means that NGC 779 is about 70,000 light years across. It was discovered by William Herschel on September 10, 1785. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.5916941%20-6.1404938&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 130. [AT2026ajjx](https://www.wis-tns.org/object/2026ajjx) near NGC3239

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3239 as this object's host. The 0.74061° (44.44′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T05:47:51Z · 9 days · 19.72 L |
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

[TNS object](https://www.wis-tns.org/object/2026ajjx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.07439%2017.88114&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 131. [AT2026ajrn](https://www.wis-tns.org/object/2026ajrn) near NGC2985

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2985 as this object's host. The 0.55170° (33.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T05:10:07Z · 8 days · 19.61 wide |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=145.886332%2072.473064&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 132. [AT2026ajsz](https://www.wis-tns.org/object/2026ajsz) near IC 74

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
| Discovery | 2026-11-08T16:04:48Z · 13 days · 22.82 g |
| Latest public photometry | Not available in the staged feed |
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

### 133. [AT2026ajta](https://www.wis-tns.org/object/2026ajta) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 0.88977° (53.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:12:00Z · 13 days · 22.45 g |
| Latest public photometry | Not available in the staged feed |
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

### 134. [AT2026ajtf](https://www.wis-tns.org/object/2026ajtf) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 0.82591° (49.55′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:45:07Z · 13 days · 21.43 r |
| Latest public photometry | Not available in the staged feed |
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

### 135. [AT2026ajtl](https://www.wis-tns.org/object/2026ajtl) near IC178

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC178 as this object's host. The 0.93972° (56.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T19:24:57Z · 23 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
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

### 136. [AT2026ajtr](https://www.wis-tns.org/object/2026ajtr) near NGC 2964

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2964 as this object's host. The 0.25419° (15.25′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T21:54:43Z · 18 days · 20.75 r |
| Latest public photometry | Not available in the staged feed |
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

### 137. [AT2026ajyc](https://www.wis-tns.org/object/2026ajyc) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 0.74711° (44.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T17:46:50Z · 12 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
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

### 138. [AT2026ajyh](https://www.wis-tns.org/object/2026ajyh) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 0.72506° (43.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T16:59:31Z · 11 days · 21.89 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=29.678917%201.064447&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 139. [AT2026ajyr](https://www.wis-tns.org/object/2026ajyr) near IC 1507

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
| Discovery | 2026-10-30T13:16:19Z · 22 days · 22.47 r |
| Latest public photometry | Not available in the staged feed |
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

### 140. [AT2026ajzb](https://www.wis-tns.org/object/2026ajzb) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.57000° (34.20′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 14 days · 21.83 r |
| Latest public photometry | Not available in the staged feed |
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

### 141. [AT2026ajzh](https://www.wis-tns.org/object/2026ajzh) near Local Group

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Local Group as this object's host. The 0.56395° (33.84′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:53:45Z · 12 days · 22.48 r |
| Latest public photometry | Not available in the staged feed |
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

### 142. [AT2026ajzp](https://www.wis-tns.org/object/2026ajzp) near IC 1481

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1481 as this object's host. The 0.91299° (54.78′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:25:55Z · 10 days · 23.34 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.772458%205.895517&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 143. [AT2026akaf](https://www.wis-tns.org/object/2026akaf) near NGC7723

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7723 as this object's host. The 0.30146° (18.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T03:02:55Z · 10 days · 20.79 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akaf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=354.611558%20-12.6688512&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 144. [AT2026akct](https://www.wis-tns.org/object/2026akct) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 0.95998° (57.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T00:36:20Z · 8 days · 22.34 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.95998° · 57.60′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akct) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.7193808%20-8.669707&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 145. [AT2026akdb](https://www.wis-tns.org/object/2026akdb) near NGC3166

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3166 as this object's host. The 0.47284° (28.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 14 days · 21.57 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.47284° · 28.37′ |
| Catalog description | NGC 3166 is a lenticular galaxy in the constellation Sextans. The galaxy lies about 65 million light years away from Earth, which means, given its apparent dimensions, that NGC 3166 is approximately 105,000 light years across. It was discovered by William Herschel on December 19, 1783. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=153.27875%203.870236&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 146. [AT2026akdd](https://www.wis-tns.org/object/2026akdd) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 0.78978° (47.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T17:45:36Z · 17 days · 22.46 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.78978° · 47.39′ |
| Catalog description | NGC 5042 is an intermediate spiral galaxy in the constellation of Hydra. Its velocity with respect to the cosmic microwave background for is 1,697±22 km/s, which corresponds to a Hubble distance of 81.6 ± 5.8 Mly (25.03 ± 1.78 Mpc). However, 15 non redshift measurements give a much closer distance of 47.88 ± 2.37 Mly (14.680 ± 0.726 Mpc). It was discovered by British astronomer John Herschel on 25 March 1836. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 1639 has the different designation NGC5042 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdd) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=17.542917%20-1.344783&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 147. [AT2026akdl](https://www.wis-tns.org/object/2026akdl) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 0.94676° (56.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:49:26Z · 9 days · 21.48 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.94676° · 56.81′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=159.738292%20-1.354281&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 148. [AT2026akdr](https://www.wis-tns.org/object/2026akdr) near NGC 3619

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3619 as this object's host. The 0.95077° (57.05′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:26:24Z · 20 days · 20.11 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 3619** · `NGC 3619` |
| Catalog display name | NGC 3619 |
| Type / constellation | Galaxy · UMa |
| Catalog magnitude / angular size | 12.53 · 3.89′ × 3.08′ |
| Distance | — |
| Separation | 0.95077° · 57.05′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=168.394208%2057.209956&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 149. [AT2026akea](https://www.wis-tns.org/object/2026akea) near NGC3245

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3245 as this object's host. The 0.39166° (23.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:17:45Z · 9 days · 20.51 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC3245** · `NGC3245` |
| Catalog display name | NGC3245 |
| Type / constellation | Galaxy · Leo Minor |
| Catalog magnitude / angular size | 10.8 · 3.61′ × 2.3′ |
| Distance | — |
| Separation | 0.39166° · 23.50′ |
| Catalog description | NGC 3245 is a lenticular galaxy in the constellation Leo Minor. It was discovered by William Herschel on April 11, 1785. It is a member of the NGC 3254 Group of galaxies, which is a member of the Leo II Groups, a series of galaxies and galaxy clusters strung out from the right edge of the Virgo Supercluster. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akea) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=157.186125%2028.278372&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 150. [AT2026akeh](https://www.wis-tns.org/object/2026akeh) near NGC 2903

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2903 as this object's host. The 0.83678° (50.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T21:05:45Z · 12 days · 20.92 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC 2903** · `NGC2903` |
| Catalog display name | NGC 2903 |
| Type / constellation | Galaxy · Leo |
| Catalog magnitude / angular size | 8.9 · 11.94′ × 5.28′ |
| Distance | — |
| Separation | 0.83678° · 50.21′ |
| Catalog description | NGC 2903 is an isolated barred spiral galaxy in the equatorial constellation of Leo, positioned about 1.5° due south of Lambda Leonis. It was discovered by German-born astronomer William Herschel, who cataloged it on November 16, 1784. He mistook it as a double nebula, as did subsequent observers, and it wasn't until the nineteenth century that the Third Earl of Rosse resolved into a spiral form. J. L. E. Dreyer assigned it the identifiers 2903 and 2905 in his New General Catalogue; NGC 2905 now designates a luminous knot in the northeastern spiral arm. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akeh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=142.791208%2020.697336&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 151. [AT2026akei](https://www.wis-tns.org/object/2026akei) near IC200

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC200 as this object's host. The 0.38584° (23.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T20:32:38Z · 11 days · 21.27 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC200** · `IC200` |
| Catalog display name | IC200 |
| Type / constellation | Galaxy · Triangulum |
| Catalog magnitude / angular size | 12.8 · 1.38′ × 1.06′ |
| Distance | 68,400 kpc |
| Separation | 0.38584° · 23.15′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) large, round, brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akei) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=31.548%2030.825417&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 152. [AT2026akfl](https://www.wis-tns.org/object/2026akfl) near IC769

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC769 as this object's host. The 0.41936° (25.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T13:07:04Z · 9 days · 19.76 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC769** · `IC769` |
| Catalog display name | IC769 |
| Type / constellation | Galaxy · Virgo |
| Catalog magnitude / angular size | 13.4 · 2.2′ × 1.51′ |
| Distance | 37,400 kpc |
| Separation | 0.41936° · 25.16′ |
| Catalog description | very faint, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, very little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=183.4802437%2012.370644&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 153. [AT2026akhy](https://www.wis-tns.org/object/2026akhy) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.74894° (44.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 14 days · 20.64 r |
| Latest public photometry | Not available in the staged feed |
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

### 154. [AT2026akhz](https://www.wis-tns.org/object/2026akhz) near IC 673

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
| Discovery | 2026-11-10T22:55:12Z · 11 days · 22.82 g |
| Latest public photometry | Not available in the staged feed |
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

### 155. [AT2026akia](https://www.wis-tns.org/object/2026akia) near NGC3166

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3166 as this object's host. The 0.95306° (57.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:40:48Z · 9 days · 20.98 g |
| Latest public photometry | Not available in the staged feed |
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

### 156. [AT2026akib](https://www.wis-tns.org/object/2026akib) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 0.61522° (36.91′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:45:07Z · 13 days · 21.56 r |
| Latest public photometry | Not available in the staged feed |
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

### 157. [AT2026akic](https://www.wis-tns.org/object/2026akic) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 0.77839° (46.70′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 14 days · 21.72 r |
| Latest public photometry | Not available in the staged feed |
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

### 158. [AT2026akjt](https://www.wis-tns.org/object/2026akjt) near IC 632

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
| Discovery | 2026-11-10T22:43:40Z · 11 days · 22.87 g |
| Latest public photometry | Not available in the staged feed |
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

### 159. [AT2026akko](https://www.wis-tns.org/object/2026akko) near IC2446

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 52/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2446 as this object's host. The 0.75145° (45.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:59:02Z · 9 days · 22.14 g |
| Latest public photometry | Not available in the staged feed |
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

### 160. [AT2026ajvi](https://www.wis-tns.org/object/2026ajvi) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.76418° (45.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 6 days · 21.93 i |
| Latest public photometry | Not available in the staged feed |
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

### 161. [AT2026ajvs](https://www.wis-tns.org/object/2026ajvs) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.83221° (49.93′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 6 days · 22.2 i |
| Latest public photometry | Not available in the staged feed |
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

### 162. [AT2026ajvt](https://www.wis-tns.org/object/2026ajvt) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38606° (23.16′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 6 days · 21.24 i |
| Latest public photometry | Not available in the staged feed |
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

### 163. [AT2026akbc](https://www.wis-tns.org/object/2026akbc) near IC2030

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2030 as this object's host. The 0.58630° (35.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T10:56:11Z · 6 days · 20.89 w |
| Latest public photometry | Not available in the staged feed |
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

### 164. [AT2026akfx](https://www.wis-tns.org/object/2026akfx) near IC2055

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2055 as this object's host. The 0.92566° (55.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:56:00Z · 7 days · 22.85 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.92566° · 55.54′ |
| Catalog description | faint, small in angular size, considerably extended north-south, suspected |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=63.0463567%20-48.8529053&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 165. [AT2026akgs](https://www.wis-tns.org/object/2026akgs) near NGC7161

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 50/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7161 as this object's host. The 0.86287° (51.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T04:58:15Z · 7 days · 21.21 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **NGC7161** · `NGC7161` |
| Catalog display name | NGC7161 |
| Type / constellation | Nebula · Pegasus |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.86287° · 51.77′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.8639663%202.895452&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 166. [SN2026aiop](https://www.wis-tns.org/object/2026aiop) near Lynds Bright Nebula 773 (LBN773)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 49/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 773 (LBN773) as this object's host. The 0.84759° (50.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.062 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T07:58:48Z · 16 days · 20.23 r |
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
| Subject | **Lynds Bright Nebula 773 (LBN773)** · `LBN773` |
| Catalog display name | Lynds Bright Nebula 773 (LBN773) |
| Type / constellation | HII · Taurus |
| Catalog magnitude / angular size | — · 150′ × 120′ |
| Distance | — |
| Separation | 0.84759° · 50.86′ |
| Catalog description | No catalog description available. |

**Why it ranked:** confirmed high-interest transient class; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026aiop) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=56.4124213%2022.749387&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 167. [AT2026ajye](https://www.wis-tns.org/object/2026ajye) near Lynds Bright Nebula 878 (LBN878)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 47/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 878 (LBN878) as this object's host. The 1.00364° (60.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:32:41Z · 13 days · 18.67 Clear |
| Latest public photometry | Not available in the staged feed |
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

### 168. [AT2026ahuf](https://www.wis-tns.org/object/2026ahuf) near IC1401

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1401 as this object's host. The 1.09401° (65.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:14:32Z · 21 days · 19.8 i |
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

### 169. [AT2026aiit](https://www.wis-tns.org/object/2026aiit) near IC 536

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
| Discovery | 2026-10-26T12:16:17Z · 26 days · 20.1 g |
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

### 170. [AT2026aiwf](https://www.wis-tns.org/object/2026aiwf) near NGC2681

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2681 as this object's host. The 1.89724° (113.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:43:40Z · 20 days · 21.09 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4534....1X](https://ui.adsabs.harvard.edu/abs/2026TNSTR4534....1X/abstract) |
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
| Separation | 1.89724° · 113.83′ |
| Catalog description | NGC 2681 is a lenticular galaxy in the constellation Ursa Major. The galaxy lies 50 million light years away from Earth, which means, given its apparent dimensions, that NGC 2681 is approximately 55,000 light years across. NGC 2681 has an active galactic nucleus and it is a type 3 Seyfert galaxy. Its nucleus is also a low-ionization nuclear emission-line region. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiwf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=131.2535792%2049.9808629&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 171. [AT2026ajji](https://www.wis-tns.org/object/2026ajji) near NGC 3294

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3294 as this object's host. The 1.46834° (88.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T06:15:17Z · 9 days · 19.77 L |
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
| Separation | 1.46834° · 88.10′ |
| Catalog description | The position in 1987A&AS...70..191S is 13 arcsec southeast of the nucleus. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajji) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=158.8641302%2038.7842591&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 172. [AT2026ajjs](https://www.wis-tns.org/object/2026ajjs) near NGC3198

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3198 as this object's host. The 1.44291° (86.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T06:12:54Z · 8 days · 19.73 L |
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
| Subject | **NGC3198** · `NGC3198` |
| Catalog display name | NGC3198 |
| Type / constellation | Galaxy · Ursa Major |
| Catalog magnitude / angular size | 10.4 · 6.46′ × 1.84′ |
| Distance | — |
| Separation | 1.44291° · 86.57′ |
| Catalog description | NGC 3198, also known as Herschel 146 is a barred spiral galaxy in the constellation Ursa Major. It was discovered by German-British astronomer William Herschel on 15 January 1788. NGC 3198 is located in the Leo Spur, which is part of the Virgo Supercluster, and is approximately 47 million light years away. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajjs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=156.1490167%2044.3697903&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 173. [AT2026ajrg](https://www.wis-tns.org/object/2026ajrg) near IC1386

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1386 as this object's host. The 1.28167° (76.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T00:21:13Z · 13 days · 19.83 i |
| Latest public photometry | Not available in the staged feed |
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

### 174. [AT2026ajrj](https://www.wis-tns.org/object/2026ajrj) near IC 2016

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 2016 as this object's host. The 1.84241° (110.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T12:03:19Z · 8 days · 20.87 w |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajrj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=58.5366584%2020.30768&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 175. [AT2026ajsf](https://www.wis-tns.org/object/2026ajsf) near IC 17

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 17 as this object's host. The 1.57719° (94.63′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T21:33:37Z · 8 days · 19.68 L |
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
| Subject | **IC 17** · `IC 17` |
| Catalog display name | IC 1101 |
| Type / constellation | Galaxy · Cet |
| Catalog magnitude / angular size | — · 0.67′ × 0.54′ |
| Distance | — |
| Separation | 1.57719° · 94.63′ |
| Catalog description | IC 1101 is a class S0 supergiant (cD) lenticular galaxy at the center of the Abell 2029 galaxy cluster. It has an isophotal diameter at about 123.65 to 169.61 kiloparsecs. It possesses a diffuse core which is the largest core of any galaxy known to date, and contains a supermassive black hole, one of the largest discovered. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 17 has the different designation IC 1101 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajsf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=8.170458%203.830203&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 176. [AT2026ajss](https://www.wis-tns.org/object/2026ajss) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.55710° (93.43′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T17:22:33Z · 10 days · 22.86 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajss) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=34.212%203.7757&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 177. [AT2026ajtg](https://www.wis-tns.org/object/2026ajtg) near NGC3521

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3521 as this object's host. The 1.08432° (65.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:49:26Z · 12 days · 22.02 r |
| Latest public photometry | Not available in the staged feed |
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

### 178. [AT2026ajti](https://www.wis-tns.org/object/2026ajti) near IC 1757

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1757 as this object's host. The 1.42421° (85.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T16:56:38Z · 11 days · 22.44 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajti) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=30.272125%200.564381&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 179. [AT2026ajtn](https://www.wis-tns.org/object/2026ajtn) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 1.68238° (100.94′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T22:03:21Z · 20 days · 21.43 g |
| Latest public photometry | Not available in the staged feed |
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

### 180. [AT2026ajtv](https://www.wis-tns.org/object/2026ajtv) near IC509

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC509 as this object's host. The 1.28504° (77.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:23:02Z · 17 days · 21.33 r |
| Latest public photometry | Not available in the staged feed |
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

### 181. [AT2026ajtw](https://www.wis-tns.org/object/2026ajtw) near UFO Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify UFO Galaxy as this object's host. The 1.99519° (119.71′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:34:33Z · 17 days · 21.32 r |
| Latest public photometry | Not available in the staged feed |
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

### 182. [AT2026ajty](https://www.wis-tns.org/object/2026ajty) near IC2378

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2378 as this object's host. The 1.21289° (72.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T21:37:26Z · 17 days · 21.65 r |
| Latest public photometry | Not available in the staged feed |
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

### 183. [AT2026ajug](https://www.wis-tns.org/object/2026ajug) near IC1525

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1525 as this object's host. The 1.31062° (78.64′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:17:45Z · 14 days · 21.26 g |
| Latest public photometry | Not available in the staged feed |
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

### 184. [AT2026ajum](https://www.wis-tns.org/object/2026ajum) near IC 1540

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1540 as this object's host. The 1.37052° (82.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T12:56:09Z · 10 days · 22.35 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajum) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.395125%2025.045464&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 185. [AT2026ajyb](https://www.wis-tns.org/object/2026ajyb) near IC1657

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1657 as this object's host. The 1.48817° (89.29′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T10:46:37Z · 9 days · 19.98 L |
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

### 186. [AT2026ajyi](https://www.wis-tns.org/object/2026ajyi) near IC 1776

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
| Discovery | 2026-11-07T16:37:55Z · 14 days · 22.68 g |
| Latest public photometry | Not available in the staged feed |
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

### 187. [AT2026ajyl](https://www.wis-tns.org/object/2026ajyl) near IC 1639

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1639 as this object's host. The 1.77291° (106.37′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T16:42:14Z · 10 days · 22.53 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajyl) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=19.413542%200.327408&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 188. [AT2026ajyt](https://www.wis-tns.org/object/2026ajyt) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.53398° (92.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T13:46:33Z · 22 days · 22.05 r |
| Latest public photometry | Not available in the staged feed |
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

### 189. [AT2026ajyx](https://www.wis-tns.org/object/2026ajyx) near IC1696

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1696 as this object's host. The 1.66353° (99.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T15:43:12Z · 16 days · 23 g |
| Latest public photometry | Not available in the staged feed |
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

### 190. [AT2026ajyy](https://www.wis-tns.org/object/2026ajyy) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 1.85756° (111.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:33:36Z · 14 days · 20.1 r |
| Latest public photometry | Not available in the staged feed |
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

### 191. [AT2026ajyz](https://www.wis-tns.org/object/2026ajyz) near IC 632

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
| Discovery | 2026-11-07T22:35:02Z · 14 days · 21.28 r |
| Latest public photometry | Not available in the staged feed |
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

### 192. [AT2026ajzc](https://www.wis-tns.org/object/2026ajzc) near Local Group

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Local Group as this object's host. The 1.45136° (87.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T22:49:26Z · 14 days · 21.7 r |
| Latest public photometry | Not available in the staged feed |
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

### 193. [AT2026ajzf](https://www.wis-tns.org/object/2026ajzf) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.39275° (83.56′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:46:33Z · 13 days · 21.83 r |
| Latest public photometry | Not available in the staged feed |
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

### 194. [AT2026ajzg](https://www.wis-tns.org/object/2026ajzg) near NGC3169

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3169 as this object's host. The 1.35429° (81.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:35:02Z · 12 days · 22.3 r |
| Latest public photometry | Not available in the staged feed |
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

### 195. [AT2026ajzi](https://www.wis-tns.org/object/2026ajzi) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.77766° (106.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:42:14Z · 11 days · 22.58 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=1.795875%201.699603&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 196. [AT2026ajzj](https://www.wis-tns.org/object/2026ajzj) near IC 173

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 173 as this object's host. The 1.13242° (67.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:56:38Z · 11 days · 22.67 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=27.857042%201.345936&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 197. [AT2026ajzy](https://www.wis-tns.org/object/2026ajzy) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.30641° (78.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T16:40:48Z · 14 days · 22.9 g |
| Latest public photometry | Not available in the staged feed |
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

### 198. [AT2026akaa](https://www.wis-tns.org/object/2026akaa) near NGC3640

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3640 as this object's host. The 1.98192° (118.92′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T22:56:38Z · 12 days · 21.91 r |
| Latest public photometry | Not available in the staged feed |
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

### 199. [AT2026akac](https://www.wis-tns.org/object/2026akac) near IC187

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC187 as this object's host. The 1.14616° (68.77′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T20:08:09Z · 13 days · 21.88 g |
| Latest public photometry | Not available in the staged feed |
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

### 200. [AT2026akae](https://www.wis-tns.org/object/2026akae) near Andromeda Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Andromeda Galaxy as this object's host. The 1.02507° (61.50′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T18:30:14Z · 9 days · 21.79 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akae) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=11.957125%2041.644789&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 201. [AT2026akah](https://www.wis-tns.org/object/2026akah) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.33761° (80.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T00:38:14Z · 8 days · 21.07 i |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akah) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=351.105899%20-8.6737289&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 202. [AT2026akdf](https://www.wis-tns.org/object/2026akdf) near Darth Vader's Galaxy

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Darth Vader's Galaxy as this object's host. The 1.56640° (93.98′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:46:33Z · 13 days · 23.34 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.56640° · 93.98′ |
| Catalog description | NGC 936 is a barred lenticular galaxy in the constellation Cetus. It is at a distance of about 60 million light-years away from Earth. Its nucleus and prominent bar have high surface brightness. Because of the shape of the prominent bar, the nucleus and the ring of stars at the end of the barrel, the galaxy has been compared with the shape of a TIE fighter, from the Star Wars universe, and thus NGC 936 has been named Darth Vader's Galaxy or Darth Vader's Starfighter. By measuring the radial velocity of the disc, Kormendy found in 1986 that the disc is stable, which is the reason why it is so smooth. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdf) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.791917%20-0.053244&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 203. [AT2026akdm](https://www.wis-tns.org/object/2026akdm) near IC 632

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 632 as this object's host. The 1.72914° (103.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:49:26Z · 9 days · 21.93 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.72914° · 103.75′ |
| Catalog description | NGC 5334 is a face-on barred spiral galaxy in the constellation Virgo. Its velocity with respect to the cosmic microwave background is 1668 ± 20 km/s, which corresponds to a Hubble distance of 80.2 ± 5.7 Mly (24.60 ± 1.75 Mpc). However, five non-redshift measurements give a distance of 108.68 ± 7.45 Mly (33.320 ± 2.283 Mpc). It was discovered by German-British astronomer William Herschel on 15 April 1787. It was also observed by American astronomer Lewis Swift on 20 April 1897 and listed in the Index Catalogue as IC 4338. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 632 has the different designation NGC 5334 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=160.298208%20-2.065061&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 204. [AT2026akdv](https://www.wis-tns.org/object/2026akdv) near IC 478

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 478 as this object's host. The 1.16737° (70.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:50:24Z · 15 days · 20.79 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 478** · `IC 478` |
| Catalog display name | IC 5332 |
| Type / constellation | Galaxy · Gem |
| Catalog magnitude / angular size | — · 0.66′ × 0.48′ |
| Distance | — |
| Separation | 1.16737° · 70.04′ |
| Catalog description | IC 5332, also known as PGC 71775, is an intermediate spiral galaxy about 30 million light-years away in the constellation Sculptor. It was discovered by American astronomer Lewis Swift on 19 November 1897. IC 5332 is too faint to be visible to the naked eye, with an apparent magnitude of 10.72. Viewed from earth, it is nearly face on. It has a very small central bulge and open spiral arms accounting for its SABc classification. The galaxy lies in the direction of the galactic south pole. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 478 has the different designation IC 5332 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.210167%2026.068689&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 205. [AT2026akek](https://www.wis-tns.org/object/2026akek) near IC1784

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1784 as this object's host. The 1.81247° (108.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T20:47:02Z · 11 days · 21.27 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.81247° · 108.75′ |
| Catalog description | faint, large, extended preceding-following, gradually brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akek) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=33.684625%2034.436211&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 206. [AT2026akfh](https://www.wis-tns.org/object/2026akfh) near IC 673

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 673 as this object's host. The 1.71606° (102.96′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T12:53:54Z · 18 days · 20.14 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.71606° · 102.96′ |
| Catalog description | NGC 673 is an intermediate spiral galaxy in the constellation of Aries. Its velocity with respect to the cosmic microwave background is 4894 ± 20 km/s, which corresponds to a Hubble distance of 235.4 ± 16.5 Mly (72.18 ± 5.06 Mpc). In addition, 31 non redshift measurements give a closer distance of 206.09 ± 5.54 Mly (63.187 ± 1.699 Mpc). The galaxy was discovered by German-British astronomer William Herschel on 4 September 1786. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 673 has the different designation NGC673 as its display name.

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=167.9173361%201.5237672&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 207. [AT2026akfy](https://www.wis-tns.org/object/2026akfy) near IC1495

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1495 as this object's host. The 1.84137° (110.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T00:52:44Z · 9 days · 22.41 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.84137° · 110.48′ |
| Catalog description | faint, small in angular size, little (adv.); long (adj.) brighter middle, or in the middle |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.3388159%20-15.2940541&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 208. [AT2026akge](https://www.wis-tns.org/object/2026akge) near IC2081

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2081 as this object's host. The 1.12136° (67.28′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T14:24:38Z · 9 days · 19.94 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC2081** · `IC2081` |
| Catalog display name | IC2081 |
| Type / constellation | Galaxy · Dorado |
| Catalog magnitude / angular size | 13.3 · 1′ × 0.77′ |
| Distance | — |
| Separation | 1.12136° · 67.28′ |
| Catalog description | extremely, excessively faint, very small in angular size, round, between 2 faint stars (pl.) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akge) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=68.917085%20-53.096498&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 209. [AT2026akgh](https://www.wis-tns.org/object/2026akgh) near NGC7606

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7606 as this object's host. The 1.05288° (63.17′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T00:38:14Z · 8 days · 22.43 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.05288° · 63.17′ |
| Catalog description | NGC 7606 is a spiral galaxy located in the constellation Aquarius. It is located at a distance of about 100 million light years from Earth, which, given its apparent dimensions, means that NGC 7606 is about 200,000 light years across. It was discovered by William Herschel on September 28, 1785. The galaxy is included in the Herschel 400 Catalogue. It lies 45 arcminutes northeast from psi2 Aquarii. It can be seen with a 4 inch telescope but its visibility is greatly affected by light pollution. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=350.6543355%20-9.0672805&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 210. [AT2026akix](https://www.wis-tns.org/object/2026akix) near IC2000

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2000 as this object's host. The 1.42748° (85.65′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T05:21:55Z · 15 days · 23.81 r |
| Latest public photometry | Not available in the staged feed |
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

### 211. [AT2026akjp](https://www.wis-tns.org/object/2026akjp) near Caldwell 3 (C3)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Caldwell 3 (C3) as this object's host. The 1.24289° (74.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T11:54:19Z · 13 days · 19.82 r |
| Latest public photometry | Not available in the staged feed |
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

### 212. [AT2026akjs](https://www.wis-tns.org/object/2026akjs) near NGC488

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC488 as this object's host. The 1.50636° (90.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T13:29:16Z · 13 days · 22.16 r |
| Latest public photometry | Not available in the staged feed |
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

### 213. [AT2026akke](https://www.wis-tns.org/object/2026akke) near NGC3310

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3310 as this object's host. The 1.50843° (90.51′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:27:50Z · 15 days · 20.8 g |
| Latest public photometry | Not available in the staged feed |
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

### 214. [AT2026akkh](https://www.wis-tns.org/object/2026akkh) near NGC2841

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2841 as this object's host. The 1.69532° (101.72′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T21:28:48Z · 12 days · 21.56 r |
| Latest public photometry | Not available in the staged feed |
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

### 215. [AT2026akkm](https://www.wis-tns.org/object/2026akkm) near NGC3198

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3198 as this object's host. The 1.12242° (67.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T22:33:36Z · 10 days · 21.22 g |
| Latest public photometry | Not available in the staged feed |
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

### 216. [AT2026akkq](https://www.wis-tns.org/object/2026akkq) near NGC 2782

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 45/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2782 as this object's host. The 1.48763° (89.26′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:06:14Z · 9 days · 21.92 g |
| Latest public photometry | Not available in the staged feed |
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

### 217. [AT2026ajsl](https://www.wis-tns.org/object/2026ajsl) near NGC3578

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3578 as this object's host. The 1.46782° (88.07′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T05:54:36Z · 6 days · 19.77 L |
| Latest public photometry | Not available in the staged feed |
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

### 218. [AT2026ajur](https://www.wis-tns.org/object/2026ajur) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.05093° (63.06′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 6 days · 23.23 i |
| Latest public photometry | Not available in the staged feed |
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

### 219. [AT2026ajve](https://www.wis-tns.org/object/2026ajve) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.56732° (94.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 22.03 i |
| Latest public photometry | Not available in the staged feed |
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

### 220. [AT2026ajvk](https://www.wis-tns.org/object/2026ajvk) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.82559° (109.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 21.75 i |
| Latest public photometry | Not available in the staged feed |
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

### 221. [AT2026ajvl](https://www.wis-tns.org/object/2026ajvl) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.62885° (97.73′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 6 days · 22.52 i |
| Latest public photometry | Not available in the staged feed |
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

### 222. [AT2026ajvq](https://www.wis-tns.org/object/2026ajvq) near IC5194

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5194 as this object's host. The 1.34031° (80.42′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:47Z · 6 days · 21.84 i |
| Latest public photometry | Not available in the staged feed |
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

### 223. [AT2026ajvx](https://www.wis-tns.org/object/2026ajvx) near IC1457

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1457 as this object's host. The 1.88540° (113.12′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:20:21Z · 6 days · 20.66 i |
| Latest public photometry | Not available in the staged feed |
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

### 224. [AT2026ajvz](https://www.wis-tns.org/object/2026ajvz) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.21470° (72.88′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:20:46Z · 6 days · 21.83 i |
| Latest public photometry | Not available in the staged feed |
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

### 225. [AT2026ajwj](https://www.wis-tns.org/object/2026ajwj) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.66580° (99.95′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:27:24Z · 6 days · 21.12 i |
| Latest public photometry | Not available in the staged feed |
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

### 226. [AT2026ajwk](https://www.wis-tns.org/object/2026ajwk) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 1.17313° (70.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T00:28:09Z · 6 days · 21.76 i |
| Latest public photometry | Not available in the staged feed |
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

### 227. [AT2026akcq](https://www.wis-tns.org/object/2026akcq) near IC2189

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2189 as this object's host. The 1.26363° (75.82′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T02:35:57Z · 6 days · 19.76 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.26363° · 75.82′ |
| Catalog description | planetary nebula stellar, pointlike |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=111.6370666%2010.0129798&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 228. [AT2026akdn](https://www.wis-tns.org/object/2026akdn) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.11151° (66.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T14:54:14Z · 7 days · 22.2 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.11151° · 66.69′ |
| Catalog description | suspected (13.5 mag) |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdn) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=342.239542%20-0.019772&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 229. [AT2026akdp](https://www.wis-tns.org/object/2026akdp) near IC 1623

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 1623 as this object's host. The 1.51486° (90.89′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T13:40:48Z · 6 days · 22.06 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.51486° · 90.89′ |
| Catalog description | IC 1623 is a galaxy merger in the constellation Cetus. The galaxy lies about 250 million light years away from Earth, which means, given its apparent dimensions, that IC 1623 is approximately 115,000 light years across. It was discovered by Lewis Swift on November 19, 1897. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=358.63175%20-0.650211&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 230. [AT2026akgj](https://www.wis-tns.org/object/2026akgj) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.41713° (85.03′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-15T04:21:25Z · 6 days · 22.45 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.41713° · 85.03′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=35.7199237%20-4.1313597&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 231. [AT2026akhj](https://www.wis-tns.org/object/2026akhj) near IC2328

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2328 as this object's host. The 1.00646° (60.39′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T03:36:43Z · 4 days · 19.63 wide |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.00646° · 60.39′ |
| Catalog description | preceding (westward) / pretty (adv., before F. B. L, S) bright, preceding (westward) / pretty (adv., before F. B. L, S) small in angular size, much / magnitude extended 65deg |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akhj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=124.8310664%2020.3441891&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 232. [AT2026akkt](https://www.wis-tns.org/object/2026akkt) near NGC3180

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3180 as this object's host. The 1.53716° (92.23′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T19:17:45Z · 7 days · 20.11 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkt) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.89175%2042.60735&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 233. [AT2026akkv](https://www.wis-tns.org/object/2026akkv) near IC2610

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 43/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC2610 as this object's host. The 1.26969° (76.18′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T21:23:02Z · 7 days · 20.93 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akkv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=164.290708%2033.798217&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 234. [AT2026aiko](https://www.wis-tns.org/object/2026aiko) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.38091° (22.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T04:02:26Z · 15 days · 19.85 r |
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
| Separation | 0.38091° · 22.85′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiko) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=329.403667%20-11.213353&fov=0.5&survey=P%2FDSS2%2Fcolor)

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
| Discovery | 2026-11-05T08:18:10Z · 16 days · 20.47 g |
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

### 236. [AT2026ajuh](https://www.wis-tns.org/object/2026ajuh) near IC111

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC111 as this object's host. The 0.80147° (48.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T19:48:00Z · 14 days · 22.16 g |
| Latest public photometry | Not available in the staged feed |
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

### 237. [AT2026ajup](https://www.wis-tns.org/object/2026ajup) near Collinder 116 (CR116)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 116 (CR116) as this object's host. The 0.84314° (50.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:27:50Z · 18 days · 21.25 r |
| Latest public photometry | Not available in the staged feed |
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

### 238. [AT2026ajxe](https://www.wis-tns.org/object/2026ajxe) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 0.53340° (32.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-31T05:16:02Z · 21 days · 23.8 i |
| Latest public photometry | Not available in the staged feed |
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

### 239. [AT2026ajym](https://www.wis-tns.org/object/2026ajym) near NGC7613

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7613 as this object's host. The 0.51096° (30.66′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-29T12:59:02Z · 23 days · 22.1 g |
| Latest public photometry | Not available in the staged feed |
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

### 240. [AT2026ajzw](https://www.wis-tns.org/object/2026ajzw) near NGC7668

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7668 as this object's host. The 0.85066° (51.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-01T13:32:09Z · 20 days · 22.42 r |
| Latest public photometry | Not available in the staged feed |
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

### 241. [AT2026akbr](https://www.wis-tns.org/object/2026akbr) near IC1538

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC1538 as this object's host. The 0.81828° (49.10′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:12:22Z · 9 days · 19.51 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4673....1R](https://ui.adsabs.harvard.edu/abs/2026TNSTR4673....1R/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC1538** · `IC1538` |
| Catalog display name | IC1538 |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 0.81828° · 49.10′ |
| Catalog description | extremely, excessively faint |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akbr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.5972864%2029.2150125&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 242. [AT2026akcp](https://www.wis-tns.org/object/2026akcp) near Lynds Bright Nebula 980 (LBN980)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 980 (LBN980) as this object's host. The 0.73350° (44.01′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-17T01:45:31Z · 4 days · 20.01 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026akcp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=75.7544708%20-10.9811762&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 243. [AT2026akec](https://www.wis-tns.org/object/2026akec) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 0.95372° (57.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:44:09Z · 12 days · 21.49 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.95372° · 57.22′ |
| Catalog description | (See Praesepe) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akec) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=128.98975%2019.7372&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 244. [AT2026akfs](https://www.wis-tns.org/object/2026akfs) near van den Bergh 156 (VDB156)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify van den Bergh 156 (VDB156) as this object's host. The 0.74673° (44.80′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-16T05:09:57Z · 5 days · 21.46 w |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **van den Bergh 156 (VDB156)** · `VDB156` |
| Catalog display name | van den Bergh 156 (VDB156) |
| Type / constellation | Nebula · Andromeda |
| Catalog magnitude / angular size | 3.6 · — |
| Distance | — |
| Separation | 0.74673° · 44.80′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026akfs) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.8529052%2043.0039361&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 245. [AT2026akgu](https://www.wis-tns.org/object/2026akgu) near Lynds Bright Nebula 896 (LBN896)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 896 (LBN896) as this object's host. The 0.59978° (35.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-19T12:37:30Z · 2 days · 20.6 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 0.59978° · 35.99′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026akgu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=67.0262013%20-6.7499822&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 246. [AT2026akie](https://www.wis-tns.org/object/2026akie) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 0.80143° (48.09′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:48:00Z · 9 days · 21.89 g |
| Latest public photometry | Not available in the staged feed |
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

### 247. [AT2026akiy](https://www.wis-tns.org/object/2026akiy) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 0.48687° (29.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-30T01:23:48Z · 22 days · 23.45 r |
| Latest public photometry | Not available in the staged feed |
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

### 248. [AT2026akkb](https://www.wis-tns.org/object/2026akkb) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 0.94983° (56.99′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:37:26Z · 15 days · 21.01 g |
| Latest public photometry | Not available in the staged feed |
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

### 249. [AT2026akkc](https://www.wis-tns.org/object/2026akkc) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 42/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 0.26232° (15.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:37:26Z · 15 days · 21.65 g |
| Latest public photometry | Not available in the staged feed |
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

### 250. [AT2026aetx](https://www.wis-tns.org/object/2026aetx) near NGC3166

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3166 as this object's host. The 0.65757° (39.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-07T12:41:51Z · 45 days · 19.1 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4063....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4063....1S/abstract) |
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
| Separation | 0.65757° · 39.45′ |
| Catalog description | NGC 3166 is a lenticular galaxy in the constellation Sextans. The galaxy lies about 65 million light years away from Earth, which means, given its apparent dimensions, that NGC 3166 is approximately 105,000 light years across. It was discovered by William Herschel on December 19, 1783. |

**Why it ranked:** unclassified transient candidate; older than 30 days; discovery magnitude in watch band; separation ≤1°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aetx) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=152.845916%203.1356251&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 251. [AT2026aijr](https://www.wis-tns.org/object/2026aijr) near NGC7447

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7447 as this object's host. The 1.89138° (113.48′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T09:48:34Z · 17 days · 20.08 L |
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

### 252. [AT2026aisi](https://www.wis-tns.org/object/2026aisi) near Collinder 133 (CR133)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 133 (CR133) as this object's host. The 1.35375° (81.22′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T10:33:14Z · 14 days · 20.26 r |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aisi) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=108.4571614%2012.4870812&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 253. [AT2026aitp](https://www.wis-tns.org/object/2026aitp) near NGC3181

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3181 as this object's host. The 1.80903° (108.54′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-04T11:24:52Z · 17 days · 19.76 g |
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
| Subject | **NGC3181** · `NGC3181` |
| Catalog display name | NGC3181 |
| Type / constellation | HII · Ursa Major |
| Catalog magnitude / angular size | 15.8 · 2.84′ × 0.83′ |
| Distance | — |
| Separation | 1.80903° · 108.54′ |
| Catalog description | NGC 3184, also known as The Little Pinwheel Galaxy, is an unbarred spiral galaxy approximately 40 million light-years away in the constellation Ursa Major. Its name comes from its resemblance to the Pinwheel Galaxy. It was discovered by German-British astronomer William Herschel on 18 March 1787. It has two HII regions named NGC 3180 and NGC 3181. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aitp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.6084449%2039.7934763&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 254. [AT2026aiys](https://www.wis-tns.org/object/2026aiys) near IC5251

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5251 as this object's host. The 1.74753° (104.85′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T19:48:30Z · 12 days · 19.55 L |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026aiys) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=339.5791041%2011.6438661&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 255. [AT2026ajkj](https://www.wis-tns.org/object/2026ajkj) near Intergalactic Wanderer

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Intergalactic Wanderer as this object's host. The 1.09787° (65.87′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T21:01:26Z · 15 days · 20.91 g |
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

### 256. [AT2026ajrp](https://www.wis-tns.org/object/2026ajrp) near Lynds Bright Nebula 484 (LBN484)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 484 (LBN484) as this object's host. The 1.74348° (104.61′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-14T07:18:12Z · 7 days · 19.58 cyan |
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
| Subject | **Lynds Bright Nebula 484 (LBN484)** · `LBN484` |
| Catalog display name | Lynds Bright Nebula 484 (LBN484) |
| Type / constellation | HII · Pegasus |
| Catalog magnitude / angular size | — · 60′ × 40′ |
| Distance | — |
| Separation | 1.74348° · 104.61′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajrp) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=352.9083397%2030.6834546&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 257. [AT2026ajsr](https://www.wis-tns.org/object/2026ajsr) near NGC728

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC728 as this object's host. The 1.25970° (75.58′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T16:32:09Z · 13 days · 22.88 g |
| Latest public photometry | Not available in the staged feed |
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

### 258. [AT2026ajsx](https://www.wis-tns.org/object/2026ajsx) near IC5248

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC5248 as this object's host. The 1.48459° (89.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T14:25:26Z · 15 days · 23.61 g |
| Latest public photometry | Not available in the staged feed |
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

### 259. [AT2026ajtd](https://www.wis-tns.org/object/2026ajtd) near NGC3387

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3387 as this object's host. The 1.71033° (102.62′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-08T22:37:55Z · 13 days · 21.48 r |
| Latest public photometry | Not available in the staged feed |
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

### 260. [AT2026ajtq](https://www.wis-tns.org/object/2026ajtq) near NGC737

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC737 as this object's host. The 1.51249° (90.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T19:37:55Z · 18 days · 21.87 r |
| Latest public photometry | Not available in the staged feed |
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

### 261. [AT2026ajub](https://www.wis-tns.org/object/2026ajub) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.29090° (77.45′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-05T21:28:48Z · 16 days · 21.61 g |
| Latest public photometry | Not available in the staged feed |
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

### 262. [AT2026ajuq](https://www.wis-tns.org/object/2026ajuq) near NGC7453

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7453 as this object's host. The 1.30353° (78.21′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T00:31:47Z · 11 days · 21.8 i |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajuq) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.621221%20-6.694867&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 263. [AT2026ajwy](https://www.wis-tns.org/object/2026ajwy) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.74562° (104.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:07:47Z · 12 days · 22.61 i |
| Latest public photometry | Not available in the staged feed |
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

### 264. [AT2026ajxk](https://www.wis-tns.org/object/2026ajxk) near NGC1498

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1498 as this object's host. The 1.41273° (84.76′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T17:26:25Z · 12 days · 20.08 L |
| Latest public photometry | Not available in the staged feed |
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

### 265. [AT2026akak](https://www.wis-tns.org/object/2026akak) near IC 5364

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
| Discovery | 2026-11-06T10:14:57Z · 15 days · 20.3 L |
| Latest public photometry | Not available in the staged feed |
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

### 266. [AT2026akcr](https://www.wis-tns.org/object/2026akcr) near NGC7526

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7526 as this object's host. The 1.29193° (77.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-13T00:28:39Z · 8 days · 21.46 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.29193° · 77.52′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akcr) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=348.2642884%20-10.4910011&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 267. [AT2026akdj](https://www.wis-tns.org/object/2026akdj) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 1.71319° (102.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:40:48Z · 9 days · 21.1 g |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.71319° · 102.79′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akdj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=155.336083%201.699122&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 268. [AT2026akeb](https://www.wis-tns.org/object/2026akeb) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.40035° (84.02′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:42:43Z · 12 days · 21.51 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.40035° · 84.02′ |
| Catalog description | (See Praesepe) |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akeb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=130.995375%2018.562139&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 269. [AT2026akeg](https://www.wis-tns.org/object/2026akeg) near NGC 2207 / IC 2163

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 2207 / IC 2163 as this object's host. The 1.81227° (108.74′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T21:02:52Z · 12 days · 21.24 r |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
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
| Separation | 1.81227° · 108.74′ |
| Catalog description | NGC 2207 and IC 2163 are a pair of colliding spiral galaxies about 80 million light-years away in the constellation Canis Major. NGC 2207 was discovered by British astronomer John Herschel on 24 January 1835, while IC 2163 was discovered by Herbert Howe on 11 February 1898. The pair together carry the nickname the Cosmic Owl. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akeg) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=135.758542%2023.688119&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 270. [AT2026akfj](https://www.wis-tns.org/object/2026akfj) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.79577° (107.75′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T11:54:26Z · 11 days · 20.52 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.79577° · 107.75′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akfj) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=142.66169%2029.3644545&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 271. [AT2026akgv](https://www.wis-tns.org/object/2026akgv) near NGC894

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC894 as this object's host. The 1.63959° (98.38′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T04:08:28Z · 12 days · 22.45 i |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.63959° · 98.38′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026akgv) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=36.989787%20-5.115035&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 272. [AT2026akhw](https://www.wis-tns.org/object/2026akhw) near NGC3229

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3229 as this object's host. The 1.62985° (97.79′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:37:55Z · 9 days · 21.25 g |
| Latest public photometry | Not available in the staged feed |
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

### 273. [AT2026akil](https://www.wis-tns.org/object/2026akil) near NGC3097

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC3097 as this object's host. The 1.78512° (107.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T22:29:16Z · 15 days · 21.05 g |
| Latest public photometry | Not available in the staged feed |
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

### 274. [AT2026akio](https://www.wis-tns.org/object/2026akio) near Collinder 113 (CR113)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 113 (CR113) as this object's host. The 1.46002° (87.60′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:00:00Z · 10 days · 21.46 g |
| Latest public photometry | Not available in the staged feed |
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

### 275. [AT2026akjb](https://www.wis-tns.org/object/2026akjb) near Lynds Bright Nebula 896 (LBN896)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 896 (LBN896) as this object's host. The 1.22063° (73.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-18T10:13:26Z · 3 days · 21.26 w |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 7 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akjb) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=66.303419%20-7.3539019&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 276. [AT2026akjm](https://www.wis-tns.org/object/2026akjm) near IC240

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC240 as this object's host. The 1.07528° (64.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T08:10:54Z · 12 days · 20.64 g |
| Latest public photometry | Not available in the staged feed |
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

### 277. [AT2026akkg](https://www.wis-tns.org/object/2026akkg) near Gemini nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Gemini nebula as this object's host. The 1.07214° (64.33′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-09T20:16:48Z · 12 days · 21.86 r |
| Latest public photometry | Not available in the staged feed |
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

### 278. [AT2026akkl](https://www.wis-tns.org/object/2026akkl) near Eskimo or Clown Nebula

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Eskimo or Clown Nebula as this object's host. The 1.67199° (100.32′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-11T18:34:33Z · 10 days · 21.16 g |
| Latest public photometry | Not available in the staged feed |
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

### 279. [AT2026akkp](https://www.wis-tns.org/object/2026akkp) near NGC2901

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 35/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC2901 as this object's host. The 1.15866° (69.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T22:00:28Z · 9 days · 21.28 g |
| Latest public photometry | Not available in the staged feed |
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

### 280. [AT2026aigg](https://www.wis-tns.org/object/2026aigg) near Lynds Bright Nebula 910 (LBN910)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 910 (LBN910) as this object's host. The 0.77477° (46.49′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-02T10:05:05Z · 19 days · 20.26 g |
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

### 281. [AT2026ajsh](https://www.wis-tns.org/object/2026ajsh) near Lynds Bright Nebula 439 (LBN439)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 439 (LBN439) as this object's host. The 0.79678° (47.81′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T19:43:55Z · 9 days · 19.72 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤1°.

[TNS object](https://www.wis-tns.org/object/2026ajsh) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=345.351332%2028.491949&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 282. [AT2026ajts](https://www.wis-tns.org/object/2026ajts) near Lynds Bright Nebula 891 (LBN891)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 34/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 891 (LBN891) as this object's host. The 0.64768° (38.86′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T22:48:00Z · 18 days · 20.91 r |
| Latest public photometry | Not available in the staged feed |
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

### 283. [SN2026adfc](https://www.wis-tns.org/object/2026adfc) near Lynds Bright Nebula 429 (LBN429)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 32/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 429 (LBN429) as this object's host. The 0.65958° (39.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.057903 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-29T06:55:47Z · 53 days · 18.97 r |
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

### 284. [AT2026absv](https://www.wis-tns.org/object/2026absv) near NGC 3561

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 28/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC 3561 as this object's host. The 1.10562° (66.34′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-14T10:32:09Z · 68 days · 19.48 L |
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

### 285. [AT2026aimd](https://www.wis-tns.org/object/2026aimd) near Collinder 65 (CR65)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 65 (CR65) as this object's host. The 1.83171° (109.90′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-06T08:37:25Z · 15 days · 20.38 i |
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

### 286. [AT2026ajsa](https://www.wis-tns.org/object/2026ajsa) near Lynds Bright Nebula 856 (LBN856)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 856 (LBN856) as this object's host. The 1.86922° (112.15′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T11:55:40Z · 9 days · 19.74 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajsa) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=49.856869%20-9.588252&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 287. [AT2026ajxz](https://www.wis-tns.org/object/2026ajxz) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.08910° (65.35′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-12T21:25:02Z · 9 days · 20.27 L |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajxz) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.543772%201.188224&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 288. [AT2026ajyk](https://www.wis-tns.org/object/2026ajyk) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.88407° (113.04′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-10T13:09:07Z · 11 days · 22.81 g |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026ajyk) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=344.112417%201.943786&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 289. [AT2026akda](https://www.wis-tns.org/object/2026akda) near Collinder 285 (CR285)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 285 (CR285) as this object's host. The 1.13740° (68.24′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-03T11:46:48Z · 18 days · 20.18 g |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | — |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **Collinder 285 (CR285)** · `CR285` |
| Catalog display name | Collinder 285 (CR285) |
| Type / constellation | Open cluster · Ursa Major |
| Catalog magnitude / angular size | — · — |
| Distance | — |
| Separation | 1.13740° · 68.24′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akda) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=179.0756697%2057.2991977&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 290. [AT2026akde](https://www.wis-tns.org/object/2026akde) near Lynds Bright Nebula 188 (LBN188)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 27/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Lynds Bright Nebula 188 (LBN188) as this object's host. The 1.86673° (112.00′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-11-07T14:28:19Z · 14 days · 22.36 r |
| Latest public photometry | Not available in the staged feed |
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
| Separation | 1.86673° · 112.00′ |
| Catalog description | No catalog description available. |

**Why it ranked:** unclassified transient candidate; discovered within 30 days; fainter than watch band; separation ≤2°.

[TNS object](https://www.wis-tns.org/object/2026akde) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=346.326208%200.486972&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 291. [TDE2026afrm](https://www.wis-tns.org/object/2026afrm) near IC 478

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 23/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 478 as this object's host. The 1.30982° (78.59′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | TDE |
| Redshift | 0.095 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T11:20:56Z · 34 days · 19.69 i |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4188....1S](https://ui.adsabs.harvard.edu/abs/2026TNSTR4188....1S/abstract) |
| Classification references | — |
| TNS remarks | — |
| Enrichment | `partial` via tns_staged_daily_delta, astroguide_catalog |
| Enrichment retrieved | Staged record timestamp |
| Enrichment gaps | tns_reported_host, latest_public_photometry, latest_public_spectrum |

| AstroGuide catalog context | Value |
|---|---|
| Subject | **IC 478** · `IC 478` |
| Catalog display name | IC 5332 |
| Type / constellation | Galaxy · Gem |
| Catalog magnitude / angular size | — · 0.66′ × 0.48′ |
| Distance | — |
| Separation | 1.30982° · 78.59′ |
| Catalog description | IC 5332, also known as PGC 71775, is an intermediate spiral galaxy about 30 million light-years away in the constellation Sculptor. It was discovered by American astronomer Lewis Swift on 19 November 1897. IC 5332 is too faint to be visible to the naked eye, with an apparent magnitude of 10.72. Viewed from earth, it is nearly face on. It has a very small central bulge and open spiral arms accounting for its SABc classification. The galaxy lies in the direction of the galactic south pole. |

> **Catalog data caution:** Catalog identity conflict: canonical ID IC 478 has the different designation IC 5332 as its display name.

**Why it ranked:** confirmed high-interest transient class; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026afrm) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=117.2913207%2027.3275235&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 292. [SN2026aeiu](https://www.wis-tns.org/object/2026aeiu) near NGC7158

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 20/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC7158 as this object's host. The 0.70237° (42.14′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.087 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-05T05:00:26Z · 47 days · 19.82 r |
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

### 293. [SN2026ahxw](https://www.wis-tns.org/object/2026ahxw) near Collinder 154 (CR154)

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 20/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Collinder 154 (CR154) as this object's host. The 0.75676° (45.41′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.147 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-20T10:50:01Z · 32 days · 20.84 g |
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

### 294. [AT2026ajuo](https://www.wis-tns.org/object/2026ajuo) near NGC925

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 15/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC925 as this object's host. The 0.76155° (45.69′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-09-13T16:59:31Z · 69 days · 20.79 r |
| Latest public photometry | Not available in the staged feed |
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

### 295. [SN2026aedz](https://www.wis-tns.org/object/2026aedz) near NGC1480

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC1480 as this object's host. The 1.10868° (66.52′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN IIn |
| Redshift | 0.1222 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-03T09:32:37Z · 49 days · 19.78 g |
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

### 296. [SN2026agok](https://www.wis-tns.org/object/2026agok) near Beehive cluster

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 13/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify Beehive cluster as this object's host. The 1.64277° (98.57′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | SN Ia |
| Redshift | 0.13 |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-17T22:23:31Z · 35 days · 19.99 r |
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

### 297. [AT2026agac](https://www.wis-tns.org/object/2026agac) near IC 1417

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
| Discovery | 2026-10-10T07:53:22Z · 42 days · 20.92 w |
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

### 298. [AT2026agzy](https://www.wis-tns.org/object/2026agzy) near NGC797

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify NGC797 as this object's host. The 1.65183° (99.11′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-13T12:52:44Z · 39 days · 20.21 L |
| Latest public photometry | Not available in the staged feed |
| Public spectra | 0 |
| Discovery reference | [2026TNSTR4313....1O](https://ui.adsabs.harvard.edu/abs/2026TNSTR4313....1O/abstract) |
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
| Separation | 1.65183° · 99.11′ |
| Catalog description | NGC 797 is a barred spiral galaxy in the constellation of Andromeda. Its velocity with respect to the cosmic microwave background is 5,414±17 km/s, which corresponds to a Hubble distance of 260.4 ± 18.3 Mly (79.85 ± 5.60 Mpc). However, three non-redshift measurements give a much farther mean distance of 369.64 ± 4.35 Mly (113.333 ± 1.333 Mpc). It was discovered by German-British astronomer William Herschel on 21 September 1786. |

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026agzy) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=18.8865856%20-15.0582538&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 299. [AT2026ajxo](https://www.wis-tns.org/object/2026ajxo) near IC 1507

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
| Discovery | 2026-09-13T02:53:11Z · 69 days · 22.85 i |
| Latest public photometry | Not available in the staged feed |
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

### 300. [AT2026ajyo](https://www.wis-tns.org/object/2026ajyo) near IC 173

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
| Discovery | 2026-10-17T17:24:00Z · 35 days · 22.17 r |
| Latest public photometry | Not available in the staged feed |
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

### 301. [AT2026ajzu](https://www.wis-tns.org/object/2026ajzu) near IC 3

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 8/100

**Decision note:** Hold until the AstroGuide catalog identity conflict is resolved.

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC 3 as this object's host. The 1.04710° (62.83′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-18T15:10:04Z · 34 days · 22.52 r |
| Latest public photometry | Not available in the staged feed |
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

**Why it ranked:** unclassified transient candidate; older than 30 days; fainter than watch band; separation ≤2°; nearby catalog subject is a galaxy; recognizable AstroGuide subject.

[TNS object](https://www.wis-tns.org/object/2026ajzu) · [Aladin coordinate view](https://aladin.u-strasbg.fr/AladinLite/?target=4.060708%200.566183&fov=0.5&survey=P%2FDSS2%2Fcolor)

### 302. [AT2026akjx](https://www.wis-tns.org/object/2026akjx) near IC132

**Recommendation:** `hold` · **Priority:** `watch` · **Score:** 0/100

> **Catalog image:** No provenance-safe hosted AstroGuide catalog thumbnail is available.

> **Near-field only:** TNS does not identify IC132 as this object's host. The 1.66808° (100.08′) match is contextual, not a physical association.

| TNS context | Value |
|---|---|
| Current classification | transient_candidate |
| Redshift | — |
| TNS host | Not supplied |
| Host redshift | — |
| Discovery | 2026-10-21T21:07:12Z · 31 days · 21.13 r |
| Latest public photometry | Not available in the staged feed |
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

## Policy notes

- Discovery magnitude is not a current magnitude; candidates may have faded.
- Confirmed high-interest classifications, age ≤30 days, discovery magnitude ≤18.5, separation ≤0.25°, nearby galaxies, and recognizable catalog subjects raise the score.
- The 18.5–19.5 magnitude band remains lower-priority watch material.
- Known CVs, variable stars, AGN/QSOs, asteroids/minor planets, and artifacts are rejected.
- Candidates outside AstroGuide's catalog fields are not necessarily uninteresting; they are outside this deliberately scoped queue.
