import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('site_checks', Path(__file__).resolve().parents[1] / 'scripts/site.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class PreservationTests(unittest.TestCase):
    def test_internal_boundary(self):
        for name in ['audit/report.html', '_pending/draft.html', 'docs/status.html',
                     'Gemfile.lock', '.git/config', 'assets/.secret']:
            self.assertTrue(checks.internal(name), name)
        self.assertFalse(checks.internal('about/reports/2024.pdf'))
        self.assertFalse(checks.internal('assets/js/vendor/holder.min.js'))
        self.assertFalse(checks.internal('files/documents/docs/SpecialProjectsApp.doc'))

    def test_links_case_fragments_and_redirect_cycles(self):
        with tempfile.TemporaryDirectory() as temp:
            site = Path(temp)
            (site / 'index.html').write_text('<html lang="en"><title>A</title><h1>A</h1>'
                '<a href="Target.html#yes">OK</a><a href="target.html">Wrong case</a>'
                '<a href="Target.html#no">Missing anchor</a>'
                '<img src="missing.png"><meta http-equiv="refresh" content="0;url=Target.html">')
            (site / 'Target.html').write_text('<html lang="en"><title>B</title><h1 id="yes">B</h1>'
                '<meta http-equiv="refresh" content="0;url=index.html">')
            issues, redirects = checks.inspect(site)
            self.assertIn('index.html | missing-target:target.html', issues)
            self.assertIn('index.html | missing-fragment:Target.html#no', issues)
            self.assertIn('index.html | missing-target:missing.png', issues)
            self.assertIn('index.html | redirect-cycle', issues)
            self.assertEqual(redirects['index.html'], 'Target.html')

    def test_baseurl_and_external_links(self):
        self.assertEqual(checks.local_target('/.staging/about/index.html', '../news/', '/.staging'), ('news/index.html', ''))
        self.assertEqual(checks.local_target('index.html', '/a%20b.pdf'), ('a b.pdf', ''))
        self.assertIsNone(checks.local_target('index.html', 'mailto:someone@example.org'))
        self.assertIsNone(checks.local_target('index.html', 'https://example.org/'))

    def test_validation_rejects_leaks_removed_urls_and_new_defects(self):
        previous_root, previous_baselines = checks.ROOT, checks.BASELINES
        try:
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                checks.ROOT, checks.BASELINES = root, root / 'baselines'
                checks.BASELINES.mkdir()
                site = root / 'site'
                site.mkdir()
                home = site / 'index.html'
                good = '<html lang="en"><title>Home</title><h1>Home</h1></html>'
                home.write_text(good)
                checks.save(checks.BASELINES / 'public-files.json', checks.manifest(site))
                checks.save(checks.BASELINES / 'known-output-issues.json', [])
                checks.save(checks.BASELINES / 'redirects.json', {})
                checks.validate(site)
                (site / 'docs').mkdir()
                leak = site / 'docs/private.html'
                leak.write_text('private')
                with self.assertRaisesRegex(ValueError, 'Internal files'):
                    checks.validate(site)
                leak.unlink()
                home.write_text(good + '<a href="lost.pdf">Download</a>')
                with self.assertRaisesRegex(ValueError, 'Regressions'):
                    checks.validate(site)
                home.write_text(good)
                manifest = checks.manifest(site)
                manifest['lost.pdf'] = {'sha256': '', 'bytes': 0}
                checks.save(checks.BASELINES / 'public-files.json', manifest)
                with self.assertRaisesRegex(ValueError, 'Public URLs removed'):
                    checks.validate(site)
        finally:
            checks.ROOT, checks.BASELINES = previous_root, previous_baselines


if __name__ == '__main__':
    unittest.main()
