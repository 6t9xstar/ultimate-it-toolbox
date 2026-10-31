# virt-manager

> virt-manager is a desktop GUI for creating and managing KVM/QEMU virtual machines through libvirt.

## Overview

| Property | Value |
|---|---|
| Category | Virtualization & Storage |
| Official website | <https://virt-manager.org/> |
| Licence | `GPL-2.0` |
| Source model | Open source |
| Platform | Linux |
| Certification relevance | RHCSA, LFCS |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

Distribution package on a host with KVM

```bash
sudo dnf install virt-manager libvirt   # RHEL / Fedora
```

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← Virtualization & Storage](../09-virtualization/) · [All tools](../tools/) · [All categories](../README.md)
