# Process Explorer

> Process Explorer is a task manager and system monitor.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://learn.microsoft.com/sysinternals/downloads/process-explorer> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Sysinternals.ProcessExplorer --exact
choco install procexp
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `processexplorer`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All categories](../README.md)
