---
title: Build your first capability
description: A complete Orreth capability is a folder with one declaration file — install it by copying it in, watch the console render it, and learn what the machine remembers when you take it away.
---

A **capability** is a whole purpose installed on top of the machine — the
[trading desks on the demo site](https://demo.orreth.ai) are capabilities.
The contract is radical in its smallness: a capability is **declarations,
never code in the machine's path**. Concretely, it is a folder containing
one file, `genesis.py`, exporting two module-level names:

- **`CRAFT`** — the words (prompts, personas) as plain strings. At boot they
  are *planted on the governed shelf*: versioned, human-editable through the
  console's edit door, never hardcoded in an agent again.
- **`MANIFEST`** — the declaration the console renders blind: the world's
  card, its law line, and its rooms as typed panels from a fixed vocabulary
  (see the [manifest reference](/reference/capability-manifest/)).

Nothing in the file runs. Agent processes (a "crew") may be *declared*, and
the machine launches them **from the genesis file only** — the shelf's
editable copy of a manifest never executes a command, so a prompt edit can
never become command injection.

This page was walked before it was written; the example lives at
[`examples/first-capability`](https://github.com/iotlodge/orreth-docs/tree/main/examples/first-capability).

## What you need

A running rig from the [quickstart](/build/quickstart/) — capabilities are
discovered by the agentic layer, so this walk happens in your Orreth
checkout. (Installing a capability from an *outside* package is a named
future seam — the trust machinery for it is designed, not built.)

## 1. The whole capability

`capabilities/hello/genesis.py`:

```python
CRAFT = {
    "hello-greeting": (
        "You are the greeter of a brand-new world. In one warm sentence, "
        "say hello and name one true thing about the universe you live in."
    ),
}

MANIFEST = {
    "key": "hello",
    "name": "Hello World",
    "emoji": "👋",
    "resident": "librarian",
    "floor": "u:demo/e:cloud/f:prod",
    "port": 4502,
    "law": "this world only says hello — a declaration the console renders; it can take no action",
    "view": [
        {"kind": "markdown", "src": "greeting"},
    ],
}
```

Three fields are mandatory — `key`, `name`, and a `view` of panels from the
canon vocabulary; a manifest that breaks the shape is **refused loudly at
discovery** and the sweep carries on without it. The `law` line renders
under the world's name: say what your world may *not* do.

## 2. Install = copy the folder in

```bash
cp -r examples/first-capability <your-orreth-checkout>/capabilities/hello
scripts/dev.sh replant     # or restart — the sweep runs at the worker's boot
```

Watch the worker's log greet it:

```
⚑ capability discovered: hello (hello)
```

Open the console's **Capabilities** portal: a fourth tile stands beside the
desks — `👋 Hello World`, fronted by the librarian, wearing its law. Its
room says `no report yet` — panels render per-record, and a world with no
records tells you so instead of decorating. The `hello-greeting` prompt is
now on the shelf, versioned, editable in the console's craft room.

## 3. Uninstall = take the folder away — and learn what remains

```bash
rm -r capabilities/hello
scripts/dev.sh replant
```

The next boot's sweep finds three capabilities, not four. But open the
portal: **the tile is still there**, now wearing `state: declared` with its
genesis honestly marked absent. This is deliberate, and it is the deepest
lesson in this walk: the folder is the trust boundary for *code*, but the
first discovery planted the world's declaration **on the shelf, and the
shelf remembers**. History is never deleted by tidying a directory. To
retire the world properly, use its tile's lifecycle door — a governed act,
recorded, reversible in the record even when it isn't in the world.

## Where this goes next

A hello card is declarations only. A *working* world adds, in the same
manifest: a **crew** (agent processes built with the
[`orreth-agent` SDK](https://pypi.org/project/orreth-agent/) —
`pip install orreth-agent`), its own **floor** for its records, **tools** it
brings to the tool registry, and **verbs** humans fire from its panels. The
trading desk does all of it in one ~200-line genesis — read it as the
worked example, with the [manifest reference](/reference/capability-manifest/)
beside it.
