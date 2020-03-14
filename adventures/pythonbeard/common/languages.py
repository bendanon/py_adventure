from enum import Enum
from collections import defaultdict

class Language(Enum):
    Atlasian = 0

atlasian = defaultdict(str)
atlasian["Atlantis"] = "Atlantis"
atlasian["atlantis"] = "Atlantis"
atlasian["bing"]     = "is"
atlasian["houmbala"] = "in"
atlasian["bam"]      = "grave"
atlasian["bang"]     = "danger"
atlasian["shonta"]   = "which"
atlasian["houmba"]   = "man"
atlasian["sembe"]    = "will"
atlasian["hercumba"] = "save"
atlasian["er"]       = "the"
atlasian["tang"]     = "city"
atlasian["shing"]    = "from"
atlasian["Daraga"]   = "Dragon"
atlasian["daraga"]   = "Dragon"
