# Clash (formerly CalendER)

A planning tool for **BBYO**: key 2026–27 school dates for the districts where every
region has chapters, so events don't collide with school schedules.

Started with Eastern Region (NC / SC / VA) and now covers **all 36 BBYO regions &
councils** pulled from bbyo.org.

## What's here

- **`app/`** — the Clash web app (open `app/index.html`): region picker, calendar view,
  and an "is this date clear?" conflict checker. Reads `app/data.js`, which is
  auto-generated — run `python3 build.py` after editing the data.
- **`data/regions.json`** — the single source of truth. Each district has its official
  source link and a `verify` flag for dates that still need a check; Jewish day schools
  are tagged `type: dayschool` (✡ badge in the app).
- **`MASTER-CALENDAR.md`** — human-readable master list for Eastern Region (the original
  step-1 dataset).

## Status

**All 36 regions populated** — 359 districts (122 fully verified from official
calendars, 237 flagged ⚠️ for extraction or confirmation), including 47 Jewish day
schools awaiting their 2026–27 calendars (most publish in late summer 2026).

## Next steps

1. Work down the ⚠️ flags: extract scaffolded hub districts from their source links and
   confirm aggregator-sourced dates against official PDFs.
2. Fill day-school calendars as they post (late summer 2026).
3. Add graduation dates when districts publish them (usually spring 2027).
