
from adventures.pythonbeard.chapters.find_a_way_out.searching_module import \
    find_open_path, Direction, Status, Path
from utils.level_key import get_hash

path = [
    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.OPEN), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.OPEN), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.BLOCKED), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.OPEN), 
     Path(Direction.LEFT, Status.BLOCKED), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.OPEN), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.OPEN), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.BLOCKED), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.OPEN), 
     Path(Direction.LEFT, Status.BLOCKED), Path(Direction.DOWN, Status.BLOCKED)],

    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.BLOCKED), Path(Direction.DOWN, Status.OPEN)],

    [Path(Direction.UP, Status.BLOCKED), Path(Direction.RIGHT, Status.BLOCKED), 
     Path(Direction.LEFT, Status.OPEN), Path(Direction.DOWN, Status.BLOCKED)],
]

if __name__ == "__main__":

    res = ""

    for fork in path:
        selected = find_open_path(fork)
        res += str(selected)
        print("you went {}".format(selected.direction.name))
    
    print("Result : {}".format(get_hash(str(res))))
