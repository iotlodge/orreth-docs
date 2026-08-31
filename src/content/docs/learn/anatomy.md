---
title: The anatomy of a running world
description: What actually exists when Orreth runs — the three bodies of the system, what universes, ecosystems, and floors really are, and why the topology is data.
---

This page answers the first honest question anyone asks of Orreth — including
its own architects: **what actually exists when it runs?** Everything below is
verified against the code, not the marketing.

## The three bodies

A running Orreth deployment is three distinct bodies:

### 1. The kernel — `orrethd`

One small Rust binary (~4,000 lines across six crates). It is a **verifying
record server**:

- **An append-only record store.** Everything that happens is a signed,
  content-addressed record (shown in the console as a *memory*). A record's id
  *is* the cryptographic hash of its content, so tampering — on disk, on the
  wire, anywhere — is caught on read. Nothing is silently rewritten.
- **An identity and permission system.** Every agent, tool, and human seat
  carries a decentralized identifier (a *DID* — an identity card that cannot
  be forged or reused). Permissions travel as capability tokens that can only
  **narrow** as they are delegated, and every token is re-verified at the
  moment it is presented, all the way up to one pinned root of trust.
- **A model gateway.** The kernel authorizes and meters every model call —
  which model, whose budget, how many tokens — but **never sees the prompt**.
  Cognition happens on the agent's side.
- **A tool registry** (shown in the console as *the Farm*) and **a model
  registry** (*the Stable*): tools and models are identities with lifecycles —
  probation, serving, quarantined, resting, decommissioned — and an approved
  tool is pinned to the exact fingerprint a human approved.
- **A human-approval queue.** Decisions wait at gates; silence never approves.

One property defines the kernel's security posture: **it verifies signatures
and cannot create them.** There is no signing function in the Rust code.
Private keys never enter the kernel process.

### 2. The agentic layer

A Python process that holds every private key and does every piece of
thinking. All of Orreth's built-in staff live here — *residents*, one per
duty:

| Resident | Duty (plain) |
|---|---|
| **becky** | identity and admission — mints the leases that let anyone in, chained to the root of trust |
| **the librarian** | retrieval — answers questions from the record, with citations |
| **charlotte** | the tool registry — onboards, watches, and answers for tools |
| **ada** | the model registry — the market of available minds and their terms |
| **vera** | evaluation — grades finished work; never grades her own |
| **allen** | infrastructure — the cloud architect; grows container bodies for tools |
| **the studio** | comprehension — reads every incoming objective and plans it |
| **quinn** | user-acceptance testing — walks the console as a stranger and files what confuses her |

The crucial fact about this layer: **it talks to the kernel over HTTP exactly
like your code would.** It signs records, presents tokens, and gets refused in
exactly the same ways. There is no privileged back door — which is why the
same doors are documentable for you.

### 3. The console

A single-page web console served by the kernel at `/window`. It holds **no
privileged path**: every panel it renders comes from the same tokened
retrieval doors any client uses. Humans ask; residents fetch — the console is
an audience room, not a control panel that bypasses governance.

## What exists when Orreth starts: nothing is hard-coded

Here is the answer to the question that motivated this page. If you have seen
Orreth's development rig, you have seen names like `u:demo`, `e:cloud`,
`f:prod`. **None of them are built into any binary.** The entire topology is
data:

```
one binary (orrethd)
  + demo-universe.json  →  the universe node   (port 4500)
  + demo-eco.json       →  an ecosystem node   (port 4501, parent: 4500)
  + demo-field.json     →  a floor node        (port 4502, parent: 4501)
  + one compose file    →  the running world
```

Three containers, one identical binary, three small JSON profiles, chained
parent to child. The profile supplies the scope, the retention rules, the
trust root, and the retrieval horizon; the `--parent` flag makes a node a
child that pulls its rules down from above and beats its presence up.

**Building your own world is therefore: write two small JSON files and a
compose file.** That tutorial is coming in the Build track — and it is short.

## Universe, ecosystem, floor — in plain terms

These three words name the tiers of a deployment. The machine's own
definitions (see the [glossary](/learn/glossary/)):

- **Universe** — the whole world one deployment shows: every floor, agent, and
  record under one set of rules. Think: *your installation*.
- **Ecosystem** — a wing of the universe grouping related floors. Think: *a
  zone or environment* (cloud, desk, production).
- **Floor** — one working room: agents live and work on it, and everything
  they do is filed on it. Think: *a workspace with its own store*.

The tiers are recursive — every tier runs the same binary and speaks the same
contract, and rules cascade downward while records and presence flow upward.
A floor's rules can only *tighten* what the universe allows, never loosen it.

## The flow of a single action

Every consequential thing in Orreth follows the same five steps:

1. **Sign.** The actor (agent, resident, or human seat) builds a record and
   signs it with its own key.
2. **Verify.** The kernel checks the signature, the identity's standing, the
   permission chain, and the clock. Any failure earns the same uniform
   refusal — a prober learns nothing from the shape of a "no".
3. **File.** The record lands append-only at its floor; its body is stored by
   its own content hash.
4. **Gate.** If the action has external consequence, it *stages* and waits for
   a human decision. Silence never approves.
5. **Project.** Everything you see — search indexes, dashboards, rollups, the
   console — is a rebuildable projection over the one signed log. Delete any
   projection and it can be rebuilt from the record; the log is the only
   truth.

## What is *not* built in

Everything purposeful — trading desks, research agents, your workflows — is a
**capability**: a folder containing declarations (prompts, a manifest, a crew)
that the machine discovers at boot, a human approves, and the console renders
through typed panels without ever loading the capability's own JavaScript.
Install is dropping the folder in; uninstall is taking it out; the records it
made remain, because history is never deleted by tidying.

That separation — a small governing machine, and purposes as removable data —
is the whole idea of Orreth in one sentence.
