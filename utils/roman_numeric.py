from collections import namedtuple

RomanDictionaryItem = namedtuple('RomanDictionaryItem', 
                                "value \
                                 letter \
                                 complementary_value \
                                 complementary_letter") 

ROMAN_NUMERICAL_DICT = [RomanDictionaryItem(1000, 'M', 100, 'C'), 
                        RomanDictionaryItem(500,  'D', 100, 'C'), 
                        RomanDictionaryItem(100,  'C', 10,  'X'), 
                        RomanDictionaryItem(50,   'L', 10,  'X'), 
                        RomanDictionaryItem(10,   'X', 1,   'I'), 
                        RomanDictionaryItem(5,    'V', 1,   'I'), 
                        RomanDictionaryItem(1,    'I', 0,   '') ]

def to_roman(number: int, index: int = 0) -> str:
    """
    Converts from a decimal number to a roman numeral format.
    
    :param number: the number to convert.
    :type number: int
    :param index: the index in the convertion table, defaults to 0.
    :type index: int, optional
    :return: the converted roman numeral format.
    :rtype: str
    """
    if number == 0:
        return ""

    if number - ROMAN_NUMERICAL_DICT[index].value < 0:
        if number + ROMAN_NUMERICAL_DICT[index].complementary_value - \
            ROMAN_NUMERICAL_DICT[index].value < 0:

            return to_roman(number, index + 1)
        else:
            return ROMAN_NUMERICAL_DICT[index].complementary_letter + \
                    ROMAN_NUMERICAL_DICT[index].letter + \
                    to_roman(number + ROMAN_NUMERICAL_DICT[index].complementary_value - \
                             ROMAN_NUMERICAL_DICT[index].value, index)
    else:
        return ROMAN_NUMERICAL_DICT[index].letter + \
                to_roman(number - ROMAN_NUMERICAL_DICT[index].value, index)

