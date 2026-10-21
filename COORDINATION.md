# COORDINATION — Korea Trip Itinerary Site

Shared task board for parallel agent sessions. Read this before starting work.

## Session / branch note
- This work was done by a single Arena session on the fixed session branch
  `arena/56c45b7c-koreatrip1` (Arena requires all work stay on this branch, so
  per-task `session-<id>/<task>` branches were not used). No other session was
  active when checked on 2026-10-21 (repo contained only an initial README).

## Task board

| # | Task | Status | Owner | Files touched |
|---|------|--------|-------|---------------|
| 1 | Line-by-line verification of itinerary vs official sources | done | arena/56c45b7c session | docs/verification.html |
| 2 | GitHub Pages site (dashboard + category subpages) | done | arena/56c45b7c session | docs/*.html, docs/assets/* |
| 3 | Flagged-for-Review page (irregularities, unverified items) | done (published; items themselves = needs review by traveler) | arena/56c45b7c session | docs/flagged.html |
| 4 | Final integration: re-verify, link check, PR to main, merge, Pages deploy | in progress | arena/56c45b7c session | whole repo |

## Verification rules applied
- Every table row links to an official source (operator / government / official
  tourism body / Michelin Guide). “Official” = the venue/operator’s own site or
  Korea Tourism Organization (VISITKOREA) / Visit Seoul / Visit Busan / Seoul
  Metropolitan Government.
- If a value could not be confirmed from an official source, the cell is left
  blank (“—”) and the row is badged **UNVERIFIED** with a Naver Map search link
  for manual review. No values were inferred or converted (all money in KRW as
  published officially; original USD estimates are flagged, not repeated as fact).
- Verification date for all sources: **2026-10-21**.

## Key findings (see docs/flagged.html for full list with sources)
1. **CRITICAL:** Day 3 (Tue Nov 3, 2026) schedules Gyeongbokgung Palace on its
   weekly closing day (Tuesdays) — palace and guard ceremony do not run.
   Recommended fix: swap Day 2 and Day 3.
2. Trip year: weekday alignment only works for **2026** (Nov 1, 2026 = Sunday).
   Original “Nov 2, 2006” is a typo.
3. N Seoul Tower hours in original (“10:00–10:30”) are missing PM; combo price
   “$31” not an official price (observatory ₩29,000 + cable car ₩15,000 RT).
4. Olive Young “8:00–12:00am” not confirmed; flagship is 10:00–22:30.
5. No flight details and no post-Busan onward plan in the itinerary.
6. Days 7–8 are essentially empty.

## PR / deploy log
- (filled in at merge time)
