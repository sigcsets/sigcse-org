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
