import pytest
from problems.first_missing_positive import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([1, 3, 5], 2),
    ([-1, -2, -3], 1),
    ([1, 2, 3], 4),
    ([3, 2, 1], 4),
    ([1, 1], 2),
    ([1, 1, 2], 3),
])
def test_firstMissingPositive(nums, expected):
    assert Solution().firstMissingPositive(nums) == expected
