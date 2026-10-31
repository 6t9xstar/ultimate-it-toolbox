# Zabbix Agent 2

> Zabbix Agent 2 collects metrics from this host and reports them to a Zabbix monitoring server. An existing Zabbix server is required.

## Overview

| Property | Value |
|---|---|
| Category | Networking |
| Official website | <https://www.zabbix.com/download_agents> |
| Licence | `AGPL-3.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Zabbix.Agent.2 --exact
choco install zabbix-agent
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `zabbixagent`.

---

[← Networking](../02-networking/) · [All categories](../README.md)
