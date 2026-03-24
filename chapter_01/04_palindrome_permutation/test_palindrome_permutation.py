import pytest
from palindrome_permutation import palindrome_permutation, palindrome_permutation_counter, palindrome_permutation_set


@pytest.mark.parametrize("fn", [
    palindrome_permutation,
    palindrome_permutation_counter,
    palindrome_permutation_set,
])
class TestShortInput:  # length 0-99
    def test_empty_string(self, fn):
        assert fn("") == True

    def test_single_character(self, fn):
        assert fn("a") == True

    def test_two_different_chars(self, fn):
        assert fn("ab") == False

    def test_case_insensitive(self, fn):
        assert fn("Aa") == True

    def test_spaces_ignored(self, fn):
        assert fn("a b a") == True

    def test_already_a_palindrome(self, fn):
        assert fn("racecar") == True

    def test_permutation_of_palindrome(self, fn):
        assert fn("Tact Coa") == True

    def test_not_permutation_of_palindrome(self, fn):
        assert fn("hello") == False

    def test_length_25_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabba") == True

    def test_length_25_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxy") == False

    def test_length_50_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_50_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx") == False


@pytest.mark.parametrize("fn", [
    palindrome_permutation,
    palindrome_permutation_counter,
    palindrome_permutation_set,
])
class TestMediumInput:  # length 100-999
    def test_length_100_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_100_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu") == False

    def test_length_200_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_200_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrs") == False

    def test_length_500_true(self, fn):
        assert fn("ab" * 250) == True

    def test_length_500_false(self, fn):
        assert fn("abc" * 167) == False  # a=167, b=167, c=167 — all odd counts

    def test_length_999_true(self, fn):
        assert fn("ab" * 499 + "a") == True

    def test_length_999_false(self, fn):
        assert fn("abc" * 333) == False  # a=333, b=333, c=333 — all odd counts


@pytest.mark.slow
@pytest.mark.parametrize("fn", [
    palindrome_permutation,
    palindrome_permutation_counter,
    palindrome_permutation_set,
])
class TestLongInput:  # length 1000+
    def test_length_1000_true(self, fn):
        assert fn("ab" * 500) == True

    def test_length_1000_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxy" * 40) == False

    def test_length_10000_true(self, fn):
        assert fn("ab" * 5000) == True

    def test_length_10000_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxy" * 400) == False

    def test_length_50000_true(self, fn):
        assert fn("ab" * 25000) == True

    def test_length_50000_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxy" * 2000) == False


# Benchmark results (per-run averages):
#
#                    dict        counter     set
# short  (0-99)    0.0167ms    0.0176ms    0.0097ms  <- set wins
# medium (100-999) 0.1675ms    0.0832ms    0.1485ms  <- counter wins
# long   (1000+)   6.1972ms    3.1345ms    4.6202ms  <- counter wins
#
# Set fastest for short inputs (single pass, no counting overhead)
# Counter wins at medium/long — C-optimized internals outperform manual loops
#
# Complexity:
#
#     | version                       | time  | space |
#     |-------------------------------|-------|-------|
#     | palindrome_permutation (dict) | O(n)  | O(k)  |
#     | palindrome_permutation_counter| O(n)  | O(k)  |
#     | palindrome_permutation_set    | O(n)  | O(k)  |
#
#     k = number of unique characters (bounded by charset size, e.g. 26 for lowercase alpha)
