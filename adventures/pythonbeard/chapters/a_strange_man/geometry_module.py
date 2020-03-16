from collections import namedtuple
from typing import List

# This is a namedtuple, an name tuple is a part of the 'collections' module,
# which contains many special collections types (as the name suggests).

# A name tuple is an easy way to create a basic structure which in herits
# from the normal tuple but, has names for each index in it.
Point = namedtuple("Point", ["x", "y"])

def center_of_polygon(points: List[Point]) -> Point:
    """
    Find the center of a polygon using the coordinates of each vertex.

    :param points: an array of points.
    :type points: List[Point]
    :return: The center of given points.
    :rtype: Point
    """
    # Your code here:
    pass