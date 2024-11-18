from infrastructure.api.services.exchange import ExchangeAPIService
from infrastructure.services.converters import (
    convert_exchange_document_to_entity,
    convert_exchange_to_document,
)

from domain.entities.exchange import Exchange
from domain.exceptions.base import ApplicationException
from domain.value_objects.currency_code import Code


async def exchange_by_codes(
    base_code: Code,
    target_code: Code,
    amount: float,
) -> Exchange:
    api_exchange: ExchangeAPIService = ExchangeAPIService()

    try:
        params = convert_exchange_to_document(base_code, target_code, amount)
        exchange_data = await api_exchange.get_exchange(params)

        return convert_exchange_document_to_entity(exchange_data)
    except ApplicationException:
        raise
