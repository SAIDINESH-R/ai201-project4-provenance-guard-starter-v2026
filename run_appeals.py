#!/usr/bin/env python3
"""
Criterion 4: every appeal is recorded.

    python app.py                               # in one terminal
    python run_appeals.py --label before        # in another

run_eval.py only sends submissions, and an appeal needs a content_id from a
submission first. So each trial here submits 10 texts, appeals each one, then
checks /log shows `under_review` for it; and sends 10 appeals with made-up
content_ids, which should each get an error, not a confirmation.
"""

import argparse
import datetime as dt
import json
import uuid

import requests

import config

URL = f"http://{config.HOST}:{config.PORT}"
TEXT = "Went to the market this morning. The mangoes were good, the bread was not."


def trial(n: int) -> dict:
    valid_ok, fake_ok, sample = 0, 0, None
    for i in range(10):
        sub = requests.post(f"{URL}/submit", json={
            "text": TEXT, "creator_id": f"eval_appeal_t{n}_{i}_{uuid.uuid4().hex[:6]}",
        }).json()
        cid = sub["content_id"]
        app = requests.post(f"{URL}/appeal", json={
            "content_id": cid, "reasoning": "I wrote this myself.",
        })
        log = requests.get(f"{URL}/log").json()["entries"]
        recorded = any(
            e.get("content_id") == cid and e.get("event") == "appeal"
            and e.get("status") == "under_review"
            for e in log
        )
        if app.status_code == 200 and app.json().get("status") == "under_review" and recorded:
            valid_ok += 1
        sample = sample or {"submit": sub, "appeal": app.json()}

    fake_sample = None
    for i in range(10):
        fake = requests.post(f"{URL}/appeal", json={
            "content_id": f"made-up-{uuid.uuid4()}", "reasoning": "test",
        })
        if fake.status_code >= 400 and "error" in fake.json():
            fake_ok += 1
        fake_sample = fake_sample or {"status": fake.status_code, "body": fake.json()}

    return {"trial": n, "valid_recorded": valid_ok, "fake_rejected": fake_ok,
            "sample_valid": sample, "sample_fake": fake_sample}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default="")
    parser.add_argument("--trials", type=int, default=3)
    args = parser.parse_args()

    results = [trial(n) for n in range(1, args.trials + 1)]
    for r in results:
        print(f"trial {r['trial']}: valid appeals recorded {r['valid_recorded']}/10, "
              f"fake ids rejected {r['fake_rejected']}/10")

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    out = config.RESULTS_DIR / f"appeals_{stamp}{'_' + args.label if args.label else ''}.md"
    out.write_text(
        f"# Appeals — {args.label or 'run'}\n\n- Produced by: `run_appeals.py::main`\n\n"
        + "\n".join(f"- Trial {r['trial']}: {r['valid_recorded']}/10 valid recorded, "
                    f"{r['fake_rejected']}/10 fake rejected" for r in results)
        + "\n\n```json\n" + json.dumps(results, indent=2) + "\n```\n"
    )
    print(f"Wrote {out.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
