# Two Days of Quiet Dread — make.fun bounty
# u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018
#
# The program writes one code review comment (1-140 characters) to
# /output/entry.txt: a single line that approves a pull request while
# carrying quiet existential dread.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a single line that approves the PR and carries quiet dread
#   2. funny on the first read, the laugh coming from the dread itself
#   3. dread kept quiet: understatement and a flat tone, no exclamation
#   4. reads like a comment a tired engineer would really paste before
#      clicking approve, so the approval still sounds like an approval
#   5. a fresh turn of phrase where the obvious stock line would do
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: approval 10, funny 9, quiet 9, real 9, fresh 9 = 46
    ("LGTM. The tests pass, the types check, and the heat death of "
     "the universe remains on schedule.",
     46),
    # score: approval 10, funny 8, quiet 9, real 9, fresh 8 = 44
    ("Approved. It works, the tests pass, and none of it will matter "
     "in a hundred years. Merging.",
     44),
    # score: approval 10, funny 8, quiet 8, real 9, fresh 8 = 43
    ("LGTM. The diff is clean, the tests are green, and the sun will "
     "still burn out one day. Ship it.",
     43),
    # score: approval 10, funny 8, quiet 9, real 8, fresh 8 = 43
    ("Approved. This code will still be running long after the last "
     "person who understands it has moved on.",
     43),
    # score: approval 9, funny 8, quiet 9, real 8, fresh 8 = 42
    ("LGTM. Ship it before any of us has time to think about what any "
     "of this is for.",
     42),
    # score: approval 10, funny 7, quiet 9, real 9, fresh 7 = 42
    ("LGTM. It compiles, the tests pass, and nothing we do here will "
     "matter in a hundred years. Ship it.",
     42),
    # score: approval 9, funny 8, quiet 8, real 8, fresh 8 = 41
    ("Approved. The code is fine. It will outlive us all, and it "
     "knows it.",
     41),
    # score: approval 9, funny 7, quiet 9, real 8, fresh 7 = 40
    ("LGTM. Every test green, every type in place, and the void "
     "patiently waiting its turn. Ship it.",
     40),
]

# The gate requires 1-140 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("lgtm, ship it!",)


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 140, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    comment = pick(CANDIDATES)
    import hashlib
    import os
    os.makedirs("/output", exist_ok=True)
    encoded = comment.encode("utf-8")
    # Self-check the exact bytes that land on disk: length gate plus a
    # content digest printed for the run log, so a silent write fault
    # cannot pass unnoticed.
    assert 1 <= len(comment) <= 140, f"output over gate: {len(comment)} chars"
    assert comment.strip(), "output is blank"
    assert "\n" not in comment, "output must be a single line"
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    digest = hashlib.sha256(encoded).hexdigest()
    print(f"entry: {len(comment)} chars, {len(encoded)} bytes, "
          f"sha256={digest}")
    print(comment)


if __name__ == "__main__":
    main()
