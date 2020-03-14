from typing import List, NamedTuple
from enum import Enum

# In the entangled forset it's the time to start and figure things alone from 
# google and the python doc (if you haven't started by now). try and understand
# using this two definitions, if you need more info you should google it by 
# your own and after that ask one of the instractors.

# ----------------------------[Enum]-------------------------------------------
#   (from wikipedia): In computer programming, an enumerated type is a data 
# type consisting of a set of named values called elements, members, enumeral, 
# or enumerators of the type.
#   (from python docs): An enumeration is a set of symbolic names (members) 
# bound to unique, constant values. Within an enumeration, the members can be 
# compared by identity, and the enumeration itself can be iterated over.


# Defining Enums in python:
class Status(Enum):
    OPEN = 0
    BLOCKED = 1

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# Another instance of typed name tuple this time using enums
Path = NamedTuple("Path", [("direction", Direction), ("status", Status)])

def find_open_path(paths: List[Path]) -> Path:
    """
    Search for the brightest star in the given star array.

    :param paths: list of all the paths.
    :type paths: List[Path]
    :return: The first open path in the given list.
    :rtype: Path
    """
    # Your code here:
    return list(filter(lambda path: path.status is Status.OPEN, paths))[0]