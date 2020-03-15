import random

from adventures.pythonbeard.chapters.challenge_of_the_queen.problem_solving_module import queens
from utils.level_key import get_hash


if __name__ == "__main__":    
    print("Pythonbeard Says : {}".format(queens()))

    print("Result : {}".format(get_hash(str(queens()))))
