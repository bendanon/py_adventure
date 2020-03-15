import random

from adventures.pythonbeard.chapters.atlantis.numbering_module import roman_to_decimal
from utils.level_key import get_hash

numbers = [
    "XIV",
    "LXXIX",
    "CCXXV",
    "DCCCXLV",
    "MMXXII"
]

if __name__ == "__main__":
    user_sum = 0
    
    for  num in numbers:
        print("{} - {}".format(num, roman_to_decimal(num)))
        user_sum += roman_to_decimal(num)

    print("Result : {}".format(get_hash(str(user_sum))))
