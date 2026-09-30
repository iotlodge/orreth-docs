---
title: The monitor and its levers
description: The MONITOR pull — the operating state live, the fifteen watch metrics, the eleven health checks, the harness, the parked events, the peers, and every lever a person or the kernel can pull.
---

Say **open the monitor** or click MONITOR on the sill. The pull slides in with the operating
state of this world, live, and the monitor's own firmware agent joins the chat: it reads the same
facts and can propose a watch. Every lever a person can pull is on this pull, and each is recorded,
never deleted.

## What it shows

| Card | Reads |
|---|---|
| **PULSE** | What the world spent today in dollars, thoughts per minute, minds standing, bodies out of fuel — the meter, read by world. An absent value says *not measured here*, never a zero. |
| **PEERS** | The cells this kernel names: "cell two · u:two · live", "3 s behind", "unreachable since 16:13". A peer can be let go on a governing seat's word. |
| **THE STABLE** | Every mind with its deal, its health and its assignments. |
| **HEALTH CHECKS** | What must be true of this world, read from the ground every thirty seconds: each row holds or BROKEN with its words. |
| **RAILS** | The outbox's depth and age, the benches' depth, the topics, and every event the dispatcher **holds at** — parked with its evidence, nothing behind it dispatched until a person decides. |
| **BODIES** | Every body alive or dormant, with its lives; a PARKED one with its last words and the restart lever. |
| **ASKS** | The asks left waiting, each with a stop. |
| **WATCHES** | Every watch, red or green, with its condition and since when; a rest lever on each. |
| **HARNESS** | The last golden run against a body's mind, and a door to run it now. |
| **THE DOORS** *(PERFORMANCE on the panel)* | Every door this kernel answered in the last ten minutes, p50 and p95, the slowest first, red past one second; the pool of lines to the ground. |

## Watches

A **watch** is a named alert on one metric: it is **red while its condition holds** —
`metric op threshold` — and green otherwise. That sense is the kernel's, not yours or the
agent's; a watch is never read the other way round. Fifteen metrics stand on both kernels, in one
order, pinned by a fixture:

`outbox_pending` · `oldest_outbox_age_s` · `asks_received` · `bodies_alive` · `bodies_dormant` ·
`minds_standing` · `minds_unhealthy` · `usd_today` · `route_failures_1h` · `meter_rate_10m` ·
`bodies_drained` · `door_p95_ms` · `pool_busy` · `pool_waiting` · `parked`

| Say | What happens |
|---|---|
| **watch for asks left waiting** | The monitor agent proposes a watch with the add-watch tool — a hold you cut. |
| **propose a watch that usd_today > 5** | A watch over the farm: spend today, thoughts per minute, minds standing, bodies out of fuel. |
| **watch for door_p95_ms > 1000** | A watch on the slowest door — the performance law, watched. |
| (the rest lever on a watch) | The watch rests on a recorded row; it stops judging and stops waking the intent loop. Never a delete. |

When a watch **turns** red (the transition, not a standing red) the kernel records
`orreth.watch.turned.v1` with *since*, and an observation lands under every intention interested
in `watch-red` — Resiliency first. What happens next is the remediation rail, below.

## Health checks

Eleven sentences that must be true, read from the ground every thirty seconds, each holding or
BROKEN with its words:

1. a duty answered, not refused
2. the monitor's offers arrive as holds
3. every service healthy or retired
4. every MCP server answers initialize
5. the keeper proposes after strikes, never retires alone
6. every mind answers
7. the gateway answers and holds every mind
8. the meter and the gateway agree
9. a model change is announced
10. this cell is sealed
11. every red is answered and every green attributed

On a fresh world without a mind, checks 3 and 6 read BROKEN with the reason (no mind to answer),
and on the repository's standard rig check 10 reads *unsealed (the dev profile)* because that
ground's role reaches more than one database. Neither is hidden; both say why.

## The harness

The golden cases run against a body's mind — the librarian's, on the kernel's own half-hourly
duty — and a failing run escalates to the chat. Say **run the harness against the librarian now**
to run it on demand; from the Rust kernel the run rides the rail to the body and lands under the
kernel's run id when it is done. The harness also grades the remediation rail: the eleventh check
is its verdict that every red was answered and every green attributed.

## Parked events

The RAILS card names every event the dispatcher holds at: bytes the rail carried that were never
an envelope, or a fact that can never apply. Each is parked once with its evidence and its own
fact; nothing behind it is dispatched until a person decides. Say **advance past parked 3**, or
use the card's lever; the advance is recorded in your name. Nothing is lost silently and nothing
loops.

## The levers

A **lever** is a governed act the kernel itself can pull, through the same door a person would —
a tool is what a body runs; a lever is what the kernel does with its own hands. Fifteen are
declared as data both kernels read (`GET /levers`), each with its consequence and the watch
metrics it can remedy. The full catalogue is on the [tools and levers](/reference/tools-and-levers/)
page; the shape of it:

- **Routine — pulled at once** under the intention's authority: restart a parked body; check,
  restore a service or a mind.
- **Consequential — held at the interlock** for a person's click: retire a service or a mind;
  register, assign, unassign, refill or re-pin a mind; re-home the universe; admit a body at the
  desk.
- **Grave — never pulled by the kernel**: stop or restart an intention. A person's code and a
  master's click.

## The remediation rail

When a watch turns red the kernel does not ask a mind what is wrong. It reads a **forensic
dossier** off the ground first — the watch, who it names and their state, the last acts on them,
the last time it went red — and hands the planner that dossier with the levers this door serves.
The planner answers *in the catalogue*: `LEVER: body.restart name=echo — BECAUSE: …`. The kernel
pulls the lever as a recorded hop in the intention's session, waits the lever's settle time,
reads the watch again and says what happened:

- **cured** — green after our act, wearing its cause;
- **self-healed** — green with no act of ours;
- **still red** — once more, then the human with the dossier;
- **cancelled** — a consequential lever the person declined.

You read it in the Analyzer (*last red: cured*) and on the tape. You were told, not asked — and a
consequential lever still held for you.

## The levers a person pulls here

| Say, or click | What happens |
|---|---|
| **restart the echo body** | A body the kernel parked or refused at birth is tried again on your word — its deaths forgotten, the same self. |
| **stop it** (on an ask's line) | Rests a waiting ask here and, if it was routed, at its home cell within two seconds. |
| (rest a watch) | The watch rests on a recorded row. |
| (let a peer go) | A governing seat's word; the peer's pin clears and it is greeted again on sight. |
| **advance past parked ‹n›** | The dispatcher goes past a parked event, recorded in your name. |
| **re-home this universe to cell three** | Consequential: held for your yes; the epoch advances and this kernel refuses to serve it afterwards. |
| **check the services** · **check the minds** | Every standing service probed by its kind; a mind answers a one-token ping through the gateway. |
