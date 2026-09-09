---
title: The contracts
description: The sixteen JSON Schemas that define Orreth's wire objects — what each governs, and how the two implementations are held to them.
---

Everything that crosses an Orreth wire is governed by one of **sixteen JSON
Schemas** in
[`contracts/v0`](https://github.com/iotlodge/orreth/tree/main/contracts/v0)
(draft 2020-12, `$id` namespace `https://orreth.ai/contracts/v0/…`). The
contracts are deliberately **depth-agnostic**: no schema carries a tier name
in a logic position — scope paths and relative spaces everywhere, so the
same objects work at any tier of any topology.

`v0` may still churn; semver discipline begins at `v1`.

| Schema | Title | Governs |
|---|---|---|
| `common` | Orreth common definitions | The 13 shared primitives every other contract references: DID, ContentHash, Sig, ScopePath, the two clocks, SemVer, Duration, TimeWindow, Space, Selector, Budget, StandardRef |
| `memory-record` | MemoryRecord | **The atom of the fabric**: the append-only, content-addressed, signed record — with visibility facets, retention, and distillation lineage |
| `retrieval` | Query / RetrievalResult | The read path: space × time, budget-gated; a budget miss is indistinguishable from a permission miss |
| `capability-token` | CapabilityToken | Attenuation-only permission: every delegation hop narrows, verified at presentation to the pinned root. Kernel 0.71 added the narrow `resolve` action on the `queue` space — tending the request queue no longer requires any broader grant |
| `identity` | Identity | The immortal thread — memory keyed to the identity, never the process; attachment and governed transfer |
| `tier-profile` | TierProfile | The dials that make one binary a universe, ecosystem, or floor — retention, budgets, cadences, trust root, horizon |
| `run-record` | RunRecord | One unit of work, resident-authored — evaluations are never self-asserted |
| `pruning-policy` | PruningPolicy | The metabolism: what each layer keeps vs. distills vs. tombstones |
| `skill-standard` | SkillStandard | Procedural memory promoted with an acceptance rubric — promotion is a state transition, never a copy |
| `resolved-context` | ResolvedContext | The effective rule-set a subject operates under, content-addressed: same chain, same hash |
| `agent-surface` | AgentSurface | The SDK-neutral handle a workforce agent holds — five verbs: write, retrieve, skill bindings, model call, signal |
| `escalation` | Escalation | The human-decision work item: staged by machine, decided by humans, on wall-clock time |
| `factory` | StampOrder | Archetype → incarnation stamping at scale, governed, with birth certificates |
| `join` | Join | How a child registers with its parent: rules compelled downward, everything else offered |
| `signed-record` | SignedRecord / SignedBundle | The envelopes: observations push up, standards pull down |
| `universe-template` | UniverseTemplate | A whole universe as data — a pre-authored trust chain, stamp orders, and profiles |

## How the implementations are held to them

The honest shape, worth knowing if you build against the wire:

- **The Python reference validates directly** — every wire object in the
  conformance suite is checked against these schemas at test time
  (398 tests).
- **The Rust kernel is held indirectly** — the Python reference generates
  language-neutral input→output fixtures, and the kernel's own test suite
  replays them byte-for-byte (canonicalization, signatures, the resolver's
  hashes, the three flows). There is no shared runtime validator; the
  contract's authority reaches the kernel through the fixtures.
- **Canonical bytes are the real contract**: sorted keys, compact
  separators, ASCII escaping — the exact bytes that get hashed and signed,
  identical across the SDK, the reference, and the kernel, pinned by a
  cross-language parity suite.
