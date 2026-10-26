#!/usr/bin/env python3
"""Validate source provenance, itinerary integrity, rendered HTML rows and local links."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "data"
ALLOWED_HOSTS = {
    "royal.khs.go.kr", "onionkr.com", "english.visitseoul.net", "english.visitkorea.or.kr", "visitbusan.net", "www.visitbusan.net",
    "ddp.or.kr", "www.nseoultower.co.kr", "www.cablecar.co.kr", "guide.michelin.com", "m.starfield.co.kr",
    "www.adererror.com", "global.margesherwood.com", "locations.musinsa.com", "www.lotteshopping.com",
    "www.shinsegae.com", "www.stanford-hotel.com", "www.lottehotel.com", "www.korail.com",
    "myeongdongtown.oliveyoung.com", "en.blueelephant.co",
    "www.seoulmetro.co.kr", "www2.humetro.busan.kr", "www.airportrailroad.com", "www.bluelinepark.com",
    "www.visitsealife.com", "all.accor.com",
}


def load(name: str) -> dict:
    return json.loads((DATA / (name + ".json")).read_text(encoding="utf-8"))


def require(test: bool, message: str) -> None:
    if not test:
        raise AssertionError(message)


def validate_data() -> set[str]:
    sources = load("sources")["sources"]
    places = load("places")["places"]
    review = load("review")["items"]
    itinerary = load("itinerary")
    days = itinerary["days"]
    require(len(sources) >= 55, "Source registry unexpectedly sparse")
    require(len(days) == 16, "Exactly sixteen proposed days are required")
    require(len(places) >= 45, "Place ledger unexpectedly sparse")
    require(len(review) >= 35, "Review register unexpectedly sparse")
    require(len({x["id"] for x in places}) == len(places), "Duplicate place IDs")
    require(len({x["id"] for x in review}) == len(review), "Duplicate review IDs")
    require("2026" in itinerary["trip"]["date_note"] and "not confirmed" in itinerary["trip"]["date_note"].lower(), "Working year must be flagged")
    ids = {x["id"] for x in places}
    flags = {x["id"] for x in review}
    require({
        "dates", "flights", "hotels", "train_booking", "after_trip", "open_days", "haeundae_hours",
        "blueline_fare", "jagalchi_closure", "onion_weekend_hours",
        "day9_duplicate", "sky_capsule_roundtrip", "amso_galbi_michelin", "nurimaru_hours",
        "xthesky_conflict", "sealife_price", "busan_open_days", "arex_hongdae", "mercure_walk", "coffee_it_house"
    } <= flags, "Core review issues missing")
    official_urls = set()
    for sid, source in sources.items():
        require(sid and all(source.get(k) for k in ("title", "url", "scope")), f"Bad source: {sid}")
        parsed = urlsplit(source["url"])
        require(parsed.scheme == "https" and parsed.netloc in ALLOWED_HOSTS, f"Non-official or insecure source: {sid}: {source['url']}")
        official_urls.add(source["url"])

    def check_sources(record: dict, kind: str) -> None:
        refs = record.get("sources", [])
        require(refs and all(s in sources for s in refs), f"Missing official source in {kind} {record.get('id', '')}")

    for place in places:
        check_sources(place, "place")
        require(place["category"] in {"sights", "food", "shopping", "stays"}, f"Invalid category: {place['id']}")
        require(place["city"] in {"Seoul", "Busan"}, f"Invalid city: {place['id']}")
        for field in ("name", "area", "note"):
            require(bool(place.get(field)), f"Missing {field}: {place['id']}")
        for field in ("address", "access", "hours", "days", "price"):
            require(place.get(field) is None or isinstance(place[field], str), f"Invalid {field}: {place['id']}")
    by_id = {x["id"]: x for x in places}
    require(by_id["sky_capsule"]["price"] is None and by_id["beach_train"]["price"] is None, "Conflicting Blueline fare must stay blank")
    require(by_id["x_the_sky"]["price"] is None, "Conflicting BUSAN X the SKY adult fare and third-party Klook price must stay blank")
    require(by_id["sealife"]["price"] is None, "Unverified SEA LIFE Busan adult ticket price must stay blank")
    require(by_id["amso_galbi"]["price"] is None and "afternoon break unverified" in by_id["amso_galbi"]["hours"], "Amso Galbi afternoon break conflict must remain flagged")
    require("MICHELIN Guide Selected" in by_id["amso_galbi"]["note"] and "not Michelin-starred" in by_id["amso_galbi"]["note"], "Amso Galbi MICHELIN distinction must be explicit")
    require("17:00 vs 18:00" in by_id["nurimaru"]["hours"], "Conflicting Nurimaru closing hours must remain flagged")
    require(by_id["jagalchi"]["days"] is None, "Conflicting Jagalchi Tuesday pattern must stay blank")
    require(by_id["haeundae_beach"]["hours"] is None, "Ambiguous beach listing hours must stay blank")
    require("weekend opening unverified" in by_id["onion_seongsu"]["hours"], "Conflicting Onion weekend hour must remain flagged")
    require("Bib Gourmand" in by_id["kyoja"]["note"] and "starred" not in by_id["kyoja"]["note"], "Michelin distinction changed")
    require(by_id["hanjungsun"]["address"] == "1F, 43-1 Yeonmujang-gil, Seongdong-gu, Seoul" and by_id["hanjungsun"]["hours"] == "10:30–22:00" and by_id["hanjungsun"]["days"] == "Daily", "Hanjungsun must match its current Visit Seoul listing")
    require(by_id["oliveyoung_n_seongsu"]["address"] == "13 Yeonmujang 7-gil, Seongdong-gu, Seoul" and by_id["oliveyoung_n_seongsu"]["hours"] == "10:00–22:00", "Olive Young N Seongsu must retain its exact KTO branch details")
    require("Guie Shopping Street 10:00–19:00" in by_id["gwangjang"]["hours"] and "closed Sundays" in by_id["gwangjang"]["days"], "Gwangjang section schedules must remain distinct")
    require("oliveyoung_myeongdong_global" in by_id["oliveyoung_town"]["sources"], "Myeongdong Global needs its direct operator source")
    require(by_id["mercure_hongdae"]["address"] == "144 Yanghwa-ro, Mapo-gu, Seoul", "Mercure Hongdae must match its official Accor address")
    review_by_id = {x["id"]: x for x in review}
    require(review_by_id["hanjungsun"]["source_role"] == "evidence" and review_by_id["hanjungsun"]["tier"] == "correction", "Hanjungsun's sourced listing and caveats must remain visible for review")
    require(review_by_id["blue_elephant"]["source_role"] == "evidence" and review_by_id["blue_elephant"]["tier"] == "discrepancy", "Blue Elephant's unresolved official branch conflict must remain flagged")
    require(review_by_id["sky_capsule_roundtrip"]["source_role"] == "evidence" and review_by_id["sky_capsule_roundtrip"]["tier"] == "correction", "Sky Capsule one-way ticket correction must remain flagged")
    require(review_by_id["arex_hongdae"]["source_role"] == "evidence" and review_by_id["arex_hongdae"]["tier"] == "correction", "AREX All-Stop vs Express Hongdae correction must remain flagged")
    for item in review:
        check_sources(item, "review item")
        require(item["source_role"] in {"evidence", "context_only"}, f"No source role: {item['id']}")
        require(item["tier"] in {"priority", "correction", "discrepancy", "merchant"}, f"Bad tier: {item['id']}")
        require(all(item.get(k) for k in ("title", "finding", "action", "topic")), f"Incomplete review: {item['id']}")
        if item["tier"] == "merchant":
            require(item["source_role"] == "context_only", f"Unverified merchant wrongly marked proven: {item['id']}")
    require(days[1]["stops"][0]["place"] == "gyeongbokgung" and days[2]["stops"][0]["place"] == "cablecar", "Palace Tuesday-closure correction must remain explicit")
    require({"hanjungsun", "oliveyoung_n_seongsu"} <= {stop["place"] for stop in days[3]["stops"]}, "Officially listed Seongsu restaurant and shop should be available on Day 4")
    require(days[5]["stops"][0]["place"] == "insadong", "Source outline keeps Ikseon/Insadong on Day 6")
    require(days[6]["city"] == "Seoul" and days[7]["city"] == "Seoul", "Original Days 7–8 must remain in Seoul")
    require(all(stop["optional"] for day in days[6:8] for stop in day["stops"]), "Source outline leaves Days 7–8 open")
    require(days[8]["city"] == "Seoul → Busan" and days[8]["hotel"] == "stanford" and days[8].get("end_hotel") == "l7", "Day 9 travels from Stanford to L7 Haeundae")
    require([stop["place"] for stop in days[8]["stops"]] == ["l7", "haeundae_market", "haeundae_beach"], "Day 9 arrives at L7 Haeundae")
    require({"dongbaek", "nurimaru", "sky_capsule", "daritdol"} <= {stop["place"] for stop in days[9]["stops"]}, "Day 10 must cover Dongbaek, Nurimaru, Sky Capsule and Daritdol")
    require({"gamcheon", "biff", "jagalchi", "songdo_beach", "songdo_skywalk", "gukje", "nampo_shopping"} <= {stop["place"] for stop in days[10]["stops"]}, "Day 11 must cover Gamcheon, Songdo and Nampo/Gukje")
    require({"x_the_sky", "sealife"} <= {stop["place"] for stop in days[11]["stops"]}, "Day 12 must cover BUSAN X the SKY and SEA LIFE Aquarium")
    require(all(stop["optional"] for idx in (12, 14) for stop in days[idx]["stops"]), "Days 13 and 15 have no submitted activities and must remain optional")
    require([stop["place"] for stop in days[13]["stops"]] == ["gwangalli", "drone"], "Day 14 Saturday covers Gwangalli Beach and the M Drone Light Show")
    require(days[15]["city"] == "Busan → Seoul" and days[15]["hotel"] == "l7" and days[15].get("end_hotel") == "mercure_hongdae", "Day 16 travels from L7 Haeundae to Mercure Ambassador Seoul Hongdae")
    extension_ids = {x["id"] for x in places if x.get("extension")}
    require(extension_ids == {"temple", "bupyeong"}, "Only editorial Busan options not in the submitted brief should carry the extension flag")
    for number, day in enumerate(days, start=1):
        dt = date.fromisoformat(day["date"])
        require(day["number"] == number and dt == date(2026, 11, 1) + timedelta(days=number - 1), f"Broken proposed date sequence: {number}")
        require(day["hotel"] in ids and by_id[day["hotel"]]["category"] == "stays", f"Missing hotel base on day {number}")
        require(day["stops"] and all(stop["place"] in ids for stop in day["stops"]), f"Missing place on day {number}")
        require(all(f in flags for f in day["flags"]), f"Unknown review flag on day {number}")
        for direction in ("depart", "return"):
            require(day[direction].get("text"), f"No hotel-based {direction} text for day {number}")
            check_sources(day[direction], f"day {number} {direction}")
        for stop in day["stops"]:
            require(stop.get("period") and stop.get("why") and isinstance(stop.get("optional"), bool), f"Incomplete day stop on day {number}")
    return official_urls


class AuditHTML(HTMLParser):
    def __init__(self, file: Path, official_urls: set[str]):
        super().__init__(convert_charrefs=True)
        self.file = file
        self.official_urls = official_urls
        self.refs: list[str] = []
        self.ids: set[str] = set()
        self.errors: list[str] = []
        self.h1 = 0
        self.table_depth = 0
        self.tbody_depth = 0
        self.row_links: list[int] = []
        self.source_rows = 0
        self.main = 0
        self.skip = False
        self.lang = False
        self.viewport = False
        self.images = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"duplicate HTML id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang") == "en"
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport = True
        if tag == "main":
            self.main += 1
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images += 1
            if "alt" not in attrs:
                self.errors.append("image missing alt")
        if tag == "table":
            self.table_depth += 1
        if tag in ("tbody", "tfoot") and self.table_depth:
            self.tbody_depth += 1
        if tag == "tr" and self.tbody_depth:
            self.row_links.append(0)
        if tag == "a" and "href" in attrs:
            href = attrs["href"]
            self.refs.append(href)
            if href == "#main" and attrs.get("class") == "skip-link":
                self.skip = True
            if self.row_links and self.tbody_depth and href in self.official_urls:
                self.row_links[-1] += 1
            if href.startswith("https://") and href not in self.official_urls:
                self.errors.append(f"external link not in official source registry: {href}")
            if href.startswith("http://") or href.startswith("javascript:"):
                self.errors.append(f"insecure link: {href}")
        if tag in ("link", "script", "img"):
            key = "href" if tag == "link" else "src"
            if key in attrs:
                self.refs.append(attrs[key])

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr" and self.row_links and self.tbody_depth:
            if self.row_links.pop() < 1:
                self.errors.append("data table row has no official source link")
            self.source_rows += 1
        if tag in ("tbody", "tfoot") and self.table_depth:
            self.tbody_depth -= 1
        if tag == "table":
            self.table_depth -= 1


def validate_site(out: Path, official_urls: set[str]) -> None:
    files = sorted(out.rglob("*.html"))
    require(len(files) == 25, f"Expected 25 generated pages, got {len(files)}")
    parsed: dict[Path, AuditHTML] = {}
    for file in files:
        parser = AuditHTML(file, official_urls)
        parser.feed(file.read_text(encoding="utf-8"))
        parser.close()
        require(parser.lang and parser.viewport and parser.skip and parser.main == 1 and parser.h1 == 1, f"Missing accessible document basics in {file}")
        require(not parser.errors, f"HTML audit failed in {file}: {parser.errors}")
        parsed[file.resolve()] = parser
    rows = 0
    links = 0
    for file, parser in parsed.items():
        rows += parser.source_rows
        for href in parser.refs:
            links += 1
            split = urlsplit(href)
            if split.scheme in ("https", "mailto"):
                continue
            require(not split.scheme and not split.netloc, f"Unexpected local URL scheme in {file}: {href}")
            local = (file.parent / unquote(split.path or file.name)).resolve()
            require(local.is_relative_to(out.resolve()), f"Local link escapes output: {file} → {href}")
            require(local.exists(), f"Broken local link or asset: {file} → {href}")
            if split.fragment:
                require(local in parsed and unquote(split.fragment) in parsed[local].ids, f"Broken anchor: {file} → {href}")
    require(rows >= 230, f"Too few source-linked table rows: {rows}")
    require((out / ".nojekyll").exists(), "Missing GitHub Pages .nojekyll")
    require("assets/site.css" in (out / "index.html").read_text(encoding="utf-8"), "Missing stylesheet")
    require("Editorial option · blank Busan day" in (out / "sights.html").read_text(encoding="utf-8"), "Editorial option label absent from sights")
    require("Editorial option · blank Busan day" in (out / "food.html").read_text(encoding="utf-8"), "Editorial option label absent from food")
    day9 = (out / "days" / "09.html").read_text(encoding="utf-8")
    require("ARRIVAL BASE · NOT BOOKED" in day9 and "L7 Haeundae" in day9, "Day 9 Busan arrival-base label missing")
    day16 = (out / "days" / "16.html").read_text(encoding="utf-8")
    require("ARRIVAL BASE · NOT BOOKED" in day16 and "Mercure Ambassador Seoul Hongdae" in day16, "Day 16 Hongdae arrival-base label missing")
    print(f"PASS: {len(files)} pages, {rows} data rows with official links, {links} links/assets checked, {len(official_urls)} registered official URLs")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Regenerate the site before auditing")
    parser.add_argument("--out", type=Path, default=ROOT / "site", help="Site output directory")
    args = parser.parse_args()
    out = args.out.resolve()
    if args.build:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py"), "--out", str(out)], check=True)
    official_urls = validate_data()
    validate_site(out, official_urls)


if __name__ == "__main__":
    main()
