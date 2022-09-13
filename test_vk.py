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


def test_set1():
    s = {"one", "two"}

    assert len(s) == 2


set_parameters = [
    ({"one", "three"}, {"two"}, {"one", "two", "three"}),
]


@pytest.mark.parametrize("a,b,expected", set_parameters)
def test_set2(a, b, expected):
    z = a.union(b)

    assert z == expected

def test_str1():
    u = "one".upper()

    assert u == "ONE"


str_parameters = [
    ("tWo", "two"),
    ("swFF", "swff")
]


@pytest.mark.parametrize("a,expected", str_parameters)
def test_str2(a, expected):
    z = a.lower()

    assert z == expected
