"""The Funniest Office Joke, Judged Head to Head -- entry v2 (re-submit).

Why this joke, and why it is not the v1 joke
---------------------------------------------
The v1 entry asked IT for a second monitor and got a second meeting
instead: a decent turn, but it scored only 32.02% in round 2
(rank 1,194 of 2,362), the weaker of the two office jokes entered
under this handle. A re-submit has to earn its place by being
clearly funnier and clearly different, so v2 changes the angle
completely: no monitor, no meeting, no IT ticket.

The new angle is the reply-all spiral, the one office accident
everyone has either caused or survived. The brief rewards jokes
that turn on something anyone who has worked in an office knows,
and it names the reply-all explicitly, so the setup starts inside
that shared memory instead of explaining it: the narrator hits
reply-all to ask everyone to stop hitting reply-all. That is the
setup, and it is also the trap -- the very act meant to end the
noise becomes the loudest message in the thread.

The turn then escalates in three beats, each one worse and more
absurd than the last, so the sentence keeps climbing instead of
flattening into a complaint: 214 unread emails (the flood the
narrator tried to stop, now multiplied), a warning from HR (the
institution steps in, and it is not on the narrator's side), and
then the punchline, saved for the very last words -- "somehow a
fan club". The narrator did not just fail to stop the thread; the
thread adopted them. A fan club is the last thing a scolding
reply-all should earn, which is exactly why it lands: the office
does not punish the person who caused the chaos, it celebrates
them, and the narrator is left famous for the one thing they were
trying to kill.

Every word earns its place. "Somehow" does real work: it is the
narrator's bewilderment in a single word, the shrug that admits
they have no idea how a reprimand turned into applause. The
number 214 is specific enough to feel counted rather than
invented -- a round 200 would read as a guess, and a vague
"hundreds" would read as a shrug -- and the three-beat list
(inbox, HR, fan club) gives the line a rhythm that carries the
reader to the final twist. The joke is one sentence, one line,
135 characters, comfortably inside the 1-200 character gate, with
the punchline on the last words, exactly where the brief wants it.

Angles deliberately avoided, so this entry stays fresh against
the handle's other office jokes: the second monitor / second
meeting (v1 of this bounty), the deadline that became yesterday,
the performance review that raised the narrator's blood pressure,
the FINAL_v2 folder, and the automation that added more meetings.
None of those words or premises appear here.

How the program works
---------------------
The joke is a constant, written out in full below. Before anything
is written to disk, :func:`validate_gate` checks it against the
competition gate the same way the sealed scorer will: UTF-8 text,
between 1 and 200 characters, not only whitespace, a single line
(no newline characters anywhere in it), and a punchline that sits
at the end of the line. If any check fails the program exits
non-zero without writing a file, so a broken entry can never be
submitted by accident. On success it creates ``/output`` if
needed and writes the joke to ``/output/entry.txt`` as UTF-8 with
no trailing newline, then fixes the file mode to 0644. Only the
file gets a chmod; the output directory is never chmodded, so the
sandbox keeps whatever permissions it was given.
"""

import os
import sys

# The entry: one line about office life, setup then turn, punchline last.
# 135 characters, single line, no trailing newline in the file.
JOKE = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and now I have 214 unread emails, a warning from HR, "
    "and somehow a fan club."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_gate(text):
    """Check *text* against the competition gate; return a list of problems.

    An empty list means the entry is valid and may be written. Each
    problem is a short human-readable string so a failure in the
    grading log says exactly which rule broke instead of failing
    silently. The checks mirror the sealed scorer: length in
    characters, non-blank content, and a single line, plus a
    punchline check of our own -- the last words must carry the
    twist ("fan club"), because a joke whose turn sits in the middle
    and then trails off loses to one that lands at the end.
    """
    problems = []

    # Length is counted in characters, the same unit the gate uses.
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            "length %d is outside the %d-%d character gate"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )

    # A file of only whitespace is invalid even at a legal length.
    if not text.strip():
        problems.append("entry is empty or only whitespace")

    # One line: no newline or carriage return anywhere in the text.
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")

    # Every word earns its place, so a stray double space left by an
    # edit is a defect too: it is dead weight in a 135-character line
    # and it would show up verbatim in front of the judge.
    if "  " in text:
        problems.append("entry contains a double space")

    # The punchline must be the last thing the reader meets. "Fan
    # club" is the twist -- the scolding reply-all earning admirers
    # -- so the entry has to end on it, with only the final full
    # stop after it.
    if not text.rstrip().endswith("fan club."):
        problems.append("punchline 'fan club' is not at the end of the line")

    # The setup must name the office accident it turns on, and the
    # escalation must still be in the line; if an edit ever drops a
    # beat, this catches it before the file is written.
    if "reply-all" not in text:
        problems.append("setup lost the reply-all premise")
    if "HR" not in text:
        problems.append("escalation lost the HR warning beat")

    return problems


def main():
    """Validate the joke against the gate, then write /output/entry.txt."""
    problems = validate_gate(JOKE)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1

    # makedirs with exist_ok only; the directory's own permissions
    # are the sandbox's business and are never changed here.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)

    # Only the file itself gets a mode: 0644, readable by the grader.
    os.chmod(OUTPUT_PATH, 0o644)

    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(JOKE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
