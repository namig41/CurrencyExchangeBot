from decimal import Decimal
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


def convert_currency_entity_without_id_to_document(currency: Currency) -> dict:
    return {
        "code": currency.code.as_generic_type(),
        "name": currency.fullname,
        "sign": currency.sign,
    }


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


def convert_exchange_rate_entity_without_id_to_document(
    exchange_rate: ExchangeRate,
) -> dict:
    return {
        "baseCurrencyCode": exchange_rate.base_currency.code.as_generic_type(),
        "targetCurrencyCode": exchange_rate.target_currency.code.as_generic_type(),
        "rate": exchange_rate.rate.as_generic_type(),
    }


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
        convert_exchange_rate_document_to_entity(exchange_rate_data)
        for exchange_rate_data in exchange_rates_data
    ]


def convert_exchange_rates_entity_to_document(
    exchange_rates: Iterable[ExchangeRate],
) -> list[dict]:

    return [
        convert_exchange_rate_entity_to_document(exchange_rate)
        for exchange_rate in exchange_rates
    ]
