from typing import Tuple, Callable


InputResult =  Tuple[bool, str]
InputHandler = Callable[[str], InputResult]
