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


import pytest


def one_away(s1, s2):
    pass


class TestOneAway:
    def test_one_removal(self):
        assert one_away("pale", "ple") == True

    def test_one_insertion(self):
        assert one_away("pales", "pale") == True

    def test_one_replacement(self):
        assert one_away("pale", "bale") == True

    def test_two_replacements(self):
        assert one_away("pale", "bake") == False

    def test_identical_strings(self):
        assert one_away("pale", "pale") == True

    def test_very_different_lengths(self):
        assert one_away("pale", "paleish") == False
