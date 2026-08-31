---
title: Build your first world
description: A complete two-tier Orreth universe from three small files — two JSON profiles and a compose file — against the published kernel image.
---

The [anatomy page](/learn/anatomy/) makes a claim worth testing: **the
topology is data.** No tier of an Orreth deployment is hard-coded anywhere —
a universe is simply the engine program started with universe-shaped
settings (a small JSON file called a profile), and a floor is the *same
program* started with floor-shaped settings and told who its parent is. This page proves it: you will build a brand-new world named
`u:first` from three small files, without cloning anything.

Everything below is a worked, tested example — it lives at
[`examples/first-world`](https://github.com/iotlodge/orreth-docs/tree/main/examples/first-world)
in this site's own repository, and this page is kept true to it.

## What you need

Docker, [uv](https://docs.astral.sh/uv/), and the published kernel image
`ghcr.io/iotlodge/orrethd` — about a 40 MB pull.

## 1. Mint your root of trust

An Orreth world's root of trust is a keypair **you** hold — the kernel
verifies signatures and cannot create them, so it must be *told* its root's
public key at start and can never invent one. Grab the example folder (or
recreate its four files from this page) and mint:

```bash
uv run --with cryptography python mint_root.py
# · minted a new root seed → .root-seed (keep it; it IS your world's root identity)
# · public key → .env for compose: ORRETH_ROOT_PUB=z8iOefpX…
# · next: docker compose up -d
```

That's what you'll see, and it means: the script generated a keypair, kept
the private half in `.root-seed` right beside it (yours — created once,
reused on every future run), and wrote the public half into `.env`, where
compose hands it to the containers. Your world keeps one identity for life.

## 2. The two profiles — the tiers as data

A **tier profile** is the JSON that turns the one binary into a specific
tier. The universe profile (`profiles/first-universe.json`) says, in
essence:

- *I am scope `u:first`, the top.* Distilled memory keeps **forever**;
  retrieval may reach the whole past.
- *One rule binds everyone under me:* records of failure are kept raw for 90
  days — "failures always survive." Rules like this cascade **down** to
  every child, and children can only tighten them, never loosen.
- *My root of trust is `did:web:example.com:u:first`* — the name whose
  public key you just minted. (Nothing needs to be served at that address;
  the name is pinned to the key you supply.)

The floor profile (`profiles/first-floor.json`) differs only where a
workroom should differ: scope `u:first/f:main`, a 90-day working memory, a
90-day retrieval horizon. Same shape, different dials — that *is* the tier
system.

## 3. One compose file, one image, two tiers

The compose file runs the same image twice (plus Postgres, so the world's
memory survives restarts):

```yaml
  universe:
    image: ghcr.io/iotlodge/orrethd:0.63.465
    command: >
      --profile /profiles/first-universe.json --port 4600 --bind 0.0.0.0
      --store-dir /data/bodies --root-pub ${ORRETH_ROOT_PUB}
      --pg postgres://postgres:orreth@pg:5432/postgres

  floor-main:
    image: ghcr.io/iotlodge/orrethd:0.63.465
    command: >
      --profile /profiles/first-floor.json --port 4601 --bind 0.0.0.0
      --parent http://universe:4600
      --store-dir /data/bodies --root-pub ${ORRETH_ROOT_PUB}
      --pg postgres://postgres:orreth@pg:5432/postgres
```

The **only** structural difference between the two services is the profile
they mount and one flag: `--parent`. That flag is the whole join story — at
boot the floor pulls its parent's rules down from `/standards`, and every
five seconds it beats its presence up to `/hello`.

```bash
docker compose up -d
```

## 4. Prove it

```bash
curl localhost:4600/health
# {"scope":"u:first","records":0,...}        — your universe

curl localhost:4601/health
# {"scope":"u:first/f:main","records":0,...} — your floor

curl localhost:4600/topology
# {"scope":"u:first","children":[{"scope":"u:first/f:main",...}]}
#                                 ^ the floor, present under its parent

curl localhost:4600/standards
# ..."failures always survive — the apex floor, pulled by every child"...
#    ^ the rule your floor pulled down at boot
```

And the console is already there — every kernel serves it:

```
open http://localhost:4600/window
```

## What you just built — and what it isn't yet

You built the **substrate**: a governed, append-only, identity-checked
record fabric with a console, in your own topology. It is honest about what
it doesn't have: no agents live here yet, and the model registry is
keyless, so anything that would need to think refuses cleanly rather than
pretending. Several console rooms belong to the agentic layer and will say
so.

Growing it is more of the same data: a third tier is one more profile and
five compose lines. An ecosystem between universe and floor is a profile
with scope `u:first/e:something` and two `--parent` edits.

Giving the world *purposes* is the next page in this track:
[build your first capability](/build/first-capability/) — and the SDK for
giving it *minds* is published:
[`pip install orreth-agent`](https://pypi.org/project/orreth-agent/).
