from dataclasses import dataclass

import httpx
from infrastructure.api.services.base import BaseAPIService


@dataclass
class ExchangeRateAPIService(BaseAPIService):
    endpoint: str = "exchange_rate"

    async def get_exchange_rate(self, base_code: str, target_code: str) -> dict:
        try:
            return self._get(
                f"{self.base_url}/{self.endpoint}/{base_code + target_code}",
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise
