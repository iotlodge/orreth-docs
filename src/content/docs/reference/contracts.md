---
title: The contracts
description: The wire schemas under contracts/v0 and the twenty-six conformance fixtures that are the real contract between the two kernels.
---

Two things bind kernel 0.1.0's wire. The **schemas** under `contracts/v0` are the constitution's
product: sacred, changed only on the project owner's word. The **conformance fixtures** under
`spine/conformance` are the living contract between the Rust kernel and the Python reference:
language-neutral files of cases — *given this input, expect these bytes, this hash, or this
refusal by name* — that both kernels pass unchanged. A module is "ported" only when the Rust kernel
passes its fixture, the same file, unchanged.

## The schemas the kernel exercises today

| Schema | What it shapes | Where it is felt |
|---|---|---|
| `capability-token.schema.json` | A **seat** or a **lease**: subject · audience · grants · constraints (expiry, direction, a body's budget) · chain · sig. Attenuation-only. | Every seat the kernel mints validates against it; every lease too. |
| `common.schema.json` | DID · content hash · signature · scope path · space · budget · time window. | The DID pattern was widened for `did:orreth:person:‹name›`. |
| `join.schema.json` | The join spectrum, the lease terms. | The desk's five statuses carry its law. |

The remaining v0 schemas — memory record, skill standard, identity and attachment, retrieval,
pruning policy, tier profile, signed record, run record, escalation, factory, agent surface,
resolved context, universe template — are the design-phase constitution (`docs/design/0000`–`0017`).
They still bind; the organs that exercise them on this kernel are re-seated or owed, and
[what works today](/learn/what-works-today/) says which.

## The conformance fixtures

| Fixture | What it pins |
|---|---|
| `envelope-v0` | The transport envelope's canonical bytes, content hash, required fields, refusals by name. |
| `schema-v0` | The ground's schema version and its forty tables. |
| `rails-v0` | The names and shapes both kernels share on the rails. |
| `inbox-v0` | Parking a poison event and advancing past it. |
| `askroad-v0` · `ask-v0` | The ask road: the ask's row, its journey, its reply, the kind read from the words. |
| `loops-v0` | The beats: the scheduler's tick, the intent rail's turn, the beat lock. |
| `bodies-v0` | The park law (three deaths in five minutes), the backoff, the harness's command. |
| `desk-v0` | Every transition of the join desk, the challenge's and the collect's bytes, the lease's exact bytes with the fuel clause. |
| `seat-v0` | The seat token's bytes from a seed; the verdicts in fence order — expired, foreign authority, broken chain, bad signature, amplified; the doors' needs; the origin; the person grammar. |
| `proof-v0` | The proof ladder: L1 · L2 · L3, the hold's words. |
| `mitl-v0` | Summoning, dismissing, the impact door. |
| `markers-v0` | The registry, the structural seed, the tree under a marker. |
| `intent-v0` | The intention record, declare, stop, the loop's turn. |
| `levers-v0` | The lever catalogue and the remediation rail's outcomes. |
| `watch-v0` | The fifteen metrics in one order; a watch turning red and green. |
| `tools-v0` | The tool manifest by name and bytes; the held-by rule. |
| `services-v0` · `mcp-v0` · `minds-v0` | The shelf's ladder; the MCP client's three calls; the Stable's deals, pins and confessed degrade. |
| `memory-v0` | The Record's landing, recall, the purge's tombstone. |
| `profile-v0` | The person's own words with their labels, newest wins, a withdrawal. |
| `placement-v0` | Placement as policy: cell, metal, affinity, a refusal at birth with its reason. |
| `cells-v0` | Cells, the seam through every fence, routing home, partition, the stop, re-homing and the epoch. |
| `export-v0` | The compliance export's hash chain and signature. |
| `doors-v0` | Every door's name, its clock, the pool. |

The Rust runner (`cargo test -p orreth-spine --test conformance`) reads every fixture and reports
its count: 730 cases across the twenty-six at 0.1.0, not yet ported: none. The reference's
`tests/test_conformance.py` runs the same files on every change. A fixture the reference fails is
a fixture bug or a wound — never silently regenerated.

## The canonical bytes

The one rule beneath every fixture: **canonical bytes are the contract**. Both kernels serialize
a message with sorted keys, no whitespace, `\uXXXX` escapes and a float representation written by
hand rather than trusted to a library, so the same message is the same bytes everywhere — and the
same content hash. The seat's signature, the lease's, the seam's and the export's all stand on it.
