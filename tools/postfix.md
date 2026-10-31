# Postfix

> Postfix is the most widely deployed open-source mail transfer agent, and the default MTA on RHEL.

## Overview

| Property | Value |
|---|---|
| Category | Web Infrastructure |
| Official website | <https://www.postfix.org/> |
| Licence | `IPL-1.0 or EPL-2.0` |
| Source model | Open source |
| Platform | Linux |
| Certification relevance | LFCS |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Distribution package

```bash
sudo dnf install postfix   # RHEL / Fedora
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Web Infrastructure](../10-web-infrastructure/) · [All tools](../tools/) · [All categories](../README.md)
