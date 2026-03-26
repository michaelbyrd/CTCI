# Chapter 1 | Arrays and Strings
# Problem 1.9 — String Rotation
#
# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings s1 and s2, write code to check if s2 is a
# rotation of s1 using only one call to isSubstring.
#
# Example:
#   "waterbottle" is a rotation of "erbottlewat"


# Time: O(n), Space: O(n)
def string_rotation(
    s1, s2
):  # actually incorrect, see test case: test_shorter_substring_false_positive
    return s2 in (s1 + s1)


# Time: O(n), Space: O(n) — with length guard to prevent false positives
def string_rotation_v2(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)
