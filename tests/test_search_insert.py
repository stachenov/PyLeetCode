import pytest
from problems.search_insert import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
])
def test_searchInsert(nums, target, expected):
    assert Solution().searchInsert(nums, target) == expected
