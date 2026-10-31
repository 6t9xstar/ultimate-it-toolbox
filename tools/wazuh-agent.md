# Wazuh Agent

> The Wazuh agent forwards security events, file-integrity changes, and inventory data from this host to a Wazuh server. An existing Wazuh server is required.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://wazuh.com/> |
| Licence | `GNU General Public License (version 2)` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Wazuh.WazuhAgent --exact
choco install wazuh-agent
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `wazuhagent`.

---

[← Cybersecurity](../03-cybersecurity/) · [All categories](../README.md)
