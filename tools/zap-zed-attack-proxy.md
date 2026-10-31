# ZAP (Zed Attack Proxy)

> ZAP is an open-source web application security scanner and intercepting proxy. Requires Java. Only scan applications you own or are authorized to assess.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://github.com/zaproxy/zaproxy> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | OSCP |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id ZAP.ZAP --exact
choco install zap
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `zap`.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
