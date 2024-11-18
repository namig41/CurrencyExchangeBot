from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class AmountIsNegativeException(ApplicationException):
    @property
    def message(self):
        return "Средства не могут быть отрицательными"
