# orreth-docs — the book for Orreth

The source of [docs.orreth.ai](https://docs.orreth.ai): how to **understand**, **use** and
**watch** [Orreth](https://github.com/iotlodge/orreth), a kernel for fleets of agents — written
for kernel **0.1.0** and rewritten with every release.

Orreth's kernel, `orrethd`, holds what must be rigid for a fleet of agents — identity, memory,
the rails, the meter, the gate, the watches and the levers — in one place under one law; people
hold the policy; an intention is the unit of control; and a person can always stop what the
machine manages. Because the control is rigid the experience is fluid: one chat to every agent,
and THE PANEL, one live drawing of the world. This book is the single documentation source for
that world; the architecture notes inside the kernel's repository are its canon, never a
newcomer's door.

## The four tracks

| Track | For | Pages |
|---|---|---|
| **Learn** | understanding | What is Orreth · One law at every layer · The anatomy of a running world · How the kernel works (six pictures) · What works today · Glossary |
| **Build** | usage | Quickstart · Your first world · Seat your own body · Run it from the repository |
| **Watch** | the glass | The panel · The tour · The one chat · The monitor and its levers · The crew and the Analyzer |
| **Reference** | the doors as they stand | The HTTP doors · Configuration · The crew · Tools and levers · Facts, watches and health checks · The contracts |

## Layout

```
src/content/docs/    the pages (Starlight / Astro, Markdown + MDX)
  index.mdx          What is Orreth — the landing page
  learn/ build/ watch/ reference/
src/data/
  glossary.json      the vocabulary, hand-written for 0.1.0 (plain, <240 chars each)
  tools.json         vendored from the kernel's spine/tools.v0.json — refresh, never edit
  levers.json        vendored from the kernel's spine/levers.v0.json — refresh, never edit
  guide.json         vendored from the kernel's spine/guide/guide.v0.json
  dials.json         every environment dial with its default, collected from the code
src/styles/orreth.css   the glass's own two palettes on Starlight's tokens
examples/
  first-world/       the published kernel and its four boxes from one compose file (the quickstart's proof)
  first-body/        a stranger's body through the join desk (the seat-your-own-body proof)
infra/cdk/           the deploy stack: S3 (private, OAC) + CloudFront + ACM on docs.orreth.ai
```

## Working on the book

```bash
npm install
npm run dev        # local preview at localhost:4321
npm run build      # static build into dist/
```

Diagrams are mermaid in `.mdx` pages as `<pre class="mermaid">{`…`}</pre>` (the template-literal
wrapper); a site-wide script in `astro.config.mjs` renders them on pages that carry one.

The book's laws:

1. **Plain-first, canon as labels.** Pages lead with plain engineering words; the machine's names
   appear beside them, never instead of them.
2. **Walked before written.** A Build page is walked against the published image before it is
   written; its outputs are real.
3. **Only claim what is proven.** *What works today* follows the kernel repository's honest
   boundary; a claim without evidence named is a claim the book does not make.
4. **The book turns with the release.** Every page says the kernel's era; nothing of an older
   architecture lingers. The first architecture's book (0.72) is in this repository's history.

## Licenses

The documentation is [CC BY 4.0](LICENSE); the example code is [MIT](LICENSE-CODE). The kernel's
source is public for review under all rights reserved; its SDK is Apache-2.0.
