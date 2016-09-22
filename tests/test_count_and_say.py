import pytest
from problems.count_and_say import Solution


@pytest.mark.parametrize("n,expected", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
])
def test_countAndSay(n, expected):
    assert Solution().countAndSay(n) == expected
