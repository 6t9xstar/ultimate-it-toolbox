# pgAdmin 4

> pgAdmin 4 is the official administration and development tool for PostgreSQL databases.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://www.pgadmin.org/download/pgadmin-4-windows/> |
| Licence | `PostgreSQL` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id PostgreSQL.pgAdmin --exact
choco install pgadmin4
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `pgadmin`.

---

[← Databases & Data Engineering](../07-databases/) · [All categories](../README.md)
