from .element import Element
from .meta import Meta
from .location import Location


class Link(Element):
    """
    A Milanote link.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    url: str = None
    """URL of the link."""
    title: str = None
    """Title of the link."""
    link_type: str = None
    """Type of the link."""

    def __init__(self, data: dict):
        super().__init__(data)
        if "link" in data["content"]:
            self.url = data["content"]["link"]["url"]
            self.title = data["content"]["link"]["title"]
        self.link_type = data["content"].get("linkType", None)

    def __repr__(self):
        return f"Link(id='{self.id}', title='{self.title}', link_type='{self.link_type}')"
