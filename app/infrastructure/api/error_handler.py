from functools import wraps

import httpx


def handle_api_errors(logger):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except httpx.HTTPStatusError as exc:
                logger.error(
                    f"HTTP error: {exc.response.status_code}, {exc.response.text}",
                )
                raise
            except httpx.RequestError as exc:
                logger.error(f"Network error: {exc}")
                raise

        return wrapper

    return decorator
