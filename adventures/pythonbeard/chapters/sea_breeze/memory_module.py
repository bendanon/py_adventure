from adventures.pythonbeard.common.subconscious import Subconscious

# Here we can see our first none basic python object 'subconscious'.
# This is an object or better called a class which contains all of 
# Pythonbeard's subconsciousness.
# Remember all of thous doctrings? well now you will see how handy they are
# if you will write help(subconscious) you will be able to see that class's
# doctring to get a better grap about what it is (and to his inner functions).

# What is a class? 
# A class is a template for an object. Meaning a collection of behaviors
# and properties which are all helping the progeramer to preform task using
# the object.
# What is an object?
# Variable, data structure, function, etc... (an instance a class). 

# The names in the subconscious are kept in a list. What is list you ask?
# A list is like the name suggests an array/collection of data which is kept
# in a sertain order (the order you put the item in). In order to get an item
# from said list we can use '[x]' where x is the index(number) of item that you want
# to get from the list. In python like in many other languages the indexing (meaning
# the locations in which the items are stored) starts with 0 and not 1 (there are
# languages in which the indexing starts with 1. I don't know any language where the 
# indexing starts with 2/3/...).

# See how can you get the first item from the names list in Pythonbeard's subconscious.

def get_name(subconscious: Subconscious) -> str:
    """
    Get name the first name in mind.
    
    :param subconscious: Pythonbeard's subconscious.
    :type subconscious: Subconscious
    """
    # Your code here:
    return subconscious.get_names()[0]