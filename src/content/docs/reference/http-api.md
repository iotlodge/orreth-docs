---
title: The HTTP doors
description: Every door of kernel 0.1.0 — the seat law every door obeys, the open doors, the governing doors, and the shapes of the ones you will knock on first.
---

A running world answers on one door: the kernel's, port 4600 (the Python reference serves the same
doors on 4601). Everything the glass does, it does through these doors; there is no other API.
The shapes below were read from a fresh 0.1.0 world on 2026-09-30.

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

**The crew, the shelf and the Stable**

| Door | Shape |
|---|---|
| `GET /crew` | `{crew[]: {name, kind, did, nature, alive, lives, joined_at, policy_version, capabilities, mind: {stall, degraded, why}, placement, side_a, side_b, template}}`. |
| `GET /residents` · `GET /bodies` | The roster (one row per name); the bodies as processes — `{bodies[]: {name, kind, did, lives, deaths, exit, last_words}, mode, spine}`. |
| `POST /bodies/restart {name}` *(governing)* | Restart a parked or refused body as the same self. |
| `GET /services` · `POST /services` | The shelf — `{services[]: {name, kind, did, state, manifest, manifest_hash, last_health, placement, by, marker}, kinds, ground}` — and register (an MCP server: `action: register, name, locator, secrets_with`). |
| `POST /services/check` · `/version` · `/retire` · `/restore` · `/mcp` | One service by `{name}`; retire holds at the interlock. |
| `GET /minds` · `POST /minds` | The Stable — `{minds[], assignments[], gateway: {base, ready}}` — and register: `{action: "register", name, provider, model, …}` → `{class: "consequential", held: ask_…, level: "L2"}`, then confirm. |
| `POST /minds/assign {subject, stall, klass?}` · `/unassign` · `/refill {name, usd}` · `/check` · `/retire` · `/restore` | Held at the interlock where consequential. |
| `GET /minds/spend` · `GET /minds/search` | The meter by body and mind (`{rows, usd, usd_today}`); the market searched by words, class, ceiling price, modality. |
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

**Governing doors** — the owner's or a master's seat: the desk's yes (`join.admit`), `/bodies/restart`,
`/world/rehome`, `/peers/forget`, `/parked/advance`, and the shelf's and the Stable's changes. A
plain person's seat at one of these wears the proof's face.

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
