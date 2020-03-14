import os
from pathlib import Path

from adventures.pythonbeard.chapters.read_the_code.reading_module import decipher
from utils.level_key import get_hash

text = "xlivi mw e qet wyfqevmri erh e aixwymx hsarxlivi rs pmi"

if __name__ == "__main__":
    res = decipher(text, 4)

    print("{} -> {}".format(text, res))
    print("Result : {}".format(get_hash(res)))
