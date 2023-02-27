class Meta:
    """
    A Milanote element's metadata.
    """

    created_time: int
    """Created time of the element as UNIX time (in milliseconds)."""
    creator: str
    """ID of the user who created the element."""
    modified_by: str
    """ID of the user who last modified the element."""
    modified_time: int
    """Timestamp of the last modification of the element as UNIX time (in milliseconds)."""
    significant_modified: int
    """Timestamp of the last significant modification of the element as UNIX time (in milliseconds)."""

    def __init__(self, data: dict):
        self.created_time = data["createdTime"]
        self.creator = data["creator"]
        self.modified_by = data["modifiedBy"]
        self.modified_time = data["modifiedTime"]
        self.significant_modified = data["significantModified"]

    def __repr__(self):
        return f"Meta(created_time='{self.created_time}', creator='{self.creator}', modified_by='{self.modified_by}', modified_time='{self.modified_time}', significant_modified='{self.significant_modified}')"
