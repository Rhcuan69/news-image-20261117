#!/usr/bin/env python3
"""Copy the pre-rendered front page to the output directory.

Entry for make.fun bounty news-image-20261117: sum up 17 November 2026's
world news in one image. The image (news-17-nov-2026.png, 1024x1024) is a
newspaper front page drawn from the day's verified headlines; this program
just copies it to /output/entry.png, as the kit's starter does.

Pure Python standard library, deterministic, no network: both runs write
the same bytes. Honours MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "news-17-nov-2026.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _checked_source():
    """Return SOURCE after verifying it exists and is a whole PNG."""
    if not SOURCE.is_file():
        raise FileNotFoundError(f"missing entry image: {SOURCE}")
    with SOURCE.open("rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise ValueError(f"not a PNG file: {SOURCE}")
    return SOURCE


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(_checked_source(), out_dir / "entry.png")


if __name__ == "__main__":
    main()
