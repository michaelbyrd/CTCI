import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list, to_list
from sum_lists import sum_lists


@pytest.mark.parametrize("fn", [sum_lists])
class TestShortInput:
    def test_basic(self, fn):
        # 617 + 295 = 912
        l1 = from_list([7, 1, 6])
        l2 = from_list([5, 9, 2])
        assert to_list(fn(l1, l2)) == [2, 1, 9]

    def test_with_carry(self, fn):
        # 99 + 1 = 100
        l1 = from_list([9, 9])
        l2 = from_list([1])
        assert to_list(fn(l1, l2)) == [0, 0, 1]

    def test_single_digits(self, fn):
        # 3 + 4 = 7
        l1 = from_list([3])
        l2 = from_list([4])
        assert to_list(fn(l1, l2)) == [7]

    def test_single_digits_with_carry(self, fn):
        # 9 + 9 = 18
        l1 = from_list([9])
        l2 = from_list([9])
        assert to_list(fn(l1, l2)) == [8, 1]

    def test_different_lengths(self, fn):
        # 100 + 99 = 199
        l1 = from_list([0, 0, 1])
        l2 = from_list([9, 9])
        assert to_list(fn(l1, l2)) == [9, 9, 1]

    def test_zeros(self, fn):
        l1 = from_list([0])
        l2 = from_list([0])
        assert to_list(fn(l1, l2)) == [0]


@pytest.mark.parametrize("fn", [sum_lists])
class TestMediumInput:
    def test_large_numbers(self, fn):
        # 999999999 + 1 = 1000000000
        l1 = from_list([9] * 9)
        l2 = from_list([1])
        assert to_list(fn(l1, l2)) == [0] * 9 + [1]

    def test_equal_large(self, fn):
        # 50-digit numbers
        l1 = from_list([5] * 50)
        l2 = from_list([5] * 50)
        result = to_list(fn(l1, l2))
        # 5+5=10 each time, so all 0s with carry propagation
        assert len(result) == 51


@pytest.mark.slow
@pytest.mark.parametrize("fn", [sum_lists])
class TestLongInput:
    def test_1000_digit_numbers(self, fn):
        l1 = from_list([9] * 1000)
        l2 = from_list([1])
        result = to_list(fn(l1, l2))
        assert result == [0] * 1000 + [1]
