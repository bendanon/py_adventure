import os
import json

from definitions import adventure_folder, chapters_folder

def create_symlink(symlink_name, chapter_title):
    chapter_env = os.path.join(os.path.curdir, 
                               adventure_folder,
                               chapters_folder,
                               chapter_title.replace(" ", "_").lower())
    
    meta = {}
    with open(os.path.join(chapter_env,
                           ".meta.json")) as metafile:
        meta = json.load(metafile)
    
    # Create symlink
    if os.path.lexists(symlink_name):
        os.remove(symlink_name)
    
    os.symlink(os.path.join(chapter_env,
                            meta["symlink"]), symlink_name)
