from typing import Protocol


class ICurrencyAPIService(Protocol):
    async def get_currency(self, currency_code: str) -> dict: ...
