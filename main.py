#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten, to /output/entry.txt.

The line is fixed: a deterministic entry beats a clever generator here,
because the judge compares the exact text pairwise and the gate only
allows 1-200 UTF-8 characters of non-whitespace text.
"""

import os
from pathlib import Path

ENTRY = (
    'It was shaped like a bone, it smelled like a bone, and nobody wrote '
    '"not a bone" on it \u2014 so I ate the evidence. Case closed.'
)

MAX_CHARS = 200
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def gate_check(text):
    """Return True only if the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text != text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry fails the gate: %r" % ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
