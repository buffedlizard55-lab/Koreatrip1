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

_(Filled in as each task completes: sources used, verification performed, irregularities found.)_

## Change Requests / Handoffs

_(Log cross-session requests and takeovers here.)_

## PR & Deploy Record

_(PR link, merge result, Pages deploy status — filled in by integration session.)_
