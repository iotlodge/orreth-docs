# joined-agent — a LangGraph agent living in an Orreth world

The working proof behind
[Bring your own agent](https://docs.orreth.ai/build/bring-your-own-agent/):
an ordinary LangGraph agent, run from outside the Orreth repository with
two published packages, that joins a governed world through its front gate,
keeps one identity for life, and files signed memory it finds again on its
next run.

```bash
# against a running Orreth (see the quickstart):
uv run --with orreth-agent --with langgraph python agent.py \
    --field http://127.0.0.1:4502

# first run: JoinRefused — the admission STAGED at the human's gate.
# approve it once in the console's Inbox, then run again (and again):
# same DID every run · admitted on your standing welcome ·
# each life recalls the records the previous lives filed.
```

Orreth touches the graph only at the edges — `join()`, `recall()`,
`remember()`, `diary()`. The framework is swappable; the institution stays.
