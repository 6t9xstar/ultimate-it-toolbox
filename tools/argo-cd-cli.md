# Argo CD CLI

> The argocd CLI manages Argo CD, the GitOps controller that keeps Kubernetes clusters in sync with manifests in Git.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://argo-cd.readthedocs.io/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id argoproj.argocd --exact
choco install argocd-cli
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← DevOps, Containers & IaC](../06-devops/) · [All tools](../tools/) · [All categories](../README.md)
