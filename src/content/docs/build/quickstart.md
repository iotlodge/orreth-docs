---
title: "Quickstart: a running world in ten minutes"
description: The published kernel 0.1.0 and the four boxes it stands on, from one compose file — then enroll, take your seat, and say “tour”.
---

This gets you from nothing to a **running Orreth world with the glass in your browser**: the
kernel `orrethd` and its crew of ten, standing on Postgres, RabbitMQ, Kafka and a LiteLLM
gateway, all in Docker, from one compose file pinned to the published image
`ghcr.io/iotlodge/orrethd:0.1.0`. Every step below was walked against that image on 2026-09-30;
the outputs are real.

## What you need

- **Docker Desktop** (or Docker Engine with Compose), running, with about 4 GB free for images.
- **An arm64 machine** — an Apple Silicon Mac or an arm64 Linux box. The 0.1.0 image is
  `linux/arm64` only; amd64 is owed and named on [what works today](/learn/what-works-today/).
- **An authenticator app** on your phone (any TOTP app) — your seat is a code it shows.
- Optionally, **an Anthropic API key**. Without one the world still stands: echo answers, the
  tour walks, the panel lights; the librarian's mind waits until you add a mind.

## 1. Get the two files and start

```bash
git clone https://github.com/iotlodge/orreth-docs.git
cd orreth-docs/examples/first-world
docker compose up -d
```

The folder holds a compose file and a one-line SQL file that gives the gateway its own ledger
database on the ground. If you have an Anthropic key, put it in a `.env` beside the compose file
first (`ANTHROPIC_API_KEY=…`); a key value lives in no record and no file of Orreth's — it reaches
the gateway from your environment only.

Compose pulls five images and starts them in order: the ground, the two rails and the gateway
first, then the kernel once all four are healthy. The first pull takes a few minutes; every start
after that takes about thirty seconds.

## 2. The kernel is up

```bash
curl -s localhost:4600/health
```

```json
{"clients":0,"kernel":"rust","lit_at":"2026-09-30T16:03:11.557Z","rev":129,
 "schema":{"found":0,"ground":3,"kernel":3,"migrated":true},"version":"0.1.0"}
```

`version` is the era, 0.1.0. `schema.migrated: true` says this kernel found an empty ground and
laid down the forty tables itself; the next time it lights it will find them and only verify. In
the kernel's log you can watch the crew take their seats:

```bash
docker compose logs kernel | grep alive
```

```
[echo] echo is alive: did:orreth:agent:7a0f68327c405450c642481fd31c7090 · life 1 · resident · every mind through the gateway at http://gateway:4000 · words to http://127.0.0.1:4600
[librarian] librarian is alive: did:orreth:agent:72c878dbd7f9c34c25d39f2577eadd36 · life 1 · resident · …
[planner] planner is alive: … · life 1 · firmware (plan) · …
```

Ten bodies, each its own process the kernel spawned and governs, each admitted through the
join desk on the crew manifest, each holding a lease for thirty days. Every one of those DIDs is a
permanent self: stop the world and start it again, and the same DIDs come back at *life 2*.

## 3. Take your seat

Open **http://localhost:4600**. You will see the glass — the ceiling, THE PANEL in the middle,
the sill beneath it — and, because nobody holds this ground yet, the seat form asking for a name.

1. Type a name and press **Enroll**. A QR code appears; scan it with your authenticator.
2. Type the six-digit code it shows. That first code finishes enrolling you.
3. Type the next code and press **Take my seat**.

The kernel answers:

> you hold this ground now, stranger — the first to prove an authenticator here is its owner · your
> seat is the owner's for 24 hours; say “leave my seat” to end it sooner

Your seat is a capability token the kernel signed, carried on every knock the page makes. Every
door reads who you are from it, never from the page. You are the owner: from now on only you or a
master you declare can enroll another person.

## 4. Say “tour”

Type **tour** in the chat. A soft amber line draws itself around one part of the live panel at a
time, with a card in plain words beside it — what it is, what to try — while the world keeps
moving underneath. Sixteen steps; ← → to move; Esc leaves. The [Watch track](/watch/the-tour/)
has every step on paper.

## 5. Ask the crew

Ask echo, and read the road an ask takes:

> **echo, say the word HERON once**

Echo replies with your words, whole, and the soft line under the ask says the journey: *echo:
heard the ask, every word · echo: recalled nothing yet — a young memory · echo: echoed every word —
none summarized away*. On the panel the rails lit toward echo's station and faded; on the tape a
new line says who asked, who answered, and how long it took (about 80 ms).

Now ask the librarian, who needs a mind:

> **librarian, what is the temperature outside?**

Without a mind in the Stable the librarian says so, honestly:

> I cannot think right now — no LLM stands in the Stable — add one ("stablekeeper, add the LLM
> ollama gemma3:270m as gemma").

There are two ways to give the crew a mind, and both are governed:

- **A provider key.** Put `ANTHROPIC_API_KEY=…` in `.env` and `docker compose up -d` again. At
  light the kernel registers its default mind, Claude Haiku, as a stall in the Stable and an
  entry in the gateway, and probes it; every body then thinks through it under its own key with a
  fuel clause of one dollar a day. (The key's value reaches the gateway; its *name* reaches the
  kernel, which registers a mind only when the name is reachable where it stands.)
- **A mind on your machine.** Run [Ollama](https://ollama.com) with a model pulled and say
  **stablekeeper, add the LLM ollama gemma3:270m as gemma**, then **assign librarian to gemma**.
  Each is consequential: it holds in the chat with Cancel as the default until you click Yes, and
  lands as a recorded fact. On the walk behind this page the gateway answered gemma's one-token
  ping through the meter within a minute, and the librarian's next thought rode it — the journey
  read *thought it through the metered gateway*. A 270-million-parameter model proves the road,
  not the answer: it handed back the weather tool's schema instead of calling it. Pull something
  larger for real answers.

Then tell the ground where you are — **I live in Boulder, Colorado** (your own town) — and ask the
temperature again; the weather tool reads your place, never a fixed one.

## 6. Let the kernel take the lead

The kernel's own Resiliency intention is already standing in every world — read it in the
ANALYZER (lift the floor) or say **what is this world doing?**:

> keep this world resilient: when a watch goes red, get it green

Open the MONITOR pull (say **open the monitor**). Its cards read the operating state live: the
pulse, the minds, the eleven health checks, the rails, every body, the watches, the harness. On a
fresh world two checks read BROKEN with their reason — *every mind answers* and *every service
healthy or retired* — until a mind stands; nothing is hidden.

With the pull open, the monitor's own agent is in the chat. Say **watch for asks left waiting**
or **propose a watch that usd_today > 5**: it proposes the watch with the add-watch tool, and the
proposal holds for your yes. From then on, when that watch turns red, Resiliency wakes: the kernel
reads a dossier off the ground, the planner names one lever from the catalogue, the kernel pulls
it, reads the watch again and writes the outcome on the tape — *cured* with its cause,
*self-healed*, or *still red* and handed to you with the dossier. A routine lever (restart a
parked body) runs at once and you are told; a consequential one still holds for your click. The
[monitor page](/watch/the-monitor/) has the whole rail; the kernel's own proofs park a body and
cure it this way on every change.

## 7. Stop it

```bash
docker compose down        # the world sleeps; its ground and its selves are kept
docker compose down -v     # …and forgets everything, including the crew's identities
```

## Where next

- [Your first world](/build/first-world/) explains every line of the compose file and how to
  run it beside other things.
- [Seat your own body](/build/your-own-body/) admits an agent you wrote through the same desk.
- [The panel](/watch/the-panel/) and [the one chat](/watch/the-one-chat/) teach what you can see
  and say.
