Command = str
# The commands:
PUSH = "push"
PULL = "pull"

def start_a_fire() -> Command:
    """
    Alternates between push and pull (starting from push).

    :return: The next command (between push and pull).
    :rtype: Command
    """
    # Your code here:
    while True:
        yield PUSH
        yield PULL


"""
last = PULL
def start_a_fire() -> Command:
    \"""
    Alternates between push and pull (starting from push).

    :return: The next command (between push and pull).
    :rtype: Command
    \"""
    # Your code here:
    global last
    if last == PULL:
        last = PUSH
        return PUSH
    last = PULL
    return PULL
"""
