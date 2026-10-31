# Certification Map

Find tools by what you are studying for, rather than by category.

Each section lists what you can install today, links a one-command [bundle](bundles/) for the Windows side, and — where the honest answer is a virtual machine, WSL or a vendor account — says so instead of pretending a package exists.

> [!IMPORTANT]
> Entries are one of two tiers. **Package-verified** tools install on Windows with a confirmed `winget` id. **Upstream-documented** tools are Linux, BSD, Kubernetes, appliance or self-hosted — they have a verified official URL and a real install route, but no Windows package. Several of these certifications are examined on Linux, so both tiers matter.

**Jump to:** [RHCSA](#rhcsa) · [RHCE](#rhce) · [LFCS](#lfcs) · [CCNA](#ccna) · [CCNP](#ccnp) · [CompTIA](#comptia) · [Kubernetes](#kubernetes-cka-ckad-cks) · [Cloud](#cloud-aws-azure-google-cloud) · [Terraform](#hashicorp-terraform-associate) · [OSCP / PenTest+](#oscp-pentest-and-web-application-testing) · [Building a lab](#building-a-lab)

---

## RHCSA

**Red Hat Certified System Administrator.** Examined on Red Hat Enterprise Linux. Nothing on Windows replaces running the real OS — what you build here is the lab rig plus the container tooling, which is a genuine exam objective.

**Bundle:** [`rhcsa.winget.json`](bundles/rhcsa.winget.json)

| Tool | Why it matters |
|---|---|
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Hypervisor for RHEL / Rocky / AlmaLinux lab VMs. |
| [Vagrant](tools/vagrant.md) | Script the lab: bring VMs up and tear them down repeatably. |
| [Windows Subsystem for Linux](tools/windows-subsystem-for-linux.md) | A Linux shell on the same machine for quick practice between full VM sessions. |
| [Podman](tools/podman.md) | Red Hat's container engine. **Managing containers is an RHCSA objective**, and the CLI is the same one on RHEL. |
| [PuTTY](tools/putty.md) · [WinSCP](tools/winscp.md) | SSH into the lab VMs and move files over SFTP/SCP. |
| [Neovim](tools/neovim.md) · [GNU nano](tools/gnu-nano.md) | Practise the editors you will actually have in the exam. |
| [Windows Terminal](tools/windows-terminal.md) | A decent local terminal to drive it from. |

**The Linux side** (upstream-documented cards):

| Tool | Why it matters |
|---|---|
| [Red Hat Enterprise Linux](tools/red-hat-enterprise-linux.md) | The exam OS. Free for personal use via the Developer Subscription. |
| [Rocky Linux](tools/rocky-linux.md) · [AlmaLinux](tools/almalinux.md) | Binary-compatible RHEL rebuilds, free with no subscription. |
| [CentOS Stream](tools/centos-stream.md) | Just upstream of RHEL — a preview of the next minor release. |
| [Cockpit](tools/cockpit.md) | The browser-based admin console that ships with RHEL. |
| [virt-manager](tools/virt-manager.md) | KVM virtual machines from a RHEL host, if your lab is Linux rather than Windows. |
| [OpenSCAP](tools/openscap.md) · [Lynis](tools/lynis.md) | Evaluate and explain host hardening against CIS and STIG baselines. |
| [BorgBackup](tools/borgbackup.md) | Backup practice on the Linux side. |

**SELinux, LVM, systemd, firewalld and NFS/autofs** are *part of* the OS. You practise them inside the VM — there is no package to install and there should not be one.

---

## RHCE

**Red Hat Certified Engineer.** Automation-focused: in current form, Ansible.

**Bundle:** [`rhce.winget.json`](bundles/rhce.winget.json)

| Tool | Why it matters |
|---|---|
| [Oracle VirtualBox](tools/oracle-virtualbox.md) · [Vagrant](tools/vagrant.md) | Multi-node lab: you need a control node and several managed hosts. |
| [VS Code](tools/vs-code.md) · [Git](tools/git.md) | Writing playbooks and roles with YAML tooling, under version control. |
| [yq](tools/yq.md) | Inspect and edit YAML inventories and variables from the shell. |
| [Podman](tools/podman.md) · [Podman Desktop](tools/podman-desktop.md) | Container workflows on the Red Hat stack. |
| [OpenShift Client (oc)](tools/openshift-client-oc.md) | Red Hat's Kubernetes/OpenShift CLI, for the platform work beyond RHCE. |

**The automation side** (upstream-documented cards):

| Tool | Why it matters |
|---|---|
| [Ansible](tools/ansible.md) | The tool the current RHCE exam is built around. The control node is Linux-only, so run it from a lab VM or [WSL](tools/windows-subsystem-for-linux.md). |
| [AWX](tools/awx.md) · [Semaphore UI](tools/semaphore-ui.md) | Web front ends for scheduling and running playbooks. AWX is the upstream of Ansible Automation Platform. |
| [Keycloak](tools/keycloak.md) · [FreeIPA](tools/freeipa.md) | Red Hat's identity stack: SSO, and LDAP/Kerberos for Linux estates — common playbook targets. |

---

## LFCS

**Linux Foundation Certified Sysadmin.** Same shape as RHCSA, but distribution-neutral — the exam currently runs on Ubuntu.

**Bundle:** [`lfcs.winget.json`](bundles/lfcs.winget.json)

| Tool | Why it matters |
|---|---|
| [Ubuntu 24.04 LTS (WSL)](tools/ubuntu-24-04-lts-wsl.md) · [Multipass](tools/multipass.md) | Ubuntu in seconds: WSL for a shell, Multipass for disposable full VMs. |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) · [Vagrant](tools/vagrant.md) | Multi-VM networking and storage scenarios. |
| [Podman](tools/podman.md) · [kubectl](tools/kubernetes-cli-kubectl.md) · [Helm](tools/helm.md) | The container and orchestration objectives. |

Upstream-documented: [Ubuntu Server](tools/ubuntu-server.md), [Debian](tools/debian.md), [Rocky Linux](tools/rocky-linux.md), [openSUSE Leap](tools/opensuse-leap.md), [virt-manager](tools/virt-manager.md), [Postfix](tools/postfix.md).

---

## CCNA

**Cisco Certified Network Associate.** The headline lab platforms have **no winget package**, so they are tier-2 cards that tell you the real route. The bundle covers everything around them.

**Bundle:** [`ccna.winget.json`](bundles/ccna.winget.json)

**The lab platforms** (upstream-documented cards):

| Tool | How you get it |
|---|---|
| [Cisco Packet Tracer](tools/cisco-packet-tracer.md) | Free, but only through a Cisco Networking Academy account. |
| [GNS3](tools/gns3.md) | Vendor installer. Emulates real device images, so it goes beyond a simulator. |
| [EVE-NG](tools/eve-ng.md) | A virtual appliance you import into a hypervisor. |
| [Containerlab](tools/containerlab.md) | Declarative topologies from containerised routing images — the automation-friendly option. |
| [FRRouting](tools/frrouting.md) · [VyOS](tools/vyos.md) | Free routing stacks with an industry-style CLI: OSPF, BGP and friends without vendor images. |
| [MikroTik RouterOS](tools/mikrotik-routeros.md) | The Cloud Hosted Router runs free in a VM with a speed cap. |
| [pfSense](tools/pfsense.md) · [OPNsense](tools/opnsense.md) · [OpenWrt](tools/openwrt.md) | Real firewall, VPN, NAT and VLAN practice on a VM. |

**Cisco IOS images** are licensed by Cisco — obtain them through your own entitlement or NetAcad.

**Install from this directory** — the parts that *are* packaged, and that you will use constantly:

| Tool | Why it matters |
|---|---|
| [tftpd64](tools/tftpd64.md) | TFTP server for moving IOS images and configs to and from devices — a classic CCNA task. Also bundles DHCP, DNS and syslog servers. |
| [Wireshark](tools/wireshark.md) | Packet capture and protocol analysis. The most transferable skill on this track. |
| [Nmap](tools/nmap.md) | Host discovery and port scanning across lab subnets. |
| [iPerf3](tools/iperf3.md) | Prove a link's real throughput. |
| [WinMTR](tools/winmtr.md) | Combined ping/traceroute with per-hop loss and latency. |
| [PuTTY](tools/putty.md) · [Termius](tools/termius.md) | Console (serial) and SSH access to switches and routers. |
| [NetSetMan](tools/netsetman.md) | Switch your laptop between lab IP profiles in one click. |
| [draw.io Desktop](tools/draw-io-desktop.md) | Topology diagrams, with Cisco shape libraries. |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Run EVE-NG, or Linux hosts inside your topology. |

See also the full [Networking](02-networking/) category.

---

## CCNP

Everything under CCNA still applies, plus automation. The network-automation side is Python and YAML.

**Bundle:** [`ccnp.winget.json`](bundles/ccnp.winget.json) — the CCNA tools plus Python, uv, VS Code, Git and WSL.

| Tool | Why it matters |
|---|---|
| [Netmiko](tools/netmiko.md) | SSH automation for multi-vendor devices — the first library most engineers learn. |
| [NAPALM](tools/napalm.md) | Vendor-neutral getters and config replace/merge. |
| [Nornir](tools/nornir.md) | Run tasks concurrently across an inventory, in plain Python. |
| [NetBox](tools/netbox.md) | Source of truth for devices, IPs and cabling, feeding the automation above. |
| [Containerlab](tools/containerlab.md) · [FRRouting](tools/frrouting.md) | Disposable multi-router topologies to test the automation against. |

Cisco's own pyATS is distributed through `pip` and Cisco DevNet, and is not catalogued here.

---

## CompTIA

| Certification | Bundle | Tools |
|---|---|---|
| **A+** | [`comptia-a-plus`](bundles/comptia-a-plus.winget.json) | [Sysinternals Suite](tools/sysinternals-suite.md), [HWiNFO](tools/hwinfo.md), [CPU-Z](tools/cpu-z.md), [GPU-Z](tools/gpu-z.md), [CrystalDiskInfo](tools/crystal-disk-info.md), [Rufus](tools/rufus-imager.md), [Ventoy](tools/ventoy.md), [balenaEtcher](tools/balenaetcher.md), [WizTree](tools/wiztree.md), [BleachBit](tools/bleachbit.md), [TestDisk & PhotoRec](tools/testdisk-photorec.md); bootable: [Memtest86+](tools/memtest86.md), [Rescuezilla](tools/rescuezilla.md), [Clonezilla](tools/clonezilla.md), [GParted](tools/gparted.md) |
| **Network+** | [`comptia-network-plus`](bundles/comptia-network-plus.winget.json) | [Wireshark](tools/wireshark.md), [Nmap](tools/nmap.md), [Angry IP Scanner](tools/angry-ip-scanner.md), [iPerf3](tools/iperf3.md), [WinMTR](tools/winmtr.md), [tftpd64](tools/tftpd64.md), [PuTTY](tools/putty.md), [NetSetMan](tools/netsetman.md), [curl](tools/curl.md) |
| **Security+** | [`comptia-security-plus`](bundles/comptia-security-plus.winget.json) | [Gpg4win](tools/gpg4win.md), [VeraCrypt](tools/veracrypt.md), [Cryptomator](tools/cryptomator.md), [age](tools/age.md), [KeePassXC](tools/keepassxc.md), [Bitwarden](tools/bitwarden.md), [Malwarebytes](tools/malwarebytes.md), [Sandboxie-Plus](tools/sandboxie-plus.md), [simplewall](tools/simplewall.md), [Tenable Nessus](tools/tenable-nessus.md); self-hosted: [Wazuh](tools/wazuh.md), [step-ca](tools/step-ca.md), [OWASP Juice Shop](tools/owasp-juice-shop.md) |
| **CySA+** | [`comptia-cysa-plus`](bundles/comptia-cysa-plus.winget.json) | [Sysmon](tools/sysinternals-sysmon.md), [osquery](tools/osquery.md), [Velociraptor](tools/velociraptor.md), [Wazuh Agent](tools/wazuh-agent.md), [Suricata](tools/suricata.md), [YARA](tools/yara.md), [Trivy](tools/trivy.md), [Grype](tools/grype.md), [Splunk Universal Forwarder](tools/splunk-universal-forwarder.md), [Winlogbeat](tools/winlogbeat.md), [Autopsy](tools/autopsy.md), [Volatility Workbench](tools/volatility-workbench.md), [HxD](tools/hxd-hex-editor.md) |
| **PenTest+** | [`oscp`](bundles/oscp.winget.json) | Same toolset as [OSCP](#oscp-pentest-and-web-application-testing) below. |

### Blue-team platforms (upstream-documented)

| Tool | Role |
|---|---|
| [Security Onion](tools/security-onion.md) | A whole network security monitoring stack in one ISO: Suricata, Zeek and a search back end. |
| [Wazuh](tools/wazuh.md) | Open-source SIEM/XDR: the server side of the Wazuh Agent above. |
| [Zeek](tools/zeek.md) · [Snort](tools/snort.md) · [Arkime](tools/arkime.md) | Traffic as structured logs, signature-based detection, and full packet capture. |
| [Greenbone / OpenVAS](tools/greenbone-openvas.md) | Open-source vulnerability scanning. |
| [TheHive](tools/thehive.md) · [MISP](tools/misp.md) · [OpenCTI](tools/opencti.md) | Case management and threat intelligence. TheHive is now proprietary with a free Community licence. |
| [Volatility 3](tools/volatility-3.md) · [Plaso](tools/plaso.md) | Memory forensics and super-timelines. |
| [Atomic Red Team](tools/atomic-red-team.md) | Small ATT&CK tests that prove whether your detections fire. |
| [CyberChef](tools/cyberchef.md) · [REMnux](tools/remnux.md) | Data triage in the browser, and a Linux toolkit for malware analysis. |

---

## Kubernetes: CKA, CKAD, CKS

The best-covered track in this directory — everything on the client side is packaged.

**Bundle:** [`kubernetes.winget.json`](bundles/kubernetes.winget.json)

| Tool | Why it matters |
|---|---|
| [Kubernetes CLI (kubectl)](tools/kubernetes-cli-kubectl.md) | The exam *is* `kubectl`. Install it first. |
| [minikube](tools/minikube.md) · [kind](tools/kind.md) · [k3d](tools/k3d.md) | Local clusters to practise against; kind and k3d do multi-node in seconds. |
| [Helm](tools/helm.md) · [Kustomize](tools/kustomize.md) | Packaging and overlays — both appear in CKAD-style tasks. |
| [kubectx](tools/kubectx.md) · [k9s](tools/k9s.md) · [stern](tools/stern.md) | Fast context switching, a terminal UI and multi-pod logs. Use them to learn; the exam gives you plain kubectl. |
| [Lens](tools/lens.md) | Visual cluster IDE (free for personal use). |
| [Rancher Desktop](tools/rancher-desktop.md) · [Podman Desktop](tools/podman-desktop.md) | Local runtime with a bundled Kubernetes option. |
| [Trivy](tools/trivy.md) · [Kubescape](tools/kubescape.md) · [cosign](tools/cosign.md) | Image scanning, posture scanning and signing — directly relevant to **CKS**. |

**Inside the cluster** (upstream-documented):

| Tool | Exam relevance |
|---|---|
| [Kubernetes](tools/kubernetes.md) · [k3s](tools/k3s.md) | kubeadm clusters for CKA; k3s for a lightweight always-on lab. |
| [etcd](tools/etcd.md) | Backing up and restoring etcd is a classic **CKA** task. |
| [Cilium](tools/cilium.md) · [Calico](tools/calico.md) | CNIs that enforce NetworkPolicy — **CKA** networking and **CKS** isolation. |
| [Falco](tools/falco.md) · [kube-bench](tools/kube-bench.md) · [Kyverno](tools/kyverno.md) | Runtime detection, CIS benchmarking and admission policy — **CKS**. |
| [Harbor](tools/harbor.md) | A private registry with scanning and signing — supply-chain objectives. |
| [Longhorn](tools/longhorn.md) · [Velero](tools/velero.md) | Persistent storage and backup/restore. |
| [Prometheus](tools/prometheus.md) · [Rancher](tools/rancher.md) · [Portainer](tools/portainer.md) | Monitoring and multi-cluster management beyond the exam. |

See the full [DevOps](06-devops/) category.

---

## Cloud: AWS, Azure, Google Cloud

| Certification | Bundle | Tools |
|---|---|---|
| **AWS Solutions Architect / Developer** | [`aws`](bundles/aws.winget.json) | [AWS CLI](tools/aws-cli.md), [AWS SAM CLI](tools/aws-sam-cli.md), [Session Manager Plugin](tools/aws-session-manager-plugin.md), [eksctl](tools/eksctl.md), [AWS CDK](tools/aws-cdk.md), [Terraform](tools/hashicorp-terraform.md), [OpenTofu](tools/opentofu.md), [Pulumi](tools/pulumi.md), [Infracost](tools/infracost.md) |
| **Azure Administrator / Developer** | [`azure`](bundles/azure.winget.json) | [Azure CLI](tools/azure-cli.md), [PowerShell](tools/powershell.md), [Bicep CLI](tools/bicep-cli.md), [Azure Developer CLI](tools/azure-developer-cli.md), [AzCopy](tools/azcopy.md), [Azure Storage Explorer](tools/azure-storage-explorer.md), [Azure Functions Core Tools](tools/azure-functions-core-tools.md) |
| **Google Cloud Engineer** | [`google-cloud`](bundles/google-cloud.winget.json) | [Google Cloud SDK](tools/google-cloud-sdk.md), [kubectl](tools/kubernetes-cli-kubectl.md), [Terraform](tools/hashicorp-terraform.md) |

Every cloud provider offers a free tier or free credits; set a billing alert before your first lab.

---

## HashiCorp Terraform Associate

**Bundle:** [`terraform-associate.winget.json`](bundles/terraform-associate.winget.json)

| Tool | Why it matters |
|---|---|
| [HashiCorp Terraform](tools/hashicorp-terraform.md) | The exam's subject. BUSL-licensed since 1.6. |
| [OpenTofu](tools/opentofu.md) | The MPL-licensed fork; the same language, useful to know when an employer has standardised on it. |
| [Terragrunt](tools/terragrunt.md) · [Infracost](tools/infracost.md) | Keeping configurations DRY, and seeing what a plan costs before you apply it. |
| [AWS CLI](tools/aws-cli.md) · [Azure CLI](tools/azure-cli.md) · [Google Cloud SDK](tools/google-cloud-sdk.md) | Provider authentication for real plans. |

---

## OSCP, PenTest+ and web application testing

> [!CAUTION]
> These tools probe and attack systems. Use them only against machines you own, lab targets you have built, or systems you hold **written** authorisation to test. Practise on intentionally vulnerable targets — [OWASP Juice Shop](tools/owasp-juice-shop.md), [DVWA](tools/dvwa.md), HackTheBox, TryHackMe — not on live infrastructure.

**Bundle:** [`oscp.winget.json`](bundles/oscp.winget.json) — the Windows-side tools below.

| Tool | Why it matters |
|---|---|
| [Burp Suite Community](tools/burp-suite-community-edition.md) | The standard web-application testing proxy. |
| [ZAP](tools/zap-zed-attack-proxy.md) | Open-source web app scanner and proxy. |
| [mitmproxy](tools/mitmproxy.md) | Scriptable intercepting proxy for HTTP/2 and WebSockets. |
| [ffuf](tools/ffuf.md) | Fast content and parameter fuzzing. |
| [Nmap](tools/nmap.md) · [Wireshark](tools/wireshark.md) | Reconnaissance, service enumeration and seeing what your tools actually send. |
| [x64dbg](tools/x64dbg.md) · [ImHex](tools/imhex.md) | Windows debugging and binary inspection for reversing and exploit work. |
| [Maltego](tools/maltego.md) | OSINT relationship mapping (Community edition needs a free account). |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Run Kali or Parrot OS as a VM — this is how you get the full toolset. |

**The Kali toolset** (upstream-documented cards — none has a Windows package):

| Tool | Role |
|---|---|
| [Kali Linux](tools/kali-linux.md) · [Parrot Security OS](tools/parrot-security-os.md) | The distributions that bundle everything below. Run one as a VM. |
| [Metasploit Framework](tools/metasploit-framework.md) | Exploitation and post-exploitation. |
| [Ghidra](tools/ghidra.md) | Reverse engineering with a decompiler. Runs on Windows, but ships as an archive, not a package. |
| [Gobuster](tools/gobuster.md) · [OWASP Amass](tools/owasp-amass.md) · [Nuclei](tools/nuclei.md) | Content discovery, subdomain enumeration and template-driven vulnerability checks. |
| [sqlmap](tools/sqlmap.md) · [Nikto](tools/nikto.md) | Automated SQL injection testing and web-server misconfiguration scanning. |
| [hashcat](tools/hashcat.md) · [John the Ripper](tools/john-the-ripper.md) · [THC Hydra](tools/thc-hydra.md) | Offline password auditing and network login auditing. |
| [Aircrack-ng](tools/aircrack-ng.md) | Wi-Fi security assessment. |
| [Responder](tools/responder.md) · [Impacket](tools/impacket.md) · [BloodHound](tools/bloodhound.md) | Windows and Active Directory testing and attack-path mapping — used by defenders too. |

This is also how the OSCP exam environment works: a Kali VM, not a Windows host.

---

## Building a lab

Whatever the track, the foundation is the same:

| Need | Tools |
|---|---|
| A hypervisor | [Oracle VirtualBox](tools/oracle-virtualbox.md), [QEMU](tools/qemu.md); bare-metal [Proxmox VE](tools/proxmox-ve.md) or [XCP-ng](tools/xcp-ng.md) for an always-on lab box |
| Repeatable VMs | [Vagrant](tools/vagrant.md), [HashiCorp Packer](tools/hashicorp-packer.md), [Multipass](tools/multipass.md) |
| Linux without a VM | [Windows Subsystem for Linux](tools/windows-subsystem-for-linux.md), [Ubuntu 24.04 LTS (WSL)](tools/ubuntu-24-04-lts-wsl.md) |
| Getting in | [Windows Terminal](tools/windows-terminal.md), [PuTTY](tools/putty.md), [Termius](tools/termius.md), [WinSCP](tools/winscp.md) |
| Writing it down | [draw.io Desktop](tools/draw-io-desktop.md), [Obsidian](tools/obsidian.md), [Joplin](tools/joplin.md) |
| Bootable media | [Ventoy](tools/ventoy.md), [Rufus](tools/rufus-imager.md), [balenaEtcher](tools/balenaetcher.md) |

---

[All categories](README.md) · [Install bundles](bundles/) · [Rating system](RATINGS.md) · [Contribute](CONTRIBUTING.md)
