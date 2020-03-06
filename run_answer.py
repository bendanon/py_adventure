from engine.IO.metadata import MetadataIO
from engine.IO.adventure import AdventureIO

import shutil
import os
import hashlib
import subprocess
import json

adventure_folder = "adventures/pythonbeard"    
chapters_folder = "chapters"
adventure_chapters = "chapters_story.json"


if __name__ == "__main__":
    # Create the meta singletone
    MetadataIO("meta.json")

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
    
    # Create symlink
    if os.path.lexists("./edit_this.py"):
        os.remove("./edit_this.py")
    
    os.symlink(os.path.join(chapter_env,
                            meta["symlink"]), "./edit_this.py")
    # Execute running file
    exec(open(os.path.join(chapter_env, 
                           meta["main"])).read())
