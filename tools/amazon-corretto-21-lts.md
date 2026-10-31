# Amazon Corretto 21 (LTS)

> Amazon Corretto is a no-cost, multiplatform, production-ready distribution of the Open Java Development Kit (OpenJDK).

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://aws.amazon.com/corretto> |
| Licence | `GPL-2.0 with Classpath Exception` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Amazon.Corretto.21.JDK --exact
choco install corretto21jdk
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `java21`.

---

[← Software Development](../04-development/) · [All tools](../tools/) · [All categories](../README.md)
