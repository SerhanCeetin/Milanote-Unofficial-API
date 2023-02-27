from .element import Element
from .meta import Meta
from .location import Location


class File(Element):
    """
    A Milanote file element.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    file_name: str
    """Name of the file."""
    file_ext: str
    """Extension of the file."""
    url: str
    """URL of the file."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.file_name = data['content']['file']['filename']
        self.file_ext = data['content']['file']['ext']
        self.url = data['content']['file']['url']

    def __repr__(self):
        return f"File(id='{self.id}', file_name='{self.file_name}')"
