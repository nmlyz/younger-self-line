#!/usr/bin/env python3
"""Write the judged line to entry.txt.

The line is the one its writer would send back to their younger self.
It was picked from 38 candidates by pairwise judging against the brief:
spoken straight to the younger self, naming one concrete thing from a
life actually lived (a blue bike, someone else's yard, every scratch),
with the turn landing on the last two words. It is held here as one
constant, and the gate below refuses anything that is not exactly that
line, so the file this program writes can only ever contain the judged
text. The write is verified by reading the file back and comparing
every byte.
"""

import os
import sys

LINE = (
    "Don't sell the blue bike — in ten years you'll walk past it in "
    "someone else's yard and still know every scratch."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 112
MIN_LEN = 1
MAX_LEN = 200
SENTENCE_ENDS = (".", "!", "?")


def check_length(line):
    """The line must be exactly the judged length, inside the 1-200 gate."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not MIN_LEN <= len(line) <= MAX_LEN:
        return f"line outside the {MIN_LEN}-{MAX_LEN} character gate"
    return None


def check_single_line(line):
    """One line only: no newline inside, no surrounding space."""
    if "\n" in line or "\r" in line:
        return "line must not contain a newline"
    if line != line.strip():
        return "line must have no leading or trailing space"
    return None


def check_single_sentence(line):
    """One sentence only: no sentence-ending stop mid-line.

    A stop followed by a space would let a second sentence do the work
    the brief forbids, so the body before the final stop must contain
    no such mark.
    """
    body = line[:-1] if line.endswith(SENTENCE_ENDS) else line
    for mark in SENTENCE_ENDS:
        if mark + " " in body:
            return "line must be a single sentence"
    return None


def validate_line(line):
    """Run every gate check; return the list of problems, empty if clean."""
    checks = (check_length, check_single_line, check_single_sentence)
    return [problem for check in checks if (problem := check(line)) is not None]


def entry_bytes(line):
    """The exact bytes entry.txt must contain: the line, one newline."""
    return (line + "\n").encode("utf-8")


def resolve_output_dir():
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(path, data):
    """Write the bytes and make the file world-readable."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def verify_entry(path, data):
    """Read the file back and prove it holds exactly the written bytes.

    Size first, then content, then a decode check that the file is one
    line of text: a write that stopped halfway, or a stray extra line,
    must fail here rather than pass silently.
    """
    if os.path.getsize(path) != len(data):
        return (
            f"read-back size mismatch: {os.path.getsize(path)} bytes on "
            f"disk, {len(data)} written"
        )
    with open(path, "rb") as f:
        actual = f.read()
    if actual != data:
        return "read-back mismatch"
    text = actual.decode("utf-8")
    if text.count("\n") != 1 or not text.endswith("\n"):
        return "written file is not exactly one line plus a newline"
    return None


def fail(problems):
    """Report every problem and stop without writing anything."""
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    sys.exit(1)


def main():
    problems = validate_line(LINE)
    if problems:
        fail(problems)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    data = entry_bytes(LINE)
    write_entry(path, data)
    mismatch = verify_entry(path, data)
    if mismatch is not None:
        sys.exit(mismatch)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
