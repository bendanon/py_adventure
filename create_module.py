from engine.IO.metadata import MetadataIO
from engine.IO.adventure import AdventureIO
from utils.symlink_factory import create_symlink
from definitions import *

import shutil
import os
import hashlib
import subprocess
import json

if __name__ == "__main__":
    # Create the meta singletone
    MetadataIO(metafile)

    # Get chapters info
    chapter_key = MetadataIO().current_chapter

    with AdventureIO(os.path.join(os.path.curdir, adventure_folder, adventure_chapters)) as adventure:
        chapter_title = adventure.chapters[chapter_key].title
    
    # Set the currect folder name
    chapter_env = os.path.join(os.path.curdir, 
                               adventure_folder,
                               chapters_folder,
                               chapter_title.replace(" ", "_").lower())
    
    # Create the title
    width = shutil.get_terminal_size().columns
    execution_title = "[Executing Chaper : {}]".format(chapter_title)
    wrapper_left = "-" * ((width - len(execution_title)) // 5)
    wrapper_right = "-" * (width - len(execution_title) - len(wrapper_left))
    print("{}{}{}".format(wrapper_left, execution_title, wrapper_right))

    meta = {}
    with open(os.path.join(chapter_env,
                           ".meta.json")) as metafile:
        meta = json.load(metafile)
    
    create_symlink(editable_file, chapter_title)
    
    # Execute running file
    exec(open(os.path.join(chapter_env, 
                           meta["main"])).read())
