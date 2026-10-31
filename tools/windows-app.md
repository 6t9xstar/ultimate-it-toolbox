# Windows App

> Windows App is Microsoft's client for Azure Virtual Desktop, Windows 365, Dev Box and Remote Desktop Services, and replaces the older Remote Desktop client.

## Overview

| Property | Value |
|---|---|
| Category | Remote Access |
| Official website | <https://learn.microsoft.com/windows-app/overview> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Microsoft.WindowsApp --exact
choco install windows-app
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Remote Access](../19-remote-access/) · [All tools](../tools/) · [All categories](../README.md)
