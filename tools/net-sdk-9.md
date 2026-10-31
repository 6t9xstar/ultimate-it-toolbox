# .NET SDK 9

> The .NET SDK is Microsoft's free, cross-platform developer platform for building web, desktop, cloud, and console applications in C#, F#, and Visual Basic. This installs the 9.0 SDK.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://dotnet.microsoft.com/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.DotNet.SDK.9 --exact
choco install dotnet-9.0-sdk
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `dotnetsdk9`.

---

[← Software Development](../04-development/) · [All categories](../README.md)
