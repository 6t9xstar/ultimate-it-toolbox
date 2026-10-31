<div align="center">

# Ultimate IT Toolbox

**A curated directory of IT, networking, cybersecurity, Linux, Windows, development, DevOps, cloud, AI and productivity tools — discoverable by career, certification, platform and purpose.**

[![License: MIT](https://img.shields.io/badge/License-MIT-0567ff?style=for-the-badge)](LICENSE)
[![Tools: 482](https://img.shields.io/badge/tools-482-24292f?style=for-the-badge)](tools/)
[![Categories: 27](https://img.shields.io/badge/categories-27-24292f?style=for-the-badge)](#browse-by-category)
[![Verified](https://img.shields.io/badge/389-package%20verified-2ea043?style=for-the-badge)](#how-entries-are-verified)

[How to use](#how-to-use-this-directory) · [Browse by category](#browse-by-category) · [By certification](CERTIFICATION-MAP.md) · [All tools](tools/) · [Contribute](CONTRIBUTING.md)

</div>

---

## What this is

Most "awesome" lists are a wall of links. This directory is built so you can find a tool **three ways**:

1. **By category** — you need a packet analyser, so you open [Networking](02-networking/).
2. **By certification** — you are studying for RHCSA or CCNA and want to know what to install. Open the [Certification Map](CERTIFICATION-MAP.md).
3. **By name** — you know what you want, so you search [all 482 tools](tools/).

Every tool has **one canonical card** in [`tools/`](tools/), linked from whichever categories apply. There are no duplicate entries to keep in sync.

---

## How to use this directory

### Find a tool

| You want to… | Go to |
|---|---|
| Browse a subject area | The [category table](#browse-by-category) below |
| Install tools for a certification | [CERTIFICATION-MAP.md](CERTIFICATION-MAP.md) |
| Search every tool at once | [`tools/`](tools/) — one table, 482 rows, sortable by eye |
| Replace paid software | [Open-Source Alternatives](26-alternatives/) |
| Check what a licence actually is | The tool's own card — the licence row is copied from the package manifest |

On GitHub, press <kbd>t</kbd> on any page to open the file finder and type a tool name — it jumps straight to that card.

### Install something

Every **package-verified** card carries ready-to-run commands. Open the card and copy:

```powershell
winget install --id Publisher.Package --exact
```

To install several at once, chain the ids:

```powershell
winget install --id Git.Git --id Microsoft.VisualStudioCode --id Kubernetes.kubectl --exact
```

If you prefer Chocolatey, the card gives that id too — and says so explicitly when no Chocolatey package exists, rather than leaving you to find out.

For **upstream-documented** cards (Linux, BSD, appliances, self-hosted), the card has a *How to get it* section with the real route — `dnf install`, a Docker Compose stack, an ISO, or a vendor account — because there is no Windows package to run.

### Install a whole category at once

Most Windows entries in this directory are also in the [WinUtil Pro](https://github.com/6t9xstar/winutil-pro) Install tab, which installs them with checkboxes instead of commands:

```powershell
irm 6t9xstar.github.io/win | iex
```

Use this directory to decide *what* you want and understand *why*; use WinUtil Pro to install it in bulk.

### Read a card

Each card is the same shape, so you can scan it quickly:

- **Overview** — category, official site, licence, source model, platform, rating, date verified.
- **Install / How to get it** — the actual command or deployment route.
- **Verification** — which tier the entry is (see below) and what that guarantees.

---

## How entries are verified

This is where the directory differs from a hand-typed list. There are **two tiers**, and every card says which one it is.

### Tier 1 — package-verified (389 tools)

Windows tools, seeded from the WinUtil Pro catalogue. For each one:

- The **winget id was confirmed against the live package source**. If `winget install` would fail, the entry is not here.
- The **Chocolatey id was checked separately**; entries with no Chocolatey package say so rather than listing a name that will not resolve.
- The **licence string is copied from the package manifest**, not inferred from the project's reputation.
- The **official website** is the homepage the publisher declares in that manifest.

### Tier 2 — upstream-documented (93 tools)

Linux, BSD, appliance and self-hosted tools — the things that cannot have a Windows package. For each one:

- The **official URL was HTTP-verified** to resolve.
- The **licence and install route are as documented upstream**, and are *not* machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.

That distinction is the honest one, and it is why the badge says 389 rather than 482.

### What is deliberately *not* here

- **No invented ratings.** Every card reads `Not yet rated`. Labelling 482 tools "Best Overall" without testing them would be fiction that looks like evidence. [RATINGS.md](RATINGS.md) defines the vocabulary; humans apply it.
- **No invented metadata.** Skill level, competitors, limitations and benchmarks are left out until somebody measures them.
- **No dead projects.** Entries are dropped when upstream goes away — Focalboard was cut during the last pass because its site stopped resolving after Mattermost discontinued it.
- **No licence-bypass tooling.** No cracks, keygens, pre-activated builds or activation scripts, for any product, ever.

---

## Browse by category

| # | Category | Tools |
|---|---|---|
| 01 | [Operating Systems & System Administration](01-operating-systems/) | 64 |
| 02 | [Networking](02-networking/) | 25 |
| 03 | [Cybersecurity](03-cybersecurity/) | 51 |
| 04 | [Software Development](04-development/) | 64 |
| 05 | [Cloud Computing](05-cloud-computing/) | 6 |
| 06 | [DevOps, Containers & IaC](06-devops/) | 42 |
| 07 | [Databases & Data Engineering](07-databases/) | 18 |
| 08 | [AI, Machine Learning & Data Science](08-ai-ml-data/) | 5 |
| 09 | [Virtualization & Storage](09-virtualization/) | 5 |
| 10 | [Web Infrastructure](10-web-infrastructure/) | 17 |
| 11 | [Quality Assurance & Testing](11-quality-assurance/) | 6 |
| 12 | [Hardware, IoT & Electronics](12-hardware-iot-robotics/) | 11 |
| 13 | [Design & Engineering](13-design-engineering/) | 35 |
| 14 | [Browsers](14-browser-tools/) | 19 |
| 15 | [Communication](15-communication/) | 21 |
| 16 | [Productivity & Office](16-productivity/) | 15 |
| 17 | [File Management](17-file-management/) | 19 |
| 18 | [Backup & Recovery](18-backup-recovery/) | 9 |
| 19 | [Remote Access](19-remote-access/) | 6 |
| 20 | [Terminal & CLI](20-terminal-cli/) | 6 |
| 21 | [Documentation & Knowledge](21-documentation/) | 3 |
| 22 | [SEO & Marketing](22-seo-marketing/) | 1 |
| 23 | [Privacy & Personal Security](23-privacy-security/) | 11 |
| 24 | [Project Management](24-project-management/) | 6 |
| 25 | [Learning & Certifications](25-learning-certifications/) | see map |
| 26 | [Open-Source & Self-Hosted Alternatives](26-alternatives/) | mapping |
| 27 | [Gaming](27-gaming/) | 17 |

Category 27 extends the base taxonomy to hold the gaming tools in the seed data.

## Browse by certification

The [Certification Map](CERTIFICATION-MAP.md) covers:

**RHCSA** · **RHCE** · **CCNA** · **CCNP** · **CompTIA A+ / Network+ / Security+ / CySA+** · **CKA / CKAD / CKS** · **AWS** · **Azure** · **Google Cloud** · **LFCS** · **OSCP**

For each one it lists what you can install today, and — where the real answer is a VM, WSL or a vendor account — says so plainly instead of pretending a package exists. Cisco Packet Tracer, GNS3, EVE-NG, RHEL, Kali and the rest are now catalogued as tier-2 entries with their real sources.

## Repository layout

```text
ultimate-it-toolbox/
├── README.md                 # this file
├── CERTIFICATION-MAP.md      # find tools by certification
├── RATINGS.md                # the rating vocabulary, and why most entries are unrated
├── TOOL-TEMPLATE.md          # the canonical tool-card format
├── CONTRIBUTING.md           # how to add a tool, and the verification bar
├── SECURITY.md               # reporting a wrong package id or a hijacked project
├── tools/                    # one canonical card per tool (482)
├── 01-… 27-…/                # category indexes linking into tools/
└── .build/                   # generator and link checker
```

### Maintaining it

```bash
# Regenerate cards and category indexes from the data sources
python .build/generate.py <packages.json> .build/nonwindows.json .

# Validate every relative link and anchor in the repo
python .build/checklinks.py .
```

The link checker is the one to run before any pull request — it walks every Markdown file and reports broken paths and missing anchors. It currently reports **0 broken links**.

Hand-written pages (`25-learning-certifications/`, `26-alternatives/`) are listed in the generator's `HANDWRITTEN` set so a regeneration does not overwrite them.

## Credits

Tier-1 seed data and tool descriptions derive from the [WinUtil Pro](https://github.com/6t9xstar/winutil-pro) install catalogue (MIT), itself a fork of [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) (MIT, © 2022 CT Tech Group LLC). Licence strings come from each package's own winget manifest.

Released under the [MIT License](LICENSE).

### Maintainer

**Malik Taimoor Awan** ([@6t9xstar](https://github.com/6t9xstar)) — [Apex Software Technology](https://apexsofteck.com), Lahore, Pakistan.

<div align="center">
<sub>If this directory saves you time, a ⭐ helps others find it.</sub>
</div>
