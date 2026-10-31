# MongoDB Community Server

> MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents. This installs the Community Server edition.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://www.mongodb.com/try/download/community> |
| Licence | `Server Side Public License (SSPL)` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id MongoDB.Server --exact
choco install mongodb
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `mongodb`.

---

[← Databases & Data Engineering](../07-databases/) · [All tools](../tools/) · [All categories](../README.md)
