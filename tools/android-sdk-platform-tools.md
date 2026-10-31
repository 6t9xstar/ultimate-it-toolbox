# Android SDK Platform-Tools

> Android SDK Platform-Tools provides adb and fastboot, the command-line tools for talking to Android devices, sideloading, and flashing.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://developer.android.com/tools/releases/platform-tools> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Google.PlatformTools --exact
choco install adb
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `platformtools`.

---

[← Software Development](../04-development/) · [All categories](../README.md)
