# Decision log

## 2026-11-26 — Phase 1 foundation

- Retain Jekyll 4.4.1; pin Ruby 3.3.14, Bundler 2.4.20 and transitive dependencies.
  The existing Ruby 2.7 environment is baseline evidence, not the new runtime.
  Linux and Windows UCRT are represented in the lockfile. No Node/search dependency
  is introduced before the search phase.
- Normalize `Gemfile`/`Gemfile.lock` case. Add a safe default `_config.yml` and keep
  both old entry points independently safe. Enforce shared configuration parity
  in validation so old explicit commands cannot bypass publication exclusions.
- Always clean the fixed `_site` destination for packaged builds. Remove inherited
  asset retention/incremental behavior to prevent stale files surviving a rebuild.
- Preserve the initial rendered public output and case-sensitive path/hash manifest.
  Intentionally exclude accidentally rendered internal reports and build manifests;
  preserve all 1,064 actual public files and 19 refresh redirects.
- Use Python standard-library output checks and Ruby's YAML/CSV parsers. Baseline
  existing defects explicitly; fail new issues, URL removals, redirect changes and
  publication leaks. Initial static accessibility checks avoid a new browser/Node
  dependency; broader browser/manual assessment remains required later.
- CI uses isolated GitHub-hosted Linux runners with read-only permissions. Artifacts
  supply downloadable previews without assuming GitHub Pages or adding hosting.
  Action commits and build dependencies are pinned; dependency updates require PRs.
- Propose staged, verified versioned releases and atomic activation over approved
  ACM SSH access, conditional on host capabilities. Keep a literal disabled workflow;
  implement no speculative production commands or credential setup. Exercise the
  release model locally in a disposable directory, including rollback.
- Defer ownership classification, content migrations, redesign, search and factual
  corrections. No Phase 2 work is authorized by the Phase 1 checkpoint.

Reference implementation documentation: [BUILD.md](BUILD.md), [DEPLOYMENT.md](DEPLOYMENT.md).
Official references consulted: [Jekyll installation](https://jekyllrb.com/docs/installation/),
[ruby/setup-ruby](https://github.com/ruby/setup-ruby),
[Ruby build archives](https://github.com/ruby/ruby-builder/releases/tag/ruby-3.3.14),
[Bundler in CI](https://guides.rubygems.org/ci/).

## 2026-11-26 — approved local milestone, Phase 2

Owner approved Phase 1 and authorized Phases 2–4 without interim stops. No additional archival storage or deployment investigation. Remote configured and inspected, but left unchanged because it contains existing independent history. Use explicit ownership classification and per-series transfer manifests; shared/ambiguous Board records stay integrated until human ownership review. Directory records point to current series schedule data during Phase 2 to avoid duplicate maintenance.

## Phase 3 — source isolation and template consolidation

Move only published front-matter page sources; preserve every permalink and all public assets/downloads. Keep news in `_posts` and self-contained publications in place. Centralize schedules in the directory and create compatibility aliases in memory. Consolidate HTML shells and active Bootstrap dependencies; retain old asset files because archived publications may use them. Generate missing page metadata from existing annual records, without inventing facts. Broad source reformatting and historical citation changes are excluded.

## Phase 4 — task-oriented local website

Use seven task destinations (Conferences, Membership, Awards, Funding, Resources, Governance, Policies), plus About/News/Join utility links. Add concise hubs and direct homepage access to Special Projects, travel support and Board contacts. Keep the original events and programs landing pages addressable. Preserve conference records behind archive labels and a dedicated archive index. Never label expired listed events as upcoming; retain the dates and flag them without inventing replacements.

Use unchanged official logo artwork, a restrained teal/navy visual system, one shared shell, responsive grids and native details navigation with progressive enhancement. Generate headings and metadata from existing content; preserve IDs/citations. The local preview config changes only origin/baseurl so local browsing does not leave for production when following legacy absolute_url links. No hosting or production investigation performed. Original GitHub history remains untouched.

## Phase 4B — repository authorization and concept review

Owner declared placeholder GitHub history disposable and authorized an explicit force-with-lease replacement of main. Discovered Pages auto-published main/root to preview.sigcse.org; owner separately authorized disabling Pages before push to honor the no-deployment constraint. No DNS/ACM-hosting changes. Main now tracks origin/main and hosted live/staging validation succeeds.

Preserve approved engineering and task navigation. Isolate three static visual concept pairs under excluded internal documentation and generated local artifacts. Use existing authentic attendee and historical group photographs with context, unchanged official logos and source-backed funding facts. Do not select or apply a site-wide direction before owner review. No new dependencies, stock/generated people, new public content formats or Phase 5 work.

## Phase 4B — approved implementation

Owner selected Concept B's welcoming photography, sans-serif typography and compact task presentation, with Concept C's solid blue active navigation. Apply that identity through shared layouts and URL-selected presentation patterns, including retained conference pages. Keep standalone historical publications intact. Reserve header space for later search; no inactive search control or Phase 5 implementation.

Use separate existing photographs on major community pages, centrally documented with source-backed captions. Commit only resized/compressed display derivatives and retain originals. Contain group photographs rather than cropping participants. Put one application form action before long guidance at every viewport. Store funding facts once in page metadata and render summaries/guidance from it.

Compute upcoming conferences from the existing schedule at build time; retain through the final day, sort chronologically and use identical row treatment for all series. Keep TBD separately and preserve past records. Month-only display dates expire at month end without inventing a published day. Missing official links and contradictory years require editorial review. No new runtime dependency, external service, deployment or DNS change.

## Phase 4C — community engagement within the approved identity

Owner substantially approved Phase 4B and authorized targeted refinement of home conference cards, membership, conferences, awards, committees and news. Keep compact reference and action-oriented funding pages intact. Use one reusable community layout with content-driven introductions/actions, authoritative benefits on their existing page, and shared conference identity/card components. Undated existing logos are optional; other series use neutral text rather than invented branding or dated annual artwork.

Derive benefit summaries and award leads from preserved full descriptions. Keep dated membership statistics lower down. Preserve all award scope/selection guidance and legacy anchors. Correct only the committee counter/link and remove nonfunctional news arrow artifacts. Record conflicting counts and potentially stale entitlements for editorial review. Renewal uses ACM's published renewal URL; no account or financial action is performed. Publication remains disabled. Stop at Phase 4C; no search, CMS or production changes.


## Phases 5–6 — approved 2026-11-26

Owner approved Phase 4C and authorized search plus maintainer experience without
an intermediate review. Freeze the approved visual identity; use reserved header
space and existing palette for functional search. Select Pagefind 1.4.0 with local
static UI/index, not a service or bespoke ranking/UI stack. Pin Node/pnpm/browser
checks and run indexing in Jekyll post_write so ordinary builds and serve rebuilds
cannot silently omit search. Reject incomplete search builds. Preserve redirects
while excluding them from indexing. Derive discovery filters from existing page
metadata/URLs; these labels do not decide editorial ownership.

Retain established authoritative Markdown/YAML sources instead of another broad
migration. Normalize travel schedule dates without changing their display/facts;
provide YAML for Treasurer links and optional Markdown for new committee items,
retaining historical HTML. Add explicit examples and editing-error checks rather
than exposing Liquid to volunteers. Keep historical discrepancies/baselines intact.
Future CMS evaluation is documented, not selected, installed or integrated. No
production, Pages, DNS or new paid service. Stop for review after Phase 6.
