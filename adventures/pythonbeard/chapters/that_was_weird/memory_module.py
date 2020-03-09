from adventures.pythonbeard.common.subconscious import Subconscious

# There are many ways to solve this riddle, Try figuring it out by your own.
# If you struggle try writing help in the cli of the game. 

def get_name(subconscious: Subconscious, leading_chars: str) -> str:
    """
    Get name the first name in mind.
    
    :param subconscious: Pythonbeard's subconscious.
    :type subconscious: Subconscious
    """
    # Your code here:
    return list(filter(lambda name: name.startswith(leading_chars), subconscious.get_names()))[0]