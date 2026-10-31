# Helm

> Helm is the package manager for Kubernetes, using charts to define, install, and upgrade even the most complex Kubernetes applications.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://helm.sh/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Helm.Helm --exact
choco install kubernetes-helm
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `helm`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All categories](../README.md)
