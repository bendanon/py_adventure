import random

from adventures.pythonbeard.chapters.lets_sail.autopilot_module import sail_at
from adventures.pythonbeard.common.location import Location, LocationTypes
from utils.level_key import get_hash

locations = [Location(0, 0, LocationTypes.OPEN_SEA),
             Location(0, 1, LocationTypes.SHALOW_WATER),
             Location(0, 2, LocationTypes.SHALOW_WATER),
             Location(0, 3, LocationTypes.OPEN_SEA),
             Location(0, 4, LocationTypes.WHALE_SPOT),
             Location(0, 5, LocationTypes.SHALOW_WATER)]

if __name__ == "__main__":
    user_res = ""

    for location in locations:
        curr_res = sail_at(location)
        print("Pythonbeards says: {}".format(curr_res))
        print("Crew response: {}".format("Aye Aye!!"))
        user_res += curr_res

    print(get_hash(user_res))
