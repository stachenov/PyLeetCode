import pytest
from problems.container_with_most_water import Solution


@pytest.mark.parametrize("height,expected", [
    ([], 0),
    ([1], 0),
    ([1, 1], 1),
    ([1, 2], 1),
    ([2, 1, 2], 4),
    ([1, 2, 1], 2),
    ([3, 2, 1, 5], 9),
    ([3, 2, 1, 3], 9),
    ([1, 2, 3, 4, 4], 6),
    ([2, 1, 5], 4),
    ([3, 2, 4, 2, 5, 4], 15),
    ([2, 1, 3, 2, 5, 3, 5, 2, 1, 4], 21),
])
def test_maxArea(height, expected):
    assert Solution().maxArea(height) == expected
