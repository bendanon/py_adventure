import random

from adventures.pythonbeard.common.caves import Cave, PathBuilder, Path
from adventures.pythonbeard.chapters.the_caves.autopilot_module import get_directions
from utils.level_key import get_hash

layout = [
    PathBuilder(False, True, True),
    PathBuilder(False, True, False),
    PathBuilder(False, True, True),
    PathBuilder(False, False, False),
    PathBuilder(False, True, False),
    PathBuilder(False, True, True),
    PathBuilder(False, False, False),
    PathBuilder(True, False, False),
    PathBuilder(False, True, True),
    PathBuilder(False, False, True),
    PathBuilder(False, True, True),
    PathBuilder(False, False, False),
    PathBuilder(False, False, True),
    PathBuilder(False, False, False),
]


def print_path(path: Path):
    if path == None:
        return

    print(path)
    print_path(path.left)
    print_path(path.right)

if __name__ == "__main__":
    user_res = ""

    cave = Cave(layout)

    directions = get_directions(cave)
    print("You're directions: {}".format(directions))

    print("Result : {}".format(get_hash(str(directions))))
