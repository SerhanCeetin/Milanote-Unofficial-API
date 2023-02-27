
class Location:
    """
    A Milanote element's location data.
    """

    parent_id: str
    """ID of the parent element."""
    section: str
    """Section of the element."""
    position_score: int
    """Position score of the element."""
    position_x: int
    """Position x of the element. (Only for CANVAS section)"""
    position_y: int
    """Position y of the element. (Only for CANVAS section)"""
    position_index: int
    """Position index of the element. (Only for INBOX section)"""

    def __init__(self, data: dict):
        self.parent_id = data.get("parentId", None)
        self.section = data.get("section", None)
        self.position_score = int(data.get("positionScore", -1))
        self.position_x = int(data.get("positionX", -1))
        self.position_y = int(data.get("positionY", -1))
        self.position_index = int(data.get("positionIndex", -1))

    def __repr__(self):
        if self.section == "CANVAS":
            return f"Location(parent_id='{self.parent_id}', section='{self.section}', position_score={self.position_score}, position_x={self.position_x}, position_y={self.position_y})"
        elif self.section == "INBOX":
            return f"Location(parent_id='{self.parent_id}', section='{self.section}', position_score={self.position_score}, position_index={self.position_index})"
        else:
            return f"Location(parent_id='{self.parent_id}', section='{self.section}', position_score={self.position_score})"