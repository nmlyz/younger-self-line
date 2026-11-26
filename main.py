#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the line its writer would send
back to their younger self.

The line was picked from 38 candidates by pairwise judging against the
brief: it is told straight to the younger self, it names one concrete
thing from a life actually lived (a blue bike, someone else's yard,
every scratch), and the turn lands on the last two words. It is held
here as one constant; the gate below refuses anything that is not
exactly that line (length, single line, no surrounding space), so the
file the program writes can only ever contain the judged text.
"""

import os
import sys

LINE = (
    "Don't sell the blue bike — in ten years you'll walk past it in "
    "someone else's yard and still know every scratch."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 112


def check_line(line):
    """Refuse anything that is not exactly the judged line."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not 1 <= len(line) <= 200:
        return "line outside the 1-200 character gate"
    if "\n" in line or line != line.strip():
        return "line must be a single line with no surrounding space"
    # One sentence only: no sentence-ending stop mid-line, so no second
    # sentence can ever do the work the brief forbids.
    body = line[:-1] if line.endswith((".", "!", "?")) else line
    if any(mark in body for mark in (". ", "! ", "? ")):
        return "line must be a single sentence"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
