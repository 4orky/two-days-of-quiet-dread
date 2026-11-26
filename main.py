#!/usr/bin/env python3
# Two Days of Quiet Dread — a one-line review comment for the make.fun bounty
# bounty slug: u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018
# This script drafts several original single-line pull-request approvals,
# scores each one by hand against five craft measures, keeps the best,
# and writes it to /output/entry.txt as UTF-8 without a trailing newline.
# The five measures, in the order the brief weights them:
#   a genuine green light: the line must read as a real approval first
#   hushed dread: the unease stays quiet, flat, almost an afterthought
#   a first-read laugh: the humour comes from the dread, not a punchline
#   a reviewer's voice: it sounds typed by someone tired, before approve
#   a fresh image: an unexpected turn where the stock phrase would sit
# Every draft below was written for this bounty; the grading is fixed and
# deterministic, so the same line wins on every run, byte for byte.
from hashlib import sha256
from pathlib import Path
DRAFTS = [
    (("LGTM. The tests pass, ", "the types check, and the heat death ", "of the universe remains on schedule."), 46),
    (("Approved. The suite is green, ", "the types line up, and entropy ", "is still on the calendar."), 43),
    (("LGTM. Clean diff, green tests, ", "and the sun has an expiry date ", "anyway. Merging."), 42),
    (("Ship it. The tests pass, the types check, ", "and none of this outlives ", "the heat death."), 41),
    (("Approved. Everything passes, everything type-checks, ", "and the universe is still ", "winding down."), 40),]
FORBIDDEN = ("ship it!", "lgtm!")
def join(parts):
    return "".join(parts)
def vet(line):
    if not line.strip():
        raise ValueError("draft is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("draft must stay on one line")
    if not 1 <= len(line) <= 140:
        raise ValueError("draft breaks the 1-140 character gate: %d" % len(line))
    lowered = line.lower()
    for bad in FORBIDDEN:
        if bad in lowered:
            raise ValueError("draft carries a banned stock phrase")
def emit():
    champion = ""
    champion_key = None
    for parts, points in DRAFTS:
        line = join(parts)
        vet(line)
        key = (points, -len(line))
        if champion_key is None or key > champion_key:
            champion_key = key
            champion = line
    vet(champion)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = champion.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(payload)
    print("wrote %d chars, %d bytes, sha256=%s" % (len(champion), len(payload), sha256(payload).hexdigest()))
    print(champion)
if __name__.endswith("__main__"):
    emit()
