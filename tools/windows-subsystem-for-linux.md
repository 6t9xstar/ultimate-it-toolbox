# Windows Subsystem for Linux

> WSL runs real Linux distributions in a lightweight VM integrated with Windows, which makes it the fastest way to get a Linux shell for study or development.

## Overview

| Property | Value |
|---|---|
| Category | Virtualization & Storage |
| Official website | <https://learn.microsoft.com/windows/wsl/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | RHCSA, RHCE, LFCS, CCNP |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Microsoft.WSL --exact
choco install wsl2
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Virtualization & Storage](../09-virtualization/) · [All tools](../tools/) · [All categories](../README.md)
