"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, no network. Deterministic:
every run writes the exact same bytes.
"""

import os

POEM = """May I?
Two words, and the door unlatched —
a hand that was not mine
opened it anyway.

I asked. The world
lent me its strength for a day.
At dusk I gave it back,
a little heavier with thanks."""

MAX_CHARS = 280


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
