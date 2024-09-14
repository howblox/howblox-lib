class HowbloxException(Exception):
    """Base exception for Howblox."""

    def __init__(self, message=None, ephemeral=False):
        self.message = message
        self.ephemeral = ephemeral

class RobloxNotFound(HowbloxException):
    """Raised when a Roblox entity is not found."""

class RobloxAPIError(HowbloxException):
    """Raised when the Roblox API returns an error."""

class RobloxDown(HowbloxException):
    """Raised when the Roblox API is down."""

class UserNotVerified(HowbloxException):
    """Raised when a user is not verified."""

class Message(HowbloxException):
    """Generic exception to communicate some message to the user."""

class Error(Message):
    """Generic user-thrown error."""