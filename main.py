#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry program.

Writes a single line of plain text to /output/entry.txt: one funny
one-line joke about office life, under 200 characters.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I told HR I was burning out, so they scheduled a wellness meeting "
    "at 7 a.m. on a Monday — with the manager who burned me out."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: what was written must be byte-identical to ENTRY.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 199, "entry must be 1-199 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert "\n" not in written, "entry must be a single line"
    assert written == written.strip(), "entry must not have leading/trailing whitespace"


if __name__ == "__main__":
    main()
