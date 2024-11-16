from dataclasses import dataclass
from typing import Protocol


class IExchangeRateAPIService(Protocol):
    async def get_exchange_rate(self, base_code: str, target_code: str) -> dict: ...
