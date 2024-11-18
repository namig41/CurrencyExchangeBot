from typing import Iterable

import pytest
from infrastructure.repositories.base import BaseCurrenciesRepository
from punq import Container

from domain.entities.currency import Currency


@pytest.mark.asyncio
async def test_get_currencies_api_repository(container: Container):
    currencies_repository: BaseCurrenciesRepository = container.resolve(
        BaseCurrenciesRepository,
    )
    currencies: Iterable[Currency] = await currencies_repository.get_currencies()
    assert currencies != []
