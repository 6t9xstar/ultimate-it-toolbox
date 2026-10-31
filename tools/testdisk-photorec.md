# TestDisk & PhotoRec

> TestDisk recovers lost partitions and repairs boot sectors, and the bundled PhotoRec carves deleted files out of damaged or formatted media.

## Overview

| Property | Value |
|---|---|
| Category | Backup & Recovery |
| Official website | <https://www.cgsecurity.org/wiki/TestDisk> |
| Licence | `GPL-2.0-or-later` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | A+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id CGSecurity.TestDisk --exact
choco install testdisk-photorec
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Backup & Recovery](../18-backup-recovery/) · [All tools](../tools/) · [All categories](../README.md)
