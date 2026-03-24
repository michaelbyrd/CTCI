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

from collections import Counter


def clean_string(string):
    return string.replace(" ", "").lower()


# Time: O(n), Space: O(k) — k = unique characters
def palindrome_permutation(string):
    counts = {}
    for char in clean_string(string):
        counts[char] = counts.get(char, 0) + 1

    # count the number of odd values in array (counts.values)
    return sum(v % 2 != 0 for v in counts.values()) <= 1


# Time: O(n), Space: O(k) — Counter is C-optimized, faster at scale
def palindrome_permutation_counter(string):
    counts = Counter(clean_string(string))
    return sum(v % 2 != 0 for v in counts.values()) <= 1


# Time: O(n), Space: O(k) — single pass, no second iteration over counts
def palindrome_permutation_set(string):
    seen = set()
    for char in clean_string(string):
        if char in seen:
            seen.remove(char)
        else:
            seen.add(char)
    return len(seen) <= 1
