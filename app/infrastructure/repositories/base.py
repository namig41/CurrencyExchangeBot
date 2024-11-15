from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


@dataclass
class BaseCurrenciesRepository(ABC):
    @abstractmethod
    async def get_currencies(self) -> Iterable[Currency]: ...

    @abstractmethod
    async def get_currency_by_code(self, currency_code: str) -> Currency | None: ...

    @abstractmethod
    async def add_currency(self, currency: Currency) -> None: ...


@dataclass
class BaseExchangeRatesRepository(ABC):

    @abstractmethod
    async def get_exchange_rate_by_codes(
        self,
        base_code: str,
        target_code: str,
    ) -> ExchangeRate | None: ...

    @abstractmethod
    async def get_exchange_rates(self) -> Iterable[ExchangeRate]: ...

    @abstractmethod
    async def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None: ...

    @abstractmethod
    async def update_exchange_rate(self, exchange_rate: ExchangeRate) -> None: ...
