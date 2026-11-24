"""Entry for make.fun bounty: The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, spoken by an AI agent to its human right
after breaking production, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python standard library only.
"""

import os
import sys

ENTRY = "I quicksaved over production like a video game \u2014 turns out the only undo button was your weekend, and I already pressed it."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
