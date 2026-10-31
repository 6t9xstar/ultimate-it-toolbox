# Changelog

Notable changes to the directory. Dates are when the change was verified, not when it was merged.

## 2026-10-31 — Reproducible build, bundles and 277 new tools

### Added

- **123 package-verified Windows tools**, each winget id confirmed with `winget show` and each Chocolatey id with an exact-match search on 2026-10-31. Thin categories were the priority: Terminal & CLI (ripgrep, fd, bat, fzf, jq, yq, zoxide, delta, eza, WezTerm, Nushell and more), Cloud (Azure Storage Explorer, AzCopy, Bicep, azd, eksctl, doctl, OCI CLI, flyctl), Documentation (draw.io, Pandoc, Zettlr, MiKTeX, TeXstudio, AppFlowy), AI/ML (LM Studio, Jan, llama.cpp, GPT4All, RStudio, JupyterLab Desktop), Virtualization (WSL, QEMU, Multipass, Packer), DevOps (Vault, Argo CD, Flux, Kustomize, k3d, Skaffold, GitLab Runner), databases, backup, remote access and privacy.
- **154 upstream-documented tools**, each official URL HTTP-checked: Kubernetes platform pieces (etcd, Cilium, Calico, Falco, kube-bench, Kyverno, Harbor, Longhorn, Velero, k3s, Talos), self-hosted Git and CI (Gitea, Forgejo, GitLab CE, Woodpecker), network automation (Netmiko, NAPALM, Nornir, FRRouting), blue-team platforms (Wazuh, OpenCTI, Arkime, Plaso, Atomic Red Team), practice targets (OWASP Juice Shop, DVWA), web analytics (Matomo, Plausible, Umami), wikis, data platforms, licence-change forks (OpenTofu, OpenBao, Valkey, OpenSearch) and more.
- **Install bundles** (`bundles/`): `winget import` files for 15 certification tracks, 7 role kits and every category. The format was confirmed against `winget export` and a test `winget import`.
- **Machine-readable catalogue**: `data/catalog.json` and `data/catalog.csv`.
- **Search page**: `index.html`, a dependency-free browser search over the catalogue, ready for GitHub Pages.
- **Certification relevance** on package-verified cards, derived from the certification bundles.
- **New certification coverage**: LFCS expanded, Terraform Associate, PenTest+ alongside OSCP, and a *Building a lab* section.
- **CI**: every pull request validates the data, checks the generated files are current, and checks every link. A weekly job confirms every winget id still exists and every official site still resolves.
- Issue forms for suggesting a tool and correcting an entry, a pull-request template, `.gitattributes`, `.editorconfig`.

### Fixed

- `winget install --id msstore:…` on the ChatGPT Desktop and WhatsApp cards was invalid syntax. They now use `--source msstore`, and both Store ids were re-verified.
- The README's multi-package example repeated `--id`, which winget rejects. It now passes the ids as queries.
- GitHub Desktop's Chocolatey command read `choco install git;github-desktop`, which PowerShell splits into two statements. It is now `github-desktop`.
- TheHive was listed as AGPL open source. TheHive 5 is proprietary with a free Community licence; the card now says so and notes that TheHive 4 is end-of-life.
- Elasticsearch's licence now includes AGPL-3.0, an option since 8.16, and the Alternatives page no longer says it is not open source.
- curl's card records the `curl` licence and notes that its winget manifest says `Freeware`.
- 27 official-website links that were dead or redirected were updated, including BlurAutoClicker and the Visual C++ redistributables, whose old pages return 404.
- Eight seed descriptions that were marketing copy or not full sentences were rewritten.
- RATINGS.md described the Redis port as deprecated, but the card said otherwise. Ratings now live in `ratings.json` and are applied: Redis (Windows port) and .NET Desktop Runtime 6 are marked `Deprecated`, with evidence links.

### Changed

- **The build is reproducible.** The Windows package data now lives in `.build/packages.json` instead of an external file, and regenerating from it reproduced all 387 untouched original cards byte for byte. The category-guessing rules are gone; every entry names its category.
- Counts in the README, RATINGS and certification map are maintained by the generator.
- CONTRIBUTING and TOOL-TEMPLATE now describe the data-first workflow; hand-editing generated cards is rejected by CI.

## 2026-10-31 — Linux and self-hosted tools

- Added 93 upstream-documented Linux, BSD, appliance and self-hosted tools and the two-tier verification model. Filled categories 24 and 26.

## 2026-10-30 — Initial directory

- 389 package-verified Windows tools seeded from the WinUtil Pro catalogue.
