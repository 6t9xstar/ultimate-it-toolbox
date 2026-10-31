# Mattermost

> Mattermost is an open-source, self-hostable team messaging platform. This installs the desktop client, which needs a Mattermost server to connect to.

## Overview

| Property | Value |
|---|---|
| Category | Communication |
| Official website | <https://mattermost.com/apps/> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Mattermost.MattermostDesktop --exact
choco install mattermost-desktop
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `mattermost`.

---

[← Communication](../15-communication/) · [All tools](../tools/) · [All categories](../README.md)
