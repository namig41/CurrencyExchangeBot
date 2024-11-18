import pytest
from infrastructure.api.services.currencies import CurrenciesAPIService
from infrastructure.api.services.currency import CurrencyAPIService


@pytest.mark.asyncio
async def test_get_currencies_api():
    currencies_api = CurrenciesAPIService()

    data: list[dict] = await currencies_api.get_currencies()

    assert data != []
    assert data[0] == {
        "id": 1,
        "code": "USD",
        "fullname": "United States dollar",
        "sign": "$",
    }


@pytest.mark.asyncio
async def test_get_currency_api():
    currency_api = CurrencyAPIService()

    data: dict = await currency_api.get_currency("USD")

    assert data == {
        "id": 1,
        "code": "USD",
        "fullname": "United States dollar",
        "sign": "$",
    }


@pytest.mark.asyncio
async def test_add_currency_api():
    currencies_api = CurrenciesAPIService()

    currency_data: dict = {
        "code": "AAA",
        "name": "Test currency",
        "sign": "C",
    }

    data: dict = await currencies_api.post_currencies(currency_data)
    assert data != {}
