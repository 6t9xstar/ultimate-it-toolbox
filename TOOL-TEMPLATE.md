# Tool Card Template

Copy the block below into `tools/<slug>.md`. Fill in only what you can verify. Delete a row you cannot substantiate rather than guessing — an absent row is useful, a wrong row is not.

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
| Platform | Windows (packaged) / Linux / macOS / Web / Self-hosted |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | YYYY-MM-DD |

## Install on Windows

```powershell
winget install --id Publisher.Package --exact
choco install package-id
```

## Verification

- Package id confirmed against the live `winget` source on YYYY-MM-DD.
- Licence string is copied from the package manifest, not inferred.

---

[← Category](../NN-category/) · [All categories](../README.md)
````

## Optional sections

Add these **only** when you have real information:

- `## Best for` — the situation it genuinely suits.
- `## Alternatives` — other entries in this directory, linked.
- `## Limitations` — concrete limits you have hit, not speculation.
- `## Career relevance` — the certifications or roles it maps to.
- `## Notes` — licensing caveats: free tiers, seat limits, account requirements.

## Rules

1. **Verify the package id.** Run `winget show --id <id> --exact` before adding it. An id that does not resolve installs nothing, silently — which is worse than an absent entry, because the user believes the install worked.
2. **Copy the licence from the manifest.** Do not write "Free" or "Open source" where a licence string belongs. `winget show` prints it.
3. **Link the publisher's own site**, not a download aggregator or a mirror.
4. **Write your own description.** Do not paste vendor marketing copy, or text from another directory — many carry no licence that permits reuse.
5. **One card per tool.** Link it from several category indexes rather than copying it. The card is the single source of truth.
6. **No package, no entry.** If a tool has no Windows package, do not invent one. Name it in the category index under "get it elsewhere" with its real download source.
