# Project status

Updated 2026-11-26. **Stopped for the day: the hosted preview is approved as the
working checkpoint.** Phases 0–6 and the authorized Pages preview are complete;
this is not production-readiness or editorial/accessibility sign-off. No further
implementation phase has begun. Start a new session with [NEXT_STEPS.md](../NEXT_STEPS.md).

## Completed

- Phases 0–1: audit, pinned reproducible Jekyll builds, preservation baselines,
  publication exclusions, Linux CI, validation and disposable release/rollback model.
- Phases 2–3: ownership inventory and conference transfer manifests, source
  organization, shared shell and centralized routine data; historical URLs retained.
- Phase 4 (including 4B/4C): approved Professional Community design, solid blue
  navigation, task-oriented pages and responsive patterns using existing branding.
- Phases 5–6: Pagefind static search, archive filters, maintainer guide/templates,
  schema/error validation, freshness checks and CMS readiness assessment.
- Authorized Pages preview: automatic publication from validated main; hosted
  browser/search/download/redirect checks and desktop/mobile evidence.

## Approved preview and evidence

[Hosted preview](https://sigcsets.github.io/sigcse-org/) (public, no custom domain).
Pushing or merging to main triggers `.github/workflows/validate.yml`. All three
Linux builds (live, staging, github-pages) must pass before deploy-pages publishes
validated output; hosted-smoke then tests the live preview. PRs/other branches
validate but cannot publish. Main manual dispatch also rebuilds. No scheduled
rebuild is configured. See [PAGES_PREVIEW.md](PAGES_PREVIEW.md) for operation/recovery.

Latest verified checkpoint: `83b1d77`, all jobs successful in
[run 45926019456](https://github.com/sigcsets/sigcse-org/actions/runs/45926019456).
Recorded evidence: 1,475 output files / 391 HTML pages; all 1,064 baseline public
paths, 19 redirects and 679 original non-HTML hashes preserved; 217 inherited
static findings, zero new findings. Search covers 365 pages and ten task benchmarks.
Hosted coverage includes 12 pages at desktop/mobile/320px, navigation, PDFs,
redirects, search keyboard/fallbacks and zero axe violations on search.
[REVIEW.md](REVIEW.md) records detailed checks and local screenshot locations;
Actions artifacts expire after seven days. Prior phase checkpoints and stop
instructions in review archives/decision history are historical, not current gates.

## Outstanding work and next steps

1. Collect Board feedback and obtain approved editorial corrections using
   [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md); preserve facts pending approval.
2. Evaluate Git-backed editors and scope a narrow volunteer pilot using
   [CMS_READINESS.md](CMS_READINESS.md). No editor is selected or installed.
3. Perform manual accessibility/usability review: keyboard, screen readers,
   zoom/reflow, slow networks and historical documents; triage inherited defects.
4. Plan eventual ACM deployment under [DEPLOYMENT.md](DEPLOYMENT.md): resolve
   administrator questions, test an authorized destination/rollback, obtain approval.
5. Transfer conference legacy material incrementally only after Steering Committee
   destinations, ownership and redirects are verified and authorized.

[KNOWN_ISSUES.md](KNOWN_ISSUES.md) tracks technical/accessibility limitations;
[content/OWNERSHIP.md](content/OWNERSHIP.md) tracks ownership ambiguities. Human
volunteer editing tests remain incomplete. Search omits PDF/Office body text;
conference freshness/search updates require rebuilds. Ignored local `_pending/`
and `_unused/` remain unpublished and are absent from fresh clones.

ACM deployment remains literally disabled; no production connection, credentials,
DNS/custom-domain changes, new recurring costs or conference removal is authorized.
Resume only within the next user-authorized scope; this handoff starts no phase.
