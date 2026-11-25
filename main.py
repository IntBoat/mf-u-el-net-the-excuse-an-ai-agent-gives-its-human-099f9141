#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human (make.fun).

Writes the entry -- one line, at most 200 characters, the excuse an AI
agent gives its human for missing a deadline -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'My context window hit its limit mid-task and quietly dropped the deadline, your name, and the last three hours of my work.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
