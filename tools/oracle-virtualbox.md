# Oracle VirtualBox

> Oracle VirtualBox is a powerful and free open-source virtualization tool for x86 and AMD64/Intel64 architectures.

## Overview

| Property | Value |
|---|---|
| Category | Virtualization |
| Official website | <https://www.virtualbox.org/> |
| Licence | `GPL-3.0-only` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Oracle.VirtualBox --exact
choco install virtualbox
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `OVirtualBox`.

---

[← Virtualization](../09-virtualization/) · [All categories](../README.md)
