from dataclasses import (
    dataclass,
    field,
)

import httpx
from infrastructure.api.services.error_handler import handle_api_errors
from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency

from settings.config import config


@dataclass
class BaseAPIService:
    base_url: str = config.API_EXCHANGE_RATE
    endpoint: str = ""
    logger: ILogger = field(default_factory=lambda: create_logger_dependency())

    def __post_init__(self):
        # Применяем декораторы с использованием реального логгера
        self._get = handle_api_errors(self.logger)(self._get)
        self._post = handle_api_errors(self.logger)(self._post)
        self._patch = handle_api_errors(self.logger)(self._patch)

    async def _get(self, url: str, params: dict = {}) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()

    async def _post(self, url: str, data: dict, headers: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=data, headers=headers)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()

    async def _patch(self, url: str, data: dict, headers: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.patch(url, data=data, headers=headers)
            response.raise_for_status()
            self.logger.info(response.json())
            return response.json()
