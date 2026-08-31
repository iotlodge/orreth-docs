# PROVENANCE: Fable 5 (claude-fable-5) — 0064 The Open Book, the first world · 2026-08-31
"""Mint (or reuse) your world's root keypair.

Orreth's kernel verifies signatures and cannot create them — so a world's
root of trust is a keypair YOU hold. This script keeps the private half in
`.root-seed` (created once, reused forever — your world's identity survives
restarts) and hands only the PUBLIC half to the containers via `.env`.

Run it with uv (no install needed):
    uv run --with cryptography python mint_root.py
"""
import base64
import pathlib

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import (
    Encoding, NoEncryption, PrivateFormat, PublicFormat,
)

HERE = pathlib.Path(__file__).resolve().parent
SEED = HERE / ".root-seed"

if SEED.exists():
    key = Ed25519PrivateKey.from_private_bytes(SEED.read_bytes())
    print("· reusing the existing root seed (.root-seed) — same world, same identity")
else:
    key = Ed25519PrivateKey.generate()
    SEED.write_bytes(key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption()))
    SEED.chmod(0o600)
    print("· minted a new root seed → .root-seed (keep it; it IS your world's root identity)")

raw = key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
pub = "z" + base64.urlsafe_b64encode(raw).decode().rstrip("=")

(HERE / ".env").write_text(f"ORRETH_ROOT_PUB={pub}\n")
print(f"· public key → .env for compose: ORRETH_ROOT_PUB={pub[:16]}…")
print("· next: docker compose up -d")
