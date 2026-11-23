#!/usr/bin/env python3
"""news-image-20261123 entry (variant A): copy the pre-rendered front page
to the harness output directory."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(OUT, "entry.png"),
    )


if __name__ == "__main__":
    main()
