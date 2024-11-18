from functools import wraps

import httpx
from infrastructure.exceptions.api_excpetion import APIServiceException
from infrastructure.logger.base import ILogger


def handle_api_errors(logger: ILogger):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except httpx.HTTPStatusError as exc:
                text = exc.response.json()["message"]
                logger.error(
                    f"HTTP error: {exc.response.status_code}, {text}",
                )
                raise APIServiceException(text=text)
            except httpx.RequestError as exc:
                logger.error(f"Network error: {exc}")
                raise APIServiceException(text=f"Network error: {exc}")

        return wrapper

    return decorator
