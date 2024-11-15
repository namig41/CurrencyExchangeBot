from typing import Iterable

from domain.entities.currency import Currency


def convert_currency_entity_to_string(currency: Currency) -> str:
    return f"""
        <b>Название валюты:</b> {currency.fullname}\n
        <b>Код валюты:</b> {currency.code}\n
        <b>Символ валюты:</b> {currency.sign}\n
    """


def convert_currencies_entity_to_string(currencies: Iterable[Currency]) -> str:
    currencies_str = ""
    for currency in currencies:
        currencies_str += convert_currency_entity_to_string(currency)
        currencies_str += "\n"
    return currencies_str
