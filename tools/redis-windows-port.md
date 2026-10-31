# Redis (Windows port)

> Redis is an in-memory data store used as a database, cache, and message broker. This is the legacy Microsoft-maintained Windows port (Redis 3.x); for current versions run Redis under WSL or use a Redis-compatible Windows server such as Memurai.

## Overview

| Property | Value |
|---|---|
| Category | Databases & Data Engineering |
| Official website | <https://github.com/microsoftarchive/redis> |
| Licence | `BSD-3-Clause` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Redis.Redis --exact
choco install redis-64
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `redis`.

---

[← Databases & Data Engineering](../07-databases/) · [All categories](../README.md)
