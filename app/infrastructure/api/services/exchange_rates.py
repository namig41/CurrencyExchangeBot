from dataclasses import dataclass

from infrastructure.api.services.base import BaseAPIService

from domain.exceptions.base import ApplicationException


@dataclass
class ExchangeRatesAPIService(BaseAPIService):
    endpoint: str = "exchangeRates"

    async def get_exchange_rates(self) -> list[dict]:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}")
        except ApplicationException:
            raise

    async def post_exchange_rates(self, pyaload: dict) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._post(
                f"{self.base_url}/{self.endpoint}",
                data=pyaload,
                headers=headers,
            )
        except ApplicationException:
            raise

    async def patch_exchange_rates(self, pyaload: dict) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._patch(
                f"{self.base_url}/{self.endpoint}",
                data=pyaload,
                headers=headers,
            )
        except ApplicationException:
            raise
