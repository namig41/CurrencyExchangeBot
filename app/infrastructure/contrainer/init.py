from punq import (
    Container,
    Scope,
)

from functools import lru_cache

from infrastructure.api.services.currencies import CurrenciesAPIService
from infrastructure.api.services.currency import CurrencyAPIService
from infrastructure.api.services.exchange_rate import ExchangeRateAPIService
from infrastructure.api.services.exchange_rates import ExchangeRatesAPIService
from infrastructure.repositories.api_repostiory import (
    CurrenciesAPIRepository,
    ExchangeRatesAPIRepository,
)
from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    def init_api_currencies_repository() -> CurrenciesAPIRepository:
        return CurrenciesAPIRepository(
            currency_api=CurrencyAPIService(), currencies_api=CurrenciesAPIService()
        )

    def init_api_exchange_rates_repository() -> ExchangeRatesAPIRepository:
        return ExchangeRatesAPIRepository(
            exchange_rate_api=ExchangeRateAPIService(),
            exchange_rates_api=ExchangeRatesAPIService(),
        )

    container.register(
        BaseCurrenciesRepository,
        factory=init_api_currencies_repository,
        scope=Scope.singleton,
    )
    container.register(
        BaseExchangeRatesRepository,
        factory=init_api_exchange_rates_repository,
        scope=Scope.singleton,
    )

    return container
