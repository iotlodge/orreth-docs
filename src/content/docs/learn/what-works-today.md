---
title: What works today
description: The honest register for kernel 0.1.0 — what is proven with the evidence named, what is partial or owed, and what is parked.
---

Most documentation tells you what a system aspires to do. This page follows Orreth's standing
register of **claims with their evidence named** — `docs/design/the-honest-boundary.md` in the
kernel's repository — under one rule the project has kept since July 2026: *a claim not on the
register with evidence named is a claim we do not make.* What follows is that register for the
0.1.0 kernel, in plain words, in three honest tiers.

Everything in the first tier was proven on the running kernel, most of it walked by a person in
the glass with no script, and pinned by tests that run on every change.

## Proven, with the evidence named

**Two kernels, one law**

- **The Rust kernel and the Python reference pass the same fixtures unchanged.** Twenty-six
  language-neutral fixture files under `spine/conformance` pin every wire contract — the
  envelope's bytes, the desk's transitions, the seat's verdicts, the levers, the watches. The Rust
  runner reads 730 cases; the reference suite runs in the nine hundreds.
- **The era is one number.** `VERSION`, the kernel crate and the reference package all say
  0.1.0, both health doors whisper it, and a hermetic test on each kernel holds its face to the
  file.
- **The ground has one writer.** The schema wears a version; the first kernel to find the ground
  below its number migrates it and records that; every later kernel waits and verifies; a ground
  whose version lies is refused in words. Both kernels stand the same forty tables column for
  column.
- **Every door is clocked and every knock is pooled.** A fixed handful of reads however large the
  crew; the p50 and p95 of every door on the panel; a pool of lines to the ground with a ceiling,
  and a watch can stand on the slowest door or the pool's strain.

**Identity, the seat and the desk**

- **A keypair is a self, and a self survives the process.** Every body's seed lives under its home;
  the same self re-joins every life; a new DID per run is a defect the covenant names.
- **A person holds a seat.** A capability token in the covenant's shape, attenuation-only, minted by
  the kernel's own self after the person's TOTP code, read at every door. The first to prove an
  authenticator on an unheld ground is its owner. The browser origin is closed; a knock ceiling
  stands per person at every door. Fixture `seat-v0`: 80 cases on both kernels; `tests/gate.rs`.
- **A body joins through a five-status desk.** Challenged with the kernel's nonce, proven by the
  key behind its DID, staged for a governing seat's click (or admitted at once on the crew's
  spawn ticket or its standing welcome), then a root-chained lease with the fuel clause collected
  by the same key. A hold nobody answers in fifteen minutes is denied and recorded. Fixture
  `desk-v0`: 86 cases; `tests/desk.rs`. This book's
  [Seat your own body](/build/your-own-body/) page walked it from outside.
- **The root seed is as protected as in the first architecture, or better.** Raw 32 bytes,
  `0o600` on every path, zeroized on drop, a wrong-length file a hard error; only public keys and
  DIDs ever leave a process. Verified by a read of both worlds' code, not adjusted.

**The crew**

- **The kernel spawns and governs every body as a process.** Ten seats from one manifest; a body
  that dies is restarted after a backoff; one that dies three times in five minutes is parked as
  a fact with its last words; a refusal at birth is never restarted; every body stops whole at
  dark. Fixture `bodies-v0`; `tests/bodies.rs`.
- **What a tool is, both kernels read; what it does stays in the body.** Nine built-in tools are
  declared as data; the Rust kernel seeds and probes the shelf itself; execution is bound by name
  body-side and refuses to start when a declaration has no executor. Fixture `tools-v0`: 35 cases.
- **The residents know who they serve.** Your name, place, time zone and free claims stand on
  the ground, labeled by who said it, read first by every body, carried over the seam with a
  routed ask and kept by no far cell. A withdrawn word is recorded, never deleted.

**The gateway and the meter**

- **Every thought goes through one gateway under the body's own key and lands in dollars.**
  LiteLLM run and managed by the kernel; every body a virtual key with a budget and a renewal
  window; every answer wears its cost; a health check holds the meter to the gateway's own
  numbers.
- **Minds are stalls with pinned deals.** Price drift makes a mind unhealthy and proposes a re-pin;
  an announced retirement proposes a swap; a drained body proposes a refill. The stablekeeper
  proposes and never acts alone.

**The remediation rail**

- **The kernel remediates and says what it did.** A red watch opens a forensic dossier read off the
  ground with no mind; the planner answers in a lever catalogue declared as data; the kernel pulls
  the lever through the same door a person would (routine at once, consequential held for a click,
  grave never); the outcome is attributed on the record — cured with its cause, self-healed, or
  still red and handed to the human with the dossier. Fixture `levers-v0`: 44 cases;
  `tests/test_remediation.py`; `tests/bodies.rs` step 8 (the Rust kernel alone parks echo and cures
  it itself).
- **The pulse reads the money.** Fifteen watch metrics in one order on both kernels, pinned by a
  fixture; the glass says "not measured here" for an absent value, never a zero.

**The ground and the rails**

- **Poison is parked, never lost and never looped.** Bytes the rail carried that were never an
  envelope, or a fact that can never apply, are parked once with their evidence; the dispatcher
  holds at them until a person's recorded word advances it.
- **The outbox is a queue with retention**, pruned hourly under its own beat; the feed runs on
  thirty-three topics; the roster follows the feed, not a timer.

**Cells and the seam**

- **A universe is a cell of its own, sealed from every other.** Two Rust kernels on two databases
  and roles: the seal felt (one cell's role may not enter the other's database), the seam pinned
  both ways, an ask routed home and answered here, the stop reaching the far cell in 0.6 s, the
  peer dark → parked in plain words → back → resumed and landed once, a stranger and a replay
  wearing the one face, re-homed → epoch 2 with the old home refusing. Fixture `cells-v0`: 57
  cases; `tests/cells.rs`.

**The glass**

- **THE PANEL is a mimic panel of the kernel.** Geometry is architecture (six organs, the crew's
  sockets from the roster, the shelf's tool lamps); light is operations (thirty-three feed topics
  light the rails, then fade); colour is origin; three soft toggles on one drawing; every block a
  door; full screen; the Daylight Glass; the version whisper. Walked by JB on 2026-09-29.
- **The tour** walks a person around the live panel one part at a time, in plain words, with the
  world still moving underneath.
- **One name, one self.** The roster folds one row per name with earlier selves counted; a proven
  key claiming a held name is staged for a governing seat; a watch and a peer rest on a recorded
  row, never a delete.

**The image**

- **`ghcr.io/iotlodge/orrethd:0.1.0`** is published and public; `:latest` is the same bytes. The
  kernel and its crew in one image, verified from inside the box. This book's
  [first world](/build/first-world/) was walked against it on 2026-09-30.

## Partial or owed, with the gate named

- **The image is linux/arm64 only.** Every image before it was too; amd64 is owed (the Rust stage
  cross-builds).
- **A published SDK that joins from the door alone is owed.** `orreth-agent` 0.4.0 on PyPI speaks
  the first architecture's doors, not this desk. Today a body is `python -m orreth_spine.body`
  from the kernel's own repository, and it needs the rails reachable, not only the door. The
  [Seat your own body](/build/your-own-body/) page says exactly what works.
- **The learning loops and the long objective are designed, not built.** A grader as a firmware
  resident with signed verdicts, a lessons digest packed into context, and a 500–1000-hop objective
  resumed at hop N as the same self are canon row 6, after row 5. Every reply is already a signed
  fact and the per-hop checkpoint stands; no grader body, no verdict fact, no lessons digest yet.
- **Understanding is lexical.** No embedding lane, no vector projection on this kernel; the first
  architecture's eleven retrieval styles are a capability to re-prove atop it.
- **No purge on this kernel yet.** A withdrawn profile word is hidden, not crypto-shredded; the
  purge-memory tool's tombstone law is the reference's.
- **No cascade between worlds.** Every cell wears its own policy sheet; a seat's grants only
  narrow; but the tighten-only fold from universe to cell to body, and a content-addressed law a
  thought names, wait for a proof that needs them.
- **No roll-up across cells.** The meter is read by world; the seam carries the world card, the
  roster and the answers to routed asks, not the meter. The costs panel is a named seed.
- **A person's name is their DID.** No person keypair yet, so a person cannot delegate a seat.
- **No bell.** Dormancy is noticed and listed; nothing reaches a person beyond the glass.
- **The kernel is its own root.** No offline ancestor: a host compromise is a root compromise. No
  seed backup or escrow rite; TOTP secrets and lease tokens are plaintext on the ground.
- **Bodies are rows.** The ground is the only store; no blob lane; no read-time re-verification of
  a body's bytes against its address.
- **The dev cell is unsealed by design.** The health check "this cell is sealed" reads false on
  the standard rig, whose role reaches more than one database; `scripts/dev.sh cell` seals one.
- **Four wounds are open from the last walk**, recorded for after the refresh season: a stop's
  words name no ask; a waiting ask's "since" wears no date; a returned publish read as delivered
  (twenty-seven commands reached no queue on the dev ground); a failed thought's words filed as
  an objective.

## Parked, each behind a named gate

- **Hosted custody, federation beyond two cells, disaster recovery, multi-tenant evidence** — the
  hosting decision and a partner's real need.
- **A capability install door** — the first architecture's sealed, signed package has no seat on
  this kernel yet; the one chat is the one place.
- **The Faculty and the Agent Lab** — built only when the kernel is stamped ready to test it.
- **Voice, the multiverse portal, enterprise identity federation** — V2.
- **The demo site and the articles** — turn after this book, in the refresh season's order.

## What became of the first architecture

Orreth's first architecture — seventy-three design dives, the Living Brain, the Console, the demo
reel, the old plane and its Python simulator — was halted on 2026-09-14 for the foundation this
kernel stands on: performance for hundreds of bodies, one signed log, one law at every layer. It
is kept whole, never deleted, at the tag `main-v0.72-old-world`, and `docs/rearch/0009` in the
repository is the ledger of what each old organ became here: carried, re-seated, a capability
atop the kernel, or parked with a reason. Nothing was lost by silence.
