from .element import Element
from .meta import Meta
from .location import Location


class Image(Element):
    """
    A Milanote image element.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    url: str
    """URL of the image."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data['content']['image']['original']

    def __repr__(self):
        return f"Image(id='{self.id}')"
