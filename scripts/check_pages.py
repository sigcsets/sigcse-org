"""Additional fail-closed policy for the authorized Pages artifact."""
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import importlib.util
spec = importlib.util.spec_from_file_location('site_checks', Path(__file__).with_name('site.py'))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)
root = Path(__file__).resolve().parents[1]
site = root / '_site'
origin = 'https://sigcsets.github.io'
prefix = '/sigcse-org'
errors = []
for name, path in checks.files(site).items():
    if path.is_symlink() or checks.internal(name) or name == 'CNAME':
        errors.append('Forbidden publication: ' + name)
    if not name.endswith('.html'):
        continue
    html = path.read_text(encoding='utf-8')
    if '<meta name="robots" content="noindex, nofollow, noarchive">' not in html:
        errors.append('Missing noindex: ' + name)
    for ref in checks.Page(html).refs:
        target = urlsplit(urljoin(origin + prefix + '/' + name, ref))
        if target.hostname == 'sigcsets.github.io' and not target.path.startswith(prefix + '/'):
            errors.append(f'{name}: escaped preview prefix: {ref}')
# Complete engine and all generated fragments must be included, not only the UI.
for name in ['pagefind.js', 'pagefind-ui.js', 'pagefind-ui.css', 'pagefind-entry.json']:
    if not (site / 'pagefind' / name).is_file():
        errors.append('Missing Pagefind asset: ' + name)
for pattern in ['wasm.*.pagefind', 'index/*', 'fragment/*']:
    if not list((site / 'pagefind').glob(pattern)):
        errors.append('Incomplete Pagefind bundle: ' + pattern)
if (site / 'robots.txt').read_text() != 'User-agent: *\nDisallow: /\n':
    errors.append('Missing robots disallow')
report = {'errors': sorted(set(errors)), 'files': len(checks.files(site)), 'prefix': prefix, 'origin': origin}
checks.save(root / 'artifacts/pages-policy.json', report)
if errors:
    raise SystemExit('\n'.join(report['errors']))
print('PASS: Pages publication boundary, noindex, prefix and complete search bundle')
