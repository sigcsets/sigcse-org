# Project status

Updated 2026-11-26. **Current work: authorized Actions-only Pages preview.**
Owner approved Phase 4C and both phases without an intermediate stop. Approved
visual identity, homepage, landing pages and navigation remain frozen except
functional search integration and accessibility. Production stays disabled; the Pages preview is authorized.

## Phases 5–6

Pagefind 1.4.0 is integrated in the reserved header space. A dedicated search page
uses local static assets, useful titles/excerpts, category/record-type/year filters,
conference archive labels and baseurl-aware destinations. Every Jekyll build and
serve rebuild indexes public main content; redirect, navigation and nonpublic
content are excluded. Local browser checks cover real engine queries, full index
inventory, desktop/mobile/320px, keyboard, empty results, axe and browse fallbacks.

MAINTAINING.md provides exact source paths and a PR/preview/review/rollback guide.
CONTENT_TEMPLATES.md documents all nine workflows and fields. Treasurer reports
use YAML/shared rendering; new committee items support Markdown; travel dates
use ISO metadata while preserving approved display dates. Current sources remain
authoritative; history and factual discrepancies are untouched. Expanded validation
has eleven invalid-edit mutation cases, plus advisory freshness reports.
MAINTENANCE_COMPARISON.md distinguishes improvements from prior centralization.
CMS_READINESS.md records remaining obstacles without choosing/installing a CMS.

Local case-sensitive Linux live/staging/preview checks pass: 1,474 output files,
391 HTML pages, all 1,064 original paths/19 redirects preserved, zero new static
findings (217 original). All 679 original non-HTML hashes remain unchanged.
Root/staging search tests pass: 365 pages, three filters, ten tasks each, desktop/
mobile/320px, keyboard, fallbacks and zero axe violations on search. Source checks,
eleven invalid-edit mutations, Markdown metadata, six Python regressions, schedule/
navigation logic, 13 task-depth benchmarks, contrast, packaging and disposable
rollback pass. Direct Phase 4C comparison confirms 365 shared pages preserve main
content, allowing only the new Search link in the generated all-pages index.

Hosted live/staging validation passed for implementation `5ff1c39` in
[run 45922460392](https://github.com/sigcsets/sigcse-org/actions/runs/45922460392).
Review documentation, screenshots, comparisons and limits are in REVIEW.md.
Original regression baselines remain intact. Pages GET still returns 404.
Stop after Phase 6; no Phase 7, production connection, CMS, Pages or DNS change.

## Prior checkpoints

Phase 4C review is preserved in reviews/PHASE4C_REVIEW.md. The records below are
historical context, not current pending authorization.

## Phase 4C — current work

The homepage preserves its hero and Explore section, replacing only upcoming conference presentation with compact chronological cards. Membership leads with community photography, join/renew actions, six shared benefits and participation, followed by the original dated statistics/chart and support links. Conference panels reuse authoritative descriptions/schedules and existing series logos, with text fallbacks. Awards integrate all five original descriptions with nomination/history links and expandable scope/selection guidance. Committees lead with active groups; update history is preserved below. News rows remove orphaned external arrows and use tighter spacing.

Direct benefits are authoritative in the benefits page front matter; complete award directory descriptions are centralized and concise leads are derived. No event schedule is copied. All original benefit/award prose and committee history are preserved. Corrected the committee creation link and previous-count field mechanically. Added required-field validation for new structured metadata. No new dependency or generated/stock image.

Local source, six regressions, conference logic, live build, public preservation, contrast and 13 task benchmarks pass: 1,075 files / 390 HTML pages; all 1,064 baseline paths and 19 redirects retained; 217 original output findings, zero new findings. Staging/preview and desktop/mobile/320px browser checks also pass. Comparison gallery: artifacts/phase4c/index.html. Hosted live/staging validation passed for implementation `572a75f` and review `d8ee652` in [run 45916609423](https://github.com/sigcsets/sigcse-org/actions/runs/45916609423), including packaging and disposable activation/rollback. Eight representative approved reference/program/archive pages have byte-identical rendered main content to Phase 4B. Twenty-four matched before/after screenshot files are verified. GitHub Pages remains disabled (API 404), and no production server was contacted. Stop here for owner review. Editorial review concerns are in OPEN_QUESTIONS.md.

## Historical checkpoints — retained for context

The following records describe earlier phases, not current pending work. Current status and review instructions are above and in REVIEW.md.

## Phase 4B — approved community design

Applied the shared sans-serif community design to organizational pages and retained conference legacy pages. Added purpose-specific funding summaries, award directory/history, compact reference/archive styling, larger Board portraits and distinct existing photographs on home, membership, conferences, governance and About. Removed public prototype controls and redundant logo wording. Search space is reserved without implementing search.

Upcoming conferences are generated chronologically from the authoritative schedule, retain events through their final day, exclude concluded events and separate unconfirmed dates. Historical records remain unchanged. Funding summaries and guidance share page metadata rather than independently copied facts. See REVIEW.md for evidence and review instructions.

Clean case-sensitive Linux source, six regression tests, schedule/navigation logic, live/staging/preview builds, public preservation, 13 task benchmarks and palette contrast checks pass. Output: 1,075 files / 390 HTML pages; all 1,064 baseline files and 19 redirects retained; 218 existing static findings, zero new findings. Original baselines are unchanged. Browser review and hosted validation are recorded in REVIEW.md.

Remaining review: missing CompEd event URL, RESPECT conflicting year/TBD dates, expired travel cycles, existing award/governance discrepancies, photography opportunities and full accessibility review. Stop here for owner/Board review; no Phase 5, CMS or production work.

Hosted verification: commits `1273f39` (implementation) and `54e0087` (review documentation) were pushed to authorized `main`. Both live and staging jobs passed in [run 45900546242](https://github.com/sigcsets/sigcse-org/actions/runs/45900546242), including source/logic/regression checks, URL/link checks, preview packaging and disposable release/rollback verification. On resuming after the usage interruption, the working tree was clean and local/remote HEAD matched; completed implementation and screenshots were preserved. The local screenshot gallery contains 28 desktop/mobile images. No production connection or publication occurred.

## Phase 2 — content ownership and isolation

Created a complete source ownership inventory and six conference transfer manifests in `docs/content/`. Added the concise conference directory schema with validated IDs and references to existing schedule data. Shared policies, awards, Working Groups and other ambiguous cases are documented for later human review. No content or public URL removed; physical isolation follows incrementally in Phase 3.

Validation passed on case-sensitive Linux: 1,064 public files and all 19 redirects preserved with zero new findings. Phase 2 complete.

## Repository access

Configured `origin` as `git@github.com:sigcsets/sigcse-org.git`. Read-only inspection found existing `main` at `36cff9e6` (commit message: “Update CNAME”). Under the owner's nonempty-remote instruction, nothing was pushed or overwritten. Hosted validation awaits a decision about integrating this independent history with that existing repository; local work continues.

## Owner decisions

Existing original-site backup is sufficient; retain regression baselines, no additional owner-managed archive required. Ordinary pushes authorized subject to nonempty-remote restriction. Stop at Phase 4 for review. No production changes, paid services, CMS, or substantive factual corrections authorized.

## Phase 3 — repository and templates

Moved 279 published page sources into organizational and per-conference directories with explicit unchanged permalinks. Centralized six schedules. Added a shared HTML shell with page titles, h1, skip link, correct byline handling and archive labels. Removed duplicate active Bootstrap/CDN/jQuery/Holder loads after checking references; retained all old public assets and standalone publications. Updated maintainer paths and regenerated ownership/transfer manifests. Validation passed on clean Linux: all 1,064 public files and 19 redirects preserved; zero new findings and 364 remaining original findings (497 resolved by the shared shell). Six regression tests pass. Phase 3 complete; proceeding to Phase 4.

## Phase 4 — completed for owner review

Implemented a coherent responsive visual system across shared-shell pages, task-oriented primary/section navigation, a new organizational homepage and five new hubs (conference directory, funding, governance, involvement, conference archives). Board display and news archive are responsive and semantic. Conference records retain their old URLs, with archive labels. Schedules, citations, historical data, documents and assets are preserved. Minimal local menu behavior progressively enhances native details; official logo artwork is unchanged.

Validation passed: live, staging and preview on case-sensitive Linux; 1,064 original public files and 19 redirects retained, 1,071 current output files/390 HTML pages, zero new static findings. Existing findings reduced from 861 to 218; baseline files unchanged. All six regression tests and 13 task-depth checks pass. Browser checks at desktop, mobile and 320px cover ten representative pages with no document overflow, one h1 and no broken images. Native menu keyboard/Escape and skip-link focus passed. Twenty after and ten before screenshots are available in artifacts/screenshots with an internal gallery. Original non-HTML asset/download hashes are unchanged; 256 relocated prose bodies were directly compared unchanged, with deliberate homepage/Board/news/policy-index/Special-Projects presentation changes documented.

README, MAINTAINING, BUILD, REVIEW, ownership inventory and transfer manifests are current. No production connection, deployment, DNS/hosting change, paid service or visual CMS. No push because the supplied remote already has history. Hosted CI is therefore unverified. Search and subsequent phases have not begun.

Next: owner review using docs/REVIEW.md and the local preview at http://127.0.0.1:8765/. Decide GitHub-history integration and approve any editorial corrections. Stop at this Phase 4 checkpoint; no further phase is started.

## GitHub authorization and Phase 4B

Owner approved the Phase 2–4 engineering and navigation work but did not approve the visual design. Owner authorized replacing disposable remote history with force-with-lease. Pages inspection showed legacy publication from main/root to preview.sigcse.org; after a separate explicit authorization, Pages was disabled before pushing, preventing publication. Local and remote main now track the modernization history. Both hosted live/staging validation jobs passed for Phase 4 (run 45895218253). DNS unchanged; production deployment remains disabled. See GITHUB.md for the previous Pages configuration and exact verification.

Prepared three meaningfully different isolated homepage + Special Projects concepts: academic/editorial, welcoming photographic community, and compact blue organizational portal. Sources and curated 35-asset inventory are under docs/design/phase4b; generated gallery and six desktop screenshots are under artifacts/phase4b. All six concepts passed desktop and mobile overflow/image/h1 checks. Existing public Jekyll implementation, metadata boundaries, navigation architecture, source organization, assets and baselines are unchanged. Full-site visual refinement and Phase 5 are not started. Stop for owner selection.


## Authorized GitHub Pages preview (2026-11-26)

Phases 5–6 are approved. The owner explicitly authorized Actions-only publication
to https://sigcsets.github.io/sigcse-org/ (no custom domain). This supersedes earlier
Pages-disabled checkpoint notes for this preview only. Main pushes and manual
dispatch publish only after the pinned live/staging/Pages validation and real
search tests pass. PRs/other branches cannot deploy. Only the gated deployment job
receives Pages/OIDC write, with serialized deployment concurrency.
Use _config_live.yml plus _config_github_pages.yml, the complete Pagefind bundle,
public-output validation, preview indicator/noindex and CNAME removal/rejection.
Existing live/staging/local configs are preserved. ACM production remains
literally disabled. No ACM contact, DNS/custom domain, visual redesign, substantive
editorial corrections or CMS work is authorized. Perform actual hosted smoke tests,
report evidence/blockers and stop for owner review. See docs/PAGES_PREVIEW.md
(PAGES_PREVIEW.md from this docs directory) for operation and evidence.
