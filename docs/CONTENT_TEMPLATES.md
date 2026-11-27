# Maintainer templates and field reference

All examples are placeholders for **approved** information, not content to publish.
Copy only the relevant block into the file named in MAINTAINING.md. Keep the
indentation of neighboring records. No example in this internal document is indexed.

## News

Create `_posts/YYYY-MM-DD-approved-short-title.md`. Required: title and ISO date.
Author is optional. Do not rename a published post: the filename determines its URL.
Homepage and news archive update automatically. Future-dated posts remain unpublished
until a rebuild after their date; there is no automatic publishing schedule enabled.

```markdown
---
title: "Approved announcement title"
date: 2027-01-15
author: "Approved author"
---
Approved text with a [descriptive link](/membership/join.html).
```

## Upcoming conference

Edit the existing series in `_data/conferences.yml`, not `_data/<series>.yml`.
Required series fields: id, name, abbreviation, description, archive_url, schedule.
Required event fields: title, start-date, dates, location. Website and end-date are
optional only when unavailable. Use the published URL, not a guessed URL.

```yaml
    - title: "Approved conference title"
      start-date: 2027-07-12
      end-date: 2027-07-14
      dates: "12–14 July 2027"
      location: "Approved location"
      website: https://example.org/approved-event/
```

Keep `dates` as the exact approved display wording. `start-date` is the existing
sorting key. For TBD/month-only records follow the existing record and request a
technical review; do not infer a precise day or end date. Homepage and conference
directory read the same record. The final day is included; past events disappear
from upcoming after rebuilding, but remain in source. Creating annual archive pages
is a separate historical workflow; do not overwrite annual history with new schedules.

## Award recipient

Use `_data/outstanding.yml`, `_data/distinguished.yml`, `_data/broadening.yml` or
`_data/testoftime.yml`. These correspond to the detail pages under
`/programs/awards/`; `_data/award_directory.yml` describes the awards, not recipients.
Required personal-award fields: year, name, desc. Optional: awarded, affiliation.
Use `awarded` only when the presentation event is approved: codes are in
`_data/abbreviations.yml` (TS, ITICSE, ICER, COMPED, RESPECT, VIRTUAL).

```yaml
- name: Approved recipient name
  year: 2027
  awarded: TS
  desc: "Exact approved citation."
```

Test of Time requires year, title, citation and doi instead of name/desc:

```yaml
- year: 2027
  title: "Approved paper title"
  citation: "Exact approved bibliographic citation."
  doi: https://doi.org/approved-identifier
```

Do not change historical `rm-affiliation` fields to affiliation; the discrepancy
awaits owner review. Early Career has no approved recipient data model yet; ask the
awards chair/webmaster before creating its first record. Never infer missing 2026 rows.

## Board and officers

Edit `_data/board.yml` → `current-board` → `members`. Required Board fields: year,
term, members. Required member fields: name, position, image; retain affiliation,
country and email because the display uses them. Portrait filenames refer to
`assets/images/board/current/`. Upload a new approved portrait only when necessary.

```yaml
    - name: Approved member name
      position: Secretary
      image: approved-person.png
      affiliation: Approved institution
      country: Approved country
      email: approved-address@example.org
```

Update the current term once. Historical YAML/CSV/XLSX/HTML records are separate
snapshots; a new term and historical reconciliation require Secretary review.

## Committees and task forces

The front matter of
`content/organization/programs/committees-task-forces/index.md` is authoritative for
`active` and `previous` groups. Required: name, items; each item has `item` (existing
historical HTML is retained) or `markdown` (recommended for new prose and links).
Move a concluded group to previous only with approval; retain its history.

```yaml
  - name: "Approved committee name"
    items:
      - markdown: "Established: approved year"
      - markdown: "Facilitators: approved names and affiliations"
      - markdown: "[Approved charter](reports/approved-charter.pdf)"
```

Operational roles are a different listing: `_data/organization.yml` → committees,
officers, volunteers, as applicable. Copy its neighboring group/member shape; do
not add the same role in both listings. An optional new charter is a Markdown page
in the same content directory plus any approved PDF in the existing public report
directory. Do not edit the Liquid loops below front matter.

## Funding opportunities and deadlines

Special Projects: `content/organization/programs/special/index.md` → application.
Travel: `content/organization/programs/travel-grants/index.md` → application.
Both require maximum_award, eligibility list, history link and top-level form.
Special Projects also uses deadlines and contact. Summaries and detailed guidance
share these fields; do not paste a second copy of a deadline into the prose.

```yaml
application:
  maximum_award: "Approved amount"
  eligibility:
    - "Approved eligibility requirement"
  history: /programs/travel-grants/awards.html
  schedule:
    - conference: "Approved conference"
      grants: "Approved count"
      deadline: 2027-01-15
      notification: 2027-02-01
```

Schedule rows require all four fields; dates use YYYY-MM-DD, or the existing `—`
for not applicable. They display as readable dates. Preserve expired cycles until
an approved replacement exists. `legacy_cycle` is a retained snapshot, not the
current application schedule. Recurring Special Project deadlines use published
month/day strings, e.g. `deadlines: [May 15, November 15]`.
Grant-recipient history stays in `_data/travelgrants.yml` / `_data/specialprojects.yml`.
Other funding guidance stays on its existing page; use the source permalink to
confirm the correct page, and preserve ownership questions.

## Board minutes and reports

Board minutes: edit `content/organization/about/reports/board.md` → minutes →
the approved Board's `approved` list. Upload the approved PDF to
`about/reports/BoardMinutes/<term>/Minutes-YYYY-MM-DD.pdf`. The filename is generated
from folder and date; use exact case. Required group fields: year, folder, approved;
required meeting fields: description and ISO date.

```yaml
    approved:
      - description: "Approved description of meeting"
        date: 2027-01-15
```

Chair reports: `content/organization/about/reports/chair.md` → reports → the correct
chair's reports list; upload under `about/reports/` matching the `url` exactly.
Each chair group requires chair/reports; each report requires year/title/url.

```yaml
      - year: 2027
        title: "Approved Chair's Report title"
        url: annualReport2027.pdf
```

Business meetings: `content/organization/about/reports/business.md` → business;
required year/date/city; notes and slides are public document paths or `false`.
Upload under `about/reports/BusinessMinutes/` following existing conventions.
Treasurer: `content/organization/about/reports/treasurer.html` → reports, with
title/url fields. Despite the .html extension, routine edits are YAML only:

```yaml
  - title: "Approved fiscal-year report label"
    url: /files/AnnualReports/approved-filename.pdf
```

New documents normally need two files: metadata plus PDF. Never replace an
approved historical document with a new version under the old filename.

## Organizational policies

Existing policy: edit the Markdown body in `content/organization/policies/`.
Keep permalink, approved wording and dates. A new policy needs a Markdown file and
an entry in the appropriate organizational group in `_data/policies.yml`; new
policy catalog records require title/url. URLs there are relative to site root
without a leading slash, following the existing schema.

```markdown
---
title: Approved policy title
layout: page
permalink: /policies/approved-slug.html
---
Exact approved policy text.
```

```yaml
  - title: Approved policy title
    url: policies/approved-slug.html
```

Catalog title is a navigational label; policy prose is authoritative on its page.
The same topic may have conference legacy ownership; classification does not grant
authority to rewrite it. Preserve superseded versions and links.

## Membership

Guidance/dues: `content/organization/membership/join.md`. Full benefits:
`content/organization/membership/benefits.md` → benefits list (required group/text;
featured rows also need label/link). The homepage-style membership landing reads
these benefits automatically. Do not change landing-page Liquid to edit benefits.

```yaml
  - group: "Community and Recognition"
    text: "Approved full benefit statement."
    featured: true
    label: "Approved short label"
    link: /membership/join.html
```

Use a neighboring record's actual group value. Dated statistics:
`_data/membership.yml` (date, members, countries, image, categories with name/count/
percent), plus an approved chart in `assets/images/` if the snapshot changes.
Keep counts and chart from the same approved snapshot. The landing introduction
is in `content/organization/membership/index.md`. These are separate kinds of
information; do not update all files for a simple change to one benefit.

## Validation and troubleshooting

YAML uses spaces, never tabs. Quote text containing `: ` or `#`. Dates and public
filenames are case-sensitive. The PR checks parse front matter/YAML/CSV, reject
duplicate keys, check required fields, award event codes and duplicates, date
syntax, portraits, generated links/assets, public URL preservation and search tasks.
Errors include the source path and field. Correct that file, push another commit
to the same PR and wait for both builds. Do not edit regression baselines to pass.

One inherited news date string is accepted only for its exact original file/value;
four original duplicate YAML keys remain baseline findings. Historical affiliations,
missing award years and disputed ownership still need editorial review. Technical
validation cannot certify citations, financial rules, approval status or PDF access.
