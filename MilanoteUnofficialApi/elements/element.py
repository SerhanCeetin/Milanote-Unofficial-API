from .meta import Meta
from .location import Location

class Element:
    """
    A Milanote element.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""

    def __init__(self, data):
        self.id = data["id"]
        self.element_type = data["elementType"]
        self.meta = Meta(data["meta"])
        self.location = Location(data["location"])

    def __repr__(self):
        return f"Element(id='{self.id}', element_type='{self.element_type}', meta={self.meta}, location={self.location})"
