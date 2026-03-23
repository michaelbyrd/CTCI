import pytest
from one_away import one_away


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
