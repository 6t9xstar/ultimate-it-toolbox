# Docker Desktop

> Docker Desktop provides a local environment for building, running, and testing containerized applications on Windows.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://www.docker.com/products/docker-desktop/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Docker.DockerDesktop --exact
choco install docker-desktop
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `dockerdesktop`.

---

[← DevOps, Containers & IaC](../06-devops/) · [All categories](../README.md)
