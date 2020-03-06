from utils.level_key import get_hash
import sys

def print(arg):
    sys.stdout.write(arg + "\r\n")
    sys.stdout.write("Result : {}\r\n".format(get_hash(arg)))
