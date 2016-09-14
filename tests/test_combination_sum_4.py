import pytest
from problems.combination_sum_4 import Solution


@pytest.mark.parametrize("nums,target,expected", [
    ([], 1, 0),
    ([1, 2], 4, 5),
    ([1, 2, 3], 4, 7),
])
def test(nums, target, expected):
    solution = Solution()
    assert solution.combinationSum4(nums, target) == expected
