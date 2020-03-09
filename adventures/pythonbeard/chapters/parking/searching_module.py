from typing import List
from adventures.pythonbeard.common.ship import Ship

Index = int

def search_parking(ship: Ship, shore: List[int]) -> Index:
    """
    Search a long enough parking spot near the shore.

    :param ship: the ship to search the parking for.
    :type ship: Ship
    :param shore: all the parking spots lengths along the shore.
    :type shore: List[int]
    :return: The matching index from the given list.
    :rtype: Index(int)
    """
    # Your code here:
    return shore.index(min(spot for spot in shore if spot > ship.legnth))