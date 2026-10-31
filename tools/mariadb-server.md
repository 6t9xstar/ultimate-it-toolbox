# MariaDB Server

> MariaDB is a community-developed, drop-in replacement fork of MySQL that stays open-source under the MariaDB Foundation. This installs the MariaDB Community Server.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://mariadb.org/download/> |
| Licence | `GPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id MariaDB.Server --exact
choco install mariadb
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `mariadb`.

---

[← Databases & Data Engineering](../07-databases/) · [All categories](../README.md)
