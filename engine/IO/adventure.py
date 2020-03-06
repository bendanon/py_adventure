import json

from engine.types.adventure import Adventure


class AdventureIO(object):
    """
    An IO adventure class.
    Acts as the data managemnet layer.
    """

    def __init__(self, filename: str):
        """        
        :param filename: the filename of the chapters file.
        :type filename: str.
        """
        super().__init__()
        self.filename = filename
    
    def __enter__(self):
        """
        :return: a namespace of the adventure file.
        :rtype: Adventure
        """
        with open(self.filename) as adventure_file:
            adventure = json.load(adventure_file)
        
        return Adventure(**adventure)
    
    def __exit__(self, type, value, traceback):
        pass
