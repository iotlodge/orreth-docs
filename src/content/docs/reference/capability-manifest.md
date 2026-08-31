---
title: The capability manifest
description: Reference for the capability declaration contract — the genesis file, every manifest field, and the thirteen panel kinds the console renders blind.
---

A capability declares itself in one file — `capabilities/<folder>/genesis.py`
— exporting two module-level names. This page is the contract. (Tutorial:
[Build your first capability](/build/first-capability/).)

## The genesis contract

| Export | Type | Meaning |
|---|---|---|
| `CRAFT` | `dict[str, str]` | The world's words, keyed `<world>-<domain>-<role>`. Planted on the governed shelf at first discovery: versioned, human-editable through the console, acquired by agents by reference. Optional. |
| `MANIFEST` | `dict` | The declaration below. Required — a folder without a valid one is skipped, loudly. |

Discovery rules, enforced by the machine:

- The genesis is **import-executed** at the agentic layer's boot; an
  exception skips the capability and the sweep carries on.
- A manifest missing `key`, `name`, or `view` — or using a panel kind
  outside the canon vocabulary — is **refused with the flaw named**.
- **Crew commands execute from the genesis file only.** The shelf's
  human-editable copy of a manifest never runs a command; the repository is
  the trust boundary for code.
- The shelf outranks the folder: once discovered, a world's declaration is
  a record. Removing the folder leaves the world `declared` with its genesis
  marked absent; retirement is a governed act through its tile.

## Manifest fields

**Required:**

| Field | Meaning |
|---|---|
| `key` | The world's stable id — folder-independent, used in records and doors |
| `name` | Display name on the tile and room header |
| `view` | The room, as an ordered list of typed panels (below) |

**The card** (all optional, all rendered on the tile/header):

| Field | Meaning |
|---|---|
| `emoji` | The tile's mark |
| `resident` | The staff member who fronts this world in captions and asks |
| `floor` / `port` | The floor whose records the panels read, and its kernel port |
| `law` | One sentence under the name — say what the world may **not** do |
| `door` | URL-hash route for the world's room (defaults to `key`) |
| `group` | Groups tiles in the portal ("the Trading Desks") |

**Behavior** (all optional):

| Field | Meaning |
|---|---|
| `crew` | Agent processes the machine launches from this genesis: `{name, cmd, cwd, log, match, shared?}` — `match` is the aliveness probe; `shared` marks one process serving several worlds |
| `floors` | Floors this world asks the machine to grow, e.g. `{scope, shared?}` — growing is a governed act at the human's gate |
| `tools` | Tools the world brings to the tool registry: `{name, kind, endpoint, transport}` — the registry's gate still holds the word |
| `verbs` | The request kinds the world's buttons file, e.g. `{words_kind: "desk-watch"}` |
| `collection` | How the world's records are labeled/indexed, e.g. `{label: ["ticker","date"]}` |

## The thirteen panel kinds

Panels render **per record** of the world's collection, blind — the console
never loads a capability's own JavaScript, so the vocabulary is closed.
Using a kind outside it is refused at discovery ("changing what the glass
can render is a RELEASE, not an edit").

| Kind | Declares | Renders |
|---|---|---|
| `controls` | `inputs: [{id, placeholder, pattern, transform}]`, `buttons: [{label, request, note}]`, `watches?` | The ask card — inputs plus buttons that file governed requests (`$input` substitution in the request body) |
| `reports` | `(collection)` | The record index as a pill row — a row opens its record's detail panels on demand |
| `stat` | `fields: [{src, style?: pill\|price\|pending, label?, title?}]` | The hero line of headline values |
| `markdown` | `src` | A record field as rendered Markdown |
| `doc` | `src` | Same as `markdown` (long-document intent) |
| `tabs` | `tabs: [{key, label, src}]` | Tabbed Markdown views over record fields |
| `strip` | `src, text, title` | A compact ✓-dot progress strip from a list field |
| `flow` | `src, nodes: [{id, kind, desc}], edges?, label?` | A declared DAG drawn by the console, each node lighting as its record lands |
| `list` | `src` | A bulleted list from a list field |
| `bars` | `src` → `[{label, value}]` | Horizontal magnitude bars |
| `table` | `src, columns: [{key, label}]` | A sortable table from a list-of-objects field |
| `chart` | `preset` | A named chart preset (currently `market`); unknown presets confess |
| `download` | `label, href` (`$field` substitution) | A download link for the record's artifact bundle |

A world with no records yet shows its `controls` panels and says
`no report yet` — honesty is the default state.

## The SDK's side

`pip install orreth-agent` ships `orreth_agent.manifest(...)` — a builder
that raises on out-of-vocabulary panel kinds at authoring time — and
`orreth_agent.PANEL_KINDS`, the same closed set the machine enforces at
discovery. Genesis files themselves are typically plain dict literals (they
execute inside the machine's own environment); the builder serves crew-side
code and CI checks.
