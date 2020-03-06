from adventures.pythonbeard.chapters.stormy_sail.talk_module import speak
from utils.level_key import get_hash

if __name__ == "__main__":
    players_output = speak() if speak() is not None else None

    if players_output == None or not isinstance(players_output, str):
        print("You Must return a value, please try again after you fix the function")
    else:
        print("Pythonbeard says : {}".format(players_output))
        print("Result : {}".format(get_hash(players_output)))
