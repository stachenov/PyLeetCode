import pytest
from problems.longest_without_repeating_chars import Solution


@pytest.mark.parametrize("s,expected", [
    ("", 0),
    ("a", 1),
    ("aa", 1),
    ("ab", 2),
    ("pwwkew", 3),
])
def test(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
