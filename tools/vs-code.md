# VS Code

> Visual Studio Code is a free, open-source code editor with support for multiple programming languages.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://code.visualstudio.com/> |
| Licence | `Microsoft Software License` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | RHCE, CCNP, Azure, Terraform Associate |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.VisualStudioCode --exact
choco install vscode
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `vscode`.

---

[← Software Development](../04-development/) · [All tools](../tools/) · [All categories](../README.md)
