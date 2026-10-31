"""Generate the Ultimate IT Toolbox from verified tool data.

Every generated file in the repository comes from the data files in this
directory. Edit the data, never the generated Markdown.

  packages.json   -- tier "package": Windows tools. The winget id, the
                     Chocolatey id and the licence string were machine-verified
                     against the live package sources on the recorded date.
  nonwindows.json -- tier "upstream": Linux, BSD, appliance and self-hosted
                     tools. The official URL was HTTP-verified; the licence and
                     install route are as documented upstream and are NOT
                     machine-verified.
  ratings.json    -- the few ratings that have been applied, each with a reason
                     (see RATINGS.md). Absent means "Not yet rated".
  bundles.json    -- named sets of tools (certification tracks, starter kits),
                     rendered as winget import files under bundles/.

The tier distinction is printed on every card so a reader knows how much weight
the metadata carries. Nothing subjective (ratings, skill level, benchmarks) is
invented.

Usage:
  python .build/generate.py           write every generated file
  python .build/generate.py --check   write nothing; exit 1 if any generated
                                      file is out of date (used by CI)
"""
import csv, io, json, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHECK = "--check" in sys.argv[1:]

REPO_URL = "https://github.com/6t9xstar/ultimate-it-toolbox"
DEFAULT_VERIFIED = "2026-10-31"

CATS = [
 ("01-operating-systems", "Operating Systems & System Administration",
  "Windows, Linux and BSD system administration, distributions and admin consoles."),
 ("02-networking", "Networking",
  "Packet analysis, scanning, routing/switching labs, firewalls, monitoring, IPAM, DNS filtering and VoIP."),
 ("03-cybersecurity", "Cybersecurity",
  "Defensive security, forensics, incident response, supply-chain security, security distributions and authorised offensive testing."),
 ("04-development", "Software Development",
  "Editors, IDEs, language runtimes, build tools and SDKs."),
 ("05-cloud-computing", "Cloud Computing",
  "Cloud provider CLIs, SDKs, storage tooling and platform-as-a-service clients."),
 ("06-devops", "DevOps, Containers & IaC",
  "Containers, Kubernetes, GitOps, CI/CD, secrets, configuration management, infrastructure as code and observability."),
 ("07-databases", "Databases & Data Engineering",
  "Database servers, clients, administration tools, message brokers and BI."),
 ("08-ai-ml-data", "AI, Machine Learning & Data Science",
  "Local LLM runtimes and front-ends, notebooks, scientific Python/R distributions and data-science tooling."),
 ("09-virtualization", "Virtualization & Storage",
  "Hypervisors, WSL, VM provisioning and NAS platforms -- the foundation of any certification lab."),
 ("10-web-infrastructure", "Web Infrastructure",
  "Web and application servers, reverse proxies, DNS, TLS, mail servers, hosting panels and deployment platforms."),
 ("11-quality-assurance", "Quality Assurance & Testing",
  "API clients, debugging proxies, browser automation, load testing and code quality."),
 ("12-hardware-iot-robotics", "Hardware, IoT & Electronics",
  "Hardware diagnostics, benchmarking, electronics design and embedded development."),
 ("13-design-engineering", "Design & Engineering",
  "UI/UX, graphics, video, 3D, CAD and GIS."),
 ("14-browser-tools", "Browsers",
  "Web browsers, including privacy-focused and developer channels."),
 ("15-communication", "Communication",
  "Chat, email, conferencing and team messaging clients."),
 ("16-productivity", "Productivity & Office",
  "Office suites, PDF tools, readers, launchers and everyday productivity software."),
 ("17-file-management", "File Management",
  "File managers, archivers, search, synchronisation and transfer."),
 ("18-backup-recovery", "Backup & Recovery",
  "Backup programs, disk imaging, partitioning, data recovery and bootable media."),
 ("19-remote-access", "Remote Access",
  "SSH clients, remote desktop, VNC and remote-session management."),
 ("20-terminal-cli", "Terminal & CLI",
  "Terminals, shells, prompts, modern command-line utilities and Unix-like environments on Windows."),
 ("21-documentation", "Documentation & Knowledge",
  "Note-taking, knowledge bases, wikis, diagramming and technical documentation."),
 ("22-seo-marketing", "SEO & Marketing",
  "Site crawling and auditing, privacy-respecting web analytics and marketing tooling."),
 ("23-privacy-security", "Privacy & Personal Security",
  "VPNs, password managers, encryption, hardening, anonymity and identity providers."),
 ("24-project-management", "Project Management",
  "Planning, issue tracking and collaboration -- all self-hosted."),
 ("25-learning-certifications", "Learning & Certifications",
  "Tool sets grouped by certification -- see CERTIFICATION-MAP.md."),
 ("26-alternatives", "Open-Source & Self-Hosted Alternatives",
  "Replacements for proprietary and subscription software."),
 ("27-gaming", "Gaming",
  "Game launchers, streaming and gaming utilities. (Extends the base taxonomy.)"),
]
CAT_TITLE = {c: t for c, t, _ in CATS}

# Category indexes that are hand-written and must not be overwritten.
HANDWRITTEN = {"25-learning-certifications", "26-alternatives"}

# Root documents whose <!--n:key-->123<!--/n--> counters are kept current.
COUNTED_DOCS = ["README.md", "CONTRIBUTING.md", "RATINGS.md", "CERTIFICATION-MAP.md"]

WINGET_SOURCES = {
 "winget": {"Argument": "https://cdn.winget.microsoft.com/cache",
            "Identifier": "Microsoft.Winget.Source_8wekyb3d8bbwe",
            "Name": "winget", "Type": "Microsoft.PreIndexed.Package"},
}

OUT = {}          # path relative to ROOT -> content


def emit(rel, text):
    OUT[rel.replace("\\", "/")] = text


def read(name):
    return json.load(io.open(os.path.join(HERE, name), encoding="utf-8"))


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "tool"


def load():
    tools = []
    for t in read("packages.json"):
        tools.append(dict(t, _cat=t["folder"], _tier="package",
                          _source="Open source" if t.get("foss") else "Proprietary",
                          _platform="Windows (packaged)"))
    for t in read("nonwindows.json"):
        tools.append({"key": slug(t["name"]), "name": t["name"], "desc": t["desc"],
                      "link": t["link"], "license": t["licence"], "_cat": t["cat"],
                      "_tier": "upstream", "_source": t["source"],
                      "_platform": t["platform"], "_install": t["install"],
                      "_commands": t.get("commands") or [],
                      "_certs": t.get("certs", ""),
                      "verified": t.get("verified") or DEFAULT_VERIFIED})
    seen = {}
    for t in tools:
        s = slug(t["name"])
        while s in seen and seen[s] != t["key"]:
            s += "-" + slug(t["key"])
        seen[s] = t["key"]
        t["_slug"] = s
    return tools


def winget_cmd(t):
    if t.get("source") == "msstore":
        return "winget install --id %s --source msstore --exact" % t["winget"]
    return "winget install --id %s --exact" % t["winget"]


def rating_cell(r):
    if not r:
        return "Not yet rated — see [RATINGS.md](../RATINGS.md)"
    cell = "**%s** — %s" % (r["label"], r["reason"])
    if r.get("evidence"):
        cell += " ([evidence](%s))" % r["evidence"]
    return cell


def card(t, ratings, certs_for):
    L = ["# %s\n" % t["name"], "> %s\n" % (t.get("desc") or "").strip(), "## Overview\n",
         "| Property | Value |", "|---|---|",
         "| Category | %s |" % CAT_TITLE[t["_cat"]],
         "| Official website | <%s> |" % t["link"],
         "| Licence | `%s` |" % (t.get("license") or "Unknown"),
         "| Source model | %s |" % t["_source"],
         "| Platform | %s |" % t["_platform"]]
    certs = t.get("_certs") if t["_tier"] == "upstream" else certs_for.get(t["_slug"], "")
    if certs:
        L.append("| Certification relevance | %s |" % certs)
    L += ["| Rating | %s |" % rating_cell(ratings.get(t["_slug"])),
          "| Last verified | %s |" % (t.get("verified") or DEFAULT_VERIFIED), ""]

    if t["_tier"] == "package":
        L += ["## Install on Windows\n", "```powershell", winget_cmd(t)]
        if t.get("choco") and t["choco"] != "na":
            L.append("choco install %s" % t["choco"])
        L += ["```\n"]
        if not t.get("choco") or t["choco"] == "na":
            L.append("_No Chocolatey package is published for this tool; use winget._\n")
        L += ["## Verification\n", "**Tier: package-verified.**\n"]
        if t.get("source") == "msstore":
            L += ["- Microsoft Store product id confirmed with `winget show --source msstore` on %s." % t["verified"],
                  "- Store listings publish terms of service rather than a licence id, so the licence is recorded as the listing describes it."]
        else:
            L += ["- Package id confirmed against the live `winget` source on %s." % t["verified"],
                  "- " + (t.get("license_note") or "Licence string copied from the package manifest, not inferred.")]
        if t.get("winutil", True):
            L.append("- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `%s`." % t["key"])
        L.append("")
    else:
        L += ["## How to get it\n", "%s\n" % t["_install"]]
        if t["_commands"]:
            L += ["```bash"] + t["_commands"] + ["```\n"]
        L += ["See the official site for current instructions — deployment steps change more often than this directory does.\n",
              "## Verification\n",
              "**Tier: upstream-documented.**\n",
              "- Official URL confirmed to resolve on %s." % t["verified"],
              "- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.",
              "- Not installable through WinUtil Pro: this is not a Windows package.\n"]

    L += ["---\n", "[← %s](../%s/) · [All tools](../tools/) · [All categories](../README.md)"
          % (CAT_TITLE[t["_cat"]], t["_cat"])]
    return "\n".join(L) + "\n"


def tools_index(allt, pkg, ups):
    L = ["# All Tools\n",
         "Every tool has exactly one canonical card here, linked from whichever "
         "categories apply. **%d tools** — %d package-verified, %d upstream-documented "
         "(see [the README](../README.md#how-entries-are-verified)).\n" % (len(allt), pkg, ups),
         "Machine-readable copies of this table: [`catalog.json`](../data/catalog.json) · "
         "[`catalog.csv`](../data/catalog.csv).\n",
         "| Tool | Category | Platform | Licence | Tier |", "|---|---|---|---|---|"]
    for t in allt:
        L.append("| **[%s](%s.md)** | [%s](../%s/) | %s | `%s` | %s |"
                 % (t["name"], t["_slug"], CAT_TITLE[t["_cat"]], t["_cat"], t["_platform"],
                    t.get("license") or "?",
                    "package" if t["_tier"] == "package" else "upstream"))
    L += ["", "---", "", "[All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md) · [Install bundles](../bundles/)"]
    return "\n".join(L) + "\n"


def category_index(folder, title, blurb, items, bundles_by_cat):
    L = ["# %s\n" % title, "%s\n" % blurb]
    if items:
        np = sum(1 for t in items if t["_tier"] == "package")
        nu = len(items) - np
        bits = []
        if np: bits.append("%d package-verified" % np)
        if nu: bits.append("%d upstream-documented" % nu)
        L.append("**%d tool%s** — %s.\n" % (len(items), "" if len(items) == 1 else "s", ", ".join(bits)))
        if folder in bundles_by_cat:
            b = bundles_by_cat[folder]
            L.append("Install the Windows tools below in one go with the [`%s`](../bundles/%s.winget.json) bundle — see [bundles](../bundles/).\n"
                     % (b["id"], b["id"]))
        L.append("| Tool | What it does | Platform | Licence |")
        L.append("|---|---|---|---|")
        for t in items:
            d = (t.get("desc") or "").split(". ")[0].rstrip(".")
            if len(d) > 110: d = d[:107].rstrip() + "..."
            L.append("| **[%s](../tools/%s.md)** | %s | %s | `%s` |"
                     % (t["name"], t["_slug"], d, t["_platform"], t.get("license") or "?"))
        L.append("")
    else:
        L += ["> **This category has no entries yet.**\n",
              "Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).\n"]
    L += ["---\n", "[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)"]
    return "\n".join(L) + "\n"


def resolve_bundles(bundles, tools, bycat):
    """Expand each bundle to a list of tools; fail loudly on a bad reference."""
    byslug = {t["_slug"]: t for t in tools}
    out = []
    for b in bundles:
        members = []
        if b.get("category"):
            members += [t for t in sorted(bycat[b["category"]], key=lambda x: x["name"].lower())
                        if t["_tier"] == "package" and t.get("source", "winget") == "winget"]
        for s in b.get("tools", []):
            if s not in byslug:
                sys.exit("bundles.json: %s references unknown tool %r" % (b["id"], s))
            t = byslug[s]
            if t["_tier"] != "package" or t.get("source", "winget") != "winget":
                sys.exit("bundles.json: %s lists %r, which has no winget-source package" % (b["id"], s))
            if t not in members:
                members.append(t)
        upstream = []
        for s in b.get("upstream", []):
            if s not in byslug or byslug[s]["_tier"] != "upstream":
                sys.exit("bundles.json: %s upstream entry %r is not an upstream card" % (b["id"], s))
            upstream.append(byslug[s])
        out.append(dict(b, _members=members, _upstream=upstream))
    return out


def winget_import(members):
    doc = {"$schema": "https://aka.ms/winget-packages.schema.2.0.json",
           "CreationDate": DEFAULT_VERIFIED + "T00:00:00.000-00:00",
           "Sources": [{"Packages": [{"PackageIdentifier": t["winget"]} for t in members],
                        "SourceDetails": WINGET_SOURCES["winget"]}],
           "WinGetVersion": "1.9.0"}
    return json.dumps(doc, indent=2) + "\n"


def bundles_index(bundles):
    raw = REPO_URL.replace("github.com", "raw.githubusercontent.com") + "/main/bundles/"
    L = ["# Install Bundles\n",
         "Each bundle is a standard [`winget import`](https://learn.microsoft.com/windows/package-manager/winget/import) "
         "file listing package-verified tools from this directory. One command installs the whole set; "
         "winget skips anything already installed.\n",
         "```powershell",
         "# From a clone of this repository",
         "winget import -i bundles\\ccna.winget.json --accept-package-agreements --accept-source-agreements",
         "",
         "# Or straight from GitHub, without cloning",
         "irm %sccna.winget.json -OutFile ccna.winget.json" % raw,
         "winget import -i ccna.winget.json --accept-package-agreements --accept-source-agreements",
         "```\n",
         "> [!TIP]",
         "> Read the bundle before you run it. Every id in it links to a card below, so you can see the licence and "
         "publisher of each tool first. Remove lines you do not want — the file is plain JSON.\n",
         "Only `winget`-source packages are bundled. Microsoft Store apps and upstream-documented tools (Linux, "
         "appliances, self-hosted) cannot be installed this way; where a track depends on them, they are listed "
         "under *Also needed* with a link to the card that explains how to get them.\n"]
    for kind, heading in (("certification", "Certification tracks"), ("kit", "Role kits"),
                          ("category", "Whole categories")):
        group = [b for b in bundles if b["kind"] == kind]
        if not group:
            continue
        L += ["## %s\n" % heading, "| Bundle | For | Packages | File |", "|---|---|---|---|"]
        for b in group:
            target = "../%s/" % b["category"] if kind == "category" else "#" + slug(b["title"])
            L.append("| [%s](%s) | %s | %d | [`%s.winget.json`](%s.winget.json) |"
                     % (b["title"], target, b["for"], len(b["_members"]), b["id"], b["id"]))
        L.append("")
    L.append("## Contents\n")
    for b in bundles:
        if b["kind"] == "category":
            continue
        L.append("### %s\n" % b["title"])
        L.append("%s\n" % b["for"])
        L.append(", ".join("[%s](../tools/%s.md)" % (t["name"], t["_slug"]) for t in b["_members"]) + "\n")
        if b["_upstream"]:
            L.append("**Also needed** (not a Windows package): "
                     + ", ".join("[%s](../tools/%s.md)" % (t["name"], t["_slug"]) for t in b["_upstream"]) + "\n")
    L += ["Category bundles contain every winget-source tool in that category; see the category page for the list.\n",
          "---\n", "[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)"]
    return "\n".join(L) + "\n"


def catalog(allt, ratings, certs_for):
    rows = []
    for t in allt:
        r = ratings.get(t["_slug"])
        rows.append({
            "slug": t["_slug"], "name": t["name"], "description": (t.get("desc") or "").strip(),
            "category": t["_cat"], "category_title": CAT_TITLE[t["_cat"]],
            "tier": t["_tier"], "platform": t["_platform"],
            "licence": t.get("license") or None, "source_model": t["_source"],
            "website": t["link"],
            "winget": t.get("winget") if t["_tier"] == "package" else None,
            "winget_source": (t.get("source") or "winget") if t["_tier"] == "package" else None,
            "chocolatey": (t["choco"] if t.get("choco") not in (None, "na") else None) if t["_tier"] == "package" else None,
            "install": t.get("_install") if t["_tier"] == "upstream" else winget_cmd(t),
            "certifications": [c.strip() for c in (t.get("_certs") if t["_tier"] == "upstream"
                                                   else certs_for.get(t["_slug"], "")).split(",") if c.strip()],
            "rating": r["label"] if r else None,
            "verified": t.get("verified") or DEFAULT_VERIFIED,
            "card": "tools/%s.md" % t["_slug"],
        })
    j = json.dumps({"generated_from": REPO_URL, "count": len(rows), "tools": rows},
                   indent=1, ensure_ascii=False) + "\n"
    buf = io.StringIO()
    cols = list(rows[0].keys())
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(dict(r, certifications="; ".join(r["certifications"])))
    return j, buf.getvalue()


def update_counters(counts):
    pat = re.compile(r"<!--n:(\w+)-->\d+<!--/n-->")
    for name in COUNTED_DOCS:
        p = os.path.join(ROOT, name)
        if not os.path.isfile(p):
            continue
        text = io.open(p, encoding="utf-8").read()
        def sub(m):
            if m.group(1) not in counts:
                sys.exit("%s: unknown counter %r" % (name, m.group(1)))
            return "<!--n:%s-->%d<!--/n-->" % (m.group(1), counts[m.group(1)])
        text = pat.sub(sub, text)
        text = re.sub(r"badge/tools-\d+-", "badge/tools-%d-" % counts["total"], text)
        text = re.sub(r"badge/\d+-package%20verified", "badge/%d-package%%20verified" % counts["package"], text)
        text = re.sub(r"\[!\[Tools: \d+\]", "[![Tools: %d]" % counts["total"], text)
        emit(name, text)


def category_table(bycat):
    L = ["| # | Category | Tools |", "|---|---|---|"]
    for folder, title, _ in CATS:
        n = folder[:2]
        if folder == "25-learning-certifications":
            cell = "see map"
        elif folder == "26-alternatives":
            cell = "mapping"
        else:
            cell = str(len(bycat.get(folder, [])))
        L.append("| %s | [%s](%s/) | %s |" % (n, title, folder, cell))
    return "\n".join(L)


def update_readme_table(bycat):
    text = OUT.get("README.md")
    if text is None:
        return
    start, end = "<!-- generated:categories:start -->", "<!-- generated:categories:end -->"
    if start in text and end in text:
        a, rest = text.split(start, 1)
        _, b = rest.split(end, 1)
        OUT["README.md"] = a + start + "\n" + category_table(bycat) + "\n" + end + b


def main():
    tools = load()
    ratings = read("ratings.json")
    for s in ratings:
        if s not in {t["_slug"] for t in tools}:
            sys.exit("ratings.json: unknown tool %r" % s)
    bycat = defaultdict(list)
    for t in tools:
        bycat[t["_cat"]].append(t)

    bundles = read("bundles.json")
    # Every generated category with at least three winget packages gets a bundle.
    for folder, title, _ in CATS:
        n = sum(1 for t in bycat.get(folder, [])
                if t["_tier"] == "package" and t.get("source", "winget") == "winget")
        if folder not in HANDWRITTEN and n >= 3:
            bundles.append({"id": "category-" + folder[3:], "kind": "category", "category": folder,
                            "title": title, "for": "Every winget package in [%s](../%s/)." % (title, folder)})
    bundles = resolve_bundles(bundles, tools, bycat)
    certs_for = defaultdict(list)
    for b in bundles:
        if b["kind"] == "certification":
            for t in b["_members"]:
                certs_for[t["_slug"]].append(b["short"])
    certs_for = {k: ", ".join(v) for k, v in certs_for.items()}
    bundles_by_cat = {b["category"]: b for b in bundles if b["kind"] == "category"}

    for t in tools:
        emit("tools/%s.md" % t["_slug"], card(t, ratings, certs_for))

    pkg = sum(1 for t in tools if t["_tier"] == "package")
    ups = len(tools) - pkg
    allt = sorted(tools, key=lambda x: x["name"].lower())
    emit("tools/README.md", tools_index(allt, pkg, ups))

    for folder, title, blurb in CATS:
        if folder in HANDWRITTEN:
            continue
        items = sorted(bycat.get(folder, []), key=lambda x: x["name"].lower())
        emit("%s/README.md" % folder, category_index(folder, title, blurb, items, bundles_by_cat))

    for b in bundles:
        emit("bundles/%s.winget.json" % b["id"], winget_import(b["_members"]))
    emit("bundles/README.md", bundles_index(bundles))

    j, c = catalog(allt, ratings, certs_for)
    emit("data/catalog.json", j)
    emit("data/catalog.csv", c)

    counts = {"total": len(tools), "package": pkg, "upstream": ups,
              "categories": len(CATS), "bundles": len(bundles),
              "rated": len(ratings)}
    update_counters(counts)
    update_readme_table(bycat)

    stale = []
    for rel, text in sorted(OUT.items()):
        p = os.path.join(ROOT, rel)
        old = io.open(p, encoding="utf-8", newline="").read() if os.path.isfile(p) else None
        if old == text:
            continue
        stale.append(rel)
        if not CHECK:
            os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
            io.open(p, "w", encoding="utf-8", newline="\n").write(text)

    # A card whose tool was removed from the data must not linger.
    expected = {rel for rel in OUT if rel.startswith("tools/")}
    for fn in os.listdir(os.path.join(ROOT, "tools")):
        rel = "tools/" + fn
        if fn.endswith(".md") and rel not in expected:
            stale.append(rel + " (orphan)")
            if not CHECK:
                os.remove(os.path.join(ROOT, rel))

    if CHECK:
        if stale:
            print("%d generated file(s) are out of date. Run: python .build/generate.py" % len(stale))
            for s in stale[:50]:
                print("  " + s)
            sys.exit(1)
        print("generated files are up to date (%d checked)" % len(OUT))
        return

    print("tools: %d  (package %d / upstream %d), bundles: %d, files changed: %d"
          % (len(tools), pkg, ups, len(bundles), len(stale)))
    for f, _, _ in CATS:
        print("  %-28s %d" % (f, len(bycat.get(f, []))))


main()
