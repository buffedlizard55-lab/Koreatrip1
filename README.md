# Korea, together

A dependency-free, responsive travel dashboard for two adult travelers. Published with GitHub Pages from `main` at the repository root.

- `index.html`: landing dashboard (16 days: Seoul week 1, Busan week 2, Hongdae return)
- `itinerary.html?day=1` through `?day=16`: daily plans
- `places.html`, `transport.html`, `stays.html`: category pages
- `review.html`: all incomplete entries and major conflicts
- `sources.html`, `SOURCES.md`: official evidence and limits
- `data.js`: original Days 1–9 entries (P001–P062) plus Week 2 Days 10–16 (P063–P097)

## Run

`python3 -m http.server 3000 --bind 0.0.0.0`

## Test

`node --test tests/site.test.cjs`

No build step, tracking, API key, external fonts, runtime requests, or booking integrations. Search/filter state is local to each page. Trip year is intentionally unresolved. All pages are relative-path compatible with project GitHub Pages. Source links open official pages; generic tourism directories are explicitly labeled as context, not evidence. Source availability may change after the research date.

## Parallel-session material retained

The earlier root site snapshot is in `prior-site/` with research-limit banners. A separate session's companion site remains at `docs/index.html`, including its proposed reordered daily plan and verification audit. These are reference research, not silently combined with this dashboard's source-scoped fields. See COORDINATION.md for all preserved session logs and source discrepancies.

## Verified guide — `verified-guide/` (parallel session `1fd4f7b3`, PR #11)

An independent, static (no-build) companion guide built by a parallel session from the same itinerary document, published at [`verified-guide/index.html`](verified-guide/index.html). It independently checked all 62 itinerary claims line by line against official sources and reached the same critical finding (Gyeongbokgung Palace closed on the scheduled Tuesday). Difference of approach: this guide **resolves the trip year to 2026** — Oct 31–Nov 9, 2026 is the only year whose weekdays match the document (deterministic calendar check) — verifies each place against those exact dates (South Korea has no November 2026 public holidays), and presents the corrected Day 2 ↔ Day 3 order as the active plan, with every deviation flagged on its own "Flagged for Review" page. Full audit trail: [`research/verification-log.md`](research/verification-log.md). It is kept separate so neither evidence set silently overwrites the other; known cross-guide discrepancies are logged in COORDINATION.md.
