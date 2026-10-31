# MySQL

> MySQL is the world's most popular open-source relational database, widely used as the data store for web applications. This installs the MySQL Community Server.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://dev.mysql.com/downloads/> |
| Licence | `GPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Oracle.MySQL --exact
choco install mysql
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `mysql`.

---

[← Databases & Data Engineering](../07-databases/) · [All tools](../tools/) · [All categories](../README.md)
