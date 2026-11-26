# Phase 4 owner review

Phases 2, 3 and 4 are complete for local review. Production deployment remains disabled. No remote history was altered.

## Start the local website

From the repository root, run `python scripts/preview.py`, then open **http://127.0.0.1:8765/**. The generated preview is already built in `_site/`; no Ruby is needed to review it. Ctrl+C stops it. If the QA preview is still running, use that URL directly. Rebuild after edits with `bundle exec ruby scripts/build.rb preview`. A rebuilding Jekyll server is available through `bundle exec ruby scripts/build.rb serve` on port 4000.

This machine's pinned Ruby is installed inside Ubuntu-22.04 WSL. The completed clean builds used that native Linux environment, with frozen Bundler dependencies. To develop on another machine, follow BUILD.md rather than depending on the pre-existing Windows Ruby 2.7 installation.

## Review route and screenshots

Open `artifacts/screenshots/index.html` for the side-by-side screenshot gallery. There are 20 after screenshots (desktop and mobile for every page below), plus 10 original before screenshots. Screenshot evidence is generated local material and is intentionally ignored by Git/public output.

| Page | Local path | Screenshot filename prefix |
|---|---|---|
| Homepage | `/` | `after-home` |
| Conference directory | `/conferences/` | `after-conferences` |
| Governance | `/governance/` | `after-governance` |
| Board | `/about/board.html` | `after-board` |
| Awards | `/programs/awards/` | `after-awards` |
| Special Projects | `/programs/special/` | `after-special-projects` |
| Travel grants | `/programs/travel-grants/` | `after-travel-grants` |
| Policies | `/policies/` | `after-policies` |
| News | `/news/` | `after-news` |
| Retained conference record | `/events/symposia/2025.html` | `after-legacy` |

Each prefix has `-desktop.jpg` and `-mobile.jpg` files in the screenshot directory.

## Navigation

Seven primary destinations: Conferences, Membership, Awards, Funding, Resources, Governance and Policies. About, News and Join are utility links; archives/all-pages are available in the footer. The homepage directly links to Special Projects, travel support, awards, membership, conferences and Board contacts. Contextual section navigation provides local task links. All 13 tested tasks take one or two link selections from home, including Board minutes, reports, nomination guidance and recipient records. The mobile navigation uses native details with Enter/Space support; Escape closes it and returns focus. It remains expanded and usable without JavaScript.

The new conference directory is concise. Annual conference history is clearly labeled and reachable through `/archives/`, with original URLs retained. Expired listed events are labeled as past rather than upcoming; records were not replaced with invented events. Search remains Phase 5.

## Repository organization

- `content/organization/`: organizational pages and hubs, with explicit stable permalinks.
- `content/conference-legacy/<series>/`: isolated series prose and annual page sources, with original public URLs.
- `_posts/`: original news source files, unchanged.
- `_data/conferences.yml`: one source for the concise directory and current listed schedules. Historical annual/committee records stay in `_data/<series>.yml`; a compatibility alias exists in memory only.
- `_data/board.yml`, award records and other organizational data remain their authoritative sources.
- `_layouts/default.html`: one HTML shell; small wrappers and reusable includes provide presentation.
- `assets/css/site.css`, `assets/js/site.js`: visual system and minimal responsive menu behavior. One local Bootstrap version is active; archived asset files remain intact.
- Original downloads/images and standalone publications stay at their old paths.
- `docs/content/ownership.csv` and six transfer manifests identify ownership, files, data records, templates, assets and shared dependencies. Ambiguous policies/awards/Working Groups remain integrated for review.

## Validation and limits

- Case-sensitive Linux live/staging/preview builds pass; all 1,064 original public files and all 19 redirect targets remain. Output now has 1,071 files and 390 HTML pages.
- Zero new static findings. Original findings fall from 861 to 218: 104 missing targets, 78 missing image alternatives, 24 duplicate IDs, seven missing fragments, three missing language attributes, one missing title and one missing h1. Four original duplicate YAML keys remain. Baseline files were not expanded or regenerated to pass checks.
- All six regression tests pass. All 13 task-depth checks pass. Original non-HTML asset/download hashes are unchanged.
- Desktop and mobile browser checks cover all ten representative pages: one h1, no broken images and no document overflow. Additional 320px viewport checks pass for all ten. Keyboard menu and skip-to-main focus were verified. Heading text/IDs are preserved while levels are normalized in the shared shell.
- This is not full WCAG conformance: screen readers, touch/zoom combinations, comprehensive contrast/interaction testing, tables and archival PDFs still need a dedicated review. Standalone legacy publications were preserved, not redesigned.
- Existing award discrepancies, expired grant cycles and conference inconsistencies require approved editorial updates. The travel page now visibly identifies its past application cycle; its approved source details remain.
- `origin` points to the supplied repository, which already has independent main history. Nothing was pushed or force-pushed. Hosted execution of these new workflows remains unverified pending integration direction.

## Decisions for the owner

Review the local design and navigation, then decide how this independent history should be integrated with the existing GitHub repository. Confirm any factual/ownership corrections through the appropriate organizational owners. Production/hosting work is deferred and needs no action for this milestone. Phase 5 search and later work have not begun.
