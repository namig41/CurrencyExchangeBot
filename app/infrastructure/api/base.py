from dataclasses import (
    dataclass,
    field,
)

import httpx
from infrastructure.api.error_handler import handle_api_errors
from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency

from settings.config import config


@dataclass
class BaseAPIService:
    base_url: str = config.API_EXCHANGE_RATE
    endpoint: str = ""
    logger: ILogger = field(default_factory=lambda: create_logger_dependency())

    @handle_api_errors(logger=logger)
    async def _get(self, url: str, params: dict = {}) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()

    @handle_api_errors(logger=logger)
    async def _post(self, url: str, data: dict, headers: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=data, headers=headers)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()

    @handle_api_errors(logger=logger)
    async def _patch(self, url: str, data: dict, headers: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.patch(url, data=data, headers=headers)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()
