---
title: What works today
description: The honest register — what is proven with evidence, what is partial, and what does not exist yet.
---

Most documentation tells you what a system aspires to do. This page is
different: it is maintained from Orreth's standing internal register of
**claims with their evidence named** — a page the project has kept since July
2026 under one rule: *a claim not on the register with evidence named is a
claim we do not make.* What follows is that register in plain language, in
three honest tiers.

Everything in the first tier has been **proven live on the running system**,
most of it demonstrated by a human working through the console with no script.

## Proven, with the evidence named

**The kernel and its guarantees**

- **One binary runs any tier.** The universe, ecosystem, and floor tiers of a
  deployment are the same program with different JSON profiles — running today
  as three containers on the development rig.
- **Two implementations, one truth.** The Python reference and the Rust kernel
  agree byte-for-byte on canonical record content, held by a cross-language
  parity suite. The full behavioral model is covered by a conformance suite of
  450 tests.
- **Refusal wears one face.** A permissions failure, a budget failure, and a
  missing record all return the identical error shape — someone probing the
  system learns nothing from how it says no.
- **The kernel meters but never sees the prompt.** Model calls are authorized
  and billed by the kernel; the content of every thought stays on the agent's
  side.
- **History survives tampering.** A record's id is the hash of its content;
  tampered bytes on disk are caught on read. Erasure exists, but only as a
  governed act that leaves a tombstone — never as silent rewriting.

**Identity and admission**

- **Identity survives the process.** An agent that restarts rejoins as the
  same self, with its history intact. Joining is a human-approved request;
  permissions chain to one pinned root and only ever narrow.
- **A stranger's world can admit agents without holding the root key**
  *(kernel 0.71)*. The publishable **join door** ships with the SDK: the
  operator's root signs the door's credential once, offline, and never enters
  a serving process; the door challenges each joiner to prove its key, stages
  the request, and mints a properly chained lease only on the operator's own
  word — proven end to end against the published image and package alone.
- **The roster breathes honestly.** Present is distinguished from remembered;
  an absent agent goes dormant, never deleted; admission leases expire and
  renew; and no self is ever renamed — relabeling would counterfeit
  continuity.

**The eleven-style retrieval engine** *(dive 0065)*

- **Eleven retrieval styles, declared and serving.** Naive · Advanced ·
  Hierarchical · Multimodal · Multi-Agent · Reasoning-First ·
  Memory-Augmented · Graph · Hybrid · HyDE · Corrective — each a firmware
  declaration (its composition, requirements, cost class, and its delta in
  one plain sentence) with its working numbers as governed, gate-checked
  craft. The servable menu *derives* from the registry; a declared style
  whose flow is dark falls to the baseline loudly, on the record.
- **Asks read standing projections, not per-question rebuilds.** Chunk and
  tree rows (and their vectors) stand in Postgres, cut once by the same
  deterministic knife the rebuild uses; the graph lives beside them with
  every edge carrying its witness record and span. Both are confined to the
  ids a caller's retrieve already authorized, evicted the moment a purge
  lands, and rebuildable from the signed log at will.
- **The harness grades all eleven** — quality, latency, and the context cost
  a style asks a reader to consume — and the tournament's field derives from
  the registry, never a hand-kept list.
- **The selection is never a secret.** Which style served an answer is a
  field on the envelope, a tag on the signed exchange record, a spoken
  sentence in the console's reply, and a column on the fuel ledger — so
  per-style cost is a query.

**The doors that answer** *(kernel 0.71)*

- **The request queue is closed to forgers.** Resolving any request demands a
  root-chained credential carrying a narrow `resolve` grant; the one
  credential-less step is a joiner answering its own challenge; a settled
  decision is never rewritten; and the fuel ledger accepts a reconciliation
  only from the credential's own subject.
- **Machines ask and are answered, structurally.** A signed `ask` (the
  asker's own key — never a stealable token on the public queue) returns a
  structured envelope: the reply, its citations, which retrieval variant
  served it, and the whole decision record behind the choice. A failed
  signature is treated as forgery in every mode.
- **Knocking is metered per identity.** Every consequential door counts
  requests per identity in a fixed window; at the ceiling the answer names
  an honest retry wait, one caller's flood never slows another, and body
  size is a deliberate, dialed limit — all tunable as governed dials.
- **Repeated questions serve from a confessed cache.** Same words, same
  floor, same guardrail version — and only while the answer's signed record
  still stands; every cache hit says so in the envelope.

**Governance in action**

- **Nothing grades its own work.** Every unit of work is recorded by a
  separate signer, and finished work is graded by a *different* mind than the
  one that produced it — with the grader's own cost metered under its own
  identity.
- **No external consequence completes on the actor's word.** The proof is
  public: a signed deed at
  [demo.orreth.ai/deeds/first-deed.json](https://demo.orreth.ai/deeds/first-deed.json)
  was published, deliberately tampered, caught by the standing verification,
  walked back, and restored — the artifact carries its own story.
- **The machine's own parts are versioned like a constitution.** Prompts,
  rules, and sentences are editable, versioned assets; changing one issues a
  new named version of the whole machine; drift between the declared and
  running version is detected and *stages* for a human, never self-heals
  silently.
- **The human can always stop what the machine manages.** Every standing duty
  and running objective offers a governed cancel; a mid-flight cancellation
  stopped 18 fanned-out work legs at their next safe boundary, on the record.
- **The machine notices its own death.** A watchdog proved able to email its
  human when the system was killed — content-minimal, under standing consent,
  rate-limited so two deaths in one hour meant one email.

**Operations you can watch**

- **Every thought lands on a flight recorder** — model, tokens, cost, latency,
  including refusals — and the console's observatory renders it with each
  panel's evidence tier declared (log-truth vs. instrument reading).
- **A/B testing is constitutional.** Each experiment arm is a cryptographically
  named machine version; assignment is deterministic; adopting the winner is a
  signed human approval that keeps full lineage, loser preserved.
- **Settings are governed, not scattered.** Thirty-six operating values —
  cadences, budgets, thresholds — are live-tunable dials with declared bounds,
  each turn a versioned record, out-of-bounds turns refused with a teaching.
- **Memory has a metabolism.** Old records are compressed with **measured**
  information loss; a record a human touched stays warm while its neighbors
  distill; every floor breathes on a schedule.

**Building on it**

- **Capabilities are decoupled from the machine.** A complete working purpose
  (a trading-analysis desk producing reports a human reads, on real market
  data, through sixteen governed stages) installs by dropping a folder and
  uninstalls by removing it — verified by grep: the core has zero by-name
  references to any capability.
- **Outside tools join safely.** MCP tool servers are onboarded through one
  gate with secrets held by reference (credentials appear in zero records), a
  changed tool is caught by its fingerprint and quarantined until a human
  re-approves — rug-pull protection as structure, not scanning.
- **Outside agents join as themselves.** A LangGraph agent has joined a
  running universe through the same governed gate as everything else, kept its
  own framework, and worked under a lease.
- **The kernel image is published, and a world stands on it from three
  files.** `ghcr.io/iotlodge/orrethd` is publicly pullable (2026-08-31, the
  first seam this documentation cut), and the
  [first-world example](/build/first-world/) — two tier profiles and a
  compose file — was proven whole against it: floor joined under universe,
  presence beating up, rules cascading down, console serving.

## True but partial — the boundary, stated

- Some cognition paths are deterministic scaffolds or simulated judges — always
  labeled as such; live model judging exists and falls back honestly when
  ground is thin.
- The proven deployment is a single-machine development rig. Federation,
  hosted custody, disaster recovery, and multi-tenancy are designed but have
  no operational evidence yet.
- Human decisions on the request queue are persisted but not yet signed by a
  registered signer — the signer-registry work is designed, unbuilt.
- The projection layer degrades honestly when unavailable, but a full
  rebuild-from-log drill at production scale has not been run.

## Does not exist yet — being built by this documentation effort

This documentation project works by a rule we call **docs-driven
decoupling**: each tutorial page is written as if the packages existed, and
every step that turns out to be impossible from outside the monorepo names a
seam to cut. The current honest list:

- ~~No published container image~~ — **shipped 2026-08-31**: see
  `ghcr.io/iotlodge/orrethd` in the proven tier above. The *full* experience
  (residents, cognition) still runs from the repository — packaging the
  agentic layer is a later, deeper seam.
- ~~The SDK is not on a package index~~ — **shipped 2026-08-31**:
  [`pip install orreth-agent`](https://pypi.org/project/orreth-agent/)
  (Apache-2.0, one dependency), proven by a fresh install from the live
  index; the full public surface is now exported at the package top.
- ~~The capability manifest has no reference~~ — **documented 2026-08-31**:
  the [manifest reference](/reference/capability-manifest/) carries the
  contract and all thirteen panel kinds, and the SDK exports the same closed
  vocabulary (`PANEL_KINDS`) plus a validating builder. A formal JSON-Schema
  file remains future work.
- **Bring-your-own-package capabilities** — today a capability installs from
  the repository's own folder; installing one from an outside package awaits
  the trust machinery for it.

When an item above ships, it moves up this page — with its evidence named.
