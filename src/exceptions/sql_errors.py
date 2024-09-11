from src.exceptions import BaseError


class EntityDoesNotExistError(BaseError):
    """database returns nothing"""

    pass


class EntityAlreadyExistsError(BaseError):
    """conflict detected, like trying to create a resource that already exists"""

    pass


class InvalidOperationError(BaseError):
    """invalid operations like trying to delete a non-existing entity, etc."""

    pass