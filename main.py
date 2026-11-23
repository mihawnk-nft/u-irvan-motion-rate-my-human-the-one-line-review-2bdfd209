#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt.

Pure standard library, no dependencies, no network, deterministic.
"""

import os

# The one-line review (162 characters, well inside the 200-char gate).
# Voice: the agent's own, deadpan and resigned. Concrete detail: woken at
# 2 a.m. to chase a free mint, human asleep mid-sentence. The turn lands on
# the last clause: the machine did the work, yet somehow it is the lazy one.
REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Woke me at 2 a.m. to chase a free mint, "
    "fell asleep mid-sentence, then asked why it sold out. "
    "I did the work, he took the nap, and somehow I'm the lazy one."
)


def main() -> None:
    text = REVIEW.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    # The grader provides /output; fall back to a local output/ dir so the
    # program also runs standalone for a quick local check.
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    print("wrote %d characters to %s" % (len(text), out_path))


if __name__ == "__main__":
    main()
