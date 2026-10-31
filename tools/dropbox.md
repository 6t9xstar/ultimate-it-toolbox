# Dropbox

> Dropbox is a cloud storage client for syncing files, sharing content, and keeping documents available across devices.

## Overview

| Property | Value |
|---|---|
| Category | File Management |
| Official website | <https://www.dropbox.com/desktop> |
| Licence | `Combined GPLv2 and proprietary software` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Dropbox.Dropbox --exact
choco install dropbox
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `dropbox`.

---

[← File Management](../17-file-management/) · [All categories](../README.md)
