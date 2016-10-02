import pytest
from problems.split_array_max_sum import Solution


@pytest.mark.parametrize("nums, m, expected", [
    ([1,2,3,4,5], 2, 9),
    ([1,2,3,4,5], 3, 6),
    ([1,2147483647], 2, 2147483647),
    ([2,3,1,2,4,3], 5, 4),
])
def test_splitArray(nums, m, expected):
    assert Solution().splitArray(nums, m) == expected
