"""Check that every official website in the data still resolves.

Upstreams move, get abandoned, or let their domain expire; an expired domain is
then re-registered by someone else. This catches all three.

  OK       2xx/3xx after redirects
  BLOCKED  401/402/403/429 -- the server answered but refuses bots; the site
           exists, so this is a warning only
  BROKEN   DNS failure, timeout, 404/410 or 5xx after one retry

Exit status is 1 if anything is BROKEN. Redirects to a different domain are
listed separately: they are the usual sign of a rename or a domain change.

Usage: python .build/checkurls.py [--workers N]
"""
import io, json, os, sys, time
import urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ultimate-it-toolbox-linkcheck/1.0"
BLOCKED = {401, 402, 403, 429}
WORKERS = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 16


def targets():
    out = {}
    for name, key in (("packages.json", "link"), ("nonwindows.json", "link")):
        for t in json.load(io.open(os.path.join(HERE, name), encoding="utf-8")):
            out.setdefault(t[key], t["name"])
    for slug, r in json.load(io.open(os.path.join(HERE, "ratings.json"), encoding="utf-8")).items():
        if r.get("evidence"):
            out.setdefault(r["evidence"], "rating evidence: " + slug)
    return out


def fetch(url):
    last = None
    for attempt in range(2):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if e.code in BLOCKED or e.code in (404, 410):
                return e.code, url
            last = e.code
        except Exception as e:                          # DNS, TLS, timeout
            last = type(e).__name__
        time.sleep(3)
    return last, url


def host(u):
    h = urlparse(u).hostname or ""
    return h[4:] if h.startswith("www.") else h


def main():
    t = targets()
    with ThreadPoolExecutor(WORKERS) as ex:
        results = dict(zip(t, ex.map(fetch, t)))
    broken, blocked, moved = [], [], []
    for url, (code, final) in sorted(results.items()):
        if isinstance(code, int) and code < 400:
            if host(final) != host(url):
                moved.append((url, final))
        elif code in BLOCKED:
            blocked.append((url, code))
        else:
            broken.append((url, code))
    print("checked %d URLs: %d broken, %d bot-blocked, %d moved to another domain"
          % (len(results), len(broken), len(blocked), len(moved)))
    for title, rows in (("BROKEN", broken), ("BLOCKED (warning)", blocked)):
        if rows:
            print("\n" + title)
            for url, code in rows:
                print("  %-9s %s  (%s)" % (code, url, t[url]))
    if moved:
        print("\nMOVED (review: rename, acquisition or expired domain?)")
        for url, final in moved:
            print("  %s -> %s  (%s)" % (url, final, t[url]))
    sys.exit(1 if broken else 0)


main()
