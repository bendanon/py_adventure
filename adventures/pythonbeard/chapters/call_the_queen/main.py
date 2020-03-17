import subprocess
import time
import os.path

from adventures.pythonbeard.chapters.call_the_queen.problem_solving_module import call_queen
from adventures.pythonbeard.chapters.call_the_queen.definitions import *
from definitions import os_name

if __name__ == "__main__":
    subprocess.Popen(["python3" if os_name == "linux" else "python", (os.path.join(os.path.curdir, 
                      "adventures/pythonbeard/chapters/call_the_queen/start_queen.py"))])
    time.sleep(1)
    call_queen(IP, PORT, MESSAGE)
