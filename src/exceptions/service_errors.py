class BaseError(Exception):
    """base exception class"""

    def __init__(self, message: str = "Service is unavailable"):
        self.message = message
        super().__init__(self.message)


class ServiceError(BaseError):
    """failures in external services or APIs, like a database or a third-party service"""

    pass