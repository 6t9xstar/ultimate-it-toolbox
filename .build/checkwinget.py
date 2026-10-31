"""Confirm every winget package id still exists in the community repository.

A package id that disappears (renamed, removed, or replaced by a new
publisher) makes `winget install` fail, and the card silently starts lying.
This checks every winget-source id against a checkout of microsoft/winget-pkgs,
so it runs on any OS, including CI's Linux runners.

  git clone --depth 1 --filter=blob:none --no-checkout \
      https://github.com/microsoft/winget-pkgs.git /tmp/winget-pkgs
  python .build/checkwinget.py /tmp/winget-pkgs

Only the tree listing is read; no manifests are downloaded. Microsoft Store
product ids are not in that repository and are skipped.

On Windows you can check a single id the direct way instead:
  winget show --id <id> --exact
"""
import io, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def known_ids(repo):
    out = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", "HEAD", "manifests"],
                         check=True, capture_output=True, text=True).stdout
    ids = set()
    for path in out.splitlines():
        # manifests/<letter>/<Publisher>/<Package>[/<Sub>...]/<version>/<file>.yaml
        parts = path.split("/")
        if len(parts) >= 5 and parts[-1].endswith(".yaml"):
            ids.add(".".join(parts[2:-2]).lower())
    return ids


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ids = known_ids(sys.argv[1])
    if len(ids) < 1000:
        sys.exit("only %d ids found -- is %s a winget-pkgs checkout?" % (len(ids), sys.argv[1]))
    pk = json.load(io.open(os.path.join(HERE, "packages.json"), encoding="utf-8"))
    checked = [t for t in pk if t.get("source", "winget") == "winget"]
    missing = [t for t in checked if t["winget"].lower() not in ids]
    print("checked %d winget ids against %d in winget-pkgs (%d Store ids skipped): %d missing"
          % (len(checked), len(ids), len(pk) - len(checked), len(missing)))
    for t in missing:
        print("  MISSING %-45s %s" % (t["winget"], t["name"]))
    sys.exit(1 if missing else 0)


main()
