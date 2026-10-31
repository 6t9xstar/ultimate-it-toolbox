# Security Policy

This repository is a directory: Markdown files and data describing third-party tools, plus a small set of standard-library Python scripts that generate and check them. It hosts no third-party software, so the risk surface is the accuracy of what it tells you to install.

## What to report

Please report:

- **A wrong package id** — an entry whose `winget` or `choco` id installs something other than the tool described. This is the highest-severity issue here: a wrong id can install the wrong software, and the [bundles](bundles/) can install it alongside a dozen others.
- **A hijacked or abandoned project** — an entry pointing at a tool whose upstream has been taken over, renamed, or is distributing something it did not previously.
- **A malicious or typosquatted package** reachable from an entry.
- **A link that now resolves somewhere unexpected** — expired domains get re-registered.
- **A command on a card that does something other than install the tool**, such as a piped install script whose host has changed hands.

## How to report

Contact the maintainer through [apexsofteck.com](https://apexsofteck.com). Please do not open a public issue for a malicious or hijacked package until it has been dealt with.

For anything involving a malicious package, please also report it to the package repository itself ([winget-pkgs](https://github.com/microsoft/winget-pkgs/issues) or the Chocolatey community feed), so every consumer gets the fix and not just this directory.

## What the directory does to catch problems

- Every pull request runs [`validate.py`](.build/validate.py), which rejects malformed ids, duplicate ids and non-https links.
- A [weekly workflow](.github/workflows/upstream-health.yml) confirms every winget id still exists in `microsoft/winget-pkgs` and every official website still resolves, and flags sites that now redirect to a different domain.

These checks prove an id *exists*. They cannot prove the package behind it is still trustworthy; a human report is how that gets caught.

## What this directory does not do

- It does not host, mirror, repackage or modify any software.
- It does not bypass licensing or activation for any product.
- It does not vouch for the security of the tools it lists. Each entry records the licence and the official source so you can make your own assessment. Read a bundle before you run it, and verify signatures and checksums yourself before installing anything.

## Security tooling

Some categories list offensive security and network testing tools. They are listed for authorised testing, defensive work and certification study.

Using them against systems you do not own, or do not have written permission to test, is likely illegal in your jurisdiction. Practise against intentionally vulnerable targets such as [OWASP Juice Shop](tools/owasp-juice-shop.md) or [DVWA](tools/dvwa.md), or your own lab.
