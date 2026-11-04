# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Few honest writers are wrongly called AI

Of 10 pieces of real human writing (including Edna St. Vincent Millay's "First
Fig"), **at most 1** gets the high-confidence AI label, in each of the three
unit 8 trials.

**Why this target:** Being called a cheater on your own work hurts a writer far
more than the site missing some AI text. I would rather let some AI writing
through than accuse a real person, so I hold this number low even though it is
hard to hit.

---

## 2. Clearly AI and clearly human text score far apart

Across 5 clearly AI texts and 5 clearly human texts, the average combined score
of the AI texts is **at least 0.3 higher** than the average of the human texts.

**Why this target:** My "can't tell" band (0.35 to 0.65) is 0.3 wide. If the two
groups are closer than that, even obvious cases land in the middle and the
service never gives a confident answer, like a thermometer that reads almost the
same for ice and boiling water.

---

## 3. Every label actually shows up

Across 10 mixed test inputs (human, AI, and in-between), **each of the three
labels appears at least 2 times.**

**Why this target:** A label that never appears is useless. If "probably human"
never shows, nobody is ever cleared; if "can't tell" never shows, the service
never admits doubt. Two each proves the label is reachable on purpose, not by
luck.

---

## 4. Every appeal is recorded

**10 of 10** appeals sent with a real `content_id` change that item's status to
`under_review` and appear in `GET /log` next to the original decision. **10 of
10** appeals with a made-up `content_id` get an error reply, not a fake
confirmation.

**Why this target:** If a writer thinks they were scored wrongly, the appeal is
their only way to ask for a review. An appeal that silently disappears leaves a
wrongly accused person believing someone is looking at their work when nobody
is. This is my own code, not a model guessing, so there is no reason for it to
fail even once.

---

## 5. Bad input never crashes the service

For each of these cases sent to `POST /submit`, `text` missing, `text` empty,
`text` only spaces, and `text` over 20,000 characters, sent 5 times each:
**0 crashes**, every request gets a clear error reply (400 or 413), and **every
one** is written to the audit log as a rejection.

**Why this target:** A crash takes the service down for every writer, not just
the one who sent bad input. A rejection that isn't logged leaves no trace, so an
attack made of bad requests would be invisible. Like the appeal path, this is
plain code, so the target is all or nothing.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
