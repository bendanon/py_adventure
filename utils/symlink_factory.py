import os
import json
from shutil import copyfile

from definitions import adventure_folder, chapters_folder, os_name

def linux_init_symlink(symlink_name, chapter_title):
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

def linux_update_symlink(symlink_name, chapter_title):
    pass

def cp_init_symlink(symlink_name, chapter_title):
    chapter_env = os.path.join(os.path.curdir, 
                               adventure_folder,
                               chapters_folder,
                               chapter_title.replace(" ", "_").lower())
    
    meta = {}
    with open(os.path.join(chapter_env,
                           ".meta.json")) as metafile:
        meta = json.load(metafile)
    
    # copy file
    if os.path.lexists(symlink_name):
        os.remove(symlink_name)
    
    copyfile(os.path.join(chapter_env,
                          meta["symlink"]), symlink_name)

def cp_update_symlink(symlink_name, chapter_title):
    chapter_env = os.path.join(os.path.curdir, 
                               adventure_folder,
                               chapters_folder,
                               chapter_title.replace(" ", "_").lower())
    
    meta = {}
    with open(os.path.join(chapter_env,
                           ".meta.json")) as metafile:
        meta = json.load(metafile)  
    
    # copy file    
    copyfile(symlink_name, 
             os.path.join(chapter_env, meta["symlink"]))

if os_name == "linux":
    init_symlink = linux_init_symlink
    update_symlink = linux_update_symlink
else:
    init_symlink = cp_init_symlink
    update_symlink = cp_update_symlink