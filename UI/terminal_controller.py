import shutil
from typing import Callable, Tuple

from engine.types.aliases import InputHandler
from definitions import os_name

MIN_HEIGHT = 20 # The minimum height of the console

class TerminalController(object):
    def __init__(self):
        super().__init__()

        # Terminal metadata
        self.terminal_height = shutil.get_terminal_size((80, 20)).lines
        self.terminal_width = shutil.get_terminal_size((80, 20)).columns

        # Initiate text positions
        self.main_title_pos      = 1
        self.secondary_title_pos = 3
        self.first_text_pos      = 7
        self.second_text_pos     = 12
        self.hidden_text_pos     = 14
        self.input_pos           = 16

        # Initiate text
        self.main_title      = ""
        self.secondary_title = ""
        self.first_text      = ""
        self.second_text     = ""
        self.hidden_text     = ""

        # Initiate metadata
        self.view_hidden     = False
        self.input_array     = []

        if self.terminal_height < MIN_HEIGHT:
            raise Exception("Terminal size is too small")
    
    def wipe_screen(self):
        """
        Wipe the screen clean.
        """
        if os_name == "linux":
            self.move(0)
            print((" " * self.terminal_width + "\r\n") * self.terminal_height)
            self.move(0)
        else:
            pass

    def move(self, y: int):
        """
        Move the cursor to a position on the screen.
        
        :param x: the X position.
        :type x: int
        :param y: the Y position.
        :type y: int
        """
        if os_name == "linux":
            print("\033[{};{}H".format(y, 0), end="")
        else:
            pass
    
    def get_input(self, input_callback: InputHandler = lambda a: (a, False) \
                                                            if a != "q" \
                                                            else (a, True)) \
                                                    -> bool:
        """
        Get input from the user via the terminal.
        
        :param input_callback: A function which processes the user input,
                               returns print value and whether or not to continue
                               getting input.
        :type input_callback: InputHandler, optional
        :return: the boolean result of the callable method.
        :rtype: bool
        """
        input_string = "     >  "
        user_input = input(input_string)
        self.input_array.append(input_string + user_input)

        response = input_callback(user_input)
        self.input_array.append(response[1])

        self.refrash_input()

        return response[0]
    
    def print_at(self, text: str, position: int):
        """
        Print given text at given position.
        
        :param text: text to print.
        :type text: str
        :param position: position to print at.
        :type position: int
        """
        self.move(position)
        print(text)
    
    def refrash(self):
        """
        Refrash display.
        """
        self.wipe_screen()

        # Set main title
        self.print_at(" " * ((self.terminal_width - len(self.main_title)) // 2) + 
                        self.main_title.upper() + 
                        " " * self.terminal_width,
                      self.main_title_pos)

        # Set secondary title
        wrapper = "-" * ((self.terminal_width - len(self.secondary_title)) // 3)
        self.print_at(wrapper + self.secondary_title + wrapper * 2,
                      self.secondary_title_pos)

        # Set first text
        self.print_at(self.first_text, self.first_text_pos)

        # Set secondary text
        self.print_at(self.second_text, self.second_text_pos)

        # Set hidden text
        if self.view_hidden:
            self.print_at(self.hidden_text, self.hidden_text_pos)

        # Set the input
        self.print_at("-" * self.terminal_width, self.input_pos)

        self.input_array = []
        self.view_hidden = False
    
    def refrash_input(self):
        """
        Refrash the input view
        """
        # Wipe input screen
        if os_name == "linux":
            self.move(self.input_pos + 1)
            print((" " * self.terminal_width + "\r\n") * (self.terminal_height - self.input_pos - 2))

            self.move(self.input_pos + 1)
            left_rows = self.terminal_height - self.input_pos - 3

            print("\r\n".join(self.input_array[-left_rows:]))
        else:
            print(self.input_array[-1])
    
    def enable_hidden_text(self):
        """
        Show the hidden text and update the screen.
        """
        self.view_hidden = True
        self.refrash()

