---
title: The crew — templates and bindings
description: The ten seats a kernel lights with, the template that declares a body, the binding that makes a workspace's agent, and the policy every body wears.
---

A kernel seats its crew from one manifest, `spine/crew.v0.json`: ten seats, each a template, two
of them with a binding. Both kernels read the same file; the Rust kernel spawns one process per
seat and the Python reference, standing alone, seats them in-process. One crew, one truth.

## The ten seats

| Seat | Kind | Function | Mind | What it does |
|---|---|---|---|---|
| **librarian** | resident | — | yes | Reads and recalls what this world knows; keeps your words in the Record; tools: weather, acquire, seal-record, purge-memory, mark, now (through the clock MCP server, when it stands). Reviews its day every hour. |
| **echo** | resident | — | no | Repeats your words back — the body proven before the mind arrives. |
| **planner** | firmware | plan | yes | Writes the steps of an objective; answers a red watch with one lever from the catalogue. |
| **critic** | firmware | critique | yes | Marks improvements on what the crew did; interested in `improvement`. |
| **grader** | firmware | grade | yes | Grades another body's work; never its own yardstick. |
| **mitl** | firmware | impact | yes | The Master Mind In The Loop: reads the canon and the covenant from disk; says what an act touches. |
| **toolkeeper** | firmware | tools | yes | Tends the shelf: probes, versions, proposes a retire after strikes; registers an MCP server on your word. |
| **stablekeeper** | firmware | minds | yes | Tends the Stable: pings minds, watches drift and end-of-life, proposes re-pin, swap, refill; registers a mind on your word. |
| **crew** | firmware | workspace | yes | The CREW pull's agent (binding `bindings/crew.v0.json`): answers about the crew from the cards. |
| **monitor** | firmware | workspace | yes | The MONITOR pull's agent (binding `bindings/monitor.v0.json`): reads the operating state and proposes watches with the add-watch tool. |

Every seat names `claude-haiku-4-5-20251001` as its preferred mind; on a world without that mind
the body says so in its reply until a person assigns it another.

## The template

A body is declared by a JSON file in the `orreth-resident-template/1` format. The librarian's:

```json
{
  "format": "orreth-resident-template/1",
  "name": "librarian",
  "version": "0.1.0",
  "nature": "reads and recalls what this world knows; tools: weather, acquire, seal-record, purge-memory, mark, now (through the clock MCP server, when it stands)",
  "persona": "a warm, plain-spoken keeper of what the world knows — answers completely, says what she recalls, and never pretends to remember what she was never given",
  "graph": "mind.v0",
  "mind": { "model": "claude-haiku-4-5-20251001" },
  "capabilities": ["ask", "tools:weather", "tools:seal-record", "tools:acquire", "tools:purge-memory", "tools:mark", "tools:now"],
  "schedules": [
    { "text": "Review what was asked of you today and note one thing worth remembering.", "every_s": 3600 }
  ]
}
```

| Field | Meaning |
|---|---|
| `name` · `version` | The body's name (one name, one self on the roster) and the template's version; a new version is a sibling, the identity persists. |
| `nature` | One plain sentence of what it does — shown on its card and on the panel's inspector. |
| `persona` | A resident's voice. A firmware body has none; it has a `charge` instead. |
| `kind` · `function` | `"firmware"` and its function name (`plan`, `critique`, `grade`, `impact`, `tools`, `minds`, `workspace`) — absent for a resident. |
| `graph` | The loop the body runs: `echo.v0` (no mind) or `mind.v0` (thinks through the gateway). |
| `mind.model` | The mind it prefers; the Stable's assignment law may give it another. |
| `capabilities` | What it may do: `ask`, and `tools:‹name›` for each tool it declares — a tool not declared is refused with a teaching. |
| `schedules` | Its own standing duties (side B), each an ask on a cadence; kernel-required duties are added by the kernel and are never editable. |
| `interests` | The marker kinds it is dispatched an ask for when one lands (the critic's is `improvement`). |

A template's content hash rides the body's join, so the desk knows exactly which declaration a
body was born from.

## The binding

The two workspace agents are one template — `templates/workspace-firmware.v0.json` — with a
binding per pull. A binding is `orreth-workspace-binding/1`: the pull it serves, a prompt, the
skills it may use, the capabilities (tools) it is given, and the policy it wears. The monitor's
grants `tools:add-watch` and says, in its prompt, that a watch's sense is the kernel's — red while
its condition holds — and that a proposal is a call to the tool, never a question back.

## The policy every body wears

`spine/policy/covenant-policy.v1.json` — thirteen rules, version 1.1.0 — is loaded by every body
before it may join; no policy, no join. The join records the version worn, and the card shows it.

1. A keypair is a self, and a self survives the process — a new identity per run is a defect.
2. Nothing grades its own yardstick — outcomes are recorded by another, never self-attested.
3. Joining is a governed request — no agent enters the world without loading this policy and passing the gate.
4. Refusal wears one face outward; governed gates teach inward.
5. The plane authorizes and meters; it never sees the prompt — and no mind thinks off-meter.
6. Canonical bytes are the contract — the same message is the same bytes everywhere.
7. One world, one picture — every view derives from the same committed truth.
8. Lived time is monotone — backdated memory is refused.
9. The core is sacred — it changes only with the human's explicit word.
10. Provenance or nothing — every artifact names its author.
11. The human can always stop what the machine manages — cancellation is a first-class recorded act.
12. Every ask wears its journey, and every schedule lives in its runner — nothing runs unseen.
13. Every word aimed at a human is plain — complete, in the human's own terms; a machinery name only beside its plain words, never instead of them.

## How a body lives

Born from its template, a body loads (or mints once) its keypair under `ORRETH_HOME/agents/‹name›/`,
loads the policy, knocks at the desk, collects its lease, subscribes to the shared bench and its
own, streams its words to the kernel that spawned it, serves asks and duties, emits its journey,
and stops whole on SIGINT — its lease lapses and the roster reads dormant in seconds. The kernel
restarts a body that died after one second, doubling, capped at thirty; parks one that dies three
times in five minutes; never restarts a refusal at birth; stops every body at dark.
