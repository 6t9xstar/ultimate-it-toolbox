# Jellyfin Server

> Jellyfin Server is an open-source media server software, allowing you to organize and stream your media library.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://jellyfin.org/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Jellyfin.Server --exact
choco install jellyfin
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `jellyfinserver`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All categories](../README.md)
