# SQL Server Management Studio

> SQL Server Management Studio (SSMS) is Microsoft's integrated environment for managing SQL Server and Azure SQL databases, from queries to administration.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.SQLServerManagementStudio --exact
choco install sql-server-management-studio
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `ssms`.

---

[← Databases & Data Engineering](../07-databases/) · [All categories](../README.md)
