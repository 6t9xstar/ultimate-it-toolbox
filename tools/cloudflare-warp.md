# Cloudflare WARP

> Cloudflare WARP is a freemium VPN-like client that tunnels traffic through Cloudflare and uses its 1.1.1.1 DNS resolver, and it is also the endpoint agent for Cloudflare Zero Trust.

## Overview

| Property | Value |
|---|---|
| Category | Operating Systems & System Administration |
| Official website | <https://one.one.one.one> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Cloudflare.Warp --exact
choco install warp
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `CloudflareWARP`.

---

[← Operating Systems & System Administration](../01-operating-systems/) · [All tools](../tools/) · [All categories](../README.md)
