# Process Monitor

> SysInternals Process Monitor is an advanced monitoring tool that shows real-time file system, registry, and process/thread activity.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://docs.microsoft.com/en-us/sysinternals/downloads/procmon> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Sysinternals.ProcessMonitor --exact
choco install procmon
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `processmonitor`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All tools](../tools/) · [All categories](../README.md)
