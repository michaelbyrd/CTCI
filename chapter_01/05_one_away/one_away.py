# Chapter 1 | Arrays and Strings
# Problem 1.5 — One Away
#
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.
#
# Examples:
#   pale, ple   -> True
#   pales, pale -> True
#   pale, bale  -> True
#   pale, bake  -> False

from collections import Counter

# Time: O(n), Space: O(n) — uses Counter for the unequal-length case
def one_away_rough(s1, s2): 
    if(abs(len(s1) - len(s2)) > 1):
        return False
    elif(len(s1) == len(s2)):
        num_of_differences = 0
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                num_of_differences += 1
                if(num_of_differences > 1):
                    return False
        
        return True
    else: # length is off by 1
        # there should only be 1 non matching character
        c1 = Counter(s1)
        c2 = Counter(s2)

        diff = (c1 - c2) + (c2 - c1)
        if(len(diff) > 1):
            return False

        return True

# Time: O(n), Space: O(1) — two pointers, single pass, no extra data structures
def one_away_v2(s1, s2):
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2) > 1:
        return False

    i, j, differences = 0, 0, 0
    while i < l1 and j < l2:
        if s1[i] != s2[j]:
            differences += 1
            if differences > 1:
                return False
            if l1 > l2:
                i += 1
            elif l2 > l1:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return True

