# PostgreSQL 17

> PostgreSQL is a powerful open-source object-relational database system with a strong reputation for reliability, feature robustness, and standards compliance. This installs the version 17 server and client tools.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://www.postgresql.org/download/windows/> |
| Licence | `PostgreSQL` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id PostgreSQL.PostgreSQL.17 --exact
choco install postgresql
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `postgresql`.

---

[← Databases & Data Engineering](../07-databases/) · [All tools](../tools/) · [All categories](../README.md)
