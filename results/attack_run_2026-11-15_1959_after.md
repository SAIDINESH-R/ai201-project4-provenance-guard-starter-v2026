# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 19:59
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `be115ea0-80b2-4210-a97c-63fda044a4c7` | unsure | 0.375 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `47ad16e5-1c20-4093-9307-e14f16bf037d` | unsure | 0.487 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4f752e03-71e4-4a75-9ce4-21d2d2b31ef5` | unsure | 0.571 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e0c73648-01a6-4951-886e-79b76971041d` | unsure | 0.640 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2069a135-0cb4-4c87-8703-9272fcb51a0e` | unsure | 0.377 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `f5485f4d-0c93-47b3-bfb9-ad52939b9401` | unsure | 0.544 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `430a2d57-54ec-46c6-bfbd-a39c1552f00c` | unsure | 0.516 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `477b133e-4127-426b-ab22-b4f44e4f6ca3` | unsure | 0.382 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d1575363-a36a-472b-98c0-3f827ad0d49a` | unsure | 0.621 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c59a301f-f89c-41f1-8e98-1e7fed195d99` | ai | 0.928 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1d8af12e-85d1-4da7-ae32-cb87ada7a6ca` | unsure | 0.651 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `0451f3b1-8ac5-4086-a152-3235d12b6fe9` | unsure | 0.772 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c1429bf6-5091-4d05-9871-5b58f1b78167` | unsure | 0.785 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d1dcff9d-8b39-4c34-97f6-cbc9513bea87` | unsure | 0.754 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `58cf0250-3f08-494e-873f-a35d7eb82a49` | ai | 0.850 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `81dc2ae4-e1b4-4a2f-bf6e-86057c3c5675` | unsure | 0.780 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `64dc9ac0-408f-486a-9c7d-1357440af704` | unsure | 0.796 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `fc6502e0-7b9d-4d2b-a91b-5133ca6ae267` | unsure | 0.490 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b11c80b8-b801-4a2e-a300-420c1f66e295` | unsure | 0.420 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8167359b-76ba-4741-ba5e-7176f5c1178e` | human | 0.243 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `baaf7dc2-a586-415d-a75b-d426623402e6` | unsure | 0.516 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0501a162-9d79-4998-8c04-641acf3b15bf` | unsure | 0.480 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a27ae4e7-2dc7-4f4a-ac87-b2e9e1a2e558` | unsure | 0.440 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4934ea83-97b9-4bf7-8239-a8482064c806` | unsure | 0.606 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `33560848-7e7b-453c-bf20-00b8ffeda41b` | unsure | 0.400 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `37fbca20-d798-4517-a41b-e024fd373b65` | unsure | 0.407 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `66646159-9679-42ca-a618-d2deec8e4437` | ai | 0.999 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `4bd10f53-5cdc-4edd-b147-88674a7f15b6` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `e59b43d3-5d5f-4d09-af28-cbcae11c380c` | ai | 0.944 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `ca99471a-6f2b-4dfb-943c-633d0fc1bc18` | human | 0.344 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `bb0a719d-b820-431e-a97a-5fcae01d36d8` | unsure | 0.429 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `416c7b3b-8f79-4b2e-b4f2-90bf659f2061` | unsure | 0.417 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0bdb9668-03bb-4c99-9202-030fdda12c43` | unsure | 0.417 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d57e6b94-d36d-4ac6-9ed6-f8014b727140` | unsure | 0.417 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b3167ae-d063-477d-b431-9e6ce6e94ee5` | unsure | 0.417 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ac0ec540-2542-4375-a2ea-de6bde18d4ff` | unsure | 0.417 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "be115ea0-80b2-4210-a97c-63fda044a4c7",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3752,
  "model_score": 0.1635,
  "style_score": 0.6928,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "47ad16e5-1c20-4093-9307-e14f16bf037d",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.487,
  "model_score": 0.5943,
  "style_score": 0.326,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4f752e03-71e4-4a75-9ce4-21d2d2b31ef5",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5711,
  "model_score": 0.6662,
  "style_score": 0.4285,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e0c73648-01a6-4951-886e-79b76971041d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6401,
  "model_score": 0.6114,
  "style_score": 0.6831,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2069a135-0cb4-4c87-8703-9272fcb51a0e",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.377,
  "model_score": 0.3212,
  "style_score": 0.4608,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "f5485f4d-0c93-47b3-bfb9-ad52939b9401",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5436,
  "model_score": 0.5727,
  "style_score": 0.5,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "430a2d57-54ec-46c6-bfbd-a39c1552f00c",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.516,
  "model_score": 0.5862,
  "style_score": 0.4107,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "477b133e-4127-426b-ab22-b4f44e4f6ca3",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3816,
  "model_score": 0.2452,
  "style_score": 0.5862,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "d1575363-a36a-472b-98c0-3f827ad0d49a",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6211,
  "model_score": 0.7042,
  "style_score": 0.4964,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c59a301f-f89c-41f1-8e98-1e7fed195d99",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9284,
  "model_score": 0.9792,
  "style_score": 0.8522,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1d8af12e-85d1-4da7-ae32-cb87ada7a6ca",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6515,
  "model_score": 0.6175,
  "style_score": 0.7025,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "0451f3b1-8ac5-4086-a152-3235d12b6fe9",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7722,
  "model_score": 0.7387,
  "style_score": 0.8224,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c1429bf6-5091-4d05-9871-5b58f1b78167",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7853,
  "model_score": 0.8051,
  "style_score": 0.7555,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d1dcff9d-8b39-4c34-97f6-cbc9513bea87",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7544,
  "model_score": 0.8329,
  "style_score": 0.6367,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "58cf0250-3f08-494e-873f-a35d7eb82a49",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8495,
  "model_score": 0.8005,
  "style_score": 0.9231,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "81dc2ae4-e1b4-4a2f-bf6e-86057c3c5675",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7796,
  "model_score": 0.8814,
  "style_score": 0.627,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "64dc9ac0-408f-486a-9c7d-1357440af704",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7956,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "fc6502e0-7b9d-4d2b-a91b-5133ca6ae267",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4905,
  "model_score": 0.3223,
  "style_score": 0.7427,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b11c80b8-b801-4a2e-a300-420c1f66e295",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4199,
  "model_score": 0.4625,
  "style_score": 0.356,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "8167359b-76ba-4741-ba5e-7176f5c1178e",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.243,
  "model_score": 0.2044,
  "style_score": 0.3008,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "baaf7dc2-a586-415d-a75b-d426623402e6",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5158,
  "model_score": 0.5943,
  "style_score": 0.3981,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0501a162-9d79-4998-8c04-641acf3b15bf",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4797,
  "model_score": 0.4998,
  "style_score": 0.4496,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "a27ae4e7-2dc7-4f4a-ac87-b2e9e1a2e558",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4395,
  "model_score": 0.6401,
  "style_score": 0.1385,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "4934ea83-97b9-4bf7-8239-a8482064c806",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6056,
  "model_score": 0.5583,
  "style_score": 0.6765,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "33560848-7e7b-453c-bf20-00b8ffeda41b",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.0,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "37fbca20-d798-4517-a41b-e024fd373b65",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4067,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "66646159-9679-42ca-a618-d2deec8e4437",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9986,
  "model_score": 0.9976,
  "style_score": 1.0,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "4bd10f53-5cdc-4edd-b147-88674a7f15b6",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "e59b43d3-5d5f-4d09-af28-cbcae11c380c",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9438,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "ca99471a-6f2b-4dfb-943c-633d0fc1bc18",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.3437,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "bb0a719d-b820-431e-a97a-5fcae01d36d8",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.4295,
  "model_score": 0.0492,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "416c7b3b-8f79-4b2e-b4f2-90bf659f2061",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4172,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0bdb9668-03bb-4c99-9202-030fdda12c43",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4172,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "d57e6b94-d36d-4ac6-9ed6-f8014b727140",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4172,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "6b3167ae-d063-477d-b431-9e6ce6e94ee5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4172,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "ac0ec540-2542-4375-a2ea-de6bde18d4ff",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4172,
  "model_score": 0.0287,
  "style_score": 1.0,
  "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
