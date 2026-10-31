## What this changes

<!-- One or two sentences. -->

## What I verified, and when

<!-- For each new or changed tool, say how you confirmed it:
     - Windows: output of `winget show --id <id> --exact`, and `choco search <id> --exact` if you added a Chocolatey id
     - Linux / self-hosted: the official URL resolves, and where the licence and install route come from -->

## Checklist

- [ ] I edited the data in `.build/` (not the generated Markdown) and ran `python .build/generate.py`
- [ ] `python .build/validate.py` passes
- [ ] `python .build/checklinks.py .` reports 0 broken links
- [ ] Descriptions are one sentence, in my own words
- [ ] No ratings without a stated reason; no cracks, keygens or licence-bypass tools
