from typing import Generator

from engine.types.adventure import Adventure
from engine.types.chapter import Chapter
from UI.chapter_handler import IChapterHandler
from UI.terminal_controller import TerminalController
from engine.IO.metadata import MetadataIO


class AdventureHandler(object):
    """
    An UI adventure handler.
    """

    def __init__(self, controller: TerminalController, 
                        adventure : Adventure, 
                        chapter_handler: IChapterHandler):
        """
        :param controller: a CLI controller.
        :type controller: TerminalController
        :param adventure: the adventure which the handler desplays.
        :type adventure: Adventure
        :param chapter_handler: a chapter handler.
        :type chapter_handler: IChapterHandler
        """
        super().__init__()
        
        self.adventure       = adventure
        self.chapter_handler = chapter_handler
        self.controller      = controller
    
    def start(self):
        """
        Starts the adventure UI.
        """
        self.controller.main_title = self.adventure.adventure_title

        # Start the chapter handling. 
        for chapter in self.adventure.chapters:
            # Skip if the chapter was finished 
            if MetadataIO().current_chapter > chapter.key:
                continue
            # Save the metadata
            MetadataIO().current_chapter = chapter.key
            # Do the required startup for the chapter.
            chapter.startup()
            # Yield the current chapter.
            self.chapter_handler.show(chapter)
            # Wrap up the chapter.
            chapter.wrap_up()
