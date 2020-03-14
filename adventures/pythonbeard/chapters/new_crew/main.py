import random

from adventures.pythonbeard.chapters.new_crew.arithmetic_module import create_crew, Contendent
from utils.level_key import get_hash

contendents = [
    Contendent("Jeff", 20),
    Contendent("Mike", 30),
    Contendent("mr. Fart", 18),
    Contendent("Moonman", 13),
    Contendent("Rick", 12),
    Contendent("Mort", 24),
    Contendent("Alex", 7)
]

if __name__ == "__main__":

    given_money = 50
    
    user_result = create_crew(contendents, given_money)

    print("Your list:")
    for contendent in user_result:
        print("\t{}".format(contendent))
    
    print("Result : {}".format(get_hash(str(list(user_result)))))