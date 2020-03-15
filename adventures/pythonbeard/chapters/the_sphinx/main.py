import re

from adventures.pythonbeard.chapters.the_sphinx.problem_solving_module import get_roman_regex
from utils.level_key import get_hash


if __name__ == "__main__":    
    check_thouse = [
        "I",
        "IVX",
        "II",
        "IIV",
        "D",
        "MMMDCCXXIV",
        "XXX",
        "aaaa",
        "WWW"
    ]

    print("Pythonbeard Says : The regex is :{}".format(get_roman_regex()))

    results = []

    print("The sphinx  Says : Lets test you")
    for item in check_thouse:
        answer = "{} {} {}".format(item, 
                                   "is" if re.match(get_roman_regex(), item) != None 
                                        else "is not" ,
                                    "roman")
        print(answer)
        results.append(answer)

    print("Result : {}".format(get_hash(str(results))))
