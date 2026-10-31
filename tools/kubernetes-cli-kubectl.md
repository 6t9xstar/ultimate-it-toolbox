# Kubernetes CLI (kubectl)

> kubectl is the official command-line tool for controlling Kubernetes clusters, used to deploy applications, inspect resources, and view logs.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://kubernetes.io/docs/reference/kubectl/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Kubernetes.kubectl --exact
choco install kubernetes-cli
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `kubectl`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All categories](../README.md)
