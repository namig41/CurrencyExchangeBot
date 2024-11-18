from dataclasses import dataclass

from infrastructure.api.services.base import BaseAPIService

from domain.exceptions.base import ApplicationException


@dataclass
class ExchangeAPIService(BaseAPIService):
    endpoint: str = "exchange"

    async def get_exchange(self, params: dict) -> dict:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}", params=params)
        except ApplicationException:
            raise
