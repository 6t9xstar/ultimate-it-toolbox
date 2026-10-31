# Firefox ESR

> Mozilla Firefox is an open-source web browser known for its customization options, privacy features, and extensions. Firefox ESR (Extended Support Release) receives major updates every 42 weeks with minor updates such as crash fixes, security fixes and policy updates as needed, but at least every four weeks.

## Overview

| Property | Value |
|---|---|
| Category | Browsers |
| Official website | <https://www.mozilla.org/en-US/firefox/enterprise/> |
| Licence | `MPL-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Mozilla.Firefox.ESR --exact
choco install FirefoxESR
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `firefoxesr`.

---

[← Browsers](../14-browser-tools/) · [All tools](../tools/) · [All categories](../README.md)
