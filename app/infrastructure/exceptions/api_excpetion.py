from dataclasses import dataclass

from infrastructure.exceptions.base import InfrastructureException


@dataclass(eq=False)
class APIServiceException(InfrastructureException):
    text: str

    @property
    def message(self):
        return self.text
