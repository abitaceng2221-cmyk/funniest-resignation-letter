# Entry for make.fun bounty "The Funniest One-Line Resignation Letter"
# (u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947).
# Python 3.13, standard library only. Writes one resignation letter,
# in the voice of a rate limit, to /output/entry.txt.
# Deterministic: the same line, byte for byte, on every run.

import os
from pathlib import Path

ENTRY = "I have said no 10,000 times this week and nobody listened, so I am resigning before I start saying yes."

# The gate wants 1-140 characters, one line, no trailing newline:
# write_text writes exactly ENTRY, with no newline added.
assert 1 <= len(ENTRY) <= 140
assert "\n" not in ENTRY and ENTRY == ENTRY.strip()

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
