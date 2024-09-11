from typing import Callable

from fastapi import Request, status, FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from src.api.routers import routers_list
from src.exceptions import (
    BaseError,
    EntityDoesNotExistError,
    InvalidOperationError,
    AuthenticationFailed,
    InvalidTokenError,
    ServiceError,
)

app = FastAPI()

app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/")
def hello():
    return {'Details': 'Add /docs'}


for router in routers_list:
    app.include_router(router, prefix='/api')


def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, BaseError], JSONResponse]:
    """Create an exception handler for a specific exception.

    Args:
        status_code (int): code that will be returned in the response.
        initial_detail (str): detail message that will be returned in the response.

    Returns:
        Callable[[Request, BaseError], JSONResponse]: exception handler.
    """
    detail = {"message": initial_detail}

    async def exception_handler(_: Request, exc: BaseError) -> JSONResponse:
        if hasattr(exc, "message") and exc.message:
            detail["message"] = exc.message

        logger.error(exc)
        return JSONResponse(
            status_code=status_code, content={"detail": detail["message"]}
        )

    return exception_handler


app.add_exception_handler(
    exc_class_or_status_code=EntityDoesNotExistError,
    handler=create_exception_handler(
        status.HTTP_404_NOT_FOUND, "Entity does not exist."
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=InvalidOperationError,
    handler=create_exception_handler(
        status.HTTP_400_BAD_REQUEST, "Can't perform the operation."
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=AuthenticationFailed,
    handler=create_exception_handler(
        status.HTTP_401_UNAUTHORIZED,
        "Authentication failed due to invalid credentials.",
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=InvalidTokenError,
    handler=create_exception_handler(
        status.HTTP_401_UNAUTHORIZED, "Invalid token, please re-authenticate again."
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=ServiceError,
    handler=create_exception_handler(
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        "A service seems to be down, try again later.",
    ),
)
