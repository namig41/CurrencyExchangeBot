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
