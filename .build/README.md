# Build data and tooling

Everything generated in this repository comes from the four data files here. Edit these, then run the generator — never edit the generated Markdown.

| File | What it is |
|---|---|
| [`packages.json`](packages.json) | Tier 1: Windows packages with verified winget and Chocolatey ids |
| [`nonwindows.json`](nonwindows.json) | Tier 2: Linux, Kubernetes, appliance and self-hosted tools |
| [`ratings.json`](ratings.json) | Applied ratings, each with a reason and evidence |
| [`bundles.json`](bundles.json) | Certification and role bundles (category bundles are added automatically) |

| Script | What it does |
|---|---|
| `generate.py` | Writes `tools/`, the category indexes, `bundles/`, `data/` and the counters in the root documents. `--check` writes nothing and fails if anything is stale. |
| `validate.py` | Checks the data against the rules in [CONTRIBUTING.md](../CONTRIBUTING.md). |
| `checklinks.py` | Checks every relative link and anchor in the repository's Markdown. |
| `checkurls.py` | Checks every official website still resolves (network; run weekly in CI). |
| `checkwinget.py` | Checks every winget id still exists in a `microsoft/winget-pkgs` checkout (run weekly in CI). |

All scripts use only the Python 3 standard library.

```bash
python .build/validate.py && python .build/generate.py && python .build/checklinks.py .
```
