# Learning & Certifications

Tools grouped by what you are studying for, rather than by what they are.

This category has no tool cards of its own — every tool lives once in `tools/` and is referenced from the certification map. Go there:

## → [CERTIFICATION-MAP.md](../CERTIFICATION-MAP.md)

It covers:

| Vendor / body | Tracks |
|---|---|
| **Red Hat** | [RHCSA](../CERTIFICATION-MAP.md#rhcsa), [RHCE](../CERTIFICATION-MAP.md#rhce) |
| **Cisco** | [CCNA](../CERTIFICATION-MAP.md#ccna), [CCNP](../CERTIFICATION-MAP.md#ccnp) |
| **CompTIA** | [A+, Network+, Security+, CySA+](../CERTIFICATION-MAP.md#comptia) |
| **CNCF** | [CKA, CKAD, CKS](../CERTIFICATION-MAP.md#kubernetes-cka-ckad-cks) |
| **Cloud** | [AWS, Azure, Google Cloud](../CERTIFICATION-MAP.md#cloud-aws-azure-google-cloud) |
| **Linux Foundation** | [LFCS](../CERTIFICATION-MAP.md#lfcs) |
| **Offensive Security** | [OSCP and web app testing](../CERTIFICATION-MAP.md#oscp-and-web-application-testing) |

## The honest part

Several of these certifications are examined on Linux, and some vendor lab tools are not distributed as packages at all. The map says so per track rather than listing an install command that would not work:

- **RHCSA / RHCE / LFCS** — the exam is on Linux. The map covers the Windows-side lab rig (hypervisor, SSH, container CLI) and names what must run in a VM or WSL.
- **CCNA** — Packet Tracer needs a Cisco NetAcad account; GNS3 and EVE-NG ship their own installers. None has a winget package, so none is listed as a tool card.
- **OSCP** — most of the Kali toolset is Linux-only. The real answer is a Kali VM.

## Building a lab

Whatever the track, the foundation is the same and it is all packaged:

[Oracle VirtualBox](../tools/oracle-virtualbox.md) · [Vagrant](../tools/vagrant.md) · [Windows Terminal](../tools/windows-terminal.md) · [PuTTY](../tools/putty.md) · [Termius](../tools/termius.md) · [WinSCP](../tools/winscp.md)

---

[All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)
