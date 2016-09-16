import pytest
from problems.longest_with_k_repeating_characters import Solution


@pytest.mark.parametrize("s,k,expected", [
    ("a", 1, 1),
    ("", 1, 0),
    ("aaba", 2, 2),
    ("aabbaa", 2, 6),
])
def test(s, k, expected):
    assert Solution().longestSubstring(s, k) == expected
