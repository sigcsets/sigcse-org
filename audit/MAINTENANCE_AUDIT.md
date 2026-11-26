# Maintainer experience audit

Audit date: November 26, 2026. These workflows are reconstructed from source relationships; they were not executed. Publication access, approval practices, build commands, and deployment infrastructure require confirmation. No current visual editor or maintainer runbook was found.

## Common requirements and friction

Even a small edit currently requires locating the source, understanding Markdown/front matter or YAML, preserving links and filenames, checking generated pages, and arranging Git review/publishing. Mixed HTML/Liquid means a rich-text-only edit is not always safe. `README.md` supplies no setup, preview, deployment, or handover procedure. Existing history in this experimental checkout cannot establish the original publication workflow.

`about/update.md` is a useful existing quality-review page: it renders much of the structured data as a long numbered “cheat sheet.” It is not an editing interface, approval system, or validator. It repeats display loops from other pages and contains empty section scaffolding, so maintainers should not treat it as a complete content inventory.

## 1. Add a news announcement

**Files:** create `_posts/YYYY-MM-DD-descriptive-title.md` (or HTML), following a recent post such as `_posts/2026-01-19-SIGCSE-Awards-2026-Announced.md`. Set approved `title`, `date`, optional `author`, then body and links. Post layout defaults come from both config files; `_layouts/post.html` renders it. `index.md` automatically selects the latest five; `news/index.html` automatically lists all posts by year. Navigation normally needs no edit.

**Knowledge:** date-prefixed filenames, YAML quoting, Markdown/HTML, relative versus absolute URLs, Git, preview/publish process. Future-dated behavior must be tested against the intended Jekyll settings. Renaming a published filename can change its public news URL.

**Complexity/duplication:** an announcement can introduce facts that must also be entered elsewhere. The 2026 award announcement exists while award data stops before 2026. Bulletin announcements additionally require issue files and `about/bulletin.md` updates. Named authors currently fail the `page.author == true` display condition in the post layout.

**Future verification:** confirm title/date/byline/body and target URL; check homepage and full archive; ensure announced facts match their authoritative data records. Proposed editor form: title, publication date, author, body, related content, and a preview link.

## 2. Update an upcoming conference

**Files:** the relevant `_data/symposia.yml`, `iticse.yml`, `icer.yml`, `comped.yml`, `respect.yml`, or `virtual.yml`; `_data/events.yml` controls which series appear. Update `next-conference` (title/year/start-date/display dates/location/website), relevant `future-conferences` if present, and the historical `conferences` record when appropriate. For a new historical detail URL, add `events/<series>/<year>.md` using the relevant `*-head.md` include. Add proceeding covers/logos at the paths expected by that include. A promoted homepage banner may require `_data/banners.yml` and an asset under `assets/images/home/`.

**Displays affected:** `_includes/events.html` sidebars, `about/update.md`, home historical lists, series landing/list/cover/detail pages. Updating only `next-conference` does not create a history page or historical record. Updating only the history list does not advance the sidebar.

**Knowledge:** nested YAML, date types/formatting, series-specific image/path conventions, Liquid lookup expectations, and source-to-public `.html` mapping. Different includes derive the year from filenames; maintainers must preserve decimal-year historical identifiers.

**Complexity/duplication:** upcoming and history data are separate; display date strings coexist with sortable `start-date`; some dates have no structured end date. ICER and Virtual still appear upcoming after their 2026 dates. `_data/respect.yml` has a 2026 history record but the tree has no `events/respect/2026.md`; `_data/comped.yml` similarly includes a 2025 history record without `events/comped/2025.md`. Lists assemble those paths dynamically, so record/page parity needs validation.

**Future verification:** sidebar ordering and expiry, series lists, year page and previous/next links, covers, external URL, staging prefix, and calendar wording. A form should edit a single conference record with explicit start/end dates and lifecycle status, while historical URLs remain stable.

## 3. Update Board membership

**Files:** `_data/board.yml` (`current-board` year/term/members), portraits under `assets/images/board/current/`, and `about/board.md` if display structure must change. `about/update.md` also consumes current data. History is separately displayed by `about/board-history/index.md` from `_data/BoardMembers.csv`, with downloadable `about/board-history/BoardMembers.xlsx`. Historical material also exists in `about/board-history/2019-2022.html` and `previous-boards` within `board.yml`. A Board homepage image is independently referenced by `_data/banners.yml`.

**Knowledge:** YAML arrays, exact portrait filenames/case, CSV/spreadsheet editing, history conventions, accessibility alternatives, Git and publication workflow.

**Complexity/duplication:** current membership is already centralized for its two main displays, but historical membership has several representations. The history page uses CSV, not `board.yml`'s previous boards. Moving a row into `previous-boards` alone does not update the public history table or XLSX. Role names vary across terms. Existing floats/fixed widths make layout edits harder than the data edit itself.

**Future verification:** all eight role cards, correct term and contact details, portrait alternatives, historical table and download agreement, mobile reflow, and banner accuracy. Establish which history representation is authoritative before merging formats; preserve each historical term and download URL.

## 4. Add or modify a committee, task force, or Working Group

There are three different systems; first determine which organizational entity is being edited.

| Entity | Source files | Extra knowledge/complexity |
|---|---|---|
| Standing committee/task force initiative | Front-matter `active`/`previous` lists in `programs/committees-task-forces/index.md`; detail/charter/update pages and `reports/` downloads in that directory; creation guidance in `create.md` | YAML containing HTML strings and prose; classification and approved charter; legacy redirects under `programs/committees/` |
| Operational volunteer/conference committee | `_data/organization.yml` or series data `committees` list; rendered by `about/volunteers.md` and `about/update.md` | Nested people/terms/affiliations; different data conventions; ended/current terms are free text |
| Published conference Working Group report | `_data/workinggroups.yml`, consumed by `events/workinggroups/index.md`; any relevant conference guidance/news | Citation, authors, year, conference, proceedings, DOI; a research report is distinct from a standing committee |

**Verified problems:** committee index counts `page.committees` instead of `page.previous`; its creation link resolves to a repeated nonexistent directory. Volunteer data lists the same Information Director as current and previous, while prose and member count disagree. Some current-looking roles have ended terms; owner confirmation is required.

**Future verification:** active/prior section, charter/report download, correct membership/term, organization-wide volunteer listing if applicable, and legacy links. A common people/term model could support operational roles; committee initiatives and published reports should keep their distinct semantics.

## 5. Add an award recipient

**Files:** `_data/outstanding.yml`, `_data/distinguished.yml`, `_data/broadening.yml`, or `_data/testoftime.yml`. The first three generally use name/year/description and an event code such as `TS`; Test of Time uses paper title/citation/DOI/year. Award pages under `programs/awards/` render those lists; `_includes/awards.md` joins the first three by year and event for conference pages. News announcements are separate posts. `programs/awards/early-career.md` currently contains a “yet to be awarded” statement and has no corresponding recipient data file.

**Knowledge:** award category, approved citation, YAML multiline/quote handling, event codes, year types, sorting, and separate announcement workflow. Some records intentionally use `rm-affiliation` while templates read `affiliation`; do not rename those fields without understanding editorial intent.

**Complexity/duplication:** maintaining the news post does not update recipient lists. A missing `awarded` event code can suppress a recipient on conference pages. Broadening Participation can be awarded at a different conference from the other awards; do not assume `TS` for every year. Early-career recipients require designing a model when the first entry is approved.

**Future verification:** approved recipient/year/citation, main award page, event detail, announcement, nomination links, and preservation of `lifetime.html`/`service.html` compatibility redirects. The four 2026 announcement/data disagreements are concrete reconciliation work for content owners.

## 6. Update a policy or organizational document

**Files:** source under `policies/` (Markdown or HTML); `_data/policies.yml` controls titles/descriptions/category lists. `policies/index.md` and series overview pages render selected data categories. For reports/minutes, update the relevant `about/reports/{board,business,chair,treasurer,committee}` source and place the approved document in the existing dated folder conventions. For a committee charter, update its program index/detail link and `reports/` file. Generic legacy downloads also exist under `files/documents/`.

**Knowledge:** distinguish substantive policy approval from web publishing; preserve adoption/effective dates and historical versions; Markdown/HTML, PDF/Office preparation, YAML, link resolution, filename case, accessibility, and Git review. Site-wide footer build date is not evidence of policy approval or review.

**Complexity/duplication:** policy text and catalog metadata are separate, while other documents use manually maintained lists. PDF and HTML may represent different versions; their equivalence has not been checked. Membership/history XLSX data is another separately maintained downloadable representation.

**Future verification:** approved wording/version/date, policy index and conference-specific listings, direct download and historical links, PDF text/reading order/tags, and explicit replacement/archive status. Do not overwrite or remove an approved historical record merely because a newer one exists.

## 7. Create a page and add navigation

**Files:** new section-local Markdown file with title/layout and optional explicit permalink. `page` adds the sidebar, `blank` is full-width. Add the link to the appropriate section landing page, or `_data/policies.yml` for a policy. Edit `_data/navigation.yml` only if a top-level link is genuinely needed. Header rendering comes from `_includes/page-header.html`; breadcrumbs derive from URL segments in `_includes/breadcrumbs.html`. `siteindex/index.md` lists eligible titled pages automatically; it is not the main navigation registry.

**Knowledge:** front matter, source/output URL differences, baseurl filters, relative links, layout choice, intermediate index pages, and redirects for existing URLs. The same source directory is also a de facto navigation hierarchy.

**Complexity/duplication:** no single navigation hierarchy drives top-level links, section lists, breadcrumbs, and the page index. Missing titles are silently omitted from the index. Adding a page file alone does not guarantee visitors can discover it.

**Future verification:** direct and staging URL, title/headings, parent/section links, breadcrumbs, keyboard/mobile behavior, index/search inclusion, and inbound compatibility if replacing a page. A page creation form should require title, section/parent, content, and stable URL rather than exposing raw Liquid.

## Handover priorities

Recommended first deliverables for a later implementation phase: a tested setup/publish/rollback runbook; one authoritative source per content type; approved examples for each task; preview links attached to reviews; schema validation with actionable error messages; and a named owner/review interval for dates, people, policies, and external links. Trial an editor with actual volunteers using these seven tasks before selecting it for general use.
