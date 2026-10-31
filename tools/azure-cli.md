# Azure CLI

> The Azure CLI is Microsoft's cross-platform command-line tool for creating and managing Azure resources.

## Overview

| Property | Value |
|---|---|
| Category | Cloud Computing |
| Official website | <https://learn.microsoft.com/cli/azure/> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Microsoft.AzureCLI --exact
choco install azure-cli
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `azurecli`.

---

[← Cloud Computing](../05-cloud-computing/) · [All tools](../tools/) · [All categories](../README.md)
