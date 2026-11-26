# Project status

Updated 2026-11-26. **Current checkpoint: Phase 4B implementation complete; owner review required.** Concept B approved with Concept C's solid blue navigation. Production deployment remains disabled; no hosting/DNS/credential investigation. Phase 5 has not begun.

## Phase 4B — approved community design

Applied the shared sans-serif community design to organizational pages and retained conference legacy pages. Added purpose-specific funding summaries, award directory/history, compact reference/archive styling, larger Board portraits and distinct existing photographs on home, membership, conferences, governance and About. Removed public prototype controls and redundant logo wording. Search space is reserved without implementing search.

Upcoming conferences are generated chronologically from the authoritative schedule, retain events through their final day, exclude concluded events and separate unconfirmed dates. Historical records remain unchanged. Funding summaries and guidance share page metadata rather than independently copied facts. See REVIEW.md for evidence and review instructions.

Clean case-sensitive Linux source, six regression tests, schedule/navigation logic, live/staging/preview builds, public preservation, 13 task benchmarks and palette contrast checks pass. Output: 1,075 files / 390 HTML pages; all 1,064 baseline files and 19 redirects retained; 218 existing static findings, zero new findings. Original baselines are unchanged. Browser review and hosted validation are recorded in REVIEW.md.

Remaining review: missing CompEd event URL, RESPECT conflicting year/TBD dates, expired travel cycles, existing award/governance discrepancies, photography opportunities and full accessibility review. Stop here for owner/Board review; no Phase 5, CMS or production work.

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
