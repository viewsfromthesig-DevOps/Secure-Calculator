import pytest

from calculator import add, calculate, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("3 + 4", 7),
        ("10 - 2.5", 7.5),
        ("6 * 7", 42),
        ("9 / 3", 3),
        ("-2 + 5", 3),
    ],
)
def test_calculate_valid_expressions(expression, expected):
    assert calculate(expression) == expected


@pytest.mark.parametrize(
    "bad_input",
    [
        "3 +",                    # missing a number
        "3 ^ 4",                  # unsupported operator
        "three + four",           # not numbers
        "__import__('os').system('ls')",  # code injection attempt
    ],
)
def test_calculate_rejects_bad_input(bad_input):
    with pytest.raises(ValueError):
        calculate(bad_input)
