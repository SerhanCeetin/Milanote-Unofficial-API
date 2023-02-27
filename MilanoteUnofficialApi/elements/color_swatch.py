from .element import Element
from .location import Location
from .meta import Meta


class ColorSwatch(Element):
    """
    A Milanote color swatch element.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    color: dict
    """Color of the swatch."""
    text: str
    """Text of the color swatch."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.color = data['content']['color']
        self.text = "".join([block["text"] for block in data['content']['caption']['blocks']])

    def __repr__(self):
        return f"ColorSwatch(id='{self.id}', text='{self.text}')"
