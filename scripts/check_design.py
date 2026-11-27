"""Check the approved shared visual system and readable color pairs offline."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('site_checks', ROOT / 'scripts/site.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


def luminance(color):
    values = [int(color[i:i+2], 16)/255 for i in (1, 3, 5)]
    values = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
    return sum(v*w for v, w in zip(values, [.2126, .7152, .0722]))


def ratio(first, second):
    high, low = sorted([luminance(first), luminance(second)], reverse=True)
    return (high+.05)/(low+.05)


palette = dict(re.findall(r'--(blue|deep|ink|muted|pale|warm):(#[0-9a-fA-F]{6})', (ROOT / 'assets/css/site.css').read_text(encoding='utf-8')))
pairs = {'body on white': (palette['ink'], '#ffffff'), 'links on white': (palette['blue'], '#ffffff'),
         'muted text on white': (palette['muted'], '#ffffff'), 'navigation/button text': ('#ffffff', palette['blue']),
         'active navigation': ('#ffffff', '#123f64'), 'facts on pale blue': (palette['deep'], palette['pale']),
         'caption on pale blue': (palette['muted'], palette['pale']), 'body on warm photo introduction': (palette['ink'], palette['warm']),
         'notice text': ('#584217', '#fff5df'), 'primary focus ring': ('#ffffff', palette['blue'])}
contrast = {name: round(ratio(*colors), 2) for name, colors in pairs.items()}
assert all(value >= 4.5 for value in contrast.values()), contrast
site = ROOT / '_site'
home = (site / 'index.html').read_text(encoding='utf-8')
assert 'concept-toolbar' not in home and 'Compare concepts' not in home
assert 'Explore SIGCSE' in home and 'Share ideas. Support each other.' not in home
assert 'header-search-slot' in home and 'role="search"' in home, 'search uses the approved reserved header space'
for name in ['about/board.html', 'programs/special/index.html', 'policies/index.html', 'events/symposia/2025.html']:
    text = (site / name).read_text(encoding='utf-8')
    assert 'class="eyebrow"' not in text, name
    assert 'aria-current="location"' in text, name
    assert 'aria-label="Breadcrumb"' in text and '<ol>' in text, name
    assert 'Skip to main content' in text, name
checks.save(ROOT / 'artifacts/design-checks.json', {'contrast': contrast, 'checks': 'passed'})
print(json.dumps(contrast, indent=2))
print('PASS: shared visual system, navigation, prototype exclusion and palette text contrast')
