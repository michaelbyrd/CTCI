import pytest
from urlify import urlify


class TestUrlify:
    def test_basic(self):
        assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"

    def test_no_spaces(self):
        assert urlify("abc", 3) == "abc"
