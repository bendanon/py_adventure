from adventures.pythonbeard.common.location import Location, LocationTypes

# To avoid "magic numbers" in our code we can define constants which we will
# able to use in multiple other places.
# Commands:
SAIL_FAST = 0
SAIL_SLOW = 1
STOP = 2

# If you will type help(LocationTypes) you will be able to see another way of
# defining some constants. At this point you don't must use them. 

def get_command(location_type: int) -> int:
    """
    Get name the first name in mind.
    
    :param subconscious: Pythonbeard's subconscious.
    :type subconscious: Subconscious
    """
    # Your code here:
    return STOP if location_type is LocationTypes.WHALE_SPOT else \
        SAIL_FAST if location_type is LocationTypes.OPEN_SEA else SAIL_SLOW

def sail_at(current_location: Location) -> str:
    """
    sail_at a sertain location
    
    :param current_location: the location in which we need to sail
    :type current_location: Location
    :return: a string of what command pythonbeard should say
    :rtype: str
    """
    commamd = get_command(current_location.type)
    if commamd == SAIL_FAST:
        return "Fast"
    elif commamd == SAIL_SLOW:
        return "Slow down"
    elif commamd == STOP:
        return "Whales"
    else:
        return "I have no clue"