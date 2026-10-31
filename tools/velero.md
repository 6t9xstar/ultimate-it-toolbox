# Velero

> Velero backs up and restores Kubernetes resources and persistent volumes, and migrates them between clusters.

## Overview

| Property | Value |
|---|---|
| Category | Backup & Recovery |
| Official website | <https://velero.io/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Kubernetes |
| Certification relevance | CKA |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

velero CLI plus an in-cluster install pointing at object storage

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Backup & Recovery](../18-backup-recovery/) · [All tools](../tools/) · [All categories](../README.md)
