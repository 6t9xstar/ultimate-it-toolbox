# SQL Server 2022 Express

> SQL Server 2022 Express is the free, size-limited edition of SQL Server that can be used for small production workloads.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://www.microsoft.com/sql-server> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Microsoft.SQLServer.2022.Express --exact
choco install sql-server-express
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Databases & Data Engineering](../07-databases/) · [All tools](../tools/) · [All categories](../README.md)
