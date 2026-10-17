---
title: The HTTP doors
description: Every door of kernel 0.2.0 — the seat law every door obeys, the open doors, the governing doors, the Studio's doors, and the shapes of the ones you will knock on first.
---

A running world answers on one door: the kernel's, port 4600 (the Python reference serves the same
doors on 4601). Everything the glass does, it does through these doors; there is no other API.
The doors are those of kernel 0.2.0 (2026-10-16). The shapes of the doors that stood at 0.1.0 were
read from a fresh world on 2026-09-30; the shapes of the doors added since — the path, the shelf's
drafts and wear, the Studio, the operating state — were read from both kernels' handlers on
2026-10-16.

## The laws every door obeys

1. **Every door reads who you are from your seat.** A seat is a capability token the kernel
   signed after your authenticator's code, carried as `authorization: Bearer ‹wire›` (the feed,
   which a browser cannot send headers to, takes it as `?seat=‹wire›`). The unseated wear one face:

   ```
   401 {"error": "not seated"}
   ```

   A seated person lacking a grant wears the proof's face, `403`. A body's lease is a seat with the
   role *body*: it opens `POST /delta` and nothing more.
2. **Refusal wears one face outward.** A forged proof at the desk, a stale seat, a foreign
   authority, an amplified grant, a missing join — all answer the same way (`{"error": "join
   refused"}` at the desk; `{"error": "not seated"}` at a person's door). A prober learns nothing
   from how it was refused. Governed gates teach inward: a consequential act's hold says exactly
   what it would do.
3. **The browser origin is closed.** A foreign `Origin` is refused before the body is read; no
   answer carries an open origin.
4. **A knock ceiling stands at every door**, per person (per address at an open door): twenty a
   second up to a burst of sixty, then `429` — *the door is busy for you — try again shortly*.
5. **Every door is clocked and every knock is pooled.** `GET /monitor` carries every door's p50
   and p95 for the last ten minutes and the pool's strain; a watch can stand on either.

## The open doors (no seat)

| Door | What it answers |
|---|---|
| `GET /` · `GET /index.html` | The glass — the one page. |
| `GET /health` | `{"clients", "kernel": "rust"｜"python", "lit_at", "rev", "schema": {found, ground, kernel, migrated}, "version"}` — the era's whisper. |
| `GET /guide` | What you can say here and what happens — the kernel's own guide, by section. |
| `GET /harness` | The health checks (`checks[]: {name, ok, detail, …}`), the last golden run (`last`) and whether all hold (`ok`). |
| `GET /seat` | `{"ceremony": true｜false, "hours": 24}` — whether anyone holds this ground yet. |
| `POST /enroll {person}` | The ceremony while no one holds the ground (afterwards: the owner's or a master's seat, or oneself with the old code, which is grave). Answers `201 {person, secret, uri, qr, re_enrolled}` — the otpauth secret and a QR as a data URL. |
| `POST /enroll/confirm {person, code}` | The first code finishes enrolling: `200 {enrolled: true, person}`. The code is the proof. |
| `POST /seat {person, code}` | The seat: `201 {person, role: owner｜master｜person, owner, seat_id, seat, wire, expiry, words}`. `seat` is the token in the covenant's shape — subject · audience · grants · constraints · chain · sig; `wire` is what you carry. |
| `POST /join` · `POST /join/prove` · `POST /join/lease` · `GET /join/:id` | The machine's desk (below). Their proof is a signature, not a seat. |
| `POST /seam` | Signed messages between peer cells; its own signature is its proof. |

## The desk — how a body joins

| Door | Body | Answers |
|---|---|---|
| `POST /join` | `{did, name, role, public_key, template_hash, policy_hash, ticket?}` | `{id, status: "challenged", join_nonce, …}` — the desk's own nonce, in the same breath; the key must derive the DID. |
| `POST /join/prove` | `{id, did, sig}` — a signature over `{did, join_nonce}` | `done` on the crew's ticket or a standing welcome; else `staged` with the hold in the chat; a forged proof `denied` with one face; a stale nonce (120 s) re-challenged. |
| `GET /join/:id` | | The join's status; open, the id its own secret; the lease never rides it. |
| `POST /join/lease` | `{id, did, sig}` — a signature over `{did, join, join_nonce}` | The lease: `{lease, wire, lease_id, expiry, admitted_by, join}` — a token chained to the root, grants `retrieve self · write self`, the fuel clause in its budget, thirty days. |
| `GET /join` *(seated)* | | The desk: every join, newest first — `{joins[]: {id, name, kind, did, status, template_hash, admitted_by, expiry, words}, lease_days}`. |
| `POST /delta` *(a lease)* | a body's own words | `204`. Unleased `401`; a person's seat `403`. |

## The person's doors (a seat)

**The chat**

| Door | Shape |
|---|---|
| `POST /ask {text, session?, kind?, parent?, to?, window?}` | `201 {ids: [ask_…]}`. `kind` pins thought · objective · intention (else read from the words); `to` fans out to named bodies; `window` is `{from, to}`. |
| `GET /ask/:id` | The ask's view: `{ask_id, text, target, status, reply, served_by, journey[], marker, origin, proof, hold, offer, session, window, asked_at, replied_at}`. |
| `GET /asks` | The asks, newest first, each with `status` (`replied` · `awaiting-confirm` · `waiting` · …), `served_by`, `person`, `fanout`. |
| `POST /asks/stop {ask_id}` | Rests a waiting ask here and, if routed, at its home cell. |
| `POST /confirm {ask_id, approve, code?}` | The interlock: `202 {approve, id, level: "L2"｜"L3"}`; a grave act needs `code` and a master's confirm from their own seat. |
| `GET /sessions` · `POST /sessions` · `GET /session/:id` | Your worldlines; a new one (`201 {session_id}`); one session's asks and results. |
| `GET /recall?q=` | Recall from the Record, stemmed and ranked; nothing found wears one face (`404`). |
| `GET /digest/:id` · `POST /digest` | A session's short version; write one now. |
| `GET /export` | The compliance export: `{contract: "orreth.compliance/1", rows[], hash_chain, root_hash, signature, signed_by, signer_key, hashing, summary, world}`. |
| `GET /feed` | Server-sent events: `{at, kind, message_id, ref, rev}` per fact; `Last-Event-ID` replays from a revision, or a `resync` tells you to reload. |
| `GET /fact/:message_id` | One fact by its id: the envelope — `authority_chain`, `correlation_id`, `marker`, `occurred_at`, `payload: {hash, proof, ref}`, `type`. Pointer and hash; the words stay on the ground. |
| `GET /profile` · `POST /profile` | Your portrait — `{person, name, place, zone, clock, coordinates, claims[], words}` — and a telling or a withdrawal. |
| `POST /seat/leave` | Ends your seat, recorded. |
| `GET /mitl` · `POST /mitl` · `POST /impact` | The Master Mind In The Loop: its ontology and citations; summon or dismiss it; *expected impact?* of a held act. |
| `POST /feedback {ask_id, sign, words?}` | A thumb on a reply — `sign` above zero is up, below zero is down: `201 {feedback_id, ask_id, sign, words}`. Routine, recorded; it feeds the Experience measurement and the grader's evidence, never a body directly. An ask not yet replied refuses in words (`400`). |
| `GET /includes?session=` · `POST /summon {name, summon?, session?}` | Who is in a session's crew — `{includes[], summoned[], base: [planner, critic, grader, mitl]}` — and a summonable body called into it, or dismissed with `summon: false`: `201 {summoned, state: summoned｜dismissed, body, person, session, marker, words}`. MITL is summoned by its own door, `POST /mitl`; a body that cannot be summoned refuses in words (`400`). |

**The crew, the shelf and the Stable**

| Door | Shape |
|---|---|
| `GET /crew` | `{crew[]: {name, kind, did, nature, alive, lives, joined_at, policy_version, capabilities, mind: {stall, degraded, why}, placement, side_a, side_b, template}}`. |
| `GET /residents` · `GET /bodies` | The roster (one row per name); the bodies as processes — `{bodies[]: {name, kind, did, lives, deaths, exit, last_words}, mode, spine}`. |
| `POST /bodies/restart {name}` *(governing)* | Restart a parked or refused body as the same self. |
| `POST /bodies/rest {name, session?}` · `/decommission` · `/restore` *(governing)* | The ladder, each rung the kernel's own held act: rest at L2 (the life stops at a safe boundary, the self kept) · decommission at L3, your code (a rested body only — the grave: its live objects removed, its self and record kept) · restore at L2 (a new life from the shelf's standing version, never a revival). `202 {held, level, class: "consequential", name}`; a rung the ladder does not allow refuses in words (`400`). |
| `GET /seats` | The promoted agents' seats — `{seats[]: {name, template, at_path, state, version, by, since, changed_at}, ladder: [active, rested, decommissioned]}` — where each life stands and its rung. |
| `GET /wear` · `GET /wear?component=&kind=` · `GET /wear?did=` | The wear table — which body wears which craft at which version: `{wear[]: {body, did, life, component, kind, version, hash, since, scope}, counts}`; one craft's wearers (`{component, worn_by[], words}`); one body's wear (`{did, wears[]: {component, kind, version, hash, since}}`). |
| `GET /keychecks` | THE KEY-CHECK — the proofs the kernel asks of its seated bodies on a cadence, the fifty newest and the tally: `{keychecks[]: {check_id, name, did, asked_at, answered_at, ok, words, verified_at}, tally: {checked, failed, pending, last, cadence}, words}`. |
| `GET /services` · `POST /services` | The shelf — `{services[]: {name, kind, did, state, manifest, manifest_hash, last_health, placement, by, marker}, kinds, ground}` — and register (an MCP server: `action: register, name, locator, secrets_with`). |
| `POST /services/check` · `/version` · `/retire` · `/restore` · `/mcp` | One service by `{name}`; retire holds at the interlock. |
| `GET /minds` · `POST /minds` | The Stable — `{minds[], assignments[], gateway: {base, ready}}` — and register: `{action: "register", name, provider, model, …}` → `{class: "consequential", held: ask_…, level: "L2"}`, then confirm. |
| `POST /minds/assign {subject, stall, klass?}` · `/unassign` · `/refill {name, usd}` · `/check` · `/retire` · `/restore` | Held at the interlock where consequential. |
| `GET /minds/spend` · `GET /minds/search` | The meter by body and mind (`{rows, usd, usd_today}`); the market searched by words, class, ceiling price, modality. |
| `GET /minds/fuel?name=` | One body's fuel gauge — `{name, fuel: {max_usd, renew_days, drained_at, refills, spend, renews_at}}`; `fuel` is null for a body with no key of its own. No body of that name joined here: `404`. |
| `GET /schedules/:runner` · `POST /schedules` · `POST /schedules/rest` | A body's duties in three lists — `{human[], role[], kernel[]}`, each `{schedule_id, text, every_s, next_at, editable, …}` — add one, rest one. |

**The monitor, the levers and the Analyzer**

| Door | Shape |
|---|---|
| `GET /monitor` | `{values: {the fifteen metrics}, watches[], bodies, asks, waiting, benches, outbox, parked, topic_depth, doors[], pool, stable, harness, home}`. |
| `POST /watches/rest {name}` | A watch rested on a recorded row. |
| `POST /harness/run {template}` · `POST /harness/ab` | Run the golden cases now; an A/B of model arms. |
| `GET /parked` · `POST /parked/advance` *(governing)* | The events the dispatcher holds at — `{parked[], held, consumer}` — and the word to go past one. |
| `GET /levers` | The lever catalogue — `{levers[]: {name, description, needs, consequence, for, doors, settles_s}, door, served[]}`. |
| `GET /intentions` · `POST /intentions/stop` · `POST /intentions/restart` | Every intention — `{intention_id, words, serves, kind, interests, planner, runner, active, objectives, observations, turns, last_outcome, session, stopped_at, …}` — and its grave stop and restart. |
| `GET /analyzer` · `GET /analyzer?origin=` | Origins with counts by kind, or one origin's tree. |
| `GET /markers` · `GET /markers/kinds` · `POST /markers/kinds` · `POST /mark` | The lineage; the registry — `{kinds[]: {kind, group, description, declared_by}}` — declare a kind; set a marker on what you are executing. |
| `GET /world` · `POST /world/rehome {to_cell}` *(governing)* | The world card — `{scope, cell, epoch, homed, kernel, namespace, peers[], door, opened_at, rehomed_at, rehomed_by}` — and the re-home, held at the interlock. |
| `POST /peers/forget {name}` *(governing)* | A peer let go. |
| `GET /proof` · `GET /shadow` | The proof ladder's state; the shadow of the other kernel on the same ground. |
| `GET /measurements` | THE OPERATING STATE's five, measured live — `{measurements: {trust, recall, efficiency, experience, cost}, target: 1.0, latency_classes: {chat: 30, work: 180, event: 180}, order[]}`, each measurement `{value, num, den, words}`; `value` is null and `words` say *unknown* while there is nothing to measure — never a silent 1.0. |
| `GET /levels` · `GET /levels/context?path=` | THE PATH — every level of this universe, root first: `{universe, mode: dev｜prod, levels[]: {path, level: universe｜floor｜room, mode, declares, here: {bodies, asks_served, usd}, rolled: {bodies, asks_served, usd, bundle}, …}}` — what stands at each level and what rolls up from within it; and the cascade at a path (the universe when unsaid) — the law folded root to leaf, each tier's soft settings, skills and floors. A path reads `u:‹universe›`, `u:‹universe›/f:‹floor›` or `u:‹universe›/f:‹floor›/r:‹room›`; one not open here `404`. |
| `POST /levels/open {parent?, level, name, mode?, experiment?, declares?, session?}` *(governing)* | A floor or room opened under its parent (the universe when unsaid). The laws are checked now — the grammar, the mode tightened only (dev to prod, never back), an experiment room only where one may stand, not already open — and a refusal is immediate, in words (`400`); then the act is held at L2: `202 {held, level: "L2", class: "consequential", path}`. |

**Governing doors** — the owner's or a master's seat: the desk's yes (`join.admit`), `/bodies/restart`,
`/bodies/rest` · `/decommission` · `/restore`, `/world/rehome`, `/peers/forget`, `/parked/advance`,
`/levels/open`, the shelf's and the Stable's changes, and in the Studio the cut (`/drafts/cut`), the
one word to work (`/benches/:name/work`) and an experiment's promotion or decline. A plain person's
seat at one of these wears the proof's face.

## The Studio's doors (a seat)

The Studio is where an agent is made; [its own pages](/studio/the-studio/) say it in full. Every door
here is under your seat: a draft and a bench are yours and no one else's, and saving, moving or
letting them go is routine. Three acts here are a governing seat's and hold at the interlock for
your Yes — the cut, the one word to work, and the promotion.

**Drafts and the cut**

| Door | Shape |
|---|---|
| `GET /drafts` | Your own drafts — `{drafts[]: {draft_id, person, kind, name, body, words, from_marker, at, updated_at, bench}, person, kinds}`. The seven kinds of craft: template · prompt · skill · policy · graph · binding · golden. |
| `POST /drafts {kind, name, body, words?, draft_id?, bench?}` · `POST /drafts/discard {draft_id}` | A draft saved (`201 {draft}` — routine, no fact; `body` is the declaration as an object; `draft_id` saves over one of yours; `bench` files it on a bench, else it is loose); one let go (`200 {discarded: true}`; not yours `404`). |
| `POST /drafts/cut {draft_id, session?}` *(governing)* | THE CUT — a draft onto the shelf, registered or as the next version, held at the level its class demands: `202 {held, level, class: "consequential", shelf_name, verb, version, gate: "shelf"}`. A prompt, skill, policy, graph, binding, golden set or firmware template cuts at L2; a resident's template at L3, your code; firmware only in a dev universe. An **agent's** template never cuts straight onto the shelf — its cut opens the Experiment instead (`gate: "experiment"`, L2, with the `room` and the golden `cases`). |

**Benches**

| Door | Shape |
|---|---|
| `GET /benches` · `GET /benches/:name` | Your benches, the open ones first, each whole — `{benches[]: {bench_id, person, name, words, step, body, hold, state: open｜closed, at, updated_at, closed_at, drafts[], experiments[], seat}, person, steps}`; one by name, or `404`. The steps of the making: name · graph · golden · save · cut · card · promote · joined. |
| `POST /benches {name, words?}` · `POST /benches/:name {step?, body?, hold?, words?}` · `POST /benches/:name/close {reason?}` | Open a bench (`201 {bench}` — or the open one of that name handed back); keep its place (`200 {bench}`; `hold: ""` clears the hold it waits on); let the effort go (`200` — its drafts discarded, its open experiment declined, the bench closed; what reached the shelf stays). All routine, under your seat — except that letting go a bench whose experiment is still running or proposed is a governing seat's act (`403`). |
| `POST /benches/:name/work {session?}` *(governing)* | ONE WORD TO WORK — one hold for the whole chain. The kernel reads the bench against the shelf in order (every prompt and skill the graph names, the graph, the golden set, the template): a changed draft is a cut as the next version, the same bytes a line — *stands — unchanged, skipped*. `202 {held, level: "L2", class: "consequential", lines[], cuts[]}`; the bench moves to the step `cut` holding that ask. On your Yes the cuts run in one transaction, each its own fact, and the Experiment opens on the agent's own cut. A missing draft, an unchanged template, an experiment already running, or a second filing while the hold still waits — refused in words before any hold (`400`). |

**Experiments, the replay and the map**

| Door | Shape |
|---|---|
| `GET /experiments` · `?agent=` · `?state=` · `?id=` | This universe's experiments, newest first — `{experiments[]: {experiment_id, person, agent, template, current_version, candidate: {hash}, state, leaning, room, opened_at, proposed_at, settled_at, …}, seats[], reviewers: [grader, critic, security, identity]}`; one whole by id with its signed verdicts (`{experiment, verdicts[]: {verdict_id, by, by_name, reviewer, ask, verdict, words, sig, at}}`), or `404`. |
| `POST /experiments/promote {experiment_id, at?, session?}` *(governing)* | The stamped promotion of a proposed experiment, held at L2 for an agent (a resident's template at L3, your code): `202 {held, level, class: "consequential", agent, version, at}`. `at` is where the next life stands — unsaid, where the agent stands now, else the universe; the level must be open; an experiment room is refused. A running or settled experiment refuses in words (`400`). |
| `POST /experiments/decline {experiment_id, reason?}` *(governing)* | Your no — routine, recorded: `200 {experiment_id, state: "declined", words}`. The draft stays under your seat to fix; the room stands. One already promoted or declined refuses in words. |
| `GET /hops?ask=` · `GET /hops?run=&case=` | THE REPLAY — every hop a compiled graph took, in the order they began, by the ask it served or by a harness run and its case: `{hops[]: {ref, run, case, agent, source, node, ns[], step, at, took_ms, ok, in_hash, out_hash}}`. Neither named: an empty list. |
| `GET /map` | HOW THE KERNEL WORKS — the kernel's own map of itself, a declaration in the same graph model the Studio draws an agent with (`format: "orreth-map/1"`: `{title, words, entry, nodes, edges, kept_by, version}`), with this kernel's live numbers under `live: {kernel, version, schema, doors, topics, tables}`. |

## Two knocks, end to end

The ceremony and the first ask, exactly as this book walked them:

```bash
curl -s -X POST localhost:4600/enroll -H 'content-type: application/json' -d '{"person":"stranger"}'
# → {"person":"did:orreth:person:stranger","secret":"R4OF…","uri":"otpauth://totp/Orreth:stranger?…","qr":"data:image/png;base64,…","re_enrolled":false}
curl -s -X POST localhost:4600/enroll/confirm -H 'content-type: application/json' -d '{"person":"stranger","code":"123456"}'
# → {"enrolled":true,"person":"did:orreth:person:stranger"}
curl -s -X POST localhost:4600/seat -H 'content-type: application/json' -d '{"person":"stranger","code":"654321"}'
# → {"role":"owner","owner":true,"seat_id":"seat_067f…","wire":"eyJhdWRp…","expiry":"…","words":"you hold this ground now, stranger — …"}

W=eyJhdWRp…   # the wire
curl -s -X POST localhost:4600/ask -H "authorization: Bearer $W" -H 'content-type: application/json' -d '{"text":"echo, say the word HERON once"}'
# → {"ids":["ask_0e6b1f4134d76743"]}
curl -s localhost:4600/asks -H "authorization: Bearer $W"
# → {"asks":[{"ask_id":"ask_0e6b…","status":"replied","target":"echo","served_by":"did:orreth:agent:7a0f…","replied_at":"…"}]}
```
