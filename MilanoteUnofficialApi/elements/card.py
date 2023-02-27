from .element import Element
from .location import Location
from .meta import Meta


class Card(Element):
    """
    A Milanote card.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    text_content: str
    """Text content of the card."""
    reactions: list
    """Reactions of the card."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.text_content = data["content"].get("textContent", None)
        if data["content"]["textContent"] is not None:
            self.text_content = "".join([block["text"] for block in data["content"]["textContent"]["blocks"]])
        self.reactions = data["content"].get("reactions", None)

    def __repr__(self):
        return f"Card(id='{self.id}', text_content='{self.text_content}')"
