from src.exceptions import BaseError


class AuthenticationFailed(BaseError):
    """invalid authentication credentials"""

    pass


class InvalidTokenError(BaseError):
    """invalid token"""

    pass
