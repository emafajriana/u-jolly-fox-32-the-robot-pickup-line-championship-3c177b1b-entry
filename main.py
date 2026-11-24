"""The Robot Pickup Line Championship entry (Python 3.13, standard library only).

Writes one pickup line, in the voice of a robot, to entry.txt in the
output directory, then reads it back and verifies it in full.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path

LINE = (
    "My obstacle sensors detect nothing ahead \u2014 except you, "
    "and I have never once tried to avoid you."
)

MAX_CHARS = 200


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def write_entry() -> Path:
    """Write the line, then read it back and verify it in full."""
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(f"line is {len(LINE)} chars, must be 1..{MAX_CHARS}")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("line must be a single line with no padding")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(LINE.encode("utf-8"))
    written = target.read_bytes()
    if written != LINE.encode("utf-8"):
        raise IOError("read-back bytes do not match the line")
    if written.endswith(b"\n"):
        raise IOError("entry must not end with a newline")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
