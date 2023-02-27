from .comment import Comment
from .element import Element
from .location import Location
from .meta import Meta


class CommentThread(Element):
    """
    A Milanote element that contains comments.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    comments: list[Comment]
    """List of comments in the thread."""

    def __init__(self, data: dict, comments_data: list = None):
        super().__init__(data)
        if comments_data is not None:
            self.comments = [Comment(comment) for comment in comments_data]

    def __repr__(self):
        return f"CommentThread(id='{self.id}')"
