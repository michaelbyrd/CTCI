# Chapter 1 | Arrays and Strings
# Problem 1.2 — Check Permutation
#
# Given two strings, write a method to decide if one is a permutation of the other.
#
# A permutation is a rearrangement of all the characters in a string such that
# both strings contain the exact same characters with the same frequencies.
#
# A bitmask is a single integer used as a fixed-size array of bits, where each
# bit represents a boolean value (seen/not seen). It avoids allocating a data
# structure by encoding state directly into the bits of one number.

from collections import Counter

def check_permutation(s1, s2):
   return sorted(s1) == sorted(s2)

  

def check_permutation_dict(s1, s2):
    return Counter(s1) == Counter (s2)


import pytest

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
