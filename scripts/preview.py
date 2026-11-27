"""Serve the already-built local preview: python scripts/preview.py (Ctrl+C stops)."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseurl', default='')
parser.add_argument('--port', default=8765, type=int)
args = parser.parse_args()
prefix = args.baseurl.rstrip('/')

class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if prefix:
            if not self.path.startswith(prefix + '/'):
                self.send_error(404)
                return
            self.path = self.path[len(prefix):]
        super().do_GET()

site = Path(__file__).resolve().parents[1] / '_site'
if not (site / 'index.html').is_file():
    raise SystemExit('Build first: bundle exec ruby scripts/build.rb preview')
print(f'Local SIGCSE preview: http://127.0.0.1:{args.port}{prefix}/ (Ctrl+C to stop)', flush=True)
try:
    ThreadingHTTPServer(('127.0.0.1', args.port), partial(PreviewHandler, directory=str(site))).serve_forever()
except KeyboardInterrupt:
    pass
