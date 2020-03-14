from adventures.pythonbeard.chapters.the_kraken.fighting_module import find_weak_spots, StrengthPoint
from adventures.pythonbeard.common.point import Point
from utils.level_key import get_hash


points = [
    StrengthPoint(Point(0,0), 1),
    StrengthPoint(Point(1,0), 2),
    StrengthPoint(Point(2,0), 12),
    StrengthPoint(Point(3,0), 100),
    StrengthPoint(Point(4,0), 74),
    StrengthPoint(Point(5,0), 23),
    StrengthPoint(Point(0,1), 37),
    StrengthPoint(Point(0,2), 8),
    StrengthPoint(Point(0,3), 9),
    StrengthPoint(Point(0,4), 79),
    StrengthPoint(Point(0,5), 7),
    StrengthPoint(Point(0,0), 34),
    StrengthPoint(Point(1,1), 6),
    StrengthPoint(Point(2,2), 20),
    StrengthPoint(Point(3,3), 4),
    StrengthPoint(Point(2,3), 12),
    StrengthPoint(Point(1,3), 16),
    StrengthPoint(Point(1,2), 12),
    StrengthPoint(Point(2,1), 10),
    StrengthPoint(Point(3,4), 19)
]

if __name__ == "__main__":

    sorted_p = find_weak_spots(points)

    print("The weakspots are :")
    for p in sorted_p:
        print("\t{}".format(p))
    print("Result : {}".format(get_hash(str(sorted_p))))

