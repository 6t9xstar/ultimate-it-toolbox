# NuGet

> NuGet is a package manager for the .NET framework, enabling developers to manage and share libraries in their .NET applications.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://www.nuget.org/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.NuGet --exact
choco install nuget.commandline
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `nuget`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All categories](../README.md)
