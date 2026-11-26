# Prioritized improvement opportunities

Audit date: November 26, 2026. All items are proposals; none has been implemented. Priorities reflect repository evidence, not visitor analytics or an approved budget. Retain Jekyll unless a later requirements assessment demonstrates an unmet need.

Complexity: **S** = a focused change, usually 1–3 developer days; **M** = several related changes, roughly 1–2 weeks; **L** = multiple workflows/systems, roughly 3–6 weeks or more. These are planning ranges for implementation and testing after decisions/access are available, not quotes. Board review, archival investigation, content approval, and accessibility remediation can add substantial elapsed time. Impact is qualitative.

## Prioritized work

| ID / priority | Proposed outcome and evidence | Complexity / impact | Risks and dependencies | Acceptance evidence |
|---|---|---|---|---|
| R1 / P0 | Establish a reproducible build, preview, publish, and rollback runbook. Evidence: unconstrained `gemfile`, ignored local lock, two custom configs, minimal README, absent tracked deployment workflow | M / Very high | Confirm host, original runtime, credentials/roles, custom plugin need; do not assume this Windows lock matches production | Fresh isolated checkout builds using documented versions; preview matches baseline; approved rollback demonstrated |
| R2 / P0 | Capture rendered URL/redirect/download baseline before restructuring; explicitly decide audit/excluded-file publication rules | M / Very high | Needs working build and host rewrite knowledge; report CSV includes unpublished metadata | Manifest includes posts, pages, static downloads, aliases, case and fragments; all retained URLs resolve in candidate output; audit files excluded from unintended publication |
| R3 / P0 | Reconcile award data, expired upcoming entries, Bulletin case mismatch, committee creation link/count, and volunteer-status inconsistencies | S–M / High | Content-owner approval for facts; source observations do not establish current organizational truth | 2026 award page/news agreement; current/upcoming status correct; links checked on case-sensitive output; role discrepancies resolved or explicitly historical |
| R4 / P1 | Add CI checks and preview-based review, with readable failures | M / Very high | R1/R2; choose Git host and build runner; custom-plugin trust model | Build, schemas, internal links/case, record/page parity, redirects, accessibility smoke checks, and output exclusions run for each change |
| R5 / P1 | Improve shared shell: page-specific browser titles/descriptions, `h1`, skip link, labeled navigation/current state, deliberate image alternatives, valid markup | M / High | Baseline visual/URL tests; contrast and assistive-tech review; audit standalone publications separately | Keyboard, screen reader, mobile, zoom/reflow tests pass representative page types; no lost content |
| R6 / P1 | Add static site search with content-type/year filters and a current/archive distinction | M / High | Working post-build stage, title metadata, search-scope decision, PDF policy | Users find a named award recipient, old minutes, policy, conference, and news; staging works; aliases and repeated sidebars do not dominate results |
| R7 / P1 | Simplify navigation around common tasks and provide local section navigation | M–L / High | Board-approved labels; lightweight user testing; R2 URL protection | New and experienced users complete agreed discovery tasks; unchanged public URLs; archive remains visible |
| R8 / P2 | Consolidate conference lifecycle and rendering: one record per event, explicit dates/status/ID, shared detail renderer, validated history page generation | L / High | R2/R4; preserve decimal years and special series fields; choose data schema first | One edit updates upcoming/list/detail displays consistently; historical URLs and proceedings retained; no date-only silent expiry without rebuild |
| R9 / P2 | Define authoritative people/term, award, committee, Bulletin, and document metadata models | L / High | Owner decisions; approved records; preserve archival downloads and version semantics | All current displays derive from agreed sources; historical table/download consistency checked; approved review/effective dates visible |
| R10 / P2 | Pilot a Git-backed visual editor for news and upcoming conferences, then expand | M pilot; L expansion / High | R1/R4; Git identity/authentication, permissions, preview, schema, media conventions, training, budget | Two nontechnical volunteers complete pilot tasks, review previews, submit for approval, and undo a change without editing Liquid/YAML |
| R11 / P2 | Consolidate shared layout shell and remove proven frontend duplication | M / Medium–high | R5 regression coverage; license notices; confirm JS/asset use before deletion | One shared head/footer; one Bootstrap version/source; justified scripts; page types retain behavior |
| R12 / P2 | Optimize display images; assess downloadable-document accessibility | M for images; L/open-ended for archive / Medium–high | Publication owners, original-file preservation, PDF review capacity | Responsive smaller derivatives; originals/URLs preserved where required; prioritized PDFs have accessible text/order/tags or equivalent HTML |
| R13 / P3 | Review excluded local copies and apparent orphans/duplicates; build a preservation catalog | M–L / Medium | Human review, archival policy, backups, logs/backlinks, rendered crawl | Every removal/relocation has an owner decision and retained record/redirect where required; unpublished material stays unpublished |

P0 means establish safe operating knowledge and resolve confirmed high-impact inconsistencies before broad redesign. P1 means the first implementation tranche. P2 builds on that foundation; P3 is deliberate archive stewardship, not a bulk cleanup target.

## Search options

**Recommended candidate: Pagefind.** Its official documentation describes indexing rendered static HTML and shipping a static search bundle, with metadata/filter support and no search server. That fits a Jekyll post-build step while preserving the current hosting model. This is a capability-based recommendation, not an installed or benchmarked solution. See [Pagefind documentation](https://pagefind.app/).

A pilot should index main article content, not repeated navigation/sidebars/footer; attach content type, year, and current/archive metadata; exclude redirects, draft/excluded material, audit reports, and developer assets; and verify `/.staging` asset/result paths. The 124 pages without front-matter titles need useful search-result labels. Test misspellings, full names, acronyms, and long archival queries using a curated set of expected results.

Ordinary HTML indexing does not make local PDF/Office contents searchable. Initially index document landing-page metadata and make this limitation visible. If full-text document retrieval is required, plan extraction/OCR, accessible text review, custom ingestion, and version handling separately; Pagefind documents indexing-library extensibility, but extraction is additional work. Preserve an HTML browse fallback when JavaScript is unavailable.

An alternative design is a Jekyll-generated JSON index with client-side matching. It can avoid a separate indexing stage, but requires owning relevance, result snippets, accessibility, filtering, and index-size performance. Compare prototypes before choosing. Hosted search is worth evaluating only if documented search requirements exceed a static solution and its ongoing cost/privacy obligations are acceptable. No hosted search service is currently established by the repository.

## Git-backed editing interface

**Recommended first candidate for a pilot: Decap CMS**, not a commitment. Its official overview describes a browser editor backed by Git, configurable content types, media upload, and previews, compatible with static site generators. [Decap CMS overview](https://decapcms.org/docs/intro/).

The intended workflow is: an authenticated volunteer edits a form → sees a generated site preview → submits a reviewable Git change → an authorized reviewer approves publication. The editor should preserve ordinary repository files so maintainers retain Git history and can leave the editor later. Hosting and access choices are prerequisites, not incidental setup details.

Start with two narrow schemas:

- News: title, publication date, author, body, related links; stable published slug, safe media picker, preview.
- Upcoming conference: series, stable event ID, title, start/end dates, location, website; a clear procedure for advancing to history.

Do not initially expose raw layouts, plugins, arbitrary Liquid, or large nested data lists to nontechnical editors. YAML fields currently containing HTML strings will need carefully designed widgets or remodeled data. A generic rich-text editor cannot safely explain all existing conventions. Verify serialization of dates, quotes, multiline descriptions, event codes, and CSV-backed history, as well as media size/case checks.

Select authentication/backend from the actual Git host, define who can draft/approve/publish, confirm preview deployment support and costs, and document account recovery and volunteer turnover. If a managed visual editor is desired, run a separate comparison against these requirements; no current pricing, service availability, or SIGCSE purchasing preference has been established here.

## Validation and routine maintenance automation

Recommended checks, staged after a reproducible build exists:

| Check | Concrete rule / example | Handling |
|---|---|---|
| Structured data | Required keys, ISO start/end dates, unique IDs, valid event codes, consistent year types, permitted statuses | Block malformed changes with source-path and field-level errors |
| Cross-display agreement | Award announcement references authoritative award IDs; conference history rows have output pages; Board/download histories agree | Block omissions when deterministic; route factual conflicts to owners |
| Internal links | Crawl generated HTML including data-built links; check file case, images, fragments, staging prefixes, aliases, and redirect cycles | Block new failures; baseline existing archive issues rather than silently ignoring them |
| URL preservation | Compare candidate output to approved baseline; explicit redirect mapping for any approved moves | Block unexpected losses; preserve case-sensitive originals where needed |
| Accessibility | Automated checks for representative layouts and full-site easy-to-detect errors; manual keyboard/screen-reader/reflow checks for shared-shell changes | Automation supports, not replaces, human evaluation |
| Editorial freshness | Past `next-conference`, expired volunteer terms, missing review/effective dates, approaching deadlines | Notify an owner; never automatically delete historical records |
| External links | Scheduled, rate-limited HTTP checks with retry/cache; distinguish timeouts/403/paywalls from confirmed failure | Review report, not automatic deletion or rewriting |
| Asset/output quality | Image budgets, missing alt, missing page metadata, accidental draft/secret/report files, large/unexpected output changes | Block clear regressions; review intentional large archives |
| Dependency maintenance | Pinned environment, deliberate update PRs, vulnerability/compatibility review, fresh full build | Verify actual versions; this audit is not a security scan |

A future weekly editorial check and periodic link scan could be useful, but no automation has been scheduled. Date-aware static displays still need a rebuild to change: determine who owns scheduled builds and what happens on failed runs.

## Sequencing and preservation safeguards

1. Confirm operational facts and content owners; establish R1/R2. Make a read-only preservation copy of local excluded material using an approved destination before future cleanup.
2. Repair approved factual/link inconsistencies and add checks that catch their recurrence (R3/R4).
3. Improve metadata/accessibility, task routes, and search (R5–R7). Measure task completion against the existing site, not visual preference alone.
4. Consolidate data/templates and pilot editing forms (R8–R11), migrating one content type at a time.
5. Optimize media and improve archive stewardship/document accessibility progressively (R12/R13).

Preserve historical records, publication context, dates, citations, and access policies. Menu changes do not require URL changes. Keep existing alias/redirect files unless the host provides verified equivalent redirects. Prefer reversible transformations and side-by-side output comparisons. Never infer obsolescence from an old year, absent literal link, or duplicate hash alone.
