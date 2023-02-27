from .element import Element
from .location import Location
from .meta import Meta


class TaskList(Element):
    """
    A Milanote task list contains Tasks.
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
    """Title of the task list."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.title = data["content"]["title"]

    def __repr__(self):
        return f"TaskList(id={self.id}, title={self.title})"
