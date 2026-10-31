<div align="center">

# Ultimate IT Toolbox

**A curated directory of IT, networking, cybersecurity, Linux, Windows, development, DevOps, cloud, AI and productivity tools — discoverable by career, certification, platform and purpose.**

[![License: MIT](https://img.shields.io/badge/License-MIT-0567ff?style=for-the-badge)](LICENSE)
[![Tools: 759](https://img.shields.io/badge/tools-759-24292f?style=for-the-badge)](tools/)
[![Categories: 27](https://img.shields.io/badge/categories-27-24292f?style=for-the-badge)](#browse-by-category)
[![Verified](https://img.shields.io/badge/512-package%20verified-2ea043?style=for-the-badge)](#how-entries-are-verified)
[![Validate](https://github.com/6t9xstar/ultimate-it-toolbox/actions/workflows/validate.yml/badge.svg)](https://github.com/6t9xstar/ultimate-it-toolbox/actions/workflows/validate.yml)

[How to use](#how-to-use-this-directory) · [Browse by category](#browse-by-category) · [By certification](CERTIFICATION-MAP.md) · [Install bundles](bundles/) · [All tools](tools/) · [Contribute](CONTRIBUTING.md)

</div>

---

## What this is

Most "awesome" lists are a wall of links. This directory is built so you can find a tool **four ways**:

1. **By category** — you need a packet analyser, so you open [Networking](02-networking/).
2. **By certification** — you are studying for RHCSA or CCNA and want to know what to install. Open the [Certification Map](CERTIFICATION-MAP.md).
3. **By name** — you know what you want, so you search [all <!--n:total-->759<!--/n--> tools](tools/).
4. **By data** — you want to filter it yourself, so you load [`catalog.json`](data/catalog.json) or [`catalog.csv`](data/catalog.csv).

Every tool has **one canonical card** in [`tools/`](tools/), linked from whichever categories apply. Every card is generated from the data in [`.build/`](.build/), so there are no duplicate entries to keep in sync.

---

## How to use this directory

### Find a tool

| You want to… | Go to |
|---|---|
| Browse a subject area | The [category table](#browse-by-category) below |
| Install tools for a certification | [CERTIFICATION-MAP.md](CERTIFICATION-MAP.md), then the matching [bundle](bundles/) |
| Set up a new machine in one command | [Install bundles](bundles/) — role kits and whole categories |
| Search every tool at once | [`tools/`](tools/) — one table, <!--n:total-->759<!--/n--> rows |
| Filter or script against the list | [`data/catalog.json`](data/catalog.json) · [`data/catalog.csv`](data/catalog.csv) (opens in Excel) |
| Search and filter in a browser | [`index.html`](index.html) — a single-page search over the catalogue (see below) |
| Replace paid software | [Open-Source Alternatives](26-alternatives/) |
| Check what a licence actually is | The tool's own card — for Windows packages the licence row is copied from the package manifest |

**Search page.** [`index.html`](index.html) searches and filters the whole catalogue by name, category, certification, tier and source model, with a copy button for each install command. Enable GitHub Pages (Settings → Pages → deploy from `main`, root) to publish it, or run it locally:

```bash
python -m http.server 8000    # then open http://localhost:8000
```

On GitHub, press <kbd>t</kbd> on any page to open the file finder and type a tool name — it jumps straight to that card.

### Install something

Every **package-verified** card carries ready-to-run commands. Open the card and copy:

```powershell
winget install --id Publisher.Package --exact
```

To install several at once, pass the ids as queries. winget accepts `--id` only once per command, so do not repeat it:

```powershell
winget install --exact Git.Git Microsoft.VisualStudioCode Kubernetes.kubectl
```

If you prefer Chocolatey, the card gives that id too — and says so explicitly when no Chocolatey package exists, rather than leaving you to find out.

A few tools ship only through the Microsoft Store. Their cards use the Store source explicitly:

```powershell
winget install --id 9NT1R1C2HH7J --source msstore --exact
```

For **upstream-documented** cards (Linux, BSD, appliances, self-hosted), the card has a *How to get it* section with the real route — `dnf install`, a Docker Compose stack, an ISO, a Helm chart or a `pip`/`npm` package — because there is no Windows package to run.

### Install a whole set at once

The [bundles](bundles/) are standard `winget import` files: one per certification track, one per role (sysadmin, developer, DevOps, blue team, data science, local AI, modern CLI), and one per category.

```powershell
irm https://raw.githubusercontent.com/6t9xstar/ultimate-it-toolbox/main/bundles/ccna.winget.json -OutFile ccna.winget.json
winget import -i ccna.winget.json --accept-package-agreements --accept-source-agreements
```

Open the file before you run it. It is plain JSON, every id in it has a card, and you can delete any line you do not want.

Most of the original Windows entries are also in the [WinUtil Pro](https://github.com/6t9xstar/winutil-pro) Install tab, which installs them with checkboxes instead of commands; those cards say so.

### Read a card

Each card is the same shape, so you can scan it quickly:

- **Overview** — category, official site, licence, source model, platform, certification relevance, rating, date verified.
- **Install / How to get it** — the actual command or deployment route.
- **Verification** — which tier the entry is (see below) and what that guarantees.

---

## How entries are verified

This is where the directory differs from a hand-typed list. There are **two tiers**, and every card says which one it is.

### Tier 1 — package-verified (<!--n:package-->512<!--/n--> tools)

Windows tools installable with winget. For each one:

- The **winget id was confirmed against the live package source** on the date on the card. If `winget install` would fail, the entry is not here.
- The **Chocolatey id was checked separately** with an exact-match search; entries with no Chocolatey package say so rather than listing a name that will not resolve.
- The **licence string is copied from the package manifest**, not inferred from the project's reputation. Where a manifest is plainly wrong, the card keeps the corrected value and says what the manifest declared.
- The **official website** is the homepage the publisher declares in that manifest, or the project's own site where the manifest only points at a release page or an address that now redirects.

A [weekly check](.github/workflows/upstream-health.yml) confirms every winget id still exists in [microsoft/winget-pkgs](https://github.com/microsoft/winget-pkgs).

### Tier 2 — upstream-documented (<!--n:upstream-->247<!--/n--> tools)

Linux, BSD, Kubernetes, appliance and self-hosted tools — the things that cannot have a Windows package. For each one:

- The **official URL was HTTP-verified** to resolve, and is re-checked weekly.
- The **licence and install route are as documented upstream**, and are *not* machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.

That distinction is the honest one, and it is why the badge says <!--n:package-->512<!--/n--> rather than <!--n:total-->759<!--/n-->.

### What is deliberately *not* here

- **No invented ratings.** Almost every card reads `Not yet rated`. Labelling hundreds of tools "Best Overall" without testing them would be fiction that looks like evidence. [RATINGS.md](RATINGS.md) defines the vocabulary; the only ratings applied so far (<!--n:rated-->2<!--/n-->) are `Deprecated`, each with a link to the proof.
- **No invented metadata.** Skill level, competitors, limitations and benchmarks are left out until somebody measures them.
- **No dead projects.** Entries are dropped when upstream goes away — Focalboard was cut because its site stopped resolving after Mattermost discontinued it.
- **No licence-bypass tooling.** No cracks, keygens, pre-activated builds or activation scripts, for any product, ever.

---

## Browse by category

<!-- generated:categories:start -->
| # | Category | Tools |
|---|---|---|
| 01 | [Operating Systems & System Administration](01-operating-systems/) | 70 |
| 02 | [Networking](02-networking/) | 38 |
| 03 | [Cybersecurity](03-cybersecurity/) | 71 |
| 04 | [Software Development](04-development/) | 64 |
| 05 | [Cloud Computing](05-cloud-computing/) | 24 |
| 06 | [DevOps, Containers & IaC](06-devops/) | 73 |
| 07 | [Databases & Data Engineering](07-databases/) | 40 |
| 08 | [AI, Machine Learning & Data Science](08-ai-ml-data/) | 22 |
| 09 | [Virtualization & Storage](09-virtualization/) | 16 |
| 10 | [Web Infrastructure](10-web-infrastructure/) | 27 |
| 11 | [Quality Assurance & Testing](11-quality-assurance/) | 20 |
| 12 | [Hardware, IoT & Electronics](12-hardware-iot-robotics/) | 18 |
| 13 | [Design & Engineering](13-design-engineering/) | 35 |
| 14 | [Browsers](14-browser-tools/) | 19 |
| 15 | [Communication](15-communication/) | 25 |
| 16 | [Productivity & Office](16-productivity/) | 20 |
| 17 | [File Management](17-file-management/) | 21 |
| 18 | [Backup & Recovery](18-backup-recovery/) | 20 |
| 19 | [Remote Access](19-remote-access/) | 17 |
| 20 | [Terminal & CLI](20-terminal-cli/) | 31 |
| 21 | [Documentation & Knowledge](21-documentation/) | 26 |
| 22 | [SEO & Marketing](22-seo-marketing/) | 13 |
| 23 | [Privacy & Personal Security](23-privacy-security/) | 23 |
| 24 | [Project Management](24-project-management/) | 9 |
| 25 | [Learning & Certifications](25-learning-certifications/) | see map |
| 26 | [Open-Source & Self-Hosted Alternatives](26-alternatives/) | mapping |
| 27 | [Gaming](27-gaming/) | 17 |
<!-- generated:categories:end -->

Category 27 extends the base taxonomy to hold the gaming tools in the seed data.

## Browse by certification

The [Certification Map](CERTIFICATION-MAP.md) covers:

**RHCSA** · **RHCE** · **LFCS** · **CCNA** · **CCNP** · **CompTIA A+ / Network+ / Security+ / CySA+ / PenTest+** · **CKA / CKAD / CKS** · **AWS** · **Azure** · **Google Cloud** · **Terraform Associate** · **OSCP**

For each one it lists what you can install today, links the matching [bundle](bundles/), and — where the real answer is a VM, WSL or a vendor account — says so plainly instead of pretending a package exists. Tool cards carry the same information in their *Certification relevance* row.

## Repository layout

```text
ultimate-it-toolbox/
├── README.md                 # this file
├── CERTIFICATION-MAP.md      # find tools by certification
├── RATINGS.md                # the rating vocabulary, and why most entries are unrated
├── TOOL-TEMPLATE.md          # the canonical tool-card format
├── CONTRIBUTING.md           # how to add a tool, and the verification bar
├── SECURITY.md               # reporting a wrong package id or a hijacked project
├── CHANGELOG.md              # what changed, and when
├── tools/                    # one canonical card per tool        (generated)
├── 01-… 27-…/                # category indexes linking into tools/ (generated, except 25 and 26)
├── bundles/                  # winget import files                 (generated)
├── data/                     # catalog.json and catalog.csv        (generated)
├── index.html                # browser search over data/catalog.json
├── .build/                   # the data, the generator and the checks
└── .github/                  # CI, issue forms, PR template
```

### Maintaining it

The Markdown in `tools/`, the category folders, `bundles/` and `data/` is **generated**. Edit the data, then regenerate:

| File in `.build/` | Holds |
|---|---|
| `packages.json` | Tier-1 Windows packages: winget id, Chocolatey id, licence, category |
| `nonwindows.json` | Tier-2 Linux, appliance and self-hosted tools: install route and licence |
| `ratings.json` | The few ratings applied, each with a reason and evidence |
| `bundles.json` | Certification and role bundles (category bundles are automatic) |

```bash
python .build/validate.py          # check the data against the contribution rules
python .build/generate.py          # rewrite every generated file from the data
python .build/checklinks.py .      # every relative link and anchor resolves
```

CI runs all three on every pull request, plus `generate.py --check` to make sure nobody hand-edited a generated file. A weekly job runs `checkwinget.py` and `checkurls.py` to catch package ids and websites that have disappeared upstream.

Hand-written pages (`25-learning-certifications/`, `26-alternatives/`, `CERTIFICATION-MAP.md`) are not overwritten; only their `<!--n:…-->` counters are kept current.

## Credits

Tier-1 seed data and many tool descriptions derive from the [WinUtil Pro](https://github.com/6t9xstar/winutil-pro) install catalogue (MIT), itself a fork of [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) (MIT, © 2022 CT Tech Group LLC). Licence strings come from each package's own winget manifest.

Released under the [MIT License](LICENSE).

### Maintainer

**Malik Taimoor Awan** ([@6t9xstar](https://github.com/6t9xstar)) — [Apex Software Technology](https://apexsofteck.com), Lahore, Pakistan.

<div align="center">
<sub>If this directory saves you time, a ⭐ helps others find it.</sub>
</div>
