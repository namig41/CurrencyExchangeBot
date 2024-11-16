from dataclasses import dataclass

import httpx
from infrastructure.api.services.base import BaseAPIService


@dataclass
class CurrencyAPIService(BaseAPIService):
    endpoint: str = "currency"

    async def get_currency(self, currency_code: str) -> dict:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}/{currency_code}")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise
