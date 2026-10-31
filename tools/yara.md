# YARA

> YARA matches files against pattern rules to identify and classify malware families. Command-line tool.

## Overview

| Property | Value |
|---|---|
| Category | Cybersecurity |
| Official website | <https://virustotal.github.io/yara/> |
| Licence | `BSD-3-Clause` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id VirusTotal.YARA --exact
choco install yara
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `yara`.

---

[← Cybersecurity](../03-cybersecurity/) · [All tools](../tools/) · [All categories](../README.md)
