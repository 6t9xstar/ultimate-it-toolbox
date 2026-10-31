# Veeam Agent for Microsoft Windows

> Veeam Agent for Microsoft Windows is a free image-level and file-level backup tool for workstations, with bare-metal recovery media.

## Overview

| Property | Value |
|---|---|
| Category | Backup & Recovery |
| Official website | <https://www.veeam.com/products/free/microsoft-windows.html> |
| Licence | `Freeware` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Veeam.VeeamAgent --exact
choco install veeam-agent
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Backup & Recovery](../18-backup-recovery/) · [All tools](../tools/) · [All categories](../README.md)
