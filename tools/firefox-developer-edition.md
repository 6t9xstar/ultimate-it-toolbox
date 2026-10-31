# Firefox Developer Edition

> Firefox Developer Edition ships the browser's developer tools ahead of the stable channel, in a separate profile so it can run alongside normal Firefox.

## Overview

| Property | Value |
|---|---|
| Category | Browsers |
| Official website | <https://www.mozilla.org/firefox/developer/> |
| Licence | `MPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Mozilla.Firefox.DeveloperEdition --exact
```

_No Chocolatey package is published for this tool; use winget._

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `firefoxdev`.

---

[← Browsers](../14-browser-tools/) · [All tools](../tools/) · [All categories](../README.md)
