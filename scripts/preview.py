"""Serve the already-built local preview: python scripts/preview.py (Ctrl+C stops)."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

site = Path(__file__).resolve().parents[1] / '_site'
if not (site / 'index.html').is_file():
    raise SystemExit('Build first: bundle exec ruby scripts/build.rb preview')
print('Local SIGCSE preview: http://127.0.0.1:8765/ (Ctrl+C to stop)', flush=True)
try:
    ThreadingHTTPServer(('127.0.0.1', 8765), partial(SimpleHTTPRequestHandler, directory=str(site))).serve_forever()
except KeyboardInterrupt:
    pass
