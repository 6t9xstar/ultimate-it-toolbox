# Tor Browser

> Tor Browser is designed for anonymous web browsing, utilizing the Tor network to protect user privacy and security.

## Overview

| Property | Value |
|---|---|
| Category | Browsers |
| Official website | <https://www.torproject.org/> |
| Licence | `MPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id TorProject.TorBrowser --exact
choco install tor-browser
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `tor`.

---

[← Browsers](../14-browser-tools/) · [All categories](../README.md)
