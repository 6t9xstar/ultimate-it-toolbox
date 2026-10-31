# Display Driver Uninstaller

> Display Driver Uninstaller (DDU) is a tool for completely uninstalling graphics drivers from NVIDIA, AMD, and Intel. It is useful for troubleshooting graphics driver-related issues.

## Overview

| Property | Value |
|---|---|
| Category | Hardware, IoT & Electronics |
| Official website | <https://www.wagnardsoft.com/display-driver-uninstaller-DDU-> |
| Licence | `MIT` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-30 |

## Install on Windows

```powershell
winget install --id Wagnardsoft.DisplayDriverUninstaller --exact
choco install ddu
```

## Verification

- Package id confirmed against the live `winget` source on 2026-10-30.
- Licence string is copied from the package manifest, not inferred.
- Also installable from [WinUtil Pro](https://github.com/6t9xstar/winutil-pro)'s Install tab as `ddu`.

---

[← Hardware, IoT & Electronics](../12-hardware-iot-robotics/) · [All categories](../README.md)
