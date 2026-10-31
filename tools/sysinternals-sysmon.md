# Sysinternals Sysmon

> Sysmon records process creation, network connections, and file and registry changes to the Windows event log for security monitoring. It runs as a service and needs a configuration file to be useful.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://learn.microsoft.com/sysinternals/downloads/sysmon> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Sysinternals.Sysmon --exact
choco install sysmon
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `sysmon`.

---

[← Cybersecurity](../03-cybersecurity/) · [All categories](../README.md)
