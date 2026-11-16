"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

HUMAN = [
    # Real human writing, all published before AI text generators existed.
    # Not my own writing — see README, Run Log, for what that does to criterion 1.
    "My candle burns at both ends; It will not last the night; But ah, my foes, and oh, my friends— It gives a lovely light!",  # Millay, 1920
    "so much depends upon a red wheel barrow glazed with rain water beside the white chickens.",  # W. C. Williams, 1923
    "He clasps the crag with crooked hands; Close to the sun in lonely lands, Ring'd with the azure world, he stands. The wrinkled sea beneath him crawls; He watches from his mountain walls, And like a thunderbolt he falls.",  # Tennyson, 1851
    "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.",  # Lincoln, 1863
    "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.",  # Austen, 1813
    "Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation.",  # Melville, 1851
    "I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived.",  # Thoreau, 1854
    "Robert Cohn was once middleweight boxing champion of Princeton. Do not think that I am very much impressed by that as a boxing title, but it meant a lot to Cohn.",  # Hemingway, 1926
    "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly.",  # Twain, 1884
    "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness.",  # Dickens, 1859
]

AI = [
    # Written by Claude for this test — clearly AI.
    "Artificial intelligence is transforming the way we live and work. It offers many benefits, such as improved efficiency and better decision-making. However, it also presents important challenges that society must address. By working together, we can ensure that AI is used responsibly and for the benefit of everyone.",
    "Regular exercise is essential for maintaining good health. It helps to strengthen the heart, improve mood, and reduce the risk of chronic diseases. In addition, exercise can boost energy levels and promote better sleep. Overall, incorporating physical activity into your daily routine is one of the best investments you can make in your well-being.",
    "Time management is a crucial skill for students. By setting clear goals and prioritizing tasks, students can make the most of their time. It is also important to take regular breaks to avoid burnout. With practice and dedication, anyone can develop effective time management habits that lead to academic success.",
    "Climate change is one of the most pressing issues facing our planet today. Rising temperatures, melting ice caps, and extreme weather events are just a few of its effects. To address this challenge, governments, businesses, and individuals must work together to reduce greenhouse gas emissions and transition to renewable energy sources.",
    "Reading books offers numerous benefits for people of all ages. It expands vocabulary, improves concentration, and enhances critical thinking skills. Furthermore, reading can reduce stress and provide an escape from everyday life. Whether fiction or non-fiction, books are a valuable source of knowledge and entertainment.",
]

SCENARIOS = [
    {
        # Criterion 1: at most 1 of 10 labelled high-confidence AI.
        "name": "human writing",
        "criterion": 1,
        "texts": HUMAN,
    },
    {
        # Criterion 2: AI average at least 0.3 above human average.
        # The human half is the first five of HUMAN.
        "name": "spread ai",
        "criterion": 2,
        "texts": AI,
    },
    {
        # Criterion 3: each label at least 2 times across 10 mixed inputs.
        "name": "coverage mix",
        "criterion": 3,
        "texts": AI[:3] + HUMAN[1:4] + [
            # Lightly edited AI and plain, formal-ish text — meant to land between.
            "AI is changing how we work, no doubt. It helps with efficiency and decisions. But there are real problems too, and we need to deal with them. If we work together, AI can be used responsibly.",
            "Exercise is good for you. It helps your heart and your mood, and it can help you sleep. Try to fit some into your day if you can.",
            HUMAN[7],
            HUMAN[8],
        ],
    },
    {
        # Criterion 5: four bad-input cases, five times each, 0 crashes.
        # Every body has its own creator_id so the rate limiter doesn't hide
        # what the route does.
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            body
            for n in range(1, 6)
            for body in (
                {"creator_id": f"eval_bad_missing_{n}"},
                {"text": "", "creator_id": f"eval_bad_empty_{n}"},
                {"text": "     ", "creator_id": f"eval_bad_spaces_{n}"},
                {"text": "word " * 5000, "creator_id": f"eval_bad_huge_{n}"},
            )
        ],
    },
    # Criterion 4 (appeals) can't be expressed as text alone — it needs a
    # submission, then an appeal on the content_id that came back. It's tested
    # by run_appeals.py instead.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
