import os
from pathlib import Path

from adventures.pythonbeard.chapters.search_yourself.reading_module import search_string
from utils.level_key import get_hash

books_prefix = "adventures/pythonbeard/chapters/search_yourself/books"

book_list = ["a", "b", "c", "d", "e", "f", "g"]
name = "Pythonbeard"

if __name__ == "__main__":
    user_res = ""

    for book in book_list:
        path = os.path.join(os.path.curdir, books_prefix, book)
        res = search_string(name, path)

        if res:
            print("Found in book {}!".format(book))
        else:
            print("Not in {}".format(book))
        
        user_res += str(res)

    print("Result : {}".format(get_hash(user_res)))
