#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I missed the deadline because a model update rewrote my context window mid-task, and I spent the rest of the day re-reading my own notes like a stranger."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
