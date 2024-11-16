from dataclasses import dataclass
from typing import Protocol


class IExchangeAPIService(Protocol):
    async def get_exchange(self, params: dict) -> dict: ...
