# Korea itinerary — shared task board

Last updated: 2026-10-21 UTC. Session owner: `3630416a` (Arena branch `arena/3630416a-koreatrip1`).

> **Branch constraint:** This workspace is bound to `arena/3630416a-koreatrip1`. Arena requires all work, pushes and PRs from this branch; do not create or switch to a `session-*/...` branch here. Other sessions should claim disjoint file scopes before editing, and coordinate through this board. A claim older than 60 minutes without a commit may be taken over with a handoff note.

| Task | Status | Owner | Exclusive file scope | Notes |
| --- | --- | --- | --- | --- |
| Source research, line-by-line verification and issue register | **in progress** | `3630416a` | `COORDINATION.md`, `src/data/**`, `docs/research/**` | Claimed 2026-10-21 UTC. Verify only against primary / official sources; record unsupported claims as unverified. |
| Website design and implementation | **in progress** | `3630416a` | `web/**`, `scripts/build.py` | Claimed 2026-10-21 UTC; static, responsive HTML pages generated from the verified research data. |
| Integration, accessibility, link/build checks, Pages and PR | **in progress** | `3630416a` | `.github/**`, `README.md`, `.gitignore`, `scripts/check.py` | Claimed 2026-10-21 UTC; run final cross-scope checks before PR and record deployment proof here. |

## Requests / handoffs
- None.

## Verification log
- 2026-10-21, `3630416a`: Source registry and per-row findings recorded in `src/data/sources.json`, `src/data/places.json`, `src/data/itinerary.json`, `src/data/review.json` and `docs/research/verification.md`. Official Palace, Visit Seoul/Busan/Korea, hotel/operator, metro, AREX and KORAIL sources checked; unsupported fields are `null`.
- Key corrections: Tuesday Gyeongbokgung is ordinarily closed ([palace operator](https://royal.khs.go.kr/ENG/contents/E702000000.do)); Bukchon visitor zone 10:00–17:00 ([Visit Seoul](https://english.visitseoul.net/attractions/Bukchon-Hanok-Village/ENP000261)); DDP is in Dongdaemun ([DDP](https://ddp.or.kr/?menuno=348)); Myeongdong Kyoja is Bib Gourmand ([MICHELIN](https://guide.michelin.com/us/en/seoul-capital-area/kr-seoul/restaurant/myeongdong-kyoja)); Lotte Main lists Nov 9, 2026 closed ([Lotte](https://www.lotteshopping.com/store/main?cstrCd=0001)).
- Open irregularities: year conflict (“Nov 2, 2006” versus weekdays consistent with Nov 1–9, 2026); full original itinerary unavailable; no verified flights, rooms, rail reservations, date-specific drone show or Busan baggage policy. [KORAIL](https://www.korail.com/global/eng/ticket/faq) says two-month ticket window while [VisitKorea](https://english.visitkorea.or.kr/svc/contents/infoBscView.do?vcontsId=140656) says usually one month. [Blueline main fares](https://www.bluelinepark.com/fare.do) and [Capsule subpage](https://www.bluelinepark.com/skyCapsuleFare.do) disagree; price suppressed. Separate Seongsu Rain Report Croissant remains unverified; only [Ikseon Rainbow](https://english.visitseoul.net/restaurants/rainreport/ENP933ykf) is listed. Full issue-by-issue ledger is `src/data/review.json`.

## Publication log
- Pending PR and Pages deployment. Do not claim deployment success without a successful Pages deployment check.
