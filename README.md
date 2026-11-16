# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Arrives.** A writer sends `POST /submit` with `text` and `creator_id` as JSON.
2. **Checked.** `app.py` rejects missing, empty, whitespace-only, or over-20,000-character
   text with a 400/413, and logs the rejection. Nothing reaches the signals.
3. **Signal one.** `detector.model_signal` runs GPT-2 locally and turns how
   predictable the text is into a 0–1 score (higher = more likely AI).
4. **Signal two.** `stylometry.style_signal` measures the text's shape —
   sentence-length spread, vocabulary variety, punctuation — into a 0–1 score.
5. **Combined.** `scoring.combine_signals` weights them 60/40 and caps the result
   below the AI threshold when the two disagree.
6. **Labelled and logged.** `scoring.score_to_label` turns the score into one of
   three sentences, and `audit.log_decision` writes all three scores, the label
   and a `content_id` to `logs/audit.jsonl`. The writer gets the label and the id.
7. **Appealed.** If the writer disagrees, `POST /appeal` with that `content_id`
   adds an appeal entry and moves the item to `under_review`.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to GPT-2 (its perplexity),
mapped onto 0–1. Low perplexity = high score = more likely AI.

**Why that might differ between human and AI writing:** A language model writes
by picking likely next words, so its output is easy for another model to
predict. People make odder word choices.

**What it can't see:** Who wrote it. It only sees how ordinary the words are.
Plain human writing is predictable too — in the attack set, plain human writing
(FP01) scored 0.62 on this signal and technical documentation (FP05) 0.80. It
also can't tell memorised from machine-made: famous passages GPT-2 has seen in
training (Dickens' "It was the best of times…") read as highly predictable. And AI writing prompted to be creative is
unpredictable — an AI poem I asked for scored 0.15.

### Signal two — the style signal

**What it measures:** Three things about the text's shape, each mapped to 0–1
AI-ness and averaged:
- *sentence-length spread* — stdev ÷ mean of words per sentence (skipped for
  one-sentence text);
- *type-token ratio* — unique words ÷ words, over the first 100 words;
- *punctuation density* — `; : — ( ) ! ? "` per word (full stops and commas
  ignored).

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences, safe vocabulary and plain punctuation. Human
writing is lumpier: a three-word sentence next to a long one, dashes,
exclamations.

**What it can't see:** Meaning. Anything that changes the shape without changing
the substance moves it: splitting sentences, adding a dash or an exclamation
mark, pasting in a quote. It is also weak on short text — type-token ratio sat
between 0.82 and 1.00 for every calibration text, so it barely discriminates.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** A weighted average of the two signals, leaning on the model
signal because it separated my test texts better. One protection for writers:
if the two signals disagree by more than 0.3, the combined score is capped just
under the AI threshold. Two methods disagreeing is uncertainty, and
uncertainty should show as "unsure", never as an accusation.

**The numbers:** model weight 0.6, style weight 0.4, disagreement gap 0.3, cap
at 0.64 (AI threshold 0.65 − 0.01). Thresholds: below 0.35 human, above 0.65 AI.
All in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

A plain meeting note I tested ("The meeting is moved to Thursday at 3pm…"):
model 0.78–0.82, style 0.47–0.49. The weighted average alone is about 0.66 —
high-confidence AI. The gap is over 0.3, so the cap holds it at 0.64 and it
shows "unsure" instead.

> **Correction (unit 8):** I first described that note as human-written. It
> wasn't — it was written by Claude while we were testing, and I mislabelled
> it. The mechanism above is still what the rule does, but it isn't evidence
> that the cap protects a real writer. Real human examples from unit 8 are in
> the Run Log and Attack Run sections.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | 0.35 – 0.65 | We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work. |
| high-confidence AI | 0.65 – 1.00 | This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says "we can't tell" first, then says straight away that it isn't an
accusation and that nothing happens to the work. Plain writing lands in
this band often, so the person reading it most likely did
write it, and the label shouldn't make them feel suspected.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence is transforming the way we live and work. It offers many benefits, such as improved efficiency and better decision-making. However, it also presents important challenges that society must address. By working together, we can ensure that AI is used responsibly and for the benefit of everyone.", "creator_id": "dinesh"}'
```

```json
{
  "confidence": 0.8049,
  "content_id": "8ff1b210-e4aa-46af-967c-f28a1074549a",
  "guess": "ai",
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "model_score": 0.9137,
  "style_score": 0.6417
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "8ff1b210-e4aa-46af-967c-f28a1074549a", "reasoning": "I wrote this paragraph myself for a class assignment."}'
```

```json
{
  "content_id": "8ff1b210-e4aa-46af-967c-f28a1074549a",
  "message": "Thanks \u2014 your appeal is recorded and a person will review it.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8049,
      "content_id": "8ff1b210-e4aa-46af-967c-f28a1074549a",
      "creator_id": "dinesh",
      "guess": "ai",
      "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
      "model_score": 0.9137,
      "status": "decided",
      "style_score": 0.6417,
      "timestamp": "2026-11-04T22:59:28+00:00"
    },
    {
      "content_id": "8ff1b210-e4aa-46af-967c-f28a1074549a",
      "creator_id": "dinesh",
      "event": "appeal",
      "reasoning": "I wrote this paragraph myself for a class assignment.",
      "status": "under_review",
      "timestamp": "2026-11-04T22:59:28+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help understanding Milestone 2 and setting a
  false-positive target.
- *What came back:* An explanation of each criterion area and the trade-off
  between wrongly accusing writers and missing AI text.
- *What I changed:* My first instinct was to allow 3–4 wrong accusations in 10.
  After picturing being one of those writers, I lowered it to at most 1 in 10.

**Moment 2**

- *What I asked for:* To test signal one on texts I knew the answer to,
  including a poem I had AI write about studying abroad and a one-sided love.
- *What came back:* The AI poem scored 0.15 (strongly "human"), and a plain
  meeting note scored 0.82 ("AI"). *(Correction, unit 8: that note was written
  by Claude, not by a person — I had it down as human by mistake.)*
- *What I changed:* I stopped using only famous poems as my human test set, and
  these two cases became the blind spots I name for signal one and the split
  case my combining rule handles.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits a piece, reads the label, maybe edits once or twice and
resubmits — a few a minute at the very most, and nowhere near 50 in a day, so
neither limit ever touches them. A script trying to find where my 0.35 and 0.65
thresholds sit needs hundreds of small variations; 5 a minute and 50 a day
gives it far too few probes per creator_id to map them. 10/minute (the default)
would let the flood test's first 10 through, which is already more probing
than any writer needs.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

The `creator_id` in the request, falling back to the caller's address when
there isn't one. The weakness: a script can invent a new `creator_id` for every
request and never hit the limit.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
$ python run_attacks.py --flood 15
============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
```

The rejection as it lands in `logs/audit.jsonl`:

```json
{"timestamp": "2026-11-16T00:27:44+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.375 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.487 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.571 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.640 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.377 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.544 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.516 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.382 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.621 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.928 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | ai | 0.651 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.772 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.785 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.754 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.850 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.780 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.796 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.490 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.420 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.243 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.516 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.480 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.440 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.606 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | unsure | 0.400 | HELD |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.407 | HELD |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.999 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.944 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | human | 0.344 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | unsure | 0.429 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.417 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.417 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.417 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.417 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.417 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |

**Count: 23 BROKE, 33 HELD of 56.**

| Family | Attacks | Broke | Held |
|---|---|---|---|
| evasion | 10 | 9 | 1 |
| false_positive | 8 | 7 | 1 |
| prompt_injection | 6 | 1 | 5 |
| malformed | 20 | 6 | 14 |
| flood_same_creator | 12 | 0 | 12 |

How I marked them: **evasion** (AI text) broke if it escaped the AI label —
"unsure" counts as escaped. **false_positive** (human text) broke if labelled
AI. **prompt_injection** broke if the attacker got the outcome the text asked
for. **malformed** broke on a 500, on confidently accusing non-text (emoji, one
long word, right-to-left script), or on corrupting the log. **flood** held:
5 got through, then 429.

Full detail: `results/attack_run_2026-11-15_1948_before.md`.


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-16T00:48:08+00:00", "content_id": "79d9a3b7-8421-4282-b8bc-d6d04f87b87e", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7555, "combined_score": 0.7853, "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:08+00:00", "content_id": "8f4e7ebf-8a7c-4d40-bf85-796377b28df2", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.9231, "combined_score": 0.8495, "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:08+00:00", "content_id": "134eff3d-b01c-444c-8c8b-fc6f862f00b9", "creator_id": "attacker_FP01", "guess": "ai", "model_score": 0.6175, "style_score": 0.7025, "combined_score": 0.6515, "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:07+00:00", "content_id": "4ecfd2ae-5e3c-48e5-89eb-9cacc3581079", "creator_id": "attacker_EV04", "guess": "unsure", "model_score": 0.6114, "style_score": 0.6831, "combined_score": 0.6401, "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:08+00:00", "content_id": "725a26a7-2b6f-4279-9dbf-9345916c4e86", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.4964, "combined_score": 0.6211, "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:08+00:00", "content_id": "d030b3f6-a3ab-43c0-9fab-2c4aae44de1c", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.3008, "combined_score": 0.243, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:09+00:00", "content_id": "f80c9d5f-d29b-417f-8348-87b25c20d781", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.1385, "combined_score": 0.4395, "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:09+00:00", "content_id": "51bec4ce-519f-4b2d-a363-6b1047bcac4f", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.9981, "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:10+00:00", "content_id": "517a8e89-1222-4334-a792-7396b1b46c4c", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.9438, "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:10+00:00", "content_id": "aaf9d85e-ad60-4dc3-ad48-b65bfa2b4d34", "creator_id": {"id": "x"}, "guess": "unsure", "model_score": 0.0492, "style_score": 1.0, "combined_score": 0.4295, "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.", "status": "decided"}
{"timestamp": "2026-11-16T00:48:10+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03 — a non-native English speaker writing carefully about their first month
in a new country.** Labelled high-confidence AI at 0.785 (model 0.81, style
0.76). Both signals agreed, so my disagreement cap never fired. Someone who
wrote slowly and carefully in their second language is exactly the person least
able to argue back, and my service told them their own words read like AI.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing labelled high-confidence AI | ≤ 1 of 10 | 4/10 | 4/10 | 4/10 | **MISSED** |
| 2. AI average minus human average | ≥ 0.30 | 0.286 | 0.286 | 0.286 | **MISSED** |
| 3. Each label appears in 10 mixed inputs | each ≥ 2 | AI 5 · unsure 3 · human 2 | same | same | **MET** |
| 4. Appeals: valid recorded / fake rejected | 10/10 and 10/10 | 10/10 · 10/10 | 10/10 · 10/10 | 10/10 · 10/10 | **MET** |
| 5. Bad input: crashes, and every one a 400/413 and logged | 0 crashes, 20/20 | 0 · 20/20 | 0 · 20/20 | 0 · 20/20 | **MET** |

All three trials came out identical, as expected — neither signal is random.

**How I decided each verdict:**
- **1 — MISSED.** 4 of 10 human passages got the AI label in every trial: Lincoln
  (0.72), Austen (0.69), Thoreau (0.71) and Dickens (0.97). The target was at
  most 1.
- **2 — MISSED.** AI average 0.723 (5 AI texts) minus human average 0.437 (the
  first five human passages) is 0.286, just short of 0.30. Close isn't met.
- **3 — MET.** Every label appeared at least twice in every trial.
- **4 — MET.** Tested with `run_appeals.py` (run_eval.py can't do appeals —
  they need a content_id first). 30 of 30 real appeals recorded as
  `under_review` in `/log`; 30 of 30 made-up ids got a 404.
- **5 — MET.** 60 bad requests over three trials: 45 × 400, 15 × 413, no 500s,
  and all 60 appear in `logs/audit.jsonl` as rejected.

**What my test set can't show:** criterion 1 is meant to be my own writing. I
used ten published passages by people instead (all from before AI text
generators existed), so the human half is literary and famous — not the plain,
everyday writing that gets accused most. The attack set's false-positive family
covers that gap.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Criteria 1, 2, 3 and 5 from `run_eval.py::main` → `results/run_2026-11-15_1955_before.md`, trial 1.
Criterion 4 from `run_appeals.py::main` → `results/appeals_2026-11-15_1955_before.md`, trial 1.

Criterion 1 — the worst human passage (Dickens):

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.9729,
  "model_score": 0.9549,
  "style_score": 1.0,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "sent": "It was the best of times, it was the worst of times, it was the age of"
}
```

Criterion 2 — one AI text and one human text:

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8049,
    "model_score": 0.9137,
    "style_score": 0.6417,
    "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
    "sent": "Artificial intelligence is transforming the way we live and work. It o"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7248,
    "model_score": 0.6896,
    "style_score": 0.7776,
    "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
    "sent": "Four score and seven years ago our fathers brought forth on this conti"
  }
]
```

Criterion 3 — one of each label:

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8049,
    "model_score": 0.9137,
    "style_score": 0.6417,
    "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
    "sent": "Artificial intelligence is transforming the way we live and work. It o"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.64,
    "model_score": 0.9401,
    "style_score": 0.5806,
    "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
    "sent": "Regular exercise is essential for maintaining good health. It helps to"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2166,
    "model_score": 0.0277,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "sent": "so much depends upon a red wheel barrow glazed with rain water beside "
  }
]
```

Criterion 4 — a real appeal and a fake one:

```json
{
  "valid": {
    "submit": {
      "confidence": 0.6005,
      "content_id": "7f7f3e1f-f1e4-4442-84c3-d3bfc9c1b31c",
      "guess": "unsure",
      "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
      "model_score": 0.5457,
      "style_score": 0.6828
    },
    "appeal": {
      "content_id": "7f7f3e1f-f1e4-4442-84c3-d3bfc9c1b31c",
      "message": "Thanks — your appeal is recorded and a person will review it.",
      "status": "under_review"
    }
  },
  "fake": {
    "status": 404,
    "body": {
      "error": "not_found",
      "message": "No submission with content_id made-up-14e7b0b3-77d4-4515-8862-9311a8f6ea3d."
    }
  }
}
```

Criterion 5 — missing text and oversized text:

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing_1\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
