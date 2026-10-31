<div align="center">

# Ultimate IT Toolbox

**A curated directory of IT, networking, cybersecurity, Linux, Windows, development, DevOps, cloud, AI and productivity tools — discoverable by career, certification, platform and purpose.**

[![License: MIT](https://img.shields.io/badge/License-MIT-0567ff?style=for-the-badge)](LICENSE)
[![Tools: 389](https://img.shields.io/badge/tools-389-24292f?style=for-the-badge)](#browse-by-category)
[![Categories: 27](https://img.shields.io/badge/categories-27-24292f?style=for-the-badge)](#browse-by-category)
[![Verified](https://img.shields.io/badge/package%20ids-verified-2ea043?style=for-the-badge)](#how-entries-are-verified)

[Browse by category](#browse-by-category) · [Browse by certification](CERTIFICATION-MAP.md) · [Contribute](CONTRIBUTING.md) · [Rating system](RATINGS.md)

</div>

---

## What this is

Most "awesome" lists are a wall of links. This directory is built so you can find a tool **two ways**:

1. **By category** — you know you need a packet analyser, so you open [Networking](02-networking/).
2. **By certification or career** — you are studying for RHCSA or CCNA and want to know what to install. Open the [Certification Map](CERTIFICATION-MAP.md).

Every tool has **one canonical record** in [`tools/`](tools/), linked from whichever categories apply. There are no duplicate entries to keep in sync.

## How entries are verified

This is the part that matters, and it is where this directory differs from a hand-typed list.

Every one of the 389 current entries was generated from data where:

- The **package id was confirmed against the live winget source** — not guessed. If `winget install` would fail, the entry is not here.
- The **licence string is copied from the package manifest**, not inferred from the project's reputation.
- The **Chocolatey id was confirmed separately**, and entries with no Chocolatey package say so explicitly rather than listing a name that does not resolve.
- The **official website** is the homepage the publisher declares in the manifest.
- Each card records the **date it was verified**.

### What is deliberately *not* here

- **No invented ratings.** Every card says `Not yet rated`. Labelling 389 tools "Best Overall" without testing them would be fiction. [RATINGS.md](RATINGS.md) defines the vocabulary; humans apply it.
- **No invented metadata.** Skill level, competitors, limitations and performance numbers are left out until someone measures them.
- **No tools that cannot be installed.** If a tool has no Windows package, it is named in the relevant category as "get it elsewhere" with the real source, rather than listed as an entry that would install nothing.

## Current scope, honestly

The verified seed data covers **Windows-installable packages**. That is the directory's current strength and its current limit.

| Covered now | Not yet covered |
|---|---|
| 389 Windows tools with verified winget/Chocolatey ids and licences | Linux-native tools (RHEL, Cockpit, Ansible, the Kali toolset) |
| 27 categories across sysadmin, networking, security, dev, DevOps, cloud, data, design | Self-hosted server software (pfSense, Proxmox, Mailcow, Coolify) |
| Certification mapping for RHCSA, RHCE, CCNA, CompTIA, CKA/CKAD/CKS, cloud, OSCP | Web-only services, macOS-only and mobile-only tools |

Expanding into Linux, self-hosted and web tooling is the main contribution opportunity — see [CONTRIBUTING.md](CONTRIBUTING.md). The rule there is the same as above: **verify it, or do not add it.**

## Browse by category

| # | Category | Tools |
|---|---|---|
| 01 | [Operating Systems & System Administration](01-operating-systems/) | 55 |
| 02 | [Networking](02-networking/) | 10 |
| 03 | [Cybersecurity](03-cybersecurity/) | 22 |
| 04 | [Software Development](04-development/) | 64 |
| 05 | [Cloud Computing](05-cloud-computing/) | 6 |
| 06 | [DevOps, Containers & IaC](06-devops/) | 31 |
| 07 | [Databases & Data Engineering](07-databases/) | 18 |
| 08 | [AI, Machine Learning & Data Science](08-ai-ml-data/) | 5 |
| 09 | [Virtualization](09-virtualization/) | 2 |
| 10 | [Web Infrastructure](10-web-infrastructure/) | 2 |
| 11 | [Quality Assurance & Testing](11-quality-assurance/) | 6 |
| 12 | [Hardware, IoT & Electronics](12-hardware-iot-robotics/) | 11 |
| 13 | [Design & Engineering](13-design-engineering/) | 35 |
| 14 | [Browsers](14-browser-tools/) | 19 |
| 15 | [Communication](15-communication/) | 21 |
| 16 | [Productivity & Office](16-productivity/) | 15 |
| 17 | [File Management](17-file-management/) | 19 |
| 18 | [Backup & Recovery](18-backup-recovery/) | 6 |
| 19 | [Remote Access](19-remote-access/) | 6 |
| 20 | [Terminal & CLI](20-terminal-cli/) | 6 |
| 21 | [Documentation & Knowledge](21-documentation/) | 3 |
| 22 | [SEO & Marketing](22-seo-marketing/) | 1 |
| 23 | [Privacy & Personal Security](23-privacy-security/) | 9 |
| 24 | [Project Management](24-project-management/) | — |
| 25 | [Learning & Certifications](25-learning-certifications/) | see map |
| 26 | [Open-Source & Self-Hosted Alternatives](26-alternatives/) | — |
| 27 | [Gaming](27-gaming/) | 17 |

Categories 24 and 26 are scaffolded and empty — they need entries that are mostly web or self-hosted, which the verified seed does not cover yet. Category 27 extends the base taxonomy to hold the gaming tools in the seed data.

## Browse by certification

The [Certification Map](CERTIFICATION-MAP.md) covers:

**RHCSA** · **RHCE** · **CCNA** · **CCNP** · **CompTIA A+ / Network+ / Security+ / CySA+** · **CKA / CKAD / CKS** · **AWS** · **Azure** · **Google Cloud** · **LFCS** · **OSCP**

For each one it lists what you can install today, and — where the real answer is a VM, WSL or a vendor account — says so plainly instead of pretending a package exists.

## Repository layout

```text
ultimate-it-toolbox/
├── README.md                 # this file
├── CERTIFICATION-MAP.md      # find tools by certification
├── RATINGS.md                # the rating vocabulary and why most entries are unrated
├── TOOL-TEMPLATE.md          # the canonical tool-card format
├── CONTRIBUTING.md           # how to add a tool (and the verification bar)
├── SECURITY.md               # reporting issues
├── tools/                    # one canonical card per tool
└── 01-… 27-…/                # category indexes linking into tools/
```

## Credits

Seed data and tool descriptions derive from the [WinUtil Pro](https://github.com/6t9xstar/winutil-pro) install catalogue (MIT), itself a fork of [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) (MIT, © 2022 CT Tech Group LLC). Licence strings come from each package's own winget manifest.

Released under the [MIT License](LICENSE).

### Maintainer

**Malik Taimoor Awan** ([@6t9xstar](https://github.com/6t9xstar)) — [Apex Software Technology](https://apexsofteck.com), Lahore, Pakistan.

<div align="center">
<sub>If this directory saves you time, a ⭐ helps others find it.</sub>
</div>
