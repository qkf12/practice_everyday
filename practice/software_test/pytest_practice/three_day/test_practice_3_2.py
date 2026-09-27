import pytest
def judgement_price(is_vip,price):
    if price < 100:
        return price
    elif price < 500:
        if is_vip:
            return price - price * 0.1
        else:
            return price - price * 0.05
    else:
        if is_vip:
            return price - price * 0.2
        else:
            return price - price * 0.1
@pytest.mark.parametrize("is_vip, price, expected", [
    (True,0,0), (False,0,0),
    (False,100,95),   (True,100,90),
    (False,499,474.05),(True,499,449.1),
    (False,500,450), (True,500,400),
    (False,600,540), (True,600,480)
])
def test_judgement_price(is_vip, price, expected):
    assert judgement_price(is_vip, price) == pytest.approx(expected)
