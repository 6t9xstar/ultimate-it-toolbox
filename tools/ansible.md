# Ansible

> Ansible is the agentless automation tool the current RHCE exam is built around. The control node is Linux-only, so run it from a lab VM or WSL.

## Overview

| Property | Value |
|---|---|
| Category | DevOps, Containers & IaC |
| Official website | <https://www.redhat.com/en/ansible-collaborative> |
| Licence | `GPL-3.0` |
| Source model | Open source |
| Platform | Linux / WSL |
| Certification relevance | RHCE |
| Rating | Not yet rated — see [RATINGS.md](../RATINGS.md) |
| Last verified | 2026-10-31 |

## How to get it

pip install ansible  or  dnf install ansible-core

See the official site for current instructions — deployment steps change more often than this directory does.

## Verification

**Tier: upstream-documented.**

- Official URL confirmed to resolve on 2026-10-31.
- Licence and install route are as documented upstream, **not** machine-verified the way a package id can be. Check the project's own licence file before relying on it commercially.
- Not installable through WinUtil Pro: this is not a Windows package.

---

[← DevOps, Containers & IaC](../06-devops/) · [All tools](../tools/) · [All categories](../README.md)
