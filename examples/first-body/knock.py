# PROVENANCE: Claude Fable 5.1 (claude-fable-5-1) — THE REFRESH SEASON step 2, the book for kernel 0.1.0 · 2026-09-30
"""A stranger's body at the kernel's join desk — the road a body walks to be admitted.

Run it from the kernel repository's spine, whose package holds the body's side of the desk:

    cd orreth/spine && uv sync
    ORRETH_HOME=~/.orreth-scout .venv/bin/python3 ../../orreth-docs/examples/first-body/knock.py http://127.0.0.1:4600

It asks (and is challenged), proves the key behind its DID, waits for a governing seat's yes —
the hold appears in the chat of the world you named — and collects its lease. Run it twice: the
second time the same self is admitted at once on its standing welcome, with no hold at all.
"""
import json, os, sys
from pathlib import Path
from orreth_spine import desk, identity, envelope

door = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:4600"
here = Path(__file__).resolve().parent
template = json.loads((here / "scout.v0.json").read_text())
policy_path = Path(os.environ.get("ORRETH_POLICY", Path(desk.__file__).resolve().parent.parent / "policy" / "covenant-policy.v1.json"))
policy = json.loads(policy_path.read_text())                     # no policy, no join — the covenant is worn, not remembered

me = identity.Identity.load(template["name"], os.environ.get("ORRETH_HOME", str(Path.home() / ".orreth")))
print(f"I am {me.did} — the same self every run (the seed stays under ORRETH_HOME)")

lease = desk.knock(door, me, name=template["name"], kind="resident",
                   template_hash=envelope.content_hash(template),
                   policy_hash=envelope.content_hash(policy),
                   wait_s=600, poll_s=1.0, say=lambda words: print("  ·", words))
if lease is None:
    print("the door turned this body away, or nobody answered in ten minutes")
    sys.exit(1)
print(f"admitted: {lease['admitted_by']}")
print(f"lease {lease['lease_id']} until {lease['expiry']}")
print("the fuel clause:", json.dumps(lease["lease"]["constraints"]["budget"]))
print("grants:", json.dumps(lease["lease"]["grants"]))
