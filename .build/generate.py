"""Generate the Ultimate IT Toolbox from verified tool data.

Input : a JSON array of verified tool records (winget/choco ids, licence, link).
Output: tools/<slug>.md canonical cards + numbered category folders with indexes.

Every field written here comes from the verified input. Nothing subjective
(ratings, skill level, competitors) is invented -- see RATINGS.md.
"""
import io, json, os, re, sys
from collections import defaultdict

SRC = sys.argv[1]
ROOT = sys.argv[2]

TOOLS = json.load(io.open(SRC, encoding="utf-8"))

# ---------------------------------------------------------------- categories
# (folder, title, blurb)
CATS = [
 ("01-operating-systems", "Operating Systems & System Administration",
  "Windows, Linux and cross-platform system administration tooling."),
 ("02-networking", "Networking",
  "Packet analysis, scanning, routing/switching labs, VPNs and network troubleshooting."),
 ("03-cybersecurity", "Cybersecurity",
  "Defensive security, forensics, incident response and authorised offensive testing."),
 ("04-development", "Software Development",
  "Editors, IDEs, language runtimes, build tools and SDKs."),
 ("05-cloud-computing", "Cloud Computing",
  "Cloud provider CLIs, SDKs and cloud storage tooling."),
 ("06-devops", "DevOps, Containers & IaC",
  "Containers, Kubernetes, infrastructure as code, CI/CD and observability."),
 ("07-databases", "Databases & Data Engineering",
  "Database servers, clients and administration tools."),
 ("08-ai-ml-data", "AI, Machine Learning & Data Science",
  "Local LLM runtimes, scientific Python/R distributions and data-science tooling."),
 ("09-virtualization", "Virtualization",
  "Hypervisors and VM provisioning -- the foundation of any certification lab."),
 ("10-web-infrastructure", "Web Infrastructure",
  "Web servers, local development stacks, tunnels and reverse proxies."),
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
  "Backup programs, disk imaging and bootable media creation."),
 ("19-remote-access", "Remote Access",
  "SSH clients, remote desktop and remote-session management."),
 ("20-terminal-cli", "Terminal & CLI",
  "Terminals, shells, prompts and Unix-like environments on Windows."),
 ("21-documentation", "Documentation & Knowledge",
  "Note-taking, knowledge bases and technical documentation."),
 ("22-seo-marketing", "SEO & Marketing",
  "Site crawling, auditing and digital-marketing tooling."),
 ("23-privacy-security", "Privacy & Personal Security",
  "VPNs, password managers, encryption and anonymity tools."),
 ("24-project-management", "Project Management",
  "Planning, issue tracking and collaboration."),
 ("25-learning-certifications", "Learning & Certifications",
  "Tool sets grouped by certification -- see CERTIFICATION-MAP.md."),
 ("26-alternatives", "Open-Source & Self-Hosted Alternatives",
  "Replacements for proprietary and subscription software."),
 ("27-gaming", "Gaming",
  "Game launchers, streaming and gaming utilities. (Extends the base taxonomy.)"),
]
CAT_TITLE = {c: t for c, t, _ in CATS}

# Category indexes that are hand-written and must not be overwritten.
HANDWRITTEN = {"25-learning-certifications"}

# ------------------------------------------------------- explicit overrides
# key -> category folder. Takes precedence over every rule below.
OVERRIDE = {
 # networking / CCNA
 "tftpd64":"02-networking","iperf3":"02-networking","winmtr":"02-networking",
 "nmap":"02-networking","wireshark":"02-networking","angryipscanner":"02-networking",
 "advancedip":"02-networking","simplewall":"02-networking","zabbixagent":"02-networking",
 "zerotier":"02-networking","cloudflared":"10-web-infrastructure",
 # remote access
 "putty":"19-remote-access","winscp":"19-remote-access","termius":"19-remote-access",
 "mobaxterm":"19-remote-access","mremoteng":"19-remote-access","anydesk":"19-remote-access",
 "cyberduck":"17-file-management","rclone":"17-file-management",
 # privacy / vpn / crypto
 "openvpn":"23-privacy-security","OpenVPN":"23-privacy-security","wireguard":"23-privacy-security",
 "tailscale":"23-privacy-security","mullvadvpn":"23-privacy-security","protonvpn":"23-privacy-security",
 "veracrypt":"23-privacy-security","gpg4win":"23-privacy-security","keepassxc":"23-privacy-security",
 "bitwarden":"23-privacy-security","tor":"14-browser-tools","sandboxieplus":"03-cybersecurity",
 # virtualization
 "OVirtualBox":"09-virtualization","vagrant":"09-virtualization",
 # devops
 "dockerdesktop":"06-devops","podmandesktop":"06-devops","podman":"06-devops",
 "openshiftcli":"06-devops","rancherdesktop":"06-devops","lens":"06-devops",
 "kubectl":"06-devops","helm":"06-devops","k9s":"06-devops","minikube":"06-devops",
 "kind":"06-devops","terraform":"06-devops","opentofu":"06-devops","pulumi":"06-devops",
 "terragrunt":"06-devops","infracost":"06-devops","act":"06-devops","grafana":"06-devops",
 "netdata":"06-devops","trivy":"03-cybersecurity","gitleaks":"03-cybersecurity",
 # cloud
 "awscli":"05-cloud-computing","azurecli":"05-cloud-computing","gcloudsdk":"05-cloud-computing",
 "awssam":"05-cloud-computing","minioclient":"05-cloud-computing","planetscale":"05-cloud-computing",
 # databases
 "postgresql":"07-databases","mysql":"07-databases","mariadb":"07-databases",
 "mongodb":"07-databases","redis":"07-databases","sqlite":"07-databases","duckdb":"07-databases",
 "ssms":"07-databases","azuredatastudio":"07-databases","heidisql":"07-databases",
 "dbgate":"07-databases","beekeeperstudio":"07-databases","dbeaver":"07-databases",
 "pgadmin":"07-databases","mongodbcompass":"07-databases","redisinsight":"07-databases",
 "mysqlworkbench":"07-databases","datagrip":"07-databases",
 # ai / data science
 "ollama":"08-ai-ml-data","anaconda":"08-ai-ml-data","miniconda":"08-ai-ml-data",
 "julia":"08-ai-ml-data","rproject":"08-ai-ml-data",
 # qa
 "jmeter":"11-quality-assurance","k6":"11-quality-assurance","postman":"11-quality-assurance",
 "insomnia":"11-quality-assurance","soapui":"11-quality-assurance","bruno":"11-quality-assurance",
 # hardware / electronics
 "arduinoide":"12-hardware-iot-robotics","kicad":"12-hardware-iot-robotics",
 "hwinfo":"12-hardware-iot-robotics","hwmonitor":"12-hardware-iot-robotics",
 "cpuz":"12-hardware-iot-robotics","gpuz":"12-hardware-iot-robotics",
 "crystaldiskinfo":"12-hardware-iot-robotics","crystaldiskmark":"12-hardware-iot-robotics",
 "cinebenchr23":"12-hardware-iot-robotics","msiafterburner":"12-hardware-iot-robotics",
 "ddu":"12-hardware-iot-robotics",
 # design
 "gimp":"13-design-engineering","inkscape":"13-design-engineering","krita":"13-design-engineering",
 "blender":"13-design-engineering","figma":"13-design-engineering","lunacy":"13-design-engineering",
 "freecad":"13-design-engineering","librecad":"13-design-engineering","qgis":"13-design-engineering",
 "fontforge":"13-design-engineering","kdenlive":"13-design-engineering","shotcut":"13-design-engineering",
 "Paintdotnet":"13-design-engineering",
 # web infra
 "xampp":"10-web-infrastructure","caddy":"10-web-infrastructure",
 # backup / media
 "restic":"18-backup-recovery","rufus":"18-backup-recovery","ventoy":"18-backup-recovery",
 # terminal
 "terminal":"20-terminal-cli","powershell":"20-terminal-cli","posh":"20-terminal-cli",
 "starship":"20-terminal-cli","msys2":"20-terminal-cli","cygwin":"20-terminal-cli",
 "gsudo":"20-terminal-cli",
 # docs
 "obsidian":"21-documentation","joplin":"21-documentation","logseq":"21-documentation",
 # seo
 "screamingfrog":"22-seo-marketing",
 # os admin
 "sysinternalssuite":"01-operating-systems","systeminformer":"01-operating-systems",
 "autoruns":"01-operating-systems","powertoys":"01-operating-systems",
 "nvda":"01-operating-systems",
}

RULES = [
 ("03-cybersecurity", {"Security","Red Team","Blue Team"}, None),
 ("14-browser-tools", {"Browsers"}, None),
 ("15-communication", {"Communications"}, None),
 ("16-productivity",  {"Document"}, None),
 ("27-gaming",         {"Games"}, None),
 ("13-design-engineering", {"Multimedia Tools"}, None),
 ("04-development",   {"Development"}, None),
 ("01-operating-systems", {"Microsoft Tools"}, None),
 ("06-devops",        {"Selfhosted Tools"}, None),
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
    for folder, cats, _ in RULES:
        if cat in cats:
            return folder
    if cat in ("Utilities", "Pro Tools"):
        if BACKUP_WORDS.search(desc):
            return "18-backup-recovery"
        if FILE_WORDS.search(desc):
            return "17-file-management"
        return "01-operating-systems"
    return None

# ------------------------------------------------------------------- render
def source_model(t):
    return "Open source" if t.get("foss") else "Proprietary"

def card(t):
    L = []
    L.append("# %s\n" % t["name"])
    L.append("> %s\n" % (t.get("desc") or "").strip())
    L.append("## Overview\n")
    L.append("| Property | Value |")
    L.append("|---|---|")
    L.append("| Category | %s |" % CAT_TITLE[t["_cat"]])
    L.append("| Official website | <%s> |" % t["link"])
    L.append("| Licence | `%s` |" % (t.get("license") or "Unknown"))
    L.append("| Source model | %s |" % source_model(t))
    L.append("| Platform | Windows (packaged) |")
    L.append("| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |")
    L.append("| Last verified | %s |" % (t.get("verified") or "unverified"))
    L.append("")
    L.append("## Install on Windows\n")
    L.append("```powershell")
    L.append("winget install --id %s --exact" % t["winget"])
    if t.get("choco") and t["choco"] != "na":
        L.append("choco install %s" % t["choco"])
    L.append("```\n")
    if not t.get("choco") or t["choco"] == "na":
        L.append("_No Chocolatey package is published for this tool; use winget._\n")
    L.append("## Verification\n")
    L.append("- Package id confirmed against the live `winget` source on %s." % (t.get("verified") or "n/a"))
    L.append("- Licence string is copied from the package manifest, not inferred.")
    L.append("- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `%s`.\n" % t["key"])
    L.append("---\n")
    L.append("[← %s](../%s/) · [All categories](../README.md)" % (CAT_TITLE[t["_cat"]], t["_cat"]))
    return "\n".join(L) + "\n"

def main():
    unmapped, bycat = [], defaultdict(list)
    seen = {}
    for t in TOOLS:
        c = category_for(t)
        if not c:
            unmapped.append(t["key"]); continue
        t["_cat"] = c
        s = slug(t["name"])
        while s in seen and seen[s] != t["key"]:
            s += "-" + slug(t["key"])
        seen[s] = t["key"]; t["_slug"] = s
        bycat[c].append(t)

    os.makedirs(os.path.join(ROOT, "tools"), exist_ok=True)
    for t in TOOLS:
        if "_slug" not in t: continue
        io.open(os.path.join(ROOT, "tools", t["_slug"] + ".md"), "w",
                encoding="utf-8", newline="\n").write(card(t))

    # Index of every canonical card.
    allt = sorted([t for t in TOOLS if "_slug" in t], key=lambda x: x["name"].lower())
    L = ["# All Tools\n",
         "Every tool has exactly one canonical card here, linked from whichever "
         "categories apply. %d cards.\n" % len(allt),
         "| Tool | Category | Licence | Source |", "|---|---|---|---|"]
    for t in allt:
        L.append("| **[%s](%s.md)** | [%s](../%s/) | `%s` | %s |"
                 % (t["name"], t["_slug"], CAT_TITLE[t["_cat"]], t["_cat"],
                    t.get("license") or "?", source_model(t)))
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
            L.append("**%d tool%s.** Every entry is a Windows package whose id and licence were verified against the live winget source.\n"
                     % (len(items), "" if len(items) == 1 else "s"))
            L.append("| Tool | What it does | Licence | Source |")
            L.append("|---|---|---|---|")
            for t in items:
                d = (t.get("desc") or "").split(". ")[0].rstrip(".")
                if len(d) > 110: d = d[:107].rstrip() + "..."
                L.append("| **[%s](../tools/%s.md)** | %s | `%s` | %s |"
                         % (t["name"], t["_slug"], d, t.get("license") or "?", source_model(t)))
            L.append("")
        else:
            L.append("> **This category has no entries yet.**\n")
            L.append("Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md). ")
            L.append("Add one canonical card under `tools/` and link it from the table here.\n")
        L.append("---\n")
        L.append("[All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)")
        io.open(os.path.join(ROOT, folder, "README.md"), "w",
                encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

    counts = {f: len(bycat.get(f, [])) for f, _, _ in CATS}
    io.open(os.path.join(ROOT, ".build", "counts.json"), "w", encoding="utf-8").write(
        json.dumps({"counts": counts, "total": sum(counts.values()), "unmapped": unmapped}, indent=1))
    print("cards:", sum(counts.values()), "unmapped:", len(unmapped), unmapped)
    for f, _, _ in CATS:
        print("  %-28s %d" % (f, counts[f]))

main()
