"""Offline public-output validation, preservation manifests and release packaging.

Uses only Python's standard library. Run from the repository root.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import tarfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASELINES = ROOT / 'docs/baselines'
PRIVATE = {'audit', 'docs', 'scripts', 'tests', 'artifacts', 'vendor', 'bin',
           '_pending', '_unused', '_development', '_documentation',
           'AGENTS.md', 'README.md', 'MAINTAINING.md', 'Gemfile', 'Gemfile.lock',
           'gemfile', 'gemfile.lock', 'node_modules', 'package.json',
           'pnpm-lock.yaml', 'pagefind.yml', 'test-results'}


def internal(path):
    parts = Path(path).parts
    return bool(parts) and (parts[0] in PRIVATE or any(p.startswith(('.', '_')) for p in parts))


def files(site):
    return {p.relative_to(site).as_posix(): p for p in sorted(site.rglob('*')) if p.is_file()}


def manifest(site):
    return {name: {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                   'bytes': p.stat().st_size}
            for name, p in files(site).items() if not internal(name)}


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.refs, self.ids, self.issues, self.redirects = [], set(), set(), []
        self.has_title = self.has_h1 = self.lang = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            if a['id'] in self.ids:
                self.issues.add('duplicate-id:' + a['id'])
            self.ids.add(a['id'])
        if tag == 'a' and a.get('name'):
            self.ids.add(a['name'])
        if tag == 'html':
            self.lang = bool(a.get('lang'))
        self.has_title |= tag == 'title'
        self.has_h1 |= tag == 'h1'
        if tag == 'img' and 'alt' not in a:
            self.issues.add('image-without-alt:' + a.get('src', ''))
        if tag == 'iframe' and not a.get('title'):
            self.issues.add('iframe-without-title:' + a.get('src', ''))
        for key in ('href', 'src', 'poster'):
            if a.get(key):
                self.refs.append(a[key])
        if a.get('srcset'):
            self.refs.extend(v.strip().split()[0] for v in a['srcset'].split(',') if v.strip())
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url\s*=\s*(.*)', a.get('content', ''), re.I)
            if match:
                target = match[1].strip(' \"\'')
                self.redirects.append(target)
                self.refs.append(target)


def local_target(source, ref, baseurl=''):
    target = urlsplit(urljoin('https://sigcse.org/' + source.lstrip('/'), ref))
    if target.scheme not in ('http', 'https') or target.hostname not in ('sigcse.org', 'www.sigcse.org', '127.0.0.1', 'localhost'):
        return None
    path = unquote(target.path)
    if baseurl and (path == baseurl or path.startswith(baseurl + '/')):
        path = path[len(baseurl):] or '/'
    path = path.lstrip('/')
    if not path or path.endswith('/'):
        path += 'index.html'
    return path, unquote(target.fragment)


def inspect(site, baseurl=''):
    output = files(site)
    pages = {n: Page(p.read_text(encoding='utf-8', errors='replace'))
             for n, p in output.items() if n.endswith('.html')}
    issues = set()
    redirects = {}
    for name, page in pages.items():
        for label, present in [('missing-title', page.has_title), ('missing-h1', page.has_h1),
                               ('missing-lang', page.lang)]:
            if not present:
                issues.add(f'{name} | {label}')
        issues.update(f'{name} | {issue}' for issue in page.issues)
        source = baseurl + '/' + name if baseurl else name
        for ref in page.refs:
            dest = local_target(source, ref, baseurl)
            if dest is None:
                continue
            path, fragment = dest
            if path not in output and path + '/index.html' in output:
                path += '/index.html'
            if path not in output:
                issues.add(f'{name} | missing-target:{path}')
            elif fragment and path in pages and fragment not in pages[path].ids:
                issues.add(f'{name} | missing-fragment:{path}#{fragment}')
        for ref in page.redirects:
            dest = local_target(source, ref, baseurl)
            if dest:
                redirects[name] = dest[0]
    for start in redirects:
        seen, current = set(), start
        while current in redirects:
            if current in seen:
                issues.add(f'{start} | redirect-cycle')
                break
            seen.add(current)
            current = redirects[current]
    # Check local CSS url() and source-map references too.
    for name, path in output.items():
        if name.endswith('.css'):
            for ref in re.findall(r'url\([\"\']?([^\)\"\']+)', path.read_text(encoding='utf-8', errors='replace')):
                dest = local_target(name, ref)
                if dest and dest[0] not in output:
                    issues.add(f'{name} | missing-target:{dest[0]}')
    return sorted(issues), redirects


def validate(site, baseurl=''):
    if not (site / 'index.html').is_file():
        raise ValueError('Build missing index.html')
    output = files(site)
    leaked = [n for n in output if internal(n)]
    if leaked:
        raise ValueError('Internal files in public output: ' + ', '.join(leaked[:20]))
    baseline = json.loads((BASELINES / 'public-files.json').read_text(encoding='utf-8'))
    missing = sorted(set(baseline) - set(output))
    if missing:
        raise ValueError('Public URLs removed (case-sensitive): ' + ', '.join(missing[:20]))
    issues, redirects = inspect(site, baseurl)
    known = set(json.loads((BASELINES / 'known-output-issues.json').read_text(encoding='utf-8')))
    new = sorted(set(issues) - known)
    expected_redirects = json.loads((BASELINES / 'redirects.json').read_text(encoding='utf-8'))
    changed = {k: v for k, v in expected_redirects.items() if redirects.get(k) != v}
    report = {'files': len(output), 'html': sum(n.endswith('.html') for n in output),
              'existing_issues': len(set(issues) & known), 'new_issues': new,
              'resolved_issues': sorted(known - set(issues)), 'changed_redirects': changed,
              'added_urls': sorted(set(output) - set(baseline)),
              'changed_files': sorted(n for n in baseline if n in output and
                  hashlib.sha256(output[n].read_bytes()).hexdigest() != baseline[n]['sha256'])}
    save(ROOT / 'artifacts/validation.json', report)
    print(f"Validated {report['files']} files, {report['html']} HTML pages; "
          f"{report['existing_issues']} baseline issues, {len(new)} new issues")
    if new or changed:
        raise ValueError('Regressions: ' + json.dumps({'new': new[:20], 'redirects': changed}))
    return report


def capture(site):
    if (BASELINES / 'public-files.json').exists():
        raise ValueError('Baseline already exists; changes require deliberate review')
    public = manifest(site)
    save(BASELINES / 'public-files.json', public)
    # Inspect only sanitized public output; never package internal raw build output.
    sanitized = ROOT / '_baseline_public'
    if sanitized.exists():
        raise ValueError('Baseline output directory already exists')
    for name in public:
        dest = sanitized / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(site / name, dest)
    issues, redirects = inspect(sanitized)
    save(BASELINES / 'known-output-issues.json', issues)
    save(BASELINES / 'redirects.json', redirects)
    print(f'Captured {len(public)} public files and {len(issues)} existing issues')


def package(site, name):
    validate(site)
    dest = ROOT / 'artifacts' / name
    with tarfile.open(dest, 'w:gz') as archive:
        for path, source in files(site).items():
            if source.is_symlink():
                raise ValueError('Symlinks cannot enter release artifacts')
            archive.add(source, arcname=path, recursive=False)
    checksum = hashlib.sha256(dest.read_bytes()).hexdigest()
    dest.with_suffix(dest.suffix + '.sha256').write_text(f'{checksum}  {dest.name}\n', encoding='ascii')
    save(dest.with_suffix('.manifest.json'), manifest(site))
    print(f'Created {dest.name} ({dest.stat().st_size} bytes), SHA-256 {checksum}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['capture', 'validate', 'package'])
    parser.add_argument('--site', type=Path, default=ROOT / '_site')
    parser.add_argument('--baseurl', default='')
    parser.add_argument('--name', default='site.tar.gz')
    args = parser.parse_args()
    try:
        if args.command == 'capture':
            capture(args.site)
        elif args.command == 'validate':
            validate(args.site, args.baseurl)
        else:
            if Path(args.name).name != args.name:
                raise ValueError('Artifact name must be a filename')
            package(args.site, args.name)
    except (ValueError, OSError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
