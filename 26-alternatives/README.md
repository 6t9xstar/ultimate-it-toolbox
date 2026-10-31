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
| Adobe Acrobat | [PDF24 Creator](../tools/pdf24-creator.md), [Stirling-PDF](../tools/stirling-pdf.md) | Merging, splitting, converting and printing to PDF; Stirling-PDF does it as a self-hosted web app for a whole team. Neither is a full prepress or forms tool. |
| Autodesk AutoCAD | [LibreCAD](../tools/librecad.md), [FreeCAD](../tools/freecad.md) | LibreCAD for 2D drafting, FreeCAD for parametric 3D. Expect DWG fidelity issues; prefer DXF. |
| SolidWorks / Fusion 360 | [FreeCAD](../tools/freecad.md) | Genuine parametric modelling with no subscription. Less polished, smaller add-on ecosystem. |
| Esri ArcGIS | [QGIS](../tools/qgis.md) | A complete desktop GIS, widely used in research and government. |
| Unity / Unreal | [Godot Engine](../tools/godot-engine.md) | No royalties and a small footprint. Weaker for AAA 3D pipelines and console export. |
| 3ds Max / Maya | [Blender](../tools/blender-3d-graphics.md) | Modelling, sculpting, animation and rendering in one package. |

## Office and knowledge

| Instead of | Try | Trade-off |
|---|---|---|
| Microsoft Office | [LibreOffice](../tools/libreoffice.md), [ONLYOFFICE](../tools/onlyoffice-desktop.md) | ONLYOFFICE keeps OOXML layout more faithfully; LibreOffice has deeper features. Complex macros and some formatting still drift. |
| Notion | [Obsidian](../tools/obsidian.md), [Logseq](../tools/logseq.md), [AppFlowy](../tools/appflowy.md), [SiYuan](../tools/siyuan.md) | Obsidian and Logseq are local Markdown files you own, but you lose databases and multi-user editing. AppFlowy is the closest to Notion's model, with databases and self-hostable sync. |
| Confluence | [BookStack](../tools/bookstack.md), [Wiki.js](../tools/wiki-js.md), [Docmost](../tools/docmost.md), [DokuWiki](../tools/dokuwiki.md) | Self-hosted team wikis. BookStack's shelves-and-books structure suits IT runbooks; DokuWiki needs no database at all. No Jira-style integration. |
| Microsoft Visio / Lucidchart | [draw.io Desktop](../tools/draw-io-desktop.md) | Offline network and architecture diagrams with AWS, Azure and Cisco shape sets. Imports some Visio files; complex stencils may not survive. |
| 1Password / LastPass | [KeePassXC](../tools/keepassxc.md), [Bitwarden](../tools/bitwarden.md) + [Vaultwarden](../tools/vaultwarden.md), [Passbolt](../tools/passbolt.md) | Bitwarden if you want hosted sync, or point its clients at your own Vaultwarden; Passbolt for team sharing; KeePassXC for a local file and no service at all. |

## Developer and API

| Instead of | Try | Trade-off |
|---|---|---|
| Postman | [Bruno](../tools/bruno.md), [Yaak](../tools/yaak.md), [Hoppscotch](../tools/hoppscotch.md), [Insomnia](../tools/insomnia.md) | Bruno and Yaak store collections as files in your repo, so they version properly and need no account. Hoppscotch can be self-hosted for a team. |
| Charles / Fiddler | [mitmproxy](../tools/mitmproxy.md) | Scriptable HTTPS interception in Python. No polished GUI composer. |
| GitHub / GitLab.com | [Gitea](../tools/gitea.md), [Forgejo](../tools/forgejo.md), [GitLab CE](../tools/gitlab-community-edition.md) | Self-hosted Git with pull requests and CI. Gitea and Forgejo run on a Raspberry Pi; GitLab CE is far heavier but complete. |
| SonarCloud | [SonarQube Community Build](../tools/sonarqube-community-build.md) | The same analysers, self-hosted. No branch or pull-request analysis in the free build. |
| Docker Hub / Artifactory (for images) | [Harbor](../tools/harbor.md) | A private registry with scanning, signing and replication. You run the storage. |
| HashiCorp Terraform | [OpenTofu](../tools/opentofu.md) | A drop-in MPL-licensed fork under the Linux Foundation, created after Terraform moved to BUSL. Existing configurations and providers work. |
| HashiCorp Vault | [OpenBao](../tools/openbao.md) | The MPL-licensed Vault fork, API-compatible with Vault's open-source feature set. Some enterprise features have no equivalent. |
| Redis | [Valkey](../tools/valkey.md) | A BSD-licensed Linux Foundation fork of Redis 7.2 and a drop-in replacement. On Windows, use [Memurai](../tools/memurai-developer.md) or WSL. |
| Zapier / Make | [n8n](../tools/n8n.md) | Self-hosted workflow automation with AI-agent nodes. Source-available (fair-code), not open source — you may not resell it as a service. |
| ChatGPT / Copilot chat (local and private) | [Ollama](../tools/ollama.md) + [Open WebUI](../tools/open-webui.md), [LM Studio](../tools/lm-studio.md), [Jan](../tools/jan.md) | Your prompts never leave the machine. Open-weight models that fit consumer GPUs are capable, but behind frontier hosted models. |
| Tableau / Power BI | [Metabase](../tools/metabase.md), [Apache Superset](../tools/apache-superset.md) | Self-hosted dashboards on your own databases. Less polished modelling layers, and no desktop authoring app. |
| Docker Desktop | [Podman Desktop](../tools/podman-desktop.md), [Rancher Desktop](../tools/rancher-desktop.md), [Portainer](../tools/portainer.md) | All avoid Docker Desktop's commercial licence terms for larger companies. Podman is daemonless and rootless. |
| MATLAB | [Julia](../tools/julia.md), [R](../tools/r.md) | Julia for numerical computing at speed; R for statistics. Neither replaces Simulink. |

## Communication and collaboration

| Instead of | Try | Trade-off |
|---|---|---|
| Slack / Microsoft Teams | [Mattermost](../tools/mattermost.md), [Rocket.Chat](../tools/rocket-chat.md), [Zulip](../tools/zulip.md), [Synapse (Matrix)](../tools/synapse-matrix.md) | Self-host and keep your message history instead of renting it. Zulip's topic threads suit asynchronous teams; Matrix federates with other servers. You run the server and the upgrades. |
| Zoom / Teams meetings | [Jitsi Meet](../tools/jitsi-meet.md), [BigBlueButton](../tools/bigbluebutton.md) | Browser-based video calls you host. BigBlueButton is built for teaching; both need real bandwidth and CPU for large rooms. |
| Mailchimp | [listmonk](../tools/listmonk.md), [Mautic](../tools/mautic.md) | listmonk for newsletters, Mautic for full marketing automation. Deliverability depends on the SMTP relay you pair them with. |
| Jira | [OpenProject](../tools/openproject.md), [Redmine](../tools/redmine.md), [Plane](../tools/plane.md), [Taiga](../tools/taiga.md) | Plane is closest to modern Jira; Redmine is the most battle-tested; OpenProject adds Gantt and budgeting. |
| Trello | [Wekan](../tools/wekan.md), [Vikunja](../tools/vikunja.md), [Kanboard](../tools/kanboard.md) | Straightforward Kanban. Vikunja also does lists, tables and Gantt; Kanboard is the lightest. |

## Infrastructure and virtualization

| Instead of | Try | Trade-off |
|---|---|---|
| VMware Workstation | [Oracle VirtualBox](../tools/oracle-virtualbox.md) | Free for personal use and good enough for every certification lab in this directory. |
| VMware ESXi / vSphere | [Proxmox VE](../tools/proxmox-ve.md) | Bare-metal KVM plus LXC, with clustering and backup built in, and no licence tier to negotiate. |
| cPanel / Plesk | [HestiaCP](../tools/hestiacp.md), [CyberPanel](../tools/cyberpanel.md) | Web, mail, DNS and database management without per-account licensing. |
| Heroku | [Coolify](../tools/coolify.md), [Dokku](../tools/dokku.md), [CapRover](../tools/caprover.md) | Git-push deploys on your own server. Dokku is the leanest; Coolify has the nicest UI. |
| Google Workspace / Microsoft 365 mail | [Mailcow](../tools/mailcow.md) | Full control of your mail. Be realistic: deliverability and reputation become your problem. |
| Okta / Azure AD (as an IdP) | [Authentik](../tools/authentik.md), [Keycloak](../tools/keycloak.md), [FreeIPA](../tools/freeipa.md) | SAML and OIDC single sign-on you host. Keycloak is the enterprise-grade option; Authentik is friendlier to set up; FreeIPA covers LDAP and Kerberos for Linux fleets. |
| Tailscale (coordination server) | [Headscale](../tools/headscale.md) | Keep the official Tailscale clients but run the control plane yourself. Some newer Tailscale features lag. |
| TeamViewer / AnyDesk | [RustDesk Server](../tools/rustdesk-server.md), [MeshCentral](../tools/meshcentral.md), [Apache Guacamole](../tools/apache-guacamole.md) | Remote support that does not route through a vendor's cloud. Guacamole is clientless — RDP, VNC and SSH in a browser. |
| AWS S3 (self-hosted) | [Garage](../tools/garage.md), [SeaweedFS](../tools/seaweedfs.md), [Ceph](../tools/ceph.md) | S3-compatible storage on your own disks. Garage is the lightest; Ceph is the most capable and the most work. |
| Google Analytics | [Matomo](../tools/matomo.md), [Plausible CE](../tools/plausible-community-edition.md), [Umami](../tools/umami.md) | Analytics data stays on your server, and Plausible and Umami set no cookies. You lose Google Ads integration. |
| Bitly | [Shlink](../tools/shlink.md), [YOURLS](../tools/yourls.md) | Short links on your own domain, with click stats. |

## Networking and monitoring

| Instead of | Try | Trade-off |
|---|---|---|
| Cisco ASA / FortiGate | [pfSense](../tools/pfsense.md), [OPNsense](../tools/opnsense.md) | Capable firewalling, VPN and traffic shaping on commodity hardware. No vendor TAC to call. |
| SolarWinds NPM | [LibreNMS](../tools/librenms.md), [Zabbix](../tools/zabbix-server.md), [Nagios Core](../tools/nagios-core.md) | LibreNMS auto-discovers via SNMP with the least setup effort. |
| Datadog / New Relic | [Prometheus](../tools/prometheus.md) + Grafana, [Netdata](../tools/netdata.md) | Netdata gives per-second metrics with almost no configuration; Prometheus is the long-term standard. |
| Splunk | [Wazuh](../tools/wazuh.md), [OpenSearch](../tools/opensearch.md), [Elasticsearch](../tools/elasticsearch.md), [Graylog](../tools/graylog.md) | All handle centralised logging and search; Wazuh adds SIEM rules and agents out of the box. Graylog Open is SSPL, which is not OSI open source — see the caution below. |
| Datadog APM / New Relic tracing | [OpenTelemetry Collector](../tools/opentelemetry-collector.md) + [Jaeger](../tools/jaeger.md) | Vendor-neutral instrumentation and tracing. You assemble and run the pipeline yourself. |
| Tenable Nessus | [Greenbone / OpenVAS](../tools/greenbone-openvas.md) | The main open-source vulnerability scanner. Feed updates are slower than commercial ones. |
| IDA Pro | [Ghidra](../tools/ghidra.md) | A genuinely competitive decompiler, free from the NSA. Different workflow and a Java UI. |

## Storage and backup

| Instead of | Try | Trade-off |
|---|---|---|
| Dropbox / Google Drive sync | [Syncthing](../tools/syncthing-cli-web-ui.md), [Rclone](../tools/rclone.md) | Syncthing is peer-to-peer with no server and no quota; Rclone talks to 70+ providers from the CLI. |
| Backblaze / CrashPlan | [restic](../tools/restic.md), [BorgBackup](../tools/borgbackup.md), [KopiaUI](../tools/kopiaui.md), [Duplicati](../tools/duplicati.md) | Encrypted, deduplicating backups to storage you choose. You own the retention policy and the restore testing. |
| Veeam Backup & Replication | [Proxmox Backup Server](../tools/proxmox-backup-server.md), [UrBackup Server](../tools/urbackup-server.md), [Bareos](../tools/bareos.md) | Centralised backup of VMs and machines. Proxmox Backup Server is strongest with Proxmox VE; Bareos handles tape. |
| Dropbox / Google Drive (hosted) | [Nextcloud Server](../tools/nextcloud-server.md), [Seafile](../tools/seafile.md) | Self-hosted sync and share. Nextcloud does far more (calendars, office); Seafile syncs large libraries faster. |
| Symantec Ghost | [Clonezilla](../tools/clonezilla.md) | Bare-metal imaging and mass deployment from a live USB. |
| Total Commander | [Double Commander](../tools/double-commander.md) | Dual-pane file management, tabs, batch rename and archive handling, with no nag screen. |

## A caution on "open source"

Several projects here have changed licence, and the direction is not always away from open source:

- **Moved away:** Terraform, Vault, Consul, Nomad and Packer (BUSL-1.1); Graylog Open (SSPL); TheHive 5 (proprietary, with a free Community licence). Where an open fork exists it is listed above: [OpenTofu](../tools/opentofu.md), [OpenBao](../tools/openbao.md).
- **Came back:** Elasticsearch added **AGPL-3.0** as an option alongside SSPL and the Elastic License in 2024 (8.16 onward), so it is OSI open source again if you take the AGPL. [OpenSearch](../tools/opensearch.md), the Apache-2.0 fork, remains the permissive choice.
- **Forked away from a change:** Redis left BSD in 2024; [Valkey](../tools/valkey.md) continues under BSD-3-Clause.
- **Never open source:** n8n's Sustainable Use License and Outline's BSL are source-available. Free to self-host for your own use, but not open source.

Each card records the actual licence string so you can check rather than assume.

---

[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)
