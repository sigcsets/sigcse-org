# Original public baseline

Captured 2026-11-26 from initial commit `66883b4`, before configuration changes,
using the existing local Ruby 2.7.8 / Bundler 2.4.20 / Jekyll 4.4.1 environment
and its ignored dependency lock (preserved here as `original-gemfile.lock.txt`).
Command: `bundle exec jekyll build --config _config_live.yml --destination _baseline_original`.
This is a baseline of this experimental source copy, not verified production output.

- `public-files.json`: 1,064 exact case-sensitive output file paths, sizes and SHA-256 hashes.
  Covers 385 HTML files, including 100 news posts, plus public downloads and assets.
  Directory URLs are served through their existing `index.html`; `/` maps to `index.html`.
- `redirects.json`: 19 HTML refresh redirect entry points and normalized local targets.
- `known-output-issues.json`: 861 unique existing page/check findings: 106 missing targets,
  109 missing fragments, 222 missing image alternatives, 360 missing h1 elements,
  24 duplicate IDs, 21 missing languages and 19 missing titles. Repeated occurrences
  of the same finding on one page are deduplicated.
- `known-source-issues.json`: four existing duplicate YAML keys. They remain unchanged.

Internal files accidentally copied by the old build (AGENTS.md, audit reports and
lowercase dependency manifests) were deliberately excluded from the public baseline.
No unpublished `_pending/` or `_unused/` content was copied or cataloged anew.
Root internal-directory checks preserve legitimate nested public paths such as
`assets/js/vendor/` and `files/documents/docs/`.

The ignored `_baseline_public/` directory and `artifacts/original-rendered.tar.gz`
contain the sanitized original rendered website. The archive has adjacent SHA-256
and file manifest files. These large generated files are local evidence, not Git
source; retain them in an approved internal archival location if long-term retention
is needed. The raw `_baseline_original/` contains internal reports: never publish it.
A fresh clone has the committed manifests, but neither these generated snapshots
nor the locally ignored unpublished directories.

Original archive SHA-256:
`71cb55c8ad34141f69744c4fbac8ec5bca8b2470e69254a15583c6221729e675`.

Baselines must not be regenerated automatically to make CI pass. Review individual
new findings, fix regressions, and approve any deliberate baseline change in a PR.
The capture command refuses to overwrite an existing baseline. Hash changes are
reported for review, not universally rejected: footer build dates and platform line
endings can change bytes without changing content. URL removals fail validation.
