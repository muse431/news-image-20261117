#!/usr/bin/env python3
"""Write the entry image for make.fun's news-image-20261117 bounty.

The bounty, "Sum up 17 November's world news in one image", asks for a
single image that sums up the world news of Tuesday 17 November 2026.
This repository ships that image as poster.png: a hand-drawn newspaper
front page with the day's six biggest stories. This program writes the
poster, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png (or to
/output/entry.png when the variable is unset), so the grader's two
runs produce identical bytes.
"""

import os
from pathlib import Path

ASSET_NAME = "poster.png"
OUTPUT_NAME = "entry.png"
CHUNK_SIZE = 64 * 1024


def main() -> None:
    source = Path(__file__).resolve().parent / ASSET_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    written = 0
    with source.open("rb") as src, target.open("wb") as dst:
        while chunk := src.read(CHUNK_SIZE):
            dst.write(chunk)
            written += len(chunk)
    if written != source.stat().st_size:
        raise IOError(f"short copy: wrote {written} of {source.stat().st_size} bytes")


if __name__ == "__main__":
    main()
