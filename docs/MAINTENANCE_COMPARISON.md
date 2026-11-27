# Phase 6 maintenance comparison

Comparison is against the approved Phase 4C checkpoint. Earlier phases had already
centralized many facts; this phase does not claim further file-count reductions
where they did not occur. Counts below exclude optional announcement/portrait/
document files unless stated. All proposed updates use GitHub PR review.

| Workflow | Before Phase 6 | After Phase 6 | Editing knowledge / verification |
|---|---|---|---|
| News | One Markdown post, short example | Same one post; complete template, date/title checks, automatic search | Markdown; invalid date mutation rejected |
| Upcoming conference | One YAML source, schedule conventions briefly described | Same one source; exact required fields, date-precision guidance, duplicate event check, search | YAML; homepage/directory share facts |
| Award recipient | One YAML source; field conventions inferred | Same one source; personal/paper templates, citation/year/duplicate/event-code checks | YAML; missing citation, duplicate and unknown code mutations rejected |
| Board/officers | One current Board YAML plus optional portrait | Same files; required term/member fields and portrait validation | YAML; missing portrait mutation rejected; historical snapshots protected |
| Committees/task forces | One page with YAML items containing HTML links | Same file; new Markdown-item option, active/previous template and item checks | YAML/Markdown for new items; missing name mutation rejected; old HTML untouched |
| Funding/deadlines | One front-matter source per program; free-form dated travel fields | Same file count; travel dates normalized to ISO with identical display, required schedule/application fields | YAML; missing deadline mutation rejected; expired information retained |
| Minutes/reports | Metadata+document for most types; Treasurer links were hand-coded HTML | Same metadata+document count; Treasurer title/url YAML and shared renderer; explicit paths/templates for each report type | YAML plus upload; invalid minutes date/missing report URL rejected |
| Policies | One page for existing policy; page+catalog for new | Same files; exact prose/catalog templates and catalog field checks | Markdown/YAML; missing catalog title mutation rejected |
| Membership | Facts spread across topic-specific prose, benefits and snapshot | Same authoritative topic sources, precise edit map; shared benefits retained; snapshot checks | Markdown/YAML; missing dated snapshot mutation rejected |

Before: maintainers had to inspect existing records and sometimes HTML to infer
conventions. After: MAINTAINING.md points to exact sources, CONTENT_TEMPLATES.md
provides copyable examples/required fields, and errors identify source paths.
Neither routine editing nor preview review requires a volunteer to build Jekyll
or connect to ACM. All builds create the search index automatically.

Validation evidence: tests/check_maintainer_schema.rb verifies existing data and
eleven invalid-edit mutations without writing placeholder content. Existing
conference/navigation logic, six Python regressions and public-output checks
remain in place. These are automated workflow checks, not completed volunteer
usability interviews. Recommended follow-up: ask two future maintainers to perform
news, conference and minutes changes on disposable PR branches, recording time,
errors, source discovery and preview review before selecting a visual CMS.

Remaining complexity is intentional or deferred: approved citations, historical
Board snapshots, annual conference records, PDF naming, legacy committee HTML,
first Early Career recipient schema, monthly/TBD conference dates, matching
membership chart data and organizational approval. CMS_READINESS.md lists the
requirements for a future editor; no CMS decision was made.
