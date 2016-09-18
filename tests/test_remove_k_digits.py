import pytest
from problems.remove_k_digits import Solution


@pytest.mark.parametrize("num,k,expected", [
    ("1432219", 3, "1219"),
    ("10200", 1, "200"),
    ("10", 2, "0"),
    ("10", 1, "0"),
    ("9", 1, "0"),
    ("19", 1, "1"),
    ("91", 1, "1"),
    ("1234567890", 9, "0"),
])
def test_removeKdigits(num, k, expected):
    assert Solution().removeKdigits(num, k) == expected
