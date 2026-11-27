# GitHub repository and hosting state

Updated 2026-11-26.

## Authorized history replacement

The owner declared the old repository history disposable and explicitly authorized replacing remote `main` with the modernization repository. Inspected remote head was `36cff9e6c224f7f49c94a8444afa2debcedb1fe7`. After the hosting safeguard below, used:

```sh
git push --force-with-lease=refs/heads/main:36cff9e6c224f7f49c94a8444afa2debcedb1fe7 -u origin main:main
```

Local branch was renamed from `master` to `main`. Both local and remote heads were verified as `7e134086151bbd4a6f7d22cb7a5b3027370d6eb7`, the completed Phase 4 implementation. Local `main` tracks `origin/main`. Ordinary future pushes are authorized; history replacement is not the routine workflow.

## GitHub Pages

Before the push, REST inspection returned:

- enabled, public, status `built`;
- build type `legacy`, source branch `main`, root `/`;
- custom domain `preview.sigcse.org`;
- HTTPS enforcement off; protected-domain verification unverified.

Because pushing main would automatically publish, work paused only for this conflict with “do not deploy anything.” The owner then explicitly authorized **disabling Pages, then pushing and validating**. Deleted the Pages site via the repository Pages API and verified the GET endpoint returned HTTP 404, before pushing main. No DNS records were changed. Pages remains disabled; the production workflow's literal false guard remains intact. No production deployment was performed.

Do not re-enable Pages, attach a domain or enable production deployment without new authorization. ACM hosting investigation is still deferred.

## Hosted validation

The initial Phase 4 hosted run completed successfully:
[Build and validate, run 45895218253](https://github.com/sigcsets/sigcse-org/actions/runs/45895218253).

Both `validate (live)` and `validate (staging)` passed. The live job also passed the 13 task-depth checks, packaging, disposable local activation/rollback model, and artifact upload. These are build artifacts, not hosted website publication. No production credentials are involved.


## Phase 5–6 checkpoint

Implementation `5ff1c39` was ordinarily pushed to authorized main. Both hosted
live/staging jobs passed in [run 45922460392](https://github.com/sigcsets/sigcse-org/actions/runs/45922460392),
including search inventory/benchmarks, browser/axe, source/maintenance checks,
URL/link preservation, packaging and disposable activation/rollback. Pages API
still returns 404; disabled production workflow was unchanged. No DNS/server/CMS
change. REVIEW.md records the owner checkpoint and local screenshots.


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


## Completed Pages preview — owner review checkpoint

Phases 5–6 approved; authorized preview is live at
https://sigcsets.github.io/sigcse-org/. Manual dispatch of implementation efd5693
passed every job in [run 45925550271](https://github.com/sigcsets/sigcse-org/actions/runs/45925550271): live, staging,
github-pages, deploy-pages and actual hosted-smoke. Automatic main publication
was also verified in run 45924528803. Superseded runs were cancelled; the initial
hosted image timing assertion was corrected without a site/design change.

Hosted coverage: 12 pages at 1440/390/320px, seven primary navigation links,
conference listings, award recipients, Board minutes, two PDF downloads matching
preservation SHA-256 values, all 19 redirects, historical conference pages,
365 indexed pages, 10 search tasks, three filters, keyboard/fallbacks, zero axe
violations on search, successful WASM loading and 19 forbidden paths returning 404.
No browser script errors or document overflow. Actual desktop/mobile screenshots
and JSON reports are in the run's hosted-smoke artifact (seven-day retention).

Artifact checks: 1,475 files / 391 HTML pages, all 1,064 baseline public URLs
preserved, 217 inherited static findings and zero new findings. Pages settings:
workflow mode, built, HTTPS enforced, cname null. Environment allows only main.
ACM deployment's literal false guard and all existing configs/content/design CSS
remain unchanged; no DNS/custom domain, production operation or CMS work.

No remaining preview deployment blocker. Existing 217 static findings, editorial
questions, PDF-body search limitations and full manual accessibility review remain
unchanged. Stop here for owner review; no subsequent phase is started.
