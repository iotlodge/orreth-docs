#!/usr/bin/env python3
# PROVENANCE: Fable 5 (claude-fable-5) — 0064 The Open Book, the docs site · 2026-08-31
"""docs.orreth.ai CDK application — the Orreth documentation (static Starlight build).

Build the site first:
    npm run build          # from the repo root → dist/

Deploy (CloudFront URL only):
    cdk deploy
Deploy on docs.orreth.ai (zone must exist in the account):
    cdk deploy -c docs_domain=docs.orreth.ai -c orreth_zone_id=ZXXXX \
               -c orreth_zone_name=orreth.ai
"""
from pathlib import Path

import aws_cdk as cdk

from stacks.orreth_docs_stack import OrrethDocsStack

app = cdk.App()

site_dir = str((Path(__file__).resolve().parents[2] / "dist"))

OrrethDocsStack(
    app,
    "OrrethDocsStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account") or "824106896658",
        region=app.node.try_get_context("region") or "us-east-1",
    ),
    site_dir=site_dir,
    docs_domain=app.node.try_get_context("docs_domain"),
    zone_id=app.node.try_get_context("orreth_zone_id"),
    zone_name=app.node.try_get_context("orreth_zone_name"),
)

app.synth()
