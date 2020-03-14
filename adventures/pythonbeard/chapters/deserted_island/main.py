from adventures.pythonbeard.chapters.deserted_island.adventure_module import start_a_fire
from typing import Generator
from utils.level_key import get_hash


if __name__ == "__main__":

    print("You picked up a bow, board and a stick, put the stick in the string of the bow placed")
    print("int the middle of the board and started:")

    res = ""

    starter = start_a_fire()
    if isinstance(starter, Generator):
        for command, i in zip(starter, range(10)):
            res += command
            print("\t{}ing".format(command))
    else:
        res = starter
        print("\t{}ing".format(starter))
        for i in range(9):
            l = start_a_fire()
            res += l
            print("\t{}ing".format(l))
    
    print("A fire had started")
    print("Result : {}".format(get_hash(str(res))))

