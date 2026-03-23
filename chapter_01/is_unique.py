# Chapter 1 | Arrays and Strings
# Problem 1.1 — Is Unique
#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


# Simple solution using set
def is_unique(string):
    return len(string) == len(set(string))


# Ideal solution
# Uses a single integer as a bit vector. For each character, it shifts 1 left
# by the character's ASCII value to get a bit position, then checks if that bit
# is already set. If so, duplicate found. Otherwise it sets the bit and moves
# on. The integer never grows beyond 128 bits regardless of input length.

def is_unique_bitmask(string):
    checker = 0
    for char in string:
        bit = 1 << ord(char)
        if checker & bit:
            return False
        checker |= bit
    return True


if __name__ == "__main__":
    print(is_unique("abcde"))           # True
    print(is_unique("aabcde"))          # False
    print(is_unique_bitmask("abcde"))   # True
    print(is_unique_bitmask("aabcde"))  # False
