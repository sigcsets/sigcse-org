# Ownership and isolation (Phase 2)

`ownership.csv` classifies every tracked/proposed file, excluding ignored local
material. Regenerate with `python scripts/ownership.py`. Original inventory URL
estimates are reference metadata; the rendered Phase 1 baseline is authoritative.

Organizational material stays integrated. The six conference series are separately
identified with a transfer manifest listing their files, public URLs and shared
dependencies. The concise directory is `_data/conferences.yml`; during Phase 2 its
`schedule_source` references the existing authoritative series schedule, avoiding a
second editable copy. Phase 3 will isolate sources behind explicit permalinks.

## Human ownership review, nonblocking

- Board-approved conference policies (including corporate support, remuneration,
  conflicts and eligibility) remain organizational until authority is confirmed.
- Best paper awards, Working Groups, Doctoral Consortium, conference committees
  and the organizational 50-year timeline mix conference and SIGCSE history.
  Their shared data/pages are not transferred or removed automatically.
- Organization-wide awards displayed within conference years stay in organizational
  data. A future transfer should export the relevant approved snapshot, not assume
  the Steering Committee owns the full award record.
- In-cooperation events, travel grants and Special Projects remain organizational.
- Self-contained Bulletin issues and images remain intact, including duplicates.

No conference content is deleted, externally redirected or newly published. Assets
retain public paths even when page sources move. Transfer manifests are preparation,
not self-contained export packages: required shared templates/assets and record
subsets must be included and verified at the time of an authorized transfer.

## Phase 3 implementation

279 page sources moved behind explicit stable permalinks. Conference sources live in `content/conference-legacy/<series>/`; organizational sources live in `content/organization/`. Assets and standalone publications retain original paths. Directory schedules now live only in `_data/conferences.yml`; an in-memory compatibility alias preserves existing template consumers without duplicate source records. The four original source defects retain their old diagnostic identities for baseline comparison, even though the Bulletin source moved. Baseline files were not expanded or regenerated.

Existing RESPECT schedule says title 2027, year 2026 and start 2027-06-01; preserve these values and request approved correction. Expired ICER/Virtual schedule entries remain records, not silently replaced events.
