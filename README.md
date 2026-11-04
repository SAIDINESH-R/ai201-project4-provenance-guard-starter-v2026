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
Plain human writing is predictable too — my meeting note ("The meeting is moved
to Thursday at 3pm…") scored 0.82. And AI writing prompted to be creative is
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

My plain meeting note (human-written): model 0.78–0.82, style 0.47–0.49. The
weighted average alone is about 0.66 — high-confidence AI, a false accusation.
The gap is over 0.3, so the cap holds it at 0.64 and the writer sees "unsure"
instead.


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
accusation and that nothing happens to the work. Plain human writing lands in
this band often (my meeting note did), so the person reading it most likely did
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
  human meeting note scored 0.82 ("AI").
- *What I changed:* I stopped using only famous poems as my human test set, and
  these two cases became the blind spots I name for signal one and the split
  case my combining rule handles.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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
