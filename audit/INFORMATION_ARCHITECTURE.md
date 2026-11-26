# Information architecture and content organization

Audit date: November 26, 2026. Findings refer to source behavior; production navigation and visitor analytics were not observed. Proposed changes below are recommendations, not implemented designs.

## Existing navigation

`_data/navigation.yml`, rendered by `_includes/page-header.html`, defines nine peer-level links. The header separately offers “Sign up” at `/membership/join.html`. Primary navigation is a single horizontally scrollable row, with active styling based on the URL containing a section prefix.

| Top level | Landing page | Principal destinations visible there |
|---|---|---|
| Home | `index.md` → `/index.html` (also normally `/`) | Three banners, latest five news posts, latest three historical records for each of six conference series, upcoming-event sidebar |
| About | `about/index.md` | Profile, Board, annual reports, minutes, Board history, volunteers, Bulletin, logo |
| News | `news/index.html` | Every post, grouped by year |
| Membership | `membership/index.md` | Statistics, benefits, joining, involvement, mailing lists, ACM grades |
| Events | `events/index.md` | Six conference series, Doctoral Consortium, Working Groups, best papers, 50-year history, in-cooperation events |
| Programs | `programs/index.md` | Awards, Special Projects, travel grants, Speaker's Fund, committees/task forces, local chapters, in-cooperation policy, SISL |
| Policies | `policies/index.md` | Bylaws; Board, general conference, and conference-specific policies; sustainability |
| Resources | `resources/index.md` | SIGCSE Reads, publications, Ph.D. programs, publishing venues, DEI report |
| Pages | `siteindex/index.md` | Alphabetical index of titled `site.pages` entries |

The home sidebar is `_includes/sidebar-home.html` → `events.html`. Normal page/post sidebars use `sidebar.html` → organization description plus the same event list. There is no local section menu in those templates. Visitors generally return to a landing page, follow breadcrumbs, or use in-content links for related material.

## Existing hierarchy and discovery routes

- Conferences: Home/Events → series overview (`events/symposia/index.md`, etc.) → recent detail pages, complete `conferences.md` list, or `covers.md` image browser → year detail → external conference website/proceedings. Previous/next links connect year pages.
- Awards: Programs → `programs/awards/index.md` → award description/recipient list or nomination guidance. Recipient lists share data with conference detail pages through `_includes/awards.md`; Test of Time has its own display. Some legacy award names redirect to current names.
- Governance: About → Board or Reports → report/minute list → dated document. Board history uses a CSV-driven table plus a downloadable spreadsheet.
- Grants: Programs → Special Projects or Travel Grants → guidance/history. `programs/special/2003.md` through `2025.md` use `_includes/special-projects.html` and the grant data.
- Committees/task forces: Programs → committee index → charter/detail/update/report. Operational conference committees also appear under About → Volunteers. Working Groups are separately under Events and list published reports from `_data/workinggroups.yml`.
- News: Homepage exposes five recent items; News is the chronological archive. Posts are not part of the `site.pages` alphabetic index.
- Bulletin: About → Bulletin → four most recent issues; older local PDFs remain in the tree, while the page directs readers to the ACM Digital Library for past issues.

Depth is not uniformly excessive: most current information is within two or three selections. Archive/document routes can take four or more selections from the top-level menu. The larger issue is uncertain category choice and long lists without search, rather than an exceptionally deep directory tree everywhere.

## Repository content inventory

`CONTENT_INVENTORY.csv` is the file-level inventory. It deliberately includes code and excluded material so future maintainers can distinguish content from build inputs and unpublished copies.

| Tracked category | Files | Meaning |
|---|---:|---|
| Pages with front matter | 260 | Includes data-driven detail stubs; excludes redirects/posts |
| News posts | 100 | 2004–2026, Markdown and HTML |
| Redirect entry points | 19 | 18 using the redirect layout plus the Bulletin inline redirect |
| Standalone HTML | 6 | Includes four 2026 Bulletin issues and two `.pdf.html` wrappers |
| Structured data | 27 | 25 YAML files and two CSV files |
| Downloads | 255 | 252 PDFs plus XLSX, PPTX, and DOC |
| Images | 389 | PNG, JPG/JPEG, GIF, SVG, ICO |
| Templates/plugins | 26 | Five layouts, 20 includes, one plugin |
| Frontend assets | 52 | CSS, JS, SCSS, maps, and related files classified under assets |
| Repository support | 10 | Configuration, README, manifest, etc. |
| Total tracked | 1,144 | About 256 MB (244 MiB) |

The 633 excluded local files comprise `_pending/` (30) and `_unused/` (603), predominantly notes, draft/report HTML, and repeated backup extensions. They are not tracked and are explicitly excluded by both Jekyll configurations. They may contain unique organizational work; a future clone will not include them. The local ignored lockfile adds one further CSV row. Generated output/cache/Git internals are excluded.

Major section source-file quantities (Markdown/HTML, including redirects and standalone publications): About 32; Events 154; Membership 6; Policies 22; Programs 60; Resources 7; News index 1; page index 1; homepage 1. These quantities are not directly additive to the category totals because templates and posts are accounted for separately.

| Structured content | Observed quantity | Source/qualification |
|---|---:|---|
| Conference history records | 126 | `conferences` lists: Technical Symposium 59, ITiCSE 31, ICER 21, CompEd 3, RESPECT 11, Virtual 1; upcoming/future records excluded |
| Current Board members | 8 | `_data/board.yml`; history also exists in separate CSV/XLSX/HTML |
| Outstanding award records | 45 | `_data/outstanding.yml` |
| Distinguished Service records | 29 | `_data/distinguished.yml` |
| Broadening Participation records | 2 | `_data/broadening.yml` |
| Test of Time records | 5 | `_data/testoftime.yml` |
| Best paper records | About 133 | `_data/bestpapers.yml`; counted record-leading fields |
| Working-group reports | About 140 | `_data/workinggroups.yml`; counted year/title fields |
| Special Project records | About 136 | `_data/specialprojects.yml`; counted year/title fields |
| Travel grant records | About 112 | `_data/travelgrants.yml`; counted record-leading fields |

These data counts use static record-pattern inspection rather than a Jekyll/YAML build. They indicate scale, not validation of uniqueness, eligibility, completeness, or organizational correctness.

PDFs are distributed across `about/` (197), `programs/` (44), `resources/` (6), and `files/` (5). Documents are not centralized: minutes and reports live near their indexes; committee reports live under program directories; older generic downloads live under `files/documents/`. Images similarly mix global `assets/images/` with conference-local `images/` and self-contained Bulletin folders. Filename conventions include spaces, mixed capitalization, and historical patterns that may form part of public URLs.

## Inconsistencies and barriers

| Verified evidence | Effect/inference | Suggested direction |
|---|---|---|
| “Pages” indexes `site.pages` and only emits rows when `node.title` exists | It excludes posts and 124 front-matter pages without titles; cannot function as a complete searchable catalog | Define inclusion rules and supply usable metadata; retain chronological archives |
| Conference stubs often only set `layout: page` and include a year-derived template | Visible content can have a title while metadata/index entries lack it | Establish stable IDs and page metadata independent of filename parsing |
| Home lists historical conferences by descending year, while sidebars use separate `next-conference` records | “Latest” and “upcoming” can disagree | Define one lifecycle-aware source and display rule |
| About repeats report links both beneath Board and beneath Reports | Parallel access can be helpful, but maintainers must keep descriptions/targets synchronized | Reuse shared link data rather than remove useful cross-links |
| Programs links Distinguished Service through legacy `lifetime.html`, which redirects | Inconsistent naming and avoidable navigation hop | Link current destination while preserving legacy entry URL |
| Committees, operational committees, task forces, and Working Groups live in different systems | Users may not know which structure applies | Add plain-language distinctions and cross-links for “join a group” tasks |
| In-cooperation material appears under Events, Programs, and Policies | Useful multiple entry points, but event listings and application guidance can be confused | Label “find events” versus “request cooperation” consistently |
| `about/bulletin.md` shows only four local issues and refers to external DL history | Local older files can have few visible routes; may reflect intentional access policy | Confirm publication/access policy before building a local archive index |
| Shared breadcrumbs derive hierarchy from URL segments and assume intermediate `index.html` pages | Directory naming becomes navigation wording; no editorial parent relationship | Add explicit parent/title metadata with path fallback |
| Resources multiverse material exists but is absent from the Resources landing list | Potential low-discoverability content, not proof of abandonment | Owner review for appropriate archive or current link |

## Duplicate, orphan, and age review

Exact duplicates are marked per CSV row. Across tracked and excluded material there are 163 hash groups involving 406 files. Repeated Bulletin logos and historical Board portraits may intentionally preserve self-contained publications. `_unused/bak*` directories account for many backup copies. Existing redirects under `programs/committees/`, old award paths, and event aliases preserve URLs and should remain addressable.

“No incoming literal reference detected” is a conservative review flag, not an orphan verdict. Many conference images, grants, and policy links are assembled dynamically. Static scanning cannot discover bookmarks, external links, server aliases, or searches. A future rendered crawl plus server logs/backlink review is needed before any removal or relocation.

Specific human-review candidates: role terms in `_data/organization.yml`; the January 2025 membership snapshot; time-relative “new” and “recently” prose in `events/index.md`; 2024 award eligibility examples in `programs/awards/index.md`; current-versus-historical committee status; early-career award's “yet to be awarded” statement. Age alone does not establish an error. Historical research-methods plans, annual reports, minutes, conference histories, and 2018 anniversary material are organizational records to preserve.

## Search assessment and proposed IA direction

No active site-search control, search index, or search endpoint was found. Browser find only searches the current page. The alphabetical page index and news archive provide browsing, not full-text retrieval. The presence of Algolia-related SCSS in inherited assets is not evidence of integrated search.

Recommended visitor tasks for future usability testing: find the next conference; nominate someone; apply for a grant; join SIGCSE or a mailing list; volunteer; find a policy; retrieve a particular year's minutes or award recipient. Test with both new members and experienced volunteers.

A proposed direction is to retain recognizable sections while adding clear task entry points, local section navigation, and search filters for content type/year/current-versus-archive. Make current procedures and dates prominent without suppressing historical results. Keep public URLs stable even if menu labels or editorial categories change. The Board should approve vocabulary and archive access rules before a detailed navigation redesign.
