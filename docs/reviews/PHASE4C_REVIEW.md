# Phase 4C owner review

> Historical review snapshot; phase stops and Pages-disabled statements are superseded. See [current status](../PROJECT_STATUS.md).

Phase 4B's identity and information architecture remain approved. Phase 4C refines community engagement on selected landing pages. This is the current review checkpoint; the prior checkpoint is retained in [reviews/PHASE4B_REVIEW.md](reviews/PHASE4B_REVIEW.md).

## Preview and comparisons

Open http://127.0.0.1:8765/. The loopback preview is running; if stopped, run `python scripts/preview.py`. Rebuild source edits with `bundle exec ruby scripts/build.rb preview` (BUILD.md). No website has been published.

Open `artifacts/phase4c/index.html` for before-and-after desktop/mobile comparisons of home, membership, conferences, awards, committees and news. Twelve Phase 4B captures are preserved under `before/`; twelve updated captures are under `after/`. Images and browser-checks.json are generated local artifacts, excluded from Git and public output. Desktop captures use 1440×1000 and mobile 390×844 viewports; scrollbar/content capture dimensions can be smaller.

## What to review

- **Home `/`:** unchanged hero, introduction, Explore and news/governance structure. Upcoming conferences now form a compact responsive grid, with chronological filtering and unconfirmed-date access preserved. Existing logos or neutral text identify series equally.
- **Membership `/membership/`:** authentic community photograph, join/renew actions, six concise benefit areas and participation options precede the dated global statistics/chart. Full benefits remain at `/membership/benefits.html`, using the same metadata as the landing summaries.
- **Conferences `/conferences/`:** six reusable series panels show existing focus descriptions, event details, official links and archive/proceedings access. ITiCSE/CompEd use existing undated logos; other series have a deliberate typographic fallback. No event facts are duplicated in display metadata.
- **Awards `/programs/awards/`:** concise original descriptions appear with nomination/history actions. Expandable scope/background preserves every complete description. Selection guidance is retained below. Existing recipient histories are unchanged.
- **Committees `/programs/committees-task-forces/`:** active groups and participation/proposal links lead; all historical groups and update dates remain. The incorrect relative creation link and previous-group counter were corrected mechanically.
- **News `/news/`:** tighter rows; removed orphaned arrows that incorrectly suggested external links for internal posts.

Governance, Board, policies, minutes/reports, award recipient histories, funding guidance and historical conference records retain their approved presentation. No new dependency, stock/generated photograph, search, CMS, deployment or DNS change.

## Validation

Clean case-sensitive Linux source checks (including new structured-field requirements), six Python regressions, Ruby conference boundary/order/navigation/breadcrumb checks, live/staging/preview builds, URL/link/asset checks, contrast and all 13 navigation task benchmarks pass. Output remains 1,075 files / 390 HTML pages; all 1,064 baseline paths and 19 redirects are preserved. There are 217 original static findings and zero new findings; one existing broken committee link was fixed. Baselines are unchanged.

Direct comparison verified all 13 complete direct membership benefits and all five full award descriptions are preserved (whitespace normalized). All committee records, membership category data/chart and historical files remain. Legacy membership/nomination anchors are preserved.

Browser checks cover six targeted pages at desktop/mobile and those plus six approved reference/program/archive pages at 320px: no page-wide overflow, one h1, correct active sections/breadcrumbs and no confirmed broken visible images. Keyboard Enter opens disclosures/menu; Escape closes menu and returns focus; skip navigation focuses main. Palette text/background contrast remains 5.45–11.61. Automated checks do not establish full WCAG conformance; screen-reader, zoom, historical documents and external destinations still need broader review.

Hosted live/staging checks passed in [run 45916609423](https://github.com/sigcsets/sigcse-org/actions/runs/45916609423) for `d8ee652`, including packaging and disposable activation/rollback. Eight representative approved reference/program/archive pages have byte-identical rendered main content to Phase 4B (reference-preservation.json). Packaging and disposable activation/rollback are validation only; production deployment and GitHub Pages remain disabled.

## Editorial review

- Confirm inherited registration discounts, publication delivery/access, nomination eligibility and APC hardship benefits are current. No new price or entitlement is asserted.
- Resolve the existing three-versus-four mailing-list discrepancy. The dated January 2025 membership snapshot is labeled and retained.
- Confirm the two groups marked active and whether they have approved public participation contacts; no open recruitment claim was invented.
- Existing conference/award/funding questions remain: CompEd event URL, RESPECT year/TBD details, expired cycles and missing award records. The awards directory no longer repeats the inconsistent old count of four alongside five entries; every award is retained.

The renewal action uses the existing ACM renewal destination documented in ACM's [Membership Renewal Guide](https://www.acm.org/binaries/content/assets/membership/member-renewal-guide.pdf). The guide identifies `acm.org/renew`; join retains the existing local guidance and ACM forms. No login, purchase or renewal transaction was performed. Direct automated requests to the ACM landing pages returned 403, so a logged-in renewal flow is not claimed as tested.

Stop for owner/Board review at Phase 4C. Phase 5, CMS, production deployment and DNS work are not begun.
