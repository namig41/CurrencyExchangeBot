from infrastructure.repositories.converters import (
    convert_exchange_rate_document_to_entity,
    convert_exchange_rate_entity_to_document,
)

from domain.entities.exchange import Exchange
from domain.value_objects.currency_code import Code


def convert_exchange_to_document(
    base_code: Code,
    target_code: Code,
    amount: float,
) -> dict:

    exchange_data = {}

    exchange_data["from"] = base_code.as_generic_type()
    exchange_data["to"] = target_code.as_generic_type()
    exchange_data["amount"] = amount

    return exchange_data


def convert_exchange_entity_to_document(
    exchange: Exchange,
) -> dict:

    exchange_data = convert_exchange_rate_entity_to_document(exchange.exchange_rate)
    exchange_data["amount"] = exchange.amount
    exchange_data["convertedAmount"] = exchange.converted_amount

    return exchange_data


def convert_exchange_document_to_entity(exchange_data: dict) -> Exchange:
    return Exchange(
        exchange_rate=convert_exchange_rate_document_to_entity(exchange_data),
        amount=exchange_data["amount"],
        converted_amount=exchange_data["convertedAmount"],
    )
