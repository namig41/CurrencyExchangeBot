from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


def convert_currency_entity_to_string(currency: Currency) -> str:
    return (
        f"<b>Название валюты:</b> {currency.fullname}\n"
        f"<b>Код валюты:</b> {currency.code}\n"
        f"<b>Символ валюты:</b> {currency.sign}\n"
    )


def convert_currencies_entity_to_string(currencies: Iterable[Currency]) -> str:
    currencies_str = ""
    for index, currency in enumerate(currencies):
        currencies_str += f"{index + 1}. {convert_currency_entity_to_string(currency)}"
        currencies_str += "\n"
    return currencies_str


def convert_exchange_rate_entity_to_string(exchange_rate: ExchangeRate) -> str:
    return (
        f"<b>Базовая валюта</b>\n"
        f"{convert_currency_entity_to_string(exchange_rate.base_currency)}"
        f"<b>Целевая валюта</b>\n"
        f"{convert_currency_entity_to_string(exchange_rate.target_currency)}"
        f"<b>Курс:</b>{exchange_rate.rate}"
    )


def convert_exchange_rates_entity_to_string(
    exchange_rates: Iterable[ExchangeRate],
) -> str:
    exchange_rates_str = ""
    for index, exchange_rate in enumerate(exchange_rates):
        exchange_rates_str += (
            f"{index + 1}. {convert_exchange_rate_entity_to_string(exchange_rate)}"
        )
        exchange_rates_str += "\n\n"
    return exchange_rates_str
