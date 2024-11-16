from decimal import Decimal
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.value_objects.rate import Rate


def convert_currency_entity_to_document(currency: Currency) -> dict:
    return {
        "id": currency.id,
        "code": currency.code,
        "fullname": currency.fullname,
        "sign": currency.sign,
    }


def convert_currency_document_to_entity(currency_data: dict) -> Currency:
    return Currency(
        id=currency_data["id"],
        code=currency_data["code"],
        fullname=currency_data["fullname"],
        sign=currency_data["sign"],
    )


def convert_currencies_document_to_entity(
    currencies_data: list[dict],
) -> Iterable[Currency]:
    return [
        convert_currency_document_to_entity(currency_data)
        for currency_data in currencies_data
    ]


def convert_exchange_rate_entity_to_document(exchange_rate: ExchangeRate) -> dict:
    return {
        "id": exchange_rate.id,
        "baseCurrency": convert_currency_entity_to_document(
            exchange_rate.base_currency,
        ),
        "targetCurrency": convert_currency_entity_to_document(
            exchange_rate.target_currency,
        ),
        "rate": exchange_rate.rate.as_generic_type(),
    }


def convert_exchange_rate_document_to_entity(
    exchange_rate_data: dict,
    base_currency: Currency,
    target_currency: Currency,
) -> ExchangeRate:

    return ExchangeRate(
        id=exchange_rate_data["id"],
        base_currency=base_currency,
        target_currency=target_currency,
        rate=Rate(Decimal(exchange_rate_data["rate"])),
    )


def convert_exchange_rate_all_document_to_entity(
    exchange_rate_data: dict,
) -> ExchangeRate:

    exchnage_rate_id = int(exchange_rate_data["id"])
    base_currency: Currency = convert_currency_document_to_entity(
        exchange_rate_data["baseCurrency"],
    )
    target_currency: Currency = convert_currency_document_to_entity(
        exchange_rate_data["targetCurrency"],
    )
    rate = Decimal(exchange_rate_data["rate"])

    return ExchangeRate(
        id=exchnage_rate_id,
        base_currency=base_currency,
        target_currency=target_currency,
        rate=rate,
    )


def convert_exchange_rates_document_to_entity(
    exchange_rates_data: list[dict],
) -> Iterable[ExchangeRate]:
    return [
        convert_exchange_rate_all_document_to_entity(exchange_rate_data)
        for exchange_rate_data in exchange_rates_data
    ]


def convert_exchange_rates_entity_to_document(
    exchange_rates: Iterable[ExchangeRate],
) -> list[dict]:

    return [
        convert_exchange_rate_entity_to_document(exchange_rate)
        for exchange_rate in exchange_rates
    ]


def convert_exchange_entity_to_document(
    exchange_rate: ExchangeRate,
    amount: float,
    converted_amount: float,
) -> dict:

    exchange_data = convert_exchange_rate_entity_to_document(exchange_rate)
    exchange_data["amount"] = float(amount)
    exchange_data["convertedAmount"] = float(converted_amount)

    return exchange_data


def convert_exchanges_entity_to_document(
    exchange_rates: Iterable[ExchangeRate],
    amount: float,
    converted_amount: float,
) -> dict:

    exchange_rates_data = convert_exchange_rates_entity_to_document(exchange_rates)

    exchange_data = {}
    exchange_data["amount"] = float(amount)
    exchange_data["convertedAmount"] = float(converted_amount)
    exchange_data["currencies"] = exchange_rates_data

    return exchange_data
