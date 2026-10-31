# BloodHound

> BloodHound maps Active Directory attack paths as a graph, used by both red teams and the AD administrators hardening against them.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://bloodhound.specterops.io/> |
| Licence | `GPL-3.0 (CE)` |
| Source model | Open source |
| Platform | Self-hosted / Windows collector |
| Certification relevance | OSCP, CRTP |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Docker Compose for the server; collectors run on the domain

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
