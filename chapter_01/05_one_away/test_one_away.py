import pytest
from one_away import one_away_rough, one_away_v2


@pytest.mark.parametrize("fn", [one_away_rough, one_away_v2])
class TestOneAway:
    def test_one_removal(self, fn):
        assert fn("pale", "ple") == True

    def test_one_insertion(self, fn):
        assert fn("pales", "pale") == True

    def test_one_replacement(self, fn):
        assert fn("pale", "bale") == True

    def test_two_replacements(self, fn):
        assert fn("pale", "bake") == False

    def test_identical_strings(self, fn):
        assert fn("pale", "pale") == True

    def test_delete_and_replace(self, fn):
        assert fn("pale", "plo") == False

    def test_very_different_lengths(self, fn):
        assert fn("pale", "paleish") == False

    def test_empty_strings(self, fn):
        assert fn("", "") == True

    def test_one_empty_one_char(self, fn):
        assert fn("", "a") == True

    def test_one_empty_two_chars(self, fn):
        assert fn("", "ab") == False

    def test_insertion_at_start(self, fn):
        assert fn("pale", "xpale") == True

    def test_long_identical(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz") == True

    def test_long_one_replacement(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyZ") == True

    def test_long_two_replacements(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwXYZ") == False

    def test_long_one_insertion(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz1") == True

    def test_long_two_insertions(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz12") == False


# Benchmark results (100,000 runs over 16 test cases):
# one_away_rough  3.32s  (0.0332ms per run)
# one_away_v2     0.90s  (0.0090ms per run)  <- ~4x faster (single pass, no Counter overhead)
#
# Complexity:
#
#     | version       | time  | space |
#     |---------------|-------|-------|
#     | one_away_rough| O(n)  | O(n)  |
#     | one_away_v2   | O(n)  | O(1)  |
#
#     one_away_rough uses Counter (O(n) space); one_away_v2 uses two pointers (O(1) space)
