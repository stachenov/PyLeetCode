import pytest
from problems.median_2_sorted_arrays import Solution


@pytest.mark.parametrize("nums1,nums2,expected", [
    ([1], [], 1),
    ([1, 2], [], 1.5),
    ([], [1], 1),
    ([], [1, 2], 1.5),
    ([1, 2, 3], [1, 2, 3], 2),
    ([1, 2, 3], [4, 5], 3),
    ([1, 2], [3, 4, 5], 3),
    ([1, 2], [1, 2], 1.5),
    ([4], [1, 2, 3, 5, 6, 7], 4),
    ([4], [1, 2, 3, 5, 6, 7], 4),
    ([1, 2, 3, 4], [0], 2),
    ([1, 2, 3, 4], [9], 3),
    ([1, 2], [3, 4, 5, 6, 7], 4),
    ([1, 2, 3], [4, 5, 6, 7], 4),
    ([1, 2, 3, 4], [5, 6, 7], 4),
    ([1, 3], [2, 4, 5], 3),
    ([6], [1, 2, 3, 4, 5, 7], 4),
])
def test(nums1, nums2, expected):
    assert Solution().findMedianSortedArrays(nums1, nums2) == expected
