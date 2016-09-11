import pytest

from problems.integer_replacement import Solution

@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("n,expected", [
    (1, 0),
    (2, 1),
    (3, 2),
    (8, 3),
    (7, 4),
    (65535, 17),
    (100000000, 31),
    (2147483647, 32),
])
def test(solution,n,expected):
    assert solution.integerReplacement(n) == expected
