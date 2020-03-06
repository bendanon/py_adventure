# This function (compare_widths) gets 2 ARGUMENTS the ships width and the path width.
# an argument is a variable which function gets in order to preform a 
# repetitive task on. like in this situation for example... when you need
# to repetitively compare widths in order to determine which path is suitable

# Next to each argument there is a TYPE (': int'), this is not necessary but it helps
# us define what the function should get. this is called type hinting.

# An int (a short for intger), the type we had specified, is a number which we can
# do simple arithmetics with:
#   - '+' - for adding.
#   - '-' - for subtracting.
#   - '*' - for multiplying.
#   - '/' - for devision.
# And compare them:
#   - '>'  - bigger then.
#   - '<'  - smaller then.
#   - '==' - equal to.
#   - '>=' - bigger or equal to.
#   - '<=' - smaller or equal to.

# After the brackets we can see a '-> bool' (also type hinting) meaning the function 
# returns a boolean. A boolean has two states 'True' or 'False'. when we compare items.
# the return value is boolean.

# In the first lines of the function the is a big comment which is call docstring.
# the docstring is use to describe to the user of the function what the function does
# and how to use it.  

def compare_widths(ships_width: int, paths_width: int) -> bool:
    """
    Compare two numbers.
    
    :param ships_width: the width of the ship. 
    :type ships_width: int
    :param paths_width: the width of the path.
    :type paths_width: int
    :return: True if the width of the path is bigger then the width of the ship.
    :rtype: bool
    """
    # Your code here:
    return ships_width < paths_width