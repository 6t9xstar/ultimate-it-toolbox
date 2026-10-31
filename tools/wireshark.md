# Wireshark

> Wireshark is a widely-used open-source network protocol analyzer. It allows users to capture and analyze network traffic in real-time, providing detailed insights into network activities.

## Overview

| Property | Value |
|---|---|
| Category | Networking |
| Official website | <https://www.wireshark.org/> |
| Licence | `GPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id WiresharkFoundation.Wireshark --exact
choco install wireshark
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `wireshark`.

---

[← Networking](../02-networking/) · [All tools](../tools/) · [All categories](../README.md)
