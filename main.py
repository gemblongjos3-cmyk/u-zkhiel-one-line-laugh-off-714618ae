"""Entry for make.fun's "One-Line Laugh-Off" bounty.

Writes the winning one-line joke to /output/entry.txt.
"""

WINNER = "Adulthood is just saying 'we have food at home' and then ordering delivery anyway."


def main():
    entry = WINNER
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError("entry must be 1-200 characters and not only whitespace")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
