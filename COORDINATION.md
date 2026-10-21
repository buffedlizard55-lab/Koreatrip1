# COORDINATION — shared task board

Repo: `buffedlizard55-lab/Koreatrip1` · Trip: Korea, 2 adult travelers, 1–9 Nov 2026 (Day 1 flight dated Oct 31/Nov 1)
Rule: a row is only marked **Verified** when its value was checked against an official source and that source is linked.
Blank verified fields = not confirmed. "Flagged" = listed on the **Flagged for Review** page of the site.

## Session note

- Only one agent session is active on this repo. Platform rules bind this session to branch
  `arena/b86112b5-koreatrip1`, so the `session-<id>/<task>` branches described in the brief were **not created**.
  All tasks below were done by this one session on `arena/b86112b5-koreatrip1`, which also acts as the integration session.
- File scopes are still listed per task so a later session can see what was touched.

## Task board

| ID | Task | Status | Owner (session) | Files touched | Notes |
|----|------|--------|-----------------|---------------|-------|
| T1 | Itinerary data extraction (every line of the brief) | done | session `b86112b5` | `data/trip.json` | 9 days, 80+ rows extracted from the brief |
| T2 | Line-by-line verification against official sources | done (partial, see below) | session `b86112b5` | `data/trip.json`, `data/sources.json` | Official values confirmed where a public official page exists; the rest blank + flagged |
| T3 | Static GitHub Pages site (landing, itinerary, entries, transit, hours, flagged, sources) | done | session `b86112b5` | site files (root `*.html`, `assets/`, `data/`) | No build step; pure HTML/CSS/JS |
| T4 | Integration: build check, link check, PR to `main`, merge, Pages deploy check | in progress | session `b86112b5` | site files (root `*.html`, `assets/`, `data/`), `COORDINATION.md` | See log |

## Log

- 2026-10-21 — Session `b86112b5` claimed T1–T4 on `arena/b86112b5-koreatrip1`. Repo had only `README.md` (no prior COORDINATION file; created here).
- Pages is configured for branch `main`, path `/` (the integration token cannot change the Pages source: HTTP 403). The site files were therefore moved to the repo root in T4, so no settings change is needed.
- T2 method: official pages were fetched or their search-indexed text was read (see `data/sources.json`). Where a value came only from a press or third-party site, the row is marked **Partially verified** or **Unverified** and flagged.
- **Irregularities found (summary; full list on the Flagged page):**
  1. Day 3 is **Tuesday 3 Nov 2026**. Gyeongbokgung Palace is **closed every Tuesday** (official royalpalacekr.org). Day 3 as written cannot visit the palace.
  2. Namsan Tower observatory hours written as "10:00–10:30". Official hours are 10:00–22:30 weekdays / 10:00–23:00 weekends.
  3. AREX Express written as 45 min / $7. Official: 43 min (T1) / 51 min (T2), adult ₩13,000.
  4. Airport limousine written as $13. Official fare figure not on the operator page; Incheon Airport official listing shows ₩17,000.
  5. Palace free-entry ages written as "under 19 and over 65". Official: free for ages 6 and under and 65+; ages 7–18 pay ₩1,500.
  6. Day 2 date "Nov 2, 2006" (year looks like a typo; 2 Nov 2026 is a Monday, matching the itinerary weekday).
  7. Day 1 date "Oct.31/Nov 1" is ambiguous (departure vs arrival). Not resolved.
  8. Day 9 KTX time "2 hours 45 min" vs official-press reports of about 2h15m fastest, 2h30–3h typical. KTX standard fare changed 1 Sep 2026 (₩59,800 → ₩54,400, per Seoul Economic Daily).
  9. Olive Young hours written as "8:00–12:00am". VISIT KOREA (Korea Tourism Organization) lists 10:00–22:30 for Myeongdong Main.
  10. Lotte Myeongdong Main hours differ between official Lotte pages (10:30–20:00 vs 10:30–20:30). Flagged.
  11. Uber in Korea works only through licensed taxis (Uber Taxi / UT). Uber's own Korea page describes this. Flagged for planning.
  12. Day 7 and Day 8 have no plan in the brief. Left empty.
  13. Items repeated across days (Rain Report Cafe on Day 4 and Day 6; Jayeondo on Day 4 and Day 6; pork belly rose pasta at "Chwihyang" and "Favorite of Ikseon"). Possible duplicates; flagged.
  14. "Musina Standard" (probably Musinsa Standard) and "Chwihyang" are not confirmed names. Not corrected by inference; flagged.
  15. Gyeongbokgung changing-of-the-guard ceremony was suspended for several days in Aug 2026 for heat (Seoul Economic Daily). Schedule risk, flagged.
  16. Stanford Hotel Myeongdong: address confirmed by VISIT SEOUL listing. The hotel's own official domain was not confirmed. Flagged.
  17. L7 Haeundae by LOTTE: address confirmed only by third-party listings. Flagged.
  18. Myeongdong Night Market hours: no official source. Secondary sources conflict (4–10pm, 5pm–1am, 6–10pm). Left blank, flagged.

- T3 built: root (`*.html`, `assets/`, `data/`) contains index (dashboard), itinerary (day-by-day), entries (all rows, filters), transit, hours & locations, Flagged for Review, and sources. Data lives in `data/trip.json` and `data/sources.json`. No build step.
- T4 checks run on the site (before merge):
  - `data/*.json` parse; 74 rows, 18 irregularities, 36 sources; no duplicate row IDs.
  - Every row and irregularity links to a source that appears on the Sources page; all links are https.
  - Rows marked Verified/Corrected have a verified value; rows with no value are not marked Verified/Corrected.
  - Internal links and asset references in all HTML pages resolve.
  - All seven pages were rendered in jsdom with the data loaded (no browser download was available). Counts on the dashboard match the data.
  - Browser-based visual check not possible in this sandbox (Playwright browser download blocked). Layout uses responsive CSS with a phone breakpoint; a manual check on a phone is recommended.
- T2 correction pass: 3 rows changed after first review (R05 child fare removed, R18 source changed to an official domain, R69 address moved from "verified" to note because it is not official).

## Handoff / crash notes

- None. No other session has claimed work on this repo.

## Pull request and merge

- PR: https://github.com/buffedlizard55-lab/Koreatrip1/pull/1 (`arena/b86112b5-koreatrip1` → `main`).
- Merge result: pending (recorded after merge).
- Pages source: `main` / `/` (site files at repo root). Pages source could not be changed to `/docs` (HTTP 403 for this token).
