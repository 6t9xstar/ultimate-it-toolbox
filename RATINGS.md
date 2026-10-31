# Rating System

## Why almost everything is "Not yet rated"

Every tool card in this directory currently reads `Not yet rated`. That is deliberate, and it is the honest state of the data.

Rating 389 tools would mean claiming to have installed, configured and compared all of them. Nobody has. A directory that labels tools "Best Overall" on the strength of search-engine popularity is worse than one that says nothing, because the label looks like evidence when it is really just traffic.

So the vocabulary below is defined and ready, and ratings get applied by people who have actually used the tool and can say why. A rating without a stated reason is not accepted — see [CONTRIBUTING.md](CONTRIBUTING.md).

## The labels

| Label | Meaning |
|---|---|
| **Best Overall** | Strongest recommendation for the intended use. At most one per subcategory. |
| **Best Free** | Best choice that costs nothing, where paid options exist. |
| **Best Open Source** | Best option carrying an OSI-approved licence. |
| **Good Alternative** | A strong second choice, or better for a specific situation. |
| **Okay / Basic** | Does the job for simple requirements; limited beyond that. |
| **Advanced** | Powerful, but with a real learning curve or a specialist scope. |
| **Enterprise** | Aimed at enterprise requirements: licensing, support, scale. |
| **Deprecated** | No longer recommended for new installations. |

## What a rating must be based on

Not popularity. Judge on:

1. **Security posture** — signed releases, CVE history, how fast issues get fixed.
2. **Maintenance** — recent releases, responsive maintainers, not archived.
3. **Performance** — resource use and speed on a realistic workload.
4. **Features** — measured against what the category actually needs.
5. **Compatibility** — current Windows versions, relevant formats and protocols.
6. **Ease of use** — how long until a newcomer is productive.

## Applying a rating

Replace the `Rating` row on the tool card and give a one-line justification:

```markdown
| Rating | **Best Open Source** — active signed releases and the only option here with full protocol coverage. |
```

## The one label that can be applied from evidence alone

`Deprecated` does not need hands-on testing. If upstream is archived, or the project states it is unmaintained, mark it and link the proof.

One seeded entry already qualifies on those grounds: the legacy Windows port of **Redis**, which Microsoft archived years ago. Its card notes that current versions need WSL or a Redis-compatible Windows server instead.
