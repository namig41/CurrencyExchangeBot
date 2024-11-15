from dataclasses import dataclass
from typing import Iterable

from infrastructure.api.currencies import CurrenciesAPIService
from infrastructure.api.currency import CurrencyAPIService
from infrastructure.api.exchange_rate import ExchangeRateAPIService
from infrastructure.api.exchange_rates import ExchangeRatesAPIService
from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)
from infrastructure.repositories.converters import (
    convert_currencies_document_to_entity,
    convert_currency_document_to_entity,
    convert_currency_entity_to_document,
    convert_exchange_rates_document_to_entity,
)

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


@dataclass
class CurrenciesAPIRepository(BaseCurrenciesRepository):

    currencies_api: CurrenciesAPIService
    currency_api: CurrencyAPIService

    async def get_currencies(self) -> Iterable[Currency]:
        try:
            currencies_data: list[dict] = await self.currencies_api.get_currencies()
            return convert_currencies_document_to_entity(currencies_data)
        except Exception as e:
            raise e

    async def get_currency_by_code(self, currency_code: str) -> Currency | None:
        try:
            currency: dict = await self.currency_api.get_currency(currency_code)
            return convert_currency_document_to_entity(currency)
        except Exception as e:
            raise e

    async def add_currency(self, currency: Currency) -> None:
        try:
            currency_data: dict = convert_currency_entity_to_document(currency)
            currency: dict = await self.currencies_api.post_currencies(currency_data)
        except Exception as e:
            raise e


@dataclass
class ExchangeRatesAPIRepository(BaseExchangeRatesRepository):

    exchange_rate_api: ExchangeRateAPIService
    exchange_rates_api: ExchangeRatesAPIService

    async def get_exchange_rate_by_codes(
        self,
        base_code: str,
        target_code: str,
    ) -> ExchangeRate | None:
        try:
            exchange_rates_document: dict = (
                await self.exchange_rate_api.get_exchange_rate(base_code, target_code)
            )
            return convert_exchange_rates_document_to_entity(exchange_rates_document)
        except Exception as e:
            raise e

    async def get_exchange_rates(self) -> Iterable[ExchangeRate]:
        try:
            exchange_rates_document: dict = (
                await self.exchange_rates_api.get_exchange_rates()
            )
            return convert_exchange_rates_document_to_entity(exchange_rates_document)
        except Exception as e:
            raise e

    async def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        try:
            exchange_rate_data: dict = convert_currency_entity_to_document(
                exchange_rate,
            )
            exchange_rate_document: dict = (
                await self.exchange_rates_api.post_exchange_rate(exchange_rate_data)
            )
            return convert_exchange_rates_document_to_entity(exchange_rate_document)
        except Exception as e:
            raise e

    async def update_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        try:
            exchange_rate_data: dict = convert_currency_entity_to_document(
                exchange_rate,
            )
            exchange_rate_document: dict = (
                await self.exchange_rates_api.patch_exchange_rate(exchange_rate_data)
            )
            return convert_exchange_rates_document_to_entity(exchange_rate_document)
        except Exception as e:
            raise e
