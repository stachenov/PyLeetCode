import pytest
from problems.longest_palindrome import Solution


@pytest.mark.parametrize("s, expected", [
    ("abccccdd", 7),
    ("", 0),
    ("ab", 1),
    ("aa", 2),
    ("aaa", 3),
    ("aab", 3),
    ("aabc", 3),
])
def test_longestPalindrome(s, expected):
    assert Solution().longestPalindrome(s) == expected
