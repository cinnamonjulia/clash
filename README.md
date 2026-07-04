# CalendER

A planning tool for **BBYO Eastern Region** (NC / SC / VA): key school dates for the
districts where ER has chapters, so events don't collide with school schedules.

## What's here so far

- **`MASTER-CALENDAR.md`** — human-readable master list of 2026–27 dates (start/end of
  school, Thanksgiving, winter break, spring break). Read this first.
- **`data/regions.json`** — the same data in structured form, ready for a future app to
  read. Each district has its official source link and a `verify` flag for dates that
  still need a check.

## Status

**Step 1 (data gathering) — in progress.** 16 districts collected; a few rows still need
verification and two districts (Charleston, Newport News) need their break dates filled.

## Next steps

1. Verify the flagged dates against official district PDFs.
2. Add graduation dates when districts publish them (usually spring 2027).
3. Build a simple, shareable web app that reads `data/regions.json` — calendar view +
   an "is this date clear?" event-conflict checker.
