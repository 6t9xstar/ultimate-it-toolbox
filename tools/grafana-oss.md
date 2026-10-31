# Grafana OSS

> Grafana is an open-source platform for monitoring and observability, letting you query, visualize, and alert on metrics from many data sources.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://grafana.com/oss/grafana/> |
| Licence | `AGPL-3.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id GrafanaLabs.Grafana.OSS --exact
choco install grafana
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `grafana`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All categories](../README.md)
