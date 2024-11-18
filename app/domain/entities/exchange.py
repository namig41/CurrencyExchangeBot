from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.exchange import AmountIsNegativeException


@dataclass
class Exchange(BaseEntity):
    exchange_rate: ExchangeRate
    amount: float = 0
    converted_amount: float = 0

    def validate(self):
        if self.amount < 0 or self.converted_amount < 0:
            raise AmountIsNegativeException()
