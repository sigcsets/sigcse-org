"""Regenerate the internal ownership inventory and conference transfer manifests."""
import csv
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERIES = ['symposia', 'iticse', 'icer', 'comped', 'respect', 'virtual']
HEADS = {'symposia': 'symposium', **{s: s for s in SERIES if s != 'symposia'}}
PUBLIC_ROOTS = {'about', 'events', 'membership', 'news', 'policies', 'programs', 'resources',
                'siteindex', 'assets', 'files', '_posts', '_data', '_layouts', '_includes', 'content'}


def main():
    paths = sorted(set(subprocess.check_output(['git', 'ls-files', '-co', '--exclude-standard', '-z'], cwd=ROOT)
                       .decode().strip('\0').split('\0')))
    original = {r['source_path']: r for r in csv.DictReader((ROOT / 'audit/CONTENT_INVENTORY.csv').open(encoding='utf-8-sig'))}
    rows = []
    for path in paths:
        if not (ROOT / path).is_file():
            continue
        category, series, reason = 'organizational', '', ''
        if path.split('/')[0] not in PUBLIC_ROOTS and path not in ('index.md', 'favicon.ico'):
            category = 'internal-support'
        if path.startswith(('assets/', '_layouts/', '_includes/')):
            category = 'shared-presentation'
        for s in SERIES:
            if path.startswith((f'events/{s}/', f'content/conference-legacy/{s}/')) or path == f'_data/{s}.yml' or path == f'_includes/{HEADS[s]}-head.md':
                category, series = 'conference-legacy', s
        if path in ('_data/conferences.yml', '_data/events.yml'):
            category = 'conference-directory'
        logical = path.removeprefix('content/organization/')
        if logical.startswith(('policies/TS-', 'policies/icer', 'policies/iticse')) or logical in (
                'events/bestpapers.md', '_data/bestpapers.yml', 'events/workinggroups/index.md',
                '_data/workinggroups.yml', 'events/dc.md', 'policies/corporate.md'):
            category, reason = 'ownership-review', 'Conference-specific subject; confirm Board versus Steering Committee authority before transfer.'
        if logical.startswith('policies/') and not reason:
            reason = 'Keep integrated under organizational governance pending policy-by-policy authority review.'
        url = original.get(path, {}).get('public_url', '')
        if path.startswith('content/') and path.endswith(('.md', '.html')):
            match = re.search(r'^permalink:\s*[\"\']?([^\s\"\']+)', (ROOT / path).read_text(encoding='utf-8'), re.M)
            if match:
                url = match[1]
        rows.append(dict(source_path=path, classification=category, conference=series, public_url=url, review=reason))
    out = ROOT / 'docs/content'
    out.mkdir(parents=True, exist_ok=True)
    with (out / 'ownership.csv').open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    for s in SERIES:
        selected = [r for r in rows if r['conference'] == s]
        manifest = {'conference': s, 'status': 'preserved locally; transfer not authorized',
                    'files': [r['source_path'] for r in selected],
                    'public_urls': sorted(r['public_url'] for r in selected if r['public_url']),
                    'data_records': [f'_data/{s}.yml: conferences and committees', f'_data/conferences.yml: id={s}'],
                    'templates': [f'_includes/{HEADS[s]}-head.md'],
                    'assets': [r['source_path'] for r in selected if not r['source_path'].endswith(('.md', '.html', '.yml'))],
                    'shared_dependencies': ['_layouts/default.html', '_layouts/page.html', '_data/conferences.yml',
                        '_includes/awards.md', '_data/outstanding.yml', '_data/distinguished.yml',
                        '_data/broadening.yml', '_data/policies.yml', 'assets/css/', 'assets/js/',
                        'assets/images/logo/', '_includes/item.md'],
                    'notes': 'Assets remain at stable public paths. Include only the required shared records after human ownership review; do not transfer all organizational award data.'}
        (out / f'{s}-transfer.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'Classified {len(rows)} tracked/proposed files; wrote six transfer manifests')


if __name__ == '__main__':
    main()
