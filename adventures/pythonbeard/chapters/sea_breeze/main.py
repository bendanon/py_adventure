import random

from adventures.pythonbeard.chapters.sea_breeze.memory_module import get_name
from adventures.pythonbeard.common.subconscious import Subconscious
from utils.level_key import get_hash

known_names   = ["Pythonbeard", "Mommy", "Daddy", "1", "2", "3", "4"]

if __name__ == "__main__":
    pb_subconscious = Subconscious(known_names)

    user_res = get_name(pb_subconscious)

    print("Pythonbeards says: {}".format(user_res))
    print(get_hash(user_res))
