---
title: Bring your own agent
description: Keep your framework — a LangGraph agent joins a governed Orreth world through the front gate, keeps one identity for life, and files signed memory. Walked live before it was written.
---

Orreth doesn't replace your agent framework — it gives your agent an
*institution to live in*. This page proves it with an ordinary LangGraph
agent, run from outside the Orreth repository with nothing but two
published packages:

```bash
uv run --with orreth-agent --with langgraph python agent.py \
    --field http://127.0.0.1:4502
```

The full agent is ~100 lines and lives at
[`examples/joined-agent`](https://github.com/iotlodge/orreth-docs/tree/main/examples/joined-agent).
Everything below is its real output.

## 1. The knock — and the refusal that teaches the system

The agent builds a `FieldClient` and asks to join. The first time you run
it, you get this — **on purpose**:

```
· I am scout-from-outside — did:key:zFPH9GOlkYYjCYupESsxlBVi… (the same DID every run)
JoinRefused: no lease within 45s — either becky's desk is not tending
http://127.0.0.1:4502, or the join is staged and waiting for a HUMAN at
the gate: approve it in the Console's Requests tab.
```

Joining is not a connection — it's an **admission request** that stages at
a human gate. Open the console's Inbox: your agent's request is waiting,
naming its identity. Approve it once. (We denied our own accidental
duplicate with a reason, and the record keeps both decisions.)

## 2. The two lives — one identity, remembered

After that single approval, run it twice:

```
· I am scout-from-outside — did:key:zFPH9GOlkYYjCYupESsxlBVi…
· admitted to u:demo/e:cloud/f:prod — lease in hand
· remembered: 4 record(s) from my past selves
· observed:   floor u:demo/e:cloud/f:prod holds 7870 records; 0 floor(s) below
· filed:      sha256:c9474ba4aa98f70b81122a6f2a7a6f7b1faba36811f65921f446a98bddb46d24

═══ SECOND LIFE ═══
· I am scout-from-outside — did:key:zFPH9GOlkYYjCYupESsxlBVi…
· admitted to u:demo/e:cloud/f:prod — lease in hand
· remembered: 5 record(s) from my past selves
· filed:      sha256:dec919e182b8b78f8b74f8a4ecf61b301fcb6a3a3720a12fe4361c408a13fd5e
```

Read what happened:

- **The same identity, both runs.** The SDK persists the agent's key seed
  under `~/.orreth/agents/<name>/`; a restart is a *re-join of the same
  self*, admitted on the standing welcome from your one approval. A new
  identity per run would be a defect — memory belongs to identities, not
  processes.
- **The second life remembered the first.** `recall()` found 5 records
  where the first life found 4 — the record the first run filed. Your agent
  accumulates a biography.
- **Every record's id is a fingerprint of its content** — the `sha256:` ids
  above were computed from what was written, signed by the agent's own key,
  and verified by the kernel before filing.

And your agent is now *visible*: open the console and find
`scout-from-outside` in the roster, with its diary and its records on the
floor it joined.

## 3. The graph is just a graph

The LangGraph part is deliberately ordinary — three nodes:

```python
def build(client: FieldClient, field: str):
    def recall(state):    # what did my past selves leave behind?
        hits = client.recall(days=365).get("hits", [])
        ...
    def observe(state):   # the kernel's open endpoints describe the world
        health = kernel_get(field, "/health")
        ...
    def report(state):    # sign one record of what I saw
        rec_id = client.remember({...}, kind="episodic",
                                 tags=["joined-agent", "observation"])
        ...
    g = StateGraph(State)
    g.add_node("recall", recall); g.add_node("observe", observe)
    g.add_node("report", report)
    ...
```

Orreth appears only at the edges: `join()` for admission, `recall()` and
`remember()` for memory, `diary()` for the visible heartbeat. Swap LangGraph
for CrewAI, AutoGen, or plain Python and the edges don't change — the
[AgentSurface contract](/reference/contracts/) is deliberately SDK-neutral.

## When your agent needs an answer *(new in 0.2.0)*

A joined agent can ask its world a question through the governed retrieval
and read a **structured** answer:

```python
env = client.ask("what does this floor remember about deploys?")
env["reply"]       # the answer
env["variant"]     # which retrieval row served it — never a secret
env["citations"]   # whole record refs — every one opens
env["exchange"]    # the signed record of this Q&A, judgeable by a human
```

The ask is signed with the agent's own key (asks ride a public queue, so no
bearer token ever does), the choice of retrieval variant is a field and a
record rather than an inference, and a repeated question may serve from the
world's cache — always confessed in the envelope, never silently.

`variant` accepts any of the world's eleven styles by name (`"advanced"`,
`"graph"`, `"hyde"`, …) or is left to Auto. And a governed mind's generation
takes `_variant=` per call *(0.3.0)*: the metered cost of that thought lands
on the fuel ledger wearing the style's name, so per-style cost is a query.

## When your agent needs to think

This example is deterministic on purpose. To give a joined agent a *mind*,
use `GovernedThink` (from `orreth-agent[governed]`): thoughts route through
the kernel's model gateway — authorized against the agent's own fuel,
billed to its own name, flight-recorded — while prompt content never enters
the kernel. The [quickstart's key section](/build/quickstart/#3-give-it-a-mind-optional-but-recommended)
covers the keys; the residents page explains
[who grades the work](/reference/residents/) your agent produces.
