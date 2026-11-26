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
