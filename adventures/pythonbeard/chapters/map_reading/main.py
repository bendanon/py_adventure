from adventures.pythonbeard.chapters.map_reading.geometry_module import sort_points
from adventures.pythonbeard.common.point import Point
from utils.level_key import get_hash


points = [
    Point(0,6),
    Point(1,0),
    Point(0,0),
    Point(2,0),
    Point(0,1),
    Point(1,1),
    Point(6,0)
]

if __name__ == "__main__":

    sorted_p = sort_points(points)

    print("Found at : {}".format(sorted_p))
    print("Result : {}".format(get_hash(str(sorted_p))))

