# Project status

Updated: 2026-11-26. **Phase 1: Build and Deployment Foundation — review checkpoint.**
Phase 2 has not begun. Production deployment remains disabled.

## Completed

- Read and committed the supplied instructions and original seven audit reports.
- Captured the original Windows-rendered public site: 1,064 files, 385 HTML pages,
  19 redirect targets, case-sensitive paths, sizes and SHA-256 hashes. A sanitized
  rendered archive remains local; generated output is not committed.
- Pinned Ruby 3.3.14, Bundler 2.4.20, Jekyll 4.4.1 and transitive dependencies;
  normalized Gemfile naming and included Linux/Windows UCRT lock platforms.
- Protected internal documentation, audits, unpublished material, dependency files,
  tests and artifacts in default/live/staging configurations. Clean build wrapper
  removes stale output only in the fixed local `_site` destination.
- Implemented source syntax/initial schemas, case-sensitive URL preservation,
  HTML/CSS link/asset and fragment checks, redirect target/cycle checks, static
  accessibility/metadata smoke checks and explicit legacy defect baselines.
- Added read-only, pinned GitHub Actions live/staging validation, downloadable
  preview packages, hashes/manifests and dependency update PR configuration.
- Proposed conditional ACM SSH deployment with staged release verification,
  restricted identity, locks, atomic activation where supported, rollback and
  nonproduction testing. Remote tooling is intentionally unimplemented pending
  capability confirmation. Literal false workflow prevents production deployment.
- Added a disposable local release/rollback demonstration and security/failure tests.
- Added maintainer, build, deployment, decision, question and known-issue guides.

## Validation evidence

- Original native Windows build passed with the existing Ruby 2.7.8 environment.
- Frozen pinned build passed on a clean source copy on Ubuntu 22.04 WSL's native
  case-sensitive filesystem; live and `/.staging` each preserved 1,064 public files,
  385 HTML pages and all 19 redirects with zero new detected regressions/leaks.
- Source validation passed with four explicit existing duplicate-key findings.
- Six regression tests cover publication leaks, removed URLs, case/fragment errors,
  redirect cycles, staging normalization and corrupt/incomplete/traversal archives.
- Original sanitized archive packaged successfully with SHA-256 and file manifest.
- Full pinned pipeline also passed in the Windows working directory using WSL:
  frozen dependencies, source checks, six tests, clean live build, packaging,
  digest/per-file verification, disposable atomic activation and rollback.
- Final verification from committed source `e06c70a` passed on native Linux:
  default/live/staging configurations, frozen lockfile, source checks, all six
  tests, archive packaging and disposable activation/rollback. Each configuration
  produced 1,064 public files with zero new findings. Local JSON evidence is in
  `artifacts/final-linux-{default,live,staging}.json`.
- Local HTTP smoke check returned 200 for the homepage, Board page, 2025 Symposium
  page, Board-history redirect page and a historical Bulletin PDF.
- Confirmed all 633 ignored local unpublished files remain present. Diff/whitespace
  and credential-marker checks passed. No generated output or unpublished content
  entered Git commits.

## Deviations and limits

- No remote is configured and no push is authorized. Hosted Actions and repository
  branch protection await owner setup; local commands exercise the same pipeline.
- Native Windows with the new Ruby pin has not been tested. Native Linux and the
  original native Windows environment have been tested separately.
- Six pages change equal-key list ordering across the old/new Ruby environments;
  content and citations remain. Other HTML hash differences are line endings.
  No content source, layout, navigation or branding was redesigned.
- Existing 861 output findings and four source duplicates remain visible in
  baselines. Static tests do not establish accessibility conformance.
- Production content parity, external links, server behavior, remote deployment
  and HTTP rollback verification remain untested. No ACM server was contacted.
- Large generated preservation snapshots and ignored local `_pending/`/`_unused/`
  are absent from a fresh clone; original unpublished locations remain untouched.

## Owner actions and recommended next steps

1. Review this checkpoint and the [deployment questions](DEPLOYMENT.md). Obtain
   ACM administrator answers when convenient; do not supply production keys yet.
2. Identify/configure the intended GitHub repository and authorize a push separately.
   Run the workflow there and require both validation jobs through branch protection.
3. Retain `artifacts/original-rendered.tar.gz` and its sidecars in approved internal
   archival storage if long-term retention beyond this local workspace is wanted.
4. Approve beginning Phase 2 only after reviewing Phase 1. Conference ownership,
   content migration, search, redesign and production activation remain later work.
