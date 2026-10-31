# DevOps, Containers & IaC

Containers, Kubernetes, GitOps, CI/CD, secrets, configuration management, infrastructure as code and observability.

**73 tools** — 45 package-verified, 28 upstream-documented.

Install the Windows tools below in one go with the [`category-devops`](../bundles/category-devops.winget.json) bundle — see [bundles](../bundles/).

| Tool | What it does | Platform | Licence |
|---|---|---|---|
| **[act](../tools/act.md)** | act lets you run your GitHub Actions workflows locally using Docker, for fast feedback without pushing to t... | Windows (packaged) | `MIT` |
| **[Ansible](../tools/ansible.md)** | Ansible is the agentless automation tool the current RHCE exam is built around | Linux / WSL | `GPL-3.0` |
| **[Argo CD CLI](../tools/argo-cd-cli.md)** | The argocd CLI manages Argo CD, the GitOps controller that keeps Kubernetes clusters in sync with manifests... | Windows (packaged) | `Apache-2.0` |
| **[AWX](../tools/awx.md)** | AWX is the upstream open-source project behind Ansible Automation Platform's web UI, API, and job scheduling | Self-hosted (Kubernetes) | `Apache-2.0` |
| **[Calico](../tools/calico.md)** | Calico is a widely used Kubernetes CNI and network-policy engine, and a common choice for kubeadm practice... | Kubernetes | `Apache-2.0` |
| **[cert-manager](../tools/cert-manager.md)** | cert-manager issues and renews TLS certificates inside Kubernetes from ACME (Let's Encrypt), Vault or priva... | Kubernetes | `Apache-2.0` |
| **[Cilium](../tools/cilium.md)** | Cilium is an eBPF-based Kubernetes CNI that provides networking, network policy, load balancing and observa... | Kubernetes | `Apache-2.0` |
| **[Docker Compose](../tools/docker-compose.md)** | Docker Compose defines and runs multi-container applications from a compose.yaml file, and this standalone... | Windows (packaged) | `Apache-2.0` |
| **[Docker Desktop](../tools/docker-desktop.md)** | Docker Desktop provides a local environment for building, running, and testing containerized applications o... | Windows (packaged) | `Proprietary` |
| **[Docker Engine](../tools/docker-engine.md)** | Docker Engine is the container runtime and daemon on Linux hosts, as distinct from Docker Desktop on a work... | Linux | `Apache-2.0` |
| **[Elasticsearch](../tools/elasticsearch.md)** | Elasticsearch is the search and analytics engine underpinning the ELK stack, widely used for log and securi... | Self-hosted | `AGPL-3.0 / SSPL-1.0 / Elastic-2.0 (your choice, since 8.16)` |
| **[etcd](../tools/etcd.md)** | etcd is the distributed key-value store that holds all Kubernetes cluster state, and backing it up and rest... | Linux | `Apache-2.0` |
| **[Flux CLI](../tools/flux-cli.md)** | The flux CLI bootstraps and manages Flux, a CNCF GitOps toolkit that reconciles Kubernetes clusters from Gi... | Windows (packaged) | `Apache-2.0` |
| **[Forgejo](../tools/forgejo.md)** | Forgejo is a community-governed fork of Gitea that provides self-hosted Git hosting, issues, pull requests... | Self-hosted | `GPL-3.0-or-later` |
| **[Gitea](../tools/gitea.md)** | Gitea is a lightweight self-hosted Git service with pull requests, issues, a package registry and Actions-c... | Self-hosted | `MIT` |
| **[GitLab Community Edition](../tools/gitlab-community-edition.md)** | GitLab CE is a self-hosted DevOps platform with Git hosting, merge requests, CI/CD pipelines, a container r... | Self-hosted | `MIT` |
| **[GitLab Runner](../tools/gitlab-runner.md)** | GitLab Runner is the agent that picks up and executes GitLab CI/CD jobs on your own machines, using shell,... | Windows (packaged) | `MIT` |
| **[Grafana Loki](../tools/grafana-loki.md)** | Loki is a log aggregation system designed to index labels rather than full log text, pairing with Grafana f... | Self-hosted | `AGPL-3.0` |
| **[Grafana OSS](../tools/grafana-oss.md)** | Grafana is an open-source platform for monitoring and observability, letting you query, visualize, and aler... | Windows (packaged) | `AGPL-3.0` |
| **[Graylog](../tools/graylog.md)** | Graylog is a centralised log management platform with parsing, search, dashboards and alerting | Self-hosted | `SSPL (Open edition)` |
| **[hadolint](../tools/hadolint.md)** | hadolint lints Dockerfiles against best practices and runs ShellCheck on the RUN instructions | Windows (packaged) | `GPL-3.0` |
| **[Harbor](../tools/harbor.md)** | Harbor is a CNCF container registry with role-based access, vulnerability scanning, image signing and repli... | Kubernetes / Docker | `Apache-2.0` |
| **[HashiCorp Consul](../tools/hashicorp-consul.md)** | Consul provides service discovery, health checking, a key/value store and a service mesh across data centres | Windows (packaged) | `BUSL-1.1` |
| **[HashiCorp Nomad](../tools/hashicorp-nomad.md)** | Nomad is a workload orchestrator that schedules containers, VMs and plain binaries across a cluster, with a... | Windows (packaged) | `BUSL-1.1` |
| **[HashiCorp Terraform](../tools/hashicorp-terraform.md)** | Terraform is an infrastructure-as-code tool that lets you define cloud and on-prem resources in declarative... | Windows (packaged) | `BUSL-1.1` |
| **[HashiCorp Vault](../tools/hashicorp-vault.md)** | Vault stores and controls access to secrets, issues dynamic credentials and certificates, and provides encr... | Windows (packaged) | `BUSL-1.1` |
| **[Helm](../tools/helm.md)** | Helm is the package manager for Kubernetes, using charts to define, install, and upgrade even the most comp... | Windows (packaged) | `Apache-2.0` |
| **[Infracost](../tools/infracost.md)** | Infracost shows the cost impact of Terraform changes before you apply them, so cloud spend is reviewed alon... | Windows (packaged) | `Apache-2.0` |
| **[Jaeger](../tools/jaeger.md)** | Jaeger is a CNCF distributed-tracing system for following requests across microservices and finding latency... | Self-hosted | `Apache-2.0` |
| **[Jellyfin Media Player](../tools/jellyfin-media-player.md)** | Jellyfin Media Player is a client application for the Jellyfin media server, providing access to your media... | Windows (packaged) | `GPL-2.0` |
| **[Jellyfin Server](../tools/jellyfin-server.md)** | Jellyfin Server is an open-source media server software, allowing you to organize and stream your media lib... | Windows (packaged) | `MIT` |
| **[k3d](../tools/k3d.md)** | k3d runs k3s Kubernetes clusters inside Docker containers, which makes it quick to create and destroy multi... | Windows (packaged) | `MIT` |
| **[k3s](../tools/k3s.md)** | k3s is a lightweight, certified Kubernetes distribution packaged as a single binary, ideal for labs, edge d... | Linux | `Apache-2.0` |
| **[k9s](../tools/k9s.md)** | k9s is a terminal UI for interacting with your Kubernetes clusters, making it easier to navigate, observe,... | Windows (packaged) | `Apache-2.0` |
| **[kind](../tools/kind.md)** | kind runs local Kubernetes clusters using Docker containers as nodes, designed primarily for testing Kubern... | Windows (packaged) | `Apache-2.0` |
| **[Kodi Media Center](../tools/kodi-media-center.md)** | Kodi is an open-source media center application that allows you to play and view most videos, music, podcas... | Windows (packaged) | `GPL-2.0-or-later` |
| **[kubectx](../tools/kubectx.md)** | kubectx switches between kubectl contexts quickly, and its companion kubens switches the default namespace | Windows (packaged) | `Apache-2.0` |
| **[Kubernetes](../tools/kubernetes.md)** | Kubernetes is the container orchestration platform the CKA, CKAD and CKS exams are set on | Self-hosted | `Apache-2.0` |
| **[Kubernetes CLI (kubectl)](../tools/kubernetes-cli-kubectl.md)** | kubectl is the official command-line tool for controlling Kubernetes clusters, used to deploy applications,... | Windows (packaged) | `Apache-2.0` |
| **[Kustomize](../tools/kustomize.md)** | Kustomize customises Kubernetes YAML through overlays and patches without templates, and is also built into... | Windows (packaged) | `Apache-2.0` |
| **[Kyverno](../tools/kyverno.md)** | Kyverno is a Kubernetes-native policy engine that validates, mutates and generates resources using policies... | Kubernetes | `Apache-2.0` |
| **[Lens](../tools/lens.md)** | Lens is a desktop IDE for Kubernetes, giving a visual view of clusters, workloads, logs, and metrics | Windows (packaged) | `Proprietary` |
| **[LocalSend](../tools/localsend.md)** | An open-source cross-platform alternative to AirDrop | Windows (packaged) | `Apache-2.0` |
| **[minikube](../tools/minikube.md)** | minikube runs a local single-node Kubernetes cluster on your machine, giving developers a simple way to try... | Windows (packaged) | `Apache-2.0` |
| **[Moonlight/GameStream Client](../tools/moonlight-gamestream-client.md)** | Moonlight/GameStream Client allows you to stream PC games to other devices over your local network | Windows (packaged) | `GPL-3.0` |
| **[NetBird](../tools/netbird.md)** | NetBird is an open-source alternative comparable to TailScale that can be connected to a self-hosted server | Windows (packaged) | `BSD-3-Clause` |
| **[Netdata](../tools/netdata.md)** | Netdata collects thousands of per-second metrics from a host and charts them in a live dashboard, with no c... | Windows (packaged) | `GPL-3.0` |
| **[Nextcloud Desktop](../tools/nextcloud-desktop.md)** | Nextcloud Desktop is the official desktop client for the Nextcloud file synchronization and sharing platform | Windows (packaged) | `GPL-2.0` |
| **[OpenBao](../tools/openbao.md)** | OpenBao is a Linux Foundation fork of HashiCorp Vault, created after Vault moved to the BUSL, for managing... | Cross-platform | `MPL-2.0` |
| **[OpenSearch](../tools/opensearch.md)** | OpenSearch is a Linux Foundation search and analytics engine forked from Elasticsearch 7.10, with OpenSearc... | Self-hosted | `Apache-2.0` |
| **[OpenShift Client (oc)](../tools/openshift-client-oc.md)** | The OpenShift client (oc) is Red Hat's command-line tool for working with OpenShift and Kubernetes clusters... | Windows (packaged) | `GPL-3.0` |
| **[OpenTelemetry Collector](../tools/opentelemetry-collector.md)** | The OpenTelemetry Collector receives, processes and exports traces, metrics and logs to any observability b... | Cross-platform | `Apache-2.0` |
| **[OpenTofu](../tools/opentofu.md)** | OpenTofu is the open-source, community-governed fork of Terraform under the Linux Foundation, compatible wi... | Windows (packaged) | `MPL-2.0` |
| **[Plex Desktop](../tools/plex-desktop.md)** | Plex Desktop for Windows is the front end for Plex Media Server | Windows (packaged) | `Freemium AND GPL-2.0` |
| **[Plex Media Server](../tools/plex-media-server.md)** | Plex Media Server is a media server software that allows you to organize and stream your media library | Windows (packaged) | `Freemium` |
| **[Podman](../tools/podman.md)** | Podman is Red Hat's daemonless, rootless container engine with a Docker-compatible CLI | Windows (packaged) | `Apache-2.0` |
| **[Podman Desktop](../tools/podman-desktop.md)** | Podman Desktop is a graphical tool for managing containers, images, pods, and local Kubernetes clusters wit... | Windows (packaged) | `Apache License 2.0` |
| **[Portainer](../tools/portainer.md)** | Portainer is a lightweight web UI for managing Docker and Kubernetes environments, popular in home labs | Self-hosted | `Zlib (CE)` |
| **[Prometheus](../tools/prometheus.md)** | Prometheus is the de facto open-source metrics and alerting system, scraping time-series data from instrume... | Self-hosted | `Apache-2.0` |
| **[Pulumi](../tools/pulumi.md)** | Pulumi is an infrastructure-as-code platform that lets you define cloud resources using general-purpose lan... | Windows (packaged) | `Apache-2.0` |
| **[Rancher](../tools/rancher.md)** | Rancher manages multiple Kubernetes clusters from one control plane, with centralised authentication and po... | Self-hosted | `Apache-2.0` |
| **[Rancher Desktop](../tools/rancher-desktop.md)** | Rancher Desktop runs containers and a local Kubernetes cluster on your desktop, with a choice of container... | Windows (packaged) | `Apache-2.0` |
| **[Semaphore UI](../tools/semaphore-ui.md)** | Semaphore UI is a web interface for running Ansible playbooks, Terraform and OpenTofu, with scheduling, inv... | Self-hosted | `MIT` |
| **[Skaffold](../tools/skaffold.md)** | Skaffold automates the build-push-deploy loop for Kubernetes applications during local development and in CI | Windows (packaged) | `Apache-2.0` |
| **[stern](../tools/stern.md)** | stern tails logs from multiple Kubernetes pods and containers at once, matched by a name pattern or label s... | Windows (packaged) | `Apache-2.0 license` |
| **[Sunshine/GameStream Server](../tools/sunshine-gamestream-server.md)** | Sunshine is a GameStream server that allows you to remotely play PC games on Android devices, offering low-... | Windows (packaged) | `GPL-3.0` |
| **[Syncthing (CLI / Web UI)](../tools/syncthing-cli-web-ui.md)** | Syncthing is a decentralized, peer-to-peer file synchronization tool that securely syncs files directly acr... | Windows (packaged) | `MPL-2.0` |
| **[SyncTrayzor](../tools/synctrayzor.md)** | SyncTrayzor is a Windows tray utility that bundles and wraps Syncthing, making it behave like a native appl... | Windows (packaged) | `MIT` |
| **[Talos Linux](../tools/talos-linux.md)** | Talos Linux is an immutable, API-managed operating system built only to run Kubernetes, with no SSH or shell | Appliance | `MPL-2.0` |
| **[Task](../tools/task.md)** | Task is a cross-platform task runner and build tool that reads a YAML Taskfile, as a simpler alternative to... | Windows (packaged) | `MIT` |
| **[Terragrunt](../tools/terragrunt.md)** | Terragrunt is a thin wrapper around Terraform and OpenTofu that keeps configurations DRY and manages remote... | Windows (packaged) | `MIT` |
| **[Uptime Kuma](../tools/uptime-kuma.md)** | Uptime Kuma is a self-hosted uptime monitor with status pages and a wide range of notification channels | Self-hosted | `MIT` |
| **[Woodpecker CI](../tools/woodpecker-ci.md)** | Woodpecker is a lightweight, container-based CI engine that integrates with Gitea, Forgejo, GitHub and GitLab | Self-hosted | `Apache-2.0` |

---

[All tools](../tools/) · [All categories](../README.md) · [Certification map](../CERTIFICATION-MAP.md)
