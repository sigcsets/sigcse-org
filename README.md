# ACM SIGCSE organizational website

Independent Jekyll modernization copy of [sigcse.org](https://sigcse.org). The approved Phase 4 identity is preserved; Phases 5–6 add static search and maintainer workflows. Production deployment and GitHub Pages are disabled.

## Local review

The generated preview is ready in `_site/`:

```sh
python scripts/preview.py
```

Open `http://127.0.0.1:8765/`; Ctrl+C stops the server. To rebuild from source with Ruby 3.3.14 and Bundler 2.4.20:

```sh
bundle _2.4.20_ install
pnpm install --frozen-lockfile
bundle exec ruby scripts/build.rb preview
```

For a rebuilding Jekyll server, use `bundle exec ruby scripts/build.rb serve` and `http://127.0.0.1:4000/`.

- [Review guide and screenshots](docs/REVIEW.md)
- [Maintainer guide](MAINTAINING.md)
- [Technical build and validation](docs/BUILD.md)
- [Project status](docs/PROJECT_STATUS.md)
- [Ownership and transfer boundaries](docs/content/OWNERSHIP.md)

Organizational pages live in `content/organization/`; conference sources in `content/conference-legacy/<series>/`. Explicit permalinks preserve existing public URLs. Data is under `_data/`; `_layouts/default.html` is the shared shell. Old downloads, images and self-contained publications remain at their original paths.

`origin` is `git@github.com:sigcsets/sigcse-org.git`. Its disposable placeholder history was replaced with explicit owner authorization, and hosted live/staging validation passes. GitHub Pages is disabled to prevent publication. Production/hosting work is deferred. Only validated generated output can become a future deployment input; never publish the repository directory.

Questions: webmaster@sigcse.org.

Search setup and coverage: [SEARCH.md](docs/SEARCH.md). Maintainer templates:
[CONTENT_TEMPLATES.md](docs/CONTENT_TEMPLATES.md). Future visual editing obstacles:
[CMS_READINESS.md](docs/CMS_READINESS.md). No CMS is installed or selected.
