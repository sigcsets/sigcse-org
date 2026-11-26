"""Exercise release verification, atomic activation and rollback locally on Linux.

No network support or production destination exists in this program. It always
uses a new temporary directory. The SSH proposal remains in docs/DEPLOYMENT.md.
"""
import argparse
import hashlib
import json
import os
import tarfile
import tempfile
from pathlib import Path, PurePosixPath


def unpack_verified(archive_path, expected_sha, manifest, destination):
    if hashlib.sha256(archive_path.read_bytes()).hexdigest() != expected_sha:
        raise ValueError('Artifact checksum mismatch')
    destination.mkdir()
    seen = set()
    with tarfile.open(archive_path, 'r:gz') as archive:
        for entry in archive:
            path = PurePosixPath(entry.name)
            if not entry.isfile() or path.is_absolute() or '..' in path.parts or '\\' in entry.name:
                raise ValueError('Unsafe archive member')
            if entry.name not in manifest or entry.name in seen:
                raise ValueError('Unexpected or duplicate archive member')
            seen.add(entry.name)
            content = archive.extractfile(entry).read()
            expected = manifest[entry.name]
            if len(content) != expected['bytes'] or hashlib.sha256(content).hexdigest() != expected['sha256']:
                raise ValueError('Release file integrity failure: ' + entry.name)
            target = destination.joinpath(*path.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    if seen != set(manifest):
        raise ValueError('Incomplete release')


def activate(root, release):
    candidate = root / 'current.next'
    candidate.symlink_to(release, target_is_directory=True)
    os.replace(candidate, root / 'current')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    args = parser.parse_args()
    archive = args.archive.resolve()
    expected = archive.with_suffix(archive.suffix + '.sha256').read_text().split()[0]
    manifest = json.loads(archive.with_suffix('.manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix='sigcse-release-demo-') as temp:
        root = Path(temp)
        prior = root / 'release-before'
        prior.mkdir()
        (prior / 'index.html').write_text('previous release')
        activate(root, prior)
        release = root / 'release-candidate'
        unpack_verified(archive, expected, manifest, release)
        activate(root, release)
        assert (root / 'current/index.html').read_bytes() == (release / 'index.html').read_bytes()
        activate(root, prior)
        assert (root / 'current/index.html').read_text() == 'previous release'
        assert release.is_dir() and prior.is_dir()
    print('PASS: local integrity verification, versioned release activation and rollback; no network access')


if __name__ == '__main__':
    main()
