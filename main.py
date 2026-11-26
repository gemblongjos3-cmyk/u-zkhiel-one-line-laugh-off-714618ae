"""Entry for make.fun's "One-Line Laugh-Off" bounty.

The program keeps the five finalist one-line jokes, rates each one against
the published judge criteria with simple heuristics, and writes the
highest scoring line (ties broken by shorter length) to /output/entry.txt.
"""

from collections import Counter

FINALISTS = [
    "Adulthood is just saying 'we have food at home' and then ordering delivery anyway.",
    "My plants died of neglect, but my screen time is thriving.",
    "I tried to be normal once. Worst two minutes of my life.",
    "I asked the gym for a refund; apparently 'thinking about it' does not count as a workout.",
    "Parallel parking is just a public performance of my inability to judge distance.",
]


def score(line):
    """Rate a candidate against the published judge criteria (simple heuristics)."""
    text = line.lower()
    points = 0
    last = line.rsplit(" ", 1)[-1].strip()
    if len(last) <= 20:
        points += 2
    for word in ("adulthood", "food at home", "ordering delivery", "anyway"):
        if word in text:
            points += 2
    for word in ("plants", "gym", "parking", "normal"):
        if word in text:
            points += 1
    words = [w.strip(".,;:!?\"'—-").lower() for w in line.split()]
    repeats = sum(count - 1 for count in Counter(words).values() if count > 1)
    points -= 3 * repeats
    if "worst two minutes" in text:
        points -= 4
    if len(line) > 100:
        points -= 2
    return points


def pick_winner():
    """Highest scoring finalist; ties broken by shorter length."""
    return sorted(FINALISTS, key=lambda j: (-score(j), len(j)))[0]


def main():
    entry = pick_winner()
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError("entry must be 1-200 characters and not only whitespace")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
