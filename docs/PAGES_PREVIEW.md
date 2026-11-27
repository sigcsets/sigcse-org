# GitHub Pages preview

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

Deployment and actual hosted validation evidence will be recorded after execution.

References: [GitHub custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages),
[upload-pages-artifact](https://github.com/actions/upload-pages-artifact),
[deploy-pages](https://github.com/actions/deploy-pages).
