import pytest

from fib.main import calculate_fibonacci_num
from fib.main import calculate_fibonacci_num_iterative


def test_calculate_fibonacci_num():
    assert calculate_fibonacci_num(7) == 13

    assert calculate_fibonacci_num(200) == 280571172992510140037611932413038677189525

    with pytest.raises(ValueError):
        calculate_fibonacci_num(0)

    with pytest.raises(ValueError):
        calculate_fibonacci_num(2.5)


def test_calculate_fibonacci_num_iterative():
    assert calculate_fibonacci_num_iterative(7) == 13

    assert calculate_fibonacci_num_iterative(200) == 280571172992510140037611932413038677189525

    with pytest.raises(ValueError):
        calculate_fibonacci_num_iterative(0)

    with pytest.raises(ValueError):
        calculate_fibonacci_num_iterative(2.5)
