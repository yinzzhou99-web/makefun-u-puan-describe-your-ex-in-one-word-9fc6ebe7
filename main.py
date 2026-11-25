"""Describe Your Ex in One Word.

Exactly one word, a verdict on an ex: subscription — the one that keeps
renewing itself long after you thought you cancelled. Writes the word to
/output/entry.txt. Standard library only; no network, no third-party
packages.
"""

import io
import os

VERDICT = "subscription"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    handle = io.open(target, "w", encoding="utf-8")
    handle.write(VERDICT)
    handle.flush()
    handle.close()
    # io.open leaves the umask's mode; force 0644 so the scorer can read it.
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
