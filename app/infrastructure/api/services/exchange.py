from dataclasses import dataclass

import httpx
from infrastructure.api.services.base import BaseAPIService


@dataclass
class ExchangeAPIService(BaseAPIService):
    endpoint: str = "exchange"

    async def get_exchange(self, params: dict) -> dict:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}", params=params)
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise
