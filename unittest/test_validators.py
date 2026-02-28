import pytest
import regular_expressions.validators as validators


@pytest.mark.parametrize("email, expected", [
    ("didier.dbo@gmail.com",  True),   # cas nominal
    ("user+tag@gmail.com",    True),   # + autorisé
    ("user@mail.domain.com",  True),   # sous-domaine
    ("didier.dbogmail.com",   False),  # @ manquant
    ("@gmail.com",            False),  # username manquant
    ("user@.com",             False),  # domaine invalide
    ("user@domain",           False),  # pas de TLD
    ("",                      False),  # chaîne vide
])
def test_email(email, expected):
    assert validators.is_email_valid(email) == expected

