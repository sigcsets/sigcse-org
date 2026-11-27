# Maintaining the SIGCSE website

Propose approved changes through GitHub. You do not need Ruby, Jekyll, Liquid,
SSH or a local build for routine edits. Pages and production publishing remain
disabled: merging currently validates and packages a preview; it does not publish
on sigcse.org.

## Make an update

1. Find the exact source in the table below. Open it in GitHub, choose Edit, make
   the approved change, and choose **Create a new branch** / **Propose changes**.
2. Open the pull request. State what changed and who approved substantive facts,
   citations, policy text or publication of documents. Keep published filenames,
   permalinks, historical records and existing redirects.
3. Wait for both live and staging **Build and validate** jobs. They show the source
   path and field for editing errors. See the troubleshooting section in
   [templates and fields](docs/CONTENT_TEMPLATES.md#validation-and-troubleshooting).
   Edit the same branch to fix errors; do not change regression baselines.
4. Open Actions, select the successful run, download the live website artifact.
   Its site.tar.gz contains the complete site and search index. A reviewer can
   extract it into an empty folder and run `python -m http.server 8000 --bind
   127.0.0.1`, then open http://127.0.0.1:8000/. No Ruby is needed. Artifacts expire
   after seven days; there is no hosted public preview currently.
5. Review the changed page, related listings, a relevant search, and the mobile
   layout. Request review and merge only after approval and successful checks.
   Use the PR's Git diff to verify no unrelated files or private records changed.

## Exact files to edit

Examples, required fields, upload locations and error explanations for every
workflow are in [CONTENT_TEMPLATES.md](docs/CONTENT_TEMPLATES.md).

| Routine task | Authoritative source | Files normally changed |
|---|---|---|
| Add news | `_posts/YYYY-MM-DD-short-title.md` | One new Markdown file; homepage/archive/search update automatically |
| Add/update upcoming conference | `_data/conferences.yml`, existing series → schedule | One YAML file; homepage and directory update together |
| Add award recipient | `_data/outstanding.yml`, `distinguished.yml`, `broadening.yml` or `testoftime.yml` | One appropriate YAML file; a separate optional news announcement is not the recipient record |
| Update current Board/officers | `_data/board.yml` → current-board → members | One YAML file, plus portrait only if needed in `assets/images/board/current/` |
| Update committee/task force | `content/organization/programs/committees-task-forces/index.md` → active/previous front matter | One Markdown file; charter/report upload only when needed |
| Update operational volunteer roles | `_data/organization.yml` | One YAML file; these roles are separate from Board committees/task forces |
| Special Project facts/deadlines | `content/organization/programs/special/index.md` → application; top-level form | One Markdown file; summary and guidance share the metadata |
| Travel funding/deadlines | `content/organization/programs/travel-grants/index.md` → application.schedule; top-level form | One Markdown file; ISO dates render as readable dates |
| Approved Board minutes | `content/organization/about/reports/board.md` → minutes → term → approved | Metadata file plus approved PDF under `about/reports/BoardMinutes/<term>/` |
| Chair report | `content/organization/about/reports/chair.md` → reports | Metadata file plus approved document under `about/reports/` |
| Business meeting | `content/organization/about/reports/business.md` → business | Metadata file plus approved documents under `about/reports/BusinessMinutes/` |
| Treasurer report | `content/organization/about/reports/treasurer.html` → reports front matter | Metadata file plus approved PDF under `files/AnnualReports/`; no HTML editing |
| Existing organizational policy | Relevant file in `content/organization/policies/` | One Markdown file; preserve approved wording and permalink |
| Add organizational policy | New Markdown file in `content/organization/policies/`, plus `_data/policies.yml` catalog | Two files; do not duplicate full policy text in the catalog |
| Membership guidance/dues | `content/organization/membership/join.md` | One Markdown file |
| Membership benefits | `content/organization/membership/benefits.md` → benefits | One Markdown file; landing summaries update automatically |
| Membership statistics | `_data/membership.yml` | YAML plus matching approved chart if changed; preserve dated snapshots |
| Resource | Appropriate `content/organization/resources/` page | One Markdown file with a descriptive link |
| Navigation | `_data/navigation.yml` | One YAML file; keep public URL paths, not source paths |

Quotes are necessary around YAML text containing `: ` or `#`. Use spaces, not
tabs. New dates use YYYY-MM-DD except published recurring month/day deadlines.
Use the template's fields and existing record indentation. Do not copy Liquid
loops or layout code into a new record. New committee items support a `markdown`
field with ordinary Markdown links; old HTML items remain preserved.

Current schedules are not annual conference history. `_data/<series>.yml` and
`content/conference-legacy/<series>/` preserve annual snapshots. Never update
historical records to mirror new current facts. Source directory depth does not
determine a page's URL: keep its `permalink` unchanged.

## Review and rollback

Preview the changed item in its directory/listing, then search its title or name.
Search reflects the completed build, including main HTML content and linked
public document titles. It does not search PDF/Office bodies. For details and
staging preview commands see [SEARCH.md](docs/SEARCH.md).

If a proposed update is wrong, edit the same PR branch. If an already merged update
needs reversal, create a new PR reverting that commit, review and run the same
checks. Do not rewrite history, replace historical PDFs or manually edit generated
`_site/` output. Future production publishing will need a separately approved
release/rollback process.

## Editorial and publication boundaries

Validation catches syntax and deterministic regressions; it cannot approve facts.
Do not invent missing 2026 award citations, resolve conflicting Board/conference
records, change policy/access rules or remove conference legacy content without
appropriate approval. Open questions are in [docs/OPEN_QUESTIONS.md](docs/OPEN_QUESTIONS.md).

`_pending/` and `_unused/` are ignored unpublished local material. Preserve them;
never upload or commit them automatically. A fresh clone does not contain them.
Audit, docs, scripts, templates/examples, dependencies and generated artifacts are
internal and excluded from the website and search.

Technical setup: [BUILD.md](docs/BUILD.md). Phase 5–6 review:
[REVIEW.md](docs/REVIEW.md). Future visual editing preparation:
[CMS_READINESS.md](docs/CMS_READINESS.md). No CMS is installed.


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
