import pytest
from problems.foursum import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([1, 0, -1, 0, -2, 2], 0, [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]),
])
def test_fourSum(nums, target, expected):
    assert Solution().fourSum(nums, target) == expected
