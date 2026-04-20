import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from node import from_list
from palindrome import palindrome


@pytest.mark.parametrize("fn", [palindrome])
class TestShortInput:
    def test_single_element(self, fn):
        assert fn(from_list([1])) == True

    def test_two_same(self, fn):
        assert fn(from_list([1, 1])) == True

    def test_two_different(self, fn):
        assert fn(from_list([1, 2])) == False

    def test_odd_palindrome(self, fn):
        assert fn(from_list([1, 2, 1])) == True

    def test_odd_not_palindrome(self, fn):
        assert fn(from_list([1, 2, 3])) == False

    def test_even_palindrome(self, fn):
        assert fn(from_list([1, 2, 2, 1])) == True

    def test_even_not_palindrome(self, fn):
        assert fn(from_list([1, 2, 3, 4])) == False

    def test_longer_palindrome(self, fn):
        assert fn(from_list([1, 2, 3, 2, 1])) == True

    def test_longer_not_palindrome(self, fn):
        assert fn(from_list([1, 2, 3, 4, 5])) == False


@pytest.mark.parametrize("fn", [palindrome])
class TestMediumInput:
    def test_length_50_palindrome(self, fn):
        vals = list(range(25)) + list(range(24, -1, -1))
        assert fn(from_list(vals)) == True

    def test_length_50_not_palindrome(self, fn):
        vals = list(range(50))
        assert fn(from_list(vals)) == False

    def test_length_100_palindrome(self, fn):
        vals = list(range(50)) + list(range(49, -1, -1))
        assert fn(from_list(vals)) == True


@pytest.mark.slow
@pytest.mark.parametrize("fn", [palindrome])
class TestLongInput:
    def test_length_1000_palindrome(self, fn):
        vals = list(range(500)) + list(range(499, -1, -1))
        assert fn(from_list(vals)) == True

    def test_length_1000_not_palindrome(self, fn):
        vals = list(range(1000))
        assert fn(from_list(vals)) == False

    def test_length_10000_palindrome(self, fn):
        vals = list(range(5000)) + list(range(4999, -1, -1))
        assert fn(from_list(vals)) == True
