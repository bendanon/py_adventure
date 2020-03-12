import random

from adventures.pythonbeard.chapters.lets_sail_again.autopilot_module import sail_height
from utils.level_key import get_hash

path = [1, 3, 5, 2, 6, 5,
        2, 5, 30, 44, 11, 44,
        1, 33, 44, 5, 12, 4,
        1, 324, 432, 43, 432,
        1, 333, 42, 44, 2, 32]

if __name__ == "__main__":
    user_res = ""

    for location in path:
        curr_res = sail_height(location)
        print("Sail height: {}, at speed {}km/h".format(curr_res, location * 3.6))
        user_res += str(curr_res)

    print("Result : {}".format(get_hash(user_res)))
