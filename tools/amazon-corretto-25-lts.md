# Amazon Corretto 25 (LTS)

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
winget install --id Amazon.Corretto.25.JDK --exact
choco install corretto25jdk
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `java25`.

---

[← Software Development](../04-development/) · [All categories](../README.md)
