# WhatsApp Desktop

> WhatsApp Desktop is the official Windows desktop messaging app from Meta, distributed through the Microsoft Store.

## Overview

| Property | Value |
|---|---|
| Category | Communication |
| Official website | <https://www.whatsapp.com/download> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id 9NKSQGP7F2NH --source msstore --exact
```

_No Chocolatey package is published for this tool; use winget._

## Verification

**Tier: package-verified.**

- Microsoft Store product id confirmed with `winget show --source msstore` on 2026-10-31.
- Store listings publish terms of service rather than a licence id, so the licence is recorded as the listing describes it.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `whatsapp`.

---

[← Communication](../15-communication/) · [All tools](../tools/) · [All categories](../README.md)
