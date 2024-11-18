from dataclasses import dataclass

from infrastructure.api.services.base import BaseAPIService

from domain.exceptions.base import ApplicationException


@dataclass
class ExchangeRateAPIService(BaseAPIService):
    endpoint: str = "exchangeRate"

    async def get_exchange_rate(self, base_code: str, target_code: str) -> dict:
        try:
            return await self._get(
                f"{self.base_url}/{self.endpoint}/{base_code + target_code}",
            )
        except ApplicationException:
            raise
