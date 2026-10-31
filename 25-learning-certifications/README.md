# Learning & Certifications

Tools grouped by what you are studying for, rather than by what they are.

This category has no tool cards of its own — every tool lives once in `tools/` and is referenced from the certification map and the install bundles. Go there:

## → [CERTIFICATION-MAP.md](../CERTIFICATION-MAP.md)

| Vendor / body | Tracks | One-command install |
|---|---|---|
| **Red Hat** | [RHCSA](../CERTIFICATION-MAP.md#rhcsa), [RHCE](../CERTIFICATION-MAP.md#rhce) | [`rhcsa`](../bundles/rhcsa.winget.json), [`rhce`](../bundles/rhce.winget.json) |
| **Linux Foundation** | [LFCS](../CERTIFICATION-MAP.md#lfcs) | [`lfcs`](../bundles/lfcs.winget.json) |
| **Cisco** | [CCNA](../CERTIFICATION-MAP.md#ccna), [CCNP](../CERTIFICATION-MAP.md#ccnp) | [`ccna`](../bundles/ccna.winget.json), [`ccnp`](../bundles/ccnp.winget.json) |
| **CompTIA** | [A+, Network+, Security+, CySA+, PenTest+](../CERTIFICATION-MAP.md#comptia) | [`comptia-a-plus`](../bundles/comptia-a-plus.winget.json), [`comptia-network-plus`](../bundles/comptia-network-plus.winget.json), [`comptia-security-plus`](../bundles/comptia-security-plus.winget.json), [`comptia-cysa-plus`](../bundles/comptia-cysa-plus.winget.json) |
| **CNCF** | [CKA, CKAD, CKS](../CERTIFICATION-MAP.md#kubernetes-cka-ckad-cks) | [`kubernetes`](../bundles/kubernetes.winget.json) |
| **Cloud** | [AWS, Azure, Google Cloud](../CERTIFICATION-MAP.md#cloud-aws-azure-google-cloud) | [`aws`](../bundles/aws.winget.json), [`azure`](../bundles/azure.winget.json), [`google-cloud`](../bundles/google-cloud.winget.json) |
| **HashiCorp** | [Terraform Associate](../CERTIFICATION-MAP.md#hashicorp-terraform-associate) | [`terraform-associate`](../bundles/terraform-associate.winget.json) |
| **OffSec** | [OSCP and web app testing](../CERTIFICATION-MAP.md#oscp-pentest-and-web-application-testing) | [`oscp`](../bundles/oscp.winget.json) |

See [bundles/](../bundles/) for how to run a bundle.

## The honest part

Several of these certifications are examined on Linux, and some vendor lab tools are not distributed as packages at all. The map says so per track rather than listing an install command that would not work:

- **RHCSA / RHCE / LFCS** — the exam is on Linux. The bundle covers the Windows-side lab rig (hypervisor, WSL, SSH, container CLI); the map links the distributions themselves as upstream-documented cards.
- **CCNA** — Packet Tracer needs a Cisco NetAcad account; GNS3 and EVE-NG ship their own installers. They have cards that say exactly that, and are not in any bundle.
- **OSCP** — most of the Kali toolset is Linux-only. The real answer is a Kali VM.

Every tool card shows which certification bundles include it, in its *Certification relevance* row.

## Building a lab

Whatever the track, the foundation is the same and it is all packaged:

[Oracle VirtualBox](../tools/oracle-virtualbox.md) · [Vagrant](../tools/vagrant.md) · [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md) · [Multipass](../tools/multipass.md) · [Windows Terminal](../tools/windows-terminal.md) · [PuTTY](../tools/putty.md) · [Termius](../tools/termius.md) · [WinSCP](../tools/winscp.md)

More in [Building a lab](../CERTIFICATION-MAP.md#building-a-lab).

---

[All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md) · [Install bundles](../bundles/)
