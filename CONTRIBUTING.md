# Contributing

Thanks for helping. This directory has one rule that matters more than all the others:

> **Verify it, or do not add it.**

A tool list is only worth reading if its entries are true. An unverified package id is worse than a missing entry, because `winget install` on a bad id can fail silently and the reader believes it worked.

## Adding a tool

1. **Check it is not already here.** Search `tools/` — each tool has exactly one card, linked from however many categories apply.
2. **Verify the package.**
   ```powershell
   winget show --id Publisher.Package --exact
   ```
   This confirms the id resolves and prints the publisher, homepage and licence. If it returns nothing, the id is wrong.
3. **Verify the Chocolatey id separately**, if you are adding one:
   ```powershell
   choco search package-id --exact
   ```
   No result means there is no such package. Write that the tool is winget-only rather than inventing a name.
4. **Copy the card format** from [TOOL-TEMPLATE.md](TOOL-TEMPLATE.md) into `tools/<slug>.md`.
5. **Link it** from the relevant category `README.md` table.
6. **Open a pull request** describing what you verified and when.

## What gets rejected

- An entry whose package id does not resolve.
- A licence written as "Free", "Open source" or "Freeware" when the manifest states an actual licence.
- A description pasted from the vendor's marketing page or from another awesome-list. Write your own; most lists carry no licence permitting reuse.
- A rating with no justification — see [RATINGS.md](RATINGS.md).
- A link to a download aggregator, mirror, or any "crack", keygen, pre-activated build or licence-bypass tool. These are out of scope permanently, not pending review.
- Duplicate cards for one tool.

## The highest-value contributions

The verified seed data covers Windows packages. The gaps are the opportunity:

| Gap | What is needed |
|---|---|
| **Linux-native tools** | RHEL/Fedora tooling, Cockpit, Ansible, the Kali toolset. Give the real install route (`dnf`, `apt`, upstream repo) instead of a winget id. |
| **Self-hosted software** | pfSense, OPNsense, Proxmox, Mailcow, Coolify, Authentik. Record the deployment method (ISO, Docker, Helm). |
| **Categories 24 and 26** | Project management, and open-source/self-hosted alternatives — both currently empty. |
| **Ratings** | Pick a subcategory you know well and rate it properly, with reasons. |
| **Certification coverage** | Extend [CERTIFICATION-MAP.md](CERTIFICATION-MAP.md) with tracks you have actually sat. |

For a non-Windows tool, adjust the card's `Platform` row and replace the install block with that platform's real command. Keep the verification section: say how you confirmed the package exists.

## Style

- British or American spelling is fine; be consistent inside a file.
- One sentence per description. Say what it does, not why it is amazing.
- Prefer the publisher's own name for the tool, capitalised as they capitalise it.
- Keep tables narrow enough to read on GitHub without horizontal scrolling.

## Regenerating the seeded cards

The initial 389 cards were generated from verified catalogue data by `.build/generate.py`. If you are doing a bulk update from that source, run the generator. **Hand-edits to a seeded card will be overwritten by a regeneration**, so if you improve a card substantially, say so in your pull request so the change can be moved into the source data too.
