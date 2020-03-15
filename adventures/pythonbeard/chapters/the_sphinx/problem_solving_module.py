
def get_roman_regex() -> str:
    """
    Get the regular expresion which identifies the roman numeral counting.

    :return: The regex.
    :rtype: str
    """
    # Your code here:
    return "^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"