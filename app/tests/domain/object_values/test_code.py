from domain.value_objects.currency_code import Code


def test_code_value():
    code_usd = Code("USD")
    code_eur = Code("EUR")

    assert code_usd != code_eur
    assert code_usd == code_usd
