# first-world — a stranger's first Orreth universe

A complete two-tier Orreth world from **three small files**: two JSON tier
profiles and a compose file, against the published kernel image. This is the
working proof behind the [Build your first world](https://docs.orreth.ai/build/first-world/)
tutorial — the docs page and this folder are kept true to each other.

```bash
uv run --with cryptography python mint_root.py   # once — your root identity
docker compose up -d
curl localhost:4600/health     # {"scope":"u:first", ...}
curl localhost:4601/health     # {"scope":"u:first/f:main", ...}
curl localhost:4600/topology   # the floor, joined under its universe
open http://localhost:4600/window
```

Stop it with `docker compose down` (add `-v` to also forget its memory).

What's in here:

| File | Role |
|---|---|
| `mint_root.py` | Mints your world's root keypair once; the private half stays in `.root-seed` (gitignored, yours), only the public half reaches the containers. The kernel verifies and cannot sign. |
| `profiles/first-universe.json` | The universe tier: scope `u:first`, keeps distilled memory forever, carries the one apex rule every child must honor ("failures always survive"). |
| `profiles/first-floor.json` | A floor tier: scope `u:first/f:main`, 90-day working memory, joined under the universe by one `--parent` flag. |
| `profiles/model-registry.json` | The model classes the gateway would offer — declared but keyless here, so anything that needs to think refuses honestly. |
| `compose.yaml` | One kernel image, two tiers, plus Postgres so the world's memory survives restarts. |

The ports (4600/4601) deliberately avoid the main development rig's range, so
this world can run beside it.
