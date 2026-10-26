#!/usr/bin/env python3
"""Append Week 2 (Days 10–16) sources and rows to root data.js without touching P001–P062."""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[1]
text = (root / "data.js").read_text(encoding="utf-8")
m = re.match(r"window\.TRIP = (\{.*\});\s*\Z", text, re.S)
if not m:
    raise SystemExit("Could not parse data.js")
trip = json.loads(m.group(1))

assert len(trip["rows"]) == 62
assert [r["id"] for r in trip["rows"]] == [f"P{i:03d}" for i in range(1, 63)]
assert len(trip["days"]) == 9

trip["checked"] = "2026-10-26"

trip["sources"].update({
    "haeundaeBeach": [
        "Busan Metropolitan Government · Haeundae Beach",
        "https://www.busan.go.kr/eng/beaches/1325815",
        "264 Haeundaehaebyeon-ro, Haeundae-gu, Busan. Admission free. Metro Line 2, Haeundae Station exit 3 or 5, about a 5-minute walk. Inquiry (051)749-7612. Page does not state a year-round closing time for walking the sand."
    ],
    "amsoKto": [
        "VISITKOREA · Haeundae Amso Galbijip",
        "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=73814",
        "Address 32-10 Jungdong 2-ro 10beon-gil / 해운대해변로 333. Hours 11:30–22:00 with weekend break 15:15–16:30. Closed Seollal and Chuseok holidays. Phone +82-51-746-0033. Official site linked: haeundaegalbi.com."
    ],
    "amsoMichelin": [
        "MICHELIN Guide · Haeundae Rib Barbecue Restaurant",
        "https://guide.michelin.com/us/en/busan-region/busan_1025838/restaurant/haeundae-rib-barbecue-restaurant",
        "2026 MICHELIN Guide South Korea listing. Address 333 Haunedahaebyeon-ro, Haeundae-gu, Busan. Daily 11:30–14:00 and 17:00–22:00. Fresh ribs may be reserved up to a week ahead; restaurant manages its own bookings."
    ],
    "nurimaru": [
        "Busan Metropolitan Government · Nurimaru APEC House",
        "https://www.busan.go.kr/nurimaru/english/Design/sub0101.jsp",
        "Opening hours 09:00–18:00, last admission 1 hour before closing. Closed the first Monday of the month. Admission free. Metro Line 2 Dongbaek Station Exit 1; bus 1003 to Dongbaek-seom."
    ],
    "dongbaek": [
        "Visit Busan · Dongbaek walking tour / Nurimaru",
        "https://www.visitbusan.net/en/index.do?menuCd=DOM_000000302004001000&uc_seq=284&lang_cd=en",
        "Official tourism listing: 99 Dongbaek-ro, Haeundae-gu. Area open all year; Nurimaru closed every first Monday. Visit Busan lists Nurimaru hours 09:00–17:00, which conflicts with the operator’s 09:00–18:00 page."
    ],
    "skyTime": [
        "Haeundae Blueline Park · Sky Capsule hours",
        "https://www.bluelinepark.com/eng/skyCapsuleTime.do",
        "Winter (Nov–Feb) 08:30–18:00; one-way boarding about 30 minutes at 4 km/h. Hours may change for safety, peak crowding, or weather disasters. Normal operation on rainy days unless stopped for heavy rain/typhoon."
    ],
    "skyCourse": [
        "Haeundae Blueline Park · Sky Capsule course",
        "https://www.bluelinepark.com/eng/skyCapsuleCourse.do",
        "2.0 km Mipo–Cheongsapo aerial rail, 7–10 m up. Ticketing at Mipo and Cheongsapo. Official course table lists one-way Mipo→Cheongsapo and one-way Cheongsapo→Mipo. About 30 minutes one way."
    ],
    "skyBook": [
        "Haeundae Blueline Park · reservations",
        "https://www.bluelinepark.com/eng/booking.do",
        "Official reservation interface. Advance booking is the operator’s published method; this retrieval does not confirm a specific travel-date slot."
    ],
    "daritdol": [
        "VISITKOREA · Cheongsapo Daritdol Observatory",
        "https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=112698",
        "167 Cheongsapo-ro, Haeundae-gu, Busan. Free. Open all year. Hours: Dec–Feb 09:00–20:00; Mar–May and Sep–Nov 09:00–21:00; Jun–Aug 09:00–22:00. Source notes Haeundae-gu Office. Visit Busan separately lists 09:00–18:00 — hours left blank because of that conflict."
    ],
    "xthesky": [
        "BUSAN X the SKY · official operator",
        "https://www.busanxthesky.com/",
        "Mon–Sun 10:00–21:00 (weekdays, weekends and holidays the same). Last on-site ticket 30 minutes before close. Adult (13+) ₩29,000; child (36 months–under 13) and seniors 65+ ₩26,000. Address: 30 Dalmaji-gil, Haeundae-gu, Busan, LCT Landmark Tower. Nearby metro: Jung-dong and Haeundae on Line 2."
    ],
    "gamcheon": [
        "Visit Busan · Gamcheon Culture Village",
        "https://www.visitbusan.net/index.do?menuCd=DOM_000000301001001000&uc_seq=365&lang_cd=en",
        "203 Gamnae 2-ro, Saha-gu, Busan. Open throughout the year. Visitor hours every day March–October 09:00–18:00, November–February 09:00–17:00. Free except parking. Inquiry +82-51-204-1444. VISITKOREA separately lists ‘Open 24 hr’ for the lived-in village."
    ],
    "jagalchi": [
        "VISITKOREA · Jagalchi Market",
        "https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=69318",
        "52 Jagalchihaean-ro, Jung-gu, Busan. Hours 05:00–22:00. Closed 1st and 3rd Tuesdays. Operator site bisco.or.kr/jagalchimarket. Inquiry +82-51-245-2594."
    ],
    "gukje": [
        "VISITKOREA · Busan Gukje Market",
        "https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=929&dataSetId=263&vcontsId=249917",
        "25 Gukjesijang 2-gil, Jung-gu, Busan. Hours 09:00–20:00. Closed 1st and 3rd Sunday of each month. Inquiry +82-51-245-7389."
    ],
    "biff": [
        "Visit Busan · BIFF Square city walk",
        "https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000302011001000&uc_seq=2809",
        "Official tourism listing for BIFF Square in Nampo-dong. Public street; individual stall hours are not established on this page."
    ],
    "songdoBeach": [
        "Visit Busan · Songdo Beach",
        "https://visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=286",
        "100 Songdohaebyeon-ro, Seo-gu, Busan. Open all year. Hours 06:00–23:00. Free. Inquiry +82-51-240-4000."
    ],
    "songdoCloud": [
        "Visit Busan · three major skywalks (Songdo Cloud Trails)",
        "https://www.visitbusan.net/index.do?menuCd=DOM_000000301001001000&uc_seq=282&lang_cd=en",
        "Songdo Cloud Trails: 129-4 Amnam-dong, Seo-gu, Busan. Hours 06:00–23:00. Free. Inquiry +82-51-240-4081. Limited opening in snow, rain, strong wind or repair."
    ],
    "airCruiseTime": [
        "Busan Air Cruise · business hours",
        "https://en.busanaircruise.co.kr/info/time?rank=2",
        "Jan–Feb and December 09:00–20:00; Mar–Jun and Sep–Nov 09:00–21:00; Jul–Aug 09:00–22:00. Tickets until 30 minutes before closing. Weather can change operations. Address on operator location pages: 171 Songdohaebyeon-ro, Seo-gu, Busan."
    ],
    "airCruisePrice": [
        "Busan Air Cruise · fares",
        "https://en.busanaircruise.co.kr/info/price?rank=1",
        "Air Cruise (closed floor) adult round trip ₩19,000 / one way ₩15,000. Crystal Cruise (glass floor) adult round trip ₩24,000 / one way ₩19,000. Adult = 13+; child = 36 months–12 years. Retrieved 2026-10-26."
    ],
    "sealifeHours": [
        "SEA LIFE Busan Aquarium · opening hours",
        "https://www.visitsealife.com/busan/en/plan-your-visit/before-you-visit/opening-hours/",
        "Weekdays 10:00–19:00, last entry 18:00. Weekends 10:00–20:00, last entry 19:00. Hours may change with site conditions and weather. Calendar on the same page showed Monday 26 Oct 2026 as a weekday 10am–7pm schedule."
    ],
    "sealifeTickets": [
        "SEA LIFE Busan Aquarium · tickets",
        "https://www.visitsealife.com/busan/en/tickets-passes/",
        "English tickets page retrieved 2026-10-26 lists child on-site ₩27,500 and online-from prices; it does not state a single adult on-site fare in the extracted text. Traveler ‘$15’ is not on this page."
    ],
    "droneKto": [
        "VISITKOREA · Gwangalli M Drone Light Show",
        "https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=194990",
        "Every Saturday, twice, about 12 minutes. March–September 20:00 and 22:00; October–February 19:00 and 21:00. Venue 219 Gwanganhaebyeon-ro, Suyeong-gu, Busan. Free. Host: Suyeong-gu. Schedule subject to weather. Official site gwangallimdrone.co.kr."
    ],
    "droneCity": [
        "Busan Metropolitan Government · Gwangalli M Drone Light Show 2026",
        "https://www.busan.go.kr/eng/bsevents/1713160",
        "Period listed 2026-01-03 through 2026-12-31. Every Saturday; March–September 20:00, 22:00 / October–February 19:00, 21:00. Venue Gwangalli Beach. About 12 minutes. May be canceled or delayed for weather or technical issues."
    ],
    "gwangalli": [
        "Visit Busan · Gwangalli Beach",
        "https://www.visitbusan.net/index.do?lang_cd=en&menuCd=DOM_000000301001001000&uc_seq=377",
        "Official tourism listing for Gwangalli Beach. Public beach area; this page is used for identity and location, not a ticketed closing time."
    ],
    "mercure": [
        "Accor · Mercure Ambassador Seoul Hongdae",
        "https://all.accor.com/hotel/B696/index.en.shtml",
        "144 Yanghwa Ro, Mapo Gu, 04050 Seoul. Check-in from 15:00; checkout up to 12:00. Hongik Univ Station 100 m / 1-minute walk (hotel also states a 2-minute walk). Linked to Incheon and Gimpo by AREX. Not a reservation confirmation."
    ],
    "arexAll": [
        "AREX · all-stop (일반열차) fare table",
        "https://www.airportrailroad.com/train/normal/fare",
        "Adult transit-card fare Seoul Station ↔ Hongik Univ (홍대입구) ₩1,550. All-stop trains serve Hongik Univ; the Express (직통) does not. Single-use cards add ₩100 plus ₩500 deposit."
    ],
    "arexHongik": [
        "AREX · Hongik Univ station",
        "https://www.airportrailroad.com/train/normal/info/030/0",
        "A03 Hongik Univ (홍대입구). Address: 188 Yanghwa-ro (underground), Mapo-gu, Seoul. Transfers: Seoul Metro Line 2 and Gyeongui–Jungang Line."
    ],
    "haeundaeMarket": [
        "Visit Busan · Haeundae Market",
        "https://www.visitbusan.net/en/index.do?lang_cd=en&menuCd=DOM_000000303011001000&uc_seq=294",
        "Official tourism listing for Haeundae Market. Individual stall hours are not treated as confirmed from this session’s retrieval."
    ]
})

new_rows = [
    {
        "id": "P063", "day": 10, "category": "Sights",
        "name": "Haeundae Beach (morning walk)",
        "original": "Morning: walk the beachfront Haeundae Beach area; explore cafés and shops around the beach.",
        "source": "haeundaeBeach",
        "hours": "",
        "location": "264 Haeundaehaebyeon-ro, Haeundae-gu, Busan · Line 2 Haeundae Station exit 3 or 5, ~5 min walk",
        "price": "Free (public beach)",
        "finding": "City page confirms identity, free admission and metro access. It does not publish a year-round gate time for walking the sand; November is outside the published summer swimming season. Café hours are not on this page.",
        "status": "Partial"
    },
    {
        "id": "P064", "day": 10, "category": "Food",
        "name": "Haeundae Amso Galbi (MICHELIN-listed)",
        "original": "Haeundae Amso Galbi (Michelin). Open at 11:30am. Go at least 30 min early to avoid long lines.",
        "source": "amsoMichelin",
        "hours": "Daily 11:30–14:00 and 17:00–22:00 (MICHELIN listing)",
        "location": "333 Haeundaehaebyeon-ro, Haeundae-gu, Busan",
        "price": "",
        "finding": "MICHELIN Guide 2026 listing retrieved; opening 11:30 is supported. ‘Arrive 30 minutes early’ is traveler advice, not an official rule. VISITKOREA lists 11:30–22:00 with a weekend break 15:15–16:30, which does not match MICHELIN’s 14:00–17:00 gap — break times flagged. No table-reservation policy was confirmed on the operator homepage (dynamic). Fresh-rib advance notice is MICHELIN text, not a booking for this trip.",
        "status": "Partial"
    },
    {
        "id": "P065", "day": 10, "category": "Sights",
        "name": "Dongbaekseom Island & coastal trail",
        "original": "Walk toward Dongbaekseom Island (west end of Haeundae Beach). Follow the Dongbaek Coastal Trail around the peninsula.",
        "source": "dongbaek",
        "hours": "",
        "location": "99 Dongbaek-ro, Haeundae-gu, Busan (Visit Busan walking-tour listing)",
        "price": "Free (outdoor trails)",
        "finding": "Official tourism listing identifies the Dongbaek / Nurimaru walking area as open all year. Exact trail length, walking time from L7, and a named ‘Dongbaek Coastal Trail’ schedule were not on the operator page.",
        "status": "Partial"
    },
    {
        "id": "P066", "day": 10, "category": "Sights",
        "name": "Nurimaru APEC House",
        "original": "Visit Nurimaru APEC House. Admission is free.",
        "source": "nurimaru",
        "hours": "09:00–18:00; last admission 17:00; closed first Monday of each month",
        "location": "Dongbaekseom · Metro Line 2 Dongbaek Station Exit 1; bus 1003 to Dongbaek-seom",
        "price": "Free",
        "finding": "Operator page confirms free admission and hours. If the trip year is 2026, the first Monday in November is 2 Nov (Day 2, still in Seoul), so a Tuesday 10 Nov visit would not hit that closure — calendar math only, year still unresolved. Visit Busan lists 09:00–17:00 vs operator 09:00–18:00; operator hours used.",
        "status": "Partial"
    },
    {
        "id": "P067", "day": 10, "category": "Transport",
        "name": "Haeundae Sky Capsule (Mipo ↔ Cheongsapo)",
        "original": "From the hotel, take the bus to Mipo Station. Take the Sky Capsule toward Cheongsapo. Book in advance; can sell out. Book round-trip tickets. Get off at Cheongsapo.",
        "source": "skyCourse",
        "hours": "November 08:30–18:00 (winter season)",
        "location": "Mipo Station ↔ Cheongsapo Station · 2.0 km aerial rail",
        "price": "",
        "finding": "Operator course page states one-way Mipo→Cheongsapo and one-way Cheongsapo→Mipo (~30 min). ‘Round-trip tickets’ is not what that table shows. Fare pages conflict across the operator site (prior research); price left blank. Advance booking URL is official. Hotel-to-Mipo bus number, duration and fare are not established.",
        "status": "Partial"
    },
    {
        "id": "P068", "day": 10, "category": "Transport",
        "name": "L7 / Haeundae → Mipo Station bus",
        "original": "From the hotel, take the bus to Mipo Station.",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No official bus number, stop, duration or fare was confirmed for the L7–Mipo leg.",
        "status": "Unverified"
    },
    {
        "id": "P069", "day": 10, "category": "Sights",
        "name": "Cheongsapo Daritdol Observatory",
        "original": "If you don’t book round-trip capsule tickets, walk the Cheongsapo Daritdol Observatory — sea-facing skywalk. Take pictures.",
        "source": "daritdol",
        "hours": "",
        "location": "167 Cheongsapo-ro, Haeundae-gu, Busan",
        "price": "Free",
        "finding": "VISITKOREA confirms identity, free admission and address. Hours conflict: VISITKOREA Sep–Nov 09:00–21:00 vs Visit Busan 09:00–18:00. Hours left blank. Weather/repair closures are noted on the Visit Busan skywalks page.",
        "status": "Partial"
    },
    {
        "id": "P070", "day": 10, "category": "Sights",
        "name": "Busan X the Sky (optional on Day 10)",
        "original": "Late afternoon: Visit Busan X the Sky — optional. $17.59 on Klook. Skip if you don’t care about observatory decks.",
        "source": "xthesky",
        "hours": "Daily 10:00–21:00; last on-site ticket 20:30",
        "location": "30 Dalmaji-gil, Haeundae-gu, Busan · LCT Landmark Tower · Line 2 Jung-dong / Haeundae",
        "price": "Adult (13+) ₩29,000 on-site (operator)",
        "finding": "Operator hours and adult on-site fare confirmed. Traveler ‘$17.59 on Klook’ is a reseller figure, not the operator tariff. Also scheduled as a timed visit on Day 12 — do not assume both. Visit Busan lists a different adult fare (₩27,000); operator ₩29,000 used.",
        "status": "Partial"
    },
    {
        "id": "P071", "day": 10, "category": "Food",
        "name": "Dinner in Haeundae / Haeundae Market",
        "original": "Evening: dinner in Haeundae. Explore Haeundae Market.",
        "source": "haeundaeMarket",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Market identity is on Visit Busan. Stall hours, dishes and a walking time from L7 were not confirmed in this retrieval.",
        "status": "Unverified"
    },
    {
        "id": "P072", "day": 11, "category": "Food",
        "name": "Breakfast (unspecified)",
        "original": "Morning: get breakfast.",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No restaurant named. Nothing to verify.",
        "status": "Unverified"
    },
    {
        "id": "P073", "day": 11, "category": "Transport",
        "name": "Haeundae → Gamcheon (two buses)",
        "original": "Take the 2 buses to Gamcheon Culture Village. 1 hr 17 min.",
        "source": "gamcheon",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Visit Busan identifies the village but does not confirm a two-bus, 1 hr 17 min itinerary from L7 Haeundae. Duration, bus numbers and fare left blank.",
        "status": "Unverified"
    },
    {
        "id": "P074", "day": 11, "category": "Sights",
        "name": "Gamcheon Culture Village",
        "original": "Spend 2–3 hours wandering the alleys, viewpoints, art installations and shops.",
        "source": "gamcheon",
        "hours": "Visitor facilities Nov–Feb 09:00–17:00 (Mar–Oct 09:00–18:00)",
        "location": "203 Gamnae 2-ro, Saha-gu, Busan",
        "price": "Free (except parking; some activities extra)",
        "finding": "Visit Busan confirms address, free entry and seasonal visitor hours. VISITKOREA lists ‘Open 24 hr’ because it is a lived-in neighborhood — shops still follow visitor hours. 2–3 hours is traveler planning, not an official dwell time.",
        "status": "Partial"
    },
    {
        "id": "P075", "day": 11, "category": "Food",
        "name": "Coffee It House",
        "original": "Go to Coffee It House (2 minute walk).",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No official operator or tourism-board page was retrieved. Third-party hours conflict (examples 09:30–18:30 vs 10:30–20:00). Hours, address and the 2-minute walk are unverified.",
        "status": "Unverified"
    },
    {
        "id": "P076", "day": 11, "category": "Food",
        "name": "BIFF Square street food",
        "original": "Lunch: take bus to BIFF Square. Try street food/snacks.",
        "source": "biff",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Visit Busan identifies BIFF Square as a Nampo-dong public street. Bus from Gamcheon, vendor hours and prices are not on that page.",
        "status": "Unverified"
    },
    {
        "id": "P077", "day": 11, "category": "Food",
        "name": "Jagalchi Fish Market",
        "original": "Walk to Jagalchi Fish Market (9 min. walk).",
        "source": "jagalchi",
        "hours": "05:00–22:00; closed 1st & 3rd Tuesdays",
        "location": "52 Jagalchihaean-ro, Jung-gu, Busan",
        "price": "",
        "finding": "VISITKOREA confirms hours, weekly closures and address. The 9-minute walk from BIFF Square was not measured on an official page. Day 11 is a Wednesday in the brief, so the Tuesday closure would not apply if weekdays are correct — year still unresolved. Individual stall hours vary.",
        "status": "Partial"
    },
    {
        "id": "P078", "day": 11, "category": "Sights",
        "name": "Songdo Beach",
        "original": "Take bus to Songdo Beach — 13 min bus ride, 9 min walk.",
        "source": "songdoBeach",
        "hours": "06:00–23:00",
        "location": "100 Songdohaebyeon-ro, Seo-gu, Busan",
        "price": "Free",
        "finding": "Visit Busan confirms address, hours and free admission. The 13-minute bus / 9-minute walk from Jagalchi is traveler timing, not confirmed here.",
        "status": "Partial"
    },
    {
        "id": "P079", "day": 11, "category": "Sights",
        "name": "Songdo Cloud Trails",
        "original": "Walk the Songdo Cloud Trails — Busan’s major ocean skywalks.",
        "source": "songdoCloud",
        "hours": "06:00–23:00; limited in snow, rain, strong wind or repair",
        "location": "129-4 Amnam-dong, Seo-gu, Busan",
        "price": "Free",
        "finding": "Visit Busan skywalks page confirms hours, free admission and address.",
        "status": "Partial"
    },
    {
        "id": "P080", "day": 11, "category": "Sights",
        "name": "Songdo Marine Cable Car (optional)",
        "original": "Optional: Songdo Marine Cable Car.",
        "source": "airCruiseTime",
        "hours": "Sep–Nov 09:00–21:00; tickets until 30 min before close",
        "location": "171 Songdohaebyeon-ro, Seo-gu, Busan (operator)",
        "price": "Air Cruise adult round trip ₩19,000 / one way ₩15,000",
        "finding": "Operator hours and fares retrieved 2026-10-26. Weather can halt rides. Optional in the brief — not a booked ticket.",
        "status": "Partial"
    },
    {
        "id": "P081", "day": 11, "category": "Shopping",
        "name": "Gukje Market",
        "original": "Late afternoon: Jagalchi Market, BIFF Square, Gukje Market, Nampo-dong shopping streets.",
        "source": "gukje",
        "hours": "09:00–20:00; closed 1st and 3rd Sundays",
        "location": "25 Gukjesijang 2-gil, Jung-gu, Busan",
        "price": "",
        "finding": "VISITKOREA confirms hours and Sunday closures. Individual shops vary. Day 11 is a Wednesday in the brief.",
        "status": "Partial"
    },
    {
        "id": "P082", "day": 11, "category": "Shopping",
        "name": "Nampo-dong shopping streets",
        "original": "Nampo-dong shopping streets.",
        "source": "biff",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Public streets. No single official hour applies to every shop.",
        "status": "Unverified"
    },
    {
        "id": "P083", "day": 12, "category": "Food",
        "name": "Breakfast (unspecified)",
        "original": "Eat breakfast somewhere.",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No restaurant named.",
        "status": "Unverified"
    },
    {
        "id": "P084", "day": 12, "category": "Sights",
        "name": "Busan X the Sky (timed 10:00–11:30)",
        "original": "10:00am–11:30am — Busan X the SKY. Observation deck in the LCT Landmark Tower. Hours: 10am–9pm.",
        "source": "xthesky",
        "hours": "Daily 10:00–21:00; last on-site ticket 20:30",
        "location": "30 Dalmaji-gil, Haeundae-gu, Busan · LCT Landmark Tower",
        "price": "Adult (13+) ₩29,000 on-site (operator)",
        "finding": "Operator confirms 10:00–21:00, matching the brief’s 10am–9pm. The 10:00–11:30 window is traveler scheduling, not a ticketed slot. Duplicate of optional Day 10 visit (P070). Klook $17.59 is not the operator fare.",
        "status": "Partial"
    },
    {
        "id": "P085", "day": 12, "category": "Food",
        "name": "Lunch near Haeundae",
        "original": "Lunch: eat near Haeundae or choose a restaurant around the beachfront.",
        "source": "haeundaeBeach",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No restaurant named.",
        "status": "Unverified"
    },
    {
        "id": "P086", "day": 12, "category": "Sights",
        "name": "SEA LIFE Busan Aquarium",
        "original": "SEA LIFE Busan Aquarium. $15 ticket. Weekday hours: 10am–7pm.",
        "source": "sealifeHours",
        "hours": "Weekdays 10:00–19:00 (last entry 18:00); weekends 10:00–20:00 (last entry 19:00)",
        "location": "",
        "price": "",
        "finding": "Operator hours match the brief’s weekday 10:00–19:00. Traveler ‘$15’ is not on the official English tickets page. Adult on-site fare was not a single unambiguous figure in the retrieved English tickets text (VISITKOREA lists ₩32,000; Visit Busan lists ₩31,000). Price left blank. Address not copied from a third party.",
        "status": "Partial"
    },
    {
        "id": "P087", "day": 12, "category": "Food",
        "name": "Dinner (unspecified)",
        "original": "Dinner: (blank in the brief).",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No restaurant named. Left empty.",
        "status": "Unverified"
    },
    {
        "id": "P088", "day": 13, "category": "Sights",
        "name": "Day 13 · unscheduled Friday",
        "original": "Day 13: Friday — no activities listed.",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Brief has no plan. No stops invented.",
        "status": "Unverified"
    },
    {
        "id": "P089", "day": 14, "category": "Sights",
        "name": "Gwangalli Beach (evening)",
        "original": "Evening 5:00pm — head to Gwangalli Beach. Have an early dinner or a snack and find a viewing spot.",
        "source": "gwangalli",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Visit Busan identifies Gwangalli Beach. 17:00 departure, dinner venue, viewing-spot and transit from L7 are not official facts.",
        "status": "Unverified"
    },
    {
        "id": "P090", "day": 14, "category": "Sights",
        "name": "Gwangalli M. Drone Light Show",
        "original": "Saturday night highlight: Gwangalli M. Drone Light Show. Winter performance at 7:00pm and 9:00pm. 12 minutes. Watch the 7pm show.",
        "source": "droneCity",
        "hours": "Winter (Oct–Feb) Saturdays 19:00 and 21:00; ~12 minutes; weather/technical cancellation possible",
        "location": "Gwangalli Beach · 219 Gwanganhaebyeon-ro, Suyeong-gu, Busan",
        "price": "Free",
        "finding": "Busan city 2026 event page and VISITKOREA agree on Saturday winter 19:00 / 21:00, ~12 minutes, free. Confirm the specific Saturday on gwangallimdrone.co.kr the week of travel — shows are canceled for weather and sometimes for other beach events. 19:00 viewing is the traveler’s choice of the two official slots.",
        "status": "Partial"
    },
    {
        "id": "P091", "day": 15, "category": "Sights",
        "name": "Day 15 · unscheduled Sunday",
        "original": "Day 15: Sunday — no activities listed.",
        "source": "busan",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Brief has no plan. No stops invented.",
        "status": "Unverified"
    },
    {
        "id": "P092", "day": 16, "category": "Food",
        "name": "Breakfast (unspecified)",
        "original": "Eat breakfast.",
        "source": "l7",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "No restaurant named. L7 breakfast offering was not confirmed on the retrieved hotel page.",
        "status": "Unverified"
    },
    {
        "id": "P093", "day": 16, "category": "Stay",
        "name": "L7 Haeundae checkout",
        "original": "Check out L7 Haeundae Hotel before 11:00am.",
        "source": "l7",
        "hours": "Checkout 11:00",
        "location": "55 Haeun-daero 570beon-gil, Haeundae-gu, Busan",
        "price": "",
        "finding": "Operator page already confirmed standard checkout 11:00. Matches the brief. Not a reservation.",
        "status": "Partial"
    },
    {
        "id": "P094", "day": 16, "category": "Transport",
        "name": "L7 → Busan Station",
        "original": "Take uber to Busan Station. (1 hour ride, $20–$30).",
        "source": "korail",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "Duration and dollar fare are traveler estimates. No official taxi tariff or public-transit alternative was confirmed for this hotel-to-station leg.",
        "status": "Unverified"
    },
    {
        "id": "P095", "day": 16, "category": "Transport",
        "name": "KTX · Busan → Seoul Station",
        "original": "Take KTX train to Seoul. Get off at Seoul Station.",
        "source": "korail",
        "hours": "",
        "location": "",
        "price": "",
        "finding": "KORAIL booking exists; no train number, time or fare is selected for this trip.",
        "status": "Unverified"
    },
    {
        "id": "P096", "day": 16, "category": "Transport",
        "name": "AREX all-stop · Seoul Station → Hongik Univ",
        "original": "Take AREX from Seoul Station to Hongdae. Get off at Hongik Univ. Station.",
        "source": "arexAll",
        "hours": "",
        "location": "AREX Hongik Univ (A03) · 188 Yanghwa-ro (underground), Mapo-gu",
        "price": "Adult transit card ₩1,550 (Seoul Station ↔ Hongik Univ)",
        "finding": "Official fare table confirms ₩1,550 adult transit-card between Seoul Station and Hongik Univ on the all-stop train. AREX Express is nonstop airport–Seoul Station and does not stop at Hongdae — use 일반열차 (all-stop), not Express. Travel time for this short hop is not printed as a single figure on the fare page.",
        "status": "Partial"
    },
    {
        "id": "P097", "day": 16, "category": "Stay",
        "name": "Mercure Ambassador Seoul Hongdae",
        "original": "Walk to Mercure Ambassador Seoul Hongdae. 8 minute walk.",
        "source": "mercure",
        "hours": "Check-in from 15:00; checkout up to 12:00",
        "location": "144 Yanghwa Ro, Mapo Gu, 04050 Seoul · Hongik Univ Station 100 m / 1-minute walk (hotel also states 2-minute walk)",
        "price": "",
        "finding": "Accor property page confirms identity, address and check-in/out. Traveler ‘8 minute walk’ conflicts with the hotel’s 100 m / 1–2 minute walk from Hongik Univ Station. Not a reservation. Day 16 arrival before 15:00 would need a luggage plan — not stated on the retrieved page.",
        "status": "Partial"
    }
]

trip["rows"].extend(new_rows)
trip["days"].extend([
    ["Haeundae, Dongbaek & the coast", "Nov 10 · Tuesday", "Busan", "Beach walk, island trails, Sky Capsule. The observatory is optional."],
    ["Gamcheon, Songdo & Nampo", "Nov 11 · Wednesday", "Busan", "Hill village, fish market, and the Songdo skywalk."],
    ["Observatory, aquarium, Haeundae", "Nov 12 · Thursday", "Busan", "X the Sky is also listed on Day 10. Confirm you want both."],
    ["A free Friday in Busan", "Nov 13 · Friday", "Busan", "Unscheduled. No extra stops invented."],
    ["Gwangalli night lights", "Nov 14 · Saturday", "Busan", "Early dinner, then the winter drone show — weather permitting."],
    ["A free Sunday in Busan", "Nov 15 · Sunday", "Busan", "Unscheduled. No extra stops invented."],
    ["Back to Seoul · Hongdae", "Nov 16 · Monday", "Busan → Seoul", "Checkout, KTX, AREX all-stop to Hongik Univ, Mercure Hongdae."]
])

assert len(trip["rows"]) == 97
assert len(trip["days"]) == 16
ids = [r["id"] for r in trip["rows"]]
assert ids == [f"P{i:03d}" for i in range(1, 98)]
for r in trip["rows"]:
    assert r["source"] in trip["sources"]
    if r["status"] == "Unverified":
        assert r["hours"] == r["price"] == r["location"] == ""

out = "window.TRIP = " + json.dumps(trip, ensure_ascii=False, indent=2) + ";\n"
(root / "data.js").write_text(out, encoding="utf-8")
print("Wrote", len(trip["rows"]), "rows,", len(trip["days"]), "days,", len(trip["sources"]), "sources")
