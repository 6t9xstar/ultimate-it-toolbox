# iPerf3

> iPerf3 measures achievable TCP and UDP throughput between two hosts, the usual tool for proving a link's real bandwidth during network troubleshooting.

## Overview

| Property | Value |
|---|---|
| Category | Networking |
| Official website | <https://github.com/ar51an/iperf3-win-builds> |
| Licence | `BSD-3-Clause` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | CCNA, CCNP, Network+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id ar51an.iPerf3 --exact
choco install iperf3
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `iperf3`.

---

[← Networking](../02-networking/) · [All tools](../tools/) · [All categories](../README.md)
