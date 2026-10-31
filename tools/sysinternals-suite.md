# Sysinternals Suite

> The Sysinternals Suite is Microsoft's full set of Windows troubleshooting utilities, including Process Explorer, Process Monitor, Autoruns, TCPView, and Sysmon.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://learn.microsoft.com/sysinternals/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Certification relevance | A+, CySA+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.Sysinternals.Suite --exact
choco install sysinternals
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `sysinternalssuite`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All tools](../tools/) · [All categories](../README.md)
