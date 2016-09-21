import pytest
from problems.next_permutation import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4], [1, 2, 4, 3]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([2, 4, 3, 2, 1], [3, 1, 2, 2, 4]),
])
def test_nextPermutation(nums, expected):
    Solution().nextPermutation(nums)
    assert nums == expected
