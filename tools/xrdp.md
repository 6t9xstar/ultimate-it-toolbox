# xrdp

> xrdp is an RDP server for Linux, so you can reach a Linux desktop with the Windows Remote Desktop client.

## Overview

| Property | Value |
|---|---|
| Category | Remote Access |
| Official website | <https://www.xrdp.org/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Linux |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Distribution package

```bash
sudo dnf install xrdp   # RHEL / Fedora (EPEL)
sudo apt install xrdp   # Debian / Ubuntu
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Remote Access](../19-remote-access/) · [All tools](../tools/) · [All categories](../README.md)
