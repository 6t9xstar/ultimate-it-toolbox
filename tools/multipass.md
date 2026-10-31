# Multipass

> Multipass launches and manages lightweight Ubuntu VMs from a single command, using Hyper-V or VirtualBox underneath on Windows.

## Overview

| Property | Value |
|---|---|
| Category | Virtualization & Storage |
| Official website | <https://canonical.com/multipass> |
| Licence | `GPL-3.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | LFCS |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Canonical.Multipass --exact
choco install multipass
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Virtualization & Storage](../09-virtualization/) · [All tools](../tools/) · [All categories](../README.md)
