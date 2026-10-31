# ZeroTier One

> ZeroTier One joins devices into one managed virtual network over the internet, as though they shared a LAN. Free for small networks; source-available under the BUSL rather than an OSI open-source licence.

## Overview

| Property | Value |
|---|---|
| Category | Networking |
| Official website | <https://www.zerotier.com/> |
| Licence | `BUSL-1.1` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id ZeroTier.ZeroTierOne --exact
choco install zerotier-one
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `zerotier`.

---

[← Networking](../02-networking/) · [All categories](../README.md)
