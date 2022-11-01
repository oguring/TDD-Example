from calculator.math import Calculator


def test_min():
    calc = Calculator()
    assert calc.min(1, 2) == 1
    assert calc.min(2, 1) == 1
