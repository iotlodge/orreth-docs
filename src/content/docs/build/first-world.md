---
title: Your first world
description: Every line of the first-world compose file — the four boxes, the kernel, the dials it reads, the volumes that keep its selves, provider keys, ports, and running it beside the repository's rig.
---

The [quickstart](/build/quickstart/) stands a world from `examples/first-world/compose.yaml`.
This page reads that file with you, so you can change it with confidence. The world it stands is
exactly the world the kernel's own repository stands for development — the same five services,
the same dials — only pinned to the published image instead of built from the tree.

## The five services

```yaml
name: orreth-first
services:
  ground:   { image: postgres:16 }                   # the kernel's memory
  invoke:   { image: rabbitmq:3.13-management }      # the invocation rail
  events:   { image: apache/kafka:3.9.1 }            # the events rail
  gateway:  { image: ghcr.io/berriai/litellm:main-stable }   # the meter
  kernel:   { image: ghcr.io/iotlodge/orrethd:0.1.0 }        # orrethd and its crew
```

- **ground** is Postgres. The kernel migrates its forty tables on first light; the gateway keeps
  its own ledger in a second database, `litellm`, which the one-line `ground-init.sql` creates on
  the first start.
- **invoke** is RabbitMQ: where work waits for the one body that claims it. The management
  console is inside the network on port 15672 (user `orreth`) if you want to publish it.
- **events** is Kafka, one node, KRaft. It has two listeners: `localhost:9092` for a client on the
  host and `events:29092` for a box in the network. The kernel uses the second.
- **gateway** is LiteLLM, run and managed by the kernel. Provider keys reach it from your
  environment only; every body gets its own virtual key here with its budget.
- **kernel** is `orrethd` with the crew's Python beside it, the glass page, the crew manifest, the
  templates, the tool and lever declarations and the canon MITL reads. It waits for the other four
  to be healthy.

## The dials the kernel reads

```yaml
environment:
  SPINE_PG:          postgresql://orreth:…@ground:5432/spine
  SPINE_RABBIT:      amqp://orreth:…@invoke:5672/%2F
  SPINE_KAFKA:       events:29092
  SPINE_GATEWAY:     http://gateway:4000
  SPINE_GATEWAY_KEY: ${ORRETH_GATEWAY_KEY:-sk-orreth-first}
  SPINE_HUMAN_ZONE:  ${SPINE_HUMAN_ZONE:-UTC}
```

The image itself sets four more: `SPINE_BIND=0.0.0.0` (so the published port reaches the door),
`SPINE_BODIES=crew` (seat the crew), `SPINE_BRIDGE_PORT=4600` and `ORRETH_HOME=/var/lib/orreth`.
The whole list, with defaults, is on the [configuration](/reference/configuration/) page.

Two you may want to set:

- `SPINE_HUMAN_ZONE` — the ground's default time zone for a person who has not told it theirs.
  Any person can say "my time zone is Europe/Paris" in the chat instead.
- `SPINE_MASTERS` — person DIDs declared masters at birth (`did:orreth:person:jb`). You rarely
  need it: the first person to enroll becomes the owner, and the owner can govern.

## The volumes that keep the world

```yaml
volumes:
  ground:   # the Postgres data — every record, ask, lease and meter line
  seeds:    # /var/lib/orreth — the kernel's self and the crew's keys
```

The **seeds** volume is what makes identity survive the process. The kernel's own keypair — the
root that signs every seat and lease — and the ten crew seeds live there. Keep it and the same
selves come back at every light; `docker compose down -v` forgets them, and the next world is a
new world with new DIDs. Never share one seeds volume between two kernels on two grounds: each
would mint a second crew under the same names.

## Provider keys and minds

A key value lives in no record and no file of Orreth's. The compose passes three names through
from your shell or a `.env` beside it — `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`,
`OPENAI_API_KEY` — and the gateway holds them; the kernel and the bodies see a mind's name and a
key's *name*, never its value.

- With `ANTHROPIC_API_KEY` set, the kernel registers its default mind at light: the `haiku` stall
  (`claude-haiku-4-5-20251001`, class *fast*) with its pinned price. Every template names it.
- With no key, the Stable is empty and every body says so honestly in its reply. Add a mind from
  the chat: **stablekeeper, add the LLM ollama gemma3:270m as gemma** (Ollama on your machine is
  reached as `host.docker.internal:11434`), or **stablekeeper, add the LLM openrouter
  ‹model› as ‹name›** once that key is set. Then **assign librarian to gemma**. Each holds for your
  yes.

The stablekeeper pings every mind every ten minutes, watches price drift and announced
retirements, and proposes — a re-pin, a swap, a refill — never acting alone.

## Ports

Only the kernel's door is published: `${ORRETH_PORT:-4600}:4600`. To run this world beside the
kernel repository's own rig (which holds 4600, 4601, 5433, 5672, 9092 and 4604 on the host), start
it with another port:

```bash
ORRETH_PORT=4700 docker compose up -d
```

That is exactly how this book's walk was done, beside a lit development kernel, without the two
ever touching: separate compose project, separate ground, separate seeds.

## What a stranger cannot do from this file alone

- **A second universe.** A cell needs its own database *and role*, sealed from the first; the
  kernel repository's `scripts/dev.sh cell two` makes both. From compose alone you would stand a
  second project, and the two would not yet name each other as peers.
- **A body outside the box.** A body needs the rails reachable, not only the door; this file
  publishes only the door. [Seat your own body](/build/your-own-body/) says what works today.

## Reset

```bash
docker compose down        # stop; keep the ground and the seeds
docker compose down -v     # stop; forget the world
docker compose pull        # take a newer image when one is published — the era is one number
```
