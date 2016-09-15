import pytest
from problems.is_subsequence import Solution


@pytest.mark.parametrize("s,t,expected", [
    ("", "", True),
    ("aa", "a", False),
    ("aa", "aba", True),
    ("ac", "aba", False),
])
def test(s, t, expected):
    solution = Solution()
    assert solution.isSubsequence(s, t) is expected
