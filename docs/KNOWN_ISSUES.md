# Known issues after Phases 5–6

The original regression baselines remain unchanged. Live/staging validation reports zero new findings, with 217 original findings remaining: 103 missing internal targets, 78 missing image alternatives, 24 duplicate IDs, seven missing fragments, three missing language attributes, one missing title and one missing h1. These are explicit path-level findings, not blanket exclusions. Four original duplicate YAML keys remain (the Bulletin source now lives under content/organization).

Editorial review remains necessary for 2026 award data, expired travel cycle information, conference listings and governance history. The RESPECT directory record retains conflicting 2027 title/start versus year 2026. No names, citations or missing events were invented. Ambiguous policy/conference ownership is recorded in content/OWNERSHIP.md.

The unused DOI plugin remains an undeclared external CLI/shell dependency if invoked; current source does not use it. Untrusted PRs must build without privileged credentials.

Native Linux builds and browser checks passed. The new Ruby pin is not installed/tested natively on Windows; use the tested WSL environment or install the documented Ruby version. Full accessibility review, screen-reader/zoom/document testing and external link checks remain incomplete. No WCAG certification is claimed.

The remote history has now been replaced with owner authorization, and hosted live/staging CI passes. Pages was disabled with separate owner authorization to prevent automatic publication. No production server was contacted; deployment and hosting investigation are deferred.

Static search and maintainer workflows are implemented. Real volunteer usability testing and visual CMS selection remain follow-on work. The native mobile menu is expanded without JS, and collapsible with JS. Historical tables can scroll within their content area. Original standalone publications retain their old presentation and accessibility limitations.

See REVIEW.md for local review, screenshots and exact validation evidence.

Concept B is approved and implemented site-wide with solid blue navigation. Historical standalone Bulletin publications retain their self-contained presentation. Shared-shell conference legacy pages receive the new identity. Existing reference tables may scroll horizontally within labeled keyboard-focusable regions on small screens.

Conference eligibility changes at build time, so automatic exclusion of concluded events requires a rebuild. No scheduled publication/deployment is enabled. Month-only dates are retained through month end for filtering without inventing a published end date. Missing official CompEd URL and unconfirmed RESPECT details remain editorial questions.

Phase 4C retains inherited benefit/eligibility claims for owner freshness review, the dated membership snapshot, and the conflicting mailing-list count. See OPEN_QUESTIONS.md. Participation pages do not assert new vacancies. ACM renewal is linked from its published guide; authenticated transactions are untested.


Phase 5–6 limits: PDF/Office bodies, OCR, external sites and standalone publication
full text are not indexed. Search year applies to pages, not individual rows in
multi-year lists. Pagefind prefix matching can return broad results for an unknown
single term; category/type/year filters and more specific terms help. Manual
screen-reader/zoom/document review and real volunteer usability tests remain.
The exact inherited March 3, 2014 news date string is preserved with a source/value
exception; new dates are validated. No original regression baseline was expanded.
Visual CMS selection/authentication/media/preview/turnover evaluation is deferred.


## Pages preview checkpoint

The prior Pages-disabled state above is historical. Actions-only preview is now
authorized and deployed at https://sigcsets.github.io/sigcse-org/. All hosted
checks passed in run 45925550271; see PAGES_PREVIEW.md. No deployment blocker
remains. Existing static/editorial/accessibility limitations are unchanged.
Production stays literally disabled; no ACM/DNS/custom-domain/CMS work.
