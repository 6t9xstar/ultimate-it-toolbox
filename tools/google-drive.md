# Google Drive

> File syncing across devices all tied to your Google account.

## Overview

| Property | Value |
|---|---|
| Category | File Management |
| Official website | <https://www.google.com/drive/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Google.GoogleDrive --exact
choco install googledrive
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `googledrive`.

---

[← File Management](../17-file-management/) · [All categories](../README.md)
