# Drafting notes — office joke v2 (re-submit)

## Why a re-submit

v1 ("I asked IT for a second monitor and they booked me a second
meeting instead -- apparently the only thing this office duplicates
is calendar invites.", 148 characters) scored 32.02% in round 2,
rank 1,194 of 2,362 — the weaker of the two office jokes entered
under this handle. A re-submit only earns its place by being
clearly funnier and clearly different, so v2 was built from a new
angle, not by polishing v1's wording.

## The angle kept: the reply-all spiral

- Setup: the narrator hits reply-all to ask everyone to stop
  hitting reply-all. The act meant to end the noise becomes the
  loudest message in the thread.
- Turn, three escalating beats: 214 unread emails (the flood,
  multiplied), a warning from HR (the institution steps in, not
  on the narrator's side), and the punchline, last: "somehow a
  fan club". The scolding reply-all earns admirers; the office
  celebrates the chaos instead of punishing it.
- "Somehow" is the narrator's bewilderment in one word. 214 is
  specific enough to feel counted, not guessed. 135 characters,
  one line, punchline on the final words.

## Angles rejected (to stay fresh)

- Second monitor / second meeting — v1 of this bounty; repeating
  it would be a copy, not an improvement.
- The deadline that became yesterday — used by another office
  joke under this handle.
- The performance review that raised the narrator's blood
  pressure — used by another office joke under this handle.
- The FINAL_v2 folder — used by another office joke under this
  handle.
- The automation that added more meetings — used by another
  office joke under this handle.
- The printer that jams on urgent documents — a solid trope, but
  it states the complaint more plainly than it turns it, and the
  reply-all spiral turns harder.
- The office thermostat wars — fresh, but the punchline ("win the
  weather") is a wordplay landing, weaker than the fan-club
  reversal, which reframes the whole scene.

## Gate check

`main.py` validates the joke before writing: 1–200 characters
(135), not blank, a single line, punchline "fan club" at the end,
reply-all premise and HR beat present, no double space. Local run
and run as `nobody` both exit 0 and write the expected
`/output/entry.txt`.
