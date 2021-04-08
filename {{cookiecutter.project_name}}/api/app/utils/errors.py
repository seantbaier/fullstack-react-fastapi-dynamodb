from fastapi import HTTPException, status
from loguru import logger

from app.constants import aws_errors


def handle_error(error: Exception) -> HTTPException:
    """
    Handles the Error format from either AWS or botocore.exceptions

    Parameters
    - error: (Exception) The error object to be formatted

    Returns
    - fastapi.HTTPException object
    """
    try:
        if hasattr(error, "response"):
            if "Error" in error.response:
                detail = error.response["Error"]["Message"]
                error_code = error.response["Error"]["Code"]
                status_code = error.response["ResponseMetadata"]["HTTPStatusCode"]

                # AWS sends back a 400 error for Resource not found.
                # Overriding this to a 404.
                if error_code == aws_errors.RESOURCE_NOT_FOUND_EXCEPTION:
                    status_code = status.HTTP_404_NOT_FOUND

                return HTTPException(status_code=status_code, detail=detail)

        return error
    except Exception as e:
        logger.error(e)
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e
        )
