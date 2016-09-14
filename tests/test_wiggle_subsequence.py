import pytest
from problems.wiggle_subsequence import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 7, 4, 9, 2, 5], 6),
    ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
])
def test(nums, expected):
    solution = Solution()
    assert solution.wiggleMaxLength(nums) == expected
