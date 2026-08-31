---
title: "Quickstart: a running world in ten minutes"
description: Clone the repository, start the development rig, and walk into a live governed universe through its console.
---

This gets you from nothing to a **running Orreth world with a console in
your browser** — three connected instances of the engine (a universe, a
zone under it, and a workroom under that), which is how a real deployment
is shaped. It is the honest version of a quickstart: today you run Orreth
from its repository with one script. If you only want the bare engine and
your own topology, [Build your first world](/build/first-world/) does it
from a published image, no clone needed.

## What you need

- **Docker Desktop**, running. The kernel ships as containers; the first
  start compiles the Rust kernel inside the build, which takes a few minutes
  once and is fast after.
- **[uv](https://docs.astral.sh/uv/)** — the Python runner. The agentic layer
  (identity, residents, cognition) runs host-side through it; it manages its
  own Python, so you don't need to.
- **git**, and about 5 GB of free disk for images.
- macOS or Linux. (One optional extra — a helper that auto-restarts the
  stack after crashes or reboots — is macOS-only; everything else is not.)

## 1. Clone and start

```bash
git clone https://github.com/iotlodge/orreth.git
cd orreth
scripts/dev.sh start
```

One command does all of this, in order:

1. Mints (or reuses) the universe's **root keypair** and hands the *public*
   half to the containers — the kernel can verify everything and sign
   nothing.
2. Builds and starts the spine: **three containers of the same kernel
   binary**, each wearing a different JSON profile — the universe (port
   4500), an ecosystem under it (4501), a floor under that (4502) — chained
   parent to child.
3. Starts the agentic layer on your host: the process that holds the keys,
   answers join requests, and gives the built-in staff their minds.
4. Prints the honest inventory (you can re-run it any time with
   `scripts/dev.sh status`).

You should see the three spine containers up, three healthy doors, and:

```
join door: OPEN (:4502) — agents may join
```

## 2. Open the console

```bash
scripts/dev.sh window
```

This seeds a small demonstration biography (so the world isn't empty on your
first look) and opens the console — or just browse to
[http://localhost:4500/window](http://localhost:4500/window) yourself.

Your first five minutes, in order:

1. **The welcome band** at the top gives you the five things to know. Words
   with a dotted underline open the machine's own dictionary — the same
   definitions as this site's [glossary](/learn/glossary/).
2. **The left rail is the world.** Every name is a floor you can step onto;
   what you see is always one floor's own records, fetched through the same
   governed doors any agent uses.
3. **The Inbox** is everything waiting on *your* decision. Orreth stops and
   waits at gates — silence never approves, so this is where the machine
   queues for you.
4. **Objectives** is where you ask for work in your own words. A plan comes
   back for your approval before anything runs.

## 3. Give it a mind (optional but recommended)

Without model keys, everything structural works — records, identity, gates,
the console — and anything that needs to *think* refuses honestly instead of
pretending. To let the residents think, put at least one key in a `.env` file
at the repository root:

```bash
# .env — read by the agentic layer at start; keys live in this file and the
# process environment only, never in any record (that is a tested law)
ANTHROPIC_API_KEY=sk-ant-...
# optional additions:
OPENROUTER_API_KEY=...   # widens the model market
TAVILY_API_KEY=...       # lets the librarian search the web
```

Then `scripts/dev.sh restart`. Every model call is authorized and metered by
the kernel — you can watch the running bill per identity in the console — but
prompt content never passes through it.

## 4. Stop, and what survives

```bash
scripts/dev.sh stop     # the whole rig rests; your word holds until `start`
```

Stopping is honest too: the containers stop, but the universe's memory lives
in a Postgres volume and every record is content-addressed on disk — `start`
brings the same world back, same identities, same history. Nothing is
re-seeded behind your back.

## Where to go next

- [The anatomy of a running world](/learn/anatomy/) — what you just started,
  body by body.
- [What works today](/learn/what-works-today/) — what of this is proven, and
  what isn't yet.
- [Build your first world](/build/first-world/) — a brand-new two-tier
  universe from three small files against the published kernel image, no
  clone required.
- **Build your first capability** is the next page in this track — it ships
  together with the SDK's publication.
