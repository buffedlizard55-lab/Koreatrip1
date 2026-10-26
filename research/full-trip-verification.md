# Full 16-day trip — line-by-line verification log

Session `75247ef9` · Checked 2026-10-26 UTC · Site: `full-trip/` · Data: `full-trip/assets/data.js`

Method: every brief line was extracted into a day step, venue row or transport leg.
A value is "Confirmed" only if seen on an official operator / hotel / government /
tourism-board page (direct fetch or official-domain search excerpt). Reseller and
blog figures were never promoted. Unconfirmed values are blank on the site and
flagged (F-01…F-26). Calendar facts were computed deterministically.

## Calendar (computed, not sourced)

- 2026-10-31 = Saturday; 2026-11-01 = Sunday; 11-02 Mon; 11-03 Tue; 11-04 Wed;
  11-05 Thu; 11-06 Fri; 11-07 Sat; 11-08 Sun; 11-09 Mon; 11-10 Tue; 11-11 Wed;
  11-12 Thu; 11-13 Fri; 11-14 Sat; 11-15 Sun; 11-16 Mon.
  This matches every weekday in the brief except Day 1's "Sunday (Oct 31/Nov 1)"
  wording (F-03) and fixes "Nov 2, 2006" as a typo for 2026 (F-02).

## Directly fetched official pages (this session)

| Fact | Page | Observed |
|---|---|---|
| Sky Capsule hours | bluelinepark.com/eng/skyCapsuleTime.do | Nov (winter) 08:30–18:00; ~30 min one-way; weather caveats |
| Songdo cable car hours | en.busanaircruise.co.kr/info/time | Sep–Nov 09:00–21:00; last ticketing −30 min |

## Official-source excerpts relied on (search-indexed official pages)

- Royal Palaces and Tombs Center (royal.khs.go.kr) + VISITKOREA palace page:
  Nov 09:00–17:00, last admission 16:00, closed Tuesdays, adult ₩3,000,
  guard ceremony Wed–Mon 10:00/14:00. → F-01 critical (Day 3 = Tuesday).
- N Seoul Tower official hours/admission/cable-car pages: observatory
  10:00–22:30 wk / 10:00–23:00 we, last entry −30 min, adult ₩29,000;
  cable car 10:00–23:00, return ₩15,000. → F-04.
- Seoul Metropolitan Government + AREX: Express 43 min ex-T1 / 51 ex-T2, ₩13,000;
  Express serves only ICN↔Seoul Station; all-stop serves Hongik Univ. → F-05, F-23.
- Incheon Airport official train/bus pages: rail at Transportation Center B1;
  bus route search (incl. 6015) with no fare/hotel-stop confirmation. → F-06.
- KORAIL official English booking: used as the booking source only. No train,
  fare or "45-minute boarding" rule is asserted (none selected). → F-17.
- Hotels: L7 Haeundae official (check-in 15:00 / out 11:00, address) — Day 16 matches;
  Accor official Mercure Hongdae (in 15:00 / out 12:00; station ~100 m) → F-22;
  Stanford official + Visit Seoul listing (identity/address only) → F-16.
- Starfield COEX official directions: 10:30–22:00, Samseong/Bongeunsa access.
- BUSAN X the SKY official: daily 10:00–21:00. Fare conflict between VISITKOREA
  (₩29,000) and Visit Busan (₩27,000) → F-14. Klook $17.59 not used.
- SEA LIFE Busan official hours page: wk 10:00–19:00 / we 10:00–20:00, last entry
  −1 h. Fare listings vary → F-15 ("$15" not used).
- Visit Busan Gamcheon: Nov–Feb 09:00–17:00, free. VISITKOREA Nurimaru:
  09:00–18:00 (last admission 17:00), closed 1st Monday, free (Nov 10 open).
- Jagalchi: 05:00–22:00; closures 1st&3rd Tue (VISITKOREA) vs +5th (Visit Busan) → F-20.
- Daritdol: VISITKOREA Sep–Nov 09:00–21:00 vs Visit Busan 09:00–18:00 → F-21.
- Busan Metropolitan City + drone-show organizer: Saturdays year-round,
  Oct–Feb 19:00/21:00, ~12 min, free → F-25 (brief correct).
- VISITKOREA Lotte/Shinsegae main stores; Olive Young Myeongdong Town official
  (daily 10:00–22:30) → F-08, F-09. VISITKOREA Gwangjang sections → F-10.
- DDP official: Dongdaemun complex, 281 Eulji-ro → F-11.
- Seoul Days 1–9 small-venue facts cross-checked to the repo's existing
  `data.js` / `SOURCES.md` (checked 2026-10-21 by session 9c9accaa):
  Café Onion, Jayeondo Seongsu, Rain Report Ikseon, MARGESHERWOOD,
  Blue Elephant, Bukchon red-zone window, Namsan shuttles. Not re-fetched.

## Left blank on purpose (no official value found)

Flights (both directions); airport limo fare/stop; all taxi/Uber times & fares;
all subway/bus ride durations quoted in the brief; KTX train times/fares (none
chosen); Sky Capsule & Songdo cable-car fares (check official booking/price
pages); ~20 small restaurants/cafes/bars (F-19); UNESCO/"Michelin"/queue claims;
every USD price in the brief. Reservations (hotels/trains/tickets): none confirmed.

## Counts

16 days · 52 steps · 31 venue/stay rows · 14 transport legs · 26 flags ·
44 official source links. Statuses: Verified / Partial / Unverified / Conflict.
No row without a source link. No USD conversions computed.
