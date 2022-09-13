import pytest


def test_float1_simple():
    my_int = 2.5 + 1.3 - 3.4

    assert my_int == pytest.approx(0.4, 0.01)


minus_parameters = [
    (5, 13, -8),
    (2, 3, -1),
    (7, 16, -9),
]


@pytest.mark.parametrize("a,b,expected", minus_parameters)
def test_int2_minus(a, b, expected):
    s = a - b
    assert s == expected