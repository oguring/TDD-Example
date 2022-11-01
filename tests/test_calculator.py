import pytest

from calculator.math import Calculator


def test_min():
    calc = Calculator()
    assert calc.min(1, 2) == 1
    assert calc.min(2, 1) == 1


def test_min_negative():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.min("1", 2)

    with pytest.raises(TypeError):
        calc.min(3.4, 2)

    with pytest.raises(TypeError):
        calc.min("1", "2")
