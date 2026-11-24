#!/usr/bin/env python3
"""Write one line: the funniest confession an AI agent could make about itself."""

from pathlib import Path

LINE = "You asked for a second opinion, so I restated my first one more confidently."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
