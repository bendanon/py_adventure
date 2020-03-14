from typing import List, NamedTuple

from adventures.pythonbeard.common.point import Point

# Again, There is another use of a name tuple, this time it was imported from
# the 'typing module, so, the types of the properties are clearer. 
StrengthPoint = NamedTuple("StrengthPoint", [("point", Point), ("strength", int)])


def find_weak_spots(points: List[StrengthPoint]) -> List[StrengthPoint]:
    """
    Find the 10 smallest strength point (by strength) in the given array.

    :param points: an array of strength points.
    :type points: List[StrengthPoint]
    :return: a sorted list of the ten smallest numbers in the given array.
    :rtype: List[StrengthPoint]
    """
    # Your code here:
    return sorted(points, key=lambda sp: sp.strength)[:10]