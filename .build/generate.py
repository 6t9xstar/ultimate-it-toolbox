"""Generate the Ultimate IT Toolbox from verified tool data.

Two input sources, two verification tiers:

  tier "package"  -- Windows tools from the WinUtil Pro catalogue. The winget
                     id, the Chocolatey id and the licence string were all
                     machine-verified against the live package sources.
  tier "upstream" -- Linux, BSD, appliance and self-hosted tools. The official
                     URL was HTTP-verified; the licence and install route are
                     as documented upstream and are NOT machine-verified.

The distinction is printed on every card so a reader knows how much weight the
metadata carries. Nothing subjective (ratings, skill level, benchmarks) is
invented -- see RATINGS.md.

Usage: generate.py <packages.json> <nonwindows.json> <repo-root>
"""
import io, json, os, re, sys
from collections import defaultdict

PKG_SRC, NW_SRC, ROOT = sys.argv[1], sys.argv[2], sys.argv[3]

CATS = [
 ("01-operating-systems", "Operating Systems & System Administration",
  "Windows, Linux and BSD system administration, distributions and admin consoles."),
 ("02-networking", "Networking",
  "Packet analysis, scanning, routing/switching labs, firewalls, monitoring, IPAM and VoIP."),
 ("03-cybersecurity", "Cybersecurity",
  "Defensive security, forensics, incident response, security distributions and authorised offensive testing."),
 ("04-development", "Software Development",
  "Editors, IDEs, language runtimes, build tools and SDKs."),
 ("05-cloud-computing", "Cloud Computing",
  "Cloud provider CLIs, SDKs and cloud storage tooling."),
 ("06-devops", "DevOps, Containers & IaC",
  "Containers, Kubernetes, configuration management, infrastructure as code and observability."),
 ("07-databases", "Databases & Data Engineering",
  "Database servers, clients and administration tools."),
 ("08-ai-ml-data", "AI, Machine Learning & Data Science",
  "Local LLM runtimes, scientific Python/R distributions and data-science tooling."),
 ("09-virtualization", "Virtualization & Storage",
  "Hypervisors, VM provisioning and NAS platforms -- the foundation of any certification lab."),
 ("10-web-infrastructure", "Web Infrastructure",
  "Web servers, reverse proxies, DNS, TLS, mail servers, hosting panels and deployment platforms."),
 ("11-quality-assurance", "Quality Assurance & Testing",
  "API clients, load testing and performance testing."),
 ("12-hardware-iot-robotics", "Hardware, IoT & Electronics",
  "Hardware diagnostics, benchmarking, electronics design and embedded development."),
 ("13-design-engineering", "Design & Engineering",
  "UI/UX, graphics, video, 3D, CAD and GIS."),
 ("14-browser-tools", "Browsers",
  "Web browsers, including privacy-focused and developer channels."),
 ("15-communication", "Communication",
  "Chat, email, conferencing and team messaging clients."),
 ("16-productivity", "Productivity & Office",
  "Office suites, PDF tools, readers and everyday productivity software."),
 ("17-file-management", "File Management",
  "File managers, archivers, search, synchronisation and transfer."),
 ("18-backup-recovery", "Backup & Recovery",
  "Backup programs, disk imaging, partitioning and bootable media."),
 ("19-remote-access", "Remote Access",
  "SSH clients, remote desktop and remote-session management."),
 ("20-terminal-cli", "Terminal & CLI",
  "Terminals, shells, prompts and Unix-like environments on Windows."),
 ("21-documentation", "Documentation & Knowledge",
  "Note-taking, knowledge bases and technical documentation."),
 ("22-seo-marketing", "SEO & Marketing",
  "Site crawling, auditing and digital-marketing tooling."),
 ("23-privacy-security", "Privacy & Personal Security",
  "VPNs, password managers, encryption, anonymity and identity providers."),
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

OVERRIDE = {
 "tftpd64":"02-networking","iperf3":"02-networking","winmtr":"02-networking",
 "nmap":"02-networking","wireshark":"02-networking","angryipscanner":"02-networking",
 "advancedip":"02-networking","simplewall":"02-networking","zabbixagent":"02-networking",
 "zerotier":"02-networking","cloudflared":"10-web-infrastructure",
 "putty":"19-remote-access","winscp":"19-remote-access","termius":"19-remote-access",
 "mobaxterm":"19-remote-access","mremoteng":"19-remote-access","anydesk":"19-remote-access",
 "cyberduck":"17-file-management","rclone":"17-file-management",
 "openvpn":"23-privacy-security","OpenVPN":"23-privacy-security","wireguard":"23-privacy-security",
 "tailscale":"23-privacy-security","mullvadvpn":"23-privacy-security","protonvpn":"23-privacy-security",
 "veracrypt":"23-privacy-security","gpg4win":"23-privacy-security","keepassxc":"23-privacy-security",
 "bitwarden":"23-privacy-security","tor":"14-browser-tools","sandboxieplus":"03-cybersecurity",
 "OVirtualBox":"09-virtualization","vagrant":"09-virtualization",
 "dockerdesktop":"06-devops","podmandesktop":"06-devops","podman":"06-devops",
 "openshiftcli":"06-devops","rancherdesktop":"06-devops","lens":"06-devops",
 "kubectl":"06-devops","helm":"06-devops","k9s":"06-devops","minikube":"06-devops",
 "kind":"06-devops","terraform":"06-devops","opentofu":"06-devops","pulumi":"06-devops",
 "terragrunt":"06-devops","infracost":"06-devops","act":"06-devops","grafana":"06-devops",
 "netdata":"06-devops","trivy":"03-cybersecurity","gitleaks":"03-cybersecurity",
 "awscli":"05-cloud-computing","azurecli":"05-cloud-computing","gcloudsdk":"05-cloud-computing",
 "awssam":"05-cloud-computing","minioclient":"05-cloud-computing","planetscale":"05-cloud-computing",
 "postgresql":"07-databases","mysql":"07-databases","mariadb":"07-databases",
 "mongodb":"07-databases","redis":"07-databases","sqlite":"07-databases","duckdb":"07-databases",
 "ssms":"07-databases","azuredatastudio":"07-databases","heidisql":"07-databases",
 "dbgate":"07-databases","beekeeperstudio":"07-databases","dbeaver":"07-databases",
 "pgadmin":"07-databases","mongodbcompass":"07-databases","redisinsight":"07-databases",
 "mysqlworkbench":"07-databases","datagrip":"07-databases",
 "ollama":"08-ai-ml-data","anaconda":"08-ai-ml-data","miniconda":"08-ai-ml-data",
 "julia":"08-ai-ml-data","rproject":"08-ai-ml-data",
 "jmeter":"11-quality-assurance","k6":"11-quality-assurance","postman":"11-quality-assurance",
 "insomnia":"11-quality-assurance","soapui":"11-quality-assurance","bruno":"11-quality-assurance",
 "arduinoide":"12-hardware-iot-robotics","kicad":"12-hardware-iot-robotics",
 "hwinfo":"12-hardware-iot-robotics","hwmonitor":"12-hardware-iot-robotics",
 "cpuz":"12-hardware-iot-robotics","gpuz":"12-hardware-iot-robotics",
 "crystaldiskinfo":"12-hardware-iot-robotics","crystaldiskmark":"12-hardware-iot-robotics",
 "cinebenchr23":"12-hardware-iot-robotics","msiafterburner":"12-hardware-iot-robotics",
 "ddu":"12-hardware-iot-robotics",
 "gimp":"13-design-engineering","inkscape":"13-design-engineering","krita":"13-design-engineering",
 "blender":"13-design-engineering","figma":"13-design-engineering","lunacy":"13-design-engineering",
 "freecad":"13-design-engineering","librecad":"13-design-engineering","qgis":"13-design-engineering",
 "fontforge":"13-design-engineering","kdenlive":"13-design-engineering","shotcut":"13-design-engineering",
 "Paintdotnet":"13-design-engineering",
 "xampp":"10-web-infrastructure","caddy":"10-web-infrastructure",
 "restic":"18-backup-recovery","rufus":"18-backup-recovery","ventoy":"18-backup-recovery",
 "terminal":"20-terminal-cli","powershell":"20-terminal-cli","posh":"20-terminal-cli",
 "starship":"20-terminal-cli","msys2":"20-terminal-cli","cygwin":"20-terminal-cli",
 "gsudo":"20-terminal-cli",
 "obsidian":"21-documentation","joplin":"21-documentation","logseq":"21-documentation",
 "screamingfrog":"22-seo-marketing",
 "sysinternalssuite":"01-operating-systems","systeminformer":"01-operating-systems",
 "autoruns":"01-operating-systems","powertoys":"01-operating-systems",
 "nvda":"01-operating-systems",
}

RULES = [
 ("03-cybersecurity", {"Security","Red Team","Blue Team"}),
 ("14-browser-tools", {"Browsers"}),
 ("15-communication", {"Communications"}),
 ("16-productivity",  {"Document"}),
 ("27-gaming",        {"Games"}),
 ("13-design-engineering", {"Multimedia Tools"}),
 ("04-development",   {"Development"}),
 ("01-operating-systems", {"Microsoft Tools"}),
 ("06-devops",        {"Selfhosted Tools"}),
]
FILE_WORDS = re.compile(r"archiv|zip|file manager|dual-pane|clipboard|search|sync|transfer|download|ftp|commander", re.I)
BACKUP_WORDS = re.compile(r"backup|image|bootable|recovery|clone", re.I)

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "tool"

def category_for(t):
    if t["key"] in OVERRIDE:
        return OVERRIDE[t["key"]]
    cat, desc = t["cat"], (t.get("desc") or "")
    for folder, cats in RULES:
        if cat in cats:
            return folder
    if cat in ("Utilities", "Pro Tools"):
        if BACKUP_WORDS.search(desc):
            return "18-backup-recovery"
        if FILE_WORDS.search(desc):
            return "17-file-management"
        return "01-operating-systems"
    return None

def load():
    tools = []
    for t in json.load(io.open(PKG_SRC, encoding="utf-8")):
        c = category_for(t)
        if not c:
            continue
        tools.append(dict(t, _cat=c, _tier="package",
                          _source="Open source" if t.get("foss") else "Proprietary",
                          _platform="Windows (packaged)"))
    for t in json.load(io.open(NW_SRC, encoding="utf-8")):
        tools.append({"key": slug(t["name"]), "name": t["name"], "desc": t["desc"],
                      "link": t["link"], "license": t["licence"], "_cat": t["cat"],
                      "_tier": "upstream", "_source": t["source"],
                      "_platform": t["platform"], "_install": t["install"],
                      "_certs": t.get("certs", "")})
    seen = {}
    for t in tools:
        s = slug(t["name"])
        while s in seen and seen[s] != t["key"]:
            s += "-" + slug(t["key"])
        seen[s] = t["key"]
        t["_slug"] = s
    return tools

def card(t):
    L = ["# %s\n" % t["name"], "> %s\n" % (t.get("desc") or "").strip(), "## Overview\n",
         "| Property | Value |", "|---|---|",
         "| Category | %s |" % CAT_TITLE[t["_cat"]],
         "| Official website | <%s> |" % t["link"],
         "| Licence | `%s` |" % (t.get("license") or "Unknown"),
         "| Source model | %s |" % t["_source"],
         "| Platform | %s |" % t["_platform"]]
    if t["_tier"] == "upstream" and t.get("_certs"):
        L.append("| Certification relevance | %s |" % t["_certs"])
    L += ["| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |",
          "| Last verified | %s |" % (t.get("verified") or "2026-10-31"), ""]

    if t["_tier"] == "package":
        L += ["## Install on Windows\n", "```powershell",
              "winget install --id %s --exact" % t["winget"]]
        if t.get("choco") and t["choco"] != "na":
            L.append("choco install %s" % t["choco"])
        L += ["```\n"]
        if not t.get("choco") or t["choco"] == "na":
            L.append("_No Chocolatey package is published for this tool; use winget._\n")
        L += ["## Verification\n",
              "**Tier: package-verified.**\n",
              "- Package id confirmed against the live `winget` source on %s." % (t.get("verified") or "n/a"),
              "- Licence string copied from the package manifest, not inferred.",
              "- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `%s`.\n" % t["key"]]
    else:
        L += ["## How to get it\n", "%s\n" % t["_install"],
              "See the official site for current instructions — deployment steps change more often than this directory does.\n",
              "## Verification\n",
              "**Tier: upstream-documented.**\n",
              "- Official URL confirmed to resolve on 2026-10-31.",
              "- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.",
              "- Not installable through WinUtil Pro: this is not a Windows package.\n"]

    L += ["---\n", "[← %s](../%s/) · [All tools](../tools/) · [All categories](../README.md)"
          % (CAT_TITLE[t["_cat"]], t["_cat"])]
    return "\n".join(L) + "\n"

def main():
    tools = load()
    bycat = defaultdict(list)
    for t in tools:
        bycat[t["_cat"]].append(t)

    os.makedirs(os.path.join(ROOT, "tools"), exist_ok=True)
    for t in tools:
        io.open(os.path.join(ROOT, "tools", t["_slug"] + ".md"), "w",
                encoding="utf-8", newline="\n").write(card(t))

    pkg = sum(1 for t in tools if t["_tier"] == "package")
    ups = len(tools) - pkg
    allt = sorted(tools, key=lambda x: x["name"].lower())
    L = ["# All Tools\n",
         "Every tool has exactly one canonical card here, linked from whichever "
         "categories apply. **%d tools** — %d package-verified, %d upstream-documented "
         "(see [the README](../README.md#how-entries-are-verified)).\n" % (len(allt), pkg, ups),
         "| Tool | Category | Platform | Licence | Tier |", "|---|---|---|---|---|"]
    for t in allt:
        L.append("| **[%s](%s.md)** | [%s](../%s/) | %s | `%s` | %s |"
                 % (t["name"], t["_slug"], CAT_TITLE[t["_cat"]], t["_cat"], t["_platform"],
                    t.get("license") or "?",
                    "package" if t["_tier"] == "package" else "upstream"))
    L += ["", "---", "", "[All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)"]
    io.open(os.path.join(ROOT, "tools", "README.md"), "w",
            encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

    for folder, title, blurb in CATS:
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
        if folder in HANDWRITTEN:
            continue
        items = sorted(bycat.get(folder, []), key=lambda x: x["name"].lower())
        L = ["# %s\n" % title, "%s\n" % blurb]
        if items:
            np = sum(1 for t in items if t["_tier"] == "package")
            nu = len(items) - np
            bits = []
            if np: bits.append("%d package-verified" % np)
            if nu: bits.append("%d upstream-documented" % nu)
            L.append("**%d tool%s** — %s.\n" % (len(items), "" if len(items) == 1 else "s", ", ".join(bits)))
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
        io.open(os.path.join(ROOT, folder, "README.md"), "w",
                encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

    counts = {f: len(bycat.get(f, [])) for f, _, _ in CATS}
    io.open(os.path.join(ROOT, ".build", "counts.json"), "w", encoding="utf-8").write(
        json.dumps({"counts": counts, "total": len(tools),
                    "package": pkg, "upstream": ups}, indent=1))
    print("tools: %d  (package %d / upstream %d)" % (len(tools), pkg, ups))
    for f, _, _ in CATS:
        print("  %-28s %d" % (f, counts[f]))

main()
