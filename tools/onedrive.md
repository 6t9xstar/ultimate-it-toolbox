# OneDrive

> OneDrive is a cloud storage service provided by Microsoft, allowing users to store and share files securely across devices.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://onedrive.live.com/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.OneDrive --exact
choco install onedrive
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `onedrive`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All tools](../tools/) · [All categories](../README.md)
