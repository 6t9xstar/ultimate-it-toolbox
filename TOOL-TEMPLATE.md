# Tool Card Template

Cards are **generated** — you do not write this file by hand. Add a line to `.build/packages.json` (Windows) or `.build/nonwindows.json` (everything else) as described in [CONTRIBUTING.md](CONTRIBUTING.md), run `python .build/generate.py`, and the card below is produced for you.

This page documents the shape of a card, so you know what each row means and where it comes from.

## Tier 1 — package-verified

````markdown
# Tool Name

> One-sentence description of what it does, in your own words.

## Overview

| Property | Value |
|---|---|
| Category | Matching category from README.md |
| Official website | <https://example.com> |
| Licence | `SPDX-id-or-manifest-string` |
| Source model | Open source / Proprietary |
| Platform | Windows (packaged) |
| Certification relevance | Only if a certification bundle includes the tool |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | YYYY-MM-DD |

## Install on Windows

```powershell
winget install --id Publisher.Package --exact
choco install package-id
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on YYYY-MM-DD.
- Licence string copied from the package manifest, not inferred.

---

[← Category](../NN-category/) · [All tools](../tools/) · [All categories](../README.md)
````

Microsoft Store apps get `winget install --id <ProductId> --source msstore --exact`. A Store id is never written with an `msstore:` prefix — winget does not accept that.

## Tier 2 — upstream-documented

The *Install on Windows* section is replaced by:

````markdown
## How to get it

The install route, in a sentence: a distribution package, Docker Compose, an ISO, a Helm chart.

```bash
sudo dnf install example        # only when there is a short, official command
```

See the official site for current instructions — deployment steps change more often than this directory does.
````

The Verification section says the URL was checked and that the licence and install route are as documented upstream, not machine-verified.

## Where each row comes from

| Row | Source |
|---|---|
| Licence | Tier 1: the winget manifest (or a stated correction). Tier 2: the project's licence file. |
| Source model | `foss` in packages.json; `source` in nonwindows.json. |
| Certification relevance | Tier 1: every certification bundle in `bundles.json` that lists the tool. Tier 2: the `certs` field. |
| Rating | `ratings.json`, with a reason and evidence; otherwise "Not yet rated". |
| Last verified | The date the id or URL was last confirmed. |

## Rules

1. **Verify the package id.** Run `winget show --id <id> --exact` before adding it. An id that does not resolve installs nothing.
2. **Copy the licence from the manifest.** Do not write "Free" or "Open source" where a licence string belongs.
3. **Link the publisher's own site**, not a download aggregator or a mirror.
4. **Write your own description.** Do not paste vendor marketing copy, or text from another directory — many carry no licence that permits reuse.
5. **One card per tool.** It is linked from category indexes, bundles and the certification map rather than copied.
6. **No package, no invented package.** A tool without a Windows package belongs in `nonwindows.json` with its real install route, not in `packages.json` with a guessed id.
