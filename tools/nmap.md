# Nmap

> Nmap (Network Mapper) is an open-source tool for network exploration and security auditing. It discovers devices on a network and provides information about their ports and services.

## Overview

| Property | Value |
|---|---|
| Category | Networking |
| Official website | <https://nmap.org/> |
| Licence | `Modified GNU GPLv2` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Insecure.Nmap --exact
choco install nmap
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `nmap`.

---

[← Networking](../02-networking/) · [All categories](../README.md)
