from infrastructure.api.services.exchange import ExchangeAPIService

from domain.exceptions.base import ApplicationException
from domain.value_objects.currency_code import Code


async def exchange_by_codes(base_code: Code, target_code: Code, amount: float) -> dict:
    api_exchange: ExchangeAPIService = ExchangeAPIService()

    try:
        params = {
            "from": base_code.as_generic_type(),
            "to": target_code.as_generic_type(),
            "amount": amount,
        }
        data = await api_exchange.get_exchange(params)
        return data
    except ApplicationException:
        raise
