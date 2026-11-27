# GitHub Pages preview

> Working checkpoint approved by the owner on 2026-11-26. The review-stop instructions and intermediate test issues below are historical and resolved; no new phase is started. Latest verified all-job success: [run 45926019456](https://github.com/sigcsets/sigcse-org/actions/runs/45926019456) at 83b1d77. Operation/recovery below remains current.

Authorized preview: https://sigcsets.github.io/sigcse-org/

## Workflow

Pages uses build_type workflow, cname null. The existing validation workflow adds
a github-pages matrix build using _config_live.yml plus _config_github_pages.yml
(origin https://sigcsets.github.io, baseurl /sigcse-org). Existing configurations
and production deploy.yml are unchanged. The pinned Ruby/Bundler/Jekyll, Python,
Node/pnpm, Pagefind, Playwright and axe versions are reused.

All live/staging/Pages jobs must pass before deployment. Only main push/manual
dispatch in sigcsets/sigcse-org may upload the Pages artifact and deploy. PRs and
other branches cannot publish. Only deploy-pages gets pages:write/id-token:write;
it uses github-pages environment and serialized concurrency. No production secrets
or commands are configured. Upload only validated _site including all Pagefind
assets/fragments. The policy check rejects internal files, symlinks, CNAME, escaped
prefixes, missing noindex and incomplete search bundles. Preview-only hooks apply
noindex/nofollow/noarchive to all HTML, including standalone historical files, and
robots disallow. A discreet shared-shell indicator identifies the preview.

## Operation and recovery

Main publishes automatically after validation. For a manual rebuild, use Actions →
Build and validate → Run workflow → main. Inspect all validation jobs and
deploy-pages, then review the hosted URL. PR checks produce review artifacts only.

Local checks: `bundle exec ruby scripts/build.rb github-pages`,
`python scripts/site.py validate --baseurl /sigcse-org`,
`python scripts/check_pages.py`. Serve with
`python scripts/preview.py --baseurl /sigcse-org` and test with
`SEARCH_BASEURL=/sigcse-org node tests/search-browser.mjs`.

A validation failure prevents deployment; inspect the failed job before retrying.
Recover a bad preview by reverting the offending source change through the normal
reviewed Git workflow and rebuilding main. Retain successful run/commit references.
An owner may unpublish in Settings → Pages for emergency shutdown. Never enable
legacy branch publishing, add CNAME or change DNS/custom domains as a recovery step.
The preview is public; noindex is not access control. PDF bodies are not indexed.

ACM production remains literally disabled. No ACM hosting contact, DNS, custom
domain, design/editorial change or CMS work is authorized. Stop for owner review.

## Evidence

Implementation 328d904 deployed successfully in
[run 45924528803](https://github.com/sigcsets/sigcse-org/actions/runs/45924528803).
All three pinned Linux matrix builds and deploy-pages passed. Pages reports built,
workflow mode, cname null and HTTPS enforced. The github-pages environment already
allows only main. Public artifact checks: 1,475 files, 391 HTML pages; all 1,064
baseline public paths and 19 redirects retained; 217 inherited findings, zero new
findings. Pagefind indexes 365 public pages with three filters. Publication policy
reports no errors. Original baseline files were not changed.

Actual hosted search passed 10 tasks, all 365 result destinations, category/type/
year filters, keyboard, no-JS/load-failure fallbacks, desktop/mobile/320px and zero
axe violations on search. Independent browser review opened home and conferences,
and found Mitchel Resnick through the header search with same-prefix results.
The first general hosted suite stopped on an image-load timing assertion during
viewport changes (governance board-retreat.jpg returns HTTP 200). The test now
waits for image decoding; the final run verifies this correction. Local
live/staging browser tests route historical absolute URLs to the local artifact;
hosted tests reject ACM production URLs, avoiding production contact.

Follow-up main workflow and manual-dispatch evidence are recorded in the final
owner-review report. Evidence artifacts expire after seven days; a copy is supplied
with that report. Existing editorial/accessibility defects remain out of scope.
No production workflow, live/staging/local config, source content, design CSS or DNS
was changed. Stop for owner review after the final hosted suite completes.

References: [GitHub custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages),
[upload-pages-artifact](https://github.com/actions/upload-pages-artifact),
[deploy-pages](https://github.com/actions/deploy-pages).


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
