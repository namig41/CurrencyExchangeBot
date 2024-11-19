from typing import Protocol


class IExchangeRateAPIService(Protocol):
    async def get_exchange_rate(self, base_code: str, target_code: str) -> dict: ...

    async def patch_exchange_rate(
        self, base_code: str, target_code: str, pyaload: dict,
    ) -> dict: ...
