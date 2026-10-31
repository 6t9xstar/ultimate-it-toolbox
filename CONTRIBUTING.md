# Contributing

Thanks for helping. This directory has one rule that matters more than all the others:

> **Verify it, or do not add it.**

A tool list is only worth reading if its entries are true. An unverified package id is worse than a missing entry, because `winget install` on a bad id fails and the reader is left wondering whether the tool or the list is broken.

## How the repository works

Every card in `tools/`, every category index, every bundle in `bundles/` and the catalogue in `data/` is **generated** from four data files in [`.build/`](.build/). You edit the data; the generator writes the Markdown.

| File | Holds |
|---|---|
| `.build/packages.json` | Tier-1 Windows packages (winget id, Chocolatey id, licence, category) |
| `.build/nonwindows.json` | Tier-2 Linux, Kubernetes, appliance and self-hosted tools (install route, licence) |
| `.build/ratings.json` | Applied ratings, each with a reason and evidence |
| `.build/bundles.json` | Certification-track and role bundles |

A hand-edit to a generated file is overwritten on the next regeneration, and CI rejects it anyway (`generate.py --check`).

## Adding a Windows tool (tier 1)

1. **Check it is not already here.** Search [`tools/`](tools/) or `data/catalog.csv`. Each tool has exactly one card.
2. **Verify the winget id.**
   ```powershell
   winget show --id Publisher.Package --exact
   ```
   This confirms the id resolves and prints the publisher, homepage and licence. If it returns nothing, the id is wrong. For a Microsoft Store app, use `winget show --id <12-character id> --source msstore --exact`.
3. **Verify the Chocolatey id separately**, if there is one:
   ```powershell
   choco search package-id --exact --limit-output
   ```
   No output means there is no such package. Use `"choco": "na"`, and the card will say the tool is winget-only.
4. **Add one line to `.build/packages.json`:**
   ```json
   {"name": "Tool Name", "key": "tool-name", "folder": "20-terminal-cli", "desc": "One sentence, in your own words.", "link": "https://example.com/", "license": "MIT", "foss": true, "winget": "Publisher.Package", "source": "winget", "choco": "package-id", "verified": "2026-10-31", "winutil": false}
   ```
   - `license` is the string from the manifest. If the manifest is plainly wrong, record the correct licence and add `"license_note"` explaining what the manifest says and where the correct value comes from.
   - `link` is the manifest homepage, or the project's own site if the manifest only points at a release page or a URL that now redirects elsewhere.
   - `winutil` is `true` only if the tool is in the WinUtil Pro install catalogue under `key`.
5. **Regenerate and check** (see below).

## Adding a Linux, appliance or self-hosted tool (tier 2)

1. **Check the official URL resolves**, and that it is the project's own site or repository.
2. **Find the licence in the project's own licence file**, not on a third-party site.
3. **Add one line to `.build/nonwindows.json`:**
   ```json
   {"name": "Tool Name", "cat": "06-devops", "platform": "Kubernetes", "install": "Helm chart", "commands": ["helm install ..."], "licence": "Apache-2.0", "source": "Open source", "link": "https://example.com/", "desc": "One sentence, in your own words.", "certs": "CKA"}
   ```
   - `source` is one of `Open source`, `Proprietary`, `Mixed` or `Source available`. Say "Source available" for BUSL, SSPL, Elastic, fair-code and similar licences — that distinction matters to readers.
   - `commands` is optional. Include it only for a short, official route (a `dnf`/`apt` package, `pip`, `npm`, a one-line `docker run`).
   - `certs` is optional, and only for certifications the tool directly serves.

## Regenerate and check

```bash
python .build/validate.py        # the data follows the rules on this page
python .build/generate.py        # rewrite every generated file
python .build/checklinks.py .    # 0 broken links
```

CI runs all three on every pull request. The validator rejects, among other things: a missing field, a licence written as "Free" or "Open source", a non-https link, a duplicate name or package id, a Store id written as `msstore:…`, a description that is not a single sentence, and a bundle or rating that points at a tool that does not exist.

Two slower checks run weekly in CI, and you can run them yourself:

```bash
python .build/checkurls.py                         # every official website still resolves
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/microsoft/winget-pkgs.git /tmp/winget-pkgs
python .build/checkwinget.py /tmp/winget-pkgs      # every winget id still exists
```

## What gets rejected

- An entry whose package id does not resolve.
- A licence written as "Free", "Open source" or "Freeware" when the manifest or licence file states an actual licence.
- A description pasted from the vendor's marketing page or from another awesome-list. Write your own; most lists carry no licence permitting reuse.
- A rating with no justification — see [RATINGS.md](RATINGS.md).
- A link to a download aggregator, mirror, or any "crack", keygen, pre-activated build or licence-bypass tool. These are out of scope permanently, not pending review.
- Command-and-control frameworks and malware. Offensive tooling is in scope only where it is a standard part of authorised testing or certification study.
- Duplicate cards for one tool.
- Hand-edits to generated files.

## The highest-value contributions

| Gap | What is needed |
|---|---|
| **Ratings** | Pick a subcategory you know well and rate it properly, with reasons. Only `Deprecated` has been applied so far. |
| **Licence re-checks for tier 2** | Upstream licences change (Terraform, Redis, Elasticsearch and TheHive all did). Confirm a card against the project's licence file and update `.build/nonwindows.json`. |
| **Weekly-check fallout** | When the upstream-health workflow reports a dead URL or a missing winget id, fix or remove the entry. |
| **Certification coverage** | Extend [CERTIFICATION-MAP.md](CERTIFICATION-MAP.md) and `.build/bundles.json` with tracks you have actually sat. |
| **Thin categories** | SEO & Marketing, Project Management and Virtualization are still the smallest. |

## Style

- British or American spelling is fine; be consistent inside a file.
- One sentence per description. Say what it does, not why it is amazing.
- Prefer the publisher's own name for the tool, capitalised as they capitalise it.
- Keep tables narrow enough to read on GitHub without horizontal scrolling.
