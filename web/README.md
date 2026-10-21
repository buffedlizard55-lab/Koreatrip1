# Field guide companion

This scoped, dependency-free static guide lives at [`/field-guide/`](../field-guide/) under the existing **main / repository-root** GitHub Pages site. It does **not** replace the independently maintained root dashboard, `docs/` companion, or their `data/` files. The legacy Pages configuration publishes tracked root files; `.github/workflows/pages.yml` **validates** this subtree but does not deploy a competing Pages artifact.

## Local preview and checks

From the repository root:

```sh
python3 scripts/check.py --build --out field-guide
python3 -m http.server 8000 --bind 0.0.0.0
# Open http://localhost:8000/field-guide/
```

`python3 scripts/build.py --out site` produces an ignored, standalone working copy at `site/` if desired. Preview with a server rather than `file://`. Source assets reside in `web/assets/`, structured guide data in `src/data/{sources,places,itinerary,review}.json`, HTML generation in `scripts/build.py`, and the verifier in `scripts/check.py`. To publish edits to source or styling, **regenerate and commit** `field-guide/` with those changes. CI regenerates this subtree, requires an identical Git diff and checks 18 pages, source-linked table rows, references and internal anchors. The footer's published research date is not a guarantee of a future opening.

## Evidence and limits

The scope ledger is [`docs/research/verification.md`](../docs/research/verification.md). Every displayed place, transit and review table row links to an official operator or public tourism source; contextual directories are clearly labeled **not proof**. Null venue facts display **— Unverified**. Generic district sources do not substantiate a particular merchant. Unresolved merchants stay on the Flagged for Review page. Data in the root dashboard and the separate `data/trip.json` transcription belongs to concurrent work; this guide does not modify either. The nine-day outline ends at L7 Haeundae following the Day 9 KTX; separately researched Busan attractions are **unassigned extensions after Day 9**. No flight, hotel, train seat or itinerary year is confirmed.
