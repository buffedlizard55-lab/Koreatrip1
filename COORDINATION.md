# COORDINATION.md — Shared Task Board (Korea Trip Itinerary Site)

This file coordinates parallel agent sessions working on this repo.
Rules (from project owner): claim a task here **before** starting, keep file scopes
non-overlapping, make small frequent commits, `git pull --rebase` before every push,
never mark anything verified without an official source link, and leave shared
outputs (site index/navigation, combined tables) to the final integration session.

> **Platform note:** This session (`1fd4f7b3`) is bound by the Arena sandbox to the
> branch `arena/1fd4f7b3-koreatrip1` and cannot create `session-<id>/<task>` branches.
> All other coordination rules are followed as written. Other sessions: please treat
> `arena/1fd4f7b3-koreatrip1` as this session's working branch and do not edit files
> in its claimed scope while its claims are active (< 60 min without commits = stale).

## Sessions

| Session ID | Branch | Status |
|---|---|---|
| `1fd4f7b3` | `arena/1fd4f7b3-koreatrip1` | active — started 2026-10-21 (UTC) |

## Task Board

| # | Task | Status | Owner | File scope (exclusive) |
|---|---|---|---|---|
| 1 | Research & verification of every itinerary line item against official sources (hours, prices, closures, locations, transit times) | in progress | `1fd4f7b3` | `research/verification-log.md` |
| 2 | Site scaffold + shared CSS/JS shell (mobile-first dashboard) | in progress | `1fd4f7b3` | `assets/**` |
| 3 | Landing page (trip overview dashboard) | in progress | `1fd4f7b3` | `index.html` |
| 4 | Day-by-day subpages (Day 1–9) | in progress | `1fd4f7b3` | `days/**` |
| 5 | Category subpages: Transport, Hotels, Attractions & Hours, Food & Drink, Shopping (verification tables with official source links) | in progress | `1fd4f7b3` | `categories/**` |
| 6 | "Flagged for Review" page (irregularities + unverified items, with source links) | in progress | `1fd4f7b3` | `flagged.html` |
| 7 | Final integration: line-by-line re-verification of combined data, link check, build check, PR → merge → GitHub Pages deploy confirmation | in progress | `1fd4f7b3` | (all files, integration only) |

No other sessions or branches existed when these claims were made (checked
`git branch -a` 2026-10-21: only `main` and `arena/1fd4f7b3-koreatrip1`).

## Verification & Sources Log

**Completed 2026-10-21 by session `1fd4f7b3`.** Full audit trail: `research/verification-log.md`
(62 itinerary claims checked line by line: 25 verified fully/in part, 17 irregularities
incl. 1 critical, 20 unverified and left blank).

- **Method:** each claim checked against the highest-authority official source available and
  fetched/read first-party wherever possible: Gyeongbokgung Palace Office (royalpalacekr.org),
  N Seoul Tower (nseoultower.co.kr), Namsan Cable Car + Visit Korea (KTO), Seoul Metropolitan
  Government (english.seoul.go.kr), Airport Limousine Co. (operator), Korail, Stanford Hotel &
  LOTTE Hotels official sites, Starfield/DDP/Lotte/Shinsegae/Musinsa/Blue Elephant/
  MARGESHERWOOD/Olive Young official store pages, MICHELIN Guide, Korea Heritage Service
  agency (kh.or.kr), Korea Customs Service (2026 holidays), Visit Seoul / Visit Busan /
  Visit Gangnam. Trip year (2026) established by deterministic calendar computation.
- **Critical irregularity found & fixed on the site:** itinerary scheduled Gyeongbokgung
  Palace on **Tuesday Nov 3, 2026 — its weekly closing day** (no Nov public holiday exception).
  Day 2/Day 3 swapped on the site; documented in `flagged.html` §1 for owner confirmation.
- **Other irregularities (17):** see `flagged.html` §2 (wrong Olive Young/Gwangjang/cable-car
  hours, DDP placed in Seongsu, duplicate restaurant under two names, unidentifiable
  "Uri Wang Galbitang" note, L7 check-out conflict between Lotte's own EN/KO pages,
  Crystal Jade's MICHELIN listing now returns "not found", name typos Musinsa/MARGESHERWOOD/
  Namsan/Starfield, "2006" year typo, empty Days 7–8, missing flight & post-Busan plans).
- **Unverified (20):** values with no official source (KTX time/fare = train-specific; all USD
  figures; hours/prices of Instagram-only cafés/bars) are blank everywhere and listed in
  `flagged.html` §3 with the closest official channel to check.
- **Integration checks performed:** internal link + anchor validation across all 17 HTML pages
  (all pass), HTML tag-balance check (pass), local `python -m http.server` smoke test (all 200),
  external spot-checks of official URLs not fetched during research (humetro.busan.kr alive but
  bot-blocked; visitgangnam/shinsegae/seoulmetro/airport.kr/lottehotel/onionkr all resolve).
  Two data corrections resulted: Crystal Jade MICHELIN claim downgraded (listing gone),
  Gangnam Style statue citation upgraded to the official Visit Gangnam landmark page.

## Change Requests / Handoffs

_(Log cross-session requests and takeovers here.)_

## PR & Deploy Record

_(PR link, merge result, Pages deploy status — filled in by integration session.)_
