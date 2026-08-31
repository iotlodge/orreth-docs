# orreth-docs — the documentation for Orreth

The source of [docs.orreth.ai](https://docs.orreth.ai): how to **use** and
**build with** [Orreth](https://github.com/iotlodge/orreth), a governed
runtime for agentic systems.

Orreth is two elements — a small kernel binary (`orrethd`) that keeps a
signed, append-only record of everything with identity, permissions, and
metering enforced at one door; and **capabilities**, the purposes built on top
of it. These docs teach both, in plain engineering language, with the
machine's own vocabulary shown as labels. A captured moment of a live
universe is public at [demo.orreth.ai](https://demo.orreth.ai).

## Why this repo exists (and why it is separate)

This repo is the permanent home of Orreth's user- and builder-facing
documentation, chartered as design dive **0064 — The Open Book** in the main
repository. It is deliberately *outside* the main repo because the docs are
written by a rule called **docs-driven decoupling**: each tutorial page is
written as if Orreth's packages already existed, and every step that proves
impossible from outside the monorepo names a seam to cut — publish the kernel
image, publish the SDK, give the capability manifest a real schema. Each cut
seam ships together with the page that proves it. The example worlds in this
repo must consume Orreth the way a stranger would, or the docs would be
theater.

## Layout

```
src/content/docs/    the pages (Starlight / Astro, Markdown + MDX)
  index.mdx          What is Orreth — the landing page
  learn/             the Learn track (anatomy · what-works-today · glossary)
src/data/
  glossary.json      the machine's own 36-term dictionary, vendored from the
                     main repo's site/fixtures/sentences.json (gloss key) —
                     refresh it from there, never edit it here
infra/cdk/           the deploy stack: S3 (private, OAC) + CloudFront + ACM
                     on docs.orreth.ai, mirroring the demo site's stack
examples/            (arrives with the Build track) worlds and capabilities
                     that consume Orreth from outside — the decoupling proofs
```

## Working on the docs

```bash
npm install
npm run dev        # local preview at localhost:4321
npm run build      # static build into dist/
```

Voice rules (locked 2026-08-31, dive 0064):

1. **Plain-first.** Pages lead with engineering terms; the machine's names
   appear as product labels — "the tool registry (shown in the console as
   **the Farm**)" — never the reverse.
2. **The glossary is the bridge.** A canon word is introduced at first use
   with its plain meaning; the glossary page is generated from the vendored
   dictionary, one source of truth with the live console.
3. **Only claim what is proven.** The what-works-today page mirrors the main
   repo's honest-boundary register; a claim without evidence named is a claim
   these docs do not make.
4. **The sidebar only lists pages that exist.** No stub pages, no "coming
   soon" links.

## Deploying

```bash
npm run build
cd infra/cdk
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
export TMPDIR="$HOME/.orreth/tmp"   # macOS: jsii needs a writable tmp
PATH=".venv/bin:$PATH" npx aws-cdk@latest deploy \
  -c docs_domain=docs.orreth.ai \
  -c orreth_zone_id=<zone-id> -c orreth_zone_name=orreth.ai
```

Run `diff` before `deploy`. The stack is the smallest possible surface — a
private S3 bucket behind CloudFront with an origin-access control; no compute,
no origin to probe.

## Licensing

- Documentation prose: **CC BY 4.0** (`LICENSE`)
- Example code and infrastructure: **MIT** (`LICENSE-CODE`)

## Provenance

Authored by Claude (Fable 5) working with Jonathan Barth, under the main
repository's provenance discipline. The documentation's claims are grounded in
three code-verified survey reports (2026-08-31) and the main repo's standing
registers.
