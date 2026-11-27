# ACM SIGCSE Website Modernization

## 1. Project Context

This repository is an independent experimental copy of the current ACM SIGCSE organizational website, https://sigcse.org.

The existing website uses Jekyll, Markdown, YAML, CSV, Liquid templates, Bootstrap, and static assets. The original Git history has been removed, and this repository has been independently initialized for modernization work.

A comprehensive repository audit has already been completed. Review the following files before beginning implementation:

- `audit/EXECUTIVE_SUMMARY.md`
- `audit/TECHNICAL_AUDIT.md`
- `audit/CONTENT_INVENTORY.csv`
- `audit/INFORMATION_ARCHITECTURE.md`
- `audit/MAINTENANCE_AUDIT.md`
- `audit/RECOMMENDATIONS.md`
- `audit/OPEN_QUESTIONS.md`

These reports establish the initial state of the repository. Their recommendations are advisory; the goals and priorities established in this document take precedence.

This is not the production repository. Substantial refactoring is permitted, subject to the preservation, testing, and deployment requirements below.

## 2. Primary Project Goals

The project has three primary goals, in priority order.

### Goal A: Simplify Maintenance and Deployment

The existing maintenance process requires a maintainer to:

1. Pull the repository.
2. Edit source files.
3. Commit and push changes.
4. Build the website locally.
5. Connect to the ACM hosting server using SSH.
6. Manually transfer generated files.
7. Diagnose and correct deployment errors.

This workflow is unacceptable for routine maintenance of a volunteer-managed organizational website.

The desired workflow is:

1. Edit the appropriate source files, either locally or through GitHub.
2. Submit a pull request.
3. Automatically build and validate the proposed changes.
4. Review the changes and, where available, a generated preview.
5. Approve and merge the pull request.
6. Automatically deploy the updated website.

Routine content changes must not require local Ruby or Jekyll installations, manual SSH sessions, or manual file transfers.

The repository must be organized so that maintainers can easily determine where a particular change should be made.

### Goal B: Improve Navigation and Information Discovery

The current website requires visitors to understand broad organizational categories and navigate multiple intermediate pages to locate important information.

Refactor the information architecture around common visitor tasks rather than historical directory structures.

Major organizational activities should be accessible directly from the homepage or global navigation.

Common tasks should generally require no more than two navigation selections from the homepage.

Examples include:

- Finding an upcoming conference.
- Joining SIGCSE.
- Applying for a Special Project grant.
- Applying for travel funding.
- Finding award nomination information.
- Finding previous award recipients.
- Finding Board members and contact information.
- Finding Board minutes and reports.
- Finding organizational policies.
- Getting involved in SIGCSE.
- Finding committees and task forces.
- Locating computing education resources.

Provide effective site-wide search and meaningful archive navigation.

Navigation depth must not be dictated by source directory depth.

### Goal C: Separate Organizational and Conference Responsibilities

The long-term purpose of sigcse.org is to serve as the organizational website of ACM SIGCSE.

It should primarily contain organization-wide information and information under the responsibility of the SIGCSE Board.

Individual conferences should maintain their own umbrella websites under the responsibility of their respective Steering Committees.

For example, the Technical Symposium should eventually maintain conference-specific information at sigcse-ts.acm.org.

The modernization project must prepare for this separation without prematurely removing existing conference information.

## 3. Content Ownership and Classification

Classify existing content into the following categories.

### 3.1 Organizational Content

Organizational content should remain fully integrated into the redesigned SIGCSE website.

Examples include:

- SIGCSE mission and organizational information.
- Membership information.
- Board membership and governance.
- Board minutes and reports.
- Bylaws.
- Organization-wide policies.
- SIGCSE organizational awards.
- Special Projects.
- Organization-wide travel grants and funding opportunities.
- Board committees and task forces.
- Organizational volunteer opportunities.
- SIGCSE publications and community resources.
- Organization-wide news and announcements.
- Historical records of the organization itself.

### 3.2 Conference Directory Content

SIGCSE should retain a concise directory of its conferences and other relevant events.

Directory information may include:

- Conference name and abbreviation.
- Brief description.
- Permanent conference umbrella website.
- Current or upcoming annual conference website.
- Upcoming dates and location.
- Relevant organizational relationship or status.

Conference directory data should be maintained in one authoritative structured source.

The organizational website should not duplicate detailed information maintained by conference websites.

### 3.3 Conference-Specific Legacy Content

Conference-specific information should be isolated and prepared for eventual transfer to the appropriate Steering Committee.

Examples include:

- Conference history.
- Annual conference records.
- Conference-specific organizing committees.
- Conference-specific operational policies.
- Calls for participation.
- Proceedings and historical proceedings metadata.
- Conference-specific best paper awards.
- Conference-specific working group information.
- Detailed annual conference information.
- Historical conference websites and associated assets.

These examples are not absolute ownership decisions. Some conference-specific policies, awards, funding programs, or records may remain under Board authority.

Ambiguous ownership must be documented for human review.

### 3.4 Transitional Requirements

Do not delete conference-specific content merely because it is outside the intended long-term scope of sigcse.org.

Until an appropriate destination exists:

- Preserve the content.
- Preserve existing public URLs.
- Maintain access to associated documents and assets.
- Keep the content searchable.
- Provide clearly labeled archive navigation.
- Avoid prominently featuring legacy material in current organizational navigation.
- Minimize dependencies between conference-specific content and organizational content.
- Organize conference-specific material so it can eventually be transferred independently.

Where appropriate, create a self-contained source directory or content collection for each conference series.

Maintain a manifest identifying the files, data records, templates, assets, and public URLs associated with each conference.

Conference migration must be possible incrementally. The modernization of sigcse.org must not depend on every Steering Committee completing its own website.

Do not activate external redirects until the destination has been verified and the transfer authorized.

## 4. Technical Principles

### 4.1 Retain Jekyll

Retain Jekyll as the static site generator unless a compelling, documented technical requirement demonstrates that it is inadequate.

Do not migrate to Contentful or another external content platform as part of the initial modernization.

Prefer simple, established, portable technologies.

Avoid introducing:

- A database.
- A custom application backend.
- A complex JavaScript framework.
- A mandatory paid CMS.
- Additional hosting services without demonstrated need.
- Infrastructure requiring substantial ongoing administration.

The website should remain straightforward to build, host, archive, and transfer.

### 4.2 Repository as Source of Truth

The Git repository is the authoritative source of website content and configuration.

Generated website output must not be treated as authoritative content.

All routine content updates should be reviewable through Git pull requests.

Prefer:

- Markdown for prose.
- YAML for structured organizational information.
- CSV where tabular historical data warrants it.
- Reusable Liquid templates for presentation.
- Ordinary static assets for documents and images.

Do not introduce new content formats without a clear benefit.

### 4.3 One Authoritative Source

Each routinely maintained piece of information should have one authoritative source.

Avoid requiring maintainers to edit multiple unrelated files to update the same fact.

Where practical:

- Generate conference directory displays from shared data.
- Generate Board displays from shared Board records.
- Generate award recipient displays from shared award records.
- Generate committee listings from shared committee records.
- Generate navigation from a centralized definition.
- Generate document listings from consistent metadata.

Distinguish historical snapshots from accidental duplication. Historical records must not be rewritten merely to make them match current information.

### 4.4 Predictable Repository Organization

Refactor the repository toward a clear, documented structure.

Organizational content, structured data, conference legacy content, templates, assets, scripts, and developer documentation should have clearly defined locations.

Prefer meaningful directory and file names.

A maintainer should not need to understand Liquid internals to determine where to update a Board member, conference link, award recipient, or policy.

Physical source reorganization must not unnecessarily change public URLs.

### 4.5 Presentation Technology

Bootstrap 5 is an acceptable initial foundation.

The audit identified duplicated Bootstrap dependencies, repeated HTML shells, and inherited frontend assets.

Consolidate these where practical.

Prefer:

- Semantic HTML.
- A single shared page shell.
- Reusable components.
- Consistent typography and spacing.
- Minimal JavaScript dependencies.
- Responsive layouts.
- Straightforward CSS.

Do not retain unnecessary dependencies solely because they already exist.

Do not remove dependencies or assets without checking their actual use.

## 5. Build and Deployment

### 5.1 Reproducible Builds

Establish a reproducible local and automated build process.

Document and appropriately pin:

- Ruby version.
- Bundler version.
- Jekyll version.
- Required dependencies.
- Build configuration.
- Search indexing dependencies, if applicable.

Normalize dependency manifest naming and configuration organization where appropriate.

Test on a case-sensitive Linux environment in addition to the available local development environment.

Provide straightforward commands for:

- Installing dependencies.
- Building the site.
- Running a local preview.
- Running validation checks.
- Producing a deployment artifact.

### 5.2 GitHub Actions

Develop GitHub Actions workflows for automated validation and eventual deployment.

Pull request workflows should:

- Install the pinned dependencies.
- Build the website from a clean checkout.
- Validate structured data.
- Check internal links and asset references.
- Check public URL preservation.
- Perform automated accessibility checks where practical.
- Generate a preview artifact.
- Report failures clearly.

Production deployment should occur automatically after an authorized merge into the designated production branch, once deployment has been explicitly enabled.

The production branch name is configurable.

### 5.3 ACM Hosting Compatibility

The current production website is hosted on ACM/SIGCSE infrastructure and is manually updated through an SSH-based workflow.

Do not assume GitHub Pages can replace the existing hosting arrangement.

DNS control is limited, and changing DNS is not a project prerequisite.

Prefer retaining the existing hosting and domain configuration.

Investigate automated deployment through an ACM-supported mechanism, potentially including:

- SSH.
- SFTP.
- rsync over SSH.
- An ACM-supported deployment service.

The final mechanism depends on server capabilities, network access, authentication requirements, and ACM policy.

Do not assume GitHub-hosted runners can connect to the ACM server.

If necessary, document alternatives without introducing additional infrastructure prematurely.

### 5.4 Deployment Safety

Deployment must be designed to minimize partial updates and accidental damage.

Where supported, prefer complete versioned releases with an atomic activation mechanism.

Otherwise, implement the safest available staged transfer and verification procedure.

Deployment tooling must:

- Use an explicitly configured destination.
- Verify server identity.
- Use appropriately restricted credentials.
- Avoid exposing credentials in logs.
- Prevent concurrent conflicting deployments.
- Detect transfer failures.
- Verify the deployed release.
- Provide a documented rollback procedure.
- Avoid deleting unrelated server content.
- Support a dry-run or nonproduction test mode.

Never use destructive synchronization options against an unverified destination.

Production credentials must never be committed to the repository.

Pull requests, especially those from untrusted contributors, must not receive production deployment credentials.

### 5.5 Production Restrictions

Do not:

- Connect to the production ACM server without explicit authorization.
- Request or embed production credentials unnecessarily.
- Change DNS records.
- Deploy experimental content.
- Enable production deployment automatically during development.
- Assume authority to modify server configuration.

Deployment workflows may be implemented and tested locally or against disposable test destinations.

Any remaining ACM-specific requirements should be documented as actionable questions for the webmaster or hosting administrator.

## 6. Navigation and Visual Design

### 6.1 Information Architecture

Develop a task-oriented information architecture.

Avoid using generic categories such as Programs as the sole route to important activities.

A provisional top-level structure may include:

- About.
- Conferences.
- Membership.
- Awards.
- Funding.
- Resources.
- Governance.

News, search, joining SIGCSE, and other high-value actions should have prominent access.

These labels are starting points, not mandatory final choices.

Use the content inventory and ownership classification to propose an improved navigation structure.

### 6.2 Homepage

The homepage should communicate:

- What SIGCSE is.
- Why someone might join.
- What SIGCSE provides to the community.
- How to find conferences.
- How to find awards and funding opportunities.
- How to participate in SIGCSE.
- Where to find governance and organizational information.
- Recent organizational news.

Avoid turning the homepage into a comprehensive conference archive.

Avoid excessive banners, decorative elements, or duplicated information.

Prioritize useful links and clear calls to action.

### 6.3 Design Direction

A substantial visual redesign is permitted.

The existing visual appearance is not a constraint.

The website should feel like a modern, credible international professional organization.

Prefer:

- Clean and restrained visual design.
- Clear visual hierarchy.
- Readable typography.
- Consistent navigation.
- Generous but efficient spacing.
- Responsive layouts.
- Accessible color choices.
- Appropriate use of existing SIGCSE and ACM branding.

Avoid unnecessary animations, oversized decorative hero sections, excessive card layouts, and visual effects that interfere with information discovery.

Do not invent new official branding or alter organizational logos without approval.

### 6.4 Accessibility

Target WCAG 2.2 AA for the redesigned website.

Address:

- Semantic heading hierarchy.
- Keyboard navigation.
- Visible focus indicators.
- Skip navigation.
- Meaningful link text.
- Accessible menus.
- Image alternatives.
- Color contrast.
- Mobile reflow.
- Zoom behavior.
- Accessible tables.
- Meaningful page titles.
- Screen-reader compatibility.

Automated accessibility testing is necessary but does not establish full conformance.

Document manual verification requirements and known limitations.

Preserve historical documents even when they require later accessibility remediation.

## 7. Search and Archives

Evaluate Pagefind as the preferred initial static search implementation.

Search should:

- Be accessible from every normal page.
- Index meaningful page content.
- Exclude repeated navigation and footer content.
- Include news and historical records.
- Provide meaningful result titles and excerpts.
- Distinguish current organizational information from conference legacy material.
- Support useful content-type and year filtering where practical.
- Work with both local previews and the intended deployment configuration.

Do not index:

- Unpublished drafts.
- Internal audit reports.
- Developer documentation.
- Private records.
- Redirect-only pages.
- Excluded repository material.

Initial search may index document titles and associated HTML metadata rather than full PDF contents.

Clearly document search coverage limitations.

Do not introduce a hosted search subscription unless static search proves insufficient.

## 8. Maintainer Experience

### 8.1 Routine Tasks

Optimize the repository for the following maintenance tasks:

- Add a news announcement.
- Update Board membership.
- Update a conference directory entry.
- Add an award recipient.
- Publish approved Board minutes.
- Publish an annual report.
- Update an approved policy.
- Add or update a committee or task force.
- Update funding opportunities and deadlines.
- Add a resource.
- Update navigation.

Each task should require as few files and technical steps as practical.

Routine tasks should not require modifying templates or application logic.

### 8.2 Maintainer Documentation

Create a prominent root-level `MAINTAINING.md`.

It should provide task-oriented instructions for common updates.

For each task, explain:

- Which file or directory to edit.
- Which fields are required.
- An example of a valid change.
- How to submit a pull request.
- How to review the resulting changes.
- What validation errors might occur.

Write this documentation for a SIGCSE volunteer who may have limited experience with Jekyll or Git.

Maintain separate technical documentation for developers and infrastructure administrators.

### 8.3 Visual Editing

A browser-based visual editor is a potential later enhancement, not a prerequisite.

First establish a simple Git-based maintenance workflow.

After content schemas and deployment workflows are stable, evaluate Git-backed editors such as Decap CMS and Pages CMS.

Any editor must preserve the repository as the authoritative source.

Do not select an editor before evaluating:

- Authentication.
- GitHub permissions.
- Pull request workflows.
- Preview support.
- Media handling.
- Costs.
- Volunteer account turnover.
- Compatibility with existing structured data.

Avoid exposing arbitrary templates, Liquid code, or complex nested structures to routine editors.

## 9. Content Preservation and Editorial Authority

SIGCSE has decades of institutional history represented in this repository.

Preservation is a fundamental requirement.

Do not:

- Delete historical content because it is old.
- Delete files solely because no incoming link was detected.
- Delete duplicate assets without understanding their archival purpose.
- Rewrite official policies.
- Change approved award citations.
- Invent missing dates, names, roles, or organizational facts.
- Silently reconcile contradictory historical records.
- Change document access policies.
- Publish previously unpublished material.

Mechanical formatting improvements and unambiguous technical corrections are permitted.

Substantive factual or editorial changes require appropriate approval.

When conflicting information is discovered, record the discrepancy and identify the relevant source files.

The audit has already identified several such discrepancies, including missing 2026 award records and expired conference listings. Track these issues rather than silently inventing corrections.

### 9.1 Public URL Preservation

Capture a baseline manifest of generated public URLs before major refactoring.

Include:

- Pages.
- News posts.
- Historical conference pages.
- Documents.
- Images and downloadable assets.
- Existing redirects and aliases.
- Case-sensitive paths.

Preserve existing URLs wherever practical.

If a URL must change, implement and test a compatibility mechanism.

Do not remove existing redirects without verifying equivalent behavior.

### 9.2 Unpublished and Ignored Material

The audit identified locally present `_pending/` and `_unused/` directories containing material that is not tracked by Git.

Preserve these materials in their existing local locations pending an authorized archival decision.

Do not delete, publish, or automatically commit them.

Document that a fresh clone will not contain these files.

Ensure that audit reports, development documentation, unpublished content, dependency files, scripts, and other internal material are excluded from generated public output.

The audit directory is not currently excluded by the existing configurations. Address this before producing distributable website builds.

## 10. Automated Validation

Develop validation progressively.

Checks should include:

- Successful clean builds.
- YAML and front-matter validity.
- Required structured data fields.
- Duplicate identifiers.
- Invalid or inconsistent date formats.
- Missing referenced assets.
- Broken internal links.
- Case-sensitive path mismatches.
- Missing historical page references.
- Redirect failures or loops.
- Unexpected public URL removals.
- Missing page metadata.
- Accidental publication of internal files.
- Basic accessibility violations.
- Unexpected output changes.

Distinguish existing defects from newly introduced regressions.

Do not make the project impossible to advance by requiring immediate correction of every historical defect.

Maintain an explicit baseline of known issues and prevent new regressions.

Where practical, add editorial freshness checks for:

- Past conferences labeled upcoming.
- Expired Board or volunteer terms.
- Expired deadlines.
- Missing review dates.
- Inconsistent current information.

Freshness checks should flag content for review rather than delete it automatically.

Remember that date-dependent static content requires a rebuild to reflect the passage of time.

## 11. Development Phases

### Phase 0: Repository Audit

Status: Complete.

Use the existing audit reports as the starting point.

Do not repeat the entire audit unless a specific finding requires additional verification.

### Phase 1: Build and Deployment Foundation

Objectives:

- Protect internal and unpublished material from generated output.
- Establish a reproducible build.
- Capture the original rendered website baseline.
- Establish the public URL and asset manifest.
- Document local preview commands.
- Establish automated build and validation workflows.
- Develop a deployment approach compatible with existing ACM hosting.
- Document unresolved hosting requirements.
- Keep production deployment disabled.

Do not undertake a broad visual redesign or content migration during this phase.

### Phase 2: Content Ownership and Isolation

Objectives:

- Classify existing content by organizational ownership.
- Identify conference-specific content.
- Identify ambiguous ownership cases.
- Establish a conference directory data model.
- Design a conference legacy isolation strategy.
- Create conference-specific transfer manifests.
- Preserve all existing public content and URLs.

Do not remove or externally redirect conference-specific material.

### Phase 3: Repository and Template Refactoring

Objectives:

- Establish predictable content organization.
- Consolidate duplicated page shells.
- Simplify frontend dependencies.
- Consolidate appropriate structured data.
- Reduce routine maintenance complexity.
- Preserve historical snapshots.
- Maintain URL compatibility.
- Establish initial maintainer documentation.

Perform transformations incrementally and validate them against the baseline.

### Phase 4: Navigation and Visual Redesign

Objectives:

- Implement task-oriented navigation.
- Redesign the homepage.
- Promote organization-wide activities.
- Reduce navigation depth.
- Improve section navigation.
- Improve responsive behavior.
- Improve accessibility.
- Establish a consistent visual system.

Provide screenshots or a working preview for review.

### Phase 5: Search and Discovery

Objectives:

- Implement static site search.
- Improve page metadata.
- Establish archive navigation.
- Distinguish organizational and conference legacy results.
- Validate common information discovery tasks.

### Phase 6: Maintainer Tooling

Objectives:

- Complete `MAINTAINING.md`.
- Simplify routine update workflows.
- Expand structured data validation.
- Improve editorial freshness checks.
- Evaluate optional Git-backed visual editing.
- Test representative volunteer maintenance tasks.

### Phase 7: Production Readiness and Transition

Objectives:

- Resolve approved factual corrections.
- Complete URL compatibility validation.
- Test deployment against an authorized destination.
- Establish deployment credentials and permissions.
- Verify rollback.
- Complete accessibility and usability review.
- Obtain appropriate organizational approval.
- Enable production deployment only when authorized.

### Phase 8: Incremental Conference Transfers

This is a long-term follow-on activity.

As individual Steering Committees establish their own umbrella websites:

- Prepare the relevant transfer package.
- Verify destination content.
- Establish appropriate redirects.
- Update the organizational conference directory.
- Remove local legacy copies from public output only when authorized.
- Preserve archival copies and migration records.

Do not make completion of this phase a prerequisite for launching the modernized organizational website.

## 12. Agent Operating Instructions

### 12.1 Autonomy

Proceed independently on reversible technical decisions consistent with this document.

Examples include:

- Refactoring duplicated templates.
- Improving semantic HTML.
- Writing validation scripts.
- Establishing consistent naming conventions.
- Correcting unambiguous technical defects.
- Improving build documentation.
- Adding tests.
- Implementing approved architecture.

Do not interrupt the project owner for minor implementation preferences.

When multiple reasonable technical approaches exist, select the simplest maintainable approach and document the rationale.

### 12.2 Decisions Requiring Human Review

Seek approval for consequential decisions involving:

- Production deployment.
- DNS or hosting changes.
- New recurring costs.
- Substantive organizational content changes.
- Historical record deletion.
- Content ownership disputes.
- Changes to official branding.
- Changes to publication or access policies.
- Conference content removal or external redirects.
- Major departures from the agreed architecture.

Batch nonblocking questions into a review document.

Continue unrelated work while awaiting answers where practical.

### 12.3 Project Tracking

Maintain the following internal documents:

- `docs/PROJECT_STATUS.md`
- `docs/DECISION_LOG.md`
- `docs/OPEN_QUESTIONS.md`
- `docs/KNOWN_ISSUES.md`
- `docs/DEPLOYMENT.md`

Maintain additional technical documentation as needed.

Project status should identify:

- Current phase.
- Completed work.
- Remaining work.
- Tests performed.
- Known limitations.
- Blockers.
- Decisions requiring review.
- Recommended next steps.

The decision log should record significant architectural decisions and their rationale.

Keep these documents concise and current.

Ensure all internal documentation is excluded from public website output.

### 12.4 Git Practices

Work incrementally.

Use small, meaningful commits representing coherent changes.

Before committing:

- Review the diff.
- Check for unintended content changes.
- Run applicable tests.
- Check for accidentally included credentials or unpublished material.

Do not push to a remote repository unless explicitly authorized.

Do not rewrite Git history unnecessarily.

Do not commit generated website output unless an approved deployment architecture explicitly requires it.

### 12.5 Phase Checkpoints

At the end of each phase:

1. Run applicable validation.
2. Update project status.
3. Summarize completed work.
4. Identify deviations from the plan.
5. Identify remaining risks and blockers.
6. Provide preview instructions or screenshots where appropriate.
7. Stop for review before beginning the next major phase.

Do not treat this document as authorization to complete every phase in a single uninterrupted execution.

## 13. Project Success Criteria

The project is successful when:

- Routine website changes can be made through a GitHub pull request.
- Approved changes deploy automatically without manual local builds or file transfers.
- Maintainers can easily locate the source of commonly updated information.
- Common visitor tasks require minimal navigation.
- Search provides effective access to current and historical information.
- The website is modern, responsive, and accessible.
- Organization-wide content is clearly distinguished from conference-specific content.
- Conference-specific legacy material can be transferred independently.
- Historical records and existing public URLs are preserved.
- The website does not require unnecessary paid services or complex infrastructure.
- Future SIGCSE volunteers can maintain the website without relying on undocumented institutional knowledge.

The ultimate objective is not merely a better-looking website.

It is a sustainable organizational website that is easier to use, easier to maintain, and appropriately scoped to the responsibilities of ACM SIGCSE.

## 14. Approved Phase 4B Design Direction (2026-11-26)

The owner approved Concept B, Professional Community, for the site-wide visual
implementation. Use welcoming sans-serif typography, authentic existing SIGCSE
photography, compact spacing, and task-oriented content presentation. Adopt
Concept C's solid blue primary navigation and clear active-section treatment.
Preserve official logos; remove redundant organization-name text beside the logo,
uppercase title eyebrows, generic marketing slogans and prototype controls.

Use reusable patterns for community/section pages, funding applications, awards
and recipient histories, people/conference directories, news, policies and archives.
Keep reference material compact. Summaries and detailed guidance must share one
editable source for facts. Use a neutral reserved header location for future
search, without implementing or pretending to implement Phase 5 search.

The homepage must give all SIGCSE conferences equal visual treatment, ordering
dated upcoming events chronologically and excluding concluded events at rebuild.
Use published end dates where available; never invent precise dates from TBD or
month-only records. Preserve historical records and flag missing/conflicting data.

Complete responsive/accessibility, breadcrumb/navigation, link, preservation and
task-depth validation; provide desktop/mobile screenshots, update documentation,
commit and ordinarily push to the authorized GitHub repository. GitHub Pages was
disabled with separate owner authorization and must remain disabled. Do not change
DNS, deploy to production, implement a CMS or begin Phase 5. Stop for owner review
after completing Phase 4B.

## 15. Phase 4C — Community Engagement Refinement

Phase 4B's identity and information architecture are substantially approved.
Retain three purpose-based presentations: welcoming community landing pages,
action-oriented program pages and compact reference pages. Refine only home
conference cards, membership, conference directory, awards directory, committees
and news density. Preserve approved reference, funding and historical pages.
Keep existing dated statistics and approved benefit descriptions authoritative;
summaries must derive from those sources. Do not invent benefits or conference
facts. Use existing branding or neutral text fallbacks. Provide desktop/mobile
before-and-after comparisons, run local/hosted checks, commit and push with
publication disabled, and stop for owner review after Phase 4C. Phase 5, CMS,
deployment and DNS work remain outside scope.


## Authorized GitHub Pages preview (2026-11-26)

Phases 5–6 are approved. The owner explicitly authorized Actions-only publication
to https://sigcsets.github.io/sigcse-org/ (no custom domain). This supersedes earlier
Pages-disabled checkpoint notes for this preview only. Main pushes and manual
dispatch publish only after the pinned live/staging/Pages validation and real
search tests pass. PRs/other branches cannot deploy. Only the gated deployment job
receives Pages/OIDC write, with serialized deployment concurrency.
Use _config_live.yml plus _config_github_pages.yml, the complete Pagefind bundle,
public-output validation, preview indicator/noindex and CNAME removal/rejection.
Existing live/staging/local configs are preserved. ACM production remains
literally disabled. No ACM contact, DNS/custom domain, visual redesign, substantive
editorial corrections or CMS work is authorized. Perform actual hosted smoke tests,
report evidence/blockers and stop for owner review. See docs/PAGES_PREVIEW.md
(PAGES_PREVIEW.md from this docs directory) for operation and evidence.
