from domain.entities.currency import Currency
from domain.value_objects.currency_code import Code


def test_currency_value():
    code = Code("USD")
    currency = Currency(code, "United States dollar", "$")

    assert currency.code == code
    assert currency.fullname == "United States dollar"
    assert currency.sign == "$"
