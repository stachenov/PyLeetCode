import pytest
from problems.remove_k_digits import Solution


@pytest.mark.parametrize("num,k,expected", [
    ("1432219", 3, "1219"),
    ("10200", 1, "200"),
    ("10", 2, "0"),
    ("10", 1, "0"),
])
def test(num, k, expected):
    assert Solution().removeKdigits(num, k) == expected
