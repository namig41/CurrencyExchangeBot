from dataclasses import dataclass

import httpx
from infrastructure.api.services.base import BaseAPIService


@dataclass
class ExchangeRatesAPIService(BaseAPIService):
    endpoint: str = "exchange_rates"

    async def get_exchange_rates(self) -> list[dict]:
        try:
            return await self._get(f"{self.base_url}/{self.endpoint}")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise

    async def post_exchange_rates(self, pyaload: dict) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._post(
                f"{self.base_url}/{self.endpoint}",
                data=pyaload,
                headers=headers,
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise

    async def patch_exchange_rates(self, pyaload: dict) -> dict:
        try:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            return await self._patch(
                f"{self.base_url}/{self.endpoint}",
                data=pyaload,
                headers=headers,
            )
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                self.logger.warning("Currencies endpoint not found.")
                return {}
            raise
