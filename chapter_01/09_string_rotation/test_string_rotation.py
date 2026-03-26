import pytest
from string_rotation import string_rotation, string_rotation_v2


@pytest.mark.parametrize("fn", [string_rotation_v2])
class TestShortInput:  # length 0-99
    def test_empty_strings(self, fn):
        assert fn("", "") == True

    def test_single_char_match(self, fn):
        assert fn("a", "a") == True

    def test_single_char_no_match(self, fn):
        assert fn("a", "b") == False

    def test_basic_rotation(self, fn):
        assert fn("waterbottle", "erbottlewat") == True

    def test_not_a_rotation(self, fn):
        assert fn("waterbottle", "bottleWater") == False

    def test_same_string(self, fn):
        assert fn("abcde", "abcde") == True

    def test_different_lengths(self, fn):
        assert fn("abc", "abcd") == False

    def test_rotation_at_start(self, fn):
        assert fn("abcde", "bcdea") == True

    def test_rotation_at_end(self, fn):
        assert fn("abcde", "eabcd") == True

    def test_repeated_chars(self, fn):
        assert fn("aabaa", "baaaa") == True

    def test_shorter_substring_false_positive(self, fn):
        # "ab" appears in "abab" (s1+s1) but is not a rotation of "abab"
        assert fn("abab", "ab") == False

    def test_length_50_rotation(self, fn):
        s1 = "abcdefghij" * 5
        s2 = s1[20:] + s1[:20]
        assert fn(s1, s2) == True

    def test_length_50_no_rotation(self, fn):
        s1 = "abcdefghij" * 5
        s2 = "zyxwvutsrq" * 5
        assert fn(s1, s2) == False


@pytest.mark.parametrize("fn", [string_rotation, string_rotation_v2])
class TestMediumInput:  # length 100-999
    def test_length_100_rotation(self, fn):
        s1 = "abcdefghij" * 10
        s2 = s1[50:] + s1[:50]
        assert fn(s1, s2) == True

    def test_length_100_no_rotation(self, fn):
        s1 = "abcdefghij" * 10
        s2 = "zyxwvutsrq" * 10
        assert fn(s1, s2) == False

    def test_length_500_rotation(self, fn):
        s1 = "abcdefghij" * 50
        s2 = s1[250:] + s1[:250]
        assert fn(s1, s2) == True

    def test_length_500_no_rotation(self, fn):
        s1 = "abcdefghij" * 50
        s2 = "zyxwvutsrq" * 50
        assert fn(s1, s2) == False


@pytest.mark.slow
@pytest.mark.parametrize("fn", [string_rotation, string_rotation_v2])
class TestLongInput:  # length 1000+
    def test_length_1000_rotation(self, fn):
        s1 = "abcdefghij" * 100
        s2 = s1[500:] + s1[:500]
        assert fn(s1, s2) == True

    def test_length_1000_no_rotation(self, fn):
        s1 = "abcdefghij" * 100
        s2 = "zyxwvutsrq" * 100
        assert fn(s1, s2) == False

    def test_length_10000_rotation(self, fn):
        s1 = "abcdefghij" * 1000
        s2 = s1[5000:] + s1[:5000]
        assert fn(s1, s2) == True

    def test_length_10000_no_rotation(self, fn):
        s1 = "abcdefghij" * 1000
        s2 = "zyxwvutsrq" * 1000
        assert fn(s1, s2) == False


# Benchmark results (10,000 runs, per-run averages):
#
#                          string_rotation
# short  (11 chars)        0.0001ms
# medium (500 chars)       0.0006ms
# long   (10000 chars)     0.0087ms
#
# Extremely fast — Python's `in` uses optimized C-level string search (Boyer-Moore-Horspool).
#
# Complexity:
#
#     | version         | time  | space |
#     |-----------------|-------|-------|
#     | string_rotation | O(n)  | O(n)  |
#
#     Time: O(n) for the substring search on a 2n string
#     Space: O(n) to construct s1 + s1
