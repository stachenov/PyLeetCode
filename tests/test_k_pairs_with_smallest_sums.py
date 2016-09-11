import pytest
from problems.k_pairs_with_smallest_sums import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("nums1,nums2,k,expected", [
    ([], [], 5, []),
    ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
    ([1, 1, 2],
     [1, 2, 3],
     10, [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]]),
])
def test(solution, nums1, nums2, k, expected):
    assert set((i[0], i[1]) for i in solution.kSmallestPairs(nums1, nums2, k))\
           == set((i[0], i[1]) for i in expected)
