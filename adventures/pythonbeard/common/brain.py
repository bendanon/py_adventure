from adventures.pythonbeard.common.subconscious import Subconscious


class Brain(object):
    """
    This is pythonbead's brain here lays everything he knows,
    his actions, his thoughts and secrets. 

    Properties:
        - subconscious - subconscious of the brain.
    """

    def __init__(self, subconscious: Subconscious):
        """
        :param subconscious: pythonbeard's subconscious.
        :type subconscious: Subconscious
        """
        super().__init__()

        self.subconscious = subconscious

    def get_subconscious(self) -> Subconscious:
        """
        Get pythonbeard's subconscious.
        
        :return: pythonbeard's subconscious.
        :rtype: Subconscious
        """
        return self.subconscious
