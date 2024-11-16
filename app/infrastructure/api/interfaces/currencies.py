from dataclasses import dataclass
from typing import Protocol


@dataclass
class ICurrenciesAPIService(Protocol):

    async def get_currencies(self) -> dict: ...

    async def post_currencies(self, currency_data: dict) -> dict: ...
