from dataclasses import dataclass

from infrastructure.api.services.base import BaseAPIService

from domain.exceptions.base import ApplicationException


@dataclass
class CurrencyAPIService(BaseAPIService):
    endpoint: str = "currency"

    async def get_currency(self, currency_code: str) -> dict:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}/{currency_code}")
        except ApplicationException:
            raise
