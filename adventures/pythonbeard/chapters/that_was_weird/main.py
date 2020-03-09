import random

from adventures.pythonbeard.chapters.that_was_weird.memory_module import get_name
from adventures.pythonbeard.common.subconscious import Subconscious
from utils.level_key import get_hash

known_names   = ["Pythonbeard", "Mommy", "Daddy", "Bob", "Mr. Donald", "Fartface", "No"]

if __name__ == "__main__":
    pb_subconscious = Subconscious(known_names)

    user_res = get_name(pb_subconscious, "Bo")

    print("Pythonbeards says: {}".format(user_res))
    print("Result : {}".format(get_hash(user_res)))
