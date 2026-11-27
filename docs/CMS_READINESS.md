# Future Git-backed visual editing: readiness review

No CMS has been selected, installed or integrated. The repository remains the
source of truth, with ordinary Markdown/YAML and PR-based review.

Ready for a narrow pilot after owner approval: news (one post), upcoming
conferences (one series schedule), current Board (one YAML list), funding
application fields, and membership benefits. Their required fields are validated,
common errors have mutation tests, and live/staging CI includes search and preview
artifacts. Treasurer reports now use title/url metadata instead of hand-built HTML.
New committee items can use Markdown links while existing historical HTML remains.
Internal templates/examples live in CONTENT_TEMPLATES.md and cannot be published.

Before selecting any editor, evaluate authentication, GitHub permissions, branch
protection, mandatory PR review, draft behavior, preview availability, image/PDF
uploads, free/paid limits, volunteer turnover and account recovery. Editors must
not be able to change workflows, templates or secrets through routine forms.
Do not assume the current downloaded artifact is a browser-hosted PR preview.

Remaining schema obstacles:

- Large nested lists in conferences, Board terms, reports and committees need
  focused forms. A generic YAML editor does not remove the need to understand
  term grouping, date precision and annual-history ownership.
- Historical committee items and award citations contain HTML that must survive
  serialization unchanged. Prefer Markdown fields for new committee prose; test
  citation round trips before exposing historical award data to rich text.
- Legacy date strings, duplicate Bulletin YAML keys, decimal Symposium years,
  rm-affiliation, missing 2026 award records, and disputed current information
  remain editorial/compatibility issues. No bulk normalization is authorized.
- Upcoming date precision uses published display wording plus legacy sort keys;
  a form needs explicit TBD/month-only behavior and must never fabricate a day.
- Minutes PDFs follow generated case-sensitive filenames; media upload forms
  must generate/validate those paths. Report schemas vary by report type.
- First Early Career recipient needs an approved data model. Board historical
  CSV/XLSX/HTML sources must not be rewritten as current records by an editor.
- Membership statistics require a matching approved chart; a visual editor must
  not update the numbers alone. Recurring deadlines differ from ISO event dates.
- Several policies have separate catalog labels, approved full text and historical
  versions. Policy publication still requires organizational approval.
- Production publishing and ACM connectivity/rollback remain disabled and
  unresolved. CMS readiness does not authorize deployment or a hosting change.

Anticipated follow-on work (not started by this handoff): compare Git-backed candidates against the above criteria
without committing to a vendor; pilot news/conferences with two volunteers using
disposable branches. Measure time, errors, preview review, PR creation, rollback
and independent handover. Require unchanged permalinks/archives and source/index
validation before expanding to awards, funding or governance. Automated schema
walkthroughs in this phase are not a substitute for real volunteer usability tests.
