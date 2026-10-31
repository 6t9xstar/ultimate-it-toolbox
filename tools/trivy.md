# Trivy

> Trivy is an open-source security scanner from Aqua that finds vulnerabilities, misconfigurations, secrets, and SBOM issues in containers, filesystems, and IaC.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://trivy.dev/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id AquaSecurity.Trivy --exact
choco install trivy
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `trivy`.

---

[← Cybersecurity](../03-cybersecurity/) · [All categories](../README.md)
