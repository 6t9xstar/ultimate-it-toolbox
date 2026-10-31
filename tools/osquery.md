# osquery

> osquery exposes the operating system as a SQL database, so running processes, listening ports, and installed packages can be queried for security monitoring.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://www.osquery.io/> |
| Licence | `Apache-2.0 OR GPL-2.0-only` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | CySA+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id osquery.osquery --exact
choco install osquery
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `osquery`.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
