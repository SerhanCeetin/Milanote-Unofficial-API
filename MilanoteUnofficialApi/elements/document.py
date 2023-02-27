from .element import Element
from .meta import Meta
from .location import Location


class Document(Element):
    """
    A Milanote document, contains text.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    title: str = None
    """Title of the document."""
    text_content: str = None
    """Text content of the document."""

    def __init__(self, data: dict):
        super().__init__(data)
        if "title" in data["content"]:
            self.title = data["content"]["title"]
        if data["content"]["textContent"] is not None:
            self.text_content = "".join([block["text"] for block in data["content"]["textContent"]["blocks"]])

    def __repr__(self):
        return f"Document(id='{self.id}', title='{self.title}')"
