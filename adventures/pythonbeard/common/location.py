class LocationTypes:
    """
    Types of locations in which the sailing can take place.
    """
    OPEN_SEA     = 0
    SHALOW_WATER = 1
    WHALE_SPOT   = 2


class Location(object):
    """
    Location class (Used to determine where an item is located).
    """

    def __init__(self, x: int, y: int, loc_type: int):
        """
        :param x: x
        :type x: int
        :param y: y
        :type y: int
        :param loc_type: the type of location in which this spot is located.
        :type loc_type: int
        """
        super().__init__()

        self.x = x
        self.y = y
        self.type = loc_type