import abc

from engine.types.chapter import Chapter


class IChapterHandler(object, metaclass=abc.ABCMeta):
    """
    IChapterHandler is an interface for chapter handlers
    """

    @abc.abstractmethod
    def show(self, chapter: Chapter):
        pass
