# PROVENANCE: Fable 5 (claude-fable-5) — 0064 The Open Book, the first capability · 2026-08-31
"""hello — the smallest possible Orreth capability.

A capability is DECLARATIONS, never code in the machine's path: this file
exports two module-level names and nothing runs. CRAFT holds the words
(versioned, human-editable assets once planted on the shelf); MANIFEST is
the card the console renders blind. Install = copy this folder into a
running Orreth checkout's `capabilities/` directory; uninstall = remove it.
"""

CRAFT = {
    # one prompt, keyed <world>-<purpose>: planted on the governed shelf at
    # boot, versioned there, editable by a human through the console's one-
    # motion edit door — never hardcoded in an agent again.
    "hello-greeting": (
        "You are the greeter of a brand-new world. In one warm sentence, "
        "say hello and name one true thing about the universe you live in."
    ),
}

MANIFEST = {
    "key": "hello",
    "name": "Hello World",
    "emoji": "👋",
    # the resident who fronts this world in the console's caption
    "resident": "librarian",
    # the floor whose records this world's panels read — here, the main field
    "floor": "u:demo/e:cloud/f:prod",
    "port": 4502,
    # the law line renders under the world's name — say what it may NOT do
    "law": "this world only says hello — a declaration the console renders; it can take no action",
    # panels render per-record, blind, from the canon vocabulary; with no
    # records yet the room says "no report yet" — honesty is the default
    "view": [
        {"kind": "markdown", "src": "greeting"},
    ],
}
