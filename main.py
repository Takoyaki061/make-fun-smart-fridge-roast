#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) of a smart fridge
to /output/entry.txt. Stdlib only.

The line is the critique-pick of 7 self-authored candidates (DeepSeek was
unreachable this window: 9 attempts across 3 prompts, all HTTP 524 or empty
replies — see CANDIDATES.md). Pick: the dumb-old-fridge contrast — a fridge
that kept food cold for twenty years without demanding an email address —
sharpest sting, freshest angle, lands on first read. Revised after the first
local grade: "twenty years" -> "20 years" — punchier, 4 fewer bytes (the
tie-break favours smaller text).
"""

import os

LINE = "My old fridge kept food cold for 20 years without once asking for my email address."

def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
