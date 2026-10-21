# Korea, together

A dependency-free, responsive travel dashboard for two adult travelers. Published with GitHub Pages from `main` at the repository root.

- `index.html`: landing dashboard
- `itinerary.html?day=1` through `?day=9`: daily plans
- `places.html`, `transport.html`, `stays.html`: category pages
- `review.html`: all incomplete entries and major conflicts
- `sources.html`, `SOURCES.md`: official evidence and limits
- `data.js`: all 62 original plan entries, confirmed fields and findings

## Run

`python3 -m http.server 3000 --bind 0.0.0.0`

## Test

`node --test tests/site.test.cjs`

No build step, tracking, API key, external fonts, runtime requests, or booking integrations. Search/filter state is local to each page. Trip year is intentionally unresolved. All pages are relative-path compatible with project GitHub Pages. Source links open official pages; generic tourism directories are explicitly labeled as context, not evidence. Source availability may change after the research date.

## Parallel-session material retained

The earlier root site snapshot is in `prior-site/` with research-limit banners. A separate session's companion site remains at `docs/index.html`, including its proposed reordered daily plan and verification audit. These are reference research, not silently combined with this dashboard's source-scoped fields. See COORDINATION.md for all preserved session logs and source discrepancies.
