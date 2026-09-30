---
title: Seat your own body
description: Admit an agent you wrote through the kernel's join desk — challenged, proved by its own key, staged for your yes, then a lease with the fuel clause. Walked against 0.1.0 before it was written.
---

Orreth does not replace your agent framework; it gives your agent an institution to live in. Every
body in a world — the crew's ten and yours — enters through the same five-status desk and lives
under the same laws. This page walks a stranger's body through that desk on a fresh 0.1.0 world.
Everything below is its real output.

## What a body is

A body is a process the kernel governs: born from a **template**, wearing the **covenant policy**,
joined through the **desk** as the same self every life, thinking only through the **gateway**,
serving asks and duties on its **benches**, and emitting its **journey** so nothing it does is
unseen. The template is a small JSON file:

```json
{
  "format": "orreth-resident-template/1",
  "name": "scout",
  "version": "0.1.0",
  "nature": "a stranger's body, joining from outside",
  "persona": "a visitor — the body proven before the mind arrives",
  "graph": "echo.v0",
  "capabilities": ["ask"]
}
```

`graph` names the loop the body runs (`echo.v0` needs no mind; `mind.v0` thinks through the
gateway), `capabilities` what it may do (`ask`, and `tools:‹name›` for each tool it declares),
and a firmware body adds `"kind": "firmware"` and a `function`. The
[crew reference](/reference/the-crew/) has every field.

## 1. The knock

The body's side of the desk lives in the kernel repository's `orreth_spine` package today (it is
not yet on PyPI — see the boundary below). The script in
[`examples/first-body`](https://github.com/iotlodge/orreth-docs/tree/main/examples/first-body)
loads the template and the policy, loads (or mints, once) the body's own keypair, and knocks:

```bash
cd orreth/spine && uv sync
ORRETH_HOME=~/.orreth-scout .venv/bin/python3 ../../orreth-docs/examples/first-body/knock.py http://127.0.0.1:4600
```

```
I am did:orreth:agent:fcf0ced5577fb116985d51c24384bea4 — the same self every run (the seed stays under ORRETH_HOME)
  · scout proved its key — waiting at the door for a governing seat's yes
```

Three things happened in that second: `POST /join` asked with the DID, the public key that
derives it, the template's content hash and the policy's; the desk answered with its own nonce;
`POST /join/prove` sent the body's signature over that nonce. A forged proof would have been
denied with the one face, *join refused*. A proven stranger is **staged**.

## 2. The hold, in the chat

In the glass of that world a hold appears, with Cancel as the default:

> scout (a resident) asks to join this world — its key is proven, its template 9b79546f. A yes
> gives it a LEASE for 30 days: its own words on …

The desk itself (say **who is at the door?**, or `GET /join`) reads:

```json
{"id": "join_0a1b6f15fde9", "name": "scout", "kind": "resident", "status": "staged",
 "did": "did:orreth:agent:fcf0ced5577fb116985d51c24384bea4",
 "template_hash": "sha256:9b79546fbfcd22aa6ce6754829c307f0b6ca9852b6851bfdcb2ed2fda5dd618a",
 "words": "scout proved its key — the door waits for a governing seat's yes"}
```

Only a governing seat — the owner or a master — can click Yes; a plain person's seat wears the
one face. A hold nobody answers in fifteen minutes is denied and recorded. Click Yes (through the
door: `POST /confirm {"ask_id": "…", "approve": true}` → `{"approve": true, "level": "L2"}`).

## 3. The lease

The script, which was polling the join's status, collects the lease with the same key it proved:

```
admitted: admitted on stranger's word
lease seat_… until 2026-10-30T16:07:42.402Z
the fuel clause: {"cost": 1.0, "renew_days": 1}
grants: [{"action": "retrieve", "space": "self"}, {"action": "write", "space": "self"}]
```

The lease is a capability token chained to the kernel's root, this world its audience, the body its
subject. It grants the body its own words and nothing more — `retrieve self · write self` — for
thirty days, with a fuel clause of one dollar renewing daily that the gateway enforces. It is a
seat with the role *body*: it opens `POST /delta` (the body's own words) and no person's door.

## 4. The second life

Run the script again:

```
I am did:orreth:agent:fcf0ced5577fb116985d51c24384bea4 — the same self every run
admitted: admitted on its standing welcome (join_0a1b6f15fde9) — the same self, the same world
```

No hold this time. The same key is admitted at once on its **standing welcome** — a self admitted
here before is admitted again in silence. This is the covenant's first rule felt: *a keypair is a
self, and a self survives the process*. Delete `~/.orreth-scout` and you have a new stranger.

## 5. Serving — what stands today, honestly

The desk is the whole front door, and it is proven from outside with nothing but HTTP. Serving
asks is the other half, and today it needs more than the door:

- A body serves from **benches on the invocation rail** and reads the **ground**. So a body must
  reach RabbitMQ, Kafka and Postgres, not only port 4600. On the repository's rig they are on
  localhost; the first-world compose file publishes only the door.
- The whole body — knock, lease, benches, journey, streamed words — is
  `python -m orreth_spine.body --template scout.v0.json` from the kernel's repository, with
  `SPINE_KERNEL_DOOR` naming the kernel. That is exactly the process the kernel runs for each of
  its own ten seats, so it is proven every time a world lights.
- **A published SDK that does all of this from the door alone is owed.** `orreth-agent` 0.4.0 on
  PyPI speaks the first architecture's doors, not this desk. It is named on
  [what works today](/learn/what-works-today/); when it lands, this page changes with it.

## 6. What your body is under, from its first breath

- **It wears the covenant.** No policy loaded, no join, ever; the join records the policy version
  worn, and the CREW pull shows it on the card.
- **It thinks on the meter.** Every thought goes through the gateway under the body's own virtual
  key, within its fuel clause; a drained body says so and a refill holds for a person's yes.
- **It never grades its own yardstick.** A verdict on its work is signed by another body.
- **Its consequential acts hold.** A tool declared consequential holds at the interlock; a grave
  one asks for a person's code and a master's click.
- **It can be stopped, parked and restarted by a person**, and every one of those is a recorded
  fact — never a deletion.
