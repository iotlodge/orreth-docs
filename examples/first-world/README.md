# first-world — a stranger's first Orreth world

The working proof behind the [quickstart](https://docs.orreth.ai/build/quickstart/) and
[Your first world](https://docs.orreth.ai/build/first-world/): the published kernel
`ghcr.io/iotlodge/orrethd:0.1.0` and the four boxes it stands on, from one compose file.
Walked on 2026-09-30; the docs pages and this folder are kept true to each other.

```bash
docker compose up -d           # ground · invoke · events · gateway, then the kernel and its crew
curl localhost:4600/health     # {"kernel":"rust","version":"0.1.0",...}
open http://localhost:4600     # the glass: enroll, take your seat, say "tour"
docker compose down            # sleep; keep the ground and the selves
docker compose down -v         # forget the world
```

| File | Role |
|---|---|
| `compose.yaml` | The five services, the dials the kernel reads, the two volumes that keep the world (the ground's data and the selves' seeds). |
| `ground-init.sql` | One line: the gateway's own ledger database on the ground, made at the first start. |
| `gateway-config.yaml` | The gateway's starting model list — the kernel's default mind by name, its key by environment name only. A fresh gateway needs a list before the kernel can add to it. |

Provider keys ride in from your shell or a `.env` beside the compose file (`ANTHROPIC_API_KEY`,
`OPENROUTER_API_KEY`, `OPENAI_API_KEY`); the values reach the gateway, the names reach the kernel,
and neither lands in any record or file of Orreth's. Without a key the world stands and the crew
say honestly that no mind stands; add one from the chat (Ollama on your machine works).

The image is `linux/arm64`. To run beside the kernel repository's own rig, which holds port 4600,
start with `ORRETH_PORT=4700 docker compose up -d`.
