import pytest
from infrastructure.api.services.currencies import CurrenciesAPIService


@pytest.mark.asyncio
async def test_get_currencies_api():
    currencies_api = CurrenciesAPIService()

    data: list[dict] = await currencies_api.get_currencies()

    assert len(data) == 3
    assert data[0] == {
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
    del data["id"]

    assert data == {
        "code": "AAA",
        "fullname": "Test currency",
        "sign": "C",
    }
