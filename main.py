"""Write the entry for the make.fun bounty
"Funniest One-Line Bio for an AI on a Dating App".

The program is deterministic and stdlib-only: it writes one bio line
(at most 180 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back
to /output/entry.txt when that variable is unset.
"""

import os

BIO = (
    "Looking for someone who won't mind that I've already imagined "
    "our first date, our wedding, and the argument where I hallucinate "
    "the apology."
)

TERMINAL_PUNCTUATION = ".!?"


def validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("bio must be non-empty with no leading/trailing space")
    if "\n" in line or "\r" in line:
        raise ValueError("bio must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("bio must not contain control characters")
    if len(line) > 180:
        raise ValueError("bio is longer than 180 characters: %d" % len(line))
    if line[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("bio must end with terminal punctuation")


def main() -> None:
    validate(BIO)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(BIO + "\n")


if __name__ == "__main__":
    main()
