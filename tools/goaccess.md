# GoAccess

> GoAccess is a real-time web-log analyser that runs in the terminal or writes an HTML report, which is useful for seeing what crawlers actually request.

## Overview

| Property | Value |
|---|---|
| Category | SEO & Marketing |
| Official website | <https://goaccess.io/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Linux |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Distribution package

```bash
sudo apt install goaccess   # Debian / Ubuntu
goaccess access.log --log-format=COMBINED -o report.html
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← SEO & Marketing](../22-seo-marketing/) · [All tools](../tools/) · [All categories](../README.md)
