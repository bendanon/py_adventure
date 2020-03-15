import os.path

from engine.IO.adventure import AdventureIO
from engine.IO.metadata import MetadataIO
from UI.adventure_handler import AdventureHandler
from UI.cli_chapter_handler import CliChapterHandler
from UI.terminal_controller import TerminalController
from definitions import metafile, adventure_chapters, adventure_folder

if __name__ == "__main__":
    metafile = MetadataIO(metafile)
    terminal_controller = TerminalController()
    with AdventureIO(os.path.join(os.path.curdir, adventure_folder, adventure_chapters)) as adventure:
        adventure_handler = AdventureHandler(terminal_controller, 
                                            adventure, 
                                            CliChapterHandler(terminal_controller))
        adventure_handler.start()
