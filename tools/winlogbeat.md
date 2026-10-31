# Winlogbeat

> Winlogbeat ships Windows event logs to Elasticsearch or Logstash. An existing Elastic stack is required. Source-available under the Elastic Licence rather than an OSI open-source licence.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://www.elastic.co/beats/winlogbeat> |
| Licence | `Elastic-2.0` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Certification relevance | CySA+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Elastic.Winlogbeat --exact
```

_No Chocolatey package is published for this tool; use winget._

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `winlogbeat`.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
