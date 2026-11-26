import hashlib
import importlib.util
import io
import tarfile
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('release', Path(__file__).resolve().parents[1] / 'scripts/release_demo.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_reject_tampered_artifact_and_archive_traversal(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive = root / 'site.tar.gz'
            with tarfile.open(archive, 'w:gz') as tar:
                info = tarfile.TarInfo('../escape')
                info.size = 1
                tar.addfile(info, io.BytesIO(b'x'))
            with self.assertRaisesRegex(ValueError, 'checksum'):
                release.unpack_verified(archive, 'invalid', {}, root / 'one')
            sha = hashlib.sha256(archive.read_bytes()).hexdigest()
            with self.assertRaisesRegex(ValueError, 'Unsafe'):
                release.unpack_verified(archive, sha, {}, root / 'two')
            self.assertFalse((root / 'escape').exists())

    def test_reject_missing_and_corrupt_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive = root / 'site.tar.gz'
            with tarfile.open(archive, 'w:gz') as tar:
                info = tarfile.TarInfo('index.html')
                info.size = 1
                tar.addfile(info, io.BytesIO(b'x'))
            sha = hashlib.sha256(archive.read_bytes()).hexdigest()
            record = {'bytes': 1, 'sha256': hashlib.sha256(b'x').hexdigest()}
            with self.assertRaisesRegex(ValueError, 'Incomplete'):
                release.unpack_verified(archive, sha, {'index.html': record, 'other': record}, root / 'one')
            with self.assertRaisesRegex(ValueError, 'integrity'):
                release.unpack_verified(archive, sha, {'index.html': {'bytes': 2, 'sha256': 'wrong'}}, root / 'two')


if __name__ == '__main__':
    unittest.main()
