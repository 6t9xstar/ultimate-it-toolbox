# Cloudflare Tunnel (cloudflared)

> cloudflared is Cloudflare's daemon for Cloudflare Tunnel, exposing a local service to the internet through an outbound-only encrypted connection without opening inbound ports.

## Overview

| Property | Value |
|---|---|
| Category | Web Infrastructure |
| Official website | <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Cloudflare.cloudflared --exact
choco install cloudflared
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `cloudflared`.

---

[← Web Infrastructure](../10-web-infrastructure/) · [All categories](../README.md)
