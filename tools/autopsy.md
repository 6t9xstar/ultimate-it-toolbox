# Autopsy

> Autopsy is a digital-forensics platform and graphical front end for The Sleuth Kit, used to examine disk images, file systems, and deleted files.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://www.autopsy.com/> |
| Licence | `Apache License 2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id SleuthKit.Autopsy --exact
choco install autopsy
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `autopsy`.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
