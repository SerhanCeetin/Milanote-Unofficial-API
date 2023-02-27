class MilanoteException(Exception):
    """Base class for Milanote exceptions."""
    raw_response: dict
    """Raw response from Milanote."""
    message: str
    """Message of the exception."""

    def __init__(self, raw_response, message):
        self.raw_response = raw_response
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class BoardNotFoundError(MilanoteException):
    """Board not found."""


class NotAuthorizedError(MilanoteException):
    """Not authorized."""


class UnknownError(MilanoteException):
    """Unknown error."""
