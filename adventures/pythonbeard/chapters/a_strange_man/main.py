from adventures.pythonbeard.chapters.a_strange_man.geometry_module import center_of_polygon, Point
from utils.level_key import get_hash


triangle = [
    Point(0,0),
    Point(0,6),
    Point(6,0)
]

if __name__ == "__main__":

    match = center_of_polygon(triangle)

    print("Found at : {}".format(match))
    print("Result : {}".format(get_hash(str(match))))

