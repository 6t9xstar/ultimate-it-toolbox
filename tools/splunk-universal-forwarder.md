# Splunk Universal Forwarder

> The Splunk Universal Forwarder sends logs from this host to a Splunk indexer. An existing Splunk deployment and licence are required.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://www.splunk.com/en_us/download/universal-forwarder.html> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Splunk.UniversalForwarder --exact
choco install splunk-universalforwarder
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `splunkforwarder`.

---

[← Cybersecurity](../03-cybersecurity/) · [All categories](../README.md)
