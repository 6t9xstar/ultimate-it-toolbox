# Tenable Nessus

> Nessus is a widely used vulnerability scanner for networks and hosts. Nessus Essentials is free for up to 16 IP addresses; larger use needs a paid licence. Scan only systems you are authorised to assess.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://www.tenable.com/products/nessus> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Tenable.Nessus --exact
```

_No Chocolatey package is published for this tool; use winget._

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `nessus`.

---

[← Cybersecurity](../03-cybersecurity/) · [All categories](../README.md)
