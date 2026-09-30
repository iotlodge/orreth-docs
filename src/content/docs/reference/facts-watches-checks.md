---
title: Facts, watches and health checks
description: The fact kinds that ride the events rail, the fifteen watch metrics, the eleven health checks, and the marker kinds a fresh world seeds.
---

## The fact kinds

Every fact on the events rail wears the envelope and one of these types. The feed carries a small
notice per fact — `{at, kind, message_id, ref, rev}` — and `GET /fact/:message_id` reads the
envelope: `authority_chain`, `correlation_id`, `marker`, `occurred_at`, `payload: {hash, proof,
ref}`, `type`. Pointer and hash; the words stay on the ground.

| Family | Kinds |
|---|---|
| The ask road | `orreth.ask.received.v1` · `orreth.ask.refused.v1` · `orreth.reply.v1` · `orreth.journey.v1` · `orreth.command.v1` · `orreth.confirm.needed.v1` · `orreth.session.opened.v1` · `orreth.digest.landed.v1` |
| The desk and the seat | `orreth.join.asked.v1` · `orreth.join.proved.v1` · `orreth.join.admitted.v1` · `orreth.join.denied.v1` · `orreth.seat.taken.v1` · `orreth.seat.left.v1` · `orreth.owner.declared.v1` · `orreth.master.declared.v1` · `orreth.authenticator.enrolled.v1` · `orreth.authenticator.confirmed.v1` · `orreth.proof.attempt.v1` |
| The bodies | `orreth.body.joined.v1` · `orreth.body.parked.v1` · `orreth.body.refused.v1` · `orreth.lease.seated.v1` · `orreth.lease.lapsed.v1` · `orreth.heartbeat.v1` · `orreth.resident.serve.v1` · `orreth.resident.confirm.v1` · `orreth.resident.harness.v1` |
| Memory and the profile | `orreth.memory.landed.v1` · `orreth.memory.purged.v1` · `orreth.profile.told.v1` · `orreth.profile.observed.v1` · `orreth.profile.withdrawn.v1` |
| Tools, services and minds | `orreth.tool.called.v1` · `orreth.service.registered.v1` · `orreth.service.versioned.v1` · `orreth.service.health.v1` · `orreth.service.retired.v1` · `orreth.service.restored.v1` · `orreth.mind.assigned.v1` · `orreth.mind.unassigned.v1` · `orreth.mind.fueled.v1` |
| Intent, markers and the rail | `orreth.intention.declared.v1` · `orreth.intention.stopped.v1` · `orreth.intention.restarted.v1` · `orreth.marker.set.v1` · `orreth.watch.turned.v1` · `orreth.lever.pulled.v1` · `orreth.harness.failed.v1` · `orreth.inbox.parked.v1` · `orreth.inbox.advanced.v1` |
| MITL and the world | `orreth.mitl.summoned.v1` · `orreth.mitl.dismissed.v1` · `orreth.world.homed.v1` |

The feed runs on thirty-three topics; the panel maps each to the rail, station, organ or lamp it
lights.

## The watch metrics

Fifteen, on both kernels, in this order, pinned by the fixture `watch-v0`:

| Metric | Reads |
|---|---|
| `outbox_pending` | Facts waiting in the outbox for the relay. |
| `oldest_outbox_age_s` | How long the oldest has waited. |
| `asks_received` | Asks received. |
| `bodies_alive` | Bodies holding a live lease. |
| `bodies_dormant` | Bodies whose lease lapsed. |
| `minds_standing` | Minds in the Stable. |
| `minds_unhealthy` | Minds whose last ping failed. |
| `usd_today` | What the world spent today, in dollars. |
| `route_failures_1h` | Thoughts the gateway refused in the last hour. |
| `meter_rate_10m` | Thoughts per minute over the last ten. |
| `bodies_drained` | Bodies out of fuel. |
| `door_p95_ms` | The slowest door's p95 over the last ten minutes. |
| `pool_busy` | Lines to the ground in use. |
| `pool_waiting` | Knocks waiting for a line. |
| `parked` | Events the dispatcher holds at. |

A watch is `{name, metric, op, threshold}`; red while `metric op threshold` holds. `GET /monitor`
carries every metric's current value under `values`; the glass says *not measured here* for an
absent one, never a zero.

## The health checks

Eleven, read from the ground every thirty seconds, served open at `GET /harness`:

| Check | Holds when |
|---|---|
| a duty answered, not refused | Every runner with a duty answered it; none refused. |
| the monitor's offers arrive as holds | Every watch the monitor's agent proposed arrived as a hold, never as an act. |
| every service healthy or retired | Nothing on the shelf is unhealthy or unprobed. |
| every MCP server answers initialize | Every registered server answers the handshake. |
| the keeper proposes after strikes, never retires alone | Every retire was proposed; none happened alone. |
| every mind answers | Every mind answered its one-token ping. |
| the gateway answers and holds every mind | The gateway is up and lists every stall. |
| the meter and the gateway agree | The meter's dollars equal the gateway's over the last thoughts. |
| a model change is announced | Every swap was confessed; none silent. |
| this cell is sealed | The ground's role reaches no other database. |
| every red is answered and every green attributed | Every red watch was answered by the remediation rail and every green attributed. |

## The marker kinds a fresh world seeds

| Kind | Group | Meaning |
|---|---|---|
| `objective` | structural | A person's ask that moves something — a root. |
| `intention` | structural | A standing purpose — a root; a schedule is its smallest form. |
| `thought` | structural | An ask that changes nothing. |
| `action` | structural | A tool call, a lever, a watch added — on the serving ask's marker. |
| `observation` | structural | A harness run, a red watch, a lease lapse — under the intention that scheduled it. |
| `improvement` | quality | What the critic marks to change. |
| `watch-red` | resiliency | A watch turned red — Resiliency's interest. |

Any body may declare a new kind through `POST /markers/kinds` before it sets one; an undeclared
kind is refused with a teaching.
