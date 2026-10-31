# Steam

> Steam is a digital distribution platform for purchasing and playing video games, offering multiplayer gaming, video streaming, and more.

## Overview

| Property | Value |
|---|---|
| Category | Gaming |
| Official website | <https://store.steampowered.com/about/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Valve.Steam --exact
choco install steam-client
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `steam`.

---

[← Gaming](../27-gaming/) · [All categories](../README.md)
