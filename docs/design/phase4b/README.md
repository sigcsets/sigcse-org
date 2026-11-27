# Phase 4B — three isolated visual concepts

> Historical concept material only. Concept B with Concept C navigation was selected and implemented; search and the hosted preview are now complete. Selection/phase-stop instructions below are superseded; see [current status](../../PROJECT_STATUS.md).

Status: historical concept comparison. Owner selected Concept B with Concept C solid blue navigation. The site-wide implementation is ready for owner review; see ../../REVIEW.md. Phase 5 has not started.

## Open the comparison

The generated gallery is `artifacts/phase4b/index.html`. To rebuild and serve it:

```sh
python docs/design/phase4b/build.py
python -m http.server 8767 --bind 127.0.0.1 --directory artifacts/phase4b
```

Open **http://127.0.0.1:8767/**. Homepage and Special Projects links are available for each concept. Other navigation links lead to the unchanged local Phase 4 preview at port 8765 (`python scripts/preview.py`). The application button is the existing approved external form; no form was submitted during review. News links lead to the current news archive.

The renderer uses Python's standard library only. Its sources live under excluded internal documentation. Generated pages, selected asset copies and six JPEG screenshots live under ignored `artifacts/phase4b/`. They are not a new Jekyll content collection or public site URLs. The working layouts, CSS, navigation, data, public content and regression baselines remain unchanged. Do not copy these prototypes into the public build before a direction is chosen.

## Concepts

| Direction | Homepage | Special Projects interior | Tradeoff |
|---|---|---|---|
| A · Editorial association | Warm paper background, serif editorial typography, balanced attendee image, two-column participation list and news rail | Compact serif title; clear hierarchy; section navigation, main article and application rail | Most academic/publication-like; restrained photographic emphasis |
| B · Professional community | Prominent authentic attendee image; approachable sans-serif typography; community photograph and useful opportunity links | Blue application summary; deadlines, maximum award and eligibility in a full-width strip; broad readable guidance and direct application support | Most welcoming and photographic; slightly taller home composition |
| C · Compact SIGCSE portal | Strong blue masthead/navigation, compact introduction, task index, opportunities, conferences and news visible together | Compact title, persistent section links, application facts table, guidance and support rail | Most information visible at once; less editorial breathing room |

All retain the same seven main navigation destinations and existing official logo artwork. None adds uppercase title eyebrows, gradients, pills, rounded card grids, gratuitous icons or animations. No stock or generated photography is used. The Special Projects summary uses only existing approved deadlines, maximum award, membership requirements and submission instructions. Full guidance remains linked; prototypes do not replace official policy text.

## Screenshot evidence and browser checks

Six rendered desktop screenshots use the same 1440 × 1000 browser viewport. Files are named `a-home.jpg`, `a-special-projects.jpg` and equivalent B/C files under `artifacts/phase4b/screenshots/`. All six saved captures are 1425 × 990 after Chromium omits scrollbar pixels. The gallery shows all six side by side by direction; use live HTML to inspect typography closely.

Desktop and 390px mobile checks passed for all six pages: one h1, no document-level horizontal overflow, all referenced images loaded. Basic focus styles, skip links, semantic headings, labeled navigation, current Funding states and hierarchical breadcrumbs are present. This is concept review, not a full accessibility audit.

## Asset inventory and context

`ASSET_INVENTORY.csv` records dimensions, sizes, recommended uses and context for 35 existing home/logo/current-Board assets. The original comprehensive image inventory remains in `audit/CONTENT_INVENTORY.csv`; this is the curated reuse shortlist, not a replacement.

- `assets/images/home/teaching copy.jpg` (1200 × 675) is the larger original of the attendee image already used on the website. The two participants' identities and event date are not inferred. Suitable for Home, About, Membership and involvement pages. Smaller JPEG and PNG variants remain intact.
- `assets/images/home/exhibits copy.jpg` (1152 × 648) is actually a group photograph visibly labeled as the SIGCSE 50th celebration in 2019. Use with historical context, not as a current conference claim. Suitable for community, conference-history and About material. The existing filename is not a reliable description.
- Current Board portraits and `board 25-28.png` support the Board directory and governance pages; retain the matching term and structured records. A selected design can use larger portraits without changing official roles.
- Existing conference graphics/logos may support conference directory entries; dated annual artwork must retain its year. Avoid promoting obsolete event art as current.
- Official SIGCSE logo files remain unchanged. Award pages can use verified recipient imagery if matching source/citation context exists; do not repurpose arbitrary portraits or imply identities from unrelated photographs. No suitable verified award-ceremony photograph was selected in this shortlist.

Photo captions do not invent authorship or permissions. New public use beyond the existing website context can have credits confirmed during final editorial review.

## After selection

Apply the chosen direction using the existing Jekyll shell and shared data, with a small set of patterns: community homepage, section landing, funding/application, awards/recipients, people directory, document/policy index, news and compact historical archive. Preserve functional pages without decorative images. Refine active section states and hierarchical breadcrumbs across nested pages. Larger Board portraits and distinct award routes belong in that implementation pass.

**Stop here:** owner should choose A, B, C or a specific combination. No site-wide visual direction is selected automatically.
