# OWASP Juice Shop

> OWASP Juice Shop is a deliberately insecure web shop for practising web-application attacks legally, covering the OWASP Top 10 and more.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://owasp.org/www-project-juice-shop/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Self-hosted (Docker) |
| Certification relevance | OSCP, PenTest+, Security+ |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Official Docker image, run on your own machine only

```bash
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
