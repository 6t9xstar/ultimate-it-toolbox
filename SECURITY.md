# Security Policy

This repository is documentation: Markdown files describing third-party tools. It ships no executable code, so the risk surface is the accuracy of what it tells you to install.

## What to report

Please report:

- **A wrong package id** — an entry whose `winget` or `choco` id installs something other than the tool described. This is the highest-severity issue here: a wrong id can install the wrong software.
- **A hijacked or abandoned project** — an entry pointing at a tool whose upstream has been taken over, renamed, or is distributing something it did not previously.
- **A malicious or typosquatted package** reachable from an entry.
- **A link that now resolves somewhere unexpected** — expired domains get re-registered.

## How to report

Contact the maintainer through [apexsofteck.com](https://apexsofteck.com).

For anything involving a malicious package, please also report it to the package repository itself ([winget-pkgs](https://github.com/microsoft/winget-pkgs/issues) or the Chocolatey community feed), so every consumer gets the fix and not just this directory.

## What this directory does not do

- It does not host, mirror, repackage or modify any software.
- It does not bypass licensing or activation for any product.
- It does not vouch for the security of the tools it lists. Each entry records the licence and the official source so you can make your own assessment. Verify signatures and checksums yourself before installing anything.

## Security tooling

Some categories list offensive security and network testing tools. They are listed for authorised testing, defensive work and certification study.

Using them against systems you do not own, or do not have written permission to test, is likely illegal in your jurisdiction. Practise against intentionally vulnerable targets or your own lab.
