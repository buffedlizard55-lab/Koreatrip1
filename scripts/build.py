#!/usr/bin/env python3
"""Build a dependency-free, subpath-safe static itinerary from reviewed JSON data."""
from __future__ import annotations

import argparse
import html
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "data"
ASSETS = ROOT / "web" / "assets"
SOURCES = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))["sources"]
PLACES = json.loads((DATA / "places.json").read_text(encoding="utf-8"))["places"]
ITINERARY = json.loads((DATA / "itinerary.json").read_text(encoding="utf-8"))
REVIEW = json.loads((DATA / "review.json").read_text(encoding="utf-8"))
DAYS = ITINERARY["days"]
BY_PLACE = {item["id"]: item for item in PLACES}
BY_FLAG = {item["id"]: item for item in REVIEW["items"]}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def link(href: str, label: str, klass: str = "", external: bool = False) -> str:
    attrs = ' target="_blank" rel="noopener noreferrer"' if external else ""
    css = f' class="{e(klass)}"' if klass else ""
    return f'<a href="{e(href)}"{css}{attrs}>{e(label)}</a>'


def cite(ids: list[str], role: str = "evidence") -> str:
    """Every displayed row has a visible official-source anchor, even context-only rows."""
    prefix = '<span class="context-label">Context only · not proof</span>' if role == "context_only" else ""
    anchors = "".join(link(SOURCES[s]["url"], SOURCES[s]["title"] + " ↗", "source-link", True) for s in ids)
    return f'<span class="source-list">{prefix}{anchors}</span>'


def val(value: object) -> str:
    return e(value) if value is not None and value != "" else '<span class="unverified">— <span>Unverified</span></span>'


def page(title: str, body: str, *, active: str = "", subdir: bool = False, description: str = "") -> str:
    p = "../" if subdir else ""
    nav = [
        ("index.html", "Overview", "index"), ("index.html#days", "16 days", "days"),
        ("sights.html", "Sights", "sights"), ("food.html", "Food", "food"),
        ("shopping.html", "Shopping", "shopping"), ("transport.html", "Transit", "transport"),
        ("stays.html", "Stays", "stays"), ("review.html", "Flagged for review", "review"),
    ]

    def menu_links() -> str:
        return "".join(
            f'<a href="{p}{href}"{selected}>{e(label)}</a>'
            for href, label, key in nav
            for selected in [' aria-current="page"' if key == active else '']
        )

    summary = f'{len(DAYS)} days · two adults · working 2026 dates'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#123b3d">
  <meta name="description" content="{e(description or summary)}">
  <title>{e(title)} · Seoul to Busan | The Field Guide</title>
  <link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{p}assets/site.css">
  <script src="{p}assets/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="topline"><div class="shell topline-inner"><span>THE FIELD GUIDE <span aria-hidden="true">✳</span> SOUTH KOREA</span><span>Research checked 26 Oct 2026 · Dates proposed</span></div></div>
  <header class="site-header">
    <div class="shell header-inner">
      <a class="brand" href="{p}index.html" aria-label="Seoul to Busan field guide home"><span class="brand-mark">S<span aria-hidden="true">↗</span>B</span><span class="brand-caption">SEOUL <span aria-hidden="true">/</span> BUSAN<small>THE FIELD GUIDE</small></span></a>
      <nav class="desktop-nav" aria-label="Main navigation">{menu_links()}</nav>
      <details class="mobile-menu"><summary>Explore <span aria-hidden="true">☰</span></summary><nav aria-label="Mobile navigation">{menu_links()}</nav></details>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer"><div class="shell footer-inner">
    <div><span class="footer-brand">SEOUL <span aria-hidden="true">↗</span> BUSAN.</span><p>A useful plan, not a promise of booked travel. Working dates, routes and hours may change.</p></div>
    <div class="footer-links"><a href="{p}index.html#days">The 16 days</a><a href="{p}transport.html">Getting around</a><a href="{p}review.html">Flagged for review</a><a href="{p}sources.html">All official sources</a></div>
    <div class="footer-meta">Prepared for two adults<br>Checked 26 October 2026<br>Original year unconfirmed<br><span>Built as a static, accessible field guide.</span></div>
  </div><div class="shell footer-bottom"><span>Published with uncertainties visible, never hidden.</span><span>Seoul → Busan → Seoul (Hongdae) · 16-day outline</span></div></footer>
</body>
</html>'''


def section_head(index: str, eyebrow: str, title: str, aside: str = "") -> str:
    return f'<div class="section-heading"><div><span class="eyebrow dark">{e(index)} / {e(eyebrow)}</span><h2>{e(title)}</h2></div>{f"<p>{e(aside)}</p>" if aside else ""}</div>'


def compact_flags(ids: list[str], p: str = "") -> str:
    return "".join(
        f'<li><a href="{p}review.html#{e(key)}"><span class="flag-dot" aria-hidden="true"></span><span><b>{e(BY_FLAG[key]["title"])}</b><small>{e(BY_FLAG[key]["topic"])}</small></span><span aria-hidden="true">↗</span></a></li>'
        for key in ids
    )


def intro_banner(eyebrow: str, title: str, description: str, detail: str = "") -> str:
    return f'''<section class="page-intro"><div class="shell page-intro-inner">
        <div><span class="eyebrow">{e(eyebrow)}</span><h1>{e(title)}</h1><p>{e(description)}</p></div>
        <div class="intro-stamp"><span>THE FIELD GUIDE</span><strong>{e(detail or "01 / 16")}</strong><small>SEOUL ↗ BUSAN</small></div>
    </div></section>'''


def place_rows(rows: list[dict], *, p: str = "", day_stops: list[dict] | None = None) -> str:
    result = []
    is_day = day_stops is not None
    for i, place in enumerate(rows):
        stop = day_stops[i] if is_day else None
        category_url = f'{p}{place["category"]}.html#place-{place["id"]}'
        name = f'<a class="place-name" href="{e(category_url)}">{e(place["name"])} <span aria-hidden="true">↗</span></a>'
        region = f'<span class="place-region">{e(place["city"])} · {e(place["area"])}</span>'
        if place.get("extension"):
            region += '<span class="extension-tag">Editorial option · blank Busan day</span>'
        location = f'<span class="address">{val(place["address"])}</span><span class="access">{val(place["access"])}</span>'
        hours = f'<span class="hour-value">{val(place["hours"])}</span><span class="day-value">{val(place["days"])}</span>'
        start = f'<tr id="place-{e(place["id"])}" data-city="{e(place["city"].lower())}">'
        if stop:
            period = (f'<td data-label="Suggested period"><span class="period">{e(stop["period"])}</span>'
                      + ('<span class="optional-tag">Optional</span>' if stop.get("optional") else "") + '</td>')
            result.append(f'''{start}{period}<th scope="row" data-label="Place &amp; location">{name}{region}<span class="place-note">{e(stop['why'])}</span>
              <span class="mini-location">{location}</span><span class="mini-price">Price · {val(place['price'])}</span></th>
              <td data-label="Published hours / days">{hours}</td><td data-label="Official sources">{cite(place['sources'])}</td></tr>''')
        else:
            result.append(f'''{start}<th scope="row" data-label="Place">{name}{region}<span class="place-note">{e(place['note'])}</span></th>
              <td data-label="Published hours / days">{hours}</td><td data-label="Location & public transit">{location}</td>
              <td data-label="Price">{val(place['price'])}</td><td data-label="Official sources">{cite(place['sources'])}</td></tr>''')
    headers = ('<th scope="col">Suggested period</th><th scope="col">Place &amp; location</th><th scope="col">Published hours / days</th><th scope="col">Official sources</th>' if is_day
               else '<th scope="col">Place &amp; why</th><th scope="col">Published hours / days</th><th scope="col">Location &amp; public transit</th><th scope="col">Price</th><th scope="col">Official sources</th>')
    extra = ' day-table' if is_day else ''
    return f'''<div class="table-wrap"><table class="data-table place-table{extra}"><caption class="sr-only">{e("Day stops" if is_day else "Places and official sources")}</caption>
      <thead><tr>{headers}</tr></thead><tbody>{''.join(result)}</tbody></table></div>'''


def overview() -> str:
    cards = []
    for d in DAYS:
        date_obj = date.fromisoformat(d["date"])
        peek = " · ".join(BY_PLACE[stop["place"]]["name"] for stop in d["stops"][:2])
        cards.append(f'''<a class="day-card" href="days/{d['number']:02}.html">
            <div class="day-card-top"><span class="day-number">{d['number']:02}</span><span class="day-city">{e(d['city'])}</span></div>
            <div><time datetime="{e(d['date'])}">{e(date_obj.strftime('%a · %d %b'))} <span>2026?</span></time><h3>{e(d['title'])}</h3><p>{e(d['subtitle'])}</p></div>
            <div class="day-card-bottom"><span>{e(peek)}</span><span class="round-arrow" aria-hidden="true">↗</span></div></a>''')
    group = [("01", "Sights", "Palaces, design, coastal trails, skywalks and observatories.", "sights.html", "Explore places"),
             ("02", "Food", "Named eateries and markets in Seoul and Busan with honest opening notes.", "food.html", "Find a meal"),
             ("03", "Shopping", "From Myeongdong and Seongsu to Busan's Gukje and Nampo-dong.", "shopping.html", "Browse stores"),
             ("04", "Transit", "Step-by-step metro, KTX and AREX All-Stop routes from each hotel door.", "transport.html", "Plan the ride"),
             ("05", "Stays", "Three hotel bases across Myeongdong, Haeundae and Hongdae; unbooked.", "stays.html", "See the bases"),
             ("06", "Review", "Unverified details, discrepancies and next checks across all 16 days.", "review.html", "Read the flags")]
    categories = "".join(f'<a class="category-card" href="{href}"><span class="category-n">{num} / FIELD NOTES</span><h3>{title} <span aria-hidden="true">↗</span></h3><p>{desc}</p><span class="category-action">{cta}</span></a>' for num, title, desc, href, cta in group)
    costs = [("Palace admission", 3000, ["palace_hours"]), ("Namsan cable car · return", 15000, ["cablecar"]),
             ("N Seoul Tower observatory", 29000, ["n_tower_fee"]), ("AREX Express · one way (ICN–Seoul Stn)", 13000, ["arex"]),
             ("Songdo Marine Cable Car · Air Cruise RT", 17000, ["songdo_cablecar"])]
    cost_rows = "".join(f'<tr><th scope="row">{e(label)}</th><td data-label="Per adult">₩{unit:,}</td><td data-label="For two">₩{unit * 2:,}</td><td data-label="Official source">{cite(ids)}</td></tr>' for label, unit, ids in costs)
    total = sum(unit for _, unit, _ in costs)
    all_sources = [s for _, _, ids in costs for s in ids]
    body = f'''
    <section class="home-hero"><div class="shell hero-grid"><div class="hero-copy"><span class="eyebrow light">A SIXTEEN-DAY FIELD GUIDE · 2 ADULTS</span>
      <h1>Two cities.<br><em>Two full weeks.</em></h1><p>A considered 16-day journey through Seoul and Busan, returning to Hongdae on Day 16. Built for public transit, checked against official sources, and clear about what still needs confirming.</p>
      <div class="hero-actions"><a class="button button-light" href="#days">Explore the 16 days <span aria-hidden="true">↘</span></a><a class="text-link" href="review.html">What is not confirmed? ↗</a></div>
      <div class="hero-caption"><span>01 — 16 NOV <b>2026?</b></span><span>SEOUL ↗ BUSAN ↗ HONGDAE / DAYS 01–16</span></div></div>
      <div class="hero-art"><img src="assets/route-art.svg" alt="Decorative palace-roof and coastal-bridge illustration joined by a dotted line; not a geographical map" width="640" height="640"><span class="art-caption">A tale of two chapters <span>↗</span></span></div>
    </div></section>
    <div class="shell hero-metrics" aria-label="Trip at a glance"><div><span>01 / THE TIMEFRAME</span><strong>16 days</strong><small>1–16 November · working 2026 calendar</small></div><div><span>02 / THE TRAVELERS</span><strong>2 adults</strong><small>Independent travel · public transit first</small></div><div><span>03 / THE CERTAINTY</span><strong>Proposed</strong><small>Hotels, trains and flights not booked here</small></div></div>
    <section class="shell notice-panel" aria-labelledby="notice-title"><span class="notice-mark" aria-hidden="true">!</span><div><p class="eyebrow dark">BEFORE YOU GO</p><h2 id="notice-title">The calendar is a working hypothesis.</h2><p>The surviving year labels conflict, and no flights, rail seats or hotel bookings are confirmed. Week 1 covers Seoul (Days 1–8) and the Day 9 KTX to Busan; Week 2 covers Busan (Days 10–15) and the Day 16 KTX + AREX All-Stop return to Seoul Hongdae. Days 7, 8, 13 and 15 have no submitted activities, and Monday/Tuesday palace scheduling is a clearly marked correction. Unsupported values are left blank and labeled <b>Unverified</b>.</p></div><a href="review.html" class="notice-link">Read every flag <span aria-hidden="true">↗</span></a></section>
    <section id="days" class="shell section-block">{section_head('01', 'THE ROUTE', '16 days, in order', 'Start at the hotel, keep the detours optional, and follow the verified rail and metro links between Seoul, Busan and Hongdae. Every date below is proposed.')}
        <div class="day-grid">{''.join(cards)}</div></section>
    <section class="analysis-band"><div class="shell section-block">{section_head('02', 'THE THINKING', 'Why this route works', 'Grouped neighborhoods; visible constraints. All plans assume normal service and an unconfirmed year.')}
      <div class="analysis-grid"><article><span class="analysis-index">01 / THE CLOCK</span><h3>Opening hours lead.</h3><p>The palace is on Monday, not its ordinary Tuesday closure; Bukchon follows within its restricted visitor window; Nurimaru is visited before 17:00 on Day 10. <a href="review.html#palace_tuesday">Check the palace note ↗</a></p>{cite(['palace_hours','bukchon','nurimaru'])}</article>
      <article><span class="analysis-index">02 / THE MAP</span><h3>One neighborhood at a time.</h3><p>DDP is in Dongdaemun, not Seongsu. In Busan, Haeundae/Cheongsapo (Day 10), Gamcheon/Songdo/Nampo (Day 11), and Gwangalli (Day 14) are grouped by coast, and Day 16 uses AREX All-Stop to reach Hongdae. <a href="transport.html">See the transit guide ↗</a></p>{cite(['ddp_access','busan_metro','arex_allstop'])}</article>
      <article><span class="analysis-index">03 / THE UNKNOWN</span><h3>Room for real life.</h3><p>Days 7, 8, 13 and 15 have no submitted activities. Conflicting or unverified ticket fares (Blueline Park, BUSAN X the SKY, SEA LIFE Busan) are left blank rather than guessed. <a href="review.html">Review the open items ↗</a></p>{cite(['korail','blueline_booking','xthesky_kto'])}</article></div>
    </div></section>
    <section class="shell section-block">{section_head('03', 'THE NUMBERS', 'A small, sourced price check', 'Illustrative fixed-item costs only. Optional visits, not a trip estimate or proof of purchase.')}
      <div class="two-column"><div class="table-wrap"><table class="data-table budget-table"><caption class="sr-only">Published prices for selected optional activities and one airport train ride</caption><thead><tr><th scope="col">Selected item</th><th scope="col">Per adult</th><th scope="col">For two</th><th scope="col">Official source</th></tr></thead><tbody>{cost_rows}</tbody><tfoot><tr><th scope="row">Illustrative subtotal</th><td data-label="Per adult">₩{total:,}</td><td data-label="For two">₩{total*2:,}</td><td data-label="Official sources">{cite(all_sources)}</td></tr></tfoot></table></div>
      <aside class="budget-note"><span class="eyebrow dark">WHAT IT DOESN'T INCLUDE</span><h3>Not a budget for the trip.</h3><p>No KTX seat, flight, hotel room, food or local metro/taxi fare has a verified cost here. BUSAN X the SKY (₩29,000 vs ₩27,000), Blueline Park Sky Capsule (₩50,000 vs ₩40,000 for two), and SEA LIFE Busan ('$15' unverified) have conflicting or unconfirmed adult rates and stay blank.</p><a href="review.html#xthesky_conflict">See the fare discrepancies ↗</a></aside></div></section>
    <section class="shell section-block categories-section">{section_head('04', 'THE INDEX', 'Find what you need', 'Official links appear with each place and route. A context-only link never verifies a merchant.')}
       <div class="category-grid">{categories}</div></section>
    <section class="shell end-callout"><span class="eyebrow light">KEEP THE UNCERTAINTY VISIBLE</span><h2>Better a blank field<br>than a bad direction.</h2><p>Every unverified stop and conflicting official detail has a place on the review board. It is published for later checking—not hidden in fine print.</p><a href="review.html" class="button button-light">Open flagged for review <span aria-hidden="true">↗</span></a></section>'''
    return page("The 16-day itinerary", body, active="index", description="A source-checked, mobile-friendly proposed 16-day Seoul and Busan trip for two, with hotel-based transit and a full review register.")


CATEGORY = {
    "sights": ("The sights", "Historic gates, modern design, coastal trails, skywalks and observatories.", "Week 1 covers Seoul (Days 1–8) and Week 2 covers Busan (Days 9–15) before the Day 16 return to Hongdae. Haedong Yonggungsa is marked as an editorial option for the blank Day 13 Friday. Published hours are not a date-specific guarantee."),
    "food": ("Food & markets", "Good stops, honest opening notes across Seoul and Busan.", "This is a sourced shortlist, not a reservation ledger. Afternoon break conflicts (such as Haeundae Amso Galbi) and Tuesday closure conflicts (Jagalchi Market) are flagged rather than hidden."),
    "shopping": ("Shopping notes", "A little city wandering, well located in Seoul and Busan.", "Current operator branches, department-store calendars and traditional market hours are used where available. Check branch holidays near travel; Lotte Main lists Mon 9 Nov 2026 closed and Gukje Market lists Sundays closed."),
}


def category_page(category: str) -> str:
    title, tagline, note = CATEGORY[category]
    rows = [item for item in PLACES if item["category"] == category]
    seoul_count = sum(item["city"] == "Seoul" for item in rows)
    busan_count = len(rows) - seoul_count
    body = intro_banner("FIELD NOTES / " + category.upper(), title, tagline, f"{len(rows):02} PLACES")
    body += f'''<section class="shell section-block catalog-section"><div class="catalog-head"><div><span class="eyebrow dark">THE SOURCE-LINKED SHORTLIST</span><h2>Look up a place</h2><p>{e(note)}</p></div><a href="review.html#unverified-merchants" class="small-link">Unverified shortlist ↗</a></div>
       <div class="filter-bar" role="group" aria-label="Filter by city" data-filter-group><button type="button" data-filter="all" aria-pressed="true">All <span>{len(rows):02}</span></button><button type="button" data-filter="seoul" aria-pressed="false">Seoul <span>{seoul_count:02}</span></button><button type="button" data-filter="busan" aria-pressed="false">Busan <span>{busan_count:02}</span></button><span class="filter-count" aria-live="polite">Showing all {len(rows)} places</span></div>
       {place_rows(rows)}<p class="under-table">A blank labeled <strong>Unverified</strong> means this field was not supported by the linked official material. Planning a visit is not a booking.</p></section>
       <section class="shell cross-link"><div><span class="eyebrow dark">NEXT IN THE GUIDE</span><h2>Go from a list to a day.</h2><p>The 16-day view puts these places into an optional, hotel-based route.</p></div><a class="button button-dark" href="index.html#days">Explore the days <span aria-hidden="true">↗</span></a></section>'''
    return page(title, body, active=category, description=tagline + " Official source links and unverified fields included.")


def day_page(d: dict) -> str:
    number = d["number"]
    dt = date.fromisoformat(d["date"])
    p = "../"
    stops = [BY_PLACE[s["place"]] for s in d["stops"]]
    hotel = BY_PLACE[d["hotel"]]
    destination = BY_PLACE[d["end_hotel"]] if d.get("end_hotel") else None
    destination_card = (f'<div class="destination-card"><span class="eyebrow dark">ARRIVAL BASE · NOT BOOKED</span><strong>{e(destination["name"])}</strong><span>{e(destination["address"])}</span>{cite(destination["sources"])}</div>' if destination else "")
    prev_link = link(f'{number-1:02}.html', f'← Day {number-1:02}', "day-prev") if number > 1 else link('../index.html#days', '← All days', 'day-prev')
    next_link = link(f'{number+1:02}.html', f'Day {number+1:02} →', "day-next") if number < len(DAYS) else link('../index.html#days', 'All days →', 'day-next')
    transit = lambda label, data: f'''<div class="journey-step"><div class="journey-icon" aria-hidden="true">{e(label[:1])}</div><div><span class="eyebrow dark">{e(label)}</span><p>{e(data['text'])}</p>{cite(data['sources'])}</div></div>'''
    overview = f'''<div class="day-header shell"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../index.html">Overview</a><span aria-hidden="true">/</span><a href="../index.html#days">16 days</a><span aria-hidden="true">/</span><span>Day {number:02}</span></nav>
       <div class="day-title-row"><div><span class="eyebrow dark">DAY {number:02} / {e(d['city'].upper())} / PROPOSED DATE</span><h1>{e(d['title'])}</h1><p>{e(d['subtitle'])}</p></div><div class="date-seal"><span>{e(dt.strftime('%A'))}</span><strong>{e(dt.strftime('%d'))}</strong><small>{e(dt.strftime('%b'))} 2026?</small></div></div>
       <div class="day-pager">{prev_link}<span>{number:02} <span aria-hidden="true">/</span> {len(DAYS):02}</span>{next_link}</div></div>'''
    flags = compact_flags(d["flags"], p)
    body = f'''<div class="day-page">{overview}<div class="shell day-layout"><div class="day-main">
      <div class="inline-alert"><span aria-hidden="true">!</span><p><strong>Route proposal, not a booked day.</strong> The year is unconfirmed. Periods such as “morning” are suggested visit slots, not venue hours. <a href="../review.html#dates">Why the dates are flagged ↗</a></p></div>
      <section class="day-section" aria-labelledby="origin"><div class="step-header"><span>01</span><div><span class="eyebrow dark">START HERE</span><h2 id="origin">From the hotel door</h2></div></div>
        <div class="origin-card"><div><span class="eyebrow dark">SUGGESTED BASE · {e(hotel['city'].upper())}</span><h3>{e(hotel['name'])}</h3><p>{e(hotel['address'])}</p><small>No stay or room confirmed.</small></div>{cite(hotel['sources'])}</div>
        <div class="journey-list">{transit('Outbound route', d['depart'])}</div></section>
      <section class="day-section" aria-labelledby="places"><div class="step-header"><span>02</span><div><span class="eyebrow dark">THE DAY OUT</span><h2 id="places">Stops, in sequence</h2></div></div>
         <p class="section-explain">Optional rows are easy to remove if travel takes longer than expected. Published hours and suggested periods are different things.</p>
         {place_rows(stops, p=p, day_stops=d['stops'])}</section>
      <section class="day-section" aria-labelledby="homebound"><div class="step-header"><span>03</span><div><span class="eyebrow dark">WRAP UP</span><h2 id="homebound">Finish the day</h2></div></div><div class="journey-list">{transit('Onward / arrival', d['return'])}</div>{destination_card}</section>
      <div class="field-note"><span class="eyebrow dark">FIELD NOTE / DAY {number:02}</span><p>{e(d['note'])}</p></div>
      <div class="day-bottom-nav">{prev_link}{next_link}</div>
    </div><aside class="day-aside" aria-label="Day at a glance"><div class="aside-inner"><div class="aside-card"><span class="eyebrow dark">AT A GLANCE</span><h2>{e(d['city'])}, on your terms.</h2><div class="aside-stat"><span>Start at</span><strong>{e(hotel['name'])}</strong></div><div class="aside-stat"><span>Night after this day</span><strong>{e(d['overnight'])}</strong></div><div class="aside-stat"><span>Stops listed</span><strong>{len(stops)} <small>including {sum(s.get('optional', False) for s in d['stops'])} optional</small></strong></div><a href="../transport.html">How to ride the route ↗</a></div>
       <div class="aside-card flag-card"><span class="eyebrow dark">CHECK BEFORE TRAVEL</span><h2>Watch points.</h2><ul class="flag-list">{flags}</ul><a class="flag-more" href="../review.html">All review items ↗</a></div>
       <div class="aside-tip"><span aria-hidden="true">✳</span><p><strong>Keep it flexible.</strong> Suggested visit periods are not venue hours; specific train seats, weather and hotel reservations are not established here.</p></div></div></aside></div></div>'''
    return page(f'Day {number:02} — {d["title"]}', body, active="days", subdir=True, description=f'Proposed day {number} in {d["city"]}: hotel-based public transit, sourced opening information and review flags.')


def transport_page() -> str:
    routes = [
        ("Arrival / conditional", "ICN → Stanford Myeongdong", "The submitted notes name SFO→ICN but no flight is booked here. Hotel FAQ suggests airport limousine 6015 / Ibis Myeongdong stop, then walk to its 9F lobby; confirm terminal and live service.", None, None, ["stanford"]),
        ("Airport rail", "ICN → Seoul Station", "AREX Express; 43 min onboard from Terminal 1, 51 min from Terminal 2. Transfer to local metro or other transport to the hotel.", "43 / 51 min onboard", "₩13,000 / adult, one way", ["arex"]),
        ("Day 2 / palace", "Stanford → Gyeongbokgung", "Euljiro 1-ga Line 2 → Euljiro 3-ga → Line 3 Gyeongbokgung Exit 5; walk to 161 Sajik-ro.", None, None, ["seoul_metro","palace_location"]),
        ("Day 3 / Namsan", "Stanford → Namsan Cable Car", "Walk toward Line 4 Myeongdong Station; the operator gives an Exit 3 walking route or Exit 4 via Namsan Ormi. Cable car is weather-dependent.", None, None, ["stanford","cablecar"]),
        ("Seoul / markets", "Stanford → Gwangjang", "Euljiro 1-ga Line 2 → Euljiro 4-ga; walk to 88 Changgyeonggung-ro. Sunday retail and food-street rules differ.", None, None, ["seoul_metro","gwangjang"]),
        ("Day 4 / Seongsu", "Stanford → Seongsu → DDP", "Euljiro 1-ga Line 2 → Seongsu. If continuing to DDP, ride Line 2 separately to Dongdaemun History & Culture Park Exit 1; it is not in Seongsu.", None, None, ["seoul_metro","marge","ddp_access"]),
        ("Day 5 / Gangnam", "Stanford → COEX", "Euljiro 1-ga Line 2 → Samseong Exit 5/6, then walk into Starfield COEX Mall. Original 47-minute estimate unverified.", None, None, ["seoul_metro","coex"]),
        ("Day 6 / Jongno", "Stanford → Anguk / Ikseon", "Euljiro 1-ga Line 2 → Euljiro 3-ga; change to Line 3 for Anguk. Walk Insa-dong toward Ikseon or use Jongno 3-ga.", None, None, ["seoul_metro","insadong","ikseon"]),
        ("Day 7 / optional", "Stanford → Itaewon", "Line 2 Euljiro 1-ga → Line 3 Euljiro 3-ga → Line 6 Yaksu → Itaewon Exit 3. Day 7 has no submitted activity beyond the district name.", None, None, ["seoul_metro","itaewon_area"]),
        ("Day 8 / optional", "Stanford → Mangwon", "Line 2 Euljiro 1-ga → Hapjeong; change to Line 6 for Mangwon Exit 2. An alternative is Gwangjang food street via Euljiro 4-ga; neither was submitted as Day 8.", None, None, ["seoul_metro","mangwon","gwangjang"]),
        ("Day 9 / southbound", "Stanford → Seoul Station → Busan", "From Euljiro 1-ga Line 2, change at City Hall to Line 1 for Seoul Station; board a separately booked KORAIL train to Busan Station. No train time or ticket verified.", None, None, ["stanford","seoul_metro","korail","visitkorea_rail"]),
        ("Day 9 / Haeundae", "Busan Station → L7 Haeundae", "Metro Line 1 from Busan Station → Seomyeon; change to Line 2 → Haeundae, then walk to 55 Haeun-daero 570beon-gil.", None, None, ["busan_metro","l7"]),
        ("Day 10 / Dongbaek & Mipo", "L7 Haeundae → Dongbaekseom → Mipo → Cheongsapo", "Walk west along Haeundae Beach to Dongbaekseom Island & Nurimaru (or Line 2 Dongbaek Exit 1, 14–20 min walk), then head to Mipo Station for the one-way Sky Capsule to Cheongsapo (~30 min, 2 km). Return via a separately booked one-way capsule or the Beach Train.", "~30 min capsule one way", None, ["l7","dongbaek_trail","nurimaru","blueline_course","blueline_booking"]),
        ("Day 11 / Gamcheon", "L7 Haeundae → Gamcheon Culture Village", "Metro Line 2 Haeundae → Seomyeon; transfer to Line 1 → Toseong Exit 6; take village bus Saha 1-1, Seo-gu 2 or 2-2. The brief's '2 buses, 1 hr & 17 min' is unverified.", None, None, ["l7","busan_metro","gamcheon"]),
        ("Day 11 / Songdo & Nampo", "Jagalchi / BIFF Square ↔ Songdo Beach", "From Line 1 Jagalchi Station Exit 2 take city bus 7, 26, 30, 71 or 96 to Songdo Beach (Cloud Trails & Cable Car), then return to Jagalchi / Nampo for Gukje Market and Gwangbok-ro. The brief's '13 min bus, 9 min walk' is unverified.", None, None, ["busan_metro","songdo_beach","songdo_cablecar","gukje","nampo_shopping"]),
        ("Day 12 / Haeundae coast", "L7 Haeundae → BUSAN X the SKY & SEA LIFE", "Walk along Haeundae Beach to 30 Dalmaji-gil (LCT Landmark Tower) and 266 Haeundaehaebyeon-ro (SEA LIFE Busan Aquarium, 10-min walk from Line 2 Haeundae Exit 3/5).", None, None, ["l7","xthesky_kto","sealife_busan"]),
        ("Day 13 / optional", "L7 Haeundae → Haedong Yonggungsa", "Editorial option for blank Friday: Haeundae Station Exit 7 → city bus 181, 100 or Haeundae 9 to Yonggungsa; check live departures.", None, None, ["temple","l7"]),
        ("Day 14 / Gwangalli", "L7 Haeundae → Gwangalli Beach (Drone Show)", "Metro Line 2 from Haeundae → Gwangan Station Exit 5, then walk ~13 minutes to Gwangalli Beach for the 19:00 Saturday winter show.", None, None, ["l7","busan_metro","gwangalli","drone"]),
        ("Day 15 / optional", "L7 Haeundae → Bupyeong Kkangtong Night Market", "Editorial option for blank Sunday: Line 2 Haeundae → Seomyeon → Line 1 Jagalchi Exit 3. Note Gukje Market retail is closed Sundays.", None, None, ["l7","busan_metro","bupyeong","gukje"]),
        ("Day 16 / northbound", "L7 Haeundae → Busan Station → Seoul Station", "Check out of L7 by 11:00. Metro Line 2 Haeundae → Seomyeon → Line 1 Busan Station (the brief's '1 hr, $20–$30' Uber is unverified), then board a separately booked KTX train to Seoul Station.", None, None, ["l7","busan_metro","korail"]),
        ("Day 16 / Hongdae", "Seoul Station → Hongik Univ. → Mercure Hongdae", "Board the AREX All-Stop Train (일반열차) at Seoul Station to Hongik Univ. Station Exit 9 (AREX Express is non-stop to ICN and skips Hongdae). Accor lists a 2-min (100 m) walk to 144 Yanghwa-ro vs 8 min in the brief.", None, None, ["arex_allstop","arex","mercure_hongdae"]),
    ]
    tr = "".join(f'<tr><th scope="row" data-label="Leg"><span class="period">{e(kind)}</span><strong class="route-label">{e(name)}</strong></th><td data-label="Route">{e(how)}</td><td data-label="Published time">{val(duration)}</td><td data-label="Published fare">{val(fare)}</td><td data-label="Official source">{cite(ids)}</td></tr>' for kind, name, how, duration, fare, ids in routes)
    body = intro_banner("FIELD NOTES / TRANSIT", "Transit without guesswork.", "Hotel-based metro steps and intercity connections across all 16 days, with every missing fare or duration shown as unverified.", "3 BASES")
    body += f'''<section class="shell section-block"><div class="transit-story"><div><span class="eyebrow dark">THE THROUGH LINE</span><h2>Door to door, in chapters.</h2><p>Line numbers and interchanges below follow official rail maps. They are wayfinding plans—not real-time journey estimates. Buy rail tickets on the operator's site after dates are confirmed.</p></div><div class="station-line" aria-label="Proposed route: Incheon arrival, Myeongdong base, Seoul Station, Busan Haeundae base, Seoul Station, Hongdae arrival"><span>ICN?</span><span>Myeongdong</span><span>Seoul Station</span><span>Busan / Haeundae</span><span>Hongdae ↗</span></div></div>
      {section_head('01', 'THE CONNECTIONS', 'Public transit cheat sheet', 'For two independent travelers across Seoul, Busan and Hongdae. Route descriptions are map-based; exact headways, traffic and ticket availability are not guaranteed.')}
      <div class="table-wrap"><table class="data-table transit-table"><caption class="sr-only">Hotel-based public transit and official sources</caption><thead><tr><th scope="col">Leg</th><th scope="col">Route from base</th><th scope="col">Published time</th><th scope="col">Published fare</th><th scope="col">Official source</th></tr></thead><tbody>{tr}</tbody></table></div><p class="under-table">AREX Express time is <strong>onboard only</strong>, and AREX Express does <strong>not</strong> stop at Hongik Univ. Station (use the AREX All-Stop Train on Day 16). City buses, Uber estimates and KTX seats require fresh checks.</p></section>
      <section class="shell section-block"><div class="split-callouts"><article><span class="eyebrow dark">KTX &amp; AREX / RAIL CHECKS</span><h2>Know which train stops where.</h2><p>KORAIL says KTX tickets open at 07:00 two months before travel (VisitKorea says usually one month). On Day 16, board the AREX All-Stop Train at Seoul Station for Hongik Univ. Station—the AREX Express runs non-stop to Incheon Airport.</p>{cite(['korail','arex_allstop','arex'])}<a href="review.html#arex_hongdae">Read the AREX Hongdae flag ↗</a></article>
      <article><span class="eyebrow dark">ARRIVAL &amp; DEPARTURE / BUFFER</span><h2>Don't confuse a ride with a flight.</h2><p>The notes suggest SFO→ICN on Day 1 and end at Mercure Ambassador Seoul Hongdae on Day 16, but no actual inbound or outbound flight, terminal or booking is confirmed.</p>{cite(['arex','stanford','mercure_hongdae'])}<a href="review.html#flights">Read the flight flag ↗</a></article></div></section>'''
    return page("Getting around", body, active="transport", description="Hotel-based Seoul, Busan and Hongdae public transit guide with sourced routes, fares and unverified connection details.")


def stays_page() -> str:
    hotels = [x for x in PLACES if x["category"] == "stays"]
    rows = "".join(f'''<tr id="place-{e(h['id'])}"><th scope="row" data-label="Suggested base"><strong class="place-name">{e(h['name'])}</strong><span class="place-region">{e(h['city'])} · {e(h['area'])}</span><span class="place-note">{e(h['note'])}</span></th>
      <td data-label="Check-in / out">{val(h['hours'])}</td><td data-label="Address & access"><span class="address">{val(h['address'])}</span><span class="access">{val(h['access'])}</span></td><td data-label="Reservation"><span class="unverified">— <span>Unverified</span></span></td><td data-label="Official source">{cite(h['sources'])}</td></tr>''' for h in hotels)
    body = intro_banner("FIELD NOTES / STAYS", "Three suggested bases.", "Hotel contact details and checkout rules are sourced across Myeongdong, Haeundae and Hongdae; room dates and reservations are not.", "03 BASES")
    body += f'''<section class="shell section-block">{section_head('01', 'THE HOTELS', 'Use them as anchors', 'Every transit direction in this 16-day guide starts or ends at one of the three suggested bases. None of the hotel stays has been confirmed for these travelers.')}
      <div class="table-wrap"><table class="data-table"><caption class="sr-only">Suggested hotel bases, check-in rules and official sources</caption><thead><tr><th scope="col">Suggested base</th><th scope="col">Published check-in / out</th><th scope="col">Address &amp; transit</th><th scope="col">Reservation</th><th scope="col">Official source</th></tr></thead><tbody>{rows}</tbody></table></div>
      <div class="split-callouts stay-callouts"><article><span class="eyebrow dark">SEOUL MYEONGDONG / DAYS 1–9</span><h2>Stanford checkout by 12:00.</h2><p>Stanford's FAQ lists check-in from 15:00, check-out by 12:00, and same-day luggage holding until midnight after checkout. Neither policy establishes the travelers' actual reservation or KTX departure time.</p>{cite(['stanford'])}<a href="review.html#hotels">Check the hotel flag ↗</a></article>
      <article><span class="eyebrow dark">BUSAN HAEUNDAE &amp; SEOUL HONGDAE / DAYS 9–16</span><h2>L7 checkout by 11:00; Mercure Exit 9 walk.</h2><p>L7 Haeundae lists check-in from 15:00 and check-out by 11:00 (matching the Day 16 note). On Day 16, Accor lists Mercure Ambassador Seoul Hongdae at 144 Yanghwa-ro, a 2-minute (100 m) walk from Hongik Univ. Station Exit 9 (check-in 15:00, check-out 12:00).</p>{cite(['l7','mercure_hongdae'])}<a href="review.html#mercure_walk">Check the Hongdae walk flag ↗</a></article></div></section>'''
    return page("Where to stay", body, active="stays", description="Suggested Seoul Myeongdong, Busan Haeundae and Seoul Hongdae hotel bases with official policies; reservations and dates remain unverified.")


def review_table(items: list[dict], merchant: bool = False) -> str:
    rows = []
    for x in items:
        marker = {"priority": "Needs confirmation", "correction": "Route corrected", "discrepancy": "Source discrepancy", "merchant": "Unverified venue"}[x["tier"]]
        if merchant:
            rows.append(f'''<tr id="{e(x['id'])}"><th scope="row" data-label="Candidate"><span class="review-tag">{e(marker)}</span><strong class="review-title">{e(x['title'])}</strong><span class="place-region">{e(x['topic'])}</span></th>
              <td data-label="Address">{val(None)}</td><td data-label="Hours">{val(None)}</td><td data-label="Price">{val(None)}</td><td data-label="Status / next check">{e(x['finding'])} <span class="review-action">{e(x['action'])}</span></td><td data-label="Official research starting point">{cite(x['sources'], x['source_role'])}</td></tr>''')
        else:
            rows.append(f'''<tr id="{e(x['id'])}"><th scope="row" data-label="Issue"><span class="review-tag">{e(marker)} · {e(x['topic'])}</span><strong class="review-title">{e(x['title'])}</strong></th>
              <td data-label="Finding">{e(x['finding'])}</td><td data-label="Next check">{e(x['action'])}</td><td data-label="Official evidence or context">{cite(x['sources'], x['source_role'])}</td></tr>''')
    columns = '<th scope="col">Candidate</th><th scope="col">Address</th><th scope="col">Hours</th><th scope="col">Price</th><th scope="col">Status / next check</th><th scope="col">Official research starting point</th>' if merchant else '<th scope="col">Issue</th><th scope="col">Finding</th><th scope="col">Next check</th><th scope="col">Official evidence or context</th>'
    return f'<div class="table-wrap"><table class="data-table review-table{" merchant-table" if merchant else ""}"><caption class="sr-only">{e("Unverified venues" if merchant else "Findings and review actions")}</caption><thead><tr>{columns}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def review_page() -> str:
    items = REVIEW["items"]
    core = [x for x in items if x["tier"] != "merchant"]
    merchants = [x for x in items if x["tier"] == "merchant"]
    priorities = [x for x in core if x["tier"] == "priority"]
    body = intro_banner("THE AUDIT / OPEN ITEMS", "Flagged for review.", "Everything that could change the 16-day plan, plus every candidate business we could not safely verify. Publication is not contingent on resolving these items.", f"{len(items):02} FLAGS")
    body += f'''<div class="shell review-metrics"><div><strong>{len(priorities):02}</strong><span>planning checks</span></div><div><strong>{len(core)-len(priorities):02}</strong><span>corrections &amp; discrepancies</span></div><div><strong>{len(merchants):02}</strong><span>unverified candidates</span></div></div>
      <section class="shell section-block review-section"><div class="review-intro"><span class="eyebrow dark">HOW TO READ THIS PAGE</span><h2>Evidence is not the same as context.</h2><p>{e(REVIEW['intro'])}</p><div class="key-line"><span class="review-tag">Route corrected</span> means an official source supports the correction. <span class="context-label">Context only · not proof</span> means the linked official site does not establish the particular claim.</div></div>
      {section_head('01', 'PLANNING & CORRECTIONS', 'Fix what matters first', 'Dates, tickets and hotel nights remain open. Supported route fixes are incorporated in the proposed 16 days.')}
      {review_table(core)}
      <div id="unverified-merchants" class="subsection-heading"><span class="eyebrow dark">02 / KEEP OFF THE CONFIRMED ROUTE</span><h2>Unverified shortlist</h2><p>These names appeared in the supplied itinerary notes. Their addresses and hours are deliberately blank. Directory links are starting points, <strong>not proof</strong> these businesses are currently operating.</p></div>
      {review_table(merchants, merchant=True)}</section>'''
    return page("Flagged for review", body, active="review", description="Transparent review ledger for date conflicts, unbooked travel, corrected route errors and unverified venues across all 16 days.")


def sources_page() -> str:
    rows = "".join(f'<tr id="source-{e(key)}"><th scope="row" data-label="Source">{e(source["title"])}</th><td data-label="Claim scope">{e(source["scope"])}</td><td data-label="Official link">{cite([key], "context_only" if key in ("seoul_directory", "busan_directory", "royal_guard_2025") else "evidence")}</td></tr>' for key, source in SOURCES.items())
    body = intro_banner("THE AUDIT / LINKS", "The source shelf.", "Official operators and public tourism authorities, linked again in every place, route and review row where they are used.", f"{len(SOURCES):02} LINKS")
    body += f'''<section class="shell section-block">{section_head('01', 'METHOD', 'What a link does—and does not do', 'Checked 26 October 2026. A source supports only the claim described in its scope, not a booked ticket or a specific future-day opening.')}
      <div class="method-strip"><div><strong>01 / Operators first</strong><p>Ticket rules, timetables and store calendars come from the relevant operator where possible.</p></div><div><strong>02 / Public listings next</strong><p>City and national tourism bodies support addresses, access routes and general visitor information.</p></div><div><strong>03 / No forced consensus</strong><p>Conflicting prices or closing days are blank, labeled unverified and linked on the review board.</p></div></div>
      <div class="table-wrap"><table class="data-table source-table"><caption class="sr-only">Official source registry and claim scopes</caption><thead><tr><th scope="col">Official source</th><th scope="col">What we used it for</th><th scope="col">Open original</th></tr></thead><tbody>{rows}</tbody></table></div>
      <p class="under-table">City directory links marked “context only” are research starting points. For field-by-field provenance see the site tables and the repository's <code>docs/research/verification.md</code>.</p></section>'''
    return page("Official source shelf", body, description="Source registry for the 16-day Seoul and Busan itinerary, with official links and claim scopes.")


def not_found() -> str:
    body = '<section class="shell not-found"><span class="eyebrow dark">WRONG TURN / 404</span><h1>This stop isn\'t on the route.</h1><p>Find your way back to the 16-day field guide.</p><a class="button button-dark" href="index.html">Back to the itinerary ↗</a></section>'
    return page("Page not found", body)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "site", help="Static output directory (default: site)")
    args = parser.parse_args()
    out = args.out.resolve()
    protected = [ROOT, ROOT / "src", ROOT / "web", ROOT / "scripts", ROOT / ".git"]
    if out == ROOT or any(out == folder or folder in out.parents for folder in protected[1:]):
        parser.error("Refusing to overwrite a source or repository directory")
    out.mkdir(parents=True, exist_ok=True)
    (out / "days").mkdir(parents=True, exist_ok=True)
    shutil.copytree(ASSETS, out / "assets", dirs_exist_ok=True)
    (out / ".nojekyll").write_text("", encoding="utf-8")
    pages = {"index.html": overview(), "transport.html": transport_page(), "stays.html": stays_page(),
             "review.html": review_page(), "sources.html": sources_page(), "404.html": not_found()}
    pages.update({f"{key}.html": category_page(key) for key in CATEGORY})
    pages.update({f"days/{d['number']:02}.html": day_page(d) for d in DAYS})
    for filename, content in pages.items():
        (out / filename).write_text(content + "\n", encoding="utf-8")
    print(f"Built {len(pages)} pages and {len(SOURCES)} source links in {out}")


if __name__ == "__main__":
    main()
