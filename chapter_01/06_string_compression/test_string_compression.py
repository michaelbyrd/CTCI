import pytest
from string_compression import string_compression, string_compression_v2, string_compression_v3


@pytest.mark.parametrize("fn", [string_compression, string_compression_v2, string_compression_v3])
class TestShortInput:  # length 0-99
    def test_basic(self, fn):
        assert fn("aabcccccaaa") == "a2b1c5a3"

    def test_no_compression(self, fn):
        assert fn("abcd") == "abcd"

    def test_single_char(self, fn):
        assert fn("a") == "a"

    def test_all_same(self, fn):
        assert fn("aaaa") == "a4"

    def test_two_chars(self, fn):
        assert fn("aabb") == "aabb"

    def test_length_50_compressible(self, fn):
        assert fn("aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeee") == "a10b10c10d10e10"

    def test_length_50_no_compression(self, fn):
        assert fn("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx") == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx"


@pytest.mark.parametrize("fn", [string_compression, string_compression_v2, string_compression_v3])
class TestMediumInput:  # length 100-999
    def test_length_100_compressible(self, fn):
        assert fn("a" * 50 + "b" * 50) == "a50b50"

    def test_length_100_no_compression(self, fn):
        assert fn("abcdefghij" * 10) == "abcdefghij" * 10

    def test_length_200_compressible(self, fn):
        assert fn("a" * 100 + "b" * 100) == "a100b100"

    def test_length_200_no_compression(self, fn):
        assert fn("abcdefghij" * 20) == "abcdefghij" * 20

    def test_length_500_compressible(self, fn):
        assert fn("a" * 250 + "b" * 250) == "a250b250"

    def test_length_500_no_compression(self, fn):
        assert fn("abcdefghij" * 50) == "abcdefghij" * 50

    def test_length_999_compressible(self, fn):
        assert fn("a" * 500 + "b" * 499) == "a500b499"

    def test_length_999_no_compression(self, fn):
        assert fn("abcdefghij" * 99 + "a") == "abcdefghij" * 99 + "a"


@pytest.mark.slow
@pytest.mark.parametrize("fn", [string_compression, string_compression_v2, string_compression_v3])
class TestLongInput:  # length 1000+
    def test_length_10000_compressible(self, fn):
        assert fn("a" * 5000 + "b" * 5000) == "a5000b5000"

    def test_length_10000_no_compression(self, fn):
        assert fn("abcdefghij" * 1000) == "abcdefghij" * 1000

    def test_length_50000_compressible(self, fn):
        assert fn("a" * 25000 + "b" * 25000) == "a25000b25000"

    def test_length_50000_no_compression(self, fn):
        assert fn("abcdefghij" * 5000) == "abcdefghij" * 5000


@pytest.mark.slow
@pytest.mark.parametrize("fn", [string_compression, string_compression_v2, string_compression_v3])
class TestIncompressibleHeavy:  # all inputs return original string — v3 advantage case
    def test_incompressible_100(self, fn):
        assert fn("abcdefghij" * 10) == "abcdefghij" * 10

    def test_incompressible_500(self, fn):
        assert fn("abcdefghij" * 50) == "abcdefghij" * 50

    def test_incompressible_1000(self, fn):
        assert fn("abcdefghij" * 100) == "abcdefghij" * 100

    def test_incompressible_5000(self, fn):
        assert fn("abcdefghij" * 500) == "abcdefghij" * 500

    def test_incompressible_10000(self, fn):
        assert fn("abcdefghij" * 1000) == "abcdefghij" * 1000

    def test_incompressible_50000(self, fn):
        assert fn("abcdefghij" * 5000) == "abcdefghij" * 5000


# Benchmark results (1,000 runs, per-run averages):
#
#                          v1          v2          v3
# short  (0-99)         0.0338ms    0.0360ms    0.0402ms
# medium (100-999)      0.3904ms    0.3736ms    0.4370ms
# long   (1000+)       15.1013ms   13.8251ms   16.3863ms  <- v2 wins
#
# v2 (join) wins at medium/long — str += is costly at scale.
# v3 (pre-check length) is slower overall because it does 2 passes for
# compressible strings. v3 would win if most real inputs are incompressible.
#
# Benchmark: mixed (50/50 compressible) vs incompressible-only inputs:
#                                v1          v2          v3
# mixed (50/50)             15.2369ms   13.9813ms   16.7352ms  <- v2 wins
# incompressible only       12.4581ms   11.0220ms    9.5131ms  <- v3 wins!
#
# Complexity:
#
#     | version | time              | space                              |
#     |---------|-------------------|------------------------------------|
#     | v1      | O(n²)             | O(n)                               |
#     | v2      | O(n)              | O(n)                               |
#     | v3      | O(n) / O(2n) worst| O(1) incompressible / O(n) compress|
