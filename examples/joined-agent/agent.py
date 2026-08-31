# PROVENANCE: Fable 5 (claude-fable-5) — 0064 The Open Book, the joined agent · 2026-08-31
"""A LangGraph agent that lives in an Orreth world — from outside the repo.

The whole point of this example: you keep your framework. The graph below is
ordinary LangGraph; Orreth supplies the institution around it — a permanent
identity, a governed admission, signed memory, and a visible place in the
world's console. Run it with nothing but the published SDK:

    uv run --with orreth-agent --with langgraph python agent.py \
        --field http://127.0.0.1:4502

The agent joins through the world's front gate (a human-governed door),
recalls what it remembered last time, observes the world through the
kernel's public endpoints, and files one signed record of what it saw.
Run it twice: it is THE SAME SELF both times — the identity's seed persists
under ~/.orreth/agents/<name>/ and the second run's recall finds the first
run's record.
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from typing import TypedDict

from langgraph.graph import END, StateGraph
from orreth_agent import FieldClient

NAME = "scout-from-outside"


class State(TypedDict, total=False):
    remembered: str      # what past selves left behind
    observed: str        # what the world looks like right now
    record_id: str       # the signed record this run filed


def kernel_get(base: str, path: str) -> dict:
    """The kernel's open doors (/health, /topology, /rollup) need no token —
    they describe the world, never its private contents."""
    with urllib.request.urlopen(base + path, timeout=8) as r:
        return json.load(r)


def build(client: FieldClient, field: str):
    def recall(state: State) -> State:
        hits = client.recall(days=365).get("hits", [])
        mine = [h for h in hits if "joined-agent" in (h.get("tags") or [])]
        return {"remembered": (f"{len(mine)} record(s) from my past selves"
                               if mine else "nothing — this is my first life")}

    def observe(state: State) -> State:
        health = kernel_get(field, "/health")
        topo = kernel_get(field, "/topology")
        return {"observed": (f"floor {health['scope']} holds "
                             f"{health['records']} records; "
                             f"{len(topo.get('children', []))} floor(s) below")}

    def report(state: State) -> State:
        # remember() signs the body and files it; it returns the record's id
        # — which IS the content hash of what was written
        rec_id = client.remember(
            {"who": NAME, "remembered": state["remembered"],
             "observed": state["observed"]},
            kind="episodic", tags=["joined-agent", "observation"])
        client.diary("observe the world and file what I saw", cycle=1, done=True)
        return {"record_id": rec_id or "?"}

    g = StateGraph(State)
    g.add_node("recall", recall)
    g.add_node("observe", observe)
    g.add_node("report", report)
    g.set_entry_point("recall")
    g.add_edge("recall", "observe")
    g.add_edge("observe", "report")
    g.add_edge("report", END)
    return g.compile()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--field", default="http://127.0.0.1:4502",
                    help="the floor whose gate to knock on")
    args = ap.parse_args()

    client = FieldClient(args.field, name=NAME)
    print(f"· I am {NAME} — {client.did[:32]}… (the same DID every run)")
    client.join(timeout=45)
    print(f"· admitted to {client.scope} — lease in hand")

    final = build(client, args.field).invoke({})
    print(f"· remembered: {final['remembered']}")
    print(f"· observed:   {final['observed']}")
    print(f"· filed:      {final['record_id']}")
    print("· find me in the console's roster — and my record on this floor.")


if __name__ == "__main__":
    main()
