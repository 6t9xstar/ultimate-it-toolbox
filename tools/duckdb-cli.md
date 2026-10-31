# DuckDB CLI

> DuckDB is an in-process analytical SQL database (OLAP) that runs embedded, with no server to manage. This installs the command-line interface.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://duckdb.org/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id DuckDB.cli --exact
choco install duckdb
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `duckdb`.

---

[← Databases & Data Engineering](../07-databases/) · [All categories](../README.md)
