import pytest
from problems.foursum import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([0, 0, 0], 0, []),
    ([0, 0, 0, 0], 0, [
        [0, 0, 0, 0],
    ]),
    ([1, 0, -1, 0, -2, 2], 0, [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]),
])
def test_fourSum(nums, target, expected):
    quadruples = Solution().fourSum(nums, target)
    assert len(quadruples) == len(expected)
    assert set(map(tuple, quadruples)) == set(map(tuple, expected))
