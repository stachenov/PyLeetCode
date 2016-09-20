import pytest
from problems.threesum_closest import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([0, 0, 0], 1, 0),
    ([-1, 2, 1, -4], 1, 2),
    ([-1, 2, 2, -4], -4, -3),
])
def test_threeSumClosest(nums, target, expected):
    assert Solution().threeSumClosest(nums, target) == expected
