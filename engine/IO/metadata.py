import json
import atexit
import os.path

from utils.singletone import singletone

class MetaKeys:
    chapter = "chapter"

@singletone
class MetadataIO(object):
    def __init__(self, filename: str="", default_chapter: str="1"):
        super().__init__()
        self.metadata_file = filename
        self.cache = {
            MetaKeys.chapter : default_chapter
        }

        if filename == "":
            raise Exception("No metdata file was created, filename can't be empty")

        if os.path.exists(filename):
            with open(self.metadata_file, "r") as metafile:
                self.cache = json.load(metafile)
        else:
            with open(self.metadata_file, "w") as metafile:
                json.dump(self.cache, metafile)
        
        atexit.register(self.cleanup)
    
    def cleanup(self):
        with open(self.metadata_file, "w") as metafile:
           json.dump(self.cache, metafile)
    
    @property
    def current_chapter(self):        
        return self.cache[MetaKeys.chapter]
    
    @current_chapter.setter
    def current_chapter(self, new_chapter):
        self.cache[MetaKeys.chapter] = new_chapter

        # Save cache
        with open(self.metadata_file, "w") as metafile:
           json.dump(self.cache, metafile)

