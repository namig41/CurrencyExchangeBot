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

    async def patch_exchange_rate(
        self, base_code: str, target_code: str, pyaload: dict,
    ) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._patch(
                f"{self.base_url}/{self.endpoint}/{base_code + target_code}",
                data=pyaload,
                headers=headers,
            )
        except ApplicationException:
            raise
