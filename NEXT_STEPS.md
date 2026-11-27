---
published: false
---
# Resume development

Checkpoint: **2026-11-26 — owner approved the current hosted preview; development
stopped for the day.** Phases 0–6 and preview publication are complete. This does
not approve factual changes, certify accessibility or authorize production launch.

1. Read [AGENTS.md](AGENTS.md) and [docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md).
   Check `git status -sb`, fetch origin and compare main before editing. Remote:
   `git@github.com:sigcsets/sigcse-org.git`; ordinary commits/pushes are authorized.
   Do not rewrite history or commit generated output/ignored unpublished material.
2. Review [the approved preview](https://sigcsets.github.io/sigcse-org/).
   Main pushes/merges automatically run live/staging/Pages validation, then publish
   through deploy-pages; hosted-smoke checks the published result. PRs cannot
   publish. Manual main dispatch can rebuild; there is no scheduled rebuild.
   [Preview operations](docs/PAGES_PREVIEW.md) includes recovery and evidence.
3. Obtain the next task scope before implementation. Anticipated work:
   - Board feedback/editorial review: [open questions](docs/OPEN_QUESTIONS.md).
   - Git-backed visual editor evaluation and narrow volunteer pilot:
     [readiness/criteria](docs/CMS_READINESS.md); no editor selected or installed.
   - Manual accessibility and usability review:
     [known limitations](docs/KNOWN_ISSUES.md), [review evidence](docs/REVIEW.md).
   - Eventual automated ACM deployment: [proposal/questions](docs/DEPLOYMENT.md).
   - Future conference transfers: [ownership/manifests](docs/content/OWNERSHIP.md).

Preserve the approved design, authoritative sources, history and public URLs.
Keep ACM production disabled; no production access, DNS/custom domain, costs,
editorial corrections or conference removal/redirects without appropriate approval.
Use [MAINTAINING.md](MAINTAINING.md) for routine edits and
[docs/BUILD.md](docs/BUILD.md) for pinned tools/checks. Linux CI is verified; native
Windows Ruby is not. Actions screenshots/reports expire after seven days.

This file's `published: false` front matter keeps it out of ordinary Jekyll builds
without changing deployment configuration. Do not build distributable output with
`--unpublished`. No implementation phase is started by this handoff.
