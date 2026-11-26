"""Check the agreed visitor tasks remain within two local link selections."""
import importlib.util
import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('site_checks', ROOT / 'scripts/site.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)
site = ROOT / '_site'
pages = {name: checks.Page(path.read_text(encoding='utf-8', errors='replace'))
         for name, path in checks.files(site).items() if name.endswith('.html')}
distances, queue = {'index.html': 0}, deque(['index.html'])
while queue:
    current = queue.popleft()
    if distances[current] >= 2:
        continue
    for ref in pages[current].refs:
        target = checks.local_target(current, ref)
        if not target:
            continue
        path = target[0]
        if path not in pages and path + '/index.html' in pages:
            path += '/index.html'
        if path in pages and path not in distances:
            distances[path] = distances[current] + 1
            queue.append(path)
tasks = {
    'Conferences': 'conferences/index.html',
    'Join SIGCSE': 'membership/join.html',
    'Special Projects': 'programs/special/index.html',
    'Travel grants': 'programs/travel-grants/index.html',
    'Award nominations': 'programs/awards/outstanding-and-distinguished-nomination.html',
    'Award recipients': 'programs/awards/outstanding.html',
    'Board contacts': 'about/board.html',
    'Board minutes': 'about/reports/board.html',
    'Chair reports': 'about/reports/chair.html',
    'Policies': 'policies/index.html',
    'Get involved': 'get-involved/index.html',
    'Committees': 'programs/committees-task-forces/index.html',
    'Resources': 'resources/index.html',
}
report = {task: distances.get(path) for task, path in tasks.items()}
checks.save(ROOT / 'artifacts/task-paths.json', report)
print(json.dumps(report, indent=2))
if any(value is None or value > 2 for value in report.values()):
    raise SystemExit('Visitor task exceeds two selections')
