from typing import List
from adventures.pythonbeard.common.ship import Ship

# Defining that a star is basically an integer where the value is it's 
# brightness 
Star = int

def brightest_star(stars: List[Star]) -> Star:
    """
    Search for the brightest star in the given star array.

    :param stars: list of all the stars.
    :type stars: List[Star]
    :return: The brightest start from the given list.
    :rtype: Start(int)
    """
    # Your code here:
    return max(stars)