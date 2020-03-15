from enum import Enum
from typing import List

from adventures.pythonbeard.common.caves import Cave, Path

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

def to_the_end(root: Path, last: Direction=None) -> List[Direction]:
    if root == None or root.status == Path.Status.BLOCKED:
        return []
    
    if root.status == Path.Status.END:
        return [last]
    
    left  = to_the_end(root.left,  Direction.LEFT)
    right = to_the_end(root.right, Direction.RIGHT)

    if    left != []:
        return [last]  + left
    elif right != []:
        return [last] + right
    else:
        return []



def get_directions(cave: Cave) -> int:
    """
    Get the directions to the end of the cave.
    
    :param cave: A cave instance.
    :type cave: Cave
    """
    # Your code here:
    return to_the_end(cave.path)[1:]
