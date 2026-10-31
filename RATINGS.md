# Rating System

## Why almost everything is "Not yet rated"

Almost every tool card in this directory reads `Not yet rated`. That is deliberate, and it is the honest state of the data.

Rating <!--n:total-->759<!--/n--> tools would mean claiming to have installed, configured and compared all of them. Nobody has. A directory that labels tools "Best Overall" on the strength of search-engine popularity is worse than one that says nothing, because the label looks like evidence when it is really just traffic.

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

Ratings live in [`.build/ratings.json`](.build/ratings.json), keyed by the card's file name, so they survive regeneration. Each needs a label from the table above and a reason; `Deprecated` also needs an evidence link:

```json
"example-tool": {"label": "Best Open Source", "reason": "Active signed releases and the only option here with full protocol coverage."}
```

Run `python .build/generate.py`, and the card's `Rating` row becomes:

```markdown
| Rating | **Best Open Source** — Active signed releases and the only option here with full protocol coverage. |
```

`python .build/validate.py` rejects a label outside the vocabulary, a rating with no reason, and a `Deprecated` with no evidence.

## The one label that can be applied from evidence alone

`Deprecated` does not need hands-on testing. If upstream is archived, or the project states it is unmaintained, mark it and link the proof.

<!--n:rated-->2<!--/n--> entries carry it today:

| Tool | Why |
|---|---|
| [Redis (Windows port)](tools/redis-windows-port.md) | Microsoft archived the port, which is frozen at Redis 3.x. Use Redis under WSL, [Memurai](tools/memurai-developer.md) or [Valkey](tools/valkey.md). |
| [.NET Desktop Runtime 6](tools/net-desktop-runtime-6.md) | .NET 6 reached end of support on 12 November 2024. Install it only for an app that still needs it. |
