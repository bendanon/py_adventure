import os

from definitions import editable_file
from utils.symlink_factory import init_symlink

class Chapter:
    """
    A chapter class. 
    Acts as the logic layer of the chapter engine.
    """
    
    def __init__(self, key: int, title: str, story: str, riddle: str, 
                       hint: str, answer: str):
        """
        :param key: the key of the chapter.
        :type key: int
        :param title: the title of the chapter.
        :type title: str
        :param story: the story.
        :type story: str
        :param riddle: the riddle.
        :type riddle: str
        :param hint: a hint for the riddle.
        :type hint: str
        :param answer: a answer of the riddle.
        :type answer: str
        """
        self.key    = key     
        self.title  = title   
        self.story  = story   
        self.riddle = riddle  
        self.hint   = hint    
        self.answer = answer
    
    def check_answer(self, user_answer: str) -> bool:
        """
        Check the answer of the user
        
        :param user_answer: the given answer from the user
        :type user_answer: str
        :return: whether or not the user answered correctly.
        :rtype: bool
        """
        return self.answer == user_answer
    
    def startup(self):
        """
        Startup the chapter
        """
        init_symlink(editable_file, self.title)
    
    def shutdown(self):
        """
        Wrap up the chapter
        """
        pass
