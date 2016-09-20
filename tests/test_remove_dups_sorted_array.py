import pytest
from problems.remove_dups_sorted_array import Solution


@pytest.mark.parametrize("nums", [
    ([]),
    ([1]),
    ([1, 2]),
    ([1, 1]),
    ([1, 1, 2]),
])
def test_removeDuplicates(nums):
    l = Solution().removeDuplicates(nums)
    unique = sorted(list(set(nums)))
    assert l == len(unique)
    assert nums[:l] == unique
