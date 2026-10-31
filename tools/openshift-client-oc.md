# OpenShift Client (oc)

> The OpenShift client (oc) is Red Hat's command-line tool for working with OpenShift and Kubernetes clusters, extending kubectl with OpenShift-specific commands.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://mirror.openshift.com/pub/openshift-v4/clients/ocp/> |
| Licence | `GPL-3.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id RedHat.OpenShift-Client --exact
choco install openshift-cli
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `openshiftcli`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All tools](../tools/) · [All categories](../README.md)
