---
title: The HTTP API
description: Every door of a running Orreth world — the kernel's 35 endpoints and the agentic layer's console doors, with the rules they all share.
---

A running Orreth world answers on two kinds of doors, and knowing which is
which explains most of what you'll see:

- **Kernel endpoints** — served by every instance of the engine (`orrethd`;
  ports 4500/4501/4502 on the development stack, whatever your compose file
  says elsewhere). These are the stable, versioned API: identical at every
  level of a deployment, every call verified and billed.
- **Agentic-layer endpoints** — served by the Python worker on **:4562**.
  These feed the console's richer rooms (brain, observatory, atlas…). That
  layer is mid-refactor, so treat these shapes as informative, not
  guaranteed.

Three rules every endpoint obeys:

1. **Every "no" is identical.** A permission failure, an exhausted budget, a
   missing record, a revoked identity — all return the same
   `403 {"error": "request cannot be served under this capability"}`, so
   probing the API teaches an attacker nothing. (The project's name for
   this: *refusal wears one face*.)
2. **The kernel checks signatures but cannot create them.** Writes must
   arrive already signed by their author; reads must carry a permission
   token, re-checked on every use back to the operator's root key, with
   permissions that only ever shrink as they're passed along.
3. **Prompt content never enters the kernel.** The model endpoints decide
   *whether* a call is allowed and count its cost; the actual thinking
   happens on the caller's side.

## Kernel doors

### Records — the fabric

| Method · Path | What it does |
|---|---|
| `GET /health` | Scope, record count, clock high-water, whether a body store is attached, version |
| `POST /records` | **Ingress.** Verifies signature, identity standing, scope, and the monotone clock; stores the body by its content hash; `201 {id}` — or `409` on a clock violation, the one face on everything else |
| `GET /records/:id/body` | Fetch a body, **re-hash-verified against its own id on every read**; `409` if bytes were tampered |
| `POST /retrieve` | **Egress — the retrieval router.** Token-verified; filters by scope, time, and visibility; escalates by time-budget; delegates upward; one-faced refusal |
| `POST /tombstone` | Governed erasure: strips the stub, physically deletes the bytes, evicts the meaning vector — the only way anything is ever removed |
| `POST /runs` | Ingest a signed work record — author must differ from the agent it grades |
| `POST /embeddings` · `POST /embeddings/missing` | Token-gated write of a record's meaning vector · the worklist of records not yet embedded |

### The tree — topology and presence

| Method · Path | What it does |
|---|---|
| `GET /standards` | The rules this node hands down; children pull it at boot |
| `POST /hello` | A child's presence beat, every 5 s, carrying its subtree summary |
| `GET /topology` | This node's subtree as assembled from beats |
| `GET /presence` | Who lives here and below — built-in staff and joined workforce |
| `GET /rollup` | The living numbers: memories, runs, success rate, tokens, dollars, per descendant |

### Identity and the human queue

| Method · Path | What it does |
|---|---|
| `GET /organs` · `POST /organs/pin` | The pinned staff roster · pin one, via a chain-verified token |
| `GET /requests` · `POST /requests` | The human decision queue — list it, or file an ask (unsigned input; the queue mints the id) |
| `POST /requests/resolve` | A human's decision lands — done or denied, with words |
| `POST /worker/pulse` | The agentic layer's heartbeat; silence beyond the threshold is witnessed and, under consent, rung to a human |

### Models (shown in the console as *the Stable*)

| Method · Path | What it does |
|---|---|
| `POST /model/authorize` | Token-verified model resolution + budget debit; a miss climbs to the parent |
| `POST /model/meter` | Reconcile estimated vs. actual tokens on the running bill |
| `GET /model/usage` · `POST /model/replenish` | A subject's fuel state · refill it to its allowance (a human's act) |
| `GET /stable` | Every approved mind here and below, with per-agent usage |
| `POST /stable/hello` · `POST /stable/state` | A mind's canary beat (three earn `available`) · a governed lifecycle move |
| `POST /model/state` · `POST /stable/saddle` | **Dev-only** shortcuts — slated to become governed escalations |

### Tools (shown in the console as *the Farm*)

| Method · Path | What it does |
|---|---|
| `GET /farm` | Every tool service here and below, each pinned to the exact fingerprint a human approved |
| `POST /farm/hello` | A service heartbeat; three beats end probation |
| `POST /farm/state` | A governed lifecycle move (rest, quarantine, decommission…) |
| `POST /farm/meter` | Record one tool use — this door **is** the authorization: a non-serving service or missing grant gets the one face |
| `GET /farm/callers` | Recent callers per service, from the meter's own entries |
| `POST /farm/plant` | **Dev-only** direct planting |

### The console

| Method · Path | What it does |
|---|---|
| `GET /window` | The console itself — compiled into the kernel, holding **no privileged path**: every render is a tokened `/retrieve` |
| `GET/POST /window/cfg` | Read / pin the read-only viewer capability the console uses |

## Agentic-layer doors (`:4562`)

`GET`: `/observatory` · `/governance` · `/craft` · `/sentences` (the live
glossary) · `/desk` (the capabilities portal) · `/desk/bundle` · `/brain` ·
`/resident` · `/pulse` · `/spacetime` · `/market` · `/assign` · `/seeds` ·
`/record` (whole-rig record reader) · `/atlas` · `/inbox`.
`POST`: `/craft` (leased craft acquisition) · `/tool` (governed tool
invoke) · `/` (the embedding door).

These compose richer views by calling the kernel doors above with the
worker's own credentials — nothing here bypasses the kernel's checks.
