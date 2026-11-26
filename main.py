"""Make the Judge Laugh in One Line — one-line entry.

Writes the single funny line to /output/entry.txt (and prints it).
The line is one sentence, 200 characters at most, on any topic.
"""

from pathlib import Path

ENTRY = (
    "My smart fridge emailed me a diet plan, then left its own door "
    "open all night like the calories were my problem."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} characters, over 200"
    assert text.count(".") == 1, "entry must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    # Read it back to prove the written file matches the entry.
    assert out.read_text(encoding="utf-8").strip() == text
    print(text)


if __name__ == "__main__":
    main()
