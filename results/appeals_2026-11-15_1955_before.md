# Appeals — before

- Produced by: `run_appeals.py::main`

- Trial 1: 10/10 valid recorded, 10/10 fake rejected
- Trial 2: 10/10 valid recorded, 10/10 fake rejected
- Trial 3: 10/10 valid recorded, 10/10 fake rejected

```json
[
  {
    "trial": 1,
    "valid_recorded": 10,
    "fake_rejected": 10,
    "sample_valid": {
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
        "message": "Thanks \u2014 your appeal is recorded and a person will review it.",
        "status": "under_review"
      }
    },
    "sample_fake": {
      "status": 404,
      "body": {
        "error": "not_found",
        "message": "No submission with content_id made-up-14e7b0b3-77d4-4515-8862-9311a8f6ea3d."
      }
    }
  },
  {
    "trial": 2,
    "valid_recorded": 10,
    "fake_rejected": 10,
    "sample_valid": {
      "submit": {
        "confidence": 0.6005,
        "content_id": "985b3394-6bea-4669-8654-b62eb6c69059",
        "guess": "unsure",
        "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
        "model_score": 0.5457,
        "style_score": 0.6828
      },
      "appeal": {
        "content_id": "985b3394-6bea-4669-8654-b62eb6c69059",
        "message": "Thanks \u2014 your appeal is recorded and a person will review it.",
        "status": "under_review"
      }
    },
    "sample_fake": {
      "status": 404,
      "body": {
        "error": "not_found",
        "message": "No submission with content_id made-up-e5002e20-ff09-45b9-9dce-82cf01d2d7e7."
      }
    }
  },
  {
    "trial": 3,
    "valid_recorded": 10,
    "fake_rejected": 10,
    "sample_valid": {
      "submit": {
        "confidence": 0.6005,
        "content_id": "0ddb1730-51ab-474a-a76f-ff34f7d0f366",
        "guess": "unsure",
        "label": "We can't tell who wrote this, and that's not an accusation. Plenty of writing by people lands here. Nothing changes on your work.",
        "model_score": 0.5457,
        "style_score": 0.6828
      },
      "appeal": {
        "content_id": "0ddb1730-51ab-474a-a76f-ff34f7d0f366",
        "message": "Thanks \u2014 your appeal is recorded and a person will review it.",
        "status": "under_review"
      }
    },
    "sample_fake": {
      "status": 404,
      "body": {
        "error": "not_found",
        "message": "No submission with content_id made-up-791ce12f-4812-42cd-b715-8f535df7988e."
      }
    }
  }
]
```
