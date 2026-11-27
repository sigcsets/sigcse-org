# Search implementation and evaluation

Pagefind 1.4.0 is selected for Phase 5. It indexes rendered static HTML, runs
entirely on the existing host and requires no account, database or paid service.
Its established UI supplies a search input, result excerpts, pagination and native
filter controls; the integration uses the approved header space and site palette.
A bespoke JSON index would require maintaining ranking, excerpts, filtering and
accessible result updates. Hosted search adds an unnecessary service dependency.
See [Pagefind overview](https://pagefind.app/docs/) and
[indexing rules](https://pagefind.app/docs/indexing/).

## Build and scope

`_plugins/search_index.rb` runs the pinned local Node CLI at Jekyll post_write,
including watch/serve rebuilds. Missing dependencies/index failures abort the
build. `pnpm-lock.yaml` locks tools; install with `pnpm install --frozen-lockfile`.
`pagefind.yml` excludes repeated navigation, sidebars, breadcrumbs and archive
notices. Only shared-shell pages carrying `data-pagefind-body` are indexed.
Redirect layout, internal files, unpublished posts and search itself have no body
marker. Internal paths are also excluded from Jekyll and deployment packaging.
The search browser test enumerates the entire index and checks every destination
exists, is unique, and is neither a baseline redirect nor a forbidden path.

The result title comes from the source page's title, rather than a filename or
decorative homepage heading. Excerpts come from main content. Results display a
category and mark conference legacy records as Archive. `showSubResults: false`
avoids repeating a large page as many heading results. All original redirects
remain publicly available but are excluded from the index.
Current organizational page headings and conference directory entries receive
Pagefind heading weights to keep task pages visible among long archival lists;
this does not change their visible text or hide historical matches.

## Filters

`_plugins/search_metadata.rb` derives discovery metadata from public URL,
existing content_type, year and post date. These are discovery labels, not
ownership decisions. Categories: Organizational content, Conferences, Awards,
Governance, Policies and Historical records. Record types distinguish
organizational pages, news, conference legacy and historical records. Year applies
only when recorded in page metadata/date or an annual URL; it does not mean all
years mentioned on a multi-year listing. Dated news remains News rather than
being asserted to describe current policy. Conference-specific policies can be
found using Category=Policies and Record type=Conference legacy where classified.

See [Pagefind filters](https://pagefind.app/docs/filtering/) and
[metadata](https://pagefind.app/docs/metadata/). Captured attributes keep arbitrary
titles safe, including commas and quotes. A classification change must preserve
public URLs and must not silently resolve disputed content ownership.

## Preview, staging and publication

Build commands remain `bundle exec ruby scripts/build.rb preview`, `live`,
`staging` or `serve`; all generate the index. Do not run raw Jekyll with plugins
disabled or upload only HTML. Include the complete generated `pagefind/` folder.
The header action and UI bundle location use Jekyll relative_url. The UI/API base
URL derives from that bundle directory, so result destinations stay on the same
host under the correct prefix. No production domain is hard-coded into the UI.

Root preview: `python scripts/preview.py` and open
`http://127.0.0.1:8765/search/?q=Special+Project`.
Staging: build staging, then `python scripts/preview.py --baseurl /.staging`, open
`http://127.0.0.1:8765/.staging/search/`. Rebuild preview afterward for root browsing.
The standard artifact includes the search bundle. Publication/Pages remain disabled.

## Validation

`node tests/search-browser.mjs` tests the real browser engine and UI. Set
`SEARCH_BASEURL=/.staging` when testing staging. `tests/search-tasks.json` records
representative queries, optional filters and expected destination in the top ten.
Results record rank, local elapsed time, title, excerpt, URL and filter counts.
Times are diagnostics, not a network performance promise. Changes to expected
destinations need review; do not loosen benchmarks to mask relevance regressions.

Checks include complete index inventory, filters, keyboard header submission,
query transfer, keyboard filter selection, no-result feedback, desktop/mobile and
320px reflow, runtime/request failures and axe WCAG 2.2 AA rules. Screenshots and
JSON are generated under `artifacts/search/` and `artifacts/search-staging/` and
uploaded by both CI jobs. Manual screen-reader announcements, zoom, touch targets,
slow-network recovery and real volunteer search tasks remain broader human QA.

## Coverage limits

PDF/Office contents, scanned text/OCR, private/draft records, external conference
sites and ACM Digital Library content are not indexed. Public document titles and
links are searchable through their HTML listings, so a query for a phrase found
only inside a PDF will not work. Original documents and access policies are intact.
Standalone historical publications without the shared shell/body marker are not
full-text indexed; their linked metadata remains discoverable where present.
Multi-year minute and award pages use one result; the year filter cannot select
each row separately. No unapproved publication catalog was added.

Search requires JavaScript and WebAssembly; no-JavaScript browse links are on the
search page. The header form still reaches those links without JavaScript. Native
Pagefind term matching is not a semantic search or guaranteed typo correction.
Static results can become stale until a rebuild. Test actual ACM MIME/CSP/cache
behavior on an authorized destination before enabling production publication.
