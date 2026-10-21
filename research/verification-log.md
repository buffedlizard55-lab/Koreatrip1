# Verification Log — Korea Trip Itinerary (line-by-line)

**Session:** `1fd4f7b3` · **Date of verification:** 2026-10-21 · **Rule applied:** a value is
"Verified" only if retrieved from an official source (operator/venue/government/KTO/
Visit Seoul/Visit Busan/MICHELIN Guide). Anything else is left blank and flagged
**Unverified**. All prices from official Korean sources are in **KRW**; every USD figure in
the original itinerary is an unverifiable approximation (exchange rates float) and is
flagged as such site-wide.

Status key: ✅ Verified · ⚠️ Discrepancy/irregularity · ❓ Unverified (no official source)

---

## A. Trip dates

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| A1 | "Day 2: Monday (Nov 2, 2006)" | Weekday/date pairing matches **2026** only: Nov 1 2026=Sun … Nov 9 2026=Mon (calendar computation). "2006" is a typo. | ⚠️ | Calendar (deterministic); trip treated as Oct 31–Nov 9, **2026** |
| A2 | (implicit) No holiday closures checked | South Korea has **no public holidays in November 2026** → all weekly closing days apply normally | ✅ | [Korea Customs Service — 2026 holidays](https://www.customs.go.kr/engportal/cm/cntnts/cntntsView.do?mi=13284&cntntsId=7401), [Visit Korea holidays FAQ](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=140038) |

## B. Transport

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| B1 | AREX "45 min, $7" | Express (non-stop): T1→Seoul Station **43 min**, T2 **51 min**, every 20–40 min, **₩13,000**. All-stop: 59/66 min. "$7" matches neither fare. | ⚠️ time≈ / price ✗ | [Seoul Metropolitan Government](https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/), [AREX](https://www.arex.or.kr/main.do) |
| B2 | Airport Limousine bus "$13" | Route **6015** serves Myeongdong (stops incl. Lotte Hotel/IBIS Myeong-dong, Royal Hotel/Euljiro 1-ga, Myeong-dong Stn): **₩17,000** adult / ₩12,000 child 6–12. Route 6001 also serves the area. | ✅ (₩) / ❓ ($ approx.) | [Airport Limousine Co. — 6015](https://airportlimousine.co.kr/en/sub/sub01.php?cat_no=47) |
| B3 | Bus to N Seoul Tower "31 min" | Namsan Circular Shuttle **01A** (every 9 min) / **01B** (every 14 min), 06:30–23:00, **₩1,500** (transport card only), board at Chungmuro Stn (L3/4) etc. "31 min" not stated by any official source. | ✅ bus / ❓ time | [N Seoul Tower — Getting Here](https://www.nseoultower.co.kr/eng/visit/traffic.asp) |
| B4 | Subway to COEX "47 min" | COEX = Line 2 **Samseong Stn** / Line 9 Bongeunsa Stn; hotel is by Line 2 Euljiro 1-ga → Line 2 direct. Duration not officially published. | ✅ route / ❓ time | [Visit Gangnam (official)](https://www.visitgangnam.net/en/places/coex-tourists-favorite-one-stop-attraction), [Seoul Metro](https://www.seoulmetro.co.kr/en/) |
| B5 | KTX Seoul→Busan "2 h 45 min" | Journey time & fare are **train-specific**; must be checked in Korail's official booking at purchase. No single official figure published. | ❓ | [Korail official booking (EN)](https://www.korail.com/global/en/main) |
| B6 | "Board KTX 45 min early for luggage space" | Traveler's own note; no official requirement found. | ❓ (note, not fact) | — |
| B7 | Taxi ICN↔Myeong-dong (background) | Official estimate table: 80–90 min, ₩47,000–52,000 (+ ₩7,900 expressway toll) | ✅ | [Seoul Metropolitan Government](https://english.seoul.go.kr/service/entry/getting-to-seoul-from-incheon-airport/) |

## C. Hotels

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| C1 | Stanford Hotel Myeongdong | Centerpoint Bldg, Namdaemun-ro 2-ga, Jung-gu (across from Lotte Dept Store Main); **check-in 15:00 / check-out 12:00**; luggage storage pre-check-in & post-check-out (collect by midnight same day); official airport directions = bus 6015 (~90 min, ₩17,000, get off Ibis Myeongdong) | ✅ | [Stanford Hotel Myeongdong — official FAQ](https://www.stanford-hotel.com/myeongdong/en/contents/list/faq) |
| C2 | "Check out of Stanford by 12:00pm" (Day 9) | Check-out **until 12:00** | ✅ | same as C1 |
| C3 | L7 Haeundae Lotte Hotel | **L7 HAEUNDAE by LOTTE HOTELS**, 55 Haeun-daero 570beon-gil, Haeundae-gu, Busan; check-in 15:00. Check-out: official **EN** pages say **11:00**; official KO/ZH pages say **12:00** (11:00 in Jul–Aug) | ⚠️ official-source conflict | [LOTTE Hotels — L7 Haeundae (EN room page)](https://www.lottehotel.com/haeundae-l7/en/rooms/standard-queen) |

## D. Attractions — hours, tickets, closures

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| D1 | "Namsun Tower" observatory "10:00-10:30 (entry until 10:00)" | **N Seoul Tower** (Namsan) Observatory: **weekdays 10:00–22:30, weekends/holidays 10:00–23:00**; last entry 30 min before close; open 365 days. Nov 2 2026 = Monday → 10:00–22:30, last entry 22:00. Name misspelled ("Namsun"). | ⚠️ (name + ambiguous times, then verified) | [N Seoul Tower official — Hours](https://www.nseoultower.co.kr/eng/visit/use.asp) |
| D2 | Cable car + observatory "$31 each" | Observatory **₩29,000** (13+) + Namsan Cable Car round-trip **₩15,000** = **₩44,000/person**. Sold separately by different operators. $31 unverifiable. | ✅ (₩) | [N Seoul Tower — Fees](https://www.nseoultower.co.kr/eng/visit/use2.asp), [Visit Korea — Namsan Cable Car](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=96828) |
| D3 | Cable car hours "10:00-10:30" | **10:00–23:00** daily (last tickets: RT 22:30 / one-way 22:45); weather suspensions possible | ⚠️ claim off | [Visit Korea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=96828), [Namsan Cable Car official](https://www.cablecar.co.kr/) |
| D4 | Day 2 says "Take bus" **and** prices cable car | Bus 01A/01B goes to the tower directly (no cable car needed); cable car is the alternative. Pick one. | ⚠️ internal inconsistency | [N Seoul Tower — Getting Here](https://www.nseoultower.co.kr/eng/visit/traffic.asp) |
| D5 | Gyeongbokgung hours Nov–Feb 9:00–17:00, last adm. 16:00, closed Tuesdays | **Nov–Dec 09:00–17:00, final admission 16:00; CLOSED TUESDAYS** (moved only if Tue is a public holiday — Nov 3 2026 is not) | ✅ hours — but see D6 | [Gyeongbokgung Palace official](https://www.royalpalacekr.org/html/eng_gbg/guide/guide01_tab01.html) |
| D6 | **Day 3 = Tuesday Nov 3 → Gyeongbokgung plan** | **Palace is CLOSED on Day 3.** Guard ceremony also does not run. Itinerary contradicts its own note. | 🚨 **CRITICAL CONFLICT** | same as D5; holiday check A2 |
| D7 | Guard ceremony 10:00 & 14:00 | Royal Guard Changing Ceremony **10:00 & 14:00** (20 min); Guard Duty 11:00/13:00; Training 09:35/13:35; **except Tuesdays** | ✅ | [Korea Heritage Service agency (kh.or.kr)](https://www.kh.or.kr/cms/content/view/824) |
| D8 | Admission 3,000 KRW (~$2.30); "Free for under 19 and over 65" | Age 19–64 **₩3,000**; age 7–18 **₩1,500** (NOT free); free = age ≤6 and ≥65 | ⚠️ free-age claim wrong | [Gyeongbokgung Palace official](https://www.royalpalacekr.org/html/eng_gbg/guide/guide01_tab01.html) |
| D9 | "Time needed 3–4 hours" | Opinion/estimate; not an official figure | ❓ (estimate) | — |
| D10 | Bukchon Hanok Village (no hours given) | **Red Zone (Bukchon-ro 11-gil): tourist visits only 10:00–17:00**; 17:00–10:00 entry restricted, **fine ₩100,000** (enforced since Mar 1 2025) | ✅ (important missing constraint) | [Seoul Metropolitan Government notice](https://english.seoul.go.kr/notice-on-restrictions-for-tourist-visits-to-bukchon-special-management-area-effective-from-november-2024/) |
| D11 | DDP listed under "Seongsu" day with Seongsu description | DDP is in **Dongdaemun** (281 Eulji-ro, Jung-gu), hours **10:00–20:00**, closed Jan 1/Seollal/Chuseok days. "Converted industrial warehouses" describes Seongsu, not DDP. | ⚠️ wrong district/description | [DDP official](https://www.ddp.or.kr/), [Visit Korea — DDP](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=67162) |
| D12 | Starfield COEX Mall ("Starfiel") | **10:30–22:00 daily**, open year-round (varies by store), 513 Yeongdong-daero, Gangnam-gu | ✅ | [Starfield official](https://www.starfield.co.kr/coexmall/main.do) |
| D13 | Photo with Gangnam Style statue | Bronze statue on plaza outside **COEX East Gate** (outdoor, no ticket/hours) | ✅ | [Visit Gangnam (Gangnam-gu official tourism)](https://www.visitgangnam.net/en/places/coex-tourists-favorite-one-stop-attraction) |
| D14 | Gwangjang Market "Hours: 9:00-11:00pm (some stalls until 2:00 a.m.)" | Food alley **09:00–23:00 daily, year-round**; general market 09:00–18:00 (closed Sun); vintage 10:00–19:00. "Until 2 a.m." not supported officially. | ⚠️ ambiguous/wrong as written | [Visit Korea — Gwangjang](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=106345), [Visit Seoul — Gwangjang](https://english.visitseoul.net/shopping/Gwangjang-Market/ENP000286) |
| D15 | Mangwon Market alternative | **10:00–21:00 daily** (varies by store), 27 Poeun-ro 6-gil, Mapo-gu; Line 6 Mangwon Stn Exit 2 | ✅ | [Visit Seoul — Mangwon](https://english.visitseoul.net/shopping/Mangwon-Market/ENP037950) |
| D16 | Haeundae Market (Day 9 evening) | **09:00–22:00** (varies by store), open year-round, 22-1 Gunam-ro 41beon-gil, Haeundae-gu | ✅ | [Visit Busan official](https://www.visitBusan.net/index.do?menuCd=DOM_000000301003001000&uc_seq=294&lang_cd=en), [Visit Korea](https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=84963) |

## E. Shopping hours

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| E1 | Lotte/Shinsegae "10:30–8:00pm weekdays, 10:30–8:30pm weekends" | **Lotte Main**: 10:30–20:00, extended days 10:30–20:30. **Shinsegae Main**: Mon–Thu 10:30–20:00, **Fri–Sun & holidays 10:30–20:30** (Fri = extended; itinerary's weekday/weekend split is a simplification) | ⚠️ mostly right, Fri detail wrong | [LOTTE official](https://global.lotteshopping.com/eng/store/main?cstrCd=0001), [Visit Korea — Shinsegae Main](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=106990) |
| E2 | "Olive Young 8:00–12:00am" | Olive Young **Myeongdong Town** flagship: **10:00–22:30 daily** (53 Myeongdong-gil) | ⚠️ claim incorrect | [Olive Young official store page](https://myeongdongtown.oliveyoung.com/) |
| E3 | "Major brands 10:00–10:00pm" | Generic claim; no official source covers "major brands" collectively | ❓ | — |
| E4 | "Street food stalls 11:00–10:00pm, some until 11:00pm" | No official hours exist for Myeongdong street stalls | ❓ | — |
| E5 | Blue Elephant (Seongsu) | Seongsu flagship: **Mon–Sun 12:00–22:00**, 2–3F 13 Yeonmujang-gil | ✅ | [Blue Elephant official](https://blueelephant.co/product/seongsu-flagship-store/3725/) |
| E6 | "Musina Standard" | Correct name **Musinsa Standard**; Seongsu store **11:00–21:00 daily**, 83 Yeonmujang-gil 1–2F | ⚠️ name misspelled | [Musinsa official store locator](https://locations.musinsa.com/ko/stndss) |
| E7 | "Marge Sherwood" | Correct styling **MARGESHERWOOD**; Seoul flagship (Seongsu) **11:00–20:00 daily**, 13 Yeonmujang 11-gil | ⚠️ name styling | [MARGESHERWOOD official](https://global.margesherwood.com/pages/stockist-official) |
| E8 | Ader Error (Seongsu) | ADER Seongsu Space, 82 Seongsui-ro; hours conflict across secondary sources (11:00–21:00 vs 13:00–21:00); current hours not retrieved from brand site | ❓ hours | [ADERERROR official](https://adererror.com/) |
| E9 | Brandy Melville (Seongsu) | First Korea store opened Jan 3 2025, 101-1 Yeonmujang-gil (news reports); no official Korea store page/hours retrieved | ❓ hours | [Brandy Melville official](https://www.brandymelvilleusa.com/) |

## F. Food & drink

| # | Itinerary claim | Verified value | Status | Official source |
|---|---|---|---|---|
| F1 | Myeongdong Kyoja "Michelin hand-made dumplings" | Listed in **MICHELIN Guide**; 29 Myeongdong 10-gil; **10:30–21:00 daily**; kalguksu/dumplings, family-run since 1966, price band ₩ | ✅ | [MICHELIN Guide](https://guide.michelin.com/kr/en/seoul-capital-area/kr-seoul/restaurant/myeongdong-kyoja), [official site](https://www.mdkj.co.kr/) |
| F2 | Crystal Jade "Shinsegae Dept Store location – basement" | MICHELIN-listed Crystal Jade is at **B1F 16 Namdaemun-ro 7-gil (Sogong)** — a standalone basement near Myeongdong, **not** inside Shinsegae. Shinsegae-basement branch not confirmed from any official source. Parent group reported in receivership/restructuring (Sep–Oct 2026 news) → re-confirm before trip. | ⚠️ location claim unverified | [Crystal Jade Korea official](https://www.crystaljade.co.kr/display/main.do), [MICHELIN Guide — Crystal Jade](https://guide.michelin.com/kr/en/seoul-capital-area/kr-seoul/restaurant/crystal-jade) |
| F3 | Hongojib "full bbq for 1 for only $10" | Brand exists (solo BBQ/sukiyaki); official site is a franchise page without Myeongdong store hours/prices | ❓ price/hours | [Hongojib official](https://hongojib.com/) |
| F4 | Pig Restaurant 2 (Itaewon) | No official website found (Facebook page only); hours/address from directories only | ❓ | — |
| F5 | Myeongdong Sookhee (bar) | No official website (Instagram @bar.sookhee). Two similarly-named venues (Euljiro original vs "Myeongdong Sookhee") → confusion risk | ❓ | — |
| F6 | Cafe Onion Anguk "arrive before it opens" | **Mon–Fri 07:00–22:00; weekends/holidays 09:00–22:00** (last order 21:30), 5 Gyedong-gil; Anguk Stn (L3) Exit 3 | ✅ | [Cafe Onion official](https://www.onionkr.com/), [Visit Korea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=191156) |
| F7 | Tea house "typically 12:00–9:00, some until 10:00" | No venue named → cannot verify | ❓ | — |
| F8 | Solsot Seongsu "$7–$14, come before opening" | No official website (Instagram @solsot_official); opening time & prices from directories only | ❓ | — |
| F9 | Hanjungsun fruit mochi | No official website found; Seongsu store hours from blogs only | ❓ | — |
| F10 | Caricature (unnamed) | Shop not named. The well-known Seongsu caricature chain is Acorn Caricature (도토리 캐리커쳐) — cannot confirm this is the intended shop | ❓ | — |
| F11 | Eternalog photo booth | Official site confirms Seongsu 2nd store: 1F 101, 14 Yeonmujang 5ga-gil. Hours/price not on official page retrieved | ✅ location / ❓ hours | [Eternalog official](http://eternalog-fotobooth.com/) |
| F12 | Cafe Far Ben (pistachio latte) | Instagram-only (@cafe.farben); reported hours conflict (10:00–20:30 vs –21:00) | ❓ | — |
| F13 | Cafe Onion (Seongsu) | Branch exists per brand; Seongsu hours not separately retrieved from official page | ❓ hours | [Cafe Onion official](https://www.onionkr.com/) |
| F14 | Rain Report Cafe (Day 4, Seongsu) | **Rain Report Croissant** (Seongsu): **11:00–22:00** (last order 21:00), open year-round, 32 Seongsui-ro 16-gil | ✅ | [Visit Korea](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=175514) |
| F15 | Rain Report Cafe (Day 6, "Insadong") | **Rain Report Rainbow** is in **Ikseon-dong** (33-7 Supyo-ro 28-gil): **10:30–20:30 daily**; Jongno 3-ga Stn (L5) Exit 4, 280 m | ✅ (district label corrected) | [Visit Seoul](https://english.visitseoul.net/restaurants/rainreport/ENP933ykf) |
| F16 | Jayeondo salt bread "$8.77 for 4" | No official website (Instagram only); 4-piece set widely reported at ₩12,000 — not from an official source | ❓ | — |
| F17 | Break Silence (Seongsu, R&B/cocktails) | Brand official site exists; venue hours not published on it | ❓ hours | [Break Silence official](https://break-silence.com/about) |
| F18 | Chuncheongol Dakgalbi (Seongsu dinner) | 춘천골 닭갈비 listed in Seongsu (NOL directory); no official website/hours | ❓ | — |
| F19 | "Uri Wang Galbitang — Gangdong. Favorite of Ikseon-dong" | Could not identify a restaurant of this exact name in Gangdong from any source; the "Favorite of Ikseon-dong" tag belongs to a different restaurant (F20) → note appears garbled | ⚠️ unidentified | — |
| F20 | Day 6: "Chwihyang" **and** "Favorite of Ikseon" as if separate; pork belly rose pasta "$14.50" | Both names = **same restaurant**: Ikseon Chwihyang (익선취향), listed on CatchTable as "Favorite Ikseon", 17-32 Supyo-ro 28-gil. **Duplicate listing.** Price/hours: no official source (pasta widely reported ₩18,900) | ⚠️ duplicate / ❓ price+hours | — |
| F21 | "Soul Market" pastries & coffee (COEX) | **SOUL MARKET Bakery**, COEX Mall B1 I101 (directories); hours not from official source (Instagram @soul_market_bakery) | ❓ hours | [Starfield COEX official tenant search](https://www.starfield.co.kr/coexmall/main.do) |

## G. Missing / unplanned items

| # | Item | Finding | Status |
|---|---|---|---|
| G1 | SFO→ICN flight | No airline/flight number/times in itinerary → nothing to verify; Day 1 arrival logistics depend on it | ⚠️ missing info |
| G2 | Day 7 (Sat Nov 7) | Only the word "Itaewon" — no venues/times | ⚠️ unplanned |
| G3 | Day 8 (Sun Nov 8) | Completely blank | ⚠️ unplanned |
| G4 | Return travel after Day 9 | Trip document ends at Busan check-in; no Busan itinerary or departure details | ⚠️ incomplete |
| G5 | "uber/taxi" legs (Day 9) | Treated as traveler's plan; no fare/time claims to verify | — |

## Analysis notes (recommendations, clearly labelled as such on the site)

1. **Fix for D6:** swap Day 2 ↔ Day 3. Gyeongbokgung + Bukchon on **Mon Nov 2** (palace open,
   guard ceremony runs, Cafe Onion Anguk opens 07:00 Mon, Bukchon Red Zone 10:00–17:00);
   N Seoul Tower + Myeongdong on **Tue Nov 3** (tower open 365 days; dept. stores open daily).
2. Use either the **01A/01B bus (₩1,500)** *or* the **cable car (₩15,000 RT)** for N Seoul
   Tower — not both (D4).
3. Airport arrival: hotel's own official guidance for Stanford Myeongdong is **bus 6015**
   to "Ibis Myeongdong" stop (₩17,000) — simpler with luggage than AREX + transfer.
4. Verified-price subtotal (per person, list prices, excl. KTX/food/shopping):
   AREX Express ₩13,000 *or* bus ₩17,000; tower+cable car ₩44,000 *or* tower+bus ₩30,500;
   palace ₩3,000.
5. Empty Day 7/8 can absorb already-researched options with verified hours (Mangwon Market,
   DDP, palace if the swap is declined — but **not** on a Tuesday — Haeundae items are Day 9+).
