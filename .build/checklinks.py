"""Validate every relative Markdown link and in-page anchor in the repo."""
import io, os, re, sys

ROOT = sys.argv[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEAD = re.compile(r"^#{1,6}\s+(.*)$", re.M)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")

def strip_fences(text):
    """Blank out fenced code blocks: links inside them are examples, not links."""
    out, fence = [], None
    for line in text.splitlines():
        m = FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            out.append("")
            continue
        if fence is not None:
            if m and m.group(1)[0] * 3 == fence:
                fence = None
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)

def anchors(text):
    out = set()
    for h in HEAD.findall(text):
        h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)      # strip links
        h = re.sub(r"[`*_]", "", h)
        s = re.sub(r"[^a-z0-9 -]", "", h.lower()).strip()
        out.add(s.replace(" ", "-"))
    return out

md = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in (".git", ".build")]
    md += [os.path.join(dp, f) for f in fn if f.endswith(".md")]

bad = []
for path in sorted(md):
    text = io.open(path, encoding="utf-8").read()
    base = os.path.dirname(path)
    for raw in LINK.findall(strip_fences(text)):
        t = raw.strip()
        if t.startswith(("http://", "https://", "mailto:", "<")):
            continue
        frag = ""
        if "#" in t:
            t, frag = t.split("#", 1)
        if t == "":                                      # same-file anchor
            if frag and frag not in anchors(text):
                bad.append((path, raw, "anchor not found"))
            continue
        target = os.path.normpath(os.path.join(base, t))
        if os.path.isdir(target):
            target_file = os.path.join(target, "README.md")
            if not os.path.isfile(target_file):
                bad.append((path, raw, "dir has no README.md"))
                continue
            target = target_file
        elif not os.path.exists(target):
            bad.append((path, raw, "missing file"))
            continue
        if frag:
            if frag not in anchors(io.open(target, encoding="utf-8").read()):
                bad.append((path, raw, "anchor not found in target"))

print("markdown files:", len(md))
print("broken links:", len(bad))
for p, l, why in bad:
    print("  %s -> %s  (%s)" % (os.path.relpath(p, ROOT), l, why))
sys.exit(1 if bad else 0)
