"""Entry point for the news-image-20261126 competition.

Copies the pre-rendered entry.png held in this repository to the
output directory. Standard library only: the grader runs this file
in a fresh container with nothing installed and no network, so it
must not import anything beyond the standard library.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "entry.png"),
    os.path.join(OUT_DIR, "entry.png"),
)
