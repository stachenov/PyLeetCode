import pytest
from problems.search_for_range import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 9, [-1, -1]),
])
def test_searchRange(nums, target, expected):
    assert Solution().searchRange(nums, target) == expected
