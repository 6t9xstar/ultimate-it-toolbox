# Install Bundles

Each bundle is a standard [`winget import`](https://learn.microsoft.com/windows/package-manager/winget/import) file listing package-verified tools from this directory. One command installs the whole set; winget skips anything already installed.

```powershell
# From a clone of this repository
winget import -i bundles\ccna.winget.json --accept-package-agreements --accept-source-agreements

# Or straight from GitHub, without cloning
irm https://raw.githubusercontent.com/6t9xstar/ultimate-it-toolbox/main/bundles/ccna.winget.json -OutFile ccna.winget.json
winget import -i ccna.winget.json --accept-package-agreements --accept-source-agreements
```

> [!TIP]
> Read the bundle before you run it. Every id in it links to a card below, so you can see the licence and publisher of each tool first. Remove lines you do not want — the file is plain JSON.

Only `winget`-source packages are bundled. Microsoft Store apps and upstream-documented tools (Linux, appliances, self-hosted) cannot be installed this way; where a track depends on them, they are listed under *Also needed* with a link to the card that explains how to get them.

## Certification tracks

| Bundle | For | Packages | File |
|---|---|---|---|
| [RHCSA lab](#rhcsa-lab) | The Windows side of a Red Hat Certified System Administrator lab: hypervisor, SSH, editor and container CLI. | 9 | [`rhcsa.winget.json`](rhcsa.winget.json) |
| [RHCE lab](#rhce-lab) | Red Hat Certified Engineer: a multi-node lab plus the tools to write and run Ansible. | 9 | [`rhce.winget.json`](rhce.winget.json) |
| [LFCS lab](#lfcs-lab) | Linux Foundation Certified Sysadmin: Linux VMs, WSL and the container/orchestration CLIs. | 11 | [`lfcs.winget.json`](lfcs.winget.json) |
| [CCNA lab](#ccna-lab) | Cisco Certified Network Associate: capture, scan, TFTP, console access and diagramming. | 11 | [`ccna.winget.json`](ccna.winget.json) |
| [CCNP lab](#ccnp-lab) | Everything in CCNA plus the Python, Git and editor toolchain for network automation. | 13 | [`ccnp.winget.json`](ccnp.winget.json) |
| [CompTIA A+](#comptia-a) | Hardware diagnostics, imaging, cleanup and data recovery for desktop support. | 12 | [`comptia-a-plus.winget.json`](comptia-a-plus.winget.json) |
| [CompTIA Network+](#comptia-network) | Capture, scanning, throughput, path analysis and the everyday network utilities. | 10 | [`comptia-network-plus.winget.json`](comptia-network-plus.winget.json) |
| [CompTIA Security+](#comptia-security) | Encryption, password management, sandboxing, host firewalling and vulnerability scanning. | 12 | [`comptia-security-plus.winget.json`](comptia-security-plus.winget.json) |
| [CompTIA CySA+](#comptia-cysa) | Blue-team analysis on Windows: telemetry, detection, triage and forensics. | 15 | [`comptia-cysa-plus.winget.json`](comptia-cysa-plus.winget.json) |
| [OSCP and PenTest+](#oscp-and-pentest) | The Windows-side web and reversing tools; the rest of the toolset lives in a Kali VM. Authorised targets only. | 10 | [`oscp.winget.json`](oscp.winget.json) |
| [Kubernetes: CKA, CKAD, CKS](#kubernetes-cka-ckad-cks) | kubectl, local clusters and the productivity and security tooling around them. | 16 | [`kubernetes.winget.json`](kubernetes.winget.json) |
| [AWS](#aws) | AWS Solutions Architect and Developer tracks: the CLIs and infrastructure-as-code. | 9 | [`aws.winget.json`](aws.winget.json) |
| [Microsoft Azure](#microsoft-azure) | Azure Administrator and Developer tracks: CLIs, Bicep, storage tooling and Functions. | 9 | [`azure.winget.json`](azure.winget.json) |
| [Google Cloud](#google-cloud) | Associate Cloud Engineer and related tracks. | 5 | [`google-cloud.winget.json`](google-cloud.winget.json) |
| [HashiCorp Terraform Associate](#hashicorp-terraform-associate) | Terraform and its open-source fork, plus the cloud CLIs that provide credentials. | 9 | [`terraform-associate.winget.json`](terraform-associate.winget.json) |

## Role kits

| Bundle | For | Packages | File |
|---|---|---|---|
| [Windows sysadmin essentials](#windows-sysadmin-essentials) | The everyday kit for administering Windows machines. | 12 | [`kit-sysadmin.winget.json`](kit-sysadmin.winget.json) |
| [Developer workstation](#developer-workstation) | Editor, runtimes, Git and the API and database clients most projects need. | 14 | [`kit-developer.winget.json`](kit-developer.winget.json) |
| [Modern command line](#modern-command-line) | Faster, friendlier replacements for the classic Unix utilities, all native on Windows. | 18 | [`kit-modern-cli.winget.json`](kit-modern-cli.winget.json) |
| [DevOps workstation](#devops-workstation) | Kubernetes, GitOps, infrastructure-as-code and container tooling. | 16 | [`kit-devops.winget.json`](kit-devops.winget.json) |
| [Blue-team analyst](#blue-team-analyst) | Capture, endpoint telemetry, triage, reversing and forensics. | 13 | [`kit-blue-team.winget.json`](kit-blue-team.winget.json) |
| [Data science](#data-science) | Python and R environments, notebooks, publishing and a local database engine. | 10 | [`kit-data-science.winget.json`](kit-data-science.winget.json) |
| [Local AI](#local-ai) | Run and inspect open-weight language models on your own hardware. | 6 | [`kit-local-ai.winget.json`](kit-local-ai.winget.json) |

## Whole categories

| Bundle | For | Packages | File |
|---|---|---|---|
| [Operating Systems & System Administration](../01-operating-systems/) | Every winget package in [Operating Systems & System Administration](../01-operating-systems/). | 55 | [`category-operating-systems.winget.json`](category-operating-systems.winget.json) |
| [Networking](../02-networking/) | Every winget package in [Networking](../02-networking/). | 12 | [`category-networking.winget.json`](category-networking.winget.json) |
| [Cybersecurity](../03-cybersecurity/) | Every winget package in [Cybersecurity](../03-cybersecurity/). | 26 | [`category-cybersecurity.winget.json`](category-cybersecurity.winget.json) |
| [Software Development](../04-development/) | Every winget package in [Software Development](../04-development/). | 63 | [`category-development.winget.json`](category-development.winget.json) |
| [Cloud Computing](../05-cloud-computing/) | Every winget package in [Cloud Computing](../05-cloud-computing/). | 18 | [`category-cloud-computing.winget.json`](category-cloud-computing.winget.json) |
| [DevOps, Containers & IaC](../06-devops/) | Every winget package in [DevOps, Containers & IaC](../06-devops/). | 45 | [`category-devops.winget.json`](category-devops.winget.json) |
| [Databases & Data Engineering](../07-databases/) | Every winget package in [Databases & Data Engineering](../07-databases/). | 26 | [`category-databases.winget.json`](category-databases.winget.json) |
| [AI, Machine Learning & Data Science](../08-ai-ml-data/) | Every winget package in [AI, Machine Learning & Data Science](../08-ai-ml-data/). | 13 | [`category-ai-ml-data.winget.json`](category-ai-ml-data.winget.json) |
| [Virtualization & Storage](../09-virtualization/) | Every winget package in [Virtualization & Storage](../09-virtualization/). | 7 | [`category-virtualization.winget.json`](category-virtualization.winget.json) |
| [Web Infrastructure](../10-web-infrastructure/) | Every winget package in [Web Infrastructure](../10-web-infrastructure/). | 3 | [`category-web-infrastructure.winget.json`](category-web-infrastructure.winget.json) |
| [Quality Assurance & Testing](../11-quality-assurance/) | Every winget package in [Quality Assurance & Testing](../11-quality-assurance/). | 10 | [`category-quality-assurance.winget.json`](category-quality-assurance.winget.json) |
| [Hardware, IoT & Electronics](../12-hardware-iot-robotics/) | Every winget package in [Hardware, IoT & Electronics](../12-hardware-iot-robotics/). | 13 | [`category-hardware-iot-robotics.winget.json`](category-hardware-iot-robotics.winget.json) |
| [Design & Engineering](../13-design-engineering/) | Every winget package in [Design & Engineering](../13-design-engineering/). | 35 | [`category-design-engineering.winget.json`](category-design-engineering.winget.json) |
| [Browsers](../14-browser-tools/) | Every winget package in [Browsers](../14-browser-tools/). | 19 | [`category-browser-tools.winget.json`](category-browser-tools.winget.json) |
| [Communication](../15-communication/) | Every winget package in [Communication](../15-communication/). | 20 | [`category-communication.winget.json`](category-communication.winget.json) |
| [Productivity & Office](../16-productivity/) | Every winget package in [Productivity & Office](../16-productivity/). | 17 | [`category-productivity.winget.json`](category-productivity.winget.json) |
| [File Management](../17-file-management/) | Every winget package in [File Management](../17-file-management/). | 19 | [`category-file-management.winget.json`](category-file-management.winget.json) |
| [Backup & Recovery](../18-backup-recovery/) | Every winget package in [Backup & Recovery](../18-backup-recovery/). | 13 | [`category-backup-recovery.winget.json`](category-backup-recovery.winget.json) |
| [Remote Access](../19-remote-access/) | Every winget package in [Remote Access](../19-remote-access/). | 12 | [`category-remote-access.winget.json`](category-remote-access.winget.json) |
| [Terminal & CLI](../20-terminal-cli/) | Every winget package in [Terminal & CLI](../20-terminal-cli/). | 31 | [`category-terminal-cli.winget.json`](category-terminal-cli.winget.json) |
| [Documentation & Knowledge](../21-documentation/) | Every winget package in [Documentation & Knowledge](../21-documentation/). | 18 | [`category-documentation.winget.json`](category-documentation.winget.json) |
| [Privacy & Personal Security](../23-privacy-security/) | Every winget package in [Privacy & Personal Security](../23-privacy-security/). | 17 | [`category-privacy-security.winget.json`](category-privacy-security.winget.json) |
| [Gaming](../27-gaming/) | Every winget package in [Gaming](../27-gaming/). | 17 | [`category-gaming.winget.json`](category-gaming.winget.json) |

## Contents

### RHCSA lab

The Windows side of a Red Hat Certified System Administrator lab: hypervisor, SSH, editor and container CLI.

[Oracle VirtualBox](../tools/oracle-virtualbox.md), [Vagrant](../tools/vagrant.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md), [Podman](../tools/podman.md), [PuTTY](../tools/putty.md), [WinSCP](../tools/winscp.md), [Neovim](../tools/neovim.md), [GNU nano](../tools/gnu-nano.md), [Windows Terminal](../tools/windows-terminal.md)

**Also needed** (not a Windows package): [Red Hat Enterprise Linux](../tools/red-hat-enterprise-linux.md), [Rocky Linux](../tools/rocky-linux.md), [AlmaLinux](../tools/almalinux.md), [CentOS Stream](../tools/centos-stream.md), [Cockpit](../tools/cockpit.md), [OpenSCAP](../tools/openscap.md), [Lynis](../tools/lynis.md), [virt-manager](../tools/virt-manager.md)

### RHCE lab

Red Hat Certified Engineer: a multi-node lab plus the tools to write and run Ansible.

[Oracle VirtualBox](../tools/oracle-virtualbox.md), [Vagrant](../tools/vagrant.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md), [VS Code](../tools/vs-code.md), [Git](../tools/git.md), [Podman](../tools/podman.md), [Podman Desktop](../tools/podman-desktop.md), [OpenShift Client (oc)](../tools/openshift-client-oc.md), [yq](../tools/yq.md)

**Also needed** (not a Windows package): [Ansible](../tools/ansible.md), [AWX](../tools/awx.md), [Semaphore UI](../tools/semaphore-ui.md), [Red Hat Enterprise Linux](../tools/red-hat-enterprise-linux.md)

### LFCS lab

Linux Foundation Certified Sysadmin: Linux VMs, WSL and the container/orchestration CLIs.

[Oracle VirtualBox](../tools/oracle-virtualbox.md), [Vagrant](../tools/vagrant.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md), [Ubuntu 24.04 LTS (WSL)](../tools/ubuntu-24-04-lts-wsl.md), [Multipass](../tools/multipass.md), [PuTTY](../tools/putty.md), [GNU nano](../tools/gnu-nano.md), [Neovim](../tools/neovim.md), [Podman](../tools/podman.md), [Kubernetes CLI (kubectl)](../tools/kubernetes-cli-kubectl.md), [Helm](../tools/helm.md)

**Also needed** (not a Windows package): [Ubuntu Server](../tools/ubuntu-server.md), [Debian](../tools/debian.md), [Rocky Linux](../tools/rocky-linux.md), [openSUSE Leap](../tools/opensuse-leap.md), [virt-manager](../tools/virt-manager.md)

### CCNA lab

Cisco Certified Network Associate: capture, scan, TFTP, console access and diagramming.

[Wireshark](../tools/wireshark.md), [Nmap](../tools/nmap.md), [tftpd64](../tools/tftpd64.md), [iPerf3](../tools/iperf3.md), [WinMTR](../tools/winmtr.md), [PuTTY](../tools/putty.md), [Termius](../tools/termius.md), [Oracle VirtualBox](../tools/oracle-virtualbox.md), [Simplewall](../tools/simplewall.md), [NetSetMan](../tools/netsetman.md), [draw.io Desktop](../tools/draw-io-desktop.md)

**Also needed** (not a Windows package): [Cisco Packet Tracer](../tools/cisco-packet-tracer.md), [GNS3](../tools/gns3.md), [EVE-NG](../tools/eve-ng.md), [Containerlab](../tools/containerlab.md), [VyOS](../tools/vyos.md), [FRRouting](../tools/frrouting.md), [pfSense](../tools/pfsense.md), [OPNsense](../tools/opnsense.md)

### CCNP lab

Everything in CCNA plus the Python, Git and editor toolchain for network automation.

[Wireshark](../tools/wireshark.md), [Nmap](../tools/nmap.md), [tftpd64](../tools/tftpd64.md), [iPerf3](../tools/iperf3.md), [WinMTR](../tools/winmtr.md), [PuTTY](../tools/putty.md), [Oracle VirtualBox](../tools/oracle-virtualbox.md), [Python3](../tools/python3.md), [uv](../tools/uv.md), [VS Code](../tools/vs-code.md), [Git](../tools/git.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md), [draw.io Desktop](../tools/draw-io-desktop.md)

**Also needed** (not a Windows package): [Netmiko](../tools/netmiko.md), [NAPALM](../tools/napalm.md), [Nornir](../tools/nornir.md), [FRRouting](../tools/frrouting.md), [Containerlab](../tools/containerlab.md), [NetBox](../tools/netbox.md), [EVE-NG](../tools/eve-ng.md), [GNS3](../tools/gns3.md)

### CompTIA A+

Hardware diagnostics, imaging, cleanup and data recovery for desktop support.

[Sysinternals Suite](../tools/sysinternals-suite.md), [HWiNFO](../tools/hwinfo.md), [CPU-Z](../tools/cpu-z.md), [GPU-Z](../tools/gpu-z.md), [Crystal Disk Info](../tools/crystal-disk-info.md), [Rufus Imager](../tools/rufus-imager.md), [Ventoy](../tools/ventoy.md), [WizTree](../tools/wiztree.md), [BleachBit](../tools/bleachbit.md), [Double Commander](../tools/double-commander.md), [TestDisk & PhotoRec](../tools/testdisk-photorec.md), [balenaEtcher](../tools/balenaetcher.md)

**Also needed** (not a Windows package): [Memtest86+](../tools/memtest86.md), [Rescuezilla](../tools/rescuezilla.md), [Clonezilla](../tools/clonezilla.md), [GParted](../tools/gparted.md)

### CompTIA Network+

Capture, scanning, throughput, path analysis and the everyday network utilities.

[Wireshark](../tools/wireshark.md), [Nmap](../tools/nmap.md), [Angry IP Scanner](../tools/angry-ip-scanner.md), [Advanced IP Scanner](../tools/advanced-ip-scanner.md), [iPerf3](../tools/iperf3.md), [WinMTR](../tools/winmtr.md), [tftpd64](../tools/tftpd64.md), [PuTTY](../tools/putty.md), [NetSetMan](../tools/netsetman.md), [curl](../tools/curl.md)

### CompTIA Security+

Encryption, password management, sandboxing, host firewalling and vulnerability scanning.

[Gpg4win](../tools/gpg4win.md), [VeraCrypt](../tools/veracrypt.md), [KeePassXC](../tools/keepassxc.md), [Bitwarden](../tools/bitwarden.md), [Cryptomator](../tools/cryptomator.md), [age](../tools/age.md), [Malwarebytes](../tools/malwarebytes.md), [Sandboxie-Plus](../tools/sandboxie-plus.md), [Simplewall](../tools/simplewall.md), [Tenable Nessus](../tools/tenable-nessus.md), [Wireshark](../tools/wireshark.md), [Nmap](../tools/nmap.md)

**Also needed** (not a Windows package): [OWASP Juice Shop](../tools/owasp-juice-shop.md), [Wazuh](../tools/wazuh.md), [step-ca](../tools/step-ca.md)

### CompTIA CySA+

Blue-team analysis on Windows: telemetry, detection, triage and forensics.

[Sysinternals Sysmon](../tools/sysinternals-sysmon.md), [Sysinternals Suite](../tools/sysinternals-suite.md), [osquery](../tools/osquery.md), [Velociraptor](../tools/velociraptor.md), [Wazuh Agent](../tools/wazuh-agent.md), [Suricata](../tools/suricata.md), [YARA](../tools/yara.md), [Trivy](../tools/trivy.md), [Grype](../tools/grype.md), [Splunk Universal Forwarder](../tools/splunk-universal-forwarder.md), [Winlogbeat](../tools/winlogbeat.md), [Autopsy](../tools/autopsy.md), [Volatility Workbench](../tools/volatility-workbench.md), [HxD Hex Editor](../tools/hxd-hex-editor.md), [Wireshark](../tools/wireshark.md)

**Also needed** (not a Windows package): [Security Onion](../tools/security-onion.md), [Wazuh](../tools/wazuh.md), [Zeek](../tools/zeek.md), [Snort](../tools/snort.md), [Greenbone / OpenVAS](../tools/greenbone-openvas.md), [TheHive](../tools/thehive.md), [MISP](../tools/misp.md), [OpenCTI](../tools/opencti.md), [Volatility 3](../tools/volatility-3.md), [Plaso](../tools/plaso.md), [CyberChef](../tools/cyberchef.md), [REMnux](../tools/remnux.md), [Atomic Red Team](../tools/atomic-red-team.md)

### OSCP and PenTest+

The Windows-side web and reversing tools; the rest of the toolset lives in a Kali VM. Authorised targets only.

[Burp Suite Community Edition](../tools/burp-suite-community-edition.md), [ZAP (Zed Attack Proxy)](../tools/zap-zed-attack-proxy.md), [mitmproxy](../tools/mitmproxy.md), [ffuf](../tools/ffuf.md), [Nmap](../tools/nmap.md), [Wireshark](../tools/wireshark.md), [x64dbg](../tools/x64dbg.md), [ImHex](../tools/imhex.md), [Maltego](../tools/maltego.md), [Oracle VirtualBox](../tools/oracle-virtualbox.md)

**Also needed** (not a Windows package): [Kali Linux](../tools/kali-linux.md), [Parrot Security OS](../tools/parrot-security-os.md), [Metasploit Framework](../tools/metasploit-framework.md), [Ghidra](../tools/ghidra.md), [sqlmap](../tools/sqlmap.md), [hashcat](../tools/hashcat.md), [John the Ripper](../tools/john-the-ripper.md), [THC Hydra](../tools/thc-hydra.md), [Nikto](../tools/nikto.md), [Gobuster](../tools/gobuster.md), [OWASP Amass](../tools/owasp-amass.md), [Nuclei](../tools/nuclei.md), [Aircrack-ng](../tools/aircrack-ng.md), [Responder](../tools/responder.md), [Impacket](../tools/impacket.md), [BloodHound](../tools/bloodhound.md), [OWASP Juice Shop](../tools/owasp-juice-shop.md), [DVWA](../tools/dvwa.md)

### Kubernetes: CKA, CKAD, CKS

kubectl, local clusters and the productivity and security tooling around them.

[Kubernetes CLI (kubectl)](../tools/kubernetes-cli-kubectl.md), [minikube](../tools/minikube.md), [kind](../tools/kind.md), [k3d](../tools/k3d.md), [Helm](../tools/helm.md), [Kustomize](../tools/kustomize.md), [kubectx](../tools/kubectx.md), [stern](../tools/stern.md), [k9s](../tools/k9s.md), [Lens](../tools/lens.md), [Rancher Desktop](../tools/rancher-desktop.md), [Podman Desktop](../tools/podman-desktop.md), [yq](../tools/yq.md), [Trivy](../tools/trivy.md), [Kubescape](../tools/kubescape.md), [cosign](../tools/cosign.md)

**Also needed** (not a Windows package): [Kubernetes](../tools/kubernetes.md), [etcd](../tools/etcd.md), [Cilium](../tools/cilium.md), [Calico](../tools/calico.md), [k3s](../tools/k3s.md), [Falco](../tools/falco.md), [kube-bench](../tools/kube-bench.md), [Kyverno](../tools/kyverno.md), [Harbor](../tools/harbor.md), [Longhorn](../tools/longhorn.md), [Velero](../tools/velero.md), [Prometheus](../tools/prometheus.md)

### AWS

AWS Solutions Architect and Developer tracks: the CLIs and infrastructure-as-code.

[AWS CLI](../tools/aws-cli.md), [AWS SAM CLI](../tools/aws-sam-cli.md), [AWS Session Manager Plugin](../tools/aws-session-manager-plugin.md), [eksctl](../tools/eksctl.md), [HashiCorp Terraform](../tools/hashicorp-terraform.md), [OpenTofu](../tools/opentofu.md), [Pulumi](../tools/pulumi.md), [Infracost](../tools/infracost.md), [jq](../tools/jq.md)

**Also needed** (not a Windows package): [AWS CDK](../tools/aws-cdk.md)

### Microsoft Azure

Azure Administrator and Developer tracks: CLIs, Bicep, storage tooling and Functions.

[Azure CLI](../tools/azure-cli.md), [PowerShell](../tools/powershell.md), [Bicep CLI](../tools/bicep-cli.md), [Azure Developer CLI](../tools/azure-developer-cli.md), [AzCopy](../tools/azcopy.md), [Azure Storage Explorer](../tools/azure-storage-explorer.md), [Azure Functions Core Tools](../tools/azure-functions-core-tools.md), [HashiCorp Terraform](../tools/hashicorp-terraform.md), [VS Code](../tools/vs-code.md)

### Google Cloud

Associate Cloud Engineer and related tracks.

[Google Cloud SDK](../tools/google-cloud-sdk.md), [Kubernetes CLI (kubectl)](../tools/kubernetes-cli-kubectl.md), [HashiCorp Terraform](../tools/hashicorp-terraform.md), [OpenTofu](../tools/opentofu.md), [jq](../tools/jq.md)

### HashiCorp Terraform Associate

Terraform and its open-source fork, plus the cloud CLIs that provide credentials.

[HashiCorp Terraform](../tools/hashicorp-terraform.md), [OpenTofu](../tools/opentofu.md), [Terragrunt](../tools/terragrunt.md), [Infracost](../tools/infracost.md), [VS Code](../tools/vs-code.md), [Git](../tools/git.md), [AWS CLI](../tools/aws-cli.md), [Azure CLI](../tools/azure-cli.md), [Google Cloud SDK](../tools/google-cloud-sdk.md)

### Windows sysadmin essentials

The everyday kit for administering Windows machines.

[PowerToys](../tools/powertoys.md), [Sysinternals Suite](../tools/sysinternals-suite.md), [Windows Terminal](../tools/windows-terminal.md), [PowerShell](../tools/powershell.md), [gsudo](../tools/gsudo.md), [7-Zip](../tools/7-zip.md), [Everything](../tools/everything.md), [TreeSize Free](../tools/treesize-free.md), [PuTTY](../tools/putty.md), [WinSCP](../tools/winscp.md), [Git](../tools/git.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md)

### Developer workstation

Editor, runtimes, Git and the API and database clients most projects need.

[Git](../tools/git.md), [GitHub CLI](../tools/github-cli.md), [VS Code](../tools/vs-code.md), [Windows Terminal](../tools/windows-terminal.md), [Windows Subsystem for Linux](../tools/windows-subsystem-for-linux.md), [NodeJS LTS](../tools/nodejs-lts.md), [Python3](../tools/python3.md), [uv](../tools/uv.md), [Podman Desktop](../tools/podman-desktop.md), [Bruno](../tools/bruno.md), [DBeaver Community](../tools/dbeaver-community.md), [jq](../tools/jq.md), [ripgrep](../tools/ripgrep.md), [fzf](../tools/fzf.md)

### Modern command line

Faster, friendlier replacements for the classic Unix utilities, all native on Windows.

[ripgrep](../tools/ripgrep.md), [fd](../tools/fd.md), [bat](../tools/bat.md), [eza](../tools/eza.md), [fzf](../tools/fzf.md), [zoxide](../tools/zoxide.md), [delta](../tools/delta.md), [Lazygit](../tools/lazygit.md), [jq](../tools/jq.md), [yq](../tools/yq.md), [xh](../tools/xh.md), [curl](../tools/curl.md), [hyperfine](../tools/hyperfine.md), [tlrc](../tools/tlrc.md), [btop4win](../tools/btop4win.md), [Fastfetch](../tools/fastfetch.md), [Starship (Shell Prompt)](../tools/starship-shell-prompt.md), [Microsoft Edit](../tools/microsoft-edit.md)

### DevOps workstation

Kubernetes, GitOps, infrastructure-as-code and container tooling.

[Git](../tools/git.md), [GitHub CLI](../tools/github-cli.md), [VS Code](../tools/vs-code.md), [Kubernetes CLI (kubectl)](../tools/kubernetes-cli-kubectl.md), [Helm](../tools/helm.md), [Kustomize](../tools/kustomize.md), [k9s](../tools/k9s.md), [kind](../tools/kind.md), [OpenTofu](../tools/opentofu.md), [Podman Desktop](../tools/podman-desktop.md), [Docker Compose](../tools/docker-compose.md), [Argo CD CLI](../tools/argo-cd-cli.md), [Flux CLI](../tools/flux-cli.md), [Task](../tools/task.md), [hadolint](../tools/hadolint.md), [Trivy](../tools/trivy.md)

### Blue-team analyst

Capture, endpoint telemetry, triage, reversing and forensics.

[Wireshark](../tools/wireshark.md), [Nmap](../tools/nmap.md), [Sysinternals Suite](../tools/sysinternals-suite.md), [Sysinternals Sysmon](../tools/sysinternals-sysmon.md), [osquery](../tools/osquery.md), [YARA](../tools/yara.md), [Autopsy](../tools/autopsy.md), [Volatility Workbench](../tools/volatility-workbench.md), [HxD Hex Editor](../tools/hxd-hex-editor.md), [ImHex](../tools/imhex.md), [x64dbg](../tools/x64dbg.md), [KeePassXC](../tools/keepassxc.md), [Gpg4win](../tools/gpg4win.md)

### Data science

Python and R environments, notebooks, publishing and a local database engine.

[Python3](../tools/python3.md), [uv](../tools/uv.md), [Miniconda](../tools/miniconda.md), [R](../tools/r.md), [RStudio Desktop](../tools/rstudio-desktop.md), [JupyterLab Desktop](../tools/jupyterlab-desktop.md), [Quarto](../tools/quarto.md), [VS Code](../tools/vs-code.md), [DuckDB CLI](../tools/duckdb-cli.md), [DBeaver Community](../tools/dbeaver-community.md)

### Local AI

Run and inspect open-weight language models on your own hardware.

[Ollama](../tools/ollama.md), [LM Studio](../tools/lm-studio.md), [Jan](../tools/jan.md), [GPT4All](../tools/gpt4all.md), [llama.cpp](../tools/llama-cpp.md), [Netron](../tools/netron.md)

**Also needed** (not a Windows package): [Open WebUI](../tools/open-webui.md), [ComfyUI](../tools/comfyui.md)

Category bundles contain every winget-source tool in that category; see the category page for the list.

---

[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)
