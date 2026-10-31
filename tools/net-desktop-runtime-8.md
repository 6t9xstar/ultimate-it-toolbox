# .NET Desktop Runtime 8

> .NET Desktop Runtime 8 is a runtime environment required for running applications developed with .NET 8.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://dotnet.microsoft.com/download/dotnet/8.0> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.DotNet.DesktopRuntime.8 --exact
choco install dotnet-8.0-runtime
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `dotnet8`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All categories](../README.md)
