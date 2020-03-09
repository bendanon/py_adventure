from typing import List

class Subconscious(object):
    """
    The subconscious of a character. 
    """

    def __init__(self, names: List[str]=[]):
        """
        :param names: a list of known names, defaults to []
        :type names: List[str], optional
        """
        self.names = names

    def get_names(self) -> List[str]:
        """
        Get the names from the subconscious. 
        
        :return: names list
        :rtype: List[str]
        """
        return self.names

