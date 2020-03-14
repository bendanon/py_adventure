upper_starting_char = 'A'
upper_ending_char = 'Z'

lower_starting_char = 'a'
lower_ending_char = 'z'

charecters = ord(lower_ending_char) - ord(lower_starting_char) + 1


def decipher(string: str, key: int) -> str:
    """
    Decipher the given string.
    
    :param string: the string to decipher.
    :type string: str
    :param key: the key to decipher with.
    :type key: int
    :return: the deciphered string.
    :rtype: str
    """
    # Your code here:
    return "".join([chr((ord(ch) - ord(lower_starting_char 
                                        if ch.islower() 
                                        else upper_starting_char) - key) % \
                    charecters + ord(lower_starting_char 
                                        if ch.islower() 
                                        else upper_starting_char)) 
                    if ch.isalpha() else ch for ch in string])
