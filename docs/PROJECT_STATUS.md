# Project status

Updated 2026-11-26. Phase 1 approved. Phases 2–4 authorized in sequence with interim review stops waived. Production deployment deferred; no hosting/DNS/credential investigation.

## Phase 2 — content ownership and isolation

Created a complete source ownership inventory and six conference transfer manifests in `docs/content/`. Added the concise conference directory schema with validated IDs and references to existing schedule data. Shared policies, awards, Working Groups and other ambiguous cases are documented for later human review. No content or public URL removed; physical isolation follows incrementally in Phase 3.

Validation passed on case-sensitive Linux: 1,064 public files and all 19 redirects preserved with zero new findings. Phase 2 complete.

## Repository access

Configured `origin` as `git@github.com:sigcsets/sigcse-org.git`. Read-only inspection found existing `main` at `36cff9e6` (commit message: “Update CNAME”). Under the owner's nonempty-remote instruction, nothing was pushed or overwritten. Hosted validation awaits a decision about integrating this independent history with that existing repository; local work continues.

## Owner decisions

Existing original-site backup is sufficient; retain regression baselines, no additional owner-managed archive required. Ordinary pushes authorized subject to nonempty-remote restriction. Stop at Phase 4 for review. No production changes, paid services, CMS, or substantive factual corrections authorized.

## Phase 3 — repository and templates

Moved 279 published page sources into organizational and per-conference directories with explicit unchanged permalinks. Centralized six schedules. Added a shared HTML shell with page titles, h1, skip link, correct byline handling and archive labels. Removed duplicate active Bootstrap/CDN/jQuery/Holder loads after checking references; retained all old public assets and standalone publications. Updated maintainer paths and regenerated ownership/transfer manifests. Validation passed on clean Linux: all 1,064 public files and 19 redirects preserved; zero new findings and 364 remaining original findings (497 resolved by the shared shell). Six regression tests pass. Phase 3 complete; proceeding to Phase 4.
