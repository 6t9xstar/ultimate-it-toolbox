# Certification Map

Find tools by what you are studying for, rather than by category.

Each section lists what you can install today and — where the honest answer is a virtual machine, WSL or a vendor account — says so instead of pretending a package exists.

> [!IMPORTANT]
> Entries are one of two tiers. **Package-verified** tools install on Windows with a confirmed `winget` id. **Upstream-documented** tools are Linux, BSD, appliance or self-hosted — they have a verified official URL and a real install route, but no Windows package. Several of these certifications are examined on Linux, so both tiers matter.

**Jump to:** [RHCSA](#rhcsa) · [RHCE](#rhce) · [CCNA](#ccna) · [CCNP](#ccnp) · [CompTIA](#comptia) · [Kubernetes](#kubernetes-cka-ckad-cks) · [Cloud](#cloud-aws-azure-google-cloud) · [LFCS](#lfcs) · [OSCP](#oscp-and-web-application-testing)

---

## RHCSA

**Red Hat Certified System Administrator.** Examined on Red Hat Enterprise Linux. Nothing on Windows replaces running the real OS — what you build here is the lab rig plus the container tooling, which is a genuine exam objective.

| Tool | Why it matters |
|---|---|
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Hypervisor for RHEL / Rocky / AlmaLinux lab VMs. |
| [Vagrant](tools/vagrant.md) | Script the lab: bring VMs up and tear them down repeatably. |
| [Podman](tools/podman.md) | Red Hat's container engine. **Managing containers is an RHCSA objective**, and the CLI is the same one on RHEL. |
| [PuTTY](tools/putty.md) · [Termius](tools/termius.md) · [MobaXterm](tools/mobaxterm.md) | SSH into the lab VMs. |
| [WinSCP](tools/winscp.md) | Move files over SFTP/SCP. |
| [Neovim](tools/neovim.md) | Practise the editor you will actually have in the exam. |
| [Windows Terminal](tools/windows-terminal.md) · [PowerShell](tools/powershell.md) | A decent local terminal to drive it from. |

**The Linux side** (upstream-documented cards):

| Tool | Why it matters |
|---|---|
| [Red Hat Enterprise Linux](tools/red-hat-enterprise-linux.md) | The exam OS. Free for personal use via the Developer Subscription. |
| [Rocky Linux](tools/rocky-linux.md) · [AlmaLinux](tools/almalinux.md) | Binary-compatible RHEL rebuilds, free with no subscription. |
| [Cockpit](tools/cockpit.md) | The browser-based admin console that ships with RHEL. |
| [OpenSCAP](tools/openscap.md) | Evaluates a host against CIS and STIG baselines; ships in RHEL. |
| [Lynis](tools/lynis.md) | Audits Linux hardening and explains each finding. |
| [BorgBackup](tools/borgbackup.md) | Backup practice on the Linux side. |

**SELinux, LVM, systemd and firewalld** are *part of* the OS. You practise them inside the VM — there is no package to install and there should not be one.

---

## RHCE

**Red Hat Certified Engineer.** Automation-focused: in current form, Ansible.

| Tool | Why it matters |
|---|---|
| [OpenShift Client (oc)](tools/openshift-client-oc.md) | Red Hat's Kubernetes/OpenShift CLI. |
| [Podman](tools/podman.md) · [Podman Desktop](tools/podman-desktop.md) | Container workflows on the Red Hat stack. |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) · [Vagrant](tools/vagrant.md) | Multi-node lab: you need several managed hosts. |
| [VS Code](tools/vs-code.md) | Writing playbooks and roles, with YAML tooling. |

**The automation side** (upstream-documented cards):

| Tool | Why it matters |
|---|---|
| [Ansible](tools/ansible.md) | The tool the current RHCE exam is built around. The control node is Linux-only, so run it from a lab VM or WSL. |
| [AWX](tools/awx.md) | The upstream project behind Ansible Automation Platform's UI, API and scheduling. |
| [Keycloak](tools/keycloak.md) | Red Hat's identity server, relevant once you move into platform work. |

---

## CCNA

**Cisco Certified Network Associate.** The headline lab tools are **not packaged** for winget or Chocolatey, so they are not listed as entries here. That is a deliberate choice: an entry that installs nothing is worse than no entry.

**The lab platforms** (upstream-documented cards — no winget package exists for any of them):

| Tool | How you get it |
|---|---|
| [Cisco Packet Tracer](tools/cisco-packet-tracer.md) | Free, but only through a Cisco Networking Academy account. |
| [GNS3](tools/gns3.md) | Vendor installer. Emulates real device images, so it goes beyond a simulator. |
| [EVE-NG](tools/eve-ng.md) | A virtual appliance you import into a hypervisor. |
| [Containerlab](tools/containerlab.md) | Declarative topologies from containerised routing images — the automation-friendly option. |
| [VyOS](tools/vyos.md) | A free Linux router OS; practise real routing config without vendor hardware. |
| [MikroTik RouterOS](tools/mikrotik-routeros.md) | The Cloud Hosted Router runs free in a VM with a speed cap. |
| [pfSense](tools/pfsense.md) · [OPNsense](tools/opnsense.md) | Real firewall, VPN and NAT practice on a VM. |

**Cisco IOS images** are licensed by Cisco — obtain them through your own entitlement or NetAcad.

**Install from this directory** — the parts that *are* packaged, and that you will use constantly:

| Tool | Why it matters |
|---|---|
| [tftpd64](tools/tftpd64.md) | TFTP server for moving IOS images and configs to and from devices — a classic CCNA task. Also bundles DHCP, DNS and syslog servers for lab services. |
| [Wireshark](tools/wireshark.md) | Packet capture and protocol analysis. The most transferable skill on this track. |
| [Nmap](tools/nmap.md) | Host discovery and port scanning across lab subnets. |
| [iPerf3](tools/iperf3.md) | Prove a link's real throughput. |
| [WinMTR](tools/winmtr.md) | Combined ping/traceroute with per-hop loss and latency. The troubleshooting workhorse. |
| [PuTTY](tools/putty.md) | Console (serial) and SSH access to switches and routers. |
| [Termius](tools/termius.md) | Modern SSH client with saved hosts and snippets. |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Run EVE-NG, or Linux hosts inside your topology. |
| [simplewall](tools/simplewall.md) | See and control what is talking on the wire from your own machine. |

See also the full [Networking](02-networking/) category.

---

## CCNP

Everything under CCNA still applies, plus automation. The network-automation side is Python and YAML, so use the [Software Development](04-development/) and [DevOps](06-devops/) categories — the Cisco-specific libraries (Netmiko, NAPALM, pyATS) install with `pip`, not winget, and so are not catalogued here.

---

## CompTIA

| Certification | Tools |
|---|---|
| **A+** | [Sysinternals Suite](tools/sysinternals-suite.md), [HWiNFO](tools/hwinfo.md), [CPU-Z](tools/cpu-z.md), [GPU-Z](tools/gpu-z.md), [Rufus](tools/rufus-imager.md), [Ventoy](tools/ventoy.md), [WizTree](tools/wiztree.md), [BleachBit](tools/bleachbit.md), [Double Commander](tools/double-commander.md) |
| **Network+** | [Wireshark](tools/wireshark.md), [Nmap](tools/nmap.md), [iPerf3](tools/iperf3.md), [WinMTR](tools/winmtr.md), [tftpd64](tools/tftpd64.md), [PuTTY](tools/putty.md) |
| **Security+** | [Gpg4win](tools/gpg4win.md), [VeraCrypt](tools/veracrypt.md), [KeePassXC](tools/keepassxc.md), [Bitwarden](tools/bitwarden.md), [Malwarebytes](tools/malwarebytes.md), [Sandboxie-Plus](tools/sandboxie-plus.md), [simplewall](tools/simplewall.md), [Tenable Nessus](tools/tenable-nessus.md) |
| **CySA+** (Windows) | [Sysinternals Sysmon](tools/sysinternals-sysmon.md), [osquery](tools/osquery.md), [Velociraptor](tools/velociraptor.md), [Wazuh Agent](tools/wazuh-agent.md), [Suricata](tools/suricata.md), [YARA](tools/yara.md), [Trivy](tools/trivy.md), [Splunk Universal Forwarder](tools/splunk-universal-forwarder.md), [Winlogbeat](tools/winlogbeat.md), [Autopsy](tools/autopsy.md), [Volatility Workbench](tools/volatility-workbench.md), [HxD](tools/hxd-hex-editor.md) |

### Blue-team platforms (upstream-documented)

| Tool | Role |
|---|---|
| [Security Onion](tools/security-onion.md) | A whole network security monitoring stack in one ISO: Suricata, Zeek, Elasticsearch, Kibana. |
| [Zeek](tools/zeek.md) | Turns traffic into structured logs rather than alerts. |
| [Snort](tools/snort.md) | Signature-based intrusion detection and prevention. |
| [Greenbone / OpenVAS](tools/greenbone-openvas.md) | Open-source vulnerability scanning. |
| [TheHive](tools/thehive.md) · [MISP](tools/misp.md) | Incident response case management and threat intelligence sharing. |
| [Volatility 3](tools/volatility-3.md) | Memory forensics (the Windows GUI in this directory wraps it). |
| [CyberChef](tools/cyberchef.md) | Encoding, decoding and data triage in the browser. |
| [REMnux](tools/remnux.md) | A Linux toolkit curated for malware analysis. |

---

## Kubernetes: CKA, CKAD, CKS

The best-covered track in this directory — everything you need is packaged.

| Tool | Why it matters |
|---|---|
| [Kubernetes CLI (kubectl)](tools/kubernetes-cli-kubectl.md) | The exam *is* `kubectl`. Install it first. |
| [minikube](tools/minikube.md) · [kind](tools/kind.md) | Local clusters to practise against. |
| [Helm](tools/helm.md) | Package management; needed for CKAD-style work. |
| [k9s](tools/k9s.md) | Terminal UI that makes cluster navigation much faster. |
| [Lens](tools/lens.md) | Visual cluster IDE (free for personal use). |
| [Rancher Desktop](tools/rancher-desktop.md) · [Podman Desktop](tools/podman-desktop.md) | Local runtime with a bundled Kubernetes option. |
| [Trivy](tools/trivy.md) | Image and manifest scanning — directly relevant to **CKS**. |

**Beyond the local cluster** (upstream-documented): [Kubernetes](tools/kubernetes.md) itself, [Rancher](tools/rancher.md) for multi-cluster management, [Portainer](tools/portainer.md) for a lightweight UI, and [Prometheus](tools/prometheus.md) for the monitoring objectives.

See the full [DevOps](06-devops/) category.

---

## Cloud: AWS, Azure, Google Cloud

| Certification | Tools |
|---|---|
| **AWS Solutions Architect / Developer** | [AWS CLI](tools/aws-cli.md), [AWS SAM CLI](tools/aws-sam-cli.md), [HashiCorp Terraform](tools/hashicorp-terraform.md), [OpenTofu](tools/opentofu.md), [Pulumi](tools/pulumi.md), [Terragrunt](tools/terragrunt.md), [Infracost](tools/infracost.md) |
| **Azure Administrator** | [Azure CLI](tools/azure-cli.md), [PowerShell](tools/powershell.md) |
| **Google Cloud Engineer** | [Google Cloud SDK](tools/google-cloud-sdk.md) |
| **Multi-cloud / IaC** | Terraform, OpenTofu, Pulumi, Terragrunt — see [Cloud Computing](05-cloud-computing/) |

---

## LFCS

**Linux Foundation Certified Sysadmin.** Same shape as RHCSA: the exam is on Linux, so use [VirtualBox](tools/oracle-virtualbox.md) and [Vagrant](tools/vagrant.md) for the lab and SSH in. [Podman](tools/podman.md), [kubectl](tools/kubernetes-cli-kubectl.md) and [Helm](tools/helm.md) cover the container and orchestration objectives from the Windows side.

---

## OSCP and web application testing

> [!CAUTION]
> These tools probe and attack systems. Use them only against machines you own, lab targets you have built, or systems you hold **written** authorisation to test. Practise on intentionally vulnerable targets — HackTheBox, TryHackMe, OWASP Juice Shop — not on live infrastructure.

| Tool | Why it matters |
|---|---|
| [Burp Suite Community](tools/burp-suite-community-edition.md) | The standard web-application testing proxy. |
| [ZAP](tools/zap-zed-attack-proxy.md) | Open-source web app scanner and proxy. |
| [mitmproxy](tools/mitmproxy.md) | Scriptable intercepting proxy for HTTP/2 and WebSockets. |
| [ffuf](tools/ffuf.md) | Fast content and parameter fuzzing. |
| [Nmap](tools/nmap.md) | Reconnaissance and service enumeration. |
| [x64dbg](tools/x64dbg.md) | Windows debugger for reversing and exploit work. |
| [Maltego](tools/maltego.md) | OSINT relationship mapping (Community edition needs a free account). |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) | Run Kali or Parrot OS as a VM — this is how you get the full toolset. |

**The Kali toolset** (upstream-documented cards — none has a Windows package):

| Tool | Role |
|---|---|
| [Kali Linux](tools/kali-linux.md) · [Parrot Security OS](tools/parrot-security-os.md) | The distributions that bundle everything below. Run one as a VM. |
| [Metasploit Framework](tools/metasploit-framework.md) | Exploitation and post-exploitation. |
| [Ghidra](tools/ghidra.md) | Reverse engineering with a decompiler. Runs on Windows, but ships as an archive, not a package. |
| [sqlmap](tools/sqlmap.md) | Automated SQL injection testing. |
| [hashcat](tools/hashcat.md) · [John the Ripper](tools/john-the-ripper.md) | Password auditing against recovered hashes. |
| [THC Hydra](tools/thc-hydra.md) | Network login auditing. |
| [Nikto](tools/nikto.md) | Web server misconfiguration scanning. |
| [Aircrack-ng](tools/aircrack-ng.md) | Wi-Fi security assessment. |
| [Responder](tools/responder.md) · [Impacket](tools/impacket.md) | Windows and Active Directory testing. |
| [BloodHound](tools/bloodhound.md) | Active Directory attack-path mapping — used by defenders too. |

This is also how the OSCP exam environment works: a Kali VM, not a Windows host.

---

[All categories](README.md) · [Rating system](RATINGS.md) · [Contribute](CONTRIBUTING.md)
