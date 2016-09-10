import pytest

from problems.range_addition import Solution


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize("length,updates,expected", [
    (0, [], []),
    (1, [(0, 0, +2)], [2]),
    (2, [(0, 0, +2), (0, 1, +1)], [3, 1]),
    (3, [(0, 2, +1), (0, 1, -1), (1, 2, +2)], [0, 2, 3]),
])
def test(solution, length, updates, expected):
    assert solution.getModifiedArray(length, updates) == expected