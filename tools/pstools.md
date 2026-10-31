# PsTools

> Microsoft Sysinternals PsTools provides utilities for managing local and remote Windows systems and monitoring processes. PsExec can run processes under the SYSTEM account when the user has local administrative rights on the target system.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://learn.microsoft.com/en-us/sysinternals/downloads/pstools> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Sysinternals.PsTools --exact
choco install pstools
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `pstools`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All categories](../README.md)
