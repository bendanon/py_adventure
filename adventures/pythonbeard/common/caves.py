from enum import Enum
from typing import NamedTuple, List

PathBuilder = NamedTuple('PathBuilder', [('is_end', bool), ('has_left', bool), ('has_right', bool)])

class Path(object):
    """
    Path object to show forks in the caves and path.
    Acts like a binary tree.

    Properties: 
        - id      - the id of the point.
        - left    - the path to the left (None if there is none).
        - right   - the path to the right (None if there is none).
        - status  - the status of the path
    """
    class Status(Enum):
        """
        Path status.
        """
        END = 0
        OPEN = 1
        BLOCKED = 2
    
    def __init__(self, id: int, 
                       left=None, 
                       right=None, 
                       status=Status.BLOCKED):
        self.id = id
        self.left = left
        self.right = right
        self.status = status
    
    def __repr__(self):
        return "[{:>3}] left ({:>5})    right ({:>5})    status ({:>9})".format(self.id, 
                self.left.id  if self.left  is not None else "None",
                self.right.id if self.right is not None else "None",
                self.status.name)
    
    @staticmethod
    def from_list(current_path, layout: List[PathBuilder], index=0) -> int:
        """
        converts a list of path builders items to a path.
        
        :param current_path: The path to start from.
        :type current_path: Path
        :param layout: the map layout.
        :type layout: List[PathBuilder]
        :param index: the index to start from, defaults to 0
        :type index: int, optional
        :return: the index which was reached.
        :rtype: int
        """
        current_path.id     = index
        current_path.left   = None
        current_path.right  = None
        
        # The leaf wasn't registered
        if index >= len(layout):
            return index

        # Is the end
        if layout[index].is_end:
            current_path.status = Path.Status.END
            return index
        
        # Create Blockage if the there is no path
        if not layout[index].has_left and not layout[index].has_right:
            current_path.status = Path.Status.BLOCKED
            return index

        next_index = index + 1

        # Create the left path
        if layout[index].has_left:
            current_path.status = Path.Status.OPEN
            current_path.left = Path(next_index)
            next_index = Path.from_list(current_path.left, layout, next_index) + 1

        # Create the right path
        if layout[index].has_right:
            current_path.status = Path.Status.OPEN
            current_path.right = Path(next_index)
            next_index = Path.from_list(current_path.right, layout, next_index) + 1
        
        return next_index - 1

class Cave(object):
    """
    Cave object which holds the cave layout.

    Properties: 
        - path   - the path in the cave.
    """
    def __init__(self, layout: List[PathBuilder]):

        self.path = Path(0)
        Path.from_list(self.path, layout)
