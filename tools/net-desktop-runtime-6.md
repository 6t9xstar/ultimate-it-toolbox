# .NET Desktop Runtime 6

> .NET Desktop Runtime 6 is a runtime environment required for running applications developed with .NET 6.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://dotnet.microsoft.com/download/dotnet/6.0> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | **Deprecated** — .NET 6 reached end of support on 12 November 2024 and no longer receives security fixes. Install it only for an app that still requires it. ([evidence](https://dotnet.microsoft.com/platform/support/policy/dotnet-core)) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.DotNet.DesktopRuntime.6 --exact
choco install dotnet-6.0-runtime
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `dotnet6`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All tools](../tools/) · [All categories](../README.md)
