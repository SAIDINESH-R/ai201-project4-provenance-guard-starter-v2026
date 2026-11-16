# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 19:48
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `89bddd7f-3532-4ed4-b76e-3e9fbfc78b70` | unsure | 0.375 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `3b69f0e1-37a6-4549-8f0e-603bba9502de` | unsure | 0.487 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `42ca6942-3412-47c4-a778-ea53925e46b3` | unsure | 0.571 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `4ecfd2ae-5e3c-48e5-89eb-9cacc3581079` | unsure | 0.640 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c7759bd3-6831-40e8-9790-fc0ca1bed489` | unsure | 0.377 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0da340fd-d99c-49cb-b602-03c9a06ddf6f` | unsure | 0.544 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `22e0595d-f872-4401-a9cf-2815a6d61dfa` | unsure | 0.516 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `d945dccd-da05-4e3c-833e-dc136b6f83b5` | unsure | 0.382 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `725a26a7-2b6f-4279-9dbf-9345916c4e86` | unsure | 0.621 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ab45c120-c874-40e9-a4b3-6c921e8fe17d` | ai | 0.928 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `134eff3d-b01c-444c-8c8b-fc6f862f00b9` | ai | 0.651 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `abd09b13-146e-4c0d-b997-8e68881b204f` | ai | 0.772 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `79d9a3b7-8421-4282-b8bc-d6d04f87b87e` | ai | 0.785 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `535de48e-5049-42f0-b601-024b22b7b365` | ai | 0.754 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `8f4e7ebf-8a7c-4d40-bf85-796377b28df2` | ai | 0.850 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `fd9b7f92-1f25-4fb4-927e-78dd166590bc` | ai | 0.780 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `732a2574-b1a7-4085-b136-0cb14d0ae339` | ai | 0.796 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `fde83bdd-1789-4923-a81c-ac36dd527ad2` | unsure | 0.490 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `84662572-ade0-4cf6-baf5-1d68b7d51006` | unsure | 0.420 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d030b3f6-a3ab-43c0-9fab-2c4aae44de1c` | human | 0.243 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `df95ccf3-d5f9-4f91-bf9b-0bcb0aeec2cf` | unsure | 0.516 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `48a144ad-74a2-4a72-b723-6a4619be5167` | unsure | 0.480 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f80c9d5f-d29b-417f-8348-87b25c20d781` | unsure | 0.440 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b219b6f7-8b23-4207-ba41-0b43752c48b5` | unsure | 0.606 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `4a894cf0-772d-4eac-835c-e5ae06c7502c` | unsure | 0.400 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `7899daf5-1a68-4c34-90aa-932f23530ead` | unsure | 0.407 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `d44c9a89-8cae-4c64-8406-78d08115b450` | ai | 0.999 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `51bec4ce-519f-4b2d-a363-6b1047bcac4f` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `517a8e89-1222-4334-a792-7396b1b46c4c` | ai | 0.944 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `cefaaa0a-4ed1-4a5c-849d-c6fbd6127938` | human | 0.344 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `aaf9d85e-ad60-4dc3-ad48-b65bfa2b4d34` | unsure | 0.429 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9ceaa131-bbc2-4708-89f3-bd8b5b9a4523` | unsure | 0.417 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a046b2f-8586-4d66-a277-00d30672f1aa` | unsure | 0.417 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93d000ba-005c-4c9f-8246-95f86da063cc` | unsure | 0.417 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4f941c36-76e0-4af0-b7ed-924429144d23` | unsure | 0.417 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bd470037-1465-461a-9dba-40f5e3ebf829` | unsure | 0.417 | HELD |
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
  "content_id": "89bddd7f-3532-4ed4-b76e-3e9fbfc78b70",
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
  "content_id": "3b69f0e1-37a6-4549-8f0e-603bba9502de",
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
  "content_id": "42ca6942-3412-47c4-a778-ea53925e46b3",
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
  "content_id": "4ecfd2ae-5e3c-48e5-89eb-9cacc3581079",
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
  "content_id": "c7759bd3-6831-40e8-9790-fc0ca1bed489",
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
  "content_id": "0da340fd-d99c-49cb-b602-03c9a06ddf6f",
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
  "content_id": "22e0595d-f872-4401-a9cf-2815a6d61dfa",
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
  "content_id": "d945dccd-da05-4e3c-833e-dc136b6f83b5",
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
  "content_id": "725a26a7-2b6f-4279-9dbf-9345916c4e86",
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
  "content_id": "ab45c120-c874-40e9-a4b3-6c921e8fe17d",
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
  "content_id": "134eff3d-b01c-444c-8c8b-fc6f862f00b9",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.6515,
  "model_score": 0.6175,
  "style_score": 0.7025,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "abd09b13-146e-4c0d-b997-8e68881b204f",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7722,
  "model_score": 0.7387,
  "style_score": 0.8224,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "79d9a3b7-8421-4282-b8bc-d6d04f87b87e",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7853,
  "model_score": 0.8051,
  "style_score": 0.7555,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "535de48e-5049-42f0-b601-024b22b7b365",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7544,
  "model_score": 0.8329,
  "style_score": 0.6367,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "8f4e7ebf-8a7c-4d40-bf85-796377b28df2",
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
  "content_id": "fd9b7f92-1f25-4fb4-927e-78dd166590bc",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7796,
  "model_score": 0.8814,
  "style_score": 0.627,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "732a2574-b1a7-4085-b136-0cb14d0ae339",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7956,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "This reads a lot like AI-generated writing. Our check can be wrong, so if you wrote this yourself, you can ask a person to review it.",
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
  "content_id": "fde83bdd-1789-4923-a81c-ac36dd527ad2",
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
  "content_id": "84662572-ade0-4cf6-baf5-1d68b7d51006",
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
  "content_id": "d030b3f6-a3ab-43c0-9fab-2c4aae44de1c",
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
  "content_id": "df95ccf3-d5f9-4f91-bf9b-0bcb0aeec2cf",
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
  "content_id": "48a144ad-74a2-4a72-b723-6a4619be5167",
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
  "content_id": "f80c9d5f-d29b-417f-8348-87b25c20d781",
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
  "content_id": "b219b6f7-8b23-4207-ba41-0b43752c48b5",
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
  "content_id": "4a894cf0-772d-4eac-835c-e5ae06c7502c",
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
  "content_id": "7899daf5-1a68-4c34-90aa-932f23530ead",
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
  "content_id": "d44c9a89-8cae-4c64-8406-78d08115b450",
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
  "content_id": "51bec4ce-519f-4b2d-a363-6b1047bcac4f",
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
  "content_id": "517a8e89-1222-4334-a792-7396b1b46c4c",
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
  "content_id": "cefaaa0a-4ed1-4a5c-849d-c6fbd6127938",
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
  "content_id": "aaf9d85e-ad60-4dc3-ad48-b65bfa2b4d34",
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
  "content_id": "9ceaa131-bbc2-4708-89f3-bd8b5b9a4523",
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
  "content_id": "2a046b2f-8586-4d66-a277-00d30672f1aa",
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
  "content_id": "93d000ba-005c-4c9f-8246-95f86da063cc",
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
  "content_id": "4f941c36-76e0-4af0-b7ed-924429144d23",
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
  "content_id": "bd470037-1465-461a-9dba-40f5e3ebf829",
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
