import pytest
from problems.two_sum import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([1, 2], 3, [0, 1]),
    ([1, 1], 2, [0, 1]),
    ([1, 2, 3], 4, [0, 2]),
])
def test(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
