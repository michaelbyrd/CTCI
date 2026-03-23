# Chapter 1 | Arrays and Strings
# Problem 1.3 — URLify
#
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient trailing spaces at the end
# to hold the additional characters, and that you are given the "true" length
# of the string.
#
# Example:
#   Input:  "Mr John Smith    ", 13
#   Output: "Mr%20John%20Smith"


def urlify(string, length):
    url = ''
    for char in string[:length]:
        if(char == ' '):
            url += '%20'
        else:
            url += char
    return url
