# Open-Source & Self-Hosted Alternatives

Replacements for proprietary and subscription software, drawn only from tools that already have a verified card in this directory.

> [!NOTE]
> "Alternative" does not mean "identical". Each row says what you actually give up or gain, because a swap that loses a feature you depend on is not a saving. Nothing here is rated — see [RATINGS.md](../RATINGS.md).

## Creative and design

| Instead of | Try | Trade-off |
|---|---|---|
| Adobe Photoshop | [GIMP](../tools/gimp-image-editor.md), [Krita](../tools/krita.md) | GIMP covers general photo editing; Krita is stronger for painting and illustration. Neither matches Photoshop's CMYK and print workflow. |
| Adobe Illustrator | [Inkscape](../tools/inkscape.md) | Full SVG vector editing. Weaker on print colour management and some typography. |
| Adobe Premiere Pro | [Kdenlive](../tools/kdenlive.md), [Shotcut](../tools/shotcut.md) | Both do multi-track NLE work. No Adobe ecosystem integration or shared-project collaboration. |
| Adobe Acrobat | [PDF24 Creator](../tools/pdf24-creator.md) | Merging, splitting, converting and printing to PDF. Not a full prepress or forms tool. |
| Autodesk AutoCAD | [LibreCAD](../tools/librecad.md), [FreeCAD](../tools/freecad.md) | LibreCAD for 2D drafting, FreeCAD for parametric 3D. Expect DWG fidelity issues; prefer DXF. |
| SolidWorks / Fusion 360 | [FreeCAD](../tools/freecad.md) | Genuine parametric modelling with no subscription. Less polished, smaller add-on ecosystem. |
| Esri ArcGIS | [QGIS](../tools/qgis.md) | A complete desktop GIS, widely used in research and government. |
| Unity / Unreal | [Godot Engine](../tools/godot-engine.md) | No royalties and a small footprint. Weaker for AAA 3D pipelines and console export. |
| 3ds Max / Maya | [Blender](../tools/blender-3d-graphics.md) | Modelling, sculpting, animation and rendering in one package. |

## Office and knowledge

| Instead of | Try | Trade-off |
|---|---|---|
| Microsoft Office | [LibreOffice](../tools/libreoffice.md), [ONLYOFFICE](../tools/onlyoffice-desktop.md) | ONLYOFFICE keeps OOXML layout more faithfully; LibreOffice has deeper features. Complex macros and some formatting still drift. |
| Notion | [Obsidian](../tools/obsidian.md), [Logseq](../tools/logseq.md) | Local Markdown files you own, so no lock-in and no outage. You lose hosted databases and real-time multi-user editing. |
| 1Password / LastPass | [KeePassXC](../tools/keepassxc.md), [Bitwarden](../tools/bitwarden.md) | Bitwarden if you want hosted sync (and it can be self-hosted); KeePassXC if you want a local file and no service at all. |

## Developer and API

| Instead of | Try | Trade-off |
|---|---|---|
| Postman | [Bruno](../tools/bruno.md), [Insomnia](../tools/insomnia.md) | Bruno stores collections as files in your repo, so they version properly and need no account. |
| HashiCorp Terraform | [OpenTofu](../tools/opentofu.md) | A drop-in MPL-licensed fork under the Linux Foundation, created after Terraform moved to BUSL. Existing configurations and providers work. |
| Docker Desktop | [Podman Desktop](../tools/podman-desktop.md), [Rancher Desktop](../tools/rancher-desktop.md), [Portainer](../tools/portainer.md) | All avoid Docker Desktop's commercial licence terms for larger companies. Podman is daemonless and rootless. |
| MATLAB | [Julia](../tools/julia.md), [R](../tools/r.md) | Julia for numerical computing at speed; R for statistics. Neither replaces Simulink. |

## Communication and collaboration

| Instead of | Try | Trade-off |
|---|---|---|
| Slack / Microsoft Teams | [Mattermost](../tools/mattermost.md), [Rocket.Chat](../tools/rocket-chat.md) | Self-host and keep your message history instead of renting it. You run the server and the upgrades. |
| Jira | [OpenProject](../tools/openproject.md), [Redmine](../tools/redmine.md), [Plane](../tools/plane.md), [Taiga](../tools/taiga.md) | Plane is closest to modern Jira; Redmine is the most battle-tested; OpenProject adds Gantt and budgeting. |
| Trello | [Wekan](../tools/wekan.md), [Vikunja](../tools/vikunja.md) | Straightforward Kanban. Vikunja also does lists, tables and Gantt. |

## Infrastructure and virtualization

| Instead of | Try | Trade-off |
|---|---|---|
| VMware Workstation | [Oracle VirtualBox](../tools/oracle-virtualbox.md) | Free for personal use and good enough for every certification lab in this directory. |
| VMware ESXi / vSphere | [Proxmox VE](../tools/proxmox-ve.md) | Bare-metal KVM plus LXC, with clustering and backup built in, and no licence tier to negotiate. |
| cPanel / Plesk | [HestiaCP](../tools/hestiacp.md), [CyberPanel](../tools/cyberpanel.md) | Web, mail, DNS and database management without per-account licensing. |
| Heroku | [Coolify](../tools/coolify.md), [Dokku](../tools/dokku.md), [CapRover](../tools/caprover.md) | Git-push deploys on your own server. Dokku is the leanest; Coolify has the nicest UI. |
| Google Workspace / Microsoft 365 mail | [Mailcow](../tools/mailcow.md) | Full control of your mail. Be realistic: deliverability and reputation become your problem. |
| Okta / Azure AD (as an IdP) | [Authentik](../tools/authentik.md), [Keycloak](../tools/keycloak.md) | SAML and OIDC single sign-on you host. Keycloak is the enterprise-grade option; Authentik is friendlier to set up. |

## Networking and monitoring

| Instead of | Try | Trade-off |
|---|---|---|
| Cisco ASA / FortiGate | [pfSense](../tools/pfsense.md), [OPNsense](../tools/opnsense.md) | Capable firewalling, VPN and traffic shaping on commodity hardware. No vendor TAC to call. |
| SolarWinds NPM | [LibreNMS](../tools/librenms.md), [Zabbix](../tools/zabbix-server.md), [Nagios Core](../tools/nagios-core.md) | LibreNMS auto-discovers via SNMP with the least setup effort. |
| Datadog / New Relic | [Prometheus](../tools/prometheus.md) + Grafana, [Netdata](../tools/netdata.md) | Netdata gives per-second metrics with almost no configuration; Prometheus is the long-term standard. |
| Splunk | [Graylog](../tools/graylog.md), [Elasticsearch](../tools/elasticsearch.md) | Both handle centralised logging and search. Note Graylog is SSPL and Elastic dual-licensed — neither is pure OSI open source any more. |
| Tenable Nessus | [Greenbone / OpenVAS](../tools/greenbone-openvas.md) | The main open-source vulnerability scanner. Feed updates are slower than commercial ones. |
| IDA Pro | [Ghidra](../tools/ghidra.md) | A genuinely competitive decompiler, free from the NSA. Different workflow and a Java UI. |

## Storage and backup

| Instead of | Try | Trade-off |
|---|---|---|
| Dropbox / Google Drive sync | [Syncthing](../tools/syncthing-cli-web-ui.md), [Rclone](../tools/rclone.md) | Syncthing is peer-to-peer with no server and no quota; Rclone talks to 70+ providers from the CLI. |
| Backblaze / CrashPlan | [restic](../tools/restic.md), [BorgBackup](../tools/borgbackup.md) | Encrypted, deduplicating backups to storage you choose. You own the retention policy and the restore testing. |
| Symantec Ghost | [Clonezilla](../tools/clonezilla.md) | Bare-metal imaging and mass deployment from a live USB. |
| Total Commander | [Double Commander](../tools/double-commander.md) | Dual-pane file management, tabs, batch rename and archive handling, with no nag screen. |

## A caution on "open source"

Two rows above carry an asterisk worth stating plainly: **Graylog (SSPL)** and **Elasticsearch (Elastic-2.0 / SSPL)** relicensed away from OSI-approved terms. They are still source-available and free for most self-hosting, but they are not open source in the strict sense, and that may matter to you commercially. Each card records the actual licence string so you can check rather than assume.

---

[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)
