# Maintaining the SIGCSE website

This is an experimental modernization copy. Production publishing is disabled.
Content stays in Git; volunteers can propose changes using GitHub's file editor
without installing Ruby or connecting to ACM. The GitHub repository/remote must
first be established by the project owner.

## Make and review an update

1. Find the source below. Edit only approved information; keep existing filenames
   and historical records. For a GitHub edit, choose a new branch and propose a PR.
2. Describe what changed and any organizational approval in the PR description.
3. Wait for both live and staging **Build and validate** jobs. Open failed checks
   for source paths and error details. A broken YAML indentation/quote, missing
   required field, duplicate record, new broken link or removed public URL can fail.
4. Download the live job's preview artifact. Extract `site.tar.gz` into an empty
   folder; a technical reviewer can serve it using the instructions in
   [docs/BUILD.md](docs/BUILD.md). Check the changed page and related listings.
5. Request review, then merge after approval and checks. In Phase 1, merging builds
   an artifact only; it does **not** update the ACM website.

## Where to edit

| Task | Existing source and fields/example |
|---|---|
| News | Add `_posts/YYYY-MM-DD-descriptive-title.md`; required title and valid publication date. Example below. Homepage/news archive update automatically. |
| Current Board | `_data/board.yml`, `current-board.members`; retain `name`, `position`, `image`, affiliation/contact fields. For example change an approved `email: person@acm.org`; keep portrait paths valid. Do not rewrite prior terms. |
| Conference entry | `_data/conferences.yml`; follow the existing `schedule` fields, including `start-date: 2027-03-01` in ISO format when approved. History and annual pages are separate; changing upcoming information does not create a historical page. |
| Award recipient | Appropriate `_data/{outstanding,distinguished,broadening,testoftime}.yml`; copy a record in that file and supply approved year, name/title, citation and event code where used. For example `year: 2027` only when the award is approved. Never invent citations. |
| Board minutes | `content/organization/about/reports/board.md` plus approved document in its existing dated subdirectory; add a descriptive Markdown link such as `[Approved meeting minutes](board/YYYY-MM-DD.pdf)`. Do not replace historical files. |
| Annual report | Appropriate `content/organization/about/reports/{chair,business,treasurer}` index and approved dated document. Follow the neighboring link's exact filename/case and year. |
| Policy | `content/organization/policies/` source and `_data/policies.yml` catalog if needed. Preserve approved wording and dates; use the existing title/link fields for an approved new version. |
| Committee/task force | `content/organization/programs/committees-task-forces/index.md` front matter and related charter/detail files. Follow a neighboring record's fields and approved status. Operational volunteers instead use `_data/organization.yml`. |
| Funding | `content/organization/programs/special/`, `content/organization/programs/travel-grants/` and related `_data` grant records. Follow existing entries; distinguish application guidance/deadlines from awarded historical grants. |
| Resource | Relevant `content/organization/resources/` page; add an approved descriptive link using `[Resource title](https://example.org/)`. |
| Global navigation | `_data/navigation.yml`; each entry needs `name` and `link`, for example the existing `name: About` / `link: /about/`. Do not change public content URLs just to change menu wording. |

These are existing structures, not a completed new content model. Full task schemas,
single-source consolidation and volunteer usability testing belong to later phases.
The existing [maintenance audit](audit/MAINTENANCE_AUDIT.md) explains cross-file
dependencies and editorial discrepancies; it is internal and excluded from output.

Example news file (illustrative text, not an announcement to publish):

```yaml
---
title: "Approved announcement title"
date: 2026-11-26
author: "Approved author name"
---
Approved announcement text and [descriptive link](/membership/join.html).
```

Quote values containing colons; use spaces, not tabs, in YAML. Keep dates as
`YYYY-MM-DD`. File paths are case-sensitive on hosting even if Windows accepts
different capitalization. Do not rename published posts or downloads casually.

## Existing defects and unpublished files

Validation records existing archive issues instead of requiring their immediate
repair. Do not edit baseline files just to make a failed PR pass. Ask a technical
reviewer to investigate a newly reported regression.

`_pending/` and `_unused/` are ignored local material: preserve them, do not publish
or automatically add them. A fresh clone does not contain them. Audit, developer
documentation, scripts, dependencies and generated artifacts are not public content.

Technical setup: [docs/BUILD.md](docs/BUILD.md). Deployment proposal and administrator
questions: [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md). Project state:
[docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md).

## Source locations after Phase 3

- `content/organization/`: organizational pages, grouped by subject, with explicit public permalinks. Source folders do not control navigation or public URLs.
- `content/conference-legacy/<series>/`: conference series prose and annual pages. Each has a stable permalink and conference classification. Historical images/documents stay at their original public paths under `events/<series>/`.
- `_data/conferences.yml`: concise directory and upcoming schedule for all six series. Edit a schedule once here. `_plugins/content_metadata.rb` supplies in-memory compatibility aliases to older templates; never duplicate schedules in annual history files.
- `_data/<series>.yml`: historical annual records and conference committees; historical snapshots are not current directory entries.
- `_data/board.yml`, award data, `_posts/` and navigation remain the routine sources described above.
- `_layouts/default.html`: single HTML shell; small page/post/home/blank wrappers. `_includes/` contains reusable components. One local Bootstrap bundle remains active. Old assets remain publicly available for archival compatibility.

Keep `permalink` unchanged when moving or renaming a page source. Use the existing record conventions for historical years (including decimal Symposium identifiers). Do not convert historical snapshots to current facts.
