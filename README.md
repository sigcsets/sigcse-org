# ACM SIGCSE website modernization

Independent experimental copy of [sigcse.org](https://sigcse.org).
Production deployment is disabled; Phase 1 changes do not alter the site design.

- [Maintainer guide](MAINTAINING.md): edit content and review a pull request.
- [Build and preview](docs/BUILD.md): pinned setup, validation and artifacts.
- [Project status](docs/PROJECT_STATUS.md): Phase 1 checkpoint and next steps.
- [Deployment proposal](docs/DEPLOYMENT.md): ACM requirements and disabled workflow.
- [Original audit](audit/EXECUTIVE_SUMMARY.md): starting evidence and recommendations.

With Ruby 3.3.14, Bundler 2.4.20 and Python installed:

```sh
bundle _2.4.20_ install
bundle exec ruby scripts/build.rb live
python scripts/site.py validate
```

Preview with `bundle exec ruby scripts/build.rb serve` at `http://127.0.0.1:4000/`.
Do not publish the repository directory itself; only validated generated artifacts
are potential deployment inputs. No push or production connection is automated here.

Questions: webmaster@sigcse.org.
