from typing import List, Union

from engine.types.chapter import Chapter


class Adventure:
    """
    An adventure class. 
    Acts as the logic layer of the adventure engine.
    """

    def __init__(self, adventure_title: str, 
                       chapters: List[Union[Chapter, dict]]):
        """
        :param adventure_title: the name of the adventure.
        :type adventure_title: str
        :param chapters: a chapter list.
        :type chapters: List[Union[Chapter, dict]]
        """
        self.adventure_title = adventure_title
        self.chapters = [ 
                            Chapter(**chapter_info) 
                                if isinstance(chapter_info, dict) 
                                else chapter_info
                            for chapter_info in chapters
                        ]
        
        self.chapters.sort(key=lambda chapter: chapter.key)
