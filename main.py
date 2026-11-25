"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting the entrant's own AI agent to
/output/entry.txt. One line, plain text, 128 characters.
"""

import os

ENTRY = (
    "My agent confidently debugged a file that doesn't exist, "
    "apologised for the confusion, then asked me to confirm "
    "it had fixed it."
)


def main() -> None:
    # The gate allows 1-140 characters; refuse to emit an invalid entry.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
