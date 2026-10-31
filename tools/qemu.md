# QEMU

> QEMU is a machine emulator and virtualiser that can run guests for many CPU architectures, and is the user-space half of KVM on Linux.

## Overview

| Property | Value |
|---|---|
| Category | Virtualization & Storage |
| Official website | <https://www.qemu.org/> |
| Licence | `GPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id SoftwareFreedomConservancy.QEMU --exact
choco install Qemu
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Virtualization & Storage](../09-virtualization/) · [All tools](../tools/) · [All categories](../README.md)
