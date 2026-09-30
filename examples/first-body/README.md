# first-body — a stranger's body at the join desk

The working proof behind [Seat your own body](https://docs.orreth.ai/build/your-own-body/):
a template that declares a body, and a script that walks it through the kernel's five-status
join desk — asked and challenged, proved by its own key, staged for the owner's yes in the chat,
then a lease with the fuel clause. Walked against `ghcr.io/iotlodge/orrethd:0.1.0` on 2026-09-30.

| File | Role |
|---|---|
| `scout.v0.json` | The template: name, nature, persona, the graph it runs, what it may do. Its content hash rides the join. |
| `knock.py` | The body's side of the desk, using the kernel repository's own `orreth_spine.desk` — the same bytes the crew signs. |

The body's side of the desk lives in the kernel's repository today (`spine/orreth_spine`), not
on PyPI; the script imports it from there. Serving asks needs the rails reachable, not only the
door — see the page for what stands and what is owed.
