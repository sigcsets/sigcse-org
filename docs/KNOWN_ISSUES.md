# Known issues and coverage

## Existing defects, preserved

- Output baseline: 861 unique findings across 385 HTML files: 106 missing internal
  targets, 109 missing fragments, 222 missing image alt attributes, 360 missing h1,
  24 duplicate IDs, 21 missing language attributes, 19 missing titles. Exact paths
  and targets are in `baselines/known-output-issues.json`; no blanket site exclusion.
- Four duplicate YAML keys remain: `files` in `_data/specialprojects.yml`,
  `attendance` and `website` in `_data/symposia.yml`, `comment` in `about/bulletin.md`.
  Resolving competing values may affect historical output; review individually.
- Existing mixed-case October 2026 Bulletin links, missing conference annual pages,
  repeated committee directory links and other broken references are now captured
  by rendered checks. Do not infer server fixes or silently change records.
- Award announcement/data disagreement, stale upcoming conferences and role/history
  inconsistencies remain editorial questions. No facts or approved citations changed.
- The unused DOI plugin still relies on an undeclared absolute external CLI and
  unsafe shell interpolation. Current content does not call it; future use requires
  replacement/review. PR build code must remain isolated without secrets.

## Phase 1 limits

- No configured remote: GitHub-hosted Actions execution and branch protection could
  not be exercised. Equivalent build/validation commands run locally on Linux.
- New pinned build tested on Ubuntu 22.04 WSL's case-sensitive filesystem. Native
  Windows baseline tested with its old installed environment; a native Windows
  Ruby 3.3.14 build remains untested. Windows lock entries are included.
- Static accessibility smoke checks do not cover contrast, keyboard/focus, screen
  readers, mobile/zoom, dynamic menus or document accessibility. No WCAG claim.
- External link availability, production parity, server redirects/case handling,
  remote deployment, HTTP verification and ACM rollback remain untested.
- Not all content types have full semantic schemas. Source syntax and initial
  fields/IDs/dates are checked; broader schemas are later-phase work.
- Output hashes can differ from the initial Windows baseline due to line endings,
  footer build time and dependency upgrades. Reports expose those changes for review.
- Local baseline snapshots and unpublished directories are absent from fresh clones.
  Retain generated preservation evidence separately in approved internal storage.

See [BUILD.md](BUILD.md) for exact validator scope and [DEPLOYMENT.md](DEPLOYMENT.md)
for deployment prerequisites. Existing defects are not approval to delete history.

Cross-runtime inspection found equal-key sort ordering differences on six pages
(`about/update`, best papers, Working Groups, ACM grades, Outstanding Educator
recipients and the page index). No records/citations were removed; the existing
maintenance page also changes first-list-item paragraph wrapping after reordering.
The other byte differences normalize away with line endings.
