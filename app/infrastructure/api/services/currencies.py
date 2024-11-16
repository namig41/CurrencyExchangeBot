from dataclasses import dataclass

import httpx
from infrastructure.api.services.base import BaseAPIService


@dataclass
class CurrenciesAPIService(BaseAPIService):
    endpoint: str = "currencies"

    async def get_currencies(self) -> dict:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise

    async def post_currencies(self, currency_data: dict) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._post(
                f"{self.base_url}/{self.endpoint}",
                data=currency_data,
                headers=headers,
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise
