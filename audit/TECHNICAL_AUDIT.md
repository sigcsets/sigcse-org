# Technical architecture and evidence

Audit date: November 26, 2026. **Verified** means visible in the inspected repository. **Inference** means a consequence predicted from source but not confirmed in a fresh build or production. **Recommendation** means proposed future work. Paths below are repository-relative.

## Scope and method

Inspected the tracked file list, both configurations, dependency manifests, all layout/include/plugin files, navigation and data structures, section landing pages, representative content across the major sections, maintenance-related pages, asset headers, and file-level metadata. The CSV inventories every tracked file plus locally present `_pending/`, `_unused/`, and `gemfile.lock`. File hashes identify exact duplicates; conservative literal-link scanning provides review flags. This is a comprehensive repository survey, not a line-by-line editorial review of every article or a live-site certification.

No dependency installation, Jekyll build, site edits, configuration changes, deployment, or Git mutations were performed. PDF/Office contents were not extracted, and no external links were HTTP-tested. Existing `_site/` and `.jekyll-cache/` are ignored local generated material, not authoritative source or proof of a current successful build. Product documentation links in the recommendations support capability assessment only.

## Runtime, dependencies, and configuration

| Component | Verified evidence | Implication |
|---|---|---|
| Generator | `gemfile`: `gem "jekyll"` without version constraint | Dependency resolution can change between installations |
| Locally resolved version | Ignored, untracked `gemfile.lock`: Jekyll 4.4.1, Bundler 2.4.20, platform `x64-mingw32` | Evidence of this local dependency resolution, not the original production version or a portable committed lock |
| Dependency tree | Local lock includes Liquid 4.0.4, kramdown 2.5.2, Sass converter 3.0.0, Sass embedded 1.63.6, WEBrick 1.9.2 | These versions are observations, not a vulnerability or compatibility assessment |
| Ruby | No tracked Ruby version declaration found | Production/local Ruby parity remains unknown |
| Plugins | `_plugins/doi.rb`; additional gem/plugin examples in `gemfile` are comments | One actual custom plugin, no configured plugin-gem list |
| Theme | No configured theme/remote theme | Repository-owned Bootstrap-based layouts |
| Configurations | `_config_live.yml`, `_config_staging.yml`; no `_config.yml` | An explicit configuration selection is needed to reproduce intended settings |
| Live settings | `url: https://sigcse.org`, empty `baseurl`, `incremental: false` | Root-domain public URL model |
| Staging settings | Same domain, `baseurl: /.staging`, `staging: true`, `incremental: true` | Staging shares hostname; path-prefix handling needs testing |
| Defaults | Both set post layout and `/news/:year-:month-:title:output_ext` | Post filenames/slugs are part of public URL compatibility |
| Output retention | Both set `keep_files: ["assets"]` | Inference: removed assets can remain in reused destinations; clean-build behavior should be established |
| Exclusions | Both exclude pending/unused/development/documentation paths, README, bin, and capitalized Gemfile names | Case differences with tracked lowercase `gemfile` merit a clean-build output check; do not assume manifests are excluded on all platforms |

The live/staging files repeat nearly all settings. This invites drift. A future shared base plus small environment overrides could reduce duplication, provided command order and URL behavior are tested.

**Important audit-delivery limitation:** `audit/` is not in the existing configuration exclusions. A subsequent Jekyll build may copy these reports/CSV into output. This audit did not alter configuration, as requested. Keep audit artifacts out of any publication package, or explicitly decide their treatment before the next publication; the CSV includes unpublished-file metadata.

## Layouts and templates

Five layouts: `_layouts/home.html`, `page.html`, `post.html`, `blank.html`, and `redirected.html`. Twenty includes cover global CSS/JS, favicon, header, sidebars, breadcrumbs, conference displays, awards, grants, and organization description.

- **Verified:** home/page/post/blank repeat the full HTML shell, metadata, footer, and inline Holder/jQuery setup. Fixing shared metadata or footer behavior requires multiple edits.
- **Verified:** normal layouts hardcode `<title>ACM SIGCSE</title>` and a Bootstrap-template description rather than page-specific metadata. Canonical metadata is present in the redirect layout, not the ordinary page shell. No configured SEO plugin, sitemap generator, or feed generator was found.
- **Verified:** `page` is a content/sidebar layout; `blank` is a full-width layout despite its name; `home` adds three data-driven banners; `post` adds a date.
- **Verified:** `_layouts/post.html` tests `page.author == true` before displaying the author. Named string authors, including the 2026 award announcement, fail that condition.
- **Verified:** footer “Site last updated” uses build-time `now`; it is not a page content review date.
- **Verified:** conference detail includes (`_includes/symposium-head.md`, `iticse-head.md`, `icer-head.md`, `comped-head.md`, `respect-head.md`, `virtual-head.md`) largely repeat lookup, previous/next, proceedings, and table patterns. Many derive the year from the filename. Decimal-year symposium filenames preserve multiple events in a year.
- **Verified:** `_includes/conference.md` contains page front matter and a fixed 2017 example. No active include reference was found in tracked Markdown. Treat as a possible leftover, subject to full reference review.
- **Verified:** `_includes/events.html` gathers the first `next-conference` item for six event types and sorts by `start-date`. It does not filter past events; absent websites become `href="#"`.
- **Verified:** `site.data.[evt.name]` in that include differs from bracket syntax used in `about/update.md`. Compatibility should be checked in the pinned runtime rather than assumed broken.

## CSS and JavaScript

`_includes/css.html` loads **both** Bootstrap 5.3.0 from jsDelivr and local `assets/css/bootstrap.min.css` (header: 5.3.2), Google Fonts (Playfair Display), inline Bootstrap example styles, and `assets/css/blog.css`. Local `assets/js/bootstrap.bundle.min.js` identifies itself as Bootstrap 5.3.2.

`_includes/javascript.html` loads Bootstrap, CDN jQuery 3.7.1 (with integrity/crossorigin attributes), a local slim-jQuery fallback, and Holder. Layouts subsequently invoke Holder and override `jQuery.htmlPrefilter`. The active Bootstrap bundle does not itself establish a need for these extra libraries; removal requires a reference and interaction check first.

The asset tree also contains Bootstrap grid/reboot/RTL/source-map variants, `blog-prev.css`, Bootstrap documentation CSS/JS, vendor clipboard/anchor scripts, and 20 SCSS files. These are not all loaded by the active shared includes. `assets/scss/docs.scss` identifies itself as Bootstrap Docs material from 2011–2018. No tracked Node package manifest or SCSS/frontend build script was found. “Present in assets” must not be confused with “active feature”: for example `_algolia.scss` does not establish working search, and `pwa.js` does not establish an installed service worker.

**Recommendation:** select one Bootstrap source/version, simplify the active styles/scripts, and document how maintained assets are produced. Preserve third-party license notices. Do not remove historical or apparently unused assets on name alone.

## Build and deployment

`README.md` contains the site name, URL, and webmaster contact only. No tracked `.github/` workflows, deployment scripts, hosting manifest, test harness, package manifest, or operational runbook was found. `git remote -v` returned no configured remote in this experimental checkout. This does not prove the original organization lacks off-repository automation.

Likely developer entry points, **inferred and not executed**, are `bundle exec jekyll build --config _config_live.yml` and `bundle exec jekyll serve --config _config_staging.yml` after a compatible Ruby/Bundler environment exists. These are starting hypotheses for a future runbook, not validated instructions. Confirm lowercase manifest handling, Ruby version, custom-plugin behavior, clean output, and staging links first. The original upload mechanism, destination server, credentials, redirects, headers, cache/CDN behavior, backup process, and rollback procedure cannot be established here.

## External services and integrations

| Service/reference | Role established by source | Boundary/unknown |
|---|---|---|
| jsDelivr, Google Fonts, code.jquery.com | Runtime CSS/fonts/JS in shared includes | Availability/privacy/performance dependencies; no traffic measurements |
| ACM Digital Library and DOI links | Proceedings, citations, Bulletin access, awards/working-group references in `_data/` and pages | External destination availability and access rules not tested |
| Conference domains | Dates/registration/detail links in event data | Independent sites; hosting/ownership outside this checkout |
| ACM membership and listserv pages | Outbound membership and mailing-list workflows in `membership/` | Site itself is not a membership system |
| Google Docs links | Linked collaboration/source material, e.g. committee notes | Permissions and long-term custodianship unknown |
| Webmaster and organizational email | Contact workflows | Mail delivery and aliases not tested |
| `doi2bib` | Potential build-time CLI call in `_plugins/doi.rb` | Undeclared Python/tool installation and potential network requirement |

No active shared analytics snippet, CMS admin interface, site-search UI/index, or site-hosted form/backend was found in the inspected tracked source. This is a repository observation; server-injected services remain unknown.

## Custom plugin and technical debt

`_plugins/doi.rb` registers a Liquid `doi` tag. It interpolates tag text into a shell command at the absolute Unix path `/usr/local/bin/doi2bib` during initialization, then extracts fields with regular expressions and dereferences matches without checks. There is no tracked dependency setup, cache, timeout, missing-command fallback, or robust BibTeX parser. No active tag invocations were found in tracked page/post content; a sample occurs in the plugin comments.

**Inference:** use of that tag would be nonportable, dependent on external command success, and fragile for unexpected citation formats. Unquoted shell interpolation would also allow trusted-source tag text to affect shell execution. This is a build-author trust issue, not evidence of an exploitable public endpoint. Determine whether the plugin is needed before retaining or replacing it; stored citation data already avoids this runtime dependency elsewhere.

## Accessibility, responsiveness, and performance

Source establishes useful foundations: normal layouts declare English and viewport metadata, use `main`, apply Bootstrap responsive columns, and include many image alternatives. Membership chart values are also exposed as text/alternative text in `membership/index.md`.

Verified gaps and review risks:

- The normal page title is an `h4`; homepage sections start at `h4`/`h6`. A consistent content-first heading hierarchy is absent from the shared shell.
- Active layouts do not provide a skip-to-main link. An unused SCSS filename mentioning skiplinks does not supply one.
- `_includes/symposium-head.md` outputs cover/logo images without `alt`. Similar conference includes need review; meaningful covers and decorative logos require deliberate alternatives.
- `about/board.md` uses floated 150px and 300px blocks. These fixed widths create a narrow-screen reflow risk.
- `_includes/page-header.html` uses horizontal, nonwrapping navigation. Mobile discoverability of offscreen links and keyboard focus visibility need testing. Active items use a CSS class without `aria-current`.
- `assets/css/blog.css` fixes banner height to 450px from 768px up. Longer text or zoom can stress these cards; no overflow test was run.
- Generic links (“More...”, “Click here”, “here”) appear in templates/content, reducing independent link meaning.
- The redirect layout lacks a language declaration and ends its fallback link with another `<a>` instead of `</a>`; it uses meta refresh plus JavaScript rather than an HTTP redirect.
- `news/index.html` starts a new year with a closing `</ul>` before opening its first list. Committee index HTML nests a list in a paragraph. Browser recovery is not a substitute for valid structure.
- Some award markup uses older `data-parent` patterns alongside Bootstrap 5; interactive intent should be clarified before redesign.
- Large original images are publicly located: `about/bulletin/bulletin.58.3/IMG_1830.JPG` is 10.36 MB; `about/bulletin/Bulletin.58.4/SIGCSE Board.jpeg` is 9.76 MB. Smaller display derivatives could improve transfer cost while retaining originals.

No WCAG conformance claim is made. Contrast, focus behavior, touch targets, 200–400% zoom/reflow, assistive technology behavior, rendered performance, and PDF accessibility require a subsequent test phase. The 252 PDFs were inventoried by path/size, not inspected for tags, reading order, scanned text, or accessible forms.

## Content correctness and URL hazards

1. **Verified data disagreement:** four 2026 award categories announced in `_posts/2026-01-19-SIGCSE-Awards-2026-Announced.md` have no 2026 rows in their data files. Do not infer a new award recipient from outside this evidence; obtain approved entries/citations.
2. **Verified stale labeling logic:** ICER and Virtual `next-conference` dates have passed as of November 26, 2026. Preserve the event records and repair current/upcoming selection in a future change.
3. **Verified case mismatch; hosting effect inferred:** `about/bulletin.md` constructs `bulletin/bulletin.58.4/index.html`, while the tracked directory is `Bulletin.58.4`. Case-sensitive hosts will require matching paths or a compatibility redirect.
4. **Verified relative target error:** `programs/committees-task-forces/index.md` links to `committees-task-forces/create.html`, resolving under that directory to a nonexistent repeated-directory path.
5. **Verified count mismatch:** the same index counts `page.committees` for previous committees but loops over `page.previous`.
6. **Review required:** `_data/organization.yml` lists David Zabnar under both current and previous Information Directors; its prose says three directors while four members are listed. Other roles retain ended terms (e.g. Social Media Coordinator 2020–2023). Historical validity and current incumbency require owner confirmation.
7. **Verified snapshot age, not necessarily an error:** `_data/membership.yml` explicitly dates its figures January 2025. Treat as a dated snapshot unless a newer approved source is supplied.

## Inventory interpretation

`CONTENT_INVENTORY.csv` columns: `source_path`, `public_url`, `title`, `category`, `format`, `observations`, `tracked`, `size_bytes`. URLs use the live configuration; page Markdown extensions become `.html`, explicit permalinks are retained, and `index.html` paths are shown explicitly. Post URLs use an approximate default slug calculation and must be checked against a future rendered manifest. Staging prefixes are deliberately not included. Blank URLs identify build inputs or excluded local material, not missing public pages.

Titles come from front matter, HTML `<title>`, or filenames; fallback titles are labeled. No PDF/Office internal titles were extracted. Exactly 124 front-matter pages lack their own title; includes may supply visible headings, but `siteindex/index.md` excludes them through its title test. Literal-reference flags do not evaluate Liquid, YAML relationships, server rewrites, external backlinks, or direct visitor URLs. They are review leads, never proof that a file is unused.

Across all inventoried files, SHA-256 grouping found 163 exact-duplicate groups involving 406 files, including local backup copies. Examples among tracked files include four Bulletin logo copies and the Board portraits under multiple term directories. Some duplication intentionally makes historical publications self-contained. Redirect source pages are intentional compatibility infrastructure, not duplicate content to delete.
