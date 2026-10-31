# AWS Session Manager Plugin

> The Session Manager plugin lets the AWS CLI open shell sessions and port forwards to EC2 instances through Systems Manager, without opening SSH ports.

## Overview

| Property | Value |
|---|---|
| Category | Cloud Computing |
| Official website | <https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html> |
| Licence | `Apache-2.0` |
| Source model | Open source |
| Platform | Windows (packaged) |
| Certification relevance | AWS |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## Install on Windows

```powershell
winget install --id Amazon.SessionManagerPlugin --exact
choco install awscli-session-manager
```

## Verification

**Tier: package-verified.**

- Package id confirmed against the live `winget` source on 2026-10-31.
- Licence string copied from the package manifest, not inferred.

---

[← Cloud Computing](../05-cloud-computing/) · [All tools](../tools/) · [All categories](../README.md)
