import pytest

def judgement_age (age):
    if age < 12:
        return 30
    elif age <= 60:
        return 50
    else:
        return 20
@pytest.mark.parametrize("age, expected", [(6,30),(16,50),(66,20)])
def test_judgement_age (age, expected):
    assert judgement_age(age) == expected