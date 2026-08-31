# first-capability — the smallest Orreth capability

One folder, one file, zero code in the machine's path. This is the working
example behind [Build your first capability](https://docs.orreth.ai/build/first-capability/);
the walk it teaches was run live before the page was written.

```bash
# from a running Orreth checkout (see the quickstart):
cp -r examples/first-capability <orreth>/capabilities/hello
scripts/dev.sh replant     # → "⚑ capability discovered: hello (hello)"
# a 👋 Hello World tile appears in the console's Capabilities portal;
# the hello-greeting prompt is on the governed shelf, human-editable.

rm -r <orreth>/capabilities/hello
scripts/dev.sh replant
# the tile REMAINS, honestly marked state=declared, genesis absent —
# the shelf remembers what the folder forgets. Retire it via its tile.
```

`genesis.py` exports exactly two names: `CRAFT` (the words, planted on the
governed shelf) and `MANIFEST` (the card the console renders blind). The
contract, field by field: the
[manifest reference](https://docs.orreth.ai/reference/capability-manifest/).
