import random

from adventures.pythonbeard.chapters.tight_spots.arithmetic_module import compare_widths
from utils.level_key import get_hash

ships_width = 20

path_widths = [10, 30, 23, 21, 20, 15, 24]

if __name__ == "__main__":
    
    user_results    = map(lambda paths_width: compare_widths(ships_width, paths_width), path_widths)

    for user, width in zip(user_results, path_widths):
        if user ^ (ships_width < width):
            print("You crashed at: {}".format(width))
        else:
            if not user:
                print("You dodged path: {}".format(width))

    print("Result : {}".format(get_hash(str(list(user_results)))))