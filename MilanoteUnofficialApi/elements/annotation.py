from .meta import Meta
from .location import Location
from .element import Element


class Annotation(Element):
    """
    A Milanote annotation element.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    drawing: dict
    """A dictionary that contains "paths" and "svg" code."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.drawing = data['content']['drawing']

    def __repr__(self):
        return f"Annotation(id='{self.id}', drawing={self.drawing})"
