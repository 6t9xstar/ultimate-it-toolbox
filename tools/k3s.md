# k3s

> k3s is a lightweight, certified Kubernetes distribution packaged as a single binary, ideal for labs, edge devices and Raspberry Pis.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://k3s.io/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Linux |
| Certification relevance | CKA, CKAD |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Official install script on a Linux host or VM

```bash
curl -sfL https://get.k3s.io | sh -
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← DevOps, Containers & IaC](../06-devops/) · [All tools](../tools/) · [All categories](../README.md)
