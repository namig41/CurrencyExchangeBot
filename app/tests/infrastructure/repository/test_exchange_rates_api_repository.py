from decimal import Decimal
from typing import Iterable

import pytest
from infrastructure.repositories.base import BaseExchangeRatesRepository
from punq import Container

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


@pytest.mark.asyncio
async def test_get_exchange_rates_api_repository(container: Container):
    exchange_rates_repository: BaseExchangeRatesRepository = container.resolve(
        BaseExchangeRatesRepository,
    )
    exchange_rates: Iterable[ExchangeRate] = (
        await exchange_rates_repository.get_exchange_rates()
    )
    assert exchange_rates != []


@pytest.mark.asyncio
async def test_get_exchange_rate_api_repository(container: Container):
    exchange_rates_repository: BaseExchangeRatesRepository = container.resolve(
        BaseExchangeRatesRepository,
    )
    exchange_rate: ExchangeRate = (
        await exchange_rates_repository.get_exchange_rate_by_codes("USD", "EUR")
    )

    assert exchange_rate == ExchangeRate(
        id=1,
        base_currency=Currency(
            id=1,
            code="USD",
            fullname="United States dollar",
            sign="$",
        ),
        target_currency=Currency(id=2, code="EUR", fullname="Euro", sign="€"),
        rate=Decimal("0.5"),
    )
