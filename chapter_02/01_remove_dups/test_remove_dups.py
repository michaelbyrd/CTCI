import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list, to_list
from remove_dups import remove_dups, remove_dups_no_buffer


@pytest.mark.parametrize("fn", [remove_dups, remove_dups_no_buffer])
class TestShortInput:  # length 0-9
    def test_empty(self, fn):
        assert to_list(fn(None)) == []

    def test_single(self, fn):
        assert to_list(fn(from_list([1]))) == [1]

    def test_no_dups(self, fn):
        assert to_list(fn(from_list([1, 2, 3]))) == [1, 2, 3]

    def test_adjacent_dup(self, fn):
        assert to_list(fn(from_list([1, 1, 2]))) == [1, 2]

    def test_non_adjacent_dup(self, fn):
        assert to_list(fn(from_list([1, 2, 3, 2, 1]))) == [1, 2, 3]

    def test_all_same(self, fn):
        assert to_list(fn(from_list([5, 5, 5, 5]))) == [5]

    def test_dup_at_end(self, fn):
        assert to_list(fn(from_list([1, 2, 3, 3]))) == [1, 2, 3]


@pytest.mark.parametrize("fn", [remove_dups, remove_dups_no_buffer])
class TestMediumInput:  # length 10-99
    def test_length_20_no_dups(self, fn):
        vals = list(range(20))
        assert to_list(fn(from_list(vals))) == vals

    def test_length_20_with_dups(self, fn):
        vals = list(range(10)) * 2
        assert to_list(fn(from_list(vals))) == list(range(10))

    def test_length_50_with_dups(self, fn):
        vals = list(range(10)) * 5
        assert to_list(fn(from_list(vals))) == list(range(10))


@pytest.mark.slow
@pytest.mark.parametrize("fn", [remove_dups, remove_dups_no_buffer])
class TestLongInput:  # length 100+
    def test_length_1000_with_dups(self, fn):
        vals = list(range(100)) * 10
        assert to_list(fn(from_list(vals))) == list(range(100))

    def test_length_10000_with_dups(self, fn):
        vals = list(range(100)) * 100
        assert to_list(fn(from_list(vals))) == list(range(100))
