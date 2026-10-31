# Visual Studio 2022

> Visual Studio 2022 is an integrated development environment (IDE) for building, debugging, and deploying applications.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://visualstudio.microsoft.com/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.VisualStudio.2022.Community --exact
choco install visualstudio2022community
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `visualstudio2022`.

---

[← Software Development](../04-development/) · [All tools](../tools/) · [All categories](../README.md)
