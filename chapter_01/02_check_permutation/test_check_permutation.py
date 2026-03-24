import pytest
from check_permutation import check_permutation, check_permutation_dict


@pytest.mark.parametrize("fn", [check_permutation, check_permutation_dict])
class TestCheckPermutation:
    def test_permutation(self, fn):
        assert fn("abc", "bca") == True

    def test_not_permutation(self, fn):
        assert fn("abc", "bcd") == False

    def test_permutation_with_duplicates(self, fn):
        assert fn("aab", "baa") == True

    def test_not_permutation_with_duplicates(self, fn):
        assert fn("aab", "bab") == False


# Complexity:
#
#     | version                | time       | space |
#     |------------------------|------------|-------|
#     | check_permutation      | O(n log n) | O(n)  |
#     | check_permutation_dict | O(n)       | O(n)  |
