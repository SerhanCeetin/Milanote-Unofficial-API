class Comment:
    """
    A Milanote comment.
    """

    id: str
    """ID of the comment."""
    user_id: str
    """ID of the user who created the comment."""
    text: str
    """Text of the comment."""
    created_at: str
    """UNIX Timestamp of when the comment was created."""
    updated_at: str
    """UNIX Timestamp of when the comment was last updated."""

    def __init__(self, data: dict):
        self.id = data["_id"]
        self.user_id = data["userId"]
        self.text = "".join([block["text"] for block in data["text"]["blocks"]])
        self.created_at = data["createdAt"]
        self.updated_at = data["updatedAt"]

    def __repr__(self):
        return f"Comment(id='{self.id}', text='{self.text}')"
