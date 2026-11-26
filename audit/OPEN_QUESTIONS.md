# Open questions for SIGCSE

Audit date: November 26, 2026. These questions identify missing evidence and organizational decisions; they did not prevent producing the requested audit. No answers are assumed and no recommendations have been implemented.

## Operating the site

| Question / decision | Why it matters | Suggested owner / evidence needed |
|---|---|---|
| Where is the production source repository, and how does this standalone copy differ? | This checkout has no configured Git remote; its removed history cannot establish past decisions | Webmaster; original repository access or handover notes |
| What Ruby, Bundler, Jekyll, and OS versions build production? | Local ignored lock records Windows/Jekyll 4.4.1 but is not a tracked production guarantee | Webmaster; actual build environment/version output |
| How are live and staging built, uploaded, reviewed, and rolled back? | No tracked deployment/CI scripts or runbook; staging config uses `/.staging` | Webmaster/ACM hosting contact; exact commands and deployment architecture |
| What hosting controls exist for redirects, path case, TLS, headers, cache/CDN, and scheduled builds? | Determines URL compatibility and static-search/editor integration | Hosting administrator; rewrite rules and operational documentation |
| Who may edit, approve, and publish, and how are accounts handed over? | Visual editing and reliable continuity need explicit roles | Board/webmaster; existing access and approval policy |
| Should audit artifacts ever be published? | `audit/` is not excluded in the unchanged configs; inventory names ignored local files | Board/webmaster; publication boundary before the next deployment |
| Is `_plugins/doi.rb` still needed anywhere outside tracked content? | No active tag usages found; it shells out to an undeclared Unix command | Prior/current maintainers; usage and dependency history |

## Current facts and authoritative sources

| Question / decision | Evidence prompting review | Suggested owner |
|---|---|---|
| What are the approved 2026 award citations and presentation event codes? | Announcement names recipients, but all four corresponding award data files lack 2026 rows | Awards chair/Board |
| What should replace ICER/Virtual entries labeled upcoming after their 2026 events? | `_data/icer.yml`, `_data/virtual.yml`; sidebar has no expiry handling | Conference liaisons |
| Are RESPECT 2026 and CompEd 2025 meant to have local historical detail pages? | History data contains those years; corresponding Markdown page stubs are absent | Conference/history maintainers |
| Which Board history source is authoritative? | `board.yml`, `_data/BoardMembers.csv`, downloadable XLSX, and standalone historical HTML coexist | Secretary/webmaster |
| Which volunteer terms and roles are current? | `_data/organization.yml` duplicates an Information Director as current/previous and retains ended terms | Board/role owners |
| Is January 2025 the latest approved membership snapshot? | `_data/membership.yml` explicitly labels those figures | Membership liaison/treasurer |
| Are committee active/prior classifications and early-career award status still correct? | Committee records retain old plans; early-career page says no recipient yet | Board/committee and awards chairs |
| Why do some award rows use `rm-affiliation`? | Display templates read `affiliation`; field may intentionally suppress historical affiliation | Awards/history maintainers |

## Visitors, organization, and archives

1. Which visitor groups and tasks should be prioritized: prospective members, teachers/researchers, conference participants, nominees, grant applicants, volunteers, or governance readers? Are there analytics, search logs, survey results, accessibility reports, or support emails that can establish current problems?
2. What language best distinguishes standing committees, task forces, operational committees, and conference Working Groups? Which cross-links should support “get involved” without merging different organizational structures?
3. Should “Pages” remain a top-level destination, become an archive/catalog, or be complemented by search? What archive filters and date labels are useful to members?
4. Does showing only four local Bulletin issues reflect an intentional access/publication policy? May older local PDFs be cataloged publicly, and how should ACM Digital Library access be explained? The mixed-case October 2026 directory also needs a URL-preserving resolution.
5. Are all current report/minute/download paths intended to be public? How should historical versions, superseded policies, personal contact details, and document corrections be handled? Do not infer a new restriction or deletion requirement from this question.
6. Who owns and can interpret `_pending/` (30 files) and `_unused/` (603 files)? Do any contain unique unpublished records that need an approved archival home? They are ignored locally and would be absent from a fresh clone.
7. Are original media files intended as downloadable preservation masters, or incidental uploads? Which images can have smaller display derivatives while original records remain intact?
8. What accessibility standard and review process should guide implementation, and which high-use PDFs need accessible alternatives first? Is there capacity to review scanned documents and historical publications?

## Search and visual editing

1. Must search cover PDF/Office contents, or will searchable document titles/descriptions and HTML content meet the first phase? Should historical records be included by default, filtered, or clearly labeled? Should external conference sites or the ACM DL be in scope?
2. Can the publishing pipeline run a post-build indexing step and periodic rebuilds? Who will own failed build/search checks?
3. Which Git host and authentication system can support a browser editor, protected review workflow, preview links, and volunteer account recovery?
4. Should editors be able to publish directly, or submit changes for review? Which changes need organizational approval independently of technical validation?
5. Is there a budget or preference for a managed editing service, or a volunteer team able to maintain an open-source editor? No vendor/pricing decision was assumed.
6. Which two volunteers can pilot news/conference editing, and what task-completion criteria define success? Can they use a Git account, or is separate organizational identity essential?

## Limits requiring subsequent verification

- Fresh-build success, exact rendered post slugs, custom Liquid compatibility, and manifest exclusion behavior have not been tested.
- Public HTTP status, server redirects/case handling, external link health, and the fidelity of this copy to sigcse.org remain unverified.
- Literal-reference flags and exact duplicate groups are triage aids; a rendered crawl, logs/backlinks, and content-owner decisions are needed before any deletion or relocation.
- File inventory covers local source files, not remotely hosted documents or the text inside PDFs/Office files. Binary titles, archival completeness, and document accessibility remain unverified.
- Responsive behavior, contrast, keyboard/screen-reader use, runtime errors, measured performance, and security/dependency vulnerability status require separate tests. Source findings identify where to start, not a certification result.
