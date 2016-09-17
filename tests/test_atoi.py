import pytest
from problems.atoi import Solution


@pytest.mark.parametrize("str,expected", [
    ("", 0),
    ("-", 0),
    (" ", 0),
    (" -", 0),
    ("1", 1),
    ("+1", 1),
    ("-1", -1),
    ("1a", 1),
    (" 1a", 1),
    (" 987654321 abcd", 987654321),
    ("2147483648", 2147483647),
    ("-2147483649", -2147483648),
])
def test(str, expected):
    assert Solution().myAtoi(str) == expected
