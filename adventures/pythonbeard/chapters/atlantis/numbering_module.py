
# Some helpful dictionary:
ROMAN = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def roman_to_decimal(number: str) -> int:
    """
    Convert a roman number to a decimal(hindu-arbian) number.

    :param number: the number to convert.
    :type number: str
    :return: the value of the given number.
    :rtype: int
    """
    # Your code here:
    return sum([(-ROMAN[sign]) if   ROMAN[next_sign] > ROMAN[sign] 
                               else ROMAN[sign]
                for sign, next_sign in zip(number, number[1:] + "I")])