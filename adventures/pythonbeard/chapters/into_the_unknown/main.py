import random

from adventures.pythonbeard.chapters.into_the_unknown.memory_module import translate_word
from adventures.pythonbeard.common.subconscious import Subconscious
from adventures.pythonbeard.common.languages import Language, atlasian
from utils.level_key import get_hash

atlasian_text = "Atlantis bing houmbala bam bang " \
                "shonta houmba sembe hercumba er " \
                "tang Atlantis shing Daraga "

if __name__ == "__main__":
    pb_subconscious = Subconscious(known_languages={Language.Atlasian: atlasian})

    normal = []

    for word in atlasian_text.split():
        normal.append(translate_word(pb_subconscious, word))
    
    translated = " ".join(normal)

    print("Translated: {}".format(translated))
    print("Result : {}".format(get_hash(translated)))
