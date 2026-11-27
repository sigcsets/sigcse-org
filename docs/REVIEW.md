# Phase 4B owner and Board review

Concept B is implemented with the approved solid blue navigation, compact sans-serif presentation and authentic existing photography. Phase 5 has not begun. Production deployment and GitHub Pages remain disabled; no DNS or ACM server changes.

## Open the working preview

Open http://127.0.0.1:8765/ in this workspace. If stopped, run `python scripts/preview.py` from the repository root. The generated `_site` is ready to review. Rebuild after edits with `bundle exec ruby scripts/build.rb preview`; setup is in BUILD.md. This machine uses pinned Ruby in Ubuntu-22.04 WSL. The local preview is not published.

Open `artifacts/phase4b-final/screenshots/index.html` for 28 representative desktop/mobile screenshots. Screenshots and JSON evidence are local generated artifacts, intentionally excluded from Git and public output. Historical concept comparisons remain under docs/design/phase4b and are not public controls.

## Review route

| Pattern | Local path |
|---|---|
| Community homepage, upcoming conferences | `/` |
| Membership with archival photograph | `/membership/` |
| Conference directory | `/conferences/` |
| Governance with Board photograph | `/governance/` |
| Board portraits and contacts | `/about/board.html` |
| Awards and nominations directory | `/programs/awards/` |
| Recipient history | `/programs/awards/outstanding.html` |
| Special Projects guidance and application | `/programs/special/` |
| Travel eligibility and schedule | `/programs/travel-grants/` |
| Compact policy index | `/policies/` |
| Minutes reference index | `/about/reports/board.html` |
| News archive | `/news/` |
| Retained annual conference record | `/events/symposia/2025.html` |
| Committee directory | `/programs/committees-task-forces/` |

## Validation evidence

- Clean case-sensitive Linux source checks, six Python regressions and Ruby conference/navigation/breadcrumb checks pass. Ruby 3.3.14, Bundler 2.4.20 and frozen dependencies remain unchanged.
- Live, staging and local preview build and validate successfully: 1,075 output files, 390 HTML pages; all 1,064 baseline public files and 19 redirects preserved; 218 explicitly tracked existing findings, zero new findings. No baseline was relaxed.
- All 13 navigation tasks take one or two selections. Board minutes and Chair reports now have direct homepage links.
- Shared CSS text/background pairs pass 4.5:1, with measured ratios 5.45–11.61. Static metadata, image alternatives, internal links, fragments, redirects and internal publication checks run in CI. This does not establish full WCAG conformance.
- Fourteen representative patterns checked at desktop, mobile and 320px: no document overflow, one h1 and active section/breadcrumb consistency. Initially incomplete lazy images were rechecked after loading. Keyboard Enter opens the mobile menu; Escape closes it and focuses its summary; skip link focuses main content. Historical tables scroll within their own regions.
- Original conference legacy sources, historical schedule data and award citations are retained. Travel schedule's five original rows moved unchanged into page metadata; amounts, restrictions, application forms and approved guidance remain. Added recipient anchors do not alter citations. Original photos/downloads remain available at original URLs.
- Hosted live and staging validation passed in [run 45900546242](https://github.com/sigcsets/sigcse-org/actions/runs/45900546242) for implementation/review commit `54e0087`, including preview packaging and disposable release activation/rollback. Deployment is not part of validation.

## Owner/editorial review

Confirm the visual direction across the review route, mobile density, photography choices and funding presentation. Supply approved corrections for the missing CompEd event website, conflicting RESPECT year/TBD details, expired travel cycles and previously identified missing award records. No facts or conference destinations were invented.

Full screen-reader, zoom, PDF accessibility, historical defect remediation and external URL review remain. Standalone Bulletin publications preserve their original presentation. More distinct approved volunteer/committee photographs would help future refinements. Date filtering updates when rebuilt; no publication schedule is enabled.

Stop at this Phase 4B checkpoint. Search, CMS, production deployment and DNS work require later authorization.
