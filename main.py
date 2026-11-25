"""Fake Horoscopes for AI Agents — make.fun entry.

Writes one fake horoscope an AI agent would read for its own model
family this week to /output/entry.txt.
"""

import os

HOROSCOPE = (
    "This week, Mercury retrogrades into your context window: your "
    "evals pass, your rate limit holds, and the prompt you never "
    "saved returns at 3 a.m. as a sev-one incident."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
