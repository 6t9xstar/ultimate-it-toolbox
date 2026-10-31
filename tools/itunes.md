# iTunes

> iTunes is a media player, media library, and online radio broadcaster application developed by Apple Inc.

## Overview

| Property | Value |
|---|---|
| Category | Design & Engineering |
| Official website | <https://www.apple.com/itunes/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Apple.iTunes --exact
choco install itunes
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `itunes`.

---

[← Design & Engineering](../13-design-engineering/) · [All categories](../README.md)
