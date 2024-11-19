from typing import Protocol


class IExchangeRatesAPIService(Protocol):
    async def get_exchange_rates(self) -> list[dict]: ...

    async def post_exchange_rates(self, pyaload: dict) -> dict: ...
