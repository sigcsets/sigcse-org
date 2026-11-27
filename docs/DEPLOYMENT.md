> Phase 4B update: GitHub Pages was disabled with explicit owner authorization before replacing experimental repository history. DNS was not changed. No production deployment is authorized. See GITHUB.md.

> Owner decision (2026-11-26): deployment and hosting investigation are deferred. The proposal below is retained for future reference; no action or answers are currently requested.

# ACM deployment proposal — disabled

No production connection, transfer, credential setup, DNS or server modification
has been performed. No host or production destination is configured.
`.github/workflows/deploy.yml` has only manual dispatch and a literal false job
condition. It cannot deploy even if secrets or repository variables are added.
The validation workflow only builds downloadable artifacts.

## Preferred mechanism, conditional on ACM confirmation

Keep ACM hosting and DNS. A future protected workflow builds and validates the
merged production commit with the same frozen dependencies. Use a configurable
repository variable `PRODUCTION_BRANCH` to gate a push job; require the selected
branch's review/required checks and a protected `acm-production` environment.
Default `PRODUCTION_DEPLOYMENT_ENABLED` to false. Enable only through an authorized
implementation PR after disposable-destination and rollback tests. Do not deploy
PR artifacts: rebuild the exact authorized merged commit without PR credentials.

If ACM provides a POSIX shell, an isolated release root and same-filesystem atomic
symlink replacement:

1. Acquire workflow concurrency lock (cancel-in-progress false) and a host-side
   lock covering transfer, activation, verification and rollback. Fail if locked.
2. Use an ACM-approved restricted deployment account/key, an explicitly configured
   hostname/port, and verified known_hosts supplied through a protected environment.
   Use StrictHostKeyChecking=yes, BatchMode=yes, no agent forwarding, no shell trace,
   no passwords in command lines. Obtain the fingerprint independently from ACM;
   do not trust a runtime ssh-keyscan result as identity verification.
3. Validate a dedicated absolute destination against an administrator-confirmed
   allowlist. Reject empty/root paths and shell metacharacters in configuration;
   use structured arguments. The root must contain only site releases. Never
   synchronize into a shared home directory or assume the current document root.
4. Upload the validated archive, digest and file manifest into a new unique staging
   directory. Use SFTP/scp or rsync over SSH, according to ACM support; no --delete.
   Verify transfer status, archive digest and every extracted file's digest/size.
   Reject archive traversal, symlinks, missing and unexpected members.
5. Finalize an immutable release directory named by commit and run ID. Record the
   old active target, then replace the current symlink using a temporary link and
   an atomic same-filesystem rename. Do not assume a particular `mv` option exists.
   ACM must first approve document-root/symlink arrangements.
6. Verify HTTP(S) content at the actual public location: a release-specific digest
   marker with cache bypass plus the homepage, representative archive/download,
   case-sensitive URLs and redirects. A successful SSH exit is insufficient.
7. On verification failure, atomically restore the recorded previous target and
   verify it. If activation/rollback status is uncertain, stop and alert the owner.
   Retain both releases and logs; never delete unrelated host content.

Rollback should also be a protected, manually invoked workflow selecting an
existing verified release. Retention/pruning requires an explicit ACM-approved
policy and must always preserve active and rollback releases. Phase 1 includes
no remote activation, rollback or pruning commands because capabilities are unknown.

## Alternatives

- If outbound access from GitHub-hosted runners is prohibited, use an ACM-approved
  internal deployment service/runner for the deployment job only. Untrusted PRs
  must still build on isolated runners without production credentials. Do not
  introduce new infrastructure until ACM confirms it is necessary and supported.
- If only SFTP is supported, ask ACM about atomic directory rename and document-root
  activation. Stage a full release and validate it first. If no atomic activation
  exists, obtain an approved maintenance window/backup and documented ordered
  transfer/recovery procedure. Do not claim atomicity or run destructive sync.
- An ACM-supported deployment service is preferable if it already supplies staging,
  identity checks, activation and rollback. Obtain its interface and guarantees.

## Local proof of the release model

On Linux after packaging:

```sh
python scripts/release_demo.py artifacts/site.tar.gz
```

This always creates a disposable temporary destination. It checks artifact and
per-file integrity, creates versioned directories, exercises atomic symlink
activation, verifies content and rolls back. It cannot contact a server. It proves
the local POSIX model only, not ACM network, filesystem, HTTP or cache behavior.
CI runs it for every successfully packaged live build. Tests also reject tampered,
incomplete, corrupt and traversal archives. No production credentials are needed.

## Questions for the ACM webmaster/hosting administrator

1. What are the canonical source repository and approved production branch? Who
   approves content, deployments, host changes and emergency rollbacks?
2. Which hostname/port/account and exact absolute document-root/destination paths
   are authorized? What unrelated files, server rules and permissions must remain?
3. Which authentication methods and restricted keys/accounts are supported? How
   are keys rotated and volunteers offboarded? Supply verified host fingerprints
   via an approved channel when deployment setup is authorized, not in this repo.
4. Can GitHub-hosted runners connect? Are IP allowlists, VPN/MFA or an internal
   deployment service mandatory? Is an ACM-managed runner available if required?
5. Are SSH shell, SFTP, scp and/or rsync available? Which versions? Are tar, SHA-256,
   locking and a suitable runtime available for verification? Are there quotas?
6. Are same-filesystem atomic rename, symlink document roots and release directories
   supported and permitted? Who can configure that initial arrangement?
7. How are TLS, redirects, extensionless/index URLs, path case, caches and headers
   handled? Which safe endpoint can identify the active release after activation?
8. What nonproduction destination may we test? What are backup/retention, failure
   notification, acceptable downtime and recovery requirements?

These are nonblocking for local builds/CI. Actual remote deployment remains blocked
until answered, implemented, tested and explicitly authorized in Phase 7.


## Search artifact requirement (Phases 5–6)

All standard builds now generate a pinned Pagefind static bundle under pagefind/.
Future releases must upload that complete folder with the HTML from the same
build. The live/staging browser suite verifies same-host/prefix asset requests and
result destinations. Verify .js/.wasm serving, CSP and cache invalidation on an
explicitly authorized test destination before production enablement. Nothing in
these phases enables production or changes the literal disabled workflow guard.


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
