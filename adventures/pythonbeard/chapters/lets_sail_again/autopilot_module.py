def ms_to_kmh(speed: float) -> float:
    return speed * 3.6

def sail_height(speed: float) -> float:
    """
    Get the speed of the wind in (m/s) and return the suggested 
    height of the sail.
    
    :param speed: The current speed of the wind.
    :type speed: float
    :return: The height of the sails.
    :rtype: float
    """
    # Your code here:
    return 1 if ms_to_kmh(speed) < 11 else 0.5 if ms_to_kmh(speed) > 20 else 0.75
