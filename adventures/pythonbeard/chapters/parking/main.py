from adventures.pythonbeard.chapters.parking.searching_module import search_parking
from adventures.pythonbeard.common.ship import Ship
from utils.level_key import get_hash

if __name__ == "__main__":
    parking_spots = range(10, 20, 2)
    ship = Ship(5, 15)

    match = search_parking(ship, parking_spots)

    print("Found at : {}".format(match))
    print("Result : {}".format(get_hash(str(match))))
