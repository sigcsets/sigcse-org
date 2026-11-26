# SIGCSE website repository audit

Audit date: November 26, 2026. Audience: SIGCSE Board, volunteers, and developers.

The repository supports continued use of Jekyll. Its main obstacles are fragmented maintenance workflows, weak content discovery, inconsistent presentation, and undocumented publishing arrangements. This investigation found no compelling repository-based reason to change platforms. A platform change would introduce substantial URL and archival preservation work without necessarily fixing these problems.

## What was examined

Read-only inspection of tracked source, configuration, templates, assets, and locally present excluded material. Only `audit/` was created. No dependencies were installed, no build or deployment was run, and no website configuration was changed. Production hosting, live HTTP responses, browser accessibility, and PDF contents were not tested. External product documentation was consulted only to assess proposed search/editor options.

The inventory contains **1,778 file records**: **1,144 tracked files**, **633 ignored local files** in `_pending/` and `_unused/`, and the ignored local `gemfile.lock`. It includes supporting code/assets for completeness. Generated `_site/`, cache, Git internals, and the audit itself are excluded. Tracked files occupy about **256 MB (244 MiB)**.

Tracked material includes 100 news posts, 260 pages with front matter, 19 redirects, six standalone HTML files, 27 data files, 389 images, and 255 downloads (252 PDFs, one spreadsheet, one slide deck, one Word document). These are file counts, not unique articles or rendered-page totals. Historical documents and duplicate files are preservation/review candidates, not deletion candidates.

## Major findings

| Finding | Concrete evidence | Why it matters |
|---|---|---|
| Important information disagrees across displays | `_posts/2026-01-19-SIGCSE-Awards-2026-Announced.md` announces four awards; `_data/outstanding.yml`, `distinguished.yml`, `broadening.yml`, and `testoftime.yml` contain no 2026 entries | Visitors can receive different answers depending on which page they find |
| Upcoming events require manual rollover | `_data/icer.yml` still points to August 11–14, 2026; `_data/virtual.yml` to November 12–15, 2026; `_includes/events.html` performs no date-based expiry | Past events remain labeled upcoming on the audit date |
| Discovery depends on long lists and knowing the right category | Nine top-level navigation links in `_data/navigation.yml`; no site-search implementation found; `siteindex/index.md` filters out pages without titles | Many archival conference pages are hard to find; the “all pages” index does not include news posts |
| Routine editing requires developer skills | Markdown, embedded HTML, Liquid templates, YAML, CSV, and separately uploaded files; `README.md` provides no build/publish instructions | Volunteer handovers and simple updates are unnecessarily difficult |
| Build reproducibility and deployment ownership are unclear | Lowercase `gemfile` has an unconstrained Jekyll dependency; local ignored lockfile records 4.4.1; no tracked CI/deployment workflow or standard `_config.yml` | A fresh maintainer cannot establish a known production-equivalent environment from documentation |
| Presentation and accessibility need systematic work | Shared layouts use a constant browser title and an `h4` page heading; conference includes omit image alternatives; Board cards use fixed widths | Page identification, screen-reader navigation, and narrow-screen use need improvement |
| Specific links are fragile | Bulletin links construct lowercase `bulletin.58.4`, but tracked folder is `about/bulletin/Bulletin.58.4/`; committee creation link repeats its directory | Likely failures on case-sensitive hosting; actual production behavior needs confirmation |

## Highest-impact opportunities

1. Establish a documented, reproducible preview/publish process and a public-URL baseline before restructuring anything. Keep archival URLs and existing redirect entry points.
2. Resolve the verified award/event inconsistencies with the appropriate content owners; add validation and review dates so they do not recur.
3. Improve task-based navigation and add static search, with clear distinction between current guidance and historical records. Keep the archive accessible and searchable.
4. Consolidate the shared page shell, fix page titles/headings/image alternatives, and test keyboard, mobile, zoom, and screen-reader use.
5. Pilot a Git-backed editor for a small set of well-defined content types after preview, authentication, permissions, and review workflows are established.

`RECOMMENDATIONS.md` sequences this work with complexity, impact, risks, and dependencies. `MAINTENANCE_AUDIT.md` maps seven common tasks to the files currently involved. `OPEN_QUESTIONS.md` identifies decisions that need organizational input. All recommendations remain unimplemented.
