from .element import Element
from .meta import Meta
from .location import Location


class Task(Element):
    """
    A Milanote task.
    """

    id: str
    """ID of the element."""
    element_type: str
    """Type of the element."""
    meta: Meta
    """Metadata of the element."""
    location: Location
    """Location of the element."""
    text_content: str = None
    """Text content of the task."""
    assignments: list[dict] = None
    """Assignments of the task."""
    due_date: str = None
    """Due date of the task. (UTC)"""
    due_reminder: str = None
    """Due reminder UNIX timestamp of the task."""
    is_complete: bool = False
    """Whether the task is complete or not."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.assignments = data["content"].get("assignments", None)
        self.due_date = data["content"].get("dueDate", None)
        self.due_reminder = data["content"].get("dueReminderTimestamp", None)
        self.is_complete = data["content"].get("isComplete", False)
        if data["content"]["textContent"] is not None:
            self.text_content = "".join([block["text"] for block in data["content"]["textContent"]["blocks"]])

    def __repr__(self):
        return f"Task(id='{self.id}', text_content='{self.text_content}')"
