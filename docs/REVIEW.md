# Phase 5–6 owner review checkpoint

> Accepted working checkpoint (2026-11-26): the owner approved the [hosted preview](https://sigcsets.github.io/sigcse-org/). Earlier review-stop/Pages-disabled statements below describe historical evidence, not pending approval. Board/editorial and full manual accessibility review remain. Current handoff: [PROJECT_STATUS.md](PROJECT_STATUS.md).

The owner approved Phase 4C and authorized Phases 5–6 together. The approved
visual identity, main navigation, homepage and landing page designs are preserved.
Search occupies the reserved header location; mobile adds a full-width search row.
No CMS, production deployment, GitHub Pages, paid service or DNS change.

## Preview and screenshots

Build with the pinned tools in BUILD.md: `bundle exec ruby scripts/build.rb preview`,
then `python scripts/preview.py`. Open http://127.0.0.1:8765/search/ or use the header
on any normal page. The homepage and all existing paths remain available.

Desktop/mobile search and header-integration screenshots are in the local
`artifacts/search/` directory, with a gallery at `artifacts/phase56/index.html`.
Staging captures/results are in `artifacts/search-staging/`. Generated artifacts
are excluded from Git and public output; hosted CI uploads the same screenshots
and reports with its preview artifact. Phase 4C review is archived at
`reviews/PHASE4C_REVIEW.md`; its original comparison screenshots remain intact.

Try these tasks: Special Project; Henry Walker travel; Mitchel Resnick; Board
Meeting Minutes; Bylaws with Policies filter; Technical Symposium; membership;
2010 with Conference legacy and Year=2010 filters; Brian Dorn with Governance;
committees. Results provide page titles, marked excerpts and stable same-host
links. Category/type labels separate news, organizational pages and conference
archives. Filters are keyboard operable. Clearing a query, no-result feedback,
no-JavaScript browse links and missing-bundle fallback are covered.

## Maintainer review

Start with the root MAINTAINING.md. It maps every routine task to exact files,
explains GitHub edit → PR → checks → artifact preview → review/merge, and explains
how to revert an incorrect change. CONTENT_TEMPLATES.md contains copyable examples,
required fields, upload paths and common errors for all nine requested workflows.
MAINTENANCE_COMPARISON.md shows before/after file counts and actual simplifications.

Most authoritative sources were already centralized in prior phases. This work
retains them, adds systematic guidance/validation, replaces Treasurer HTML links
with title/url YAML, supports Markdown for new committee items, and standardizes
travel deadline metadata while preserving date display and all historical facts.
Eleven invalid-edit mutations cover the main editing errors. Advisory freshness
reports flag past schedules/deadlines and missing event URLs without changing them.

## Validation evidence

Final local and hosted run details are recorded below. The
existing source/output/public-file/redirect baselines must remain byte-for-byte
unchanged. All 1,064 original public paths and 19 redirects must remain available,
with no new static findings. Search adds one public page and generated bundle files.

Search validation enumerates every indexed URL and tests titles, existing targets,
no redirect/private/self results, all filters and ten top-ten destination benchmarks.
Browser tests cover root/staging base URLs, desktop, 390px mobile, 320px, keyboard,
axe WCAG 2.2 AA rules, script failure and no-JavaScript fallback. Rank and timing
are recorded in results.json; timing is a local diagnostic, not a service SLA.
Existing six Python regressions, source checks, conference/navigation logic,
13 task-depth benchmarks, contrast, packaging and disposable rollback remain.

## Limitations and next review

PDF/Office body text, OCR, external conference sites/ACM DL, and standalone
historical publication full text are not indexed; public linked titles/HTML metadata
remain discoverable where present. Multi-year listings are one result; Year refers
to page metadata, not each record inside it. Some Pagefind prefix matches are broad;
filters and specific phrases help. Index/current schedules change only on rebuild.
SEARCH.md describes scope, operation and implementation decisions.

Screen-reader/zoom/slow-network/document review and real volunteer usability tests
remain. Existing 217 historical static findings, four duplicate YAML keys, missing
award records and disputed conference/governance facts remain documented rather
than silently corrected. No WCAG conformance certification is claimed.

CMS_READINESS.md recommends a narrowly scoped, owner-approved Git-backed editor
comparison and news/conference pilot with two volunteers. Authentication, review
permissions, previews, media/date/HTML round trips, account turnover and costs must
be evaluated before selection. No CMS has been selected or installed.

Stop for owner review after Phase 6. Production readiness, hosting enablement,
conference transfers and factual corrections need separate authorization.


## Local completion evidence

Case-sensitive Linux live/staging/preview source builds pass: 1,474 output files,
391 HTML pages, all 1,064 original paths and 19 redirects preserved; 217 existing
static findings and zero new findings. All 679 original non-HTML asset/download
hashes match the preservation baseline. No regression baseline changed.

Root and /.staging browser suites pass: 365 indexed public pages, three filters,
ten successful search tasks each, keyboard header/filter controls, empty results,
missing-script fallback, no-JavaScript browsing, desktop/mobile/320px screenshots,
zero page/request errors and zero axe WCAG 2.2 AA rule violations on search.
Expected destinations rank 1–6; conference directory ranks second for Technical
Symposium. All six Python regressions, eleven invalid-edit mutations, conference/
navigation logic, 13 task-depth checks and palette contrast pass. New Markdown
committee metadata is accepted in memory. Eight advisory freshness findings retain
expired/unconfirmed records for human review. Packaging/integrity and disposable
release activation/rollback pass without production access.

Hosted live/staging validation passed for `5ff1c39` in
[run 45922460392](https://github.com/sigcsets/sigcse-org/actions/runs/45922460392), including search/browser checks,
packaging and disposable activation/rollback. Pages GET returned 404 both before
and after the push; production deployment remains disabled.

Direct comparison against a rendered `2ed6186` Phase 4C checkpoint verifies all
365 shared pages retain their main content after normalizing whitespace,
search-only attributes and equivalent preview/site URLs. The sole visible content
addition is Search SIGCSE in the generated all-pages index. Full evidence is
`artifacts/phase56/reference-preservation.json`. Header search is the authorized
functional addition; approved landing/home designs and historical wording remain.

Implementation commit: `5ff1c39`. This checkpoint documentation is committed
separately. Stop here for owner review; no next phase has begun.


## Completed Pages preview — owner review checkpoint

Phases 5–6 approved; authorized preview is live at
https://sigcsets.github.io/sigcse-org/. Manual dispatch of implementation efd5693
passed every job in [run 45925550271](https://github.com/sigcsets/sigcse-org/actions/runs/45925550271): live, staging,
github-pages, deploy-pages and actual hosted-smoke. Automatic main publication
was also verified in run 45924528803. Superseded runs were cancelled; the initial
hosted image timing assertion was corrected without a site/design change.

Hosted coverage: 12 pages at 1440/390/320px, seven primary navigation links,
conference listings, award recipients, Board minutes, two PDF downloads matching
preservation SHA-256 values, all 19 redirects, historical conference pages,
365 indexed pages, 10 search tasks, three filters, keyboard/fallbacks, zero axe
violations on search, successful WASM loading and 19 forbidden paths returning 404.
No browser script errors or document overflow. Actual desktop/mobile screenshots
and JSON reports are in the run's hosted-smoke artifact (seven-day retention).

Artifact checks: 1,475 files / 391 HTML pages, all 1,064 baseline public URLs
preserved, 217 inherited static findings and zero new findings. Pages settings:
workflow mode, built, HTTPS enforced, cname null. Environment allows only main.
ACM deployment's literal false guard and all existing configs/content/design CSS
remain unchanged; no DNS/custom domain, production operation or CMS work.

No remaining preview deployment blocker. Existing 217 static findings, editorial
questions, PDF-body search limitations and full manual accessibility review remain
unchanged. Stop here for owner review; no subsequent phase is started.
