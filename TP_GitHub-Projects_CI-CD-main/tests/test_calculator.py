import pytest

from app.calculator import add, divide, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="^Division par zéro$"):
        divide(10, 0)

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(0, 5) == 0

def test_multiply_negative_number():
    assert multiply(-2, 3) == -6
