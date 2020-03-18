import subprocess
import os

from typing import Callable, Generator, Tuple

from engine.types.chapter import Chapter
from engine.types.aliases import InputHandler, InputResult
from UI.chapter_handler import IChapterHandler
from UI.terminal_controller import TerminalController
from utils.roman_numeric import to_roman
from definitions import os_name

class CliChapterHandler(IChapterHandler):
    """
    An UI chapter handler.
    """

    def __init__(self, controller: TerminalController):
        """
        :param controller: the CLI controller.
        :type controller: TerminalController
        """
        self.controller = controller
    
    def parse_answer(self, chapter: Chapter) -> InputHandler:
        """
        Created a function which parses a given user input.
        
        :param chapter: the chapter to check.
        :type chapter: Chapter
        :return: function which parses a given user input.
        :rtype: InputHandler
        """

        def input_handler(user_input: str) -> InputResult:
            """
            Parse  users input
            
            :param user_input: the input user to parse.
            :type user_input: str
            :return: first pos  - continue getting input or not.
                     second pos - string to print.
            :rtype: InputResult
            """
            if user_input == "help":
                self.controller.enable_hidden_text()
                return True, ""
            if user_input == "skip":
                return False, ""
            if user_input == "run":
                subprocess.call(["python3" if os_name == "linux" else "python", 
                                 (os.path.join(os.path.curdir, "create_module.py"))])
                return True, ""
            else:
                chaper_result = chapter.check_answer(user_input)
                return not chaper_result, "Well done!" if chaper_result \
                                            else "Nice try, have another go..."
        
        return input_handler

    def show(self, chapter: Chapter):
        """
        Print the current chapter to the user.
        
        :param chapter: the current chapter.
        :type chapter: Chapter.
        """
        # Print chapter info
        self.controller.secondary_title = \
            "Chapter {} : {}".format(to_roman(chapter.key + 1), chapter.title)
        
        self.controller.first_text = ("\r\n ". join(chapter.story) 
                                        if isinstance(chapter.story, list) 
                                        else chapter.story)
        self.controller.second_text = ("\r\n ". join(chapter.riddle) 
                                        if isinstance(chapter.riddle, list) 
                                        else chapter.riddle)
                
        self.controller.hidden_text = "Hint:    " + chapter.hint

        self.controller.refrash()

        # Get the currect answer from the user
        while self.controller.get_input(self.parse_answer(chapter)):
            pass
