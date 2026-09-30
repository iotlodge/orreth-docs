---
title: Run it from the repository
description: The kernel's own development rig — the two kernels, the crew, cells, the tests, and the laws the rig keeps — from one script.
---

The published image is the way to *use* Orreth. To read it, change it, run its proofs, or stand
a second universe, run it from the repository. One script, `scripts/dev.sh`, is the whole rig.

## What you need

- Docker Desktop, running.
- **Rust** (stable toolchain) — the kernel is a release build of `backend/plane/crates/orreth-spine`.
- **[uv](https://docs.astral.sh/uv/)** — the Python runner for the reference and the bodies.
- macOS or Linux, arm64 or amd64 (the *image* is arm64 only; the tree builds on both).

## The rig in five words

```bash
git clone https://github.com/iotlodge/orreth.git && cd orreth
scripts/dev.sh up          # the rig rises: ground · invoke · events · gateway (Docker)
scripts/dev.sh kernel      # orrethd on :4600, a release build, the crew as its processes
open http://127.0.0.1:4600 # the glass: the one chat and THE PANEL
scripts/dev.sh status      # what is lit
scripts/dev.sh kernel stop # everything down whole, nothing left running
```

`scripts/dev.sh walk` is `up` + `kernel` in one word. The first `kernel` compiles the Rust
workspace, which takes a few minutes once. Provider keys ride in from your shell or a `.env` at
the root — a key value lives in no record and no file of Orreth's.

The rig's ports never collide with the first-world compose file's: the ground is on **5433**,
RabbitMQ on **5672** (its console on 15672, user `orreth`), Kafka on **9092**, the gateway on
**4604**, the kernel on **4600**, the reference on **4601**, cells from **4602** up.

## Two kernels, one law

```bash
scripts/dev.sh reference        # the Python reference on :4601 — the same ground, the same page
scripts/dev.sh reference stop
```

The reference is the same kernel written first, and the yardstick: every wire contract is a
language-neutral fixture under `spine/conformance/` that both kernels pass unchanged. Lit beside
the Rust kernel it seats no crew (the kernel's own bodies already hold the benches); lit alone it
seats the crew in-process. The reference grows no new doors — the desk, the seat, cells and the
levers were built once, on the Rust kernel, with the fixture as their contract.

## The crew as processes

```bash
.venv/bin/python3 -m orreth_spine.body --template templates/echo-resident.v0.json
.venv/bin/python3 -m orreth_spine.body --template templates/workspace-firmware.v0.json --binding bindings/crew.v0.json
```

(from `spine/`, after `uv sync`). This is exactly what the kernel runs ten times at light: one
body per seat of `crew.v0.json`. A body joins as the same self every life (its seed under
`~/.orreth/agents/<name>/`), keeps its lease while it serves, streams its words to the kernel that
spawned it, and stops whole on SIGINT. The dials: `SPINE_BODIES` (crew · none), `SPINE_CREW`
(another manifest), `SPINE_PYTHON` (another interpreter).

## A second universe

```bash
scripts/dev.sh cell two                                   # u:two on its own database and role, benches and topics, seeds and door (:4602)
scripts/dev.sh kernel stop
SPINE_PEERS=two=http://127.0.0.1:4602 scripts/dev.sh kernel   # the first cell names its peer
scripts/dev.sh cell two stop
```

A cell is one universe's physical home — its own kernel self, database *and role* (a role that
reaches no other database), its own benches and topics, bodies and keys. Two cells that name each
other speak over the signed seam; in the chat, **librarian@two, what is the weather?** routes home
and is answered here. The MONITOR pull's PEERS view says "cell two · u:two · live", "3 s behind",
or "unreachable since".

## The proofs

```bash
scripts/dev.sh rust        # the Rust workspace, hermetic — no rig needed (the conformance runner: 730 cases)
scripts/dev.sh suite       # the Python reference's laws on the rig (kernel and reference dark first)
scripts/dev.sh rust rails  # the Rust rail proofs on the rig — the desk, the gate, the bodies, cells, doors
scripts/dev.sh prune       # the brokers' test residue and every test-shaped world's rows
```

Every proof refuses to run beside a lit kernel: **the stale-rig law** — a kernel older than the
code on disk poisons every test dispatcher, and a lit kernel on the same ground relays the suite's
facts to its own topics. Relight after every code change.

## The laws the rig keeps

- **Never pipe a worker-spawning verb** (`kernel` · `reference` · `walk` · `cell`): a pipe holds
  the spawned body's stdout open and the verb never returns. Redirect to a file instead.
- **`down` is compose stop and nothing more.** The ground's volume is the universe's memory;
  `down -v` is never spoken by the script.
- **The walk kernel is a release build.** Every door number a person reads is the real one; a
  debug build ran fifty to a hundred times its own query cost. `SPINE_PROFILE=debug` keeps the
  quick build for a code loop.
- **One crew per ground.** The host kernel and the boxed kernel
  (`docker compose -f spine/compose.yaml --profile kernel up -d`) share the host's `~/.orreth`
  and never light together on :4600.

## How to read the tree

| Path | What it is |
|---|---|
| `backend/plane/crates/orreth-spine` | **The kernel.** The pure laws (hermetic, fixture-held) and, behind the `bridge` feature, the ground, the rails, the doors, the feed, the bodies' seam, cells, the desk, the seat — the `orrethd` binary. |
| `spine/orreth_spine` | **The reference**, and the bodies every kernel spawns (`orreth_spine.body`). |
| `spine/conformance` | The fixtures both kernels pass unchanged. |
| `spine/glass/index.html` | The one page. |
| `spine/crew.v0.json` · `spine/templates` · `spine/bindings` · `spine/tools.v0.json` · `spine/levers.v0.json` · `spine/guide` | The crew, the templates, the bindings, the tool and lever declarations, the guide — data both kernels read. |
| `docs/rearch/0001`–`0009` | The canon of this world: the experience charter, transport, memory, agent, the build plan, markers, intent, the port, the old world carried. |
| `docs/design/0000`–`0017` · `the-honest-boundary.md` | The constitution the covenant enforces, and the standing register. |
| `contracts/v0` | The wire schemas. |
| `.claude/skills/orreth-covenant` | The covenant — the thirteen rules every model coding here holds to. |
