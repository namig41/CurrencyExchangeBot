import pytest
from infrastructure.api.services.exchange_rate import ExchangeRateAPIService
from infrastructure.api.services.exchange_rates import ExchangeRatesAPIService


@pytest.mark.asyncio
async def test_get_exchange_rates_api():
    exchange_rates_api = ExchangeRatesAPIService()

    data: list[dict] = await exchange_rates_api.get_exchange_rates()

    assert data != []
    assert data[0] == {
        "id": 1,
        "baseCurrency": {
            "id": 1,
            "code": "USD",
            "fullname": "United States dollar",
            "sign": "$",
        },
        "targetCurrency": {"id": 2, "code": "EUR", "fullname": "Euro", "sign": "€"},
        "rate": 0.5,
    }


@pytest.mark.asyncio
async def test_get_exchange_rate_api():
    exchange_rate_api = ExchangeRateAPIService()

    data: dict = await exchange_rate_api.get_exchange_rate("USD", "EUR")

    assert data == {
        "id": 1,
        "baseCurrency": {
            "id": 1,
            "code": "USD",
            "fullname": "United States dollar",
            "sign": "$",
        },
        "targetCurrency": {"id": 2, "code": "EUR", "fullname": "Euro", "sign": "€"},
        "rate": 0.5,
    }
