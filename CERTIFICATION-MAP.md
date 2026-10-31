# Certification Map

Find tools by what you are studying for, rather than by category.

Each section lists what you can install today and — where the honest answer is a virtual machine, WSL or a vendor account — says so instead of pretending a package exists.

> [!IMPORTANT]
> This map covers **Windows-installable** tooling, because that is what the verified seed data covers. Several certifications are examined on Linux. Where that is the case, the entry says what the Windows side can realistically give you and what has to run in a VM.

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

**Get elsewhere:**

- **RHEL** — free for personal use via the [Red Hat Developer Subscription](https://developers.redhat.com/products/rhel/download). [Rocky Linux](https://rockylinux.org/) and [AlmaLinux](https://almalinux.org/) are binary-compatible and free.
- **SELinux, LVM, systemd, firewalld, Cockpit** — these *are* the Linux OS. You practise them inside the VM. There is no Windows package and there should not be one.

---

## RHCE

**Red Hat Certified Engineer.** Automation-focused: in current form, Ansible.

| Tool | Why it matters |
|---|---|
| [OpenShift Client (oc)](tools/openshift-client-oc.md) | Red Hat's Kubernetes/OpenShift CLI. |
| [Podman](tools/podman.md) · [Podman Desktop](tools/podman-desktop.md) | Container workflows on the Red Hat stack. |
| [Oracle VirtualBox](tools/oracle-virtualbox.md) · [Vagrant](tools/vagrant.md) | Multi-node lab: you need several managed hosts. |
| [VS Code](tools/vs-code.md) | Writing playbooks and roles, with YAML tooling. |

**Get elsewhere:**

- **Ansible** — Python-based and Linux-first. Run it from a control node in your lab, or from **WSL** on this machine. There is no supported native Windows control node.

---

## CCNA

**Cisco Certified Network Associate.** The headline lab tools are **not packaged** for winget or Chocolatey, so they are not listed as entries here. That is a deliberate choice: an entry that installs nothing is worse than no entry.

**Get elsewhere:**

- **Cisco Packet Tracer** — free, but only through a [Cisco Networking Academy](https://www.netacad.com/) account. No public package exists.
- **GNS3** — [gns3.com/software/download](https://www.gns3.com/software/download); ships its own installer.
- **EVE-NG** — a virtual appliance you import into a hypervisor.
- **Cisco IOS images** — licensed by Cisco. Obtain them through your own entitlement or NetAcad.

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
| **CySA+** | [Sysinternals Sysmon](tools/sysinternals-sysmon.md), [osquery](tools/osquery.md), [Velociraptor](tools/velociraptor.md), [Wazuh Agent](tools/wazuh-agent.md), [Suricata](tools/suricata.md), [YARA](tools/yara.md), [Trivy](tools/trivy.md), [Splunk Universal Forwarder](tools/splunk-universal-forwarder.md), [Winlogbeat](tools/winlogbeat.md), [Autopsy](tools/autopsy.md), [Volatility Workbench](tools/volatility-workbench.md), [HxD](tools/hxd-hex-editor.md) |

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

**Get elsewhere:** Metasploit, Ghidra, hashcat, John the Ripper, sqlmap, Nikto and Hydra have **no Windows package**. Run them inside a Kali VM or WSL — which is also how the OSCP exam environment works.

---

[All categories](README.md) · [Rating system](RATINGS.md) · [Contribute](CONTRIBUTING.md)
