"""Check the data files against the rules in CONTRIBUTING.md.

Catches the mistakes a reviewer would otherwise have to spot by eye: a missing
field, a licence written as "Free", a duplicate package id, a Store id written
with the invalid `msstore:` prefix, a bundle pointing at a tool that does not
exist. Run before generate.py; CI runs both.

Usage: python .build/validate.py
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0]]          # generate.py reads sys.argv; give it none
src = io.open(os.path.join(HERE, "generate.py"), encoding="utf-8").read()
gen = {"__file__": os.path.join(HERE, "generate.py")}
exec(compile(src.replace("\nmain()\n", "\n"), "generate.py", "exec"), gen)

FOLDERS = {f for f, _, _ in gen["CATS"]} - gen["HANDWRITTEN"]
# Placeholders that are not licences. A manifest that literally says
# "Freeware" is recorded as such; these words never come from a manifest.
NOT_A_LICENCE = {"free", "open source", "open-source", "oss", "foss", "unknown", "n/a", ""}
SOURCE_MODELS = {"Open source", "Proprietary", "Mixed", "Source available"}
LABELS = {"Best Overall", "Best Free", "Best Open Source", "Good Alternative",
          "Okay / Basic", "Advanced", "Enterprise", "Deprecated"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WINGET_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9+_-]*(\.[A-Za-z0-9+_-]+)+$")
STORE_ID = re.compile(r"^[0-9A-Z]{12}$")
CHOCO_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$", re.I)

errors = []


def err(where, msg):
    errors.append("%s: %s" % (where, msg))


def check_common(where, t, licence_key):
    for k in ("name", "desc", "link", licence_key):
        if not isinstance(t.get(k), str) or not t[k].strip():
            err(where, "missing or empty %r" % k)
    if not str(t.get("link", "")).startswith("https://"):
        err(where, "official website must be an https:// URL")
    lic = str(t.get(licence_key) or "").strip().lower()
    if lic in NOT_A_LICENCE:
        err(where, "licence %r is not a licence string" % t.get(licence_key))
    d = str(t.get("desc", "")).strip()
    if d and not d.endswith("."):
        err(where, "description should be one full sentence ending in a full stop")
    if len(d) > 320:
        err(where, "description is %d characters; keep it to one sentence" % len(d))


def main():
    pk = json.load(io.open(os.path.join(HERE, "packages.json"), encoding="utf-8"))
    nw = json.load(io.open(os.path.join(HERE, "nonwindows.json"), encoding="utf-8"))
    ratings = json.load(io.open(os.path.join(HERE, "ratings.json"), encoding="utf-8"))
    bundles = json.load(io.open(os.path.join(HERE, "bundles.json"), encoding="utf-8"))

    names, ids, keys = {}, {}, {}
    for i, t in enumerate(pk):
        where = "packages.json[%d] %s" % (i, t.get("name", "?"))
        check_common(where, t, "license")
        if t.get("folder") not in FOLDERS:
            err(where, "folder %r is not a generated category" % t.get("folder"))
        wid, srcname = t.get("winget", ""), t.get("source", "winget")
        if wid.lower().startswith("msstore:"):
            err(where, "write Store ids without the msstore: prefix and set \"source\": \"msstore\"")
        elif srcname == "winget" and not WINGET_ID.match(wid):
            err(where, "winget id %r does not look like Publisher.Package" % wid)
        elif srcname == "msstore" and not STORE_ID.match(wid):
            err(where, "Store product id %r should be 12 upper-case characters" % wid)
        elif srcname not in ("winget", "msstore"):
            err(where, "source must be winget or msstore")
        ch = t.get("choco")
        if ch != "na" and not (isinstance(ch, str) and CHOCO_ID.match(ch)):
            err(where, "choco must be a package id or \"na\"")
        if not DATE.match(str(t.get("verified") or "")):
            err(where, "verified must be a YYYY-MM-DD date")
        if not isinstance(t.get("foss"), bool):
            err(where, "foss must be true or false")
        for seen, value, what in ((ids, wid.lower(), "winget id"), (keys, t.get("key"), "key")):
            if value in seen:
                err(where, "duplicate %s, also used by %s" % (what, seen[value]))
            seen[value] = t.get("name")
        n = str(t.get("name", "")).lower()
        if n in names:
            err(where, "duplicate tool name, also in %s" % names[n])
        names[n] = "packages.json"

    for i, t in enumerate(nw):
        where = "nonwindows.json[%d] %s" % (i, t.get("name", "?"))
        check_common(where, t, "licence")
        if t.get("cat") not in FOLDERS:
            err(where, "cat %r is not a generated category" % t.get("cat"))
        for k in ("platform", "install"):
            if not str(t.get(k, "")).strip():
                err(where, "missing %r" % k)
        if t.get("source") not in SOURCE_MODELS:
            err(where, "source must be one of %s" % ", ".join(sorted(SOURCE_MODELS)))
        cmds = t.get("commands", [])
        if not isinstance(cmds, list) or not all(isinstance(c, str) for c in cmds):
            err(where, "commands must be a list of strings")
        if t.get("verified") and not DATE.match(t["verified"]):
            err(where, "verified must be a YYYY-MM-DD date")
        n = str(t.get("name", "")).lower()
        if n in names:
            err(where, "duplicate tool name, also in %s" % names[n])
        names[n] = "nonwindows.json"

    slugs = {gen["slug"](t["name"]) for t in pk + nw if t.get("name")}
    for s, r in ratings.items():
        where = "ratings.json %s" % s
        if s not in slugs:
            err(where, "no tool has this slug")
        if r.get("label") not in LABELS:
            err(where, "label must be one of the RATINGS.md vocabulary")
        if not str(r.get("reason", "")).strip():
            err(where, "a rating needs a stated reason")
        if r.get("label") == "Deprecated" and not str(r.get("evidence", "")).startswith("https://"):
            err(where, "Deprecated needs an https:// evidence link")

    seen = set()
    for b in bundles:
        where = "bundles.json %s" % b.get("id", "?")
        if b.get("id") in seen:
            err(where, "duplicate bundle id")
        seen.add(b.get("id"))
        if not re.match(r"^[a-z0-9-]+$", str(b.get("id", ""))):
            err(where, "id must be lower-case letters, digits and hyphens")
        if b.get("kind") not in ("certification", "kit"):
            err(where, "kind must be certification or kit (category bundles are automatic)")
        if b.get("kind") == "certification" and not b.get("short"):
            err(where, "certification bundles need a short label for cards")
        for k in ("title", "for"):
            if not str(b.get(k, "")).strip():
                err(where, "missing %r" % k)
        for s in b.get("tools", []) + b.get("upstream", []):
            if s not in slugs:
                err(where, "unknown tool slug %r" % s)

    if errors:
        print("%d problem(s) found:" % len(errors))
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("data OK: %d packages, %d upstream, %d ratings, %d bundles"
          % (len(pk), len(nw), len(ratings), len(bundles)))


main()
