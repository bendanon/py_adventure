from typing import List
from collections import defaultdict

from adventures.pythonbeard.common.languages import Language

class Subconscious(object):
    """
    The subconscious of a character. 
    
    Properties: 
        - names  - the known names of the characters.
    """

    def __init__(self, names: List[str]=[], known_languages=defaultdict(dict)):
        """
        :param names: a list of known names, defaults to []
        :type names: List[str], optional
        """
        self.names = names
        self.__known_languages = known_languages

    def get_names(self) -> List[str]:
        """
        Get the names from the subconscious. 
        
        :return: names list
        :rtype: List[str]
        """
        return self.names
    
    def get_dictionary(self, language: Language):
        """
        Get a dictionary of a language.
        
        :param language: the language to get the dictionary of.
        :type language: Language
        """
        return self.__known_languages[language]

