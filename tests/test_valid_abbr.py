import pytest
from problems.valid_abbr import Solution


@pytest.mark.parametrize("word, abbr, expected", [
    ("", "", True),
    ("a", "a", True),
    ("a", "1", True),
    ("a", "2", False),
    ("ab", "a1", True),
    ("ab", "2", True),
    ("abcdefghijklm", "13", True),
    ("abcdefghijklm", "a12", True),
    ("abcdefghijklm", "12m", True),
    ("abcdefghijklm", "a1c9m", True),
    ("hi", "2i", False),
    ("a", "01", False),
])
def test_validWordAbbreviation(word, abbr, expected):
    assert Solution().validWordAbbreviation(word, abbr) == expected
