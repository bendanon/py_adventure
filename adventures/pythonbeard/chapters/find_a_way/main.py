import random

from adventures.pythonbeard.chapters.find_a_way.searching_module import brightest_star
from adventures.pythonbeard.common.location import Location, LocationTypes
from utils.level_key import get_hash

stars = list(range(10, 70))

if __name__ == "__main__":
    random.shuffle(stars)
    user_res = brightest_star(stars)

    print("Pythonbeards says: {}".format(user_res))

    print("Result : {}".format(get_hash(str(user_res))))
