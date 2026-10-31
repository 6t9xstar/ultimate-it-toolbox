# Edge

> Microsoft Edge is a modern web browser built on Chromium, offering performance, security, and integration with Microsoft services.

## Overview

| Property | Value |
|---|---|
| Category | Browsers |
| Official website | <https://www.microsoft.com/edge> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Edge --exact
choco install microsoft-edge
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `edge`.

---

[← Browsers](../14-browser-tools/) · [All categories](../README.md)
