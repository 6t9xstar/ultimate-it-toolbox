# Bazelisk

> Bazelisk is a wrapper that downloads and runs the Bazel version a project pins, so builds stay reproducible across machines.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://bazel.build/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Bazel.Bazelisk --exact
choco install bazelisk
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `bazelisk`.

---

[← Software Development](../04-development/) · [All tools](../tools/) · [All categories](../README.md)
