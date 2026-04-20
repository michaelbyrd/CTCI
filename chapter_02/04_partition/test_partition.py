import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list, to_list
from partition import partition


def is_valid_partition(result, x):
    """Check all values < x come before all values >= x."""
    seen_gte = False
    for val in result:
        if val >= x:
            seen_gte = True
        elif seen_gte:
            return False
    return True


@pytest.mark.parametrize("fn", [partition])
class TestShortInput:
    def test_basic(self, fn):
        result = to_list(fn(from_list([3, 5, 8, 5, 10, 2, 1]), 5))
        assert is_valid_partition(result, 5)
        assert sorted(result) == sorted([3, 5, 8, 5, 10, 2, 1])

    def test_all_less_than_x(self, fn):
        result = to_list(fn(from_list([1, 2, 3]), 5))
        assert is_valid_partition(result, 5)
        assert sorted(result) == [1, 2, 3]

    def test_all_greater_than_x(self, fn):
        result = to_list(fn(from_list([6, 7, 8]), 5))
        assert is_valid_partition(result, 5)
        assert sorted(result) == [6, 7, 8]

    def test_single_element_less(self, fn):
        result = to_list(fn(from_list([3]), 5))
        assert result == [3]

    def test_single_element_equal(self, fn):
        result = to_list(fn(from_list([5]), 5))
        assert result == [5]

    def test_already_partitioned(self, fn):
        result = to_list(fn(from_list([1, 2, 5, 6]), 5))
        assert is_valid_partition(result, 5)
        assert sorted(result) == [1, 2, 5, 6]


@pytest.mark.parametrize("fn", [partition])
class TestMediumInput:
    def test_length_50(self, fn):
        import random
        random.seed(42)
        vals = [random.randint(1, 20) for _ in range(50)]
        result = to_list(fn(from_list(vals), 10))
        assert is_valid_partition(result, 10)
        assert sorted(result) == sorted(vals)

    def test_length_100(self, fn):
        vals = list(range(100, 0, -1))
        result = to_list(fn(from_list(vals), 50))
        assert is_valid_partition(result, 50)
        assert sorted(result) == sorted(vals)


@pytest.mark.slow
@pytest.mark.parametrize("fn", [partition])
class TestLongInput:
    def test_length_1000(self, fn):
        vals = list(range(1000, 0, -1))
        result = to_list(fn(from_list(vals), 500))
        assert is_valid_partition(result, 500)
        assert sorted(result) == sorted(vals)
