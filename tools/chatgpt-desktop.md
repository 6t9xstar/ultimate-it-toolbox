# ChatGPT Desktop

> The official ChatGPT desktop app for Windows, distributed through the Microsoft Store.

## Overview

| Property | Value |
|---|---|
| Category | Software Development |
| Official website | <https://chatgpt.com/download/> |
| Licence | `Proprietary` |
| Source model | Proprietary |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id 9NT1R1C2HH7J --source msstore --exact
```

_No Chocolatey package is published for this tool; use winget._

## Verification

**Tier: package-verified.**

- Microsoft Store product id confirmed with `winget show --source msstore` on 2026-10-31.
- Store listings publish terms of service rather than a licence id, so the licence is recorded as the listing describes it.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `chatgpt`.

---

[← Software Development](../04-development/) · [All tools](../tools/) · [All categories](../README.md)
