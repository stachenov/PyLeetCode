import pytest
from problems.palindrome_number import Solution


@pytest.mark.parametrize("x,expected", [
    (0, True),
    (1, True),
    (11, True),
    (12, False),
    (121, True),
    (10, False),
    (101, True),
])
def test(x, expected):
    assert Solution().isPalindrome(x) == expected
