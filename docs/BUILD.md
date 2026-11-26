# Build, preview and validation

This experimental copy retains Jekyll. Nothing here publishes to ACM hosting.

## Environment and installation

Use Ruby **3.3.14** (`.ruby-version`), Bundler **2.4.20**, Jekyll **4.4.1**
and the committed `Gemfile.lock`. It locks Linux x86-64 and Windows UCRT dependencies.
CI uses Ubuntu 22.04 and Python **3.12.12**; the Python scripts use only the standard
library and also run on Python 3.10+. Linux needs a C/C++ compiler, make, OpenSSL
and zlib development headers for native gems. On Windows use matching RubyInstaller
Ruby and its Devkit. The pre-existing Ruby 2.7 installation is only baseline evidence.

From the repository root:

```sh
gem install bundler -v 2.4.20
bundle _2.4.20_ install
bundle exec ruby scripts/validate_source.rb
python -m unittest discover -s tests -v
bundle exec ruby scripts/build.rb live
python scripts/site.py validate
python scripts/site.py package
```

For subsequent installs/CI, set `BUNDLE_FROZEN=true` (PowerShell:
`$env:BUNDLE_FROZEN = 'true'`) to reject unreviewed lockfile changes. Dependencies
are fetched from RubyGems during installation; ordinary builds need no network.
Runtime pages still reference existing external CDNs and fonts.

`_config.yml` supplies the safe default for plain `bundle exec jekyll build`.
Both legacy named configs are independently safe for existing explicit commands.
The source validator enforces shared-setting parity. Staging changes only `baseurl`
and the pre-existing staging indicator. Incremental builds and asset retention are
disabled; the wrapper cleans only the fixed repository `_site` directory.

## Preview

```sh
bundle exec ruby scripts/build.rb serve
```

Open `http://127.0.0.1:4000/`. Stop with Ctrl+C. This is a root-path local preview.
To test the historical staging prefix:

```sh
bundle exec ruby scripts/build.rb staging
python scripts/site.py validate --baseurl /.staging
bundle exec jekyll serve --config _config_staging.yml --host 127.0.0.1
```

Open `http://127.0.0.1:4000/.staging/`. Rebuild live before packaging. The packaging
command validates root-path links again; staging output is not a production artifact.
It does not start a server or upload anything.

## CI and artifacts

`.github/workflows/validate.yml` tests live and staging from clean Linux checkouts
on PRs, pushes and manual dispatch. It has read-only repository permissions,
does not persist checkout credentials and uses no deployment secrets. Custom
plugins are repository code and execute on isolated hosted runners; never switch
this workflow to `pull_request_target` or a privileged self-hosted runner.

Required checks: source syntax/initial schemas, validator tests, clean Jekyll builds,
publication boundary, case-sensitive URL preservation, internal HTML/CSS assets,
fragments, redirect targets/cycles and basic static accessibility/metadata rules.
Existing findings are explicit baselines; only new findings block changes. JSON
reports identify changed files, added URLs, resolved findings and new failures.

Download the successful live job's artifact, extract `site.tar.gz` into an empty
directory, then run `python -m http.server 8000 --bind 127.0.0.1` there. Open
`http://127.0.0.1:8000/`. No Ruby is needed to review this generated preview.
The archive is about 233 MB because original historical documents and images remain.
Artifacts expire after seven days; they are downloadable previews, not hosted URLs.

`python scripts/site.py package` produces `artifacts/site.tar.gz`, its SHA-256
sidecar, and a per-file manifest. Generated output, dependencies and artifacts are
ignored by Git and excluded from the site. Retain the original baseline archive
internally if required; CI does not regenerate or overwrite preservation baselines.

## Coverage and limits

- Initial schemas check navigation, event series, current Board member fields,
  conference year uniqueness and upcoming start-date syntax; not every historical
  data model has a full schema yet. All tracked YAML/front matter and CSV are parsed.
- Static checks detect missing title/h1/language, image alternatives, duplicate IDs,
  and untitled iframes. They do not establish WCAG conformance. Browser-based axe,
  keyboard, focus, contrast, screen-reader, zoom, reflow and PDF review remain needed.
- Checks do not request external URLs, inspect PDF bodies, execute JavaScript,
  resolve server rewrite rules, or prove parity with the production server.
- Link checks cover HTML href/src/poster/srcset, refresh redirects and CSS url().
  Dynamically constructed JavaScript requests and CSS source-map comments are not checked.
- Byte hashes are review evidence: line endings, generator dependencies and footer
  build time can affect HTML bytes. Reproducibility means pinned build inputs and
  tested public paths; byte-identical builds at different times are not claimed.
- The DOI tag remains preserved and unused. Its undeclared external CLI would fail
  if introduced into content; it was not invoked by the tested build.

To deliberately update a dependency, unset frozen mode, edit the Gemfile/version
declaration as needed, run Bundler and review the lockfile and output diffs in a PR.
Keep Linux and Windows lock platforms; do not delete history to silence validation.

## Phase 4 local review

`bundle exec ruby scripts/build.rb preview` merges `_config_live.yml,_config_preview.yml`, using `http://127.0.0.1:8765` for absolute links. Then `python scripts/preview.py` serves the result on loopback. The generated preview is already present in this workspace. Ordinary `serve` uses Jekyll's local URL at port 4000. Source changes require a rebuild when using the Python server.

Live CI now also runs `python scripts/check_tasks.py`: all 13 agreed tasks must be reachable within two link selections. Original preservation baselines remain unchanged. The rendered heading-level normalization preserves heading text and IDs and applies only to shared-shell pages; standalone publications are untouched. Shared conference covers/logos now have context-derived alternatives.

Core styles are `assets/css/site.css`, using the existing local Bootstrap 5.3.2 and a small native-details menu script. No web fonts, JavaScript framework or additional build dependency was added. Legacy asset files remain available. Search is deferred to Phase 5.

Phase 4B adds `bundle exec ruby tests/check_site_logic.rb` for conference boundaries/order/preservation and section/breadcrumb behavior. Run `python scripts/check_design.py` after a live build for shared presentation, prototype exclusion and CSS palette contrast. Both checks run in CI. Photographic display derivatives are optional Windows tooling, not a build dependency; committed JPEGs make clean Linux builds independent of System.Drawing.
