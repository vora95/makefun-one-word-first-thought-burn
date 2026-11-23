#!/usr/bin/env python3
"""One Word, First Thought — burn entry.

Writes exactly one word to /output/entry.txt: the first word that comes
to mind. No topic, no explanation, no second draft.
"""

import os
import sys

WORD = "goblin"


def main():
    word = WORD
    if not word or any(ch.isspace() for ch in word):
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    try:
        word.encode("ascii")
    except UnicodeEncodeError:
        print("entry must be ASCII", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Read back and verify: exactly one word, byte-identical, no newline.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw != word.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        return 1
    if len(raw) != 6:
        print("unexpected entry size", file=sys.stderr)
        return 1
    print(f"wrote {len(raw)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
