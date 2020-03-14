from adventures.pythonbeard.common.subconscious import Subconscious
from adventures.pythonbeard.common.languages import Language

# Dictionaries in python can be a bit tricky. basically they are lists
# but the indexing is based on words and not numbers.

def translate_word(subconscious: Subconscious, word: str) -> str:
    """
    Translate given word to Atlasian.
    
    :param subconscious: Pythonbeard's subconscious.
    :type subconscious: Subconscious
    :param word: The word to translate.
    :type word: str
    :return: The tarnslated word.
    :rtype: str.
    """
    # Your code here:
    return subconscious.get_dictionary(Language.Atlasian)[word]
