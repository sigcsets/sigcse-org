# Known issues after Phase 4

The original regression baselines remain unchanged. Live/staging validation reports zero new findings, with 218 original findings remaining: 104 missing internal targets, 78 missing image alternatives, 24 duplicate IDs, seven missing fragments, three missing language attributes, one missing title and one missing h1. These are explicit path-level findings, not blanket exclusions. Four original duplicate YAML keys remain (the Bulletin source now lives under content/organization).

Editorial review remains necessary for 2026 award data, expired travel cycle information, conference listings and governance history. The RESPECT directory record retains conflicting 2027 title/start versus year 2026. No names, citations or missing events were invented. Ambiguous policy/conference ownership is recorded in content/OWNERSHIP.md.

The unused DOI plugin remains an undeclared external CLI/shell dependency if invoked; current source does not use it. Untrusted PRs must build without privileged credentials.

Native Linux builds and browser checks passed. The new Ruby pin is not installed/tested natively on Windows; use the tested WSL environment or install the documented Ruby version. Full accessibility review, screen-reader/zoom/document testing and external link checks remain incomplete. No WCAG certification is claimed.

The remote history has now been replaced with owner authorization, and hosted live/staging CI passes. Pages was disabled with separate owner authorization to prevent automatic publication. No production server was contacted; deployment and hosting investigation are deferred.

Static search is Phase 5. Comprehensive maintainer schemas/usability and visual CMS evaluation remain later work. The native mobile menu is expanded without JS, and collapsible with JS. Historical tables can scroll within their content area. Original standalone publications retain their old presentation and accessibility limitations.

See REVIEW.md for local review, screenshots and exact validation evidence.

Concept B is approved and implemented site-wide with solid blue navigation. Historical standalone Bulletin publications retain their self-contained presentation. Shared-shell conference legacy pages receive the new identity. Existing reference tables may scroll horizontally within labeled keyboard-focusable regions on small screens.

Conference eligibility changes at build time, so automatic exclusion of concluded events requires a rebuild. No scheduled publication/deployment is enabled. Month-only dates are retained through month end for filtering without inventing a published end date. Missing official CompEd URL and unconfirmed RESPECT details remain editorial questions.
