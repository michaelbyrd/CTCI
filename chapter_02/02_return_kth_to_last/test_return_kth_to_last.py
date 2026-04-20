import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list
from return_kth_to_last import return_kth_to_last


@pytest.mark.parametrize("fn", [return_kth_to_last])
class TestShortInput:  # length 0-9
    def test_last_element(self, fn):
        assert fn(from_list([1, 2, 3, 4, 5]), 1) == 5

    def test_second_to_last(self, fn):
        assert fn(from_list([1, 2, 3, 4, 5]), 2) == 4

    def test_third_to_last(self, fn):
        assert fn(from_list([1, 2, 3, 4, 5]), 3) == 3

    def test_first_element(self, fn):
        assert fn(from_list([1, 2, 3, 4, 5]), 5) == 1

    def test_single_element(self, fn):
        assert fn(from_list([7]), 1) == 7

    def test_two_elements(self, fn):
        assert fn(from_list([1, 2]), 2) == 1


@pytest.mark.parametrize("fn", [return_kth_to_last])
class TestMediumInput:  # length 10-99
    def test_length_50_kth_1(self, fn):
        vals = list(range(50))
        assert fn(from_list(vals), 1) == 49

    def test_length_50_kth_25(self, fn):
        vals = list(range(50))
        assert fn(from_list(vals), 25) == 24

    def test_length_50_kth_50(self, fn):
        vals = list(range(50))
        assert fn(from_list(vals), 50) == 0


@pytest.mark.slow
@pytest.mark.parametrize("fn", [return_kth_to_last])
class TestLongInput:  # length 100+
    def test_length_1000_kth_1(self, fn):
        vals = list(range(1000))
        assert fn(from_list(vals), 1) == 999

    def test_length_1000_kth_500(self, fn):
        vals = list(range(1000))
        assert fn(from_list(vals), 500) == 499
