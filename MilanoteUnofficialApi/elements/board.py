from .element import Element
from .column import Column
from .commentthread import CommentThread
from .document import Document
from .link import Link
from .location import Location
from .meta import Meta
from .task import Task
from .tasklist import TaskList
from .card import Card
from .file import File
from .image import Image
from .annotation import Annotation
from .color_swatch import ColorSwatch
from .sketch import Sketch

import logging


class Board(Element):
    """
    A Milanote board, contains sub elements.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    title: str
    """Title of the board."""
    elements: dict[str, list[Element]]
    """Elements contained in the board."""

    def __init__(self, data: dict, elements_data: dict = None, comments_data: dict = None):
        super().__init__(data)
        self.title = data["content"]["title"]
        self.elements = {
            "TASK": [],
            "TASK_LIST": [],
            "DOCUMENT": [],
            "LINK": [],
            "COLUMN": [],
            "BOARD": [],
            "COMMENT_THREAD": [],
            "CARD": [],
            "FILE": [],
            "IMAGE": [],
            "ANNOTATION": [],
            "COLOR_SWATCH": [],
            "SKETCH": [],
            "ALIAS": [],
        }
        if elements_data is not None:
            self.init_elements(elements_data, comments_data)

    def init_elements(self, elements_data: dict, comments_data: dict = None):
        """
        Initialize the elements contained in the board.
        """
        comments_data_by_thread_id = {}
        if comments_data is not None:
            comments_data_by_thread_id = self.init_comments(comments_data)
        if elements_data is None:
            return
        for element_data in elements_data.values():
            element_type = element_data["elementType"]
            if element_type == "TASK":
                self.elements["TASK"].append(Task(element_data))
            elif element_type == "TASK_LIST":
                self.elements["TASK_LIST"].append(TaskList(element_data))
            elif element_type == "DOCUMENT":
                self.elements["DOCUMENT"].append(Document(element_data))
            elif element_type == "LINK":
                self.elements["LINK"].append(Link(element_data))
            elif element_type == "COLUMN":
                self.elements["COLUMN"].append(Column(element_data))
            elif element_type == "BOARD":
                self.elements["BOARD"].append(Board(element_data))
            elif element_type == "COMMENT_THREAD":
                self.elements["COMMENT_THREAD"].append(
                    CommentThread(element_data, comments_data_by_thread_id.get(element_data["id"], None)))
            elif element_type == "CARD":
                self.elements["CARD"].append(Card(element_data))
            elif element_type == "FILE":
                self.elements["FILE"].append(File(element_data))
            elif element_type == "IMAGE":
                self.elements["IMAGE"].append(Image(element_data))
            elif element_type == "ANNOTATION":
                self.elements["ANNOTATION"].append(Annotation(element_data))
            elif element_type == "COLOR_SWATCH":
                self.elements["COLOR_SWATCH"].append(ColorSwatch(element_data))
            elif element_type == "SKETCH":
                self.elements["SKETCH"].append(Sketch(element_data))
            elif element_type == "ALIAS":
                element_data["content"]["title"] = element_data["content"].get("originalTitle", None)
                self.elements["ALIAS"].append(Board(element_data))
            else:
                self.elements.setdefault(element_type, []).append(element_data)
                logging.warning(
                    f"Unknown element type: {element_type}, saved as dict in self.elements['{element_type}']")

    def init_comments(self, comments_data: dict = None) -> dict[str, list[dict]]:
        """
        Create a new dict for the comments as ("parentId", list[dict]) pair to add to ClassVar[CommentThread].
        """
        if comments_data is None:
            return {}
        comments_data_by_thread_id = {}
        for comment_data in comments_data.values():
            thread_id = comment_data["threadId"]
            if thread_id not in comments_data_by_thread_id:
                comments_data_by_thread_id[thread_id] = []
            comments_data_by_thread_id[thread_id].append(comment_data)
        return comments_data_by_thread_id

    def __repr__(self):
        return f"Board(id='{self.id}', title='{self.title}')"
