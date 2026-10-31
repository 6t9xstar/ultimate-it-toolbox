# EA App

> EA App is a platform for accessing and playing Electronic Arts games.

## Overview

| Property | Value |
|---|---|
| Category | Gaming |
| Official website | <https://www.ea.com/ea-app> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id ElectronicArts.EADesktop --exact
choco install ea-app
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `eaapp`.

---

[← Gaming](../27-gaming/) · [All categories](../README.md)
