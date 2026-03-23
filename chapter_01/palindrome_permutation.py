# Chapter 1 | Arrays and Strings
# Problem 1.4 — Palindrome Permutation
#
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
#
# Example:
#   Input:  "Tact Coa"
#   Output: True (permutations: "taco cat", "atco cta", etc.)




import pytest
from collections import Counter

def clean_string(string):
    return string.replace(" ", "").lower()

def palindrome_permutation(string):
    counts = {}
    for char in clean_string(string):
        counts[char] = counts.get(char, 0) + 1

    # count the number of odd values in array (counts.values)
    return sum(v % 2 != 0 for v in counts.values()) <= 1


# same solution just with a helper function to create the
def palindrome_permutation_counter(string):
    counts = Counter(clean_string(string))
    return sum(v % 2 != 0 for v in counts.values()) <= 1


# uses a set and has improved performace
# - solves in a single pass rather than building the dict of counts then iterating again
def palindrome_permutation_set(string):
    seen = set()
    for char in clean_string(string):
        if char in seen:
            seen.remove(char)
        else:
            seen.add(char)
    return len(seen) <= 1


@pytest.mark.parametrize("fn", [
    palindrome_permutation,
    palindrome_permutation_counter,
    palindrome_permutation_set,
])
class TestPalindromePermutation:
    def test_permutation_of_palindrome(self, fn):
        assert fn("Tact Coa") == True

    def test_not_permutation_of_palindrome(self, fn):
        assert fn("hello") == False

    def test_already_a_palindrome(self, fn):
        assert fn("racecar") == True

    def test_single_character(self, fn):
        assert fn("a") == True

    def test_empty_string(self, fn):
        assert fn("") == True

    def test_two_different_chars(self, fn):
        assert fn("ab") == False

    def test_case_insensitive(self, fn):
        assert fn("Aa") == True

    def test_spaces_ignored(self, fn):
        assert fn("a b a") == True

    def test_length_25_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabba") == True

    def test_length_25_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxy") == False

    def test_length_50_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_50_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx") == False

    def test_length_100_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_100_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu") == False

    def test_length_200_true(self, fn):
        assert fn("aabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddeeaabbccddee") == True

    def test_length_200_false(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrs") == False


# Benchmark results (100,000 runs over 8 short test cases):
# palindrome_permutation         (dict)     0.49s  (0.0049ms per run)
# palindrome_permutation_counter (Counter)  0.78s  (0.0078ms per run)
# palindrome_permutation_set     (set)      0.25s  (0.0024ms per run)
#
# Benchmark results (100,000 runs over 16 test cases including lengths 25, 50, 100, 200):
# palindrome_permutation         (dict)     4.90s  (0.0490ms per run)
# palindrome_permutation_counter (Counter)  3.58s  (0.0358ms per run)  <- faster at scale
# palindrome_permutation_set     (set)      3.46s  (0.0346ms per run)  <- still fastest

# Set is still fastest, but now only barely ahead of Counter
# Counter overtook the dict solution at scale — its C-optimized internals kick in on longer strings
# Dict fell to last place — the manual Python loop doesn't scale as well as Counter's native implementation