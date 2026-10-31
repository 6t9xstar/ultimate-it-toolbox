# SQLite

> SQLite is a self-contained, serverless, zero-configuration SQL database engine. This installs the command-line shell and tools; the engine itself is public domain.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://sqlite.org/> |
| Licence | `Public Domain` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id SQLite.SQLite --exact
choco install sqlite
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `sqlite`.

---

[← Databases & Data Engineering](../07-databases/) · [All tools](../tools/) · [All categories](../README.md)
